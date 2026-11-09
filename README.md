# Trilingo — Personal Japanese Learning

A local-first Japanese study app with original content, English explanations, an openly browsable course path, and durable local settings. All published material is directly accessible; suggested order and goals never limit study.

## Current implementation

Engineering through Phases 4–6 now provides a connected React/FastAPI app, responsive course path, settings, playable lessons, reading and writing tools, strict content validation/import, and thirteen SQLite migrations. The starter practice slice contains **2 published units, 6 lessons, 30 exercises across 5 schema types, 8 core word entries and 5 separately counted expressions**. Source 0.1.21 has **230 draft lessons with 3,261 lesson checks**, seven writing tasks (four Stage A and three Stage B), two stories, four passages and two script-only audio episodes still awaiting qualified review. Internal consistency was checked; independent qualified Japanese-language review remains pending. The [review packet](docs/JAPANESE_CONTENT_REVIEW.md) contains the source keys, models and scripts; no reviewer is currently available.

Lessons now support five exercise types, authoritative grading, saved attempts/pause/resume, honest assisted/skipped evidence, voluntary mistake practice and XP. Each first lesson completion earns 20 XP; each genuine new replay/practice/assessment earns 5 XP, without daily caps. Duplicate requests return their original result. Draft recaps/placement/mastery are explicitly labeled previews with optional support and advisory placement suggestions. Reading now includes 92 basic kana, 135 separate variants/combinations/marks, 300 draft contextual kanji (100 Stage A +200 additional Stage B) and saved-item practice, with adjustable ruby/romaji, full-library word search, freely expandable word batches and two draft stories. Writing includes checked typing, IME-aware draft autosave, preserved conflicts/revisions, unassessed submissions, and formation practice using six original draft templates. New submissions earn normal session XP; autosaves/bookmarks earn none. Optional drawing samples can be kept and deleted; geometric feedback and keyboard alternatives never claim handwriting recognition. Phases 7–9 now add draft grammar/dialogues, local provider adapters and recording/transcript-feedback controls, real backend FSRS, named collections, optional quests/badges/elapsed time, and personal records. Real Japanese audio/STT and qualified content review remain unverified. Development fixtures never save learning records. The full A-B target remains 92 basic kana, 300 distinct contextual kanji and 2,000 unique core words. C-F are later narrative/essay releases, not current coverage.

See [Phases 7–9 verification](docs/PHASE_07_09_VERIFICATION.md), [Phase 6 verification](docs/PHASE_06_VERIFICATION.md), [Phase 5 verification](docs/PHASE_05_VERIFICATION.md), [Phase 4 verification](docs/PHASE_04_VERIFICATION.md), [foundation verification](docs/PHASE_01_03_VERIFICATION.md), [technical decisions](docs/TECHNICAL_DECISIONS.md), [master plan](AI_IMPLEMENTATION_PLAN.md), [curriculum](docs/CURRICULUM_ROADMAP.md), and [design system](design-system/trilingo/MASTER.md). Runtime/clean-install/physical-IME review limits are recorded; an implementation claim does not imply every gate passed.

## Remaining Phase 1–9 work

The latest bounded execution is recorded in [the curriculum continuation](docs/PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25). Read [HANDOFF.md](HANDOFF.md) for current limits and next work; expired time/check allowances do not renew automatically.

The [definitive remaining-work execution plan](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md), created 2026-10-25, is the entry point for the remaining sequence: finish Plan 9.2, verify the safe local release, prepare the public launch, then deliver later C–F releases. It maps dependencies, deliverables, human/device prerequisites and completion evidence to the existing eleven phases. The user authorized a maximum-two-hour execution with ten check/review rounds, then five more and a final three-check/30-minute writing/grammar batch within the original deadline (total18); no transfer or publication is implied.

**Cellular-data rule:** focused web search is allowed. Before any download or upload—including dependencies, models, Git transfers, reviewer files or release/social assets—ask for approval with the estimated total network size and exact scope. Use installed/local resources first; no automatic transfer or retry is authorized.

