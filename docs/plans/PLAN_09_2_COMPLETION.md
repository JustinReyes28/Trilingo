# Plan 9.2 — Trilingo: Complete Outstanding Work from Phases 1–9

Status: **Partial**. The [2026-10-25 execution continuation](../PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25) updates source to **0.1.21** under a maximum-two-hour allowance and **18 check-review rounds**, including five extra checks and a final three-check/30-minute writing/grammar batch explicitly authorized within the original deadline. It provisionally exceeds both word-authoring targets and adds focused grammar/navigation work, including completed recall replay. Existing-dependency Node24 compatibility is verified; fresh independent setup, qualified review, actual providers/devices and full reconciliation remain open. Earlier [engineering verification](../PLAN_09_2_VERIFICATION.md) and [speaking/recall continuation](../PLAN_09_2_SPEAKING.md) retain their recorded scope. The full supplement is not complete.

For the current execution order, dependencies and completion evidence, use [the definitive remaining-work execution plan](REMAINING_WORK_EXECUTION_PLAN.md), created 2026-10-25. W0–W6 map to the A–I tasks here; W7–W11 cover the existing release/publication and later-curriculum scope. This is documentation-only and leaves the checklist's implementation status unchanged.

New agents can start with [the continuation guide](../AGENT_CONTINUATION_GUIDE.md). The user also requested [Windows EXE setup](WINDOWS_EXE_SETUP_PLAN.md) and a confirmed [standalone offline Android port](ANDROID_PORT_PLAN.md). Isolated platform feasibility may run alongside this supplement; it does not close qualified review/provider/device or shared data-safety gates. No installer/APK or renewed implementation allowance is implied by creating those plans.

Current user connectivity rule: cellular data; focused web search is permitted, but **every download/upload requires prior approval with estimated total network size and exact scope**, including dependencies, models, Git transfers and reviewer/release assets. The execution plan defines the bounded-transfer approval process. Historical no-browsing/no-download window records below remain historical; they do not override this latest instruction.

This is a completion supplement between Phase 9 and Phase 10, not a twelfth implementation phase. It addresses the remaining beginner Stages A-B work owned by Phases 1–9 while preserving the eleven-phase numbering, working features and original completion gates. The [master plan](../../AI_IMPLEMENTATION_PLAN.md), [AGENTS.md](../../AGENTS.md) and each owning phase remain authoritative.

The plan was created without resuming the earlier paused run. The user subsequently authorized the maximum-one-hour execution window recorded below. That window authorizes installed-resource work, not dependency/model downloads, provider replacement or unreviewed publication. Record unmet content-review, supported-setup, provider and device prerequisites honestly.

Project identity: **Trilingo** is the confirmed project/product name. Preserve it throughout the remaining Phase 1–9 work and the Phase 10/11 handoff, including visible app identity, documentation and release preparation. Use lowercase `trilingo` only where technical slugs or filename conventions require it; generic template names must not replace Trilingo.

## Goal and boundaries

Finish missing features, expand and review the full beginner inventory, verify actual Japanese audio/input, and reconcile evidence with every applicable Phase 1–9 checklist. Preserve Phase 2's completed shell scope and Phase 4's completed technical lesson-engine scope; extend and regression-test them only where this work requires it.

The full A-B target remains 92 basic kana plus taught patterns, 100 Stage A kanji plus 200 additional Stage B kanji, and 500 Stage A core words plus 1,500 additional Stage B core words. These are content targets, never memorization prerequisites or study limits. Later Stages C-F retain their own [curriculum release gates](../CURRICULUM_ROADMAP.md); their essay workshops and portfolios are outside this supplement's beginner completion claim.

Phase 10 still owns backup/restore, destructive reset controls, notification delivery, comprehensive security/performance and local-release approval. Phase 11 still owns open-source publication and promotion. This plan supplies their upstream feature/content evidence without marking either release complete.

## Starting evidence

Inspect the current source again at execution; these are planning baselines, not newly run application checks.

