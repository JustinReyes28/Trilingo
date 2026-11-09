# Phases 1-3 verification — 2026-10-23

This record covers Phases 1-3. Subsequent playable-lesson work and current quality counts are recorded in [Phase 4 verification](PHASE_04_VERIFICATION.md).

## Scope and honest status
Implemented the native local foundation, interface/design system, and initial curriculum/content API slice. Phase 2's interface gate is verified for its declared shell/fixture scope. Phase 1 remains partial pending a complete fresh frontend installation on the supported Node 24 LTS target. Phase 3 remains partial pending independent qualified Japanese review of the starter answer keys/models. Existing internal checks and explicit technical-practice labeling do not constitute qualified review.

No production lessons, XP/streaks, review scheduler, handwriting, speech recognition, or AI adapter are claimed. Phase 4 onward stays open. No personal learning database/progress was reset. The default personal .data/trilingo.db was not used by tests; temporary pytest DBs and explicit QA DBs were used.

## Files and architecture
- frontend/: strict React/TypeScript/Vite/Tailwind/Zod application, local API client, course browsing, library/search, persistent preferences, native accessible dialog, shared controls and development previews.
- backend/: FastAPI typed public schemas, SQLAlchemy models, settings/content/assistance services, CLI validation/import, JSON input bounds, isolated tests and Alembic migrations 0001/0002 plus revision template.
- content/courses/ja/starter.json: original versioned practice slice, 10-unit outline, A-F stage metadata, beginner writing models/checklists and draft extension examples.
- scripts/: native PowerShell launcher, local-only browser checks and QA safety guard.
- design-system/trilingo/MASTER.md, TECHNICAL_DECISIONS.md and CONTENT_AUTHORING.md record the actual decisions and contracts.

## Data and inventory
Migration 0001 creates profiles/preferences;0002 creates courses/immutable course versions/enrollment/assistance. Empty migration, populated0001->0002 upgrade, drift checks and future revision generation are tested. Import is idempotent and preserves old snapshots and recorded assistance/enrollment. Attempt/completion tables do not exist before Phase 4, so their future retention test remains a carryover.

Current technical inventory:2 published units, 6 lessons, 30 objective exercise definitions, 5 discriminated types, 8 core lexical entries, 5 separately counted expressions, 0 contextual kanji inventory entries. Eight remaining beginner unit outlines, one character entry, one grammar guide, one story, two script-only audio episodes, one recap example and six writing references remain draft. Writing references cover Stage A character/word/first-sentence production and three Stage B compositions with models/checklists and an annotated revision. A-F stage targets are metadata, never access rules or proficiency claims.

The guide/content review was internal: conventional greetings, polite/casual distinctions, kana size/voicing/length, token IDs, matching maps and authored alternatives were checked. Independent qualified review is pending. The [review packet](JAPANESE_CONTENT_REVIEW.md) assembles the exact version 0.1.4 keys, models and scripts; the user confirmed no reviewer is available yet. Keep draft/practice labels and the review gate open. Assets/text are original; declared content license records are preserved. No model/audio/font/browser asset download was performed after the metered tooling allowance was exhausted.

## Commands and evidence
Commands below were run against this working tree. Historical Phases 1-3 backend count:45; frontend count:10. Frontend/browser evidence below comes from the preceding implementation run; this content-only continuation did not change frontend code. Re-run scripts when changing code.

- npm run lint — PASS.
- npm run typecheck — PASS.
- npm run test -- --run — PASS (10 API/schema/configuration tests).
- npm run build — PASS. Lucide's module-level use-client directive produces a bundler warning; the standalone client build succeeds.
- npm ci --dry-run --offline --ignore-scripts --no-audit --no-fund — PASS after completing exact manifest/lock metadata locally. This is a dry run, not a completed fresh installation.
- npm ls --all --offline --json — checked for dependency-graph consistency; PASS with no dependency-graph problems after removing an unused OXC extraction.
- python -m pytest -q — PASS:45 tests on isolated migrated databases.
- python -m ruff check app migrations tests — PASS after formatting.
- python -m pip check — PASS.
- python -m app.cli validate — PASS.
- python -m alembic upgrade head; python -m alembic check — PASS on explicit QA DB; no schema drift.
- python -m app.cli import — first import succeeds; repeat returns imported_new_version=false.
- scripts/start.ps1 -SkipOpen — PASS on isolated Windows QA DB; frontend/health reach ready state; stopping the launcher stops its owned services.
- Invoke-RestMethod http://127.0.0.1:8002/api/v1/health — PASS: schema 0002, QA mode true, unimplemented lesson/AI/TTS/STT capabilities false.
- python scripts/verify_ui.py — PASS with the already installed Playwright browser. All non-loopback requests are blocked; no external requests or page errors were observed.
- docker ps -a --format ... — UNAVAILABLE: Docker Linux engine pipe absent. No containers/images/settings changed; Phase 8 verification remains open.

