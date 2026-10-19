# Shipped features and evidence

Reconciled **19 October 2026**, using the latest release/status records and targeted source inspection across the three repositories. “Shipped” describes the published capability; it does not imply a complete new live acceptance run or reviewed content quality. Source revisions and machine-readable status are in [evaluation.json](evaluation.json).

## Student-facing capabilities

| Capability | Shipped behavior | Source / evidence | Boundary |
| --- | --- | --- | --- |
| Accounts and onboarding | Google-only Firebase sign-in, server token verification, owned profiles, resumable setup and returning Home | [Web/API cloud release](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/active.md), [API identity](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/backend.py) | Self-reported confidence is not measured proficiency. |
| Personal preferences | Saved language, field, independent language-confidence ratings and five-level support setting | [Profile](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/profile/Profile.tsx), [preference contract](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/contracts/learning-preferences.ts) | Broader preferences do not imply available courses/translations. |
| Enrollment and navigation | Analog Communication enrollment with semester, subject overview, Home continuation, Learn, Checks, Library, Profile and Lab mode | [Router](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/app/App.tsx), [Home](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/home/Home.tsx) | Prepared catalog is ECE Analog Modulation. |
| Chapter and lessons | Ten concepts; four placards each; prerequisites/reference context and saved position | [Lesson renderer](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/LessonScreen.tsx), [learning backend](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/learning.py) | Reading does not pass a check. |
| Language dial and vocabulary | Odia-led → parallel Odia/English → English-led teaching; English technical chips and Odia glossary support | [Five-notch policy](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/language.ts), [term rendering](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/termSegments.ts) | Student controls the dial. Not every optional key-idea/title field has Odia. |
| Interactive models | Ten concept-specific scene kinds, keyboard sliders and Reset; native C-AM-08 phase recovery retained | [Canvas](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/CamCanvas.tsx), [phase scene](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/PhaseRecoveryScene.tsx) | Ideal teaching models; no simulator control or proficiency award. |
| Private narration | Ten media records and 26 original WAVs published; requested playback with pause, seek and speed controls | [Cloud publication record](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/active.md), [player](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/NarrationPlayer.tsx) | 22 Odia + 4 English; English only in C-AM-08. Review/alignment limits below. |
| Concept and chapter checks | Five-question concept checks, ten-question gated chapter test, language switching, saved drafts, server grading, feedback, retry and attempt history | [Assessment UI](https://github.com/Kikiland-ai/kiki-web/tree/main/apps/web/src/features/assessment), [grading](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/learning.py) | Concept pass 60%; chapter pass 80% after all ten concept passes. Retries reuse the authored bank. |
| Honest progress | Shared Home/chapter progress, saved lesson step/dial, owned assessment state and explicit retry on save errors | [Position saver](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/learning/placeSaver.ts), [progress](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/learning.py) | Term, English and practical proficiency remain unassessed. |
| Materials and Library | PDF/PPTX selectable-text extraction, up to five 10 MB documents, topic/date/note, Firestore text persistence and static upload-history cards | [Intake](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/intake/AddMaterial.tsx), [extraction](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/intake/text/extract.ts), [text backend](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/document_text.py) | No scanned-image OCR, generated lesson from upload or shipped original-file reader/download claim. Text extraction loses images/layout/equation formatting. |
| Lab preparation | DSB-SC aim, seven-concept readiness, 12 checkpoint reading positions, prediction/model-reference/observation notes, saved preparation and same-owner locator link | [Lab UI](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/labs/LabPreparation.tsx), [preparation backend](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/lab_preparation.py) | Readiness and saved notes do not verify execution. |
| Screen guidance | Lab-mode Share, authenticated capture transport, Gemini observation, streamed authoritative guidance, pause/resume/Stop and reconnect lifecycle | [Capture](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/labs/lab-capture.ts), [backend](https://github.com/Kikiland-ai/kiki-backend/tree/main/prototypes/lab_tracking), [hosted native trial](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/verification/hosted-trial-2026-10-18.md) | Five successful live checks; trial cap exhausted. Full 12-stage native acceptance pending. |
| Student confirmations | Own-words responses, explicit criterion confirmation, intended-condition declarations and stale-context draft handling | [Student input UI](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/src/features/labs/LabStudentInput.tsx) | Self-reports do not auto-verify MATLAB actions, save state or practical skill. |
| Floating Kiki extension | Release 0.1.3, explicit MATLAB tab binding, Now/Next and screen context, movable/dockable/minimized windows, control forwarding and sharing-off state | [Extension source](https://github.com/Kikiland-ai/kiki-backend/tree/main/prototypes/floating_guidance/extension), [upstream builder](https://github.com/Kikiland-ai/kiki-backend/blob/main/prototypes/floating_guidance/scripts/build-extension.mjs) | Chrome desktop; exact hosted origins; release ZIP contains no dev variant. |
| Responsive/recoverable UI | Engineering Sketchbook theme, phone/desktop layouts, native keyboard controls, reduced-motion handling and loading/save/leave/error recovery | [UI walkthrough](https://github.com/Kikiland-ai/kiki-web/blob/main/docs/ux/ui-slice-review.md), [current status](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/active.md) | Automated responsive checks do not establish every physical device/browser. |

## Backend and content capabilities

- **Deployed service separation:** Firebase Hosting serves the React app; Cloud Run serves the authenticated API and a private lab engine; Firestore stores owned state and private Cloud Storage serves narration. The [current backend plan](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/plans/active.md) supersedes the older backend README's “not hosted” text.
- **Capture lifecycle and isolation:** exact-origin checks, verified owners, single-use cloud tickets, capture redaction, committed versus tentative decisions, persistent create replay and guarded frame cleanup. See [web lab execution](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/api/src/kiki_api/lab_execution.py) and [cloud implementation](https://github.com/Kikiland-ai/kiki-backend/tree/main/deploy/cloud).
- **Bilingual text/speech tooling:** English source/glossary → Odia-led translation → refinement → speech-ready script → Gemini speech. Real provider recordings and preservation checks exist. This is a content-generation pipeline, not an on-demand student lesson compiler; generated content reaches kiki-web through the database. See [recorded evidence](https://github.com/Kikiland-ai/kiki-backend/blob/main/prototypes/mixed_script/evidence/2026-10-13/README.md) and [ADR 0011](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/decisions/0011-generated-content-reaches-kiki-web-through-the-database.md).
- **Concept library and publisher:** recovered ten-concept C-AM canvas packets, narration assets, SQLite library and a web publisher adapter. The original generator was lost before commit; do not claim it can be reproduced from this checkout. See [continuation record](https://github.com/Kikiland-ai/kiki-backend/blob/main/docs/handoffs/concept-canvas-continuation.md).
- **Product/design foundation:** reusable lesson-ledger types and validators, worked subject examples, feature journeys, component tokens and Kiki artwork in [Design-Thinking](https://github.com/Kikiland-ai/Design-Thinking). These are design/development assets, not extra shipped courses.

## Narration and model coverage

| Concept | Teaching model | Recordings |
| --- | --- | --- |
| C-AM-01 | Signal | 4 Odia placard clips |
| C-AM-02 | Communication flow | 4 Odia placard clips |
| C-AM-03 | AM | 4 Odia placard clips |
| C-AM-04 | DSB-SC | 1 Odia whole-concept clip |
| C-AM-05 | Spectrum | 1 Odia whole-concept clip |
| C-AM-06 | Receiver | 1 Odia whole-concept clip |
| C-AM-07 | Filter | 1 Odia whole-concept clip |
| C-AM-08 | Native phase recovery | 4 Odia + 4 English placard clips |
| C-AM-09 | FM | 1 Odia whole-concept clip |
| C-AM-10 | PM | 1 Odia whole-concept clip |

Six whole-concept recordings continue across manual placard changes without invented time offsets. C-AM-01/02/03/08 use per-placard clips. Earlier [all-ten integration evidence](https://github.com/Kikiland-ai/kiki-web/blob/main/docs/evidence/all-cam-coverage-2026-10-18.md) documents model/media coverage; its pre-deployment blockers are superseded by the newer [cloud release record](https://github.com/Kikiland-ai/kiki-web/blob/main/apps/web/active.md).

## Evidence and remaining limits

The source release record reports **259 web tests, 155 API passes with 2 opt-in skips**, deployed negative/CORS/transport checks, release-file hash verification and private media readback. The hosted native trial separately records **five real successful provider checks**, coherent Now/Next and Stop cleanup. These are existing project receipts, not tests rerun while writing this profile. The new package checks are listed in `downloads/extension-build.json` and reproducible locally.

- Native hosted trial completion remained **0/12**; no student answers or experiment actions were fabricated. Remaining stage progression and broader identity/lifecycle/device acceptance stay open.
- Scientific, native-Odia, pronunciation, spoken-fidelity and individual-recording listening review remain pending. No word/sentence timing alignment or exact numeric speech-WPM guarantee is shipped.
- C-AM-01 draws two traces although its brief describes three; C-AM-04's carrier is fixed at 2000 Hz; FM/PM are normalized teaching models. These visible limits are preserved.
- Reading, confidence settings, playback, model exploration, saved preparation and self-confirmations must not be described as independently assessed practical or English proficiency.
- Uploads save extracted text/history; scanned handwriting OCR, source-grounded automatic lesson compilation and cloud original-file retrieval are not advertised as complete.

## Designed, not shipped

Handwritten-answer photo marking with concept/English scores, targeted repair maps, voice viva / Teach Kiki, adaptive learner-graph curation, spaced-revision routing, teacher/class dashboards, general graphics/GIF generation and broader course/language libraries remain planned or experimental. Design-Thinking's original diode/rectifier demo is historical; today's released teaching pilot is **Analog Modulation / DSB-SC**.
