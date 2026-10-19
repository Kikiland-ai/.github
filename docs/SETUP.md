# Quick setup

## Fastest: use the hosted app

Open **https://kiki-512012.web.app**, sign in with Google and choose the Odia/English ECE teaching path. Add Analog Communication, open Learn and select a concept. No repository checkout or provider key is needed.

For the lab overlay, use desktop Chrome and the [prebuilt extension ZIP/install guide](EXTENSION.md). Bring your own MathWorks/Simulink Online access. Hosted AI screen-analysis capacity is currently exhausted; the project team must authorize more before additional live checks.

## Local sample: no credentials

Requirements: Git and **Node.js 24.12+**. From a new directory:

```sh
git clone https://github.com/Kikiland-ai/kiki-web.git
cd kiki-web/apps/web
npm ci
npm run dev
```

Open **http://127.0.0.1:5173** → **Open sample student** → finish setup with Odia/ECE → add Analog Communication. Explore lessons, models, checks and preparation. This development sample persists synthetic data only in this browser, with no Google sign-in or cloud synchronization. It does not run live Gemini screen analysis. Sample narration depends on the checkout's available fixture media; use the hosted app for published private narration.

If 5173 is occupied, `npm run dev -- --port 5176` uses another port. Fixture mode is development-only; `npm run build` is for configured connected output.

## Connected local app: Python API + React

Requirements: **Python 3.12**, **uv**, Node.js 24.12+, a Firebase project with Google sign-in, an authorized keyless Application Default Credentials identity, and access to the matching Firestore database and published teaching catalog. For the team's hosted project, request approved access from the team rather than copying credentials or importing the catalog again. The committed `.env.example` files retain historical project defaults: replace them with your intended configuration.

Terminal 1, starting in the `kiki-web` repository root:

```sh
cd apps/api
uv sync --locked --python 3.12
cp -n .env.example .env.local
# Edit .env.local with your approved configuration before starting.
uv run uvicorn kiki_api.main:app --factory --host 127.0.0.1 --port 8000 --no-access-log
```

Set `KIKI_FIREBASE_PROJECT_ID` and `KIKI_FIRESTORE_DATABASE` to the same approved project/database as the catalog. The hosted release uses project `kiki-512012` and named database `kiki-firedb`; identifiers alone do not grant access. `KIKI_MEDIA_BUCKET` is needed for private narration delivery. Keep lab execution disabled for this initial account/learning setup. Configure Google SDK credentials through normal ADC handling.

Terminal 2, starting in the repository root:

```sh
cd apps/web
npm ci
cp -n .env.example .env.development.local
# Set public Firebase web fields for the same project, API URL :8000,
# and remove VITE_AUTH_EMULATOR_URL when using real Google sign-in.
npm run check:connected
npm run dev:connected -- --port 5174
```

Open **http://127.0.0.1:5174**. Ensure localhost is an approved Firebase Auth domain and the API CORS list includes the exact origin. Keep provider keys and Admin credentials server-side; only public Firebase web configuration belongs in `VITE_*`. Connected mode has no silent sample fallback.

On PowerShell, use `Copy-Item` only if the destination env file does not already exist; the `cp -n` examples above are for a POSIX shell. Preserve existing local configuration.

Authoritative details: [team setup](https://github.com/Kikiland-ai/kiki-web/blob/main/TEAM_HANDOFF.md), [API configuration](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/config.py), [current cloud/frontend status](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/active.md).

## Local lab engine: optional advanced setup

The prebuilt release extension targets the hosted app. Local lab integration needs the upstream **dev** extension and a separate `kiki-backend` service; do not distribute that dev build to judges as the release.

```sh
git clone https://github.com/Kikiland-ai/kiki-backend.git
cd kiki-backend
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r prototypes/screen_capture/requirements.txt
node prototypes/floating_guidance/scripts/build-extension.mjs
```

Configure server-side `GEMINI_API_KEY`, `KIKI_PROXY_SECRET` (32+ characters) and `KIKI_REQUIRE_PROXY=1` through your local secret/runtime mechanism. Then:

```sh
python -B -m prototypes.backend --port 8100 --data-dir work/backend
```

In the **kiki-web API** configuration set `KIKI_LAB_EXECUTION_MODE=local`, `KIKI_LAB_BACKEND_ORIGIN=http://127.0.0.1:8100` and `KIKI_LAB_PROXY_SECRET` to the same server-only secret. Run one local API worker. Start connected web on **5174**, load `kiki-backend/work/floating-guidance/dev` through `chrome://extensions`, and start sharing from Lab mode. Live Gemini calls consume your configured provider quota; installing or testing the extension alone requires none.

More detail: [web lab integration](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/LAB_SCREEN_SHARE_IMPLEMENTATION.md), [backend lab handoff](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/handoffs/kiki-web-lab-mode-screen-share.md), [cross-machine testing](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/plans/connected-integration-testing.md).

## Useful checks

For this documentation/distribution repository:

```sh
python3 scripts/validate.py
```

In `kiki-web/apps/web`: `npm run lint`, `npm run typecheck`, `npm test`. In `kiki-web/apps/api`: `uv run pytest -q`. These are local automated checks, not evidence of a fresh real Google/Firestore/MATLAB session.

For the complete focused extension checks, first run `npm ci` in `kiki-web/apps/web` (the UI checks need its locked jsdom/TypeScript dependencies). In `kiki-backend`, build the reader and run from its directory for fixture resolution. Set `KIKI_WEB_CHECKOUT` to the absolute web checkout path to include the actual publisher regression:

```sh
cd prototypes/json_stream_site
node scripts/build.mjs
KIKI_WEB_CHECKOUT=/absolute/path/to/kiki-web node --test ../floating_guidance/tests/test-core.mjs ../floating_guidance/tests/test-controller-lifecycle.mjs ../floating_guidance/tests/test-confirmation-ui.mjs
```

For backend narration assets rather than the extension, install Git LFS and fetch the tracked WAV files separately. No Git LFS or audio download is needed to package/install the extension.
