#!/usr/bin/env python3
"""Package the exact upstream release build; no provider or cloud calls."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = {"core.js", "ui.js", "content.js", "bridge.js", "background.js",
         "popup.html", "popup.js", "config.js", "manifest.json"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", type=Path, required=True)
    args = parser.parse_args()
    backend = args.backend.resolve()
    evaluation = json.loads((ROOT / "docs/evaluation.json").read_text())
    expected = evaluation["sources"]["backend"]["audited_commit"]
    actual = subprocess.check_output(["git", "-C", str(backend), "rev-parse", "HEAD"], text=True).strip()
    if actual != expected:
        raise SystemExit(f"Expected backend {expected}; checkout is {actual}")
    # Only tracked source changes matter; ignored work outputs are expected.
    changed = subprocess.check_output(["git", "-C", str(backend), "status", "--porcelain", "--untracked-files=no"], text=True)
    if changed.strip():
        raise SystemExit("Use a clean backend checkout to preserve source provenance")
    subprocess.run(["node", "prototypes/floating_guidance/scripts/build-extension.mjs"], cwd=backend, check=True)
    release = backend / "work/floating-guidance/release"
    if {p.name for p in release.iterdir()} != FILES:
        raise SystemExit("Unexpected release package membership")
    manifest = json.loads((release / "manifest.json").read_text())
    config = (release / "config.js").read_text()
    if '"dev":false' not in config or "localhost" in config or "127.0.0.1" in config:
        raise SystemExit("Refusing to distribute a dev extension")
    if manifest["version"] != evaluation["extension"]["version"]:
        raise SystemExit("Extension version and evaluation manifest disagree")
    destination = ROOT / "downloads" / f"kiki-windows-{manifest['version']}.zip"
    destination.parent.mkdir(exist_ok=True)
    entries = []
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(FILES):
            data = (release / name).read_bytes()
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 19, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compresslevel=9)
            entries.append({"path": name, "size_bytes": len(data), "sha256": sha(data)})
    checksum = sha(destination.read_bytes())
    provenance = {
        "schema": "kiki-extension-build/v1", "packaged_date": "2026-10-19",
        "variant": "release", "version": manifest["version"],
        "source_repository": "https://github.com/Kikiland-ai/kiki-backend",
        "source_commit": actual,
        "builder": "prototypes/floating_guidance/scripts/build-extension.mjs",
        "archive": destination.name, "archive_sha256": checksum,
        "archive_size_bytes": destination.stat().st_size,
        "manifest_version": manifest["manifest_version"],
        "minimum_chrome_version": manifest["minimum_chrome_version"],
        "permissions": manifest["permissions"], "host_permissions": manifest["host_permissions"],
        "reader_matches": manifest["content_scripts"][1]["matches"],
        "files": entries,
        "notes": "Unmodified upstream release files. Deterministic ZIP metadata; no dev files or credentials. Historical trial ZIP metadata/checksum may differ."
    }
    (destination.parent / "extension-build.json").write_text(json.dumps(provenance, indent=2) + "\n")
    (destination.parent / "SHA256SUMS").write_text(f"{checksum}  {destination.name}\n")
    print(f"Packaged {destination.name}: {len(entries)} upstream release files, {destination.stat().st_size} bytes; SHA-256 {checksum}")


if __name__ == "__main__":
    main()
