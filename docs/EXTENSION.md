# Put Kiki beside your MATLAB model

**[Download Kiki windows 0.1.3 for Chrome](https://github.com/Kikiland-ai/.github/raw/refs/heads/main/downloads/kiki-windows-0.1.3.zip)** · [SHA-256](../downloads/SHA256SUMS) · [Build provenance](../downloads/extension-build.json)

This is the **release** build from `kiki-backend`, packaged for the hosted Kiki app. It is an unpacked Chrome Manifest V3 extension, not a Chrome Web Store installation. No Node, Python, backend checkout or API key is needed to install it.

## Install in desktop Chrome

1. Download the ZIP above and **extract it** into a permanent folder.
2. Open **`chrome://extensions`** in Chrome **116 or later**.
3. Turn on **Developer mode** in the top-right corner.
4. Choose **Load unpacked**, then select the extracted folder that directly contains **`manifest.json`**. Do not select the ZIP itself.
5. Verify **Kiki windows · 0.1.3** appears and enable it. Pin Kiki through Chrome's Extensions menu if useful.

Keep the extracted folder in place while the extension is installed. To update, extract the new version into its own folder, remove the old installation and load the new folder. To uninstall, choose **Remove** on `chrome://extensions`.

## Use it with Kiki

1. Open **[Kiki](https://kiki-512012.web.app)**, sign in with Google, select the prepared Odia/English ECE path and add Analog Communication.
2. Open **Lab mode** and start or resume your **DSB-SC lab preparation**.
3. Open **[MATLAB Online](https://matlab.mathworks.com)** in another tab, using your own MathWorks account with Simulink access. Save your actual model in MathWorks.
4. While on the MATLAB tab, open the Kiki extension popup and choose **Show Kiki on this tab**. The floating windows should become visible.
5. Return to Kiki Lab mode and choose **Share your MATLAB tab**. In Chrome's picker, choose that same **Chrome tab** and explicitly share it.
6. Follow **Now / Next** in MATLAB. Move, split, dock or minimize the windows as needed. Pause/resume through the tracker or floating controls. Enter your own observations and confirmations in Kiki; the extension never answers for you.
7. Use **Stop sharing** when finished. After a reload, disconnected tab or sign-out, start again with an explicit Share gesture.

**Current hosted limit:** the documented first live trial exhausted its five AI screen checks. Installation does not grant a fresh allowance. Further hosted analysis requires the project team's approval and capacity; an unchanged quota may leave the tracker waiting/unavailable. The [demo video](https://youtu.be/bhakeLoJr0g) and [hosted trial evidence](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/verification/hosted-trial-2026-10-18.md) show the verified interaction. Reading lessons and saving preparation do not require a new live-analysis allowance.

## If the windows do not appear

- Check the extension is enabled and that you selected the extracted folder containing `manifest.json`.
- Use `https://matlab.mathworks.com`; desktop MATLAB and other web origins are outside this release's target.
- Reload the MATLAB tab, then click **Show Kiki on this tab** again. Refresh Kiki after installing the extension so its bridge can load.
- Choose the bound MATLAB **tab**, rather than your entire desktop or another tab, in the sharing picker.
- If guidance reports a missing connection, stale window position or sharing off, reconnect through Kiki. Reinstalling the extension does not reset server capacity.
- Managed school/work Chrome policies may restrict Developer mode; use a browser/device on which unpacked extensions are allowed.

## Permissions and behavior

The generated manifest requests `storage` and `scripting`, with host permission limited to `https://matlab.mathworks.com/*`. Reader bridges match the exact hosted Kiki origin plus two existing backend QA reader origins. No localhost reader, capture canary or open test shadow root is shipped in this release. See the exact generated manifest inside the ZIP.

Showing the windows binds your chosen MATLAB tab; it does not itself start screen capture. Capture starts only through the student's Share action in Kiki. Kiki masks its own floating windows in frames before analysis. The tracker remains authoritative: visible guidance and saved notes do not prove experiment completion, external model saving or assessed practical proficiency.

The archive contains the upstream release files unchanged. Its checksum differs from any earlier distribution if ZIP metadata differs; validate this distribution against the adjacent `SHA256SUMS`, not the historical trial archive checksum. [Rebuild instructions](../README.md#maintain-this-profile).