- Source `content/courses/ja/starter.json` is version **0.1.14**. Ten units exist, with two published technical-practice units, six published lessons and thirty published exercises. Eight core words and five separately counted expressions are published; publication does not establish independent qualified review.
- The source contains 286 core-word records plus five expressions, 92 basic kana, 135 separately counted variants/combinations/marks and 300 contextual kanji. Added character/word collections are draft; semantic word deduplication remains open. Raw records do not establish reviewed unique lexical coverage.
- Draft material includes seven writing tasks (four Stage A/three Stage B), six stroke templates, two stories, four passages, seven grammar notes, six dialogue scenarios, two audio episodes and three listening checks. Existing readers, writers and renderers must be reused.
- The [qualified review packet](../JAPANESE_CONTENT_REVIEW.md) identifies source **0.1.11**, while current source is 0.1.14. Refresh its content/hash before approving newer grammar/listening material. No qualified reviewer is currently available.
- The [latest implementation evidence](../PHASE_07_09_FOLLOWUP.md) records eleven migrations, 175 backend tests, 29 frontend tests, passing lint/typecheck/build, clean/populated migration checks, 72 responsive browser layouts and simulated recording checks. These historical results do not replace tests of the final Plan 9.2 source.
- Supported Node 24 LTS/fresh setup, physical IME/screen-reader/touch/stylus use, installed Kokoro/Japanese STT, human listening and qualified content review remain unverified. Audio fixtures are non-linguistic test tones.

## Execution order and evidence rules

1. **A — Baseline and setup:** identify gaps, isolate QA and verify supported setup when prerequisites permit.
2. **B — Inventory and review:** audit lexical identities and build the complete content/review queue before expansion in small validated batches.
3. **C, D and E — Reading, writing and grammar:** complete their feature/content gaps against B's inventory. **H — Review and records** can proceed against existing content/fixtures. **F — Provider discovery** may begin early without holding up unrelated work.
4. **G — Audio learning workflows:** complete real integration after F supplies working Japanese services; engineering may use explicitly labeled fixtures beforehand. Coordinate script/reading review with B/C/E.
5. **I — Combined verification:** run affected checks on the final candidate, complete manual checks and update only criteria supported by evidence.

Task IDs below are stable evidence references. All begin unchecked because they plan future implementation/verification. Inspect and reuse existing tests; an unchecked phase test does not prove behavior is absent. Do not duplicate working implementations.

When execution starts, create `docs/PLAN_09_2_VERIFICATION.md`. For each task record source/content version or hash, changed files, migration if any, exact command/result, manual operator/device/provider details, artifacts and limitations. Use pending, implemented, verified or awaiting a named prerequisite. Mock success, drafts and unavailable checks never become verified provider or qualified-review results.

## A — Baseline, supported setup and safe updates

Owns the remaining setup gate in [Phase 1](PHASE_01_FOUNDATION.md); supports every track.

- [x] **A1:** Reinspect README, all nine phase files, actual source/tests/contracts and latest evidence. Reconcile stale checklist wording with behavior; preserve historical evidence and identify necessary reruns. Record runtime/lockfile versions and starting source hash.
- [ ] **A2:** In a fresh isolated folder/environment, use Node 24 LTS and supported Python 3.11+ to follow documented dependency installation, migration, import and launch. Preserve lockfiles; record OS/runtime versions. If required runtime/cache files are missing, defer downloads until an appropriate authorized connection/work window instead of retrying on cellular data.
- [ ] **A3:** On a disposable QA database, verify empty-schema upgrade, repeatable import, API health, frontend connection, settings persistence and restart with AI/TTS/STT disabled. Check existing launcher port-conflict and missing-schema recovery.
- [x] **A4:** Separate all QA databases, caches, recordings, drafts and owned services from `.data/trilingo.db` and the personal launcher. Later schema changes require reviewed migrations plus clean and populated forward-upgrade tests preserving history/receipts. No resets, manual learner-DB edits or runtime table creation.

Evidence required: reproducible clean supported-runtime launch, relevant passing gates and persisted settings. F answers conditional Kokoro discovery; an unavailable optional provider does not block Phase 1's independent foundation gate.

## B — Complete the beginner inventory and qualified-review queue

Owns content work shared by [Phase 3](PHASE_03_CURRICULUM.md), [Phase 5](PHASE_05_READING.md), [Phase 6](PHASE_06_WRITING.md) and [Phase 7](PHASE_07_GRAMMAR_DIALOGUES.md).

