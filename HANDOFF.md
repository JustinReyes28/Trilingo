# Trilingo — resume handoff

**Planning update — 2026-10-25:** new agents should use [the continuation guide](docs/AGENT_CONTINUATION_GUIDE.md) with this handoff. The user requested a [Windows EXE setup roadmap](docs/plans/WINDOWS_EXE_SETUP_PLAN.md) and confirmed a [standalone offline Android app](docs/plans/ANDROID_PORT_PLAN.md). Both are planned only. EXE-0 and Android A0/A1 feasibility may proceed on a future implementation instruction alongside content review, without waiting for public launch/C–F; complete platform releases retain shared safety/content gates. This documentation request does not resume implementation or renew the spent application checks. The run/deadline/check records below are historical; apply the current user's bounds on a future resume and do not invent a new numeric approval requirement.

Updated: **2026-10-25** for bounded execution. Status: **remaining-work plan partially executed; full Plan 9.2/release gates remain open**. The user authorized at most **two hours and18 check/review rounds**, including five extra checks and a final three-check/30-minute writing/grammar batch. Original start: **11:05:34 UTC /19:05:34 Singapore**; outer hard stop: **13:05:34 UTC /21:05:34 Singapore**. The final batch starts **12:10:00 UTC** and stops by **12:40:00 UTC /20:40:00 Singapore**. See [the execution plan](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md) and [current run evidence](docs/PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25). A spent check/time allowance does not renew automatically; no full completion is implied.

The first ten rounds finished by11:41:31UTC and the five-check extension finished verification by12:04:42UTC. The user subsequently approved **up to three further checks and30minutes** within the original deadline: total cap **18**. Final verification finished by **12:23:25 UTC /20:23:25 Singapore**. The final batch fixes stale grammar views/error recovery and an unsaved-drawing receipt bug; Node24 quality gates, eight browser layouts, script Ruff,158 local links and source/checkbox/baseline reconciliation pass. **All18 rounds are spent; no additional check/review is authorized.** Reuse these results rather than restart broad reviews. The full objective remains incomplete.

## User constraints

- Project/product name: **Trilingo**. Preserve it in the app, documentation, repository/release identity and future uploads.
- The connection is **cellular/metered**. Prefer installed tools and local files/caches. The user's 2026-10-25 instruction permits focused web search, but **ask before any download or upload, with its purpose, exact scope/source/destination and estimated total network MB/GB**, including dependencies/layers. Wait for explicit approval; no automatic transfers/retries. This includes Git, reviewer packets and release/social assets as well as runtimes/packages/models. Ordinary documentation reads and local/loopback work are allowed. Follow the [detailed transfer protocol](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md).
- The user wants faster, focused progress: **do not overextend, overreview or overtest**. Make a coherent change, run the relevant targeted checks once, fix real failures, record results and stop at the agreed time. Do not repeat unchanged full suites or large browser matrices.
- Keep the full Plan 9.2 scope. Do not call it complete because one batch passed. Do not start Phase 10/11 publication or public uploads without the appropriate user instruction.

## Read first

1. [AGENTS.md](AGENTS.md) — mandatory architecture, unrestricted-study and data-safety rules.
2. [README.md](README.md), [master plan](AI_IMPLEMENTATION_PLAN.md), [definitive remaining-work execution plan](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md) and [Plan 9.2 checklist](docs/plans/PLAN_09_2_COMPLETION.md).
3. [Latest curriculum evidence](docs/PLAN_09_2_CURRICULUM.md), [earlier speaking/recall evidence](docs/PLAN_09_2_SPEAKING.md) and [earlier Plan 9.2 evidence](docs/PLAN_09_2_VERIFICATION.md).
4. The relevant owning phase before editing. For UI changes also follow the design brief, existing Trilingo design system and required skills in AGENTS.md.
5. [Continuation guide](docs/AGENT_CONTINUATION_GUIDE.md) for compact context and the ready queue; [Windows EXE plan](docs/plans/WINDOWS_EXE_SETUP_PLAN.md) or [Android port plan](docs/plans/ANDROID_PORT_PLAN.md) when that platform is requested.