Python executable used: .venv/Scripts/python.exe (3.14.0); browser script used the already installed system Python Playwright. Node 25.2.1 is the existing local executable. Node 24 LTS is the supported target; no completed LTS runtime test or complete fresh frontend install is claimed. A local cache audit found 151 Windows-compatible lock entries lacking archives (including mandatory TypeScript), so the current cache cannot support a full offline clean install. This continuation downloaded zero bytes.

## Content-only continuation — 2026-10-23

- Version 0.1.4 adds two draft audio-episode scripts and two draft Stage A character/word tasks. Published unit/lesson/exercise definitions and vocabulary are unchanged as parsed JSON compared to version 0.1.3. No audio assets, migrations, dependencies or frontend code changed.
- `python -m app.cli validate` — PASS for version 0.1.4.
- `python -m pytest -q tests/test_content.py` — PASS:22 tests.
- `python -m pytest -q` — PASS:45 tests; one existing Starlette/httpx deprecation warning.
- `python -m ruff check app migrations tests` — PASS after wrapping the new assertion.
- Source SHA-256 is recorded in the packet; linguistic approval remains pending. No personal database was imported or mutated.

## Rendered and interaction audit
Screenshots are local ignored QA artifacts, not invented mockups: artifacts/screenshots/{learn, practice, library, profile, preview}-{320,390,768,1440}.png. Additional loading/error and 200%-text screenshots, plus artifacts/ui-results.json, are generated by the QA script.

Verified:
- All five surfaces at 320/390/768/1440; no horizontal overflow.
- Shared native dialog focus wrapping, Escape, and restoration; visible focus and 44px target sizes.
- Skip-to-content preserves the current destination and focuses main.
- Direct later-lesson outline access without enrollment/history; upcoming study controls are explicitly disabled.
- Saved name/timezone/preferences survive reload/restart. Invalid timezone and network errors preserve unsaved input and retry works.
- Real loading/connection-retry/empty-course states; vocabulary search/empty results; an isolated real React error-boundary rendering failure and recoverable fallback.
- Fixture selected/pending/correct/incorrect/assisted/skipped states, continuation/finish/replay, pause/resume, and cancellation of obsolete delayed feedback.
- Japanese text/ruby wrapping, simulated IME composition guards, multi-line input preservation, long recovery messages and 200% text at 320px.
- Optional assessment/filter/cosmetic/timer fixtures remain labeled; elapsed time pauses/hides and never expires an activity.
- Reduced-motion settings change the actual root mode; color is accompanied by textual feedback/icons.

Independent design-skill Standards/Spec audit subagents were used as its audit workflow requires. Baseline findings and resolutions are in .design-skill/audit-report.md. Standards final recheck scored24/24 for inspected surfaces. This does not certify all accessibility or later feature behavior.

Observed defects fixed: skip link routed to Learn; mobile icon/close/footer targets undersized; excessive heading/punctuation tracking; preview coverage gaps; stale pending feedback overwrote later states; native dialog Tab could move outside;200%-text overflow; core word count included fixed phrases; outdated DB health could report ready; retrying assistance after a content update returned a conflict instead of the original snapshot.

Contrast measured from actual rendered colors: muted/paper6.68:1, muted/mint6.13, muted/plum6.24, path/white7.13, focus/white7.78, error/error surface7.90.

## Open gates and limits
- Full fresh frontend dependency installation on supported Node 24 LTS, deferred under the cellular cap. Existing cached/local installation, lock dry run, build and browser tests are verified separately.
- Independent qualified Japanese-language review before treating the starter answer keys/models as reviewed course material. Current content is clearly labeled technical practice.
- Physical Windows IME and a screen-reader session were not performed. Automated composition events/semantic controls are evidence for narrower behavior only; repeat in owning writing/reading phases.
- No real Kokoro/STT/AI provider call was made. Core browsing/settings work with all disabled. Docker absence does not block Phase 1's independent work.
- Real lesson attempt/completion retention, progression and all later language-skill claims remain Phase 4+ work.

The master and phase checklists mark only verified work. These open gates keep the overall execute-Phases 1-3 goal incomplete.
