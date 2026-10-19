#!/usr/bin/env python3
"""Check documentation links, structured claims and extension release integrity."""
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    evaluation = json.loads((ROOT / "docs/evaluation.json").read_text())
    provenance = json.loads((ROOT / "downloads/extension-build.json").read_text())
    require(evaluation["schema"] == "kiki-evaluation/v1", "Unsupported evaluation schema")
    require(evaluation["app_url"] == "https://kiki-512012.web.app", "Wrong app URL")
    require(evaluation["demo_url"] == "https://youtu.be/bhakeLoJr0g", "Wrong demo URL")
    require(evaluation["extension"]["version"] == provenance["version"] == "0.1.3", "Wrong extension version")
    require(provenance["source_commit"] == evaluation["sources"]["backend"]["audited_commit"], "Source pin mismatch")
    require(evaluation["lab_trial"]["remaining_checks"] == 0, "Trial capacity must not be invented")
    require(evaluation["catalog"]["recordings_total"] == 26, "Recording count mismatch")
    require(evaluation["catalog"]["recordings_odia"] + evaluation["catalog"]["recordings_english"] == 26, "Language totals mismatch")
    require(len(evaluation["catalog"]["concepts"]) == 10, "Missing concepts")
    for capability in evaluation["capabilities"]:
        require(bool(capability["evidence"]), f"Missing evidence for {capability['id']}")
        require(capability["status"] in {"shipped", "shipped_capacity_exhausted", "content_tooling", "design_only"}, "Unknown status")

    local_links = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text()
        for raw in re.findall(r"\]\(([^)]+)\)", text):
            target = raw.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            require((path.parent / target).exists(), f"Broken local link: {path.relative_to(ROOT)} -> {target}")
            local_links += 1

    archive = ROOT / "downloads" / provenance["archive"]
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    require(digest == provenance["archive_sha256"], "Archive checksum mismatch")
    require(archive.stat().st_size == provenance["archive_size_bytes"], "Archive size mismatch")
    require((ROOT / "downloads/SHA256SUMS").read_text() == f"{digest}  {archive.name}\n", "SHA256SUMS mismatch")
    expected = {row["path"]: row for row in provenance["files"]}
    allowlist = {"core.js", "ui.js", "content.js", "bridge.js", "background.js", "popup.html", "popup.js", "config.js", "manifest.json"}
    require(set(expected) == allowlist, "Unexpected package files")
    with zipfile.ZipFile(archive) as bundle:
        require(bundle.testzip() is None, "ZIP CRC failure")
        require(set(bundle.namelist()) == allowlist and len(bundle.namelist()) == len(allowlist), "Unexpected or duplicate ZIP entries")
        for name, row in expected.items():
            data = bundle.read(name)
            require(len(data) == row["size_bytes"] and hashlib.sha256(data).hexdigest() == row["sha256"], f"Entry mismatch: {name}")
        config_text = bundle.read("config.js").decode()
        config = json.loads(config_text.removeprefix("globalThis.KIKI_FG_CONFIG=").strip().removesuffix(";"))
        manifest = json.loads(bundle.read("manifest.json"))
        require(config["dev"] is False, "Dev config in release")
        require(config["targets"] == ["https://matlab.mathworks.com"], "Wrong MATLAB target")
        require(evaluation["app_url"] in config["readers"], "Hosted Kiki reader absent")
        require(not any("localhost" in origin or "127.0.0.1" in origin for origin in config["readers"]), "Local origins in release")
        require(manifest["manifest_version"] == 3 and manifest["version"] == provenance["version"], "Manifest mismatch")
        require(manifest["name"] == "Kiki windows", "Wrong extension name")
        require(set(manifest["permissions"]) == {"storage", "scripting"}, "Unexpected permissions")
        require(manifest["host_permissions"] == ["https://matlab.mathworks.com/*"], "Unexpected host permissions")
        require(manifest["content_scripts"][1]["matches"] == [origin + "/*" for origin in config["readers"]], "Reader config mismatch")
        for group in manifest["content_scripts"]:
            for name in group["js"]:
                require(name in allowlist, f"Missing referenced script: {name}")
        require(manifest["background"]["service_worker"] in allowlist, "Missing service worker")
        require(manifest["action"]["default_popup"] in allowlist, "Missing popup")
    print(f"PASS: evaluation claims, {local_links} local Markdown links, release policy and all {len(expected)} ZIP entry hashes/CRC; SHA-256 {digest}")


if __name__ == "__main__":
    main()
