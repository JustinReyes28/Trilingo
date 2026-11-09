Latest continuation: [additional authorized hour and current remaining work](PHASE_07_09_FOLLOWUP.md). The sections below preserve the first-hour evidence.

# Phases 7–9 bounded implementation — 2026-10-23

Status: substantial engineering implemented; all three full phase gates remain open. This is a technical practice build, not a reviewed Japanese/audio release.

## Session constraint and data use

The user authorized Phases 7, 8 and 9 with a maximum of one hour on cellular data. Work began at approximately 04:56:28 UTC (12:56:28 Singapore); the hard stop is 05:56:28 UTC (13:56:28 Singapore). No package, browser, font, model, voice, container or runtime downloads were performed. Existing Python/Node dependencies and the installed Edge executable were used. Small official provider documentation pages were read; browser QA blocked external requests.

The normal exec helper failed during setup. Commands were run through Node's child-process API with the same project working directory. Long jobs wrote durable output under ignored .tools/phase789-runs/; a timed-out observation was revalidated before restarting its finished test job. No external publication or messages were sent.

## Implemented behavior

### Grammar and dialogue

- Shared validated response_selection, dialogue_completion and constrained_roleplay exercise types use the existing renderer, authoritative grading, attempts, assistance, retry/skip, pause/resume, finish/replay and XP pipeline.
- Six original draft scenarios cover a first meeting, drink order, purchase, directions, routines and an invitation. Response-based branches are validated against permitted targets and checkpoint response IDs. Free navigation remains available and finishing honestly skips untouched checks.
- Seven structured draft grammar notes include six scoped particle guides: は/が/を/に/で/へ. Existing authored concept explanations are searchable too. English register notes and explicit alternatives stay in content, not page components.
- Grammar bookmarks, learner-selected scenario interests, practice focus and named vocabulary collections persist. Collection members retain immutable content references after a revision; bookmarking earns no XP.
- Optional local AI elaboration retrieves the authoritative session exercise after an answer or explicit reveal. Disabled/unavailable/timeout/malformed responses keep the authored explanation. Generated text is advisory and rendered as text; it cannot grade, schedule, award XP or publish content.

### Audio engineering

- Local-only Kokoro-compatible voices/synthesis adapter; installed Japanese jf_/jm_ voice validation; bounded, decoded 16-bit WAV validation; non-silent output check; disposable cache includes text, endpoint/provider/model/version/voice/settings/speed.
- User-triggered preparation, native play/replay, slow synthesis, cancellation, optional shadowing loop and text fallback. Existing stories/dialogues and two existing draft audio-episode scripts can be selected for per-turn audio.
- Microphone record/stop/cancel, local playback, delete, opt-in download, explicit local STT submission and transcript comparison. Browser recordings remain transient unless deliberately saved/sent. No cloud endpoint is accepted. Provider-side retention must be configured separately.
- Independent OpenAI-compatible local STT contract sends validated short WAV and language=ja. Transcript agreement is not phoneme, pronunciation or pitch-accent assessment. Failed/unavailable audio earns no fabricated listening/speaking evidence.
- Per-provider enable controls plus server environment gates remain off by default. Calls have a documented 10-second safety ceiling; core study is independent of AI/TTS/STT.

### Review and personal feedback

- Installed/pinned fsrs==6.3.2 performs actual backend scheduling with fuzzing disabled for reproducibility. Card state, parameters/version/retention, due dates and immutable before/after logs persist.
- Again/Hard/Good/Easy are explicitly self-reported ratings. Future-due cards and repeated new same-day reviews are allowed. Duplicate delivery returns the original receipt; stale/conflicting requests return recovery guidance.
- Published vocabulary has separate meaning, reading and typing cards. Saved mistakes can be imported as deduplicated historical exercise cards with their original skill direction. Import leaves new cards unscheduled, retains the mistake history, and earns no XP; browsing/skipping does not change a schedule.
- Each genuine committed rating completes a 5-XP practice session using the existing ledger/activity rules. No daily caps, due-only eligibility, prerequisite scores or cosmetic locks were added.
- Optional repeatable session/review/composition quests credit stable source-session IDs in the same transaction as completion/XP. Composition credit means workflow completion, not correctness. Audio-only quests are not offered without verified capability.
- Durable first-session/review/composition badges and editable monthly quest-target badges record actual source events, timestamps and criteria. Monthly awards use preserved profile-local activity dates. No badges or settings affect access.
- Free teal/plum accents; hideable quests/statistics; optional session elapsed time with server-recorded active intervals, pause/resume/hide and no expiry. A backwards clock invalidates timing only, preserving learning/XP.
- Practice mode filters and an overridable due/mistake/preference suggestion. Statistics aggregate real saved first-answer/assistance/skip evidence and self-rating directions separately; weekly XP compares only the learner's own history.