- [ ] **B1:** Produce a versioned stage/unit/objective inventory separating authored/draft/reviewed/published counts. Map target words, kanji, patterns, passages, writing tasks, guides, dialogues and episodes to stable IDs and intended practice directions.
- [ ] **B2:** Audit semantic duplicates, alternate spellings, inflections and stage reuse, including 学校/がっこう. Define canonical lexical identities while preserving historical IDs/snapshots, collections, saved items and FSRS cards. Assess a migration if stored meanings change; never silently merge learner records. Count expressions separately.
- [ ] **B3:** Expand the eight outlined units into sufficient original lessons/subunits for all ten topics and 500 unique Stage A words plus 1,500 additional Stage B words. Every entry needs contextual reading/meaning, part of speech, concept/stage links and an original example. Objective checks need validated keys/alternatives, distractors, difficulty and useful explanations; duplicate cards and filler cannot satisfy coverage.
- [ ] **B4:** Regenerate the exact-source review packet, covering the published practice slice and changed/new models, alternatives, transcripts, pronunciation overrides, distractors, guides and assets. Preserve earlier packets. Capture reviewer identity/qualifications, source version/hash, date, corrections and decisions by stable ID; review strokes/audio in D/F/G.
- [ ] **B5:** Apply corrections in small versioned batches; validate, import twice into an isolated DB and prove attempts, assistance, XP, drafts, collections and review history survive. Publish only after linguistic, asset and executable-feature checks. Without a reviewer, finish independent authoring/engineering but retain draft/practice labels and open review/publication gates.
- [ ] **B6:** Reconcile source/API/UI/README/authoring inventories: 92 basic kana with taught patterns, 100+200 distinct contextual kanji and 500+1,500 semantically unique reviewed core words. Distinguish reviewed publication, introduced material, actual recall and practice completion. Raw counts or AI output never substitute for qualified review.

Evidence required: validated versioned inventories and review decisions matching exact published source. Phase 3's initial-slice gate stays distinct from full-inventory obligations in Phases 5/7 and Phase 10's final audit.

## C — Reviewed reading, stories and accessibility

Owns remaining [Phase 5](PHASE_05_READING.md) work; depends on B for reviewed publication.

- [ ] **C1:** Review/correct the 300 kanji contexts and kana-pattern instruction, including contextual readings, small kana, long vowels, voicing and combinations. Verify stage counts and useful word/reading checks; recognition cannot imply typing, handwriting or speaking mastery.
- [ ] **C2:** Review/publish at least two original interactive stories and beginner passages covering signs, menus, schedules and messages. Check taught language/difficulty, turn/checkpoint references, glossary, optional recap, skip/finish/resume/replay and durable assisted/skipped evidence. Reuse the story reader/session service.
- [ ] **C3:** Manually read kana, a contextual kanji word and a passage with ruby/romaji on/off; check unfamiliar aids, saved items, full-library search and Show more/all. Check hidden-answer leakage through payloads, DOM and accessible labels before/after explicit assistance.
- [ ] **C4:** With an actual screen reader and keyboard, inspect Japanese language metadata, ruby reading order, glyphs, wrapping, zoom and aid toggles at narrow mobile/desktop widths. Record browser/screen-reader/voice details and unavailable Japanese speech support; screenshots and DOM assertions alone cannot close this item.

Evidence required: reviewed published reading/stories, persistent honest evidence and resolved real assistive-technology findings for the tested scope. G adds verified listen-along while preserving text participation.

## D — Reviewed writing, stroke practice and physical Japanese input

Owns remaining [Phase 6](PHASE_06_WRITING.md) work; reuse existing drafts, conflicts, submissions and formation modes.

- [x] **D1:** Verify the Windows Japanese keyboard/IME guide against current official Microsoft documentation during execution. Record links, Windows version and date; correct the guide and exercise its input tester. Preserve the draft label until verified.
- [ ] **D2:** Review Stage A character/word/first-sentence tasks and at least three Stage B guided compositions, including models/alternatives, one annotated revision and self-review checklists. Open writing stays unassessed/self-reviewed; models are not exact-string keys.
- [ ] **D3:** Audit the six draft stroke assets, replacing/extending them as needed for a reviewed kana set and first taught kanji. Verify order, direction, start points, shape, source/version/license and attribution. Retain asset integrity checks and honest geometric tracing/self-check labels.
- [ ] **D4:** On physical Windows IME, type kana, convert a word to kanji, enter a constrained sentence and compose a guided paragraph. Check conversion Enter, composition-aware autosave, paste/focus, refresh/restart, failed saves and two-tab conflicts without text loss or duplicate submission XP.
- [ ] **D5:** Exercise mouse, real touch and stylus where available across trace/freehand modes: scaling/device-pixel ratio, start/direction cues, undo, substantial-unsaved clear/change confirmation, replay, optional sample retention/deletion and keyboard sequence alternative. Identify unavailable hardware and leave its coverage open.

