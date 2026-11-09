# Phases 4–6 engineering handoff

The current practice/draft implementation is ready to try. Full release gates remain open: qualified Japanese task/stroke review, the full content inventory, current-official Windows IME guide verification, supported-LTS clean setup and physical IME/touch/stylus/screen-reader checks. No reviewer is available, so no new content was published and no proficiency claim is made.

## Delivered

- Phase4: five reusable exercise renderers, authoritative grading, durable session/pause/resume/mistake evidence, uncapped genuine-session rewards and idempotent retries. Optional assessments remain advisory.
- Phase5:92basic kana,135separate variants/combinations/marks,300draft contextual kanji(100StageA+200additionalStageB), adjustable ruby/romaji, self-reported saved/familiar items and related practice,2draft stories and4draft passages. Reading assistance/skips remain distinct from unaided answers. The300-kanji authoring target is present as draft; reviewed publication and the2000-core-word target remain open.
- Phase6: checked character/word/constrained-message typing through the shared grader; Japanese input tester and on-screen kana aid;7draft writing tasks(4StageA/3StageB) with models, checklist and an annotated revision; multiline drafts, optimistic revision identities, autosave/retry/recovery, preserved conflicts/history and unassessed/self-reviewed submissions.
- Formation:6original, versioned, licensed, digest-checked draft templates(3kana/3kanji); scalable pointer grid, numbered starts/directions, undo, confirmed clear/mode/character changes, local stroke replay, keyboard sequence alternative, geometry-only feedback, optional raw samples and deletion. Raw drawing is absent from browser recovery and idempotency receipts; only receipt identity/digest is retained unless a sample is deliberately kept.

## Data safety

Migration0004 adds reading items. Migration0005 adds writing drafts, immutable revisions, preserved conflicts, submissions, idempotency events and optional drawing samples. Both are additive; normal startup never resets data. Tests cover clean migration/drift and populated0004→0005 retention of settings, course snapshots, completed sessions, XP and saved reading items.

Autosaves, bookmarks and familiarity changes earn no XP. A committed new open-writing or formation practice session earns5XP. Duplicate deliveries return their original result. Open writing and drawing do not become objective correctness, mastery or FSRS errors from length, self-rating or XP.

Personal5173/8000services and .data/trilingo.db were left untouched. QA8014/5184uses a separate database. Restart the personal launcher to load new migrations/routes/content; do not delete the personal DB.

## Files and contracts

Backend:app/writing.py, writing_api.py, writing_models.py, writing_schemas.py, handwriting.py; additive migration0005_writing.py; shared learning/content extensions. Frontend:WritingPage, WritingEditor, useWritingDraft, ImeGuide, KanaInputAid, HandwritingPage, DrawingPad, writing schemas/API and shared pendingRequests. Original source/assets:content/courses/ja/starter.json0.1.11 and assets/strokes/. Source SHA-256:92d4dd8f429866ad8dc29007b2639804a17ea41fff5068608f9ef75ddd8e96ae.

The refreshed [review packet](JAPANESE_CONTENT_REVIEW.md) contains all keys, models, scripts, character/context references and stroke provenance. Its0.1.5predecessor was preserved under docs/reviews/. All review decisions remain pending.

## Commands and results

Real commands used the existing local Python/Node tools; no package, browser, font, asset or model download was performed.

- Backend:python -m pytest -q --tb=short --basetemp=../.tools/pytest-writing-full -o cache_dir=../.tools/pytest-cache-writing-full —118PASS. Isolated databases only.
- python -m ruff check app migrations tests —PASS.
- python -m app.cli validate —PASS for0.1.8, all original stroke hashes/references; published slice remains6lessons/30exercises/8core words/5phrases.
- With DATABASE_URL=sqlite:///.data/migration-writing-0005.db:python -m alembic upgrade 0004; python -m alembic revision --autogenerate --rev-id 0005 -m writing; migration reviewed additive-only; python -m alembic upgrade head; python -m alembic check —PASS, no drift. Populated upgrade is additionally tested in test_writing.py.
- Frontend:npm run lint; npm run typecheck; npm run test -- --run; npm run build —PASS;24tests. Existing Lucide bundler directive warnings remain benign; one existing Starlette/httpx deprecation remains.
- Root:python scripts/verify_writing_ui.py —PASS24layouts at320/390/768/1280, no browser errors/external requests. The final run used TRILINGO_QA_BROWSER_CHANNEL=msedge because the previous cached Playwright browser disappeared. No browser was downloaded.
- Browser regression checks:IME Enter/autosave delay; lost save response plus newer typing; separate-tab conflict/reload/deliberate new revision; lost submission response and one reward; genuine repeat submission; failed kana support exposes no aid, reload/retry and per-prompt support; normalized mouse strokes; clear/mode/character/preview confirmation; frozen choices during lost drawing response; optional sample deletion; keyboard sequence;200%text; no raw browser recovery.

Test construction failures were corrected rather than bypassed:XP assertions now wait for the new response, blank-answer recovery checks target the aid control, and a guarded checkbox is clicked without assuming its state changes before confirmation. A missing cached browser caused one launch failure; the installed Edge fallback completed the run. No tests were disabled or assertions weakened to hide product failures.

## Rendered audit and limits

Both required independent axes completed a bounded final recheck. Standards24/24for inspected scope; Spec has no open scoped findings. Fixes include per-prompt acknowledged kana support, guarded drawing changes, frozen pending choices,7.02:1guide contrast, visible instruction numbering, and feedback inside active dialogs. [Audit record](../.design-skill/audit-report.md) preserves detector output and the earlier findings/fixes.