## Data and migrations

Four additive migrations extend the previous 0005 schema:

- 0006: FSRS cards/logs and optional quest assignments.
- 0007: timestamped personal badges, backfilled from real prior XP/session events.
- 0008: named vocabulary collections and immutable member references.
- 0009: distinguishes historical exercise cards from existing word cards; existing card state/due/revision is preserved.

Content source is 0.1.13. Existing six published lessons/thirty exercises/eight core words/five expressions remain the same published slice. The new six scenarios and seven notes remain draft; no new unit was published. Historical snapshots are retained.

Tests and browser checks used temporary databases under .tools/, never .data/trilingo.db. The learner database was not migrated, imported, reset or edited in this run. Normal startup applies additive migrations/import without deleting progress.

## Commands and evidence

Commands below use the existing .venv/Scripts/python.exe from backend/ and node from frontend/ unless stated otherwise. Final results are recorded after the last run; intermediate failures were fixed rather than hidden.

- python -m pytest -q --basetemp=../.tools/pytest-789-complete -o cache_dir=../.tools/pytest-cache — PASS, 151 tests, one dependency deprecation warning.
- python -m ruff check app migrations tests — PASS.
- python -m app.cli validate — PASS, version 0.1.13; six published lessons, thirty exercises, eight core words and five expressions.
- node node_modules/eslint/bin/eslint.js . — PASS.
- node node_modules/typescript/bin/tsc --noEmit — PASS.
- node node_modules/vitest/vitest.mjs --run — PASS, 27 tests in 5 files.
- node node_modules/vite/bin/vite.js build — PASS, local production bundle (473.92 kB JS / 137.92 kB gzip).
- Isolated Alembic upgrade head + check — PASS in QA startup; populated 0004/0005 forward-upgrade checks preserve study/profile/reading records. A populated 0006 card upgrade additionally checks unchanged state/due/revision and word identity.
- Existing Python Playwright: python scripts/verify_phase789_ui.py — PASS, 28 layouts at 320/390/768/1280, no page errors or external requests. Includes the final checkbox/prompt hierarchy changes and a published lesson with providers disabled.
- python scripts/verify_recording_ui.py — PASS using a browser fake media device: actual browser capture/stop/cancel, local blob playback URL, 16 kHz mono WAV conversion, explicit local download, delete and disabled-STT recovery. This is simulated-device evidence, not human microphone/transcription verification.
- Read-only docker -H npipe:////./pipe/dockerDesktopLinuxEngine ps -a --format ... — failed: pipe absent; Docker config read also reported access denied. No engine/container start or image pull was attempted.

Browser evidence: artifacts/phase789/results.json, viewport/full-page PNGs and rendered HTML. It covers grammar search/bookmark, three completed text scenarios, wrong-answer branching, pause/resume, timing controls, collection membership, mistake import without XP, two new early/repeat ratings, exact quest credit, accent restart persistence, disabled TTS, denied microphone recovery, two draft episode choices and keyboard skip-link operation. It does not prove physical IME, screen reader, real audio or actual pronunciation quality.

Intermediate findings: corrected the 0006 parent revision; updated a legacy migration fixture to seed an old schema directly instead of executing future services against missing tables; extended an exercise-type test helper; preserved historical import idempotency by comparing validated additive-default semantics without rewriting stored snapshots/digests; fixed concept search, batched historical review lookups, exact dropdown names, checkbox sizing/alignment and prompt hierarchy. Stable assignment IDs make repeated browser runs distinguish quests.

## Rendered design audit

