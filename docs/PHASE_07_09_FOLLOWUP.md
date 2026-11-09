# Phases 7–9 — additional authorized hour

Date: 2026-10-23. Authorized window: 06:16:26–07:16:26 UTC (14:16:26–15:16:26 Singapore). This continues [the first-hour implementation](PHASE_07_09_VERIFICATION.md); the full phases remain partial. No dependencies, models, browsers, fonts, containers or images were downloaded. Small upstream documentation reads were used after the user allowed web search.

## Delivered scope

- Six draft particle guides link directly to scoped authored checks, with choice-specific contrast feedback. A private response-feedback field never enters public exercise payloads. The original published starter is unchanged.
- Optional scenario coaching retrieves the selected authored situation and objectives, bounds input/output, validates a strict structured reply, labels generated feedback unverified, and returns authored fallback for disabled/unreachable/timeout/malformed providers. It does not grade, award XP, publish content, change FSRS or save the transient conversation.
- Listening selection, dictation and audio contrast use the shared validated exercise union, renderer, authoritative grading and session rewards. Three original draft checks are linked to the two existing draft episodes. Focused listening remains directly selectable under the explicit draft toggle.
- Private audio cues separate displayed transcript, provider-only pronunciation override and language. Cache keys include all three, provider/model/voice configuration and speed. Both legacy string voice lists and current object-with-id lists are accepted; non-Japanese adapter requests fail honestly.
- Audio preparation records revision-safe, idempotent delivery receipts. Provider I/O occurs outside the SQLite write transaction; a concurrent action invalidates the pending delivery before evidence is written. Preparing audio is not proof of hearing it. Explicit text fallback, or an answer without all cues delivered, records assistance; grading, skips, corrections, finish and normal XP remain available.
- Optional listening quests require actual delivered-cue responses without text assistance/skips. An unfinished assignment can switch to core completed sessions under the same ID. Definition history preserves the previous predicate/source IDs; partial genuine listening credit remains once. Fallback awards no XP, and completed assignments cannot be credited again.
- Optional recall timers reuse persisted server active/pause intervals and shared controls. Opening/pausing/browsing/skipping changes neither FSRS nor XP. A deliberate self-rating commits the timer, scheduler transition, log, normal five XP and optional quest credit atomically. Duplicate rating delivery remains one event. Reopen a saved timer; hide it or pause indefinitely. Invalid timing is omitted while learning is preserved.
- Personal records show an accessible 12-week activity calendar, recent valid timed sessions with assistance/skips, and a persisted optional in-page reminder. No OS notification is claimed. Mode filters/direct links now include saved mistakes, words, kana, kanji and stories alongside existing writing, grammar, listening, speaking and recall choices.
- Fixed a real stale-load race that could replace a newly saved quest with an older initial fetch. Stale audio preparation exposes a session reload while retaining the entered answer. Preference controls show pending/optimistic transient state, preserve failure feedback and reload authoritative saved state.

## Data safety and migrations

Content source is 0.1.14. Six published lessons, thirty original published exercises, eight core words and five expressions remain unchanged. New grammar/audio content remains draft; no qualified publication is claimed.

- 0010 adds audio-delivery receipts containing authored cue/provider/result snapshots, never learner recordings.
- 0011 adds original quest kind, revision and definition history; backfill preserves existing quest kind, target, source IDs, baseline IDs and completion.
- Additive evidence/settings fields validate historical snapshots and immutable receipts without rewriting them. Timed recall reuses existing session JSON and ledger/log transactions.
- Clean schema upgrade and Alembic drift checks pass. Populated 0010 quest and prior 0001/0004/0005/0006 forward upgrades are covered by isolated tests. Historical session receipts without audio fields and existing word-card receipts remain valid.

All tests/QA used temporary or .tools databases. The learner database .data/trilingo.db was not migrated, imported, reset or edited. The personal launcher was not stopped. Restart it normally with scripts/start.ps1 to apply the additive migrations/import.

## Verification

Commands use the installed .venv/Scripts/python.exe from backend/ and installed node from frontend/ unless specified. No installation was needed.

- python -m pytest -q --basetemp=../.tools/pytest-second-ultimate -o cache_dir=../.tools/pytest-cache — PASS: 175 tests, one existing FastAPI/Starlette TestClient deprecation warning.
- python -m ruff check app migrations tests — PASS. New QA launch/fixture scripts also pass Ruff.
- python -m app.cli validate — PASS: source 0.1.14; unchanged published counts above.
- node node_modules/eslint/bin/eslint.js . — PASS.
- node node_modules/typescript/bin/tsc -b — PASS.
- node node_modules/vitest/vitest.mjs run — PASS: 29 tests in six files.
- node node_modules/vite/bin/vite.js build — PASS: 487.18 kB JS / 141.21 kB gzip; the existing two Lucide module-directive warnings remain, with no dependency changes to suppress them.
- python scripts/qa_phase789.py --fixture-audio — clean isolated migration upgrade/import and Alembic check PASS. The fixture serves non-linguistic test tones only.
- Installed Edge/Python Playwright: scripts/verify_phase789_ui.py checks 28 existing layouts; scripts/verify_listening_ui.py checks 36 added layouts; scripts/verify_recall_timing_ui.py checks eight recall layouts, all at 320/390/768/1280. Added flow checks include direct mode links, protected transcript, provider failure, synthetic IME events, text assistance, correction, repeated/new XP, native player controls, coaching fallback, quest definition change and preference persistence.
- scripts/verify_recording_ui.py verifies simulated-device capture/stop/cancel, local playback/download/delete, WAV conversion and disabled-STT fallback. It does not verify a human microphone or real Japanese STT.