The dated older records describe their own milestones. Current source/files and the latest evidence take precedence over stale historical counts.

## Current authoritative state

- Workspace: C:/Users/Administrator/Documents/Projects/Web Dev Projects/Trilingo.
- Course: [starter.json](content/courses/ja/starter.json), **ja-starter 0.1.21**.
- Source SHA-256: **94b99042f6f6054ac51807ac5482301cd0e4923bd383aaaa3d94b7d8ff5ea9d5**. The source-bound lexical identity file and current review packet match it.
- Schema head: **0013**. This batch changes content, local authoring and frontend navigation; it needs no migration or learner-data rewrite.
- Published technical slice: **2 units, 6 lessons, 30 checks, 8 word records and 5 expressions**. Published lesson/vocabulary definitions were preserved.
- Authored totals: **2,169 word records /2,167 provisional lexical identities**, plus **15 expressions**. Stage A: **541** provisional words; Stage B: **1,626 additional** words. Both separate authoring targets are exceeded; qualified semantic review may change counts.
- There are **236 lessons/3,291 lesson checks**, including **230 draft lessons/3,261 draft lesson checks**, plus **536 standalone checks**. Other inventory: 92 basic kana, 135 variants, 300 contextual kanji (100 A +200 B), 16 guides, 7 writing tasks, 6 stroke templates, 2 stories, 4 passages, 6 dialogues and 2 script-only audio episodes.
- [Current review packet](docs/reviews/ja-starter-0.1.21/inventory.json): **6,848 pending items**. No qualified reviewer is available; no addition was approved/published. Earlier packets are preserved.
- The Git working tree currently contains the project as untracked files; no remote is configured. Preserve it carefully. Do not reset/clean the tree or assume Git has a committed baseline.
- This run used **5192 frontend /8022 backend** and disposable `.tools/remaining-ui-20261025.db`, `.tools/remaining-ui-final-20261025.db` and `.tools/recall-replay-extension-20261025.db` databases. Owned services are stopped; databases/artifacts are retained. The final extension backend22236/frontend22316 stopped by **12:01:13 UTC** using ownership guards. Recheck service ownership before starting/stopping later. No personal launcher, learner database or provider preferences were changed.
- The final writing/grammar batch uses `.tools/writing-grammar-extension-20261025.db`. Its owned backend18668/frontend24828 are stopped by **12:19:59 UTC**; retain that QA database, samples and artifacts. Source0.1.21/schema0013 and the review packet are unchanged.

## What was completed most recently

### Phase 10 / W7 — Local Backup, Restore and Safe Reset (2026-11-08)
- **Consistent SQLite WAL Backup:** Implemented in `backend/app/backup_service.py` using `sqlite3.Connection.backup()`. Produces a completely consistent snapshot containing all tables, indexes, and active WAL entries without partial data. Excludes credentials, transient recordings, and disposable audio cache.
- **Versioned Manifest & Safety Contract:** Every export bundles a validated `manifest.json` declaring `format_version: 1`, `app_name: "Trilingo"`, `schema_version`, SHA-256 database checksum, profile, and an itemized entity summary (total XP, completed sessions, review cards, writing drafts, vocabulary collections, etc.).
- **Point-in-Time Restore with Automatic Pre-Restore Safety Backup:** Restoring validates the zip archive for path traversal, zip bombs (decompression limits), manifest integrity, SQLite integrity checks, and schema version compatibility. Before overwriting the live database, a safety backup is automatically archived in `.data/backups/`. Engine connections are cleanly disposed, `-wal` and `-shm` files unlinked, and the new database is swapped atomically.
- **Safe Reset with Automatic Pre-Reset Safety Backup:** Resetting clears all 20 learner data tables in strict foreign-key order, resets profile and preferences to defaults, and runs `VACUUM` while preserving course units and lesson definitions. Generates a pre-reset safety backup first. Requires explicit confirmation.
- **Accessible Profile UI:** `frontend/src/ProfilePage.tsx` now provides a dedicated "Data safety, backup & reset" card with one-click zip download, file picker with instant snapshot preview (showing date, profile, XP totals, and schema compatibility), confirmation actions, safety backups list, and an accessible confirmation dialog before resetting.
- **Verification:** 6 comprehensive backend regression tests in `backend/tests/test_backup_restore.py` and 2 new frontend tests in `frontend/src/profileBackup.test.tsx` (total 44 frontend tests, 10/10 test files passing). Vite production build passes.

