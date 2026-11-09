# Plan 9.2 — speaking and audio recall continuation

Status: this engineering batch is verified; the complete beginner plan remains partial. Authorized window: 2026-10-24 00:32:29–02:32:29 UTC. Implementation and required checks finished before 01:20 UTC, within the allowance. Installed tools and loopback services only; no dependencies, browsers, fonts, containers or models were downloaded, and no web browsing occurred.

## Delivered

- **G3:** Six draft dialogues and two draft episodes now link 16 authored speaking prompts through the shared renderer/session engine. Model/partner reference audio, slow replay/loops, explicit local recording/transcription, retry, skip, typed fallback, pause/resume, finish and replay remain available. Every new completed session uses normal practice XP. Requests bind the current session action/revision to a server-computed media digest; exact retries return the original receipt. Stale actions and changed STT configuration cannot overwrite saved work.
- **G5:** Backend evidence separates speech attempts, transcript agreements and typed fallback from objective correctness. Speaking never produces a pronunciation grade. Speaking quests require STT attempts with delivered model references for every prompt; missing audio, text fallback and skips cannot earn that credit. Same-assignment fallback preserves earlier source events/history and adds no reward. Statistics retain these distinctions.
- **G4 engineering:** Authored situations launch saved speaking sessions. Optional bounded coaching has explicit transient reply transcription and synthetic playback of advisory generated text. Neither operation creates a grade, saved speech evidence, schedule or XP. Real voiced dialogue/coaching verification remains open.
- **H1 / H2 engineering:** Published saved words and collections support meaning, reading, typing, listening and speaking self-rated recall. Media uses each card's original content snapshot, including pronunciation overrides. Existing FSRS states, cards, due dates and logs are reused; preparing, transcribing, revealing and skipping do not schedule or reward. Only an intentional rating commits normal review activity. Japanese references and English meanings retain separate language metadata. Remaining broader saved-character/story navigation audit stays open under H2.

Main implementation files: backend/app/speaking.py, review_media.py, learning.py, learning_schemas.py, grading.py, content_schema.py, content_extensions.py, public_schemas.py, audio_api.py, review.py, review_schemas.py, practice_api.py and reading.py; frontend/src/Recorder.tsx, SpeakingExercise.tsx, ReviewMedia.tsx and the existing session/audio/grammar/recall/schema components. New regressions are in test_speaking.py, test_review_media.py and speaking.test.tsx, with existing scenario, collection, migration and exhaustive grading checks extended.

## Content and data

Current source: **ja-starter 0.1.16**, SHA-256 **b9e99df150f6f37fde7d52405277402426d82ce53679f8192cddcbc532a2e7ed**. The 512 standalone practice definitions include the 16 new draft speaking prompts. Published units/lessons and published vocabulary are unchanged as structured objects: two units, six lessons, thirty exercises, eight word records and five expressions. The lexical inventory remains 285 provisional identities; full 500+1,500 coverage and qualified review remain unfinished.

[The exact-source packet](reviews/ja-starter-0.1.16/inventory.json) contains 1,472 pending review items, the complete source/keys/models/transcripts and copied assets. Earlier packets and reviewer edits are preserved. No material was promoted to reviewed/published.

Migration **0013** versions the additive speaking-evidence JSON contract. It makes no relational schema or data backfill changes: historical JSON/grades/receipts remain untouched, and compatible readers supply zero/null defaults. A populated 0012 forward-upgrade test checks the original stored JSON and receipts byte-for-byte, no XP/review changes, and no Alembic drift. Clean upgrade/import and repeated import also pass.

Trilingo never saves microphone audio. A saved speaking session retains the transcript/comparison and a SHA-256 media digest in its action receipt. Deleting the tab's recording clears local audio, not saved study history. Scenario and recall transcripts remain transient. Local STT services have their own retention/logging settings. Synthetic references/advisory playback use the disposable audio cache, which is separate from learner progress.

All writes used disposable .tools/plan-9-2-speaking-qa.db, .tools/plan-9-2-0013-clean.db or isolated pytest databases. No personal database, launcher, provider configuration or learner records were changed.