[Plan 9.2](docs/plans/PLAN_09_2_COMPLETION.md) collects the remaining supported-setup, beginner-content review/expansion, reading/writing/grammar/audio/review features and real-provider/device checks before Phase 10. Source **0.1.21** adds **1,060 provisional Stage B words, 110 draft lessons, 1,874 lesson checks and 24 particle contrasts**. The inventory now has **2,169 word records / 2,167 provisional lexical identities (541 A +1,626 additional B)**, plus 15 expressions. Both separate authoring targets are exceeded; qualified semantic review may change these counts. **6,848 items await qualified review** and no new material was published. Supported fresh setup, real-device/provider gates and broader audits remain open. Earlier [engineering evidence](docs/PLAN_09_2_VERIFICATION.md) and [speaking/recall evidence](docs/PLAN_09_2_SPEAKING.md) retain their recorded scope.

Saved reading now offers named links to individual saved characters and words, with adjustable batches and honest hidden-draft counts. Vocabulary collections clear stale words during selection/loading/failure and bind responses to their collection/request, so old word controls cannot act on a newly selected collection. Restart the normal launcher to import current content without resetting progress; this execution uses only isolated QA data.

The authorized five-check extension fixes completed recall replay: **Review this card again** reopens the same saved card for freely available early review, and completion labels its evidence as self-rated. Existing installed dependencies pass lint, typecheck, **41 frontend tests** and production build on an already installed app-embedded **Node24.21.0** runtime; a fresh independent setup remains unverified. The full current-source backend run reports **211 passes /1 fixture failure**; its focused correction and final recovery are recorded in the continuation evidence rather than claiming a repeated fully green suite. No learner-data/schema changes or external transfers occurred.

The final writing/grammar batch removes stale guide/scenario controls during view changes or failed loads and adds **Reload grammar**. Confirming an earlier drawing receipt now leaves the current unsaved grid and its leave warning intact. Node24 lint/typecheck/**42 tests**/build pass; eight rendered layouts, three AI-disabled authored dialogues, bookmark recovery and real drawing-receipt/reward checks pass in isolated QA. Qualified content/device/provider and full release gates remain open.

## Open-source release and launch plan

For future agents, [the continuation guide](docs/AGENT_CONTINUATION_GUIDE.md) provides the current baseline, evidence limits, next-work queue and copyable resume prompt. The user additionally requested a [Windows `.exe` setup plan](docs/plans/WINDOWS_EXE_SETUP_PLAN.md) and confirmed a [standalone offline Android port](docs/plans/ANDROID_PORT_PLAN.md). The Windows proposal bundles the runtime and production UI in a per-user full installer; Android reuses the UI with a device-local learning engine and persistent store. Both are **planned, not implemented**. Technical feasibility can proceed alongside content review; full releases retain the content, data-safety and platform-verification gates. No packaging tool, SDK, installer, APK or model was downloaded or built for this documentation update.

[Phase 11](docs/plans/PHASE_11_OPEN_SOURCE_LAUNCH.md) plans GitHub publication with code/content licensing, contributor guidance, CI and a verified release, followed by tailored LinkedIn, Reddit and X posts and a short feedback campaign. It is planned work; no public repository or campaign is claimed. Phases 1–10 retain their app/content and local-release gates.

## Run on this computer

Dependencies are already present. From the project root in PowerShell:

~~~powershell
.\scripts\start.ps1
~~~

This migrates SQLite, imports the versioned starter without resetting data, starts both services, and opens http://127.0.0.1:5173. If the preview is already running, stop its launcher with Ctrl+C and run it again to load new backend routes/migrations. Keep the terminal open; Ctrl+C stops the owned services. Use -SkipOpen to omit browser opening. Logs are in .data/. Startup does not install dependencies or download content/models/fonts.