Evidence required: reviewed beginner tasks/assets, physical input checks, durable drafts/revisions/conflicts and AI-disabled completion. No handwriting-recognition or C-F workshop claim follows.

## E — Full beginner grammar, explanations and dialogues

Owns remaining [Phase 7](PHASE_07_GRAMMAR_DIALOGUES.md) work; uses B's ten-unit coverage and G for voice.

- [ ] **E1:** Extend seven draft notes into reviewed unit guides/searchable concepts for all ten topics. Include English explanations, Japanese examples/readings, common mistakes, register/culture and scaffolded preparation. Preserve mistake/example links to targeted practice and durable bookmarks.
- [ ] **E2:** Review six scenarios and their branches/checkpoints, alternatives, hints and register expectations. Explain valid alternatives separately from understandable responses outside the task. Broaden answer-specific contrast explanations beyond the existing six particle checks.
- [ ] **E3:** Reuse/extend transition, resume, duplicate-event, content-update, bookmark/collection, search/filter and fallback regressions. Manually finish at least three authored scenarios with AI disabled, interrupt/resume one and revisit explanations.
- [ ] **E4:** Verify one real local explanation and coaching request with the loaded configured model. Record provider/model/version/endpoint and actual result. Reuse tests for disabled/unreachable/timeout/unloaded/incompatible/malformed/configuration-change cases. Generated text stays advisory, safely rendered and unable to mutate grades, XP, FSRS or publication.

Evidence required: reviewed ten-unit instruction and deterministic dialogues without AI. Track E4 separately: authored/fallback success cannot imply a real model was tested; unverified integration remains explicitly open here.

## F — Verify actual local Japanese providers

Owns conditional Phase 1 discovery and real-provider work in [Phase 8](PHASE_08_AUDIO_SPEAKING.md). Inspect existing adapter contracts/tests first.

- [ ] **F1:** When the existing Docker engine/service is reachable, identify Kokoro wrapper, image tag/digest, engine/model version, schema, host port, voices, Japanese dependencies, resource needs and license/output terms. Use narrow diagnostics; never infer capabilities from the VHDX or dump environment secrets. Docker remains optional for the core app.
- [ ] **F2:** Check the installed wrapper's Japanese language mapping/listed voice against current official/versioned documentation. Confirm tokenizer/dictionary/model/voice files and offline operation. Document the minimal missing setup and download/resources before installation; consider a substitute only if existing Kokoro cannot meet Phase 8's gate.
- [ ] **F3:** Run Phase 8's exact five-phrase synthesis set: kana, kanji, particles, numbers/counters and long-vowel/small-kana examples. Verify decoding, non-silence/duration, normal/slow playback, cache replay/invalidation. Record human listening against qualified contextual readings, including は/へ and counters; STT agreement is insufficient teaching-audio review.
- [ ] **F4:** Inspect available local Japanese STT options against current primary documentation, maintenance/license, language, formats, resource/retention requirements and endpoint. Select/pin the actual independent provider/model/version; adapt the existing contract only as needed. A compatible adapter is not a verified installed service.
- [ ] **F5:** Complete human microphone recording → local Japanese transcription → transcript feedback. Exercise permission denied, missing/busy device, unsupported format, silence/uncertainty, cancel/retry/delete. Distinguish real recording from fake-device tests, and transcript feedback from phoneme/pitch-accent assessment.

Evidence required: installed provider/configuration records, actual Japanese output, human listening and real microphone/STT results. If unavailable, classify the missing prerequisite accurately, leave Phase 8 partial and continue independent work. Never reset/mount/replace provider disks or delete learner data as a shortcut.

## G — Audio stories, rewarded speaking and voiced scenarios

Owns missing [Phase 8](PHASE_08_AUDIO_SPEAKING.md) workflows; depends on F for real integration and B/C/E for reviewed content.

