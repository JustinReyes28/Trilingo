# Phase 4 verification — 2026-10-23

Implemented and verified for the existing technical-practice starter slice. Qualified Japanese review and the supported-Node clean-install gate remain open. Phase 5 reading and Phase 6 writing are the active next work; this record does not claim those features or a reviewed beginner release.

## Changes and files

- backend/app/learning_models.py, learning_schemas.py, grading.py, learning.py and learning_api.py: immutable session snapshots, server-issued next-action IDs, saved action receipts, transactional answers/assistance/skips/continuation/pause/finish, corrections retaining original evidence, voluntary mistakes, XP ledger, timezone activity and descriptive streaks. Public session data protects private keys until submission or deliberate assistance.
- backend/app/main.py, services.py and public_schemas.py: thin study routes, actual lesson capability, live course-path states and validated responses.
- frontend/src/ExerciseRenderer.tsx, ExerciseSession.tsx, StudyHub.tsx, studyApi.ts and studySchemas.ts: five dedicated exercise controls, stable token identities, keyboard alternatives, IME-safe text entry, real feedback, pause/resume/replay, error recovery, explicit draft assessment support and result-based advisory placement suggestions.
- App.tsx, LessonDetails.tsx and styles.css connect the real workflow. Session hashes survive refresh and switching between saved sessions. Edited answers are clearly unchecked/unsaved; prior feedback is labeled as the previous saved result.
- backend/tests/test_learning.py, frontend/src/study.test.ts and scripts/verify_study_ui.py provide focused regression and real-browser coverage.
- Source content is 0.1.5. Only draft placement/mastery bank metadata was added; existing published units/exercises/vocabulary remain unchanged. The review packet includes these selections and the exact source hash. No unreviewed content was promoted.

## Data and migration

Migration 0003 adds study_sessions, study_events, study_mistakes and xp_ledger. No existing data is dropped or reinterpreted. Empty migration/drift and populated0002->0003 upgrade tests preserve profile/settings, course snapshots and assistance. Attempt/completion update tests preserve original answers and rewards through content changes.

SQLite writes acquire BEGIN IMMEDIATE before read-modify-write and commit answer/evidence/mistake or finish/XP/activity together. A failed receipt write rolls back the whole operation. First committed completion earns20 XP; new genuine replay/practice/assessment sessions earn5 XP without daily caps. Duplicate delivery returns its original receipt and does not create another award. No access, correctness, mastery or FSRS effect is inferred from XP.

Tests use disposable migrated databases. Browser QA used a separate database and ports8014/5184 while the existing personal preview remained running on8000/5173. The personal database was not imported, migrated, reset or used by these tests. A real QA process restart and import0.1.4->0.1.5 retained an old completed0.1.4 session with its evidence and reward.

## Commands and results

Commands use the existing .venv Python and installed frontend packages; no downloads or new dependencies.

- npm run lint — PASS.
- npm run typecheck — PASS.
- npm run test -- --run — PASS:15 tests.
- npm run build — PASS; existing benign Lucide use-client directive warnings remain.
- python -m pytest -q --tb=short --basetemp=../.tools/pytest-phase4-verified78 -o cache_dir=../.tools/pytest-cache-phase4-verified78 — PASS:78 tests. One existing Starlette/httpx deprecation warning.
- python -m ruff check app migrations tests — PASS.
- python -m app.cli validate — PASS:0.1.5,6 lessons,30 exercises,8 core words,5 phrases.
- python -m alembic upgrade head — PASS in the disposable QA launch. Alembic command.check drift checks and empty/populated upgrades also PASS inside the full pytest suite.
- python scripts/verify_study_ui.py — PASS with already-installed system Python Playwright. QA health reports schema0003, QA=true; all non-loopback and mismatched API requests are blocked.
- .tools/verify-study-restart.py — PASS read-only smoke: completed0.1.4 evidence survives the restarted QA backend while current content is0.1.5.

One later default pytest invocation hit Windows permissions on the shared Temp/pytest-of-Administrator directory. It produced setup errors, not passing tests. The final full run above uses a fresh verified workspace-local disposable target and passes every test. No assertions or tests were skipped or weakened.

## Browser and manual critical flow

artifacts/study-ui-results.json records56 passing responsive layouts: choice, typed response, ordering, matching, completion, practice hub and placement at320/390/640/768/1024/1280/1440/1536px. Representative screenshots are artifacts/screenshots/study-*.png; current rendered DOM is artifacts/study-rendered.html.

The real browser flow opens a later lesson without history, pauses/leaves, answers incorrectly repeatedly, recovers a committed answer whose response was deliberately lost, reveals/hints, types Japanese with simulated composition events, reloads a saved answer, distinguishes subsequent unsaved edits, skips, reorders with keyboard buttons, matches labeled selects, finishes, reloads, replays for5 XP, changes support mode, finishes draft placement and opens the recommended lesson. A saved completed session remains reachable after switching session hashes. It also verifies200% text at320px, loading versus successful empty results, initial session failure/reload recovery, and a44px course-path link. Zero unexpected page errors or external requests.

Backend tests additionally cover every authored key/alternate, invalid answer shapes, repeated visible tokens with stable IDs, normalization distinctions, first versus assisted/corrected/skipped evidence, direct published assessment access, unlimited same-day completions, concurrent duplicate requests, stale revisions, rollback, server-controlled XP, goals, first/consecutive/repeated/missed days, timezone changes/boundaries and spring DST.

## Design audit and limits

Applied installed ui-ux-pro-max, frontend-design and design-skill with shared tokens. Focused local search matched button alternatives for dragging and controlled form submission. No external inspiration/font/image assets were downloaded. Independent Standards and Spec axes were delegated as design-skill requires. Final Standards recheck24/24 for inspected surfaces; Spec has no remaining scoped finding. Prior findings and their fixes are appended to .design-skill/audit-report.md.

Physical Windows IME, a screen-reader session, touch/stylus hardware and qualified Japanese review were not performed. Composition events, DOM semantics, pointer-free controls and screenshots are narrower evidence. Three optional assessment banks stay draft previews; no reviewed proficiency, mastery certificate, story/audio/FSRS or handwriting capability is claimed.
