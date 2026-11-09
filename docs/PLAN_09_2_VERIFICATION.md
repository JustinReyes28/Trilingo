# Plan 9.2 execution record

Status: authorized work window finished within one hour; the full supplement remains partial.

Authorized run: 2026-10-23T11:59:10.326Z to hard stop 2026-10-23T12:59:10.326Z (maximum one hour). Installed tooling only; no dependency/model/browser downloads.

## Baseline and safety (A1, A4)

Read README, master plan, all Phase 1–9 files, Plan 9.2 and latest Phase 7–9 evidence. Preserved 195 source files and a SHA-256 manifest in ignored .tools/plan-9-2-baseline before edits. Git currently reports the application files as untracked, so that preserved baseline is the diff authority.

Source: ja-starter 0.1.14; exact file SHA-256 01f8d1951225494b5e59c472e0525f5222826679d0601852d2df7d798cab18b6. Schema starts at 0011. Windows NT 10.0.26200.0, PowerShell 5.1.26100.9444; installed Node 25.2.1 and Python 3.14.0. Lockfile/runtime details are preserved in the baseline. Supported Node 24 LTS/fresh setup (A2) remains unverified.

All test databases/caches/services use named .tools/ locations and explicit QA configuration. The learner database .data/trilingo.db and personal launcher are excluded. The normal shell tool failed at process setup; local Node child processes provide working access to installed commands.

## Scope and pending evidence

Working on the complete lexical inventory/review queue (B1/B2/B4) and historical timing access (H3/H6), followed by affected regression and rendered checks. No content publication or qualified review is implied. All unchecked plan tasks remain open until evidence below proves them.

Qualified Japanese/stroke review, physical Windows IME, screen reader, touch/stylus, human microphone/listening, real Kokoro/STT and real local model calls remain pending prerequisites. Unavailable prerequisites do not prevent independent implementation.

## Delivered and authoritative evidence

Final content: **0.1.15**, SHA-256 **4eda311cf0b265ca879dcb56d0ab0c8179f65fcc2ad7a412928b0821f731a117**. Schema: **0012**. The two published units (six lessons/thirty exercises) are byte-equivalent as structured objects to the preserved baseline. Eight published word records and five expressions remain unchanged. No content was promoted to reviewed/published.

- **Inventory/review queue:** source-bound canonical identity decisions distinguish the school spelling variant from homophones. 286 word records produce 285 provisional identities (103 Stage A +182 Stage B); semantic/qualified review and the 2,000-word target remain open. The reproducible packet contains 1,456 stable items, exact source, licenses, private keys/alternates/transcripts/overrides, and six copied stroke assets. It validates source/asset digests and refuses to overwrite a reviewer correction. Exact 0.1.14 and older Markdown packets are preserved.
- **Beginner instruction:** nine new draft guides plus the existing introduction and particle notes provide sixteen guides mapped explicitly across ten units. Eight outlined units now have one original draft lesson each, totaling 24 additional checks. Examples/readings, scoped alternatives, register/culture notes and answer-specific contrasts remain draft. Unit filtering and searches include Japanese examples/readings, common mistakes and notes. Published lesson keys remain protected; draft lesson publication is denied while explicit draft guide practice uses the existing engine.
- **Recall/history:** complete keyset timing pages support next/previous/first/last and activity filters; batches default to five and can be changed. New timers record actual paused intervals; legacy pause duration is unknown, never inferred as zero. The 1,200-session fixture reaches every history record without overlap after a new completion, preserves complete totals and stays within the bounded-query assertion.
- **Collections:** collection-scoped meaning/reading/typed self-rated recall uses saved source snapshots. Existing card snapshots, FSRS states, due dates and ratings remain unchanged. Preparing/browsing/skipping earns nothing. Added pagination/Show all and fixed the initial reload that discarded expanded card batches. A rendered race when switching directions now disables old cards while the new view loads.
- **Evidence/statistics:** objective responses join their original course snapshots. Per-skill first-answer checks and assistance/skips remain separate from self-rated review counts, composition/formation workflows and publication coverage. Workflow totals require a real completion/XP ledger event. Later stages and qualified-review gaps remain explicit; no proficiency percentage or handwriting/pronunciation grade is inferred.
- **IME guide:** verified against current official Microsoft Learn/Support pages on 2026-10-23; see [input evidence](WINDOWS_JAPANESE_INPUT.md). The unsaved tester passes synthetic composition/Enter/multiline checks. Physical Windows IME use remains unverified.

## Data and migration review