- [ ] **G1:** Finish Kokoro-backed listen-along for reviewed stories and at least two reviewed mini episodes with comprehension checkpoints, optional transcript reveal, replay and slow playback. Separate displayed transcripts, pronunciation overrides and reference audio; label synthetic speech.
- [ ] **G2:** Verify existing focused listening selection/dictation/contrast with actual Japanese output. Preserve private cues, revision-safe delivery receipts, assisted text fallback, cancellation/concurrent-action recovery and normal XP. Audio preparation/delivery is not proof it was heard.
- [x] **G3:** Complete durable speaking-only practice through shared session/reward/activity services: authored objective, reference/replay/shadowing, recording, explicit STT feedback, retry/skip/finish and typed fallback. Define speech-attempt/transcript-match/fallback evidence in backend/public schemas without client correctness/mastery flags. Genuine new completed sessions earn normal practice XP; duplicate delivery and fallback switching cannot duplicate rewards.
- [ ] **G4:** Connect authored dialogues and optional bounded local coaching to voiced references/responses and explicit recording. Preserve text participation/generated-feedback labels. Verify a real voiced authored dialogue and optional AI scenario turn; do not turn coaching into an unbounded authoritative chatbot course.
- [x] **G5:** Extend capability-aware quests/per-skill records to completed audio workflows. Text-only fallback, skips, missing audio and unperformed speech cannot earn audio-specific credit. Preserve same-assignment fallback/definition history and previously credited source events.
- [ ] **G6:** Test invalid/oversized media, missing assets, incompatible voices/language, provider latency/failure, stale sessions, cache/config changes and transient recording handling. Document provider retention/deletion. Complete a core lesson with all provider gates disabled without losing work, access or normal XP.

Evidence required: reviewed audio content, real-provider end-to-end workflows, truthful durable records and fallbacks. Durable additions require reviewed migrations/historical receipt compatibility; never retain raw recordings by default or silently submit them to cloud services.

## H — Review directions, collections and historical records

Owns remaining [Phase 9](PHASE_09_REVIEW_PROGRESS.md) work; build on real FSRS, collections, quests, badges, calendar and recall timing.

- [x] **H1:** Reconcile objective/direction mappings for reading, meaning, typing, listening and speaking against supported content/providers. Reuse cards/logs and preserve scheduler state. Keep objective grades, self-rated FSRS, handwriting self-check, composition workflows, human review and AI provenance separate; schedule only suitable validated mappings through deliberate review actions.
- [ ] **H2:** Complete collection-scoped practice and applicable flashcard/typed/listening/speaking choices, with saved mistake/word/character/story navigation. Preserve immutable snapshots after content updates. Check empty/loading/error states, adjustable batches, further pages and Show more/all without due-review requirements or new-word caps.
- [x] **H3:** Extend recent-only timing to full historical browsing with stable pagination/filtering and reachable final page. Show mode, active/paused time, assistance/skips and self-rating labels. Hide/pause never expires study; invalid timing omits only the personal record while preserving learning/XP.
- [x] **H4:** Reconcile totals, accuracy, mistakes/reviews, published/reviewed coverage, workflow counts and skill/provenance labels with stored events. Check cold-start, incomplete/unassessed/later-stage states. Preserve optional calendar/reminder visibility; in-page reminders cannot claim OS delivery.
- [ ] **H5:** Reuse/extend deterministic FSRS tests for all ratings, learning/relearning, due order, early/repeated same-day review, browse/skip without scheduling, concurrency/stale revisions, rollback, content changes and restart. Preserve atomic rating/schedule/log/session/XP/quest/badge writes and original receipts.
- [ ] **H6:** Extend the existing 1,200-session fixture as needed for complete timing/collection/review histories, correct aggregates and bounded queries without N+1/truncated access. Verify uncapped genuine-session XP, free cosmetics and no duplicate quest/badge/fallback credit. Recheck first/consecutive/repeated/missed days, timezone boundaries/changes and DST; missing a goal/day removes no XP, work or access.
- [ ] **H7:** Manually review future-due material, request more words, skip review, open a later lesson, complete multiple new same-day sessions, select a cosmetic, hide optional goals/timing and restart. Confirm durable evidence and unrestricted choices.

Evidence required: preserved real FSRS state/logs, full accessible histories and honest skill evidence. XP, length, self-rating and transcripts cannot certify proficiency.

## I — Regression, rendered screens and phase reconciliation

Owns combined Phases 1–9 verification, preserving [Phase 2](PHASE_02_INTERFACE.md) and [Phase 4](PHASE_04_LESSON_ENGINE.md). This is the Phase 10 handoff, not release approval.