Evidence is in artifacts/phase789 and artifacts/phase789-followup (screenshots, rendered HTML and JSON results); command logs are in .tools/phase789-second-runs. Physical IME and human screen-reader/touch/audio checks remain unverified.

## Rendered design audit

The direction remains Trilingo's existing Read/Operate workspace: teal/plum tokens, local fonts, Japanese examples first, asymmetric desktop columns and one mobile column. Actual screenshots were reviewed at narrow mobile and desktop. Listening controls were shortened with optional explanatory disclosure; repetitive guide pills became plain status metadata. The review fetch/preference interactions were fixed from actual browser failures rather than hidden by delays.

The design-skill detector ran against rendered HTML containing the injected styles. Its remaining repeated findings are the documented course-path dashed connector, navigation icon/heading proximity, compact status radii, unused Tailwind width/position utilities, and the standard screen-reader-only clipping/negative-margin rule. These are not observed accent rails, visible text clipping or horizontal overflow on the target screens. The initial repeated guide-badge warning was addressed. The calendar retains a text range and accessible full dates/activity; no activity is conveyed by color alone. The detector is not a zero-findings or accessibility certification; keyboard/overflow assertions and actual screen review are separate evidence.

## Reproduce isolated browser QA

Use three terminals from the repository root; these commands use existing installed dependencies only:

~~~powershell
# Terminal 1: explicit non-linguistic fixture, never a real Japanese provider
.\.venv\Scripts\python.exe scripts\qa_audio_fixture.py
# Terminal 2: always uses .tools/phase789-isolated.db and a separate cache
.\.venv\Scripts\python.exe scripts\qa_phase789.py --fixture-audio
# Terminal 3
cd frontend
$env:VITE_API_BASE_URL='http://127.0.0.1:8017/api/v1'
npm run dev -- --host 127.0.0.1 --port 5187 --strictPort
~~~

Then run the four browser scripts sequentially using the existing Python that has Playwright. The listening script explicitly configures only the disposable QA profile to localhost:18179/model qa-test-tone-v1. The backend launcher sets AI/STT disabled. The scripts refuse a non-QA backend; do not substitute a personal database. The fixture implements no transcription service. Stop these owned test processes afterward.

## Still open

Phase 7: full ten-unit authored/scaffolded coverage, qualified grammar/register review and publication, broader answer-specific explanations, a real local explanation/coaching call, and voice roleplay. The current scenario coach offers one bounded reply in the authored context, not an authoritative open-ended conversation course.

Phase 8: actual installed Kokoro engine/image/model/voice/dependencies/schema/license inspection, real Japanese five-phrase synthesis and human listening, reviewed episode publication, an independently chosen/pinned/verified local Japanese STT service, a real microphone-to-transcript round trip, rewarded speaking-only workflow and voiced AI scenario practice. Docker's engine pipe remained unavailable; no container or model was started/downloaded. Test tones and text fallback do not complete this gate.

Phase 9: broader objective per-skill evidence and scheduling where suitable content/providers exist, more complete collection/mode workflows, full historical timing browsing, and broader large-history/release audits. A bounded 1,200-session fixture now checks complete XP/calendar totals, access to the final history page, recent timing bounds and a bounded query count. Timed recall is explicitly self-report. Existing review directions, activity, streak, badge and reward tests pass, but no proficiency certification follows from them.

Supported Node LTS/fresh installs, physical devices/IME/screen-reader use and independent Japanese review remain unverified. The owning completion gates remain open. No new heart/energy, access lock, study quota, XP ceiling, countdown expiry, prerequisite pass requirement, paid/earned cosmetic, mandatory review queue or missed-day penalty was added.

## Changed areas and final review

Backend changes center on app/audio_learning.py, audio_models.py, providers.py, scenario_practice.py, learning.py, review.py, the request/public/content/settings schemas and migrations 0010_audio.py / 0011_quest_fallback.py. Frontend changes center on ListeningExercise.tsx, ScenarioPractice.tsx, the shared renderer/session, ReviewPage.tsx, GrammarPage.tsx and direct practice navigation. New regressions cover listening, quest fallback, scenario failures, populated audio/quest upgrades, recall timing and 1,200-record history. QA launch/fixture and listening/recall browser scripts are reproducible under scripts/.

Comparison to the preserved pre-continuation source confirms units, vocabulary, characters, writing tasks, concepts, assets and licenses are unchanged. Existing tests were extended for newly valid shared exercise types/references rather than weakened. Documentation links were checked locally. No commits or external publication were performed.

Final continuation handoff: approximately 2026-10-23 07:13:35 UTC, within the additional one-hour limit. The expanded backend suite passes 175 tests; frontend has 29 passing tests plus lint/typecheck/production build. The final sequential browser run passes 72 responsive layouts and simulated recording checks. A final targeted repeat also passes concurrent audio/reload recovery with the entered answer retained. Owned QA ports 5187/8017/18179 were stopped and return connection refused; cleanup evidence is recorded in artifacts/phase789-followup/cleanup.json. The broader phase goal remains paused and partial, with the open gates above preserved.