0012 adds ix_study_timing_history over profile/status/completion/ID. It does not rewrite timer JSON, receipts, XP, attempts or learner content. New optional pause metadata applies to new timers; older JSON remains readable. A populated 0011 forward-upgrade regression preserves timer metadata, immutable receipts, ledger and profile exactly and checks Alembic drift. Existing earlier populated-upgrade tests pass. No manual database edits or runtime table creation were used.

QA database/cache: .tools/plan-9-2-qa.db and .tools/plan-9-2-audio-cache; frontend/backend 5192/8022. The disposable clean migration database is .tools/plan-9-2-migration-final.db. Actual restart preserves settings, progress and XP; its health reports QA mode, schema 0012 and all provider gates false. The personal database/launcher were not migrated, imported, reset or stopped.

## Exact commands and results

Installed backend Python means .venv/Scripts/python.exe. Installed browser Python is C:/Users/Administrator/AppData/Local/Python/pythoncore-3.14-64/python.exe with its existing Playwright package; installed Edge executable is C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe. No browser/dependency install ran.

From backend/: unchanged baseline pytest run passed **175 tests**. Targeted runs passed **9 history/timing**, **3 inventory**, **17 collection/FSRS**, **27 guide/content**, and **3 personal/large-history** tests.

Final candidate:

~~~text
python -m pytest -q --basetemp=../.tools/pytest-plan-9-2-complete-run -o cache_dir=../.tools/pytest-cache-plan-9-2
185 passed, 1 existing Starlette/httpx deprecation warning (136.47s)
python -m ruff check app migrations tests
All checks passed
python -m app.cli validate
0.1.15; 6 published lessons / 30 exercises / 8 words / 5 expressions
python -m app.content_audit --output ../docs/reviews/ja-starter-0.1.15
PASS; source hash above, 285 canonical authoring identities / 1456 review items
~~~

From frontend/ (the underlying commands used by npm run lint/typecheck/test/build):

~~~text
node node_modules/eslint/bin/eslint.js .
PASS
node node_modules/typescript/bin/tsc --noEmit
PASS
node node_modules/vitest/vitest.mjs run
29 passed, 6 files
node node_modules/vite/bin/vite.js build
PASS; JS 496.15 kB / gzip 143.62 kB; two pre-existing Lucide directive warnings
~~~

From root:

~~~text
.venv/Scripts/python.exe scripts/qa_plan92.py --database .tools/plan-9-2-migration-final.db --check-only
PASS; empty schema to 0012, no drift, first import True / repeated import False
.venv/Scripts/python.exe scripts/qa_plan92.py --database .data/trilingo.db --check-only
EXPECTED REFUSAL (exit 2) before opening the personal database
.venv/Scripts/python.exe -m ruff check scripts/qa_plan92.py scripts/verify_plan92_ui.py
PASS
~~~

Isolated API smoke: health, settings/profile, course/map/library, grammar/search/unit filter, recall/collections, personal/timing and normal session actions all return validated results. Restart preserved exact settings/progress responses.

Browser commands (installed browser Python):

~~~text
python scripts/verify_plan92_ui.py
PASS: 40 layouts, no page errors or external requests
python scripts/verify_phase789_ui.py --base http://127.0.0.1:5192 --api http://127.0.0.1:8022/api/v1
PASS: 28 layouts; three authored dialogues, branch/resume, bookmarks, quests, early/repeated ratings, preferences and provider-disabled recovery
python scripts/verify_study_ui.py --base http://127.0.0.1:5192 --api http://127.0.0.1:8022/api/v1 --browser-executable "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
PASS: 56 layouts; direct later lesson, five renderers, wrong/retry/reveal/skip, lost acknowledgement, refresh/replay, genuine XP and loading/error recovery
~~~

Together these final runs checked **124 layouts**. New screens use 320/390/768/1280 widths; core study also checks 640/1024/1440/1536. Artifacts: artifacts/plan-9-2, artifacts/phase789 and artifacts/screenshots. Scripts operate only on explicit QA origins and block external requests. Other reading/writing/listening/recording scripts were not rerun: their unchanged feature scopes have historical evidence; real devices/providers remain open.

Initial failures were retained and fixed: the old schema-version assertion (0011), the previous one-result particle search after broader guides, a stale collection direction, an ambiguous history label, and browser assertions that read unchanged row counts before the next response rendered. No test was skipped or deleted and no failure was treated as success. Public counts/expected IDs were updated explicitly for version 0.1.15.

## Rendered design review

Used ui-ux-pro-max, frontend-design, design-skill and webapp-testing. The focused keyboard-pagination search returned relevant visible-focus/logical-order guidance; no new visual preset was persisted. Inherit the existing teal/plum product workspace and Japanese text roles.

