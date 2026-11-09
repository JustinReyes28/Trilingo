# Phase 5 engineering verification

The draft-scope reading implementation is usable; the full phase release gate remains open for qualified Japanese review/publication, review/publication of the300-kanji inventory and actual screen-reader verification. No reviewer is available; new content remains draft.

## Implemented

- Data-driven atlas:46basic hiragana+46basic katakana,135separately counted variants/combinations/marks,300draft contextual kanji(100StageA+200additionalStageB). Hidden romaji is absent from accessible labels. Original notes/contrast checks cover small kana, held consonants,ん,vowel length,ー,voicing and similar shapes.
- Structured Japanese ruby follows persistent always/unfamiliar/hidden settings. Unfamiliar uses explicitly self-reported word familiarity. Hidden readings are removed from DOM/API stimulus, rather than visually concealed.
- Saved words/characters persist through migration0004. Related voluntary practice uses shared server graders/sessions; saving/familiarity awards no XP and never claims mastery.
- Two original draft stories and four short draft passages use turn navigation, optional checks, glossary support, skip/finish/replay/recap and preserved snapshot evidence. Finishing explicitly records untouched checks as skipped. Every genuine completed session earns5XP; receipt retries earn nothing extra. Glossary/ruby support remains assisted even after hiding or moving turns.
- Character quiz titles and public choice IDs do not disclose the target answer. Reading, recognition and typed-response skills remain separately tagged; no handwriting/speaking claims follow from reading.

## Validation performed

Commands from backend unless noted:

- python -m pytest -q --tb=short --basetemp=../.tools/pytest-reading-complete -o cache_dir=../.tools/pytest-cache-reading-complete —96PASS before the additional neutral-title regression.
- python -m pytest tests/test_stories.py tests/test_reading_api.py -q --tb=short --basetemp=../.tools/pytest-reading-audited -o cache_dir=../.tools/pytest-cache-reading-audited —12PASS, including all92basic quiz titles/neutral IDs and persistent glossary support.
- python -m app.cli validate —PASS(content0.1.7; published slice unchanged).
- python -m ruff check app migrations tests —PASS at the reading milestone.
- npm run lint; npm run typecheck; npm run test -- --run; npm run build —PASS(19frontend tests; existing Lucide directive warnings only).
- Python scripts/verify_reading_ui.py from root using installed Playwright —PASS24layouts, no page errors/external requests; modal503/reload recovery, draft guard, save/reload, related character practice, story mistakes/help/skips/resume/replay/XP, unfamiliar ruby, hidden romaji and200%text.
- Separate owned QA services8014/5184 migrated/imported without resetting history; personal5173/8000and personal DB untouched. Later Phase6 work extends schema/content; its combined gate must be rerun.

## Rendered review

[Audit](../.design-skill/audit-report.md):Standards24/24for inspected scope; Spec no open scoped findings after fixes. Artifacts are local ignored files under artifacts/screenshots/reading-*.png and artifacts/reading-ui-results.json. Mobile/tablet/desktop and keyboard focus were checked. Automated composition/DOM checks do not certify a physical IME or screen reader.

## Remaining limitations

The300-character authoring target is present as draft. Draft examples do not satisfy the reviewed300-kanji/two-published-story gate. Current inventory and commands are recorded below; StageA-B2000-word coverage is not claimed. Phase6 adds versioned draft writing tasks/assets; that source is separately reviewed in its verification record. Audio contrast/playback belongs to Phase8.


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