- [ ] **I1:** For changed UI, follow [the design brief](../DESIGN_BRIEF.md), [shared system](../../design-system/trilingo/MASTER.md), `ui-ux-pro-max`, `frontend-design` and rendered `design-skill` detect/audit guidance. Inspect 320/390/about 768px/desktop, keyboard/focus, Japanese composition/ruby/zoom, screen-reader order/labels, contrast, reduced motion, touch and essential actions. Record findings/screenshots and fix major issues; invocation/detector output alone is not a pass.
- [ ] **I2:** Verify loading/error/empty/draft/unpublished, available/current/complete/skipped/assisted, pending/saved/conflict, provider-offline and recovery states. A new learner can open every published activity and reveal/hint/retry/skip/pause/resume/finish/continue after mistakes. Optional assessments/goals/quests/badges/timers/cosmetics cannot add locks, quotas, countdown expiry or missed-day penalties.
- [x] **I3:** Run targeted tests after each coherent change, then complete relevant frontend/backend/content/migration/API gates on the final candidate. Extend existing tests only for meaningful uncovered behavior; never weaken/delete failures or bulk-check tasks merely because files exist.
- [ ] **I4:** Run applicable isolated browser scripts and the manual flow below with actual devices/providers. Synthetic IME/test-tone/fake-microphone evidence stays separate. Record unavailable hardware/review and leave required checks open.
- [ ] **I5:** Review the final diff against a preserved baseline for regressions, licenses, answer leakage, migration/backfill/receipt compatibility, bounded queries/provider work and private data. Update README, authoring/provider/setup docs, phase checklists and master milestones only for verified scope.
- [x] **I6:** Write a completion report with exact commands/results, source/schema/content versions, files, manual device/provider/reviewer evidence, unresolved items and Phase 10 handoff. Unproved required items retain partial status with a named prerequisite.

### Commands and isolated environments

These are execution instructions, not planning results. Follow [README](../../README.md) and [latest QA reproduction instructions](../PHASE_07_09_FOLLOWUP.md) for installed tooling and explicit QA origins. Scripts use different designated QA ports; never target a personal profile or assume one launcher serves them all.

From `frontend/`:

```powershell
npm run lint
npm run typecheck
npm run test -- --run
npm run build
```

From `backend/`:

```powershell
..\.venv\Scripts\python.exe -m pytest -q --basetemp=../.tools/pytest-plan-9-2 -o cache_dir=../.tools/pytest-cache-plan-9-2
..\.venv\Scripts\python.exe -m ruff check app migrations tests
..\.venv\Scripts\python.exe -m app.cli validate
```

Migration/import checks need a newly named disposable database and QA mode. Confirm the resolved path differs from personal data; the example URL resolves against the project root under existing configuration. Run from `backend/`:

```powershell
$env:QA_MODE='true'
$env:DATABASE_URL='sqlite:///.tools/plan-9-2-migration-check.db'
..\.venv\Scripts\python.exe -m alembic upgrade head
..\.venv\Scripts\python.exe -m alembic check
..\.venv\Scripts\python.exe -m app.cli import
..\.venv\Scripts\python.exe -m app.cli import
Remove-Item Env:DATABASE_URL
Remove-Item Env:QA_MODE
```

Also run populated forward-upgrade tests and API smoke for `/api/v1/health`, content reads and changed endpoints on the isolated running backend. Keep providers disabled for core tests, then use isolated provider preferences for real audio. Tones cannot prove Japanese output.

Reuse applicable `scripts/verify_ui.py`, `verify_study_ui.py`, `verify_reading_ui.py`, `verify_writing_ui.py`, `verify_phase789_ui.py`, `verify_listening_ui.py`, `verify_recall_timing_ui.py` and `verify_recording_ui.py`. Check each script's QA startup/guards, use the installed browser and stop only owned QA processes.

### Combined manual flow

