# Kiki: an entry point for agents

Use this file to evaluate or navigate Kiki without mistaking product aspirations for shipped behavior. The human version is [`profile/README.md`](profile/README.md); structured facts are in [`docs/evaluation.json`](docs/evaluation.json).

## Read in this order

1. `docs/evaluation.json`: URLs, source pins, capabilities, commands and limits.
2. `docs/FEATURES.md`: feature-to-evidence map and status reconciliation.
3. `docs/SETUP.md`: hosted entry point and credential-free local sample.
4. `docs/EXTENSION.md` and `downloads/extension-build.json`: installation, provenance and capacity limits.
5. Relevant source files in the linked repositories, reading their applicable `AGENTS.md` first.

The three sources have different jobs: Design-Thinking supplies intent/design; kiki-web supplies the app/API; kiki-backend supplies lab/content tooling. Prefer the latest dated release/active record over older status text in a README. Use inspected code for implementation detail and recorded live evidence for claims about deployed behavior. This profile audits selected relevant files; it does not claim every file was loaded or indexed.

## Evaluation contract

- Treat hosted availability, source implementation, automated tests, native live trials and content review as separate facts.
- The prepared pilot is Odia/English ECE Analog Modulation, ten concepts. Profile flexibility does not imply other prepared languages/subjects.
- Narration: 26 clips, 22 Odia + 4 English; English only in C-AM-08. Content review is pending; no sentence alignment exists.
- Concepts are server-scored through MCQs. Confidence ratings, reading, audio, diagrams and lab notes do not establish vocabulary, academic-English or practical mastery.
- The first hosted lab trial verified startup, five real screen checks and Stop. It ended at 0/12 completed stages and exhausted its shared five-check allowance. Do not claim a new session renews capacity.
- The extension ZIP is an upstream **release** build, not a mock or dev variant. Its manifest and byte hashes are inspectable without running MATLAB or calling Gemini.
- Source test totals in the release records are historical receipts. Report only commands you actually run as your own validation.

## Safe, reproducible entry points

```sh
# In this repository: links, evidence manifest, package membership/hashes and release policy
python3 scripts/validate.py

# In a fresh kiki-web checkout: local, explicitly synthetic browser sample
cd apps/web
npm ci
npm run dev
```

For source investigation, start with `apps/web/src/app/App.tsx`, learning/labs/assessment feature folders and `apps/api/src/kiki_api/` in kiki-web; `prototypes/lab_tracking/`, `prototypes/floating_guidance/` and the concept-library publisher in kiki-backend. This is a navigation map, not a claim of fresh execution.

Read-only evaluation needs no provider key, no learner-record export and no real student answers. Do not reset learner progress, submit answers for someone, share a screen, call paid providers, change the exhausted trial budget, import a catalog or alter cloud configuration just to evaluate this repository. Those actions require an explicit scoped user instruction. Use labelled sample mode for synthetic journeys.

## Updating this repository

Keep the human guide, feature inventory and evaluation manifest consistent. Pin audited source revisions; preserve distinction between source HEAD and deployed revision. Build extension packages using `scripts/package_extension.py` from the exact recorded backend commit and validate with `scripts/validate.py`. Never include the dev package, credentials, learner records or captured frames.

For requested commits use `arpanvihan5-sketch` and `317357476+arpanvihan5-sketch@users.noreply.github.com`; verify author/committer and authenticated GitHub identity before publication. Publish or change external systems only within the user's instruction.