### Area 4 — Local Provider & Audio Verification Status (2026-11-08)
- Host inventory inspected running services, listeners, and installed programs: Docker Desktop v29.8.0 is installed with stopped `docker-desktop` WSL2 engine; LM Studio was uninstalled; local Hugging Face cache contains Qwen3.5 (0.8B, 2B GGUF) and MiniCPM5 (2B GGUF); no standalone Kokoro or Whisper daemon is listening on local ports (1234, 8880, etc.).
- Core application and all learning modes (lessons, grading, XP, FSRS review, stories, dialogues, handwriting) operate 100% reliably with providers disabled (`AI_ENABLED=false`, `TTS_ENABLED=false`, `STT_ENABLED=false`), with honest transcript and typed fallbacks tested and verified.
- Concrete requirements and bounded transfer proposals for setting up Kokoro TTS and Whisper STT are documented.

The latest source-bound additive batch accepts **1,060 Stage B words** from 1,100 contextual candidates, conservatively omitting/reporting 40 spelling/reading/する-family collisions without merging learner IDs. It adds **110 draft lessons, 1,874 lesson checks and 24 standalone particle contrasts** with answer-specific feedback. All original definitions and snapshots remain intact. New code rejects corrupted Unicode/non-kana readings, checks every generated key and guards immutable source/output hashes.

Saved reading now reopens individual characters/words with honest hidden-draft counts and expandable batches. Collection loads/pages/errors are bound to collection/request generations; switching immediately removes old words/actions, including failure/retry and out-of-order-response cases. Focused frontend and backend regressions cover these behaviors and 0.1.20 upgrade preservation of sessions/assistance/XP/FSRS, collection snapshots and writing revisions/receipts. See the run record for exact results and initial corrected failures.

Completed optional recall sessions now offer **Review this card again**, reopening the same saved card/snapshot/direction instead of the unsupported generic replay request. Completion reports self-rated evidence. Browser verification covers keyboard return, future-due review, genuine new timer, exact retry idempotency, three reviews/15XP and skip without schedule/XP mutation across eight layouts. Existing lesson/story/writing/speaking completion behavior is preserved by four focused render regressions.

The final batch binds grammar catalogs/bookmarks to the selected course and draft visibility, hides old guides/scenario actions during loading/failure and adds **Reload grammar**. Drawing recovery separates an earlier confirmed receipt from the current grid result, so a saved old sample cannot remove the unsaved-current-grid warning. Character-scoped receipt selection retains other pending confirmations. Browser evidence covers eight layouts, grammar failure/reload/search/bookmark persistence, targeted correct/skip/finish, three AI-disabled authored scenarios with correct checkpoints/alternatives and pause/resume, current stroke preservation and exact new-activity retry/XP. Earlier receipt lookup earns no XP.

Key files:

- [Current additive manifest](content/authoring/ja/stage-b-expansion-20261025.json) and [accepted/omitted rows](content/authoring/ja/stage-b-expansion-20261025-result.json); the three vocabulary files and particle contrasts are referenced by that manifest.
- [Additive builder](scripts/author_stage_b.py), [lexical decisions](content/courses/ja/lexical-identities.json), existing [review generator](backend/app/content_audit.py) and [new regressions](backend/tests/test_stage_b_expansion.py). The old beginner builder is still archived-0.1.16-specific.
- `frontend/src/SavedReadingItems.tsx`, `collectionMembers.ts`, `VocabularyCollections.tsx`, `ReadingPage.tsx`, their focused regressions and [isolated browser flow](scripts/verify_remaining_work_ui.py).
- `frontend/src/SessionCompletion.tsx`, `ExerciseSession.tsx`, `sessionCompletion.test.tsx`, [recall browser flow](scripts/verify_recall_replay_ui.py) and its [local report](artifacts/recall-replay-extension-20261025/report.json).
- `frontend/src/GrammarPage.tsx`, `HandwritingPage.tsx`, `writingApi.ts`, `writing.test.tsx`, [writing/grammar browser flow](scripts/verify_writing_grammar_ui.py) and [its report](artifacts/writing-grammar-extension-20261025/report.json). Original files/docs: `.tools/remaining-run-20261025-1105/extension2-baseline`.
- [Authoring guide](docs/CONTENT_AUTHORING.md) and [qualified review instructions](docs/JAPANESE_CONTENT_REVIEW.md).