1. From clean supported setup, create an isolated beginner profile, set timezone/aids and directly open a later published lesson without placement/earlier completion.
2. Make mistakes, retry/reveal/skip, pause/refresh/resume, finish/replay. Verify normal XP for every genuinely completed new session and no added XP for duplicate delivery.
3. Read reviewed kana/kanji text and a story with aids on/off and an actual screen reader. Save an item; keep assistance/recognition distinct from other skills.
4. Use physical IME, reviewed guided writing and mouse/touch/stylus formation where available. Preserve drafts/conflicts/revisions through restart and inspect honest sample/evidence labels.
5. Finish three scenarios with AI disabled. Separately verify optional real explanations/coaching, Japanese listen-along/two episodes, human microphone/STT, rewarded speaking and a voiced scenario.
6. Disable/unload providers mid-work; preserve input and typed/retry/skip/finish options. Verify same-assignment quest fallback without fabricated speech/duplicate rewards.
7. Early-review a future-due card, browse/skip another, expand batches, use collections/modes and browse final history pages. Restart and compare cards/logs/timing/XP/calendar/quests/badges/preferences.
8. Using isolated clocks, test missed goals/days, timezone/DST and free cosmetics. Preserve work/XP/access; elapsed-time displays never expire study.

## Completion checklist and Phase 10 handoff

- [ ] **Phase 1:** A proves supported fresh setup/settings; F records conditional provider discovery without making Docker mandatory for the core app.
- [ ] **Phase 2:** Preserve shell completion; I verifies actual new screens and resolves major design/accessibility findings in owning phases.
- [ ] **Phase 3:** B proves exact-source qualified review, narrative/writing contracts and repeatable imports preserving history. Technical practice cannot be relabeled independently reviewed without evidence.
- [ ] **Phase 4:** Preserve engine completion; I verifies renderer extensions retain authoritative grading, protected answers, unrestricted study, persistence and uncapped/idempotent rewards.
- [ ] **Phase 5:** B/C prove reviewed contextual inventory, two reviewed published stories, accurate aids, saved evidence and manual accessibility checks.
- [ ] **Phase 6:** B/D prove reviewed Stage A tasks, three Stage B compositions/models/revision/checklists, licensed reviewed stroke guidance, durable drafts and actual input/device checks. Unavailable hardware stays identified/unverified.
- [ ] **Phase 7:** B/E prove reviewed ten-unit guides/dialogues and authored/fallback operation without AI. Record real integration separately; generated advice cannot become authoritative evidence.
- [ ] **Phase 8:** F/G prove Japanese synthesis/listening, human microphone/local STT, story audio/two reviewed episodes, focused listening/speaking and voiced scenarios with honest fallbacks.
- [ ] **Phase 9:** H/I prove real FSRS, suitable separate directions/evidence, complete collections/modes/histories, truthful optional feedback and unrestricted study across failures/restart.
- [ ] **Plan 9.2:** Applicable A–I tasks/owning gates have evidence and exact-source claims agree across docs/API/UI. Required unverified items keep their phase and overall supplement partial; identify optional/unavailable integrations and hardware explicitly.

Proceed afterward to [Phase 10 — Reliability, Backup and Local Release](PHASE_10_RELEASE.md). Its backup/restore round trip, notifications, comprehensive release audits and acceptance remain required. [Phase 11](PHASE_11_OPEN_SOURCE_LAUNCH.md) remains a separate authorized public release/launch.

## Planning validation

Documentation-only validation on 2026-10-23:

- Local Node filesystem/source checks: PASS. All 75 local Markdown links across the new plan, master plan, README and Phase 9 resolve; fenced blocks are balanced; 47 task IDs are unique; all 57 new task/completion checkboxes remain unchecked. Exactly eleven numbered phase files remain (01–11).
- Preserved-baseline diff/checkbox comparison: PASS. Only the new supplement and three documentation links/handoff edits were made; existing master/Phase 9 implementation checkbox lines are unchanged. Current source confirms six published lessons/thirty exercises and version 0.1.14; the review packet still identifies 0.1.11 as recorded above.
- Independent reader review: PASS, no material gaps/contradictions found. Checked Phase 1–9 coverage, preserved Phase 2/4 scope, dependencies/external prerequisites, acceptance evidence, safe execution and separate Phase 10/11 ownership.
- Application tests/builds, migrations, real providers and rendered/device checks: NOT RUN for this documentation-only task. No learner data, application source or dependencies changed; no downloads or public publishing occurred. No implementation gate was closed.

## First execution window — 2026-10-23

Authorized maximum: one hour, 11:59:10–12:59:10 UTC (19:59:10–20:59:10 Singapore). [Evidence and per-task reconciliation](../PLAN_09_2_VERIFICATION.md) supersede the planning baseline for current implementation facts, while historical evidence above is preserved. Source is now 0.1.15/schema 0012. Current engineering gates pass; the completed checkboxes identify only their verified scope. All other tasks and the overall Phase 10 handoff remain open.