Automated critical flows and actual screenshots were inspected; this does not certify physical Japanese IME conversion, a real screen reader, touch or stylus. Official Windows instructions were not fetched under the cellular constraint; the guide is visibly draft. Stroke/model/content review remains pending. No handwriting recognition or advanced C–F workshop is claimed.

Final shared-engine regression with TRILINGO_QA_BROWSER_CHANNEL=msedge: python scripts/verify_study_ui.py — PASS 56 layouts; python scripts/verify_reading_ui.py — PASS 24 layouts. Together with writing 24, 104 actual layouts passed with no page errors or external requests. No product code changed after these final checks.


## Historical completion status — source 0.1.9 (superseded below)

Phase 4 engine is complete for the technical-practice slice. Phases 5 and 6 remain partial, not fully complete. Phase 5 still has only 18/300 contextual kanji (282 remain) and lacks qualified review/publication. Phase 6 still needs qualified model/stroke review, current-official guide verification and physical IME/touch/stylus/screen-reader checks.

The two previously missing reading formats are now original draft menu/message passages: four passages total, 218 standalone drills. Existing UI/browser evidence above covers source 0.1.8; no new browser run is claimed for these data-only additions. Source 0.1.9 SHA-256:c005f6b1e01db9d7739bad15accfa3b1609cc6c1f288439d28f8965df2b46907. The previous review packet is preserved under docs/reviews/.

Latest commands: python -m pytest -q --tb=short --basetemp=../.tools/pytest-passage-completion -o cache_dir=../.tools/pytest-cache-passage-completion —120 PASS; python -m ruff check app migrations tests —PASS; python -m app.cli validate —PASS. No frontend code, dependency, migration or personal database changed in this content-only continuation. No downloads.


## Expanded draft inventory — current source 0.1.11

The kanji authoring target is now present: 100 distinct Stage A plus 200 additional Stage B characters, all draft. Source totals: 527 characters, 481 standalone practice definitions, 286 word records and 5 expressions. The 2,000 unique-word curriculum target and semantic deduplication remain open. The 282 newly authored contexts share 263 reading checks and 262 new word records; compounds reuse stable IDs. 家 reuses ja-word-house without changing its published practice references; all new contextual checks require explicit draft preview.

The word list now searches the entire available library by Japanese, kana reading or meaning before applying the freely expandable display batch. Show more/all preserves unrestricted access; no-match text and Clear search provide recovery.

Source SHA-256: 92d4dd8f429866ad8dc29007b2639804a17ea41fff5068608f9ef75ddd8e96ae. The current review packet includes every new context, vocabulary record, example, choice and key. Earlier exact packets, including 0.1.9 and 0.1.10, are preserved under docs/reviews/. No new Japanese content was published.

Commands run from backend/:

- `..\.venv\Scripts\python.exe -m pytest -q tests/test_reading_content.py tests/test_reading_api.py --tb=short --basetemp=../.tools/pytest-kanji-targeted -o cache_dir=../.tools/pytest-cache-kanji-targeted` —15 PASS.
- `..\.venv\Scripts\python.exe -m pytest -q --tb=short --basetemp=../.tools/pytest-kanji-full -o cache_dir=../.tools/pytest-cache-kanji-full` —122 PASS before the additional draft-boundary regression.
- `..\.venv\Scripts\python.exe -m pytest -q --tb=short --basetemp=../.tools/pytest-kanji-final -o cache_dir=../.tools/pytest-cache-kanji-final` —123 PASS on final source0.1.11, including the new canonical-word draft-boundary regression.
- `..\.venv\Scripts\python.exe -m ruff format tests/test_reading_content.py` and `..\.venv\Scripts\python.exe -m ruff check app migrations tests` —PASS. Five new-test line-length findings were corrected; no test was weakened.
- `..\.venv\Scripts\python.exe -m app.cli validate` —PASS0.1.11.
- `..\.venv\Scripts\python.exe -m app.cli import` with QA_MODE=true and DATABASE_URL=sqlite:///.data/phase4-qa-1792718310946.db —PASS; additive immutable import only. No schema change/migration was needed; the backend suite exercises migration/drift and upgrade retention.

From frontend/: `npm run lint`, `npm run typecheck`, `npm run test -- --run`, `npm run build` —PASS,24 tests. Existing Lucide directive warnings remain; no dependency changes/downloads.

From root: `$env:TRILINGO_QA_BROWSER_CHANNEL='msedge'`; `& 'C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe' scripts/verify_reading_ui.py` —PASS32 layouts at320/390/768/1280 plus200% text, no page errors/external requests. Checks cover full291-record expansion, Japanese/kana/meaning search, empty/clear/focus, direct Stage B皿 practice, kana/dialog/errors, stories/replay/acknowledged rewards and reading aids. Browser run used0.1.10;0.1.11 only restores published canonical-word references, with no UI/text/key change. The final backend regression verifies that boundary.

API smoke: `Invoke-RestMethod -Uri 'http://127.0.0.1:8014/api/v1/health'` and `/api/v1/courses` —PASS, QA mode, schema0005 and imported version. Personal5173/8000 and .data/trilingo.db remain untouched.

Rendered mobile and desktop search screenshots were inspected. Full-page Edge captures show occasional blank compositor strips; both independent audits checked real viewports and found the results/buttons rendered correctly. No screenshot artifact was mistaken for a working-flow result. Scoped Spec has no findings; Standards final is recorded in the audit. This does not certify physical IME/touch/stylus/screen-reader operation or qualified Japanese/stroke quality.

Phase4 remains complete for the technical-practice engine. Phases5–6 engineering is usable, while qualified reviewed publication, official IME-guide verification and physical-device gates remain open.