The supported target is **Node 24 LTS, Python 3.11+**. This computer uses Python3.14.0 and PATH Node25.2.1. Existing dependencies also pass lint/typecheck/tests/build and isolated Vite/browser flows with an already installed app-embedded Node24.21.0 runtime; a fresh independent Node24 dependency installation and normal setup remain unverified. Native Windows is the default; Docker is not required.

## Fresh setup

These install commands download dependencies. On a metered connection, wait for Wi-Fi or use a complete local cache; do not repeatedly retry an offline cache miss.

~~~powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements.lock
Set-Location frontend
npm ci --no-audit --no-fund
Set-Location ..
.\scripts\start.ps1
~~~

If Python is not on PATH on this computer, its inspected executable is:

~~~powershell
& 'C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe' -m venv .venv
~~~

The Python lock pins the tested environment; frontend versions are exact and package-lock.json is checked. An offline npm-ci dry run passed; a complete fresh frontend dependency installation has not been re-run within the cellular allowance. No global runtimes/packages were changed.

## Configuration and manual startup

Copy .env.example to .env only when overriding defaults. Relative DATABASE_URL paths resolve against the project root; the default personal DB is .data/trilingo.db. HOST/PORT default to127.0.0.1:8000. CORS_ORIGINS is a JSON array of explicit local frontend origins. QA_MODE defaults false and cannot use the default personal database.

In separate PowerShell terminals:

~~~powershell
Set-Location backend
..\.venv\Scripts\python.exe -m alembic upgrade head
..\.venv\Scripts\python.exe -m app.cli import
..\.venv\Scripts\python.exe -m app
~~~

~~~powershell
Set-Location frontend
# Set this when the backend uses another port:
$env:VITE_API_BASE_URL='http://127.0.0.1:8000/api/v1'
npm run dev
~~~

Frontend port 5173 is fixed to detect conflicts. Set VITE_API_BASE_URL explicitly when using a different backend port. The API's OpenAPI UI is at http://127.0.0.1:8000/docs and health at /api/v1/health. Published course access does not require enrollment or a profile score.

The profile uses the browser's detected IANA timezone on first setup; Asia/Singapore is offered. An API-only first connection without a zone uses UTC. Settings persist in SQLite; important state is not stored only in localStorage.

AI_ENABLED/TTS_ENABLED/STT_ENABLED default false. Provider name, local base URL, model, voice and timeout preferences are saved through Profile; local adapters are implemented but health does not claim provider availability. Enable both the server gate and the provider in Profile before explicitly requesting a call. Core learning and real FSRS work with all providers disabled. Authored browsing/settings work without external internet while the local backend runs.

## Content and migrations

From backend/:

~~~powershell
..\.venv\Scripts\python.exe -m app.cli validate
..\.venv\Scripts\python.exe -m app.cli import
~~~

An optional file argument selects another validated course JSON. Imports are idempotent. Increment the semantic content version before changing published content; old snapshots and assistance references are retained. Re-importing an older existing snapshot does not roll back the current version. Schema changes require a reviewed Alembic migration. Runtime does not create tables automatically.

[Content format and review](docs/CONTENT_AUTHORING.md) explains publication, answer policy, lexical counting and later-mode contracts. Ordinary lesson responses exclude keys/hints/explanations. Explicit hint/reveal records assisted evidence, without claiming correctness or limiting access.

## Backup, restore and data safety

Trilingo stores all durable learning records locally on your computer in SQLite (`.data/trilingo.db`). A complete, consistent backup can be exported at any time from the **Profile** page or via the API (`/api/v1/backup/export`).

- **Consistent SQLite WAL backup:** Backups use SQLite's native backup API to create a clean, consistent snapshot of the active database, including any pending WAL pages.
- **What is included:** Profile settings, study sessions, exercise attempts, XP ledger, review cards, FSRS states, writing drafts, revisions, character drawing samples, vocabulary collections, and badges. Credentials, transient recordings, and regenerable audio caches are excluded.
- **Point-in-time restore:** Restoring replaces local learning progress with a selected backup archive (`.zip`). The Profile page provides a validated preview showing snapshot timestamp, profile name, XP summary, and schema compatibility before you confirm.
- **Automatic safety backups:** Before any restore or reset operation, Trilingo automatically saves a safety backup of your current database to `.data/backups/`.
- **Safe reset:** Reset clears learner progress while leaving installed course units and lesson definitions completely intact, accompanied by mandatory confirmation and an automatic safety backup.