Applied ui-ux-pro-max focused keyboard/React guidance, frontend-design and design-skill against actual screens. Direction: existing Trilingo product register, Read/Operate mode, Japanese examples as the focal content, quiet asymmetric desktop split and single mobile column; existing teal/plum tokens and local fonts, with no asset/font downloads or competing design system.

The detector ran on rendered HTML, not only the empty Vite entry. It reported one error and four warnings from shared stylesheet/nav patterns: the course path's dashed connector, a navigation icon preceding a heading, pill badge radius, an unused 1440px utility, and generic position utilities. These do not identify an accent rail or overflow in the new target screens. The existing documented playful path and compact status badges justify those shared shapes. Actual 320–1280 screenshots and overflow assertions found no horizontal overflow. Visual review fixed the real checkbox and recall hierarchy issues. A zero score from the empty entry was not accepted as evidence.

Physical IME, touch/stylus, screen-reader, human language/audio review and a supported Node LTS run remain unverified.

## Remaining phase requirements

Phase 7 remains partial: qualified Japanese/register review, full ten-unit beginner coverage/publication, more answer-specific contrast explanations, and optional generated scenario roleplay remain open. Real LM Studio explanation integration is unverified; contract/failure tests do not prove a loaded model.

Phase 8 remains partial: pronunciation-override metadata/cache invalidation, installed Kokoro wrapper/image/model/Japanese dependencies/voice/schema/license verification, the real five-phrase synthesis/listening set, independent maintained STT installation/version choice, real microphone round trip, reviewed audio episodes, graded listening/dictation/contrast exercises, focused rewarded audio sessions and voiced AI roleplay remain open. The text and recording workspaces do not complete the speaking release gate.

Phase 9 remains partial: separate mistakes/words/kana/story hub filters beyond the implemented category filters, a visual activity calendar and reminder visibility preferences, recorded recall-specific timing/personal timing comparisons, broader mode-specific assessed skill evidence, audio-quest definition-switch/fallback workflow once audio is verified, and further large-history/release audits remain open. Current clocks describe lesson sessions; self-rated review is not objective skill assessment. No proficiency meter is provided. Optional generated scenario roleplay, fully assessed audio practice and qualified publication are still separate requirements.

The phase checklists and master completion gates stay unchecked where these requirements are unmet. No release-ready, reviewed-content or real-provider claim is made.

## Changed implementation areas

Backend: review/collection/timing models and services, local provider/audio adapters, thin practice/audio routes, strict request/response schemas, shared exercise grading/content/session integration and migrations 0006–0009. Frontend: grammar, audio, recall, collections, practice choices, optional explanations/timer, shared renderer/schemas/navigation/settings and style refinements. Content: version 0.1.13 draft particle guides and six scenarios. Regression files cover FSRS/concurrency/idempotency/rollback, legacy upgrades, collections, media/provider failures and new renderer contracts; browser scripts are scripts/verify_phase789_ui.py and scripts/verify_recording_ui.py. No dependency lockfile or real learner progress was changed.

A supported-LTS runtime, fresh install, physical devices, independent language review and real local provider integration were not run. Their owning gates remain open. The existing FastAPI/Starlette TestClient deprecation warning and Lucide build directive warnings are recorded; dependencies were not downloaded or replaced to suppress them.

## Final handoff

The full backend run passed 151 tests. A final additional legacy-receipt API regression passed after making the new word-source field additive for old idempotency receipts; it verifies unchanged returned results and no duplicate XP. The existing TTS-cache contract test also passed after adding a file-size check before reading cached media. Ruff passes. No further full-suite claim is inferred from those targeted checks.

Deep comparison to the preserved initial source confirms units, vocabulary, characters, writing tasks, assets and licenses are unchanged; the additions are draft notes/scenarios/exercises and additive behavior. Eight changed documentation files have 54 resolving local links, and exactly eleven phase files remain. Owned QA servers were stopped; ports 8017 and 5187 refused connections afterward. The existing personal launcher was not stopped.

To use the new local features, stop the old personal launcher normally and restart scripts/start.ps1, which applies migrations/import without resetting progress. The remaining phase work is listed above; continuing it needs a new authorized work window. No automatic work is intended beyond the user’s one-hour limit.

Bounded work stopped at approximately 2026-10-23 05:56:01 UTC (about 59 minutes), within the requested one-hour maximum. The broader phase goal is paused, not marked complete.