Earlier work already implements durable speaking/text fallback with honest transcript evidence, normal/idempotent XP, capability-aware quests, saved-word/collection recall directions, real FSRS, full timing history and separated skill/workflow statistics. Reuse those implementations. An unchecked plan item may mean broader verification/publication is missing rather than that its feature is absent.

## Remaining work and next useful action

The former 934-word Stage B authoring deficit is closed provisionally: **541 A +1,626 additional B**. Do not keep adding filler to satisfy a count already exceeded. Next work is qualified semantic/language/stroke/audio review and corrections/publication, remaining W2/W3 audits, supported setup and real provider/device verification. Recalculate counts after review; author more only if justified by corrected coverage or missing useful outcomes.

At the next authorized continuation, briefly refresh W0, reuse current evidence and choose a ready W2/W3 gap or available W4 prerequisite. W5/W6 require named qualified-human/device/provider evidence; no draft or fixture substitutes for it. W7/W8 remain after the complete Plan 9.2 handoff, W9/W10 the authorized public launch, and W11 the later C–F curriculum. No full milestone/phase gate was closed by the bounded batch.

For a platform instruction, select EXE-0 or Android A0/A1 as an independent technical feasibility task, then follow that track's gated work packages. These prototypes use synthetic/disposable data and do not waive the Plan9.2/backup/reviewed-release requirements. Windows delivers a full runtime-containing setup `.exe`; Android must run core study locally without the Windows server. No packaging scripts, signed binary, Android project, device build or cross-device backup compatibility has yet been implemented/verified.

The complete remaining checklist stays in Plan 9.2. In particular:

- **B1–B6/C/E:** finish placement/semantic review and full beginner content, then obtain qualified review of keys, alternatives, distractors, guides, narratives and models. Draft authoring is not reviewed publication.
- **A2/A3:** supported Node 24 LTS fresh setup and remaining launch/settings/restart evidence. PATH still uses Node25.2.1/Python3.14, but installed app-embedded Node24.21.0 passed frontend lint/typecheck/41 tests/build and the focused Vite/browser flow with existing dependencies. Reuse its recorded evidence without changing global configuration; a fresh dependency installation and lifecycle-independent normal setup remain unverified. Do not download merely to close a box.
- **D/C4:** qualified stroke review and physical Japanese IME, screen-reader, touch/stylus checks. Scripted composition/screenshots do not prove these.
- **E4/F/G:** actual loaded local model, Japanese Kokoro/TTS, independent Japanese STT, human microphone/listening and real voiced workflows. Adapters/fixtures are implemented, but real-provider verification is outstanding. Earlier Docker probes failed; do not repeatedly probe, reset or replace provider storage.
- **H/I:** remaining collection/navigation, FSRS/history/manual-flow and combined checks must be reconciled against existing evidence. Do not rebuild working services or rerun everything merely because a checkbox remains open.

Only **I6's report artifact** was newly checked off after the final handoff report was verified. It does not mean the full plan or release gate passed. Phase 10 still owns local release/backup/reset/security/performance work; Phase 11 owns the future open-source launch.

## Safe continuation