## Validation

Frontend, from frontend/:

~~~powershell
npm run lint
npm run typecheck
npm run test -- --run
npm run build
~~~

Backend, from backend/:

~~~powershell
..\.venv\Scripts\python.exe -m pytest -q
..\.venv\Scripts\python.exe -m ruff check app migrations tests
..\.venv\Scripts\python.exe -m app.cli validate
~~~

Tests create isolated temporary migrated databases. If Windows denies access to its shared pytest temporary directory, use `python -m pytest -q --basetemp=../.tools/pytest-check -o cache_dir=../.tools/pytest-cache` from backend/. That named test directory is disposable; never point it at personal data. To check migration drift manually, use a disposable DB explicitly, never the personal DB:

~~~powershell
$env:DATABASE_URL='sqlite:///.data/migration-check.db'
..\.venv\Scripts\python.exe -m alembic upgrade head
..\.venv\Scripts\python.exe -m alembic check
Remove-Item Env:DATABASE_URL
~~~

Browser checks require the already installed Python Playwright package/browser; they do not install one. Start an isolated QA instance from the root:

~~~powershell
$env:QA_MODE='true'
$env:DATABASE_URL='sqlite:///.data/browser-qa.db'
$env:PORT='8002'
.\scripts\start.ps1 -SkipOpen
~~~

In another terminal, run the browser script with a Python that already has Playwright:

~~~powershell
python scripts/verify_ui.py
~~~

Set TRILINGO_QA_API_BASE_URL if changing the QA API origin. The test refuses a non-QA backend and blocks mismatched API origins and external requests. It changes only the designated QA profile/preferences. Screenshots/results go to ignored artifacts/. Stop QA and remove the environment overrides before starting personal use.

## Troubleshooting and boundaries

- Connection error: start the backend and retry. A missing-schema error means run migrations; do not reset data.
- Port conflict: stop the service using that port or choose a backend PORT and matching frontend API URL.
- Invalid content/version conflict: read the validation location or increment the content version; do not overwrite historical records.
- Preference failure: input stays on screen; correct the named field or retry the local connection.
- Kokoro: both inspected Docker engine pipes are unreachable; image/wrapper/voice/playback are unverified. No models or containers were installed/started.
- Physical Japanese IME, a screen reader and a supported-LTS runtime still need human/device verification. Automated composition events and accessible DOM checks do not certify them.

Learning is unrestricted: no hearts, cooldowns, prerequisite locks, mandatory assessments, daily limits, XP ceilings or paid/earned access. Future new genuine sessions can earn normal XP; duplicate deliveries will stay idempotent. Social leaderboards and fabricated peers are outside the personal scope. All assets/course text are original; content attribution is stored with the course.


## Review the new reading/writing tools

After restarting the personal launcher, open Practice > Reading or Writing. Enable the visibly labeled draft controls to inspect unreviewed material. Formation lives under Writing > Character formation. Saved compositions retain both texts on a conflict; raw drawing samples are optional. The [Windows input guide](docs/WINDOWS_JAPANESE_INPUT.md) was checked against Microsoft documentation on 2026-10-23; physical IME verification remains open.

Additional isolated browser commands from the root:

~~~powershell
$env:TRILINGO_QA_BROWSER_CHANNEL='msedge' # already installed Edge; omit for an existing Playwright cache
python scripts/verify_study_ui.py
python scripts/verify_reading_ui.py
python scripts/verify_writing_ui.py
~~~