Reviewed actual mobile/desktop images for collection recall, history, Japanese guides and feedback. Fixed a narrow collection-scope action squeezed into a tall column by making its grouping a block. History now has top navigation and a compact five-record default. Unique note IDs prevent duplicate document anchors. Native labeled controls, text feedback, existing focus and reduced-motion rules remain.

Design-skill detect on rendered HTML reports the existing dashed course-path connector, navigation icon/heading proximity, pill radii, unused 1440px utility and sr-only clipping/position/negative margin. These are inherited CSS/structure findings, not observed accent rails or horizontal overflow on these screens. Detector output alone is not an accessibility pass. Focused history screenshots are also saved as history-detail-320.png and history-detail-1280.png. Physical screen-reader, IME, touch/stylus and audio checks remain unverified.

## Task reconciliation (full supplement remains partial)

- **A1 verified:** current requirements/source/contracts and baseline/versions reconciled. **A2 awaiting** supported Node 24 LTS plus a complete authorized install cache/connection. **A3 partial:** current installed-runtime clean DB/import/health/connection/settings/restart and port-conflict behavior verified; supported fresh setup remains open. **A4 verified for this run:** isolated paths, additive migration and preserved populated history; cleanup is recorded below.
- **B1 partial:** versioned authored inventory and explicit/inferred mappings exist; full 2,000-word target inventory is missing. **B2 partial:** spelling/homophone decisions and provisional counts are reproducible, with no learner merges; comprehensive qualified semantic review remains open. **B3 partial:** eight initial draft lessons/24 checks and all ten topic guides added; 500+1,500 unique reviewed words and sufficient full courses remain open. **B4 partial:** exact-source packet regenerated/preserved; reviewer identity/qualifications/decisions are pending. **B5 partial:** repeat-import/history regressions pass; qualified corrections/publication remain pending. **B6 partial:** current claims reconcile; reviewed full inventory is unavailable.
- **C1/C2 awaiting** qualified kana/kanji/story/passage review and publication. **C3 pending** a complete current reading/library/aids manual audit. **C4 awaiting** an actual Japanese screen-reader session. No reading gate is closed.
- **D1 verified:** official-documentation check and in-app tester; physical operation is separately pending. **D2/D3 awaiting** qualified task/model/stroke review. **D4 awaiting** physical IME. **D5 awaiting** actual mouse/touch/stylus formation checks for this run; existing geometric/keyboard tests remain distinct.
- **E1/E2 partial:** ten-topic draft instruction, search/filter, scoped alternatives and contrasts exist; qualified review/publication remains open. **E3 engineering verified:** authored branch/resume/duplicate/bookmark/collection/content-update/search/fallback tests plus three browser-operated dialogues pass; no human linguistic sign-off follows. **E4 awaiting** a real loaded local explanation/coaching model.
- **F1 awaiting** reachable Docker/provider engine: context/config inspection was denied and the default engine pipe was absent. **F2 awaiting** installed wrapper/model/voice/dependency identification. **F3 awaiting** actual five-phrase Japanese synthesis and human listening. **F4 awaiting** selection/pinning/verification of an independent Japanese STT provider. **F5 awaiting** a real microphone/STT round trip. No container/model/disk changes were attempted.
- **G1/G2 partial:** existing authored audio/fallback engineering tests pass; reviewed stories/episodes and actual Japanese output remain missing. **G3 pending:** durable rewarded speaking-only sessions are still unimplemented. **G4/G5 pending:** complete voiced scenarios and speaking-aware quest evidence depend on that work. **G6 partial:** provider-disabled core study and mocked failure regressions pass; real-media/provider verification remains open.
- **H1 partial:** actual objective skills and self-rated directions/provenance now remain separate; audio/speaking mappings still need their workflows. **H2 partial:** collection-scoped meaning/reading/typed self-rated recall, snapshots and pagination verified; collection audio/speaking modes remain open. **H3 verified:** complete stable timing history, filtering/final page, active/paused/legacy labels and non-expiring behavior. **H4 verified for the existing scope:** stored objective/workflow/review/publication counts and cold/later-stage/provenance labels reconcile; no full beginner proficiency claim. **H5 engineering tests pass** for current FSRS directions; broader completion audit remains open. **H6 partial:** 1,200-session totals/history and 45-collection pages/bounded queries pass; broader review-history audit remains. **H7 automated UI evidence obtained** for early/repeated review, batches, skip, later lesson, cosmetics/preferences and restart; no physical-device claim.
- **I1/I2 partial:** current rendered/interaction/error/unrestricted-study checks pass; physical accessibility/real-provider checks remain open. **I3 verified** for changed engineering with final quality/content/migration/API/browser gates. **I4 partial:** 124 isolated layouts; actual devices/providers unavailable. **I5 diff/data/license/answer-boundary review recorded:** compare against preserved baseline, retain draft labels and immutable snapshots/receipts. **I6 this report records partial scope; full Phase 10 handoff remains unearned.**

