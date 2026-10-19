# Kikiland organisation profile

**[Open Kiki](https://kiki-512012.web.app)** · **[Watch the demo](https://youtu.be/bhakeLoJr0g)** · **[Read the unified README](profile/README.md)** · **[Agent guide](AGENTS.md)**

This repository is the public front door for Kiki. GitHub displays [`profile/README.md`](profile/README.md) on the [Kikiland-ai organisation page](https://github.com/Kikiland-ai).

- [Shipped features and evidence](docs/FEATURES.md)
- [Quick setup](docs/SETUP.md)
- [Extension download and installation](docs/EXTENSION.md)
- [Download Kiki windows 0.1.3](https://github.com/Kikiland-ai/.github/raw/refs/heads/main/downloads/kiki-windows-0.1.3.zip)
- [Machine-readable evaluation manifest](docs/evaluation.json)
- [Distribution verification](docs/VERIFICATION.md)

The profile reconciles Design-Thinking's product vision with the latest backend/web release records. Older repository READMEs retain historical status; this profile links the newer evidence directly.

## Maintain this profile

Keep human-facing capabilities, [`docs/FEATURES.md`](docs/FEATURES.md) and [`docs/evaluation.json`](docs/evaluation.json) consistent. Use source and release evidence before changing shipped status. No learner records, credentials, screenshots of private work or provider keys belong here.

Rebuild the extension from the exact backend revision in `downloads/extension-build.json`:

```sh
python3 scripts/package_extension.py --backend ../kiki-backend
python3 scripts/validate.py
```

The packaging script builds the upstream extension, archives only the release variant, verifies every entry and writes SHA-256/provenance files. The extension ZIP is served directly from this repository so judges need no build tools.