1. On a new resume request, apply the latest user constraints and any newly stated time allowance; inspect the current source/version before relying on these counts. Do not re-ask settled preferences or inherit expired time windows. Required transfer/destructive/public approvals remain separate.
2. Continue a ready remaining requirement using stable IDs and current services. Preserve unrestricted published access, retries, hints/reveal, skip, finish and normal genuine-session XP. Keep unreviewed material draft.
3. **Content versions are immutable.** If the source remains 0.1.21, changed imported content needs a newer version, ordinarily 0.1.22. Preserve historical IDs/snapshots and review artifacts.
4. The existing beginner builder reconstructs this specific batch from the exact archived **0.1.16** source. Do not blindly rerun/extend it in a way that discards later corrections. Deliberately use the latest verified baseline for the next batch and retain existing lesson boundaries.
5. Regenerate source-bound lexical decisions/review packets without overwriting reviewer edits. 学校/がっこう and 皆さん/みんな count once; older stable IDs remain intact. The additive manifest deliberately omits same-reading candidates pending semantic decisions; omissions do not prove identical meanings or justify silent learner-record merges.
6. Use isolated pytest databases or explicit .tools QA databases, never .data/trilingo.db. No reset or progress deletion without explicit confirmation. Schema changes require migrations; content-only additions ordinarily do not.
7. Run relevant targeted checks, validate/import twice in isolation when content changes, and update evidence/checklists only for proved scope. Broaden checks only for changed behavior, real failures or unresolved risks.

## Verification already available — avoid unnecessary repeats

Current 0.1.21 results and all18 rounds are in [the continuation evidence](docs/PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25). Initial frontend37 tests/12 browser layouts and recall-extension41 tests/eight layouts passed. The final writing/grammar batch passes Node24 lint/typecheck/**42 tests /9 files in1.43s**/build (all native exit codes0) and eight focused layouts, with no overflow/JavaScript errors/external page requests. Build has the existing Lucide warnings and a510.34kB minified-JS warning; no threshold was suppressed. Full backend remains **211 passed /1 expanded-guide fixture failure in676.25s** plus corrected-case recovery (**1 passed in5.59s**) and backend Ruff. Backend production code/contracts are unchanged in the final batch, so that suite is not repeated. All owned QA services are stopped. No further check allowance remains; the following0.1.20 record is historical.

- Full backend run on **0.1.19**: **200 passed, 1 failed** in 374.14s. The failure was a test hard-coding 0.1.17 as a future version. It now increments the actual source patch version; assertions were retained.
- Final affected run on **0.1.20**: **46 passed**, 59.52s. The full suite was not repeated afterward. The existing Starlette/httpx deprecation warning remains.
- Ruff, current content validation, isolated schema/no-drift check and final import/reimport passed.
- Final local browser flow: **8 layouts at 320/390/768/1280px**, no overflow/JavaScript errors/external page requests; new-word search/save, two correct checks, keyboard activation, 5 XP and exact finish retry passed. [Browser report](artifacts/plan-9-2-content/report.json); adjacent screenshots and the smoke script are preserved.
- Frontend source/contracts/dependencies were unchanged in this batch, so lint/typecheck/tests/build were not repeated. Earlier frontend results are in the speaking evidence.
- Logs: .tools/plan-9-2-content-runs. Earlier source/affected-doc baseline: .tools/plan92-content-20261024-0925-baseline. These local directories are not a complete Git backup.

Relevant targeted commands from backend/ (use only when justified by the resumed change):

~~~powershell
..\.venv\Scripts\python.exe -m pytest -q tests/test_beginner_units.py tests/test_content_audit.py tests/test_content.py tests/test_unit_guides.py tests/test_reading_content.py tests/test_speaking.py
..\.venv\Scripts\python.exe -m app.cli validate
..\.venv\Scripts\python.exe -m ruff check app tests migrations
~~~

The ordinary personal launcher is .\scripts\start.ps1 from the root; it migrates/imports without resetting progress. Do not start it just to review this handoff. For isolated QA use scripts/qa_plan92.py with a newly named .tools database. Installed Edge/Playwright can be reused without browser downloads. In the previous session the normal terminal helper failed during setup; a Node execFile fallback worked. Recheck tooling next session rather than repeatedly retrying a broken helper.

## Suggested later resume prompt

> Read AGENTS.md, docs/AGENT_CONTINUATION_GUIDE.md, HANDOFF.md and the owning phase/platform plan. Continue [task ID and concrete deliverable] under the current instruction and any stated time/check bounds. Revalidate current source/evidence, reuse the 0.1.21 proof where applicable, preserve cellular transfer approval and learner data, and keep unreviewed content draft. Do not inherit expired limits or claim full completion while required gates remain open.