## Commands and final results

Backend commands from backend/ using ..\.venv\Scripts\python.exe:

~~~text
-m pytest -q
197 passed; 1 existing Starlette/httpx deprecation warning; 155.72s
-m ruff check app tests migrations
All checks passed
-m app.cli validate
0.1.16; 6 published lessons / 30 exercises / 8 words / 5 expressions
~~~

Targeted checks ran first: speaking/listening/evidence/legacy receipts, then scenario media and collection/FSRS media. The first full run exposed an exhaustive-test assumption that every exercise has a graded key. Its speaking branch now asserts an explicit speech_unassessed error while retaining all existing answer-key assertions. The final full run passes.

Frontend commands from frontend/ using the installed Node executable:

~~~text
node node_modules/typescript/bin/tsc -b --pretty false
PASS
node node_modules/eslint/bin/eslint.js .
PASS
node node_modules/vitest/vitest.mjs run
31 tests passed
node node_modules/vite/bin/vite.js build
PASS; JS 505.14 kB / gzip 145.93 kB
~~~

The build retains two Lucide directive warnings and now crosses Vite's 500 kB chunk warning threshold. No dependency upgrade or speculative bundle refactor was added. Supported Node 24 LTS/fresh-machine setup remains unverified; this machine used existing Node 25.2.1 and Python 3.14.

Isolated migration/import command from root:

~~~text
.venv/Scripts/python.exe scripts/qa_plan92.py --check-only --database .tools/plan-9-2-0013-clean.db
PASS: clean head upgrade, no drift, import new=True, repeat import new=False
~~~

With the isolated QA backend/frontend on 8022/5192, the installed Python with Playwright ran these scripts **sequentially**:

~~~text
python scripts/verify_speaking_ui.py
12 layouts; no browser errors, external requests or horizontal overflow
python scripts/verify_audio_recall_ui.py
12 layouts; no browser errors or horizontal overflow; loopback-only requests
~~~

One initial concurrent browser run saw the other script's legitimate XP in its shared-profile baseline assertion. The unchanged audio-recall script passes when run alone; these mutating scripts must run sequentially. Earlier test/log output remains in .tools/plan-9-2-resume-runs. The previous 124-layout baseline was not rerun.

A provider-disabled core API smoke answered one prompt, skipped the others, finished for **20 XP**, and repeated the finish receipt without extra XP. Health reported schema 0013 and AI/TTS/STT=false. The smoke result is .tools/plan-9-2-resume-runs/core-smoke.json.

## Rendered audit and limits

Actual Edge screens were inspected at 320, 390, 768 and 1280px using the existing Trilingo direction/tokens and ui-ux-pro-max, frontend-design and design-skill guidance already established for this project. Fixed mobile privacy-copy dominance, duplicated speaking metadata and mixed Japanese/English language labels. No competing design system, font or decorative tile grid was introduced.

The local browser flow covered composition-aware Enter, denied microphone recovery, virtual-device local recording/playback/delete, disabled TTS/STT feedback, typed fallback, pause/resume, saved completion, replay, quest fallback, collection direction changes, adjustable batches/Show all, text reveal, self-rating and skip without scheduling. A virtual microphone is not evidence of human Japanese speech. Screens/reports are under artifacts/plan-9-2-speaking and artifacts/plan-9-2-audio-recall; the audit notes are in .design-skill/audit-report.md.

A single local Docker version probe failed: the default Docker pipe was missing and its context configuration was unreadable to this session. No containers/contexts were changed and no image was pulled. Installed Japanese Kokoro/STT/model identity, actual Japanese playback, human listening/microphone, physical Windows IME, screen reader and touch/stylus checks remain unverified. Full linguistic inventory, qualified content/stroke/audio review/publication, supported fresh setup and the remaining Plan 9.2/Phase 10 gates remain open.

Owned QA frontend/backend services are stopped; loopback ports 5192 and 8022 are closed. Only G3, G5 and H1 were newly checked off. Local documentation links resolve. No physical/provider/publication gate was closed.
