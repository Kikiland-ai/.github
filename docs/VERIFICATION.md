# Profile and distribution verification

Run date: **19 October 2026**. These checks concern this documentation and extension distribution. They are separate from the historical cloud/provider acceptance receipts linked in [FEATURES.md](FEATURES.md).

| Check | Result |
| --- | --- |
| Python documentation/package validator | PASS: structured claims, relative Markdown targets, release-only manifest/config policy, archive CRC, size and every file's SHA-256. |
| Linked source targets | PASS: 68 GitHub source/document paths resolve to files/directories in the audited local checkouts. This is path validation, not a fresh network check of every URL. |
| Release rebuild | PASS: two consecutive upstream rebuilds produced the same 19,055-byte ZIP and SHA-256. |
| Focused upstream extension suite | PASS: 26 tests, zero skips, including actual kiki-web publisher, controller lifecycle, existing-tab startup, ordering/freshness and saved-model confirmation boundaries. |
| Python script syntax | PASS for the packager and validator. |
| Documented sample startup | PASS: `npm run dev` starts fixture mode and serves the React entry point at `127.0.0.1:5173`. No browser journey was inferred from this HTTP smoke check. |
| BB8 reference package/discovery checks | PASS in Design-Thinking; no native plugin registration/runtime activation claimed. |

Runtime: Node.js **24.19.0**, Python **3.12.14**. Audited source pins are in [evaluation.json](evaluation.json); exact package entries and hashes are in [extension-build.json](../downloads/extension-build.json).

The first extension test attempt stopped because fresh checkouts had no npm dependencies or generated reader bundle. After `npm ci` in kiki-web/apps/web and the upstream dependency-free reader build, the complete focused suite passed. No product source change was needed.

No Google sign-in, real learner write, MATLAB action, paid Gemini request, trial-budget change or cloud deployment was performed for this profile. The package's JavaScript behavior is covered by upstream source tests; a fresh native Chrome install/hosted lab acceptance was not performed here.

Reproduce with the focused commands in [SETUP.md](SETUP.md#useful-checks) and `python3 scripts/validate.py` in this repository.