## Remaining work and next execution

Next independent engineering priority: durable speaking-only sessions through shared rewards/activity, typed fallback and truthful provider evidence (G3), followed by voiced scenarios/skill mappings and remaining history/mode audits. In parallel, expand original content well beyond the new first draft lessons: 397 additional Stage A and 1,318 additional Stage B authoring identities remain against the provisional counts, followed by qualified review. These are inventory gaps, not learner requirements.

Qualified Japanese/stroke/audio review, a supported Node 24 fresh install, real local AI/TTS/STT, human listening/microphone, physical IME, Japanese screen reader and touch/stylus evidence are still required. Phases 1,3,5–9 and the full supplement remain partial. Phase 2/4's previous technical scope is preserved; Phases 10/11 remain separate.

## Final audit and cleanup

The first handoff was at 2026-10-23T12:52:01.674Z (52.9 minutes); the remaining-window continuation below records the final stop. No further work is authorized beyond that cap without a new window. The full objective is not marked achieved or redefined around this run.

All owned QA services are stopped. Both 5192 and 8022 return ECONNREFUSED; artifacts/plan-9-2/cleanup.json records the check. The Vite process/console host and backend IDs were identified from their owned parent/command line before stopping; the personal launcher was excluded. Normal sandboxed process termination was denied, so approved execution was used only to stop those owned processes. No automatic approval rejection occurred.

Final baseline comparison identifies 69 changed/new files, including deliberately preserved exact-source review packets. Main areas are backend review/collections/timing/API schemas and migration 0012, original draft content/audit tooling, frontend recall/grammar/input controls, targeted tests/QA launch/browser scripts, and current documentation/checklists. The per-file SHA-256 list is .tools/plan-9-2-changes.json; full command logs, including initial failures, are in .tools/plan-9-2-runs. Dependency lockfiles and AGENTS.md are unchanged. Original published unit objects and existing source licenses/writing/character assets remain unchanged.

106 local Markdown links in the affected current documents resolve and fenced blocks balance. Final packet regeneration is idempotent and matches the exact current source hash; the previous 0.1.11 Markdown packet is byte-preserved. Git ignore checks exclude .tools, the learner DB, artifacts and frontend/dist. No secrets, raw recordings, models or learner data are added to source.

Only A1, A4, D1, H3, H4 and I3 in the supplement were checked in this run. The matching Phase 6 documentation-guide and Phase 9 honest-statistics items were updated; full phase/milestone gates remain unchecked. No supported fresh install, qualified review/publication, real AI/TTS/STT/human audio, physical IME/screen reader/touch/stylus or full Phase 10 handoff was claimed.


## Remaining-window continuation

The automatic continuation arrived at 12:53:10 UTC, inside the original 12:59:10 UTC cap; it did not create another hour. Added one H3 regression for equal completion timestamps, a new tied completion between pages, reverse navigation and final-page access. This is test-only: runtime/UI/content/schema source is unchanged.

python -m pytest -q tests/test_large_history.py --basetemp=../.tools/pytest-plan-9-2-timestamp-ties -o cache_dir=../.tools/pytest-cache-plan-9-2 — PASS: 2 tests (1.40s); Ruff for the changed test file passes. The final full backend run below supersedes the earlier 185-test total; UI/runtime source is unchanged, so prior frontend and browser gates remain valid.


Final command, from backend/:

~~~text
python -m pytest -q --basetemp=../.tools/pytest-plan-9-2-window-final -o cache_dir=../.tools/pytest-cache-plan-9-2
PASS: 186 tests, 1 existing Starlette/httpx deprecation warning, 130.71s
~~~

The final stop was 2026-10-23T12:58:38.813Z (59.5 minutes from the authorized window start), before 12:59:10 UTC. Only the history test and this record changed during the continuation; source 0.1.15/schema 0012 and all other scope/limitations are unchanged. Every owned process is terminal. The full Plan 9.2 objective remains partial and is not marked achieved.

## Current continuation — 2026-10-24

[The speaking/audio-recall continuation record](PLAN_09_2_SPEAKING.md) supersedes this first window's current-source facts: 0.1.16/schema 0013, 16 draft speaking prompts, preserved published content, five self-rated word/collection directions, final 197 backend/31 frontend tests and 24 focused new layouts. Earlier results above remain historical. G3/G5/H1 engineering scope is verified; the complete plan remains partial.