These scripts default to the separate QA frontend 5184/backend 8014 and refuse non-QA/mismatched/external targets. They do not install a browser. Do not run them against the personal profile. The final combined run checked 104 layouts (56 lesson, 24 reading, 24 writing). Physical IME, touch/stylus, screen-reader and qualified Japanese/stroke review remain open.

## Review grammar, audio engineering and FSRS

Restart the launcher after updating so it applies migrations 0006–0012 and imports content 0.1.15 without resetting progress. Practice now offers grammar/dialogues, audio, and recall/quests. New scenarios and particle guides require the explicit draft toggle. Add any published word to recall or import saved mistakes; cards remain unscheduled until an intentional self-rating. Review a future-due card whenever you wish. Named vocabulary collections preserve their original word snapshot.

Provider settings use local URLs only. AI accepts provider names lm-studio/openai-compatible; TTS uses kokoro with a listed Japanese jf_/jm_ voice and explicit model/version; STT accepts a separate openai-compatible Japanese service. Set the matching AI_ENABLED/TTS_ENABLED/STT_ENABLED server flag and enable that provider in Profile. Trilingo downloads no model and never sends audio to a cloud URL. Requests have a 10-second safety ceiling; load/configure the local model first. The installed Kokoro wrapper and an independent STT version still need real verification. Adapter references: [LM Studio chat endpoint](https://lmstudio.ai/docs/developer/openai-compat/chat-completions), [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI).

Audio is prepared on demand, with native play/replay and slow/loop controls. Recordings stay in the tab until explicitly saved or sent to configured local STT; deleting/closing removes the tab copy. Check the provider's own logging/retention policy. The disposable synthetic cache defaults to .data/audio-cache (AUDIO_CACHE_DIR); recording data is not retained by the backend. Transcript comparison is not pronunciation or pitch-accent assessment.

Additional isolated browser check (uses existing Edge by default, accepts --browser):

~~~powershell
python scripts/verify_phase789_ui.py --base http://127.0.0.1:5187 --api http://127.0.0.1:8017/api/v1
~~~

Start a separate QA instance at those ports first; the script refuses a non-QA API and blocks external requests. See the verification record for current evidence and unfinished phase gates.

The draft audio episodes now offer focused listening selection, dictation and register contrasts through the shared exercise engine. Transcripts stay hidden until explicitly requested; text fallback remains freely available and records assistance. A prepared reference records delivery, not proof that it was heard. Each new completed session uses normal practice XP; retries do not duplicate rewards.

Recall offers an optional server-recorded timer with pause/resume/hide. Only a deliberate Again/Hard/Good/Easy rating commits a timed review, schedule, log and normal XP together. Skipping/browsing changes no schedule. Recent valid timing records and a 12-week activity calendar are hideable. A gentle in-page reminder preference is available; it does not schedule OS notifications. Unfinished listening quests can switch to core sessions under the same assignment ID, preserving prior genuine evidence without extra XP.

Optional scenario coaching uses the selected authored situation and bounded strict model output. Disabled/unavailable/incompatible AI returns the authored prompt; generated coaching is unverified, transient, and never grades or changes learning records. See [the additional-hour verification](docs/PHASE_07_09_FOLLOWUP.md) for exact scope and remaining release gates.

Additional installed-browser checks use the isolated QA ports above:

~~~powershell
python scripts/verify_listening_ui.py
python scripts/verify_recall_timing_ui.py
python scripts/verify_recording_ui.py
~~~

The listening success-control check requires the documented disposable local test-tone fixture. Test tones and simulated microphone devices do not verify Japanese speech. Never point QA scripts at the learner database.


## Plan 9.2 changes and isolated verification

Recall now opens a selected vocabulary collection in meaning/reading/typed self-rated directions while retaining the saved content and any existing schedule. Preparing/browsing/skipping a card changes no XP or schedule. Timed session history supports all saved records, activity filters, adjustable pages and First/Previous/Next/Last. New timers retain active and paused duration; older pause durations are labeled unknown. Skill checks, self-rated reviews, unassessed workflows and published coverage are separate records.

Grammar has sixteen unreviewed draft guides across the ten beginner topics. The source now contains 120 draft lessons with 1,387 checks, available through explicit draft guides and related saved-word practice. They are not a full beginner course or reviewed publication. The source-bound audit reports 1,107 provisional lexical identities from 1,109 word records; the complete 500+1,500 authoring/review target remains open. See [review packet](docs/JAPANESE_CONTENT_REVIEW.md) and [run evidence](docs/PLAN_09_2_VERIFICATION.md). Migration 0012 adds a history index without rewriting old receipts or progress. Restart the personal launcher normally to apply it; this run used only disposable QA databases.

Installed-tool QA from the root:

~~~powershell
.\.venv\Scripts\python.exe scripts/qa_plan92.py
# In a separate frontend terminal:
$env:VITE_API_BASE_URL='http://127.0.0.1:8022/api/v1'
node node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5192 --strictPort
# Using the installed Python with Playwright, from root:
python scripts/verify_plan92_ui.py
~~~

The QA launcher accepts --check-only and --database .tools/name.db for a clean migration/import check, rejects paths outside .tools, and disables every provider gate. The browser script uses installed Edge and blocks external/mismatched origins. Neither command installs a browser, runtime or model. Prior-window commands/results and 124 checked layouts are in that record; current continuation scope and remaining physical/provider checks are recorded below.

## Saved speaking practice

With source 0.1.16 imported, Grammar's draft situations offer **Practice spoken responses**; Audio also lists the eight draft speaking sessions. Six dialogue situations and two episodes provide 16 prompts, model/partner audio, slow replay/loops, local recording, explicit transcript feedback, typed practice, retry, skip, pause/resume, finish and new replays. Every genuinely completed session earns normal practice XP; duplicate requests do not add attempts or rewards. Transcript comparison never assesses pronunciation or pitch accent.

Speaking quests require successful STT attempts with delivered model references for every prompt. Typed fallback, missing audio or a recorded skip prevents speaking-specific credit. An unfinished listening or speaking quest can switch to core sessions while keeping its assignment/history and prior credit. Skill records distinguish speech attempts, transcript agreements and typed fallbacks from objective grades and self-rated recall.

The backend retains recognized text and comparison in saved speaking history, plus a SHA-256 media digest in its action receipt; it never retains the microphone recording. Deleting the tab's recording removes its local audio copy and leaves saved history intact. The local recognition service has its own logging/retention settings. Optional scenario coaching can explicitly transcribe a reply and play a bounded generated response; those transcripts stay transient and earn no study evidence, grades or XP. Synthetic advisory audio uses the disposable audio cache, whose deletion never affects learning history.

Migration 0013 records the additive evidence contract without rewriting past JSON, grades, receipts or FSRS state. Use the normal launcher to apply migrations/import the new content. Real Japanese TTS, human microphone/STT, teaching-audio review and qualified publication remain unverified. [Current continuation evidence](docs/PLAN_09_2_SPEAKING.md) records the exact scope and checks. With the isolated QA runner above, use the installed browser Python to run python scripts/verify_speaking_ui.py; its virtual microphone is a control check, not real speech verification.

Saved-word and collection recall also offer **Audio → meaning** and **Meaning → Japanese speaking**, alongside meaning/reading/typing. These remain self-rated FSRS directions. Audio and transient transcript feedback use the card's original content snapshot and never change its schedule or earn speech evidence. Reveal text and skip remain available with providers off. Only Again/Hard/Good/Easy saves a rating and normal review XP. For the focused provider-disabled browser check, run python scripts/verify_audio_recall_ui.py against the same isolated QA instance. Run mutating browser scripts one at a time because they share the disposable local profile.

## License & Attribution

- **Source Code:** Licensed under the [MIT License](LICENSE). Copyright (c) 2026 Justin Reyes.
- **Educational Curriculum & Content:** All Japanese course definitions, vocabulary lists, grammar guides, and lesson data under `content/` are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