New independent work includes source-bound inventory/review tooling, eight draft lessons/24 checks, sixteen guides mapped to ten units, snapshot-preserving collection recall, complete timing histories and separate skill/workflow/coverage records. Qualified publication, full 500+1,500 lexical inventory, real audio/speaking and device checks remain unfinished.

## Speaking and audio-recall continuation — 2026-10-24

The user authorized up to two more hours (00:32:29–02:32:29 UTC), requested restrained review/testing and reiterated cellular-data limits. [Current evidence](../PLAN_09_2_SPEAKING.md) records source 0.1.16/schema 0013, the unchanged published slice, final 197 backend/31 frontend tests, required quality gates and 24 focused new responsive layouts. No downloads or web browsing occurred.

G3, G5 and H1 are checked for their verified engineering/draft scope: durable speaking practice, honest speaking quests/evidence and deliberate five-direction self-rated word recall. H2 now has listening/speaking collection choices and snapshot-preserving audio, but its broader saved-character/story navigation audit remains open. G4's controls are implemented; required real voiced/provider verification is still open. G6's media/stale/config/retention and provider-disabled core checks pass locally, while required real hardware/provider coverage remains open. All other unchecked tasks and the overall supplement remain partial; no qualified publication or Phase 10 handoff is claimed.

## Curriculum continuation — 2026-10-24

Authorized window: **09:25:12–10:25:12 UTC**, maximum one hour. User constraints: use installed/local resources on cellular data and avoid excessive tests or reviews. No dependency, model, browser, container or font downloads; no web browsing.

B3 authoring progressed with 838 original contextual rows, producing 833 new vocabulary records, 112 draft lessons and 1,363 objective checks across all ten topics. Exact current source is 0.1.20. The provisional lexical inventory is **541 Stage A +566 additional Stage B**; Stage A exceeds its raw 500-word target, while Stage B still needs **934** words against its separate 1,500-word target. These are unreviewed authoring counts, never published or mastered coverage. B3/B6 remain open.

B1/B2 now record lesson-exercise unit placement and twenty same-reading collision decisions, reuse きって/切手 and くつ/靴 IDs, retain the 学校/がっこう identity group, and conservatively count 皆さん/みんな once. No saved IDs or review cards were merged. B4 has an exact-source packet with **3,780 pending review items**; qualified review is still unavailable. B5 preserves historical attempts, assistance, drafts/session state, XP and FSRS receipts through isolated versioned imports; no new material was published.

[The run record](../PLAN_09_2_CURRICULUM.md) gives final commands/results, a small responsive saved-word flow, data safety and the concrete remaining work. Schema 0013 and all published lesson/vocabulary definitions remain unchanged. Provider/human/device/fresh-setup prerequisites and the rest of the checklist retain their prior status. Trilingo remains the confirmed project and release name in this handoff.

I6 reporting evidence: [the final bounded-run report](../PLAN_09_2_CURRICULUM.md) records source 0.1.20/schema 0013, exact check outcomes, changed files, eight local rendered layouts, preserved data, unavailable human/provider prerequisites and the Phase 10 handoff. This closes the report artifact only; the complete Plan 9.2 and all unproved gates remain partial.

## Remaining-work execution — 2026-10-25

The user authorized executing the definitive plan for at most two hours and ten check/review rounds, with cellular transfer approval preserved. Current source is **0.1.21/schema 0013**: **541 A +1,626 additional B provisional words**, 15 expressions, 92 basic kana and 300 contextual kanji. The 934-word Stage B authoring deficit is closed provisionally by 1,060 accepted candidates; 40 spelling/reading/する-family candidates are reported/omitted without merging saved IDs. B1/B2 semantic review and B4–B6 qualified review/corrections/publication remain open, with **6,848 pending review items**. Do not relabel raw target completion as reviewed publication.

E2 now has 24 additional draft particle contrasts with contextual feedback for every choice. H2 gains individual saved-character/word navigation, expandable visible batches, honest hidden-draft counts and collection/request-bound members/loading/failure/pagination, preventing old controls from acting on another collection. Existing histories/FSRS/services are reused; broader manual navigation/stories/provider/device audits remain open. No existing implementation checkbox is newly closed by these partial outputs. [The continuation record](../PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25) contains exact checks, corrected initial failures, data safety and remaining work.
