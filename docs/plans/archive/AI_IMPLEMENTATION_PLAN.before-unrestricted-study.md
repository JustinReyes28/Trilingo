# Trilingo — Ten-Phase Japanese Implementation Plan

This is the active execution contract for the project. Read [AGENTS.md](AGENTS.md), this file, [README.md](README.md), and the current phase before editing code.

The user requested both Duolingo-style interface/learning features and Babbel-style learning features for personal Japanese reading, writing, and speaking. The user confirmed a beginner starting point, a staged path through complex essays, and personal quests/badges/challenges/bests. English explanations are the initial teaching language.

The former 24-phase plan is preserved verbatim in [the archive](docs/plans/archive/AI_IMPLEMENTATION_PLAN.original.md). It is historical reference. This ten-phase sequence replaces its phase numbering and priorities; AGENTS.md remains mandatory.

## 1. Current implementation status

Inspection date: 2026-10-22.

- Existing before this planning task: AGENTS.md and the original master plan only.
- Added by this task: ten phase documents, this updated master, README, and the archived original plan.
- Missing: application code, manifests/lockfiles, runnable frontend/backend, course files, database, migration history, and application tests.
- Broken/partial app functionality: none can be assessed because there is no app yet.
- Source-control status: `git status --short` reported that this directory is not a Git repository.
- TTS status: the user identified the existing service as Kokoro TTS. Upstream Kokoro documents Japanese support; the installed wrapper/version, Japanese voice/dependencies, endpoint, and local playback still require verification. Docker's engine was unreachable during the earlier inspection; details and checks are in Phase 8.
- Next implementation task: Phase 1 foundation. Creating these documents does not complete any implementation phase.
- Learning scope: first release covers beginner Stages A-B; intermediate/advanced Stages C-F are approved later releases in the curriculum roadmap. They are not authored or implemented yet.

## 2. Product definition and boundaries

Build a local-first Windows application for one personal learner. The main learning loop is: learn a small concept, use it in context, produce an answer, receive clear feedback, then revisit it through scheduled practice.

The interface and feature set include a course path, themed units, large lesson nodes, short exercises, hearts, XP, streaks, quests, stories, mastery challenges, and a practice hub. Use original Trilingo branding, artwork, wording, sounds, and course content. This roadmap combines both products' useful learning mechanics rather than limiting Duolingo inspiration to visual design.

The learning experience includes contextual grammar notes, original practical dialogues, recaps, vocabulary collections, multiple review modes, Japanese listening, and supported speaking practice. These broad ideas were checked against [Babbel's course overview](https://support.babbel.com/hc/en-gb/articles/205600448-Babbel-courses) and [review modes](https://support.babbel.com/hc/en-us/articles/205600228-Vocab-workout-Review) on 2026-10-22. They are references for our feature choices, not imported content or a claim that Babbel supplies a Japanese course.

Japanese priorities:

- Read hiragana and katakana, then useful kanji words and short everyday passages.
- Write through Japanese typing/IME and guided kana/kanji handwriting, with distinct evidence for each.
- Speak through shadowing, microphone recording/playback, Japanese STT transcript feedback, and authored practical dialogues.
- Learn grammar, vocabulary, register, and cultural usage together; English explanations and adjustable furigana/romaji support the beginner.
- Use actual FSRS review with preserved history; do not treat recognition as proof of productive recall.

### Learning coverage and staged releases

The [curriculum roadmap](docs/CURRICULUM_ROADMAP.md) now defines the approved progression: A — script/first sentences; B — everyday messages/guided paragraphs; C — connected paragraphs/narratives; D — multi-paragraph opinions/arguments; E — extended essays/formal register; F — complex essays/source synthesis.

The first personal release remains Stages A-B with the ten beginner units and guided short writing. Intermediate and advanced releases must add reviewed language instruction, reading/listening/speaking tasks, and draft/revision/rubric tools alongside longer writing. An essay editor or AI prompt alone cannot complete that scope. Publication, practice completion, and reviewed proficiency evidence are tracked separately.

The user wants a substantial starter inventory: Stage A targets 92 basic kana plus common variants/combinations, 100 kanji, and 500 unique words; Stage B adds 200 kanji and 1,500 unique words, for 300 kanji and 2,000 words cumulatively. Follow the curriculum's deduplication/context rules and expand the topic outlines into enough lessons. These are planned authoring targets, not current content or memorization gates. The small first playable slice remains valid as explicitly partial coverage.

Keep exactly ten software phase files. Their initial completion tracking refers to the beginner release; later stages reapply the relevant content, writing, feedback, persistence, and release gates against their declared release scope. They do not become complete automatically when the beginner app launches. JLPT tags cannot substitute for writing/speaking assessment; see the [official JLPT FAQ](https://www.jlpt.jp/e/faq/index.html).

### Required design workflow

Apply `ui-ux-pro-max`, `frontend-design`, and `design-skill` to relevant UI work, following the persistent rule in [AGENTS.md](AGENTS.md) and the [design brief](docs/DESIGN_BRIEF.md). Record a product-specific direction, verify any search result before persisting it, then inspect and improve actual rendered screens. Phase 2 establishes the design system; every UI phase checks it, and Phase 10 audits it. No UI exists yet, so visual audits remain pending.

Initial assumptions that remain editable: one local profile, a suggested 20 XP daily goal, a short lesson plus due review per day, and system-detected timezone with Asia/Singapore available for this computer. No fluency deadline, complete JLPT coverage, specialized pronunciation score, or handwriting-recognition capability is promised.

Public friends, shared leagues/leaderboards, and friend streaks are outside the confirmed personal scope. Use weekly personal bests drawn from the learner's own history; do not fabricate competing users. Purchases, subscriptions, live tutors, broad multilingual course catalogs, and a generic chatbot are also outside the initial release. The generic engine and data model must still avoid hard-coding a specific course/profile into core logic.

### Duolingo-inspired personal features and phase ownership

These are explicit planned features, not a claim of full commercial-product parity:

- Course path, lesson nodes, unit guides, and a dedicated practice hub: Phases 2-4; live practice filters in Phase 9.
- Short mixed exercises, instant committed feedback, mistakes, lesson replay, hearts/recovery, XP, levels, achievements, streaks, and daily goals: Phases 4 and 9.
- Optional placement/jump-ahead checks, required unit recap checkpoints, and optional harder no-hint mastery challenges: Phase 4, using reviewed assessment content from Phase 3.
- Original short interactive stories with comprehension, vocabulary, and replay: Phase 5; listen-along story/mini audio episodes and focused speaking/listening sessions: Phase 8.
- Personal daily quests, monthly challenge badges, optional streak protection, earned cosmetic rewards, weekly personal bests, and optional timed matching/recall challenges: Phase 9.
- Personal practice selection based on actual errors/skill evidence: Phase 9; local in-app reminders and an optional permission-based notification mechanism: Phase 10.
- Contextual answer explanations and optional local AI roleplay: Phase 7, voiced in Phase 8. Core progression stays independent of AI.

Duolingo's [practice feature overview](https://blog.duolingo.com/ways-to-practice-in-duolingo/) documents stories, harder mastery-style challenges, targeted practice, timed activities, and AI conversation. Its [quest overview](https://blog.duolingo.com/time-spent-learning-well/) describes daily and monthly challenges. These sources were checked on 2026-10-22; Trilingo's exact rules, names, content, and rewards are defined in its own phase files.

### Babbel-inspired learning features and phase ownership

- Structured beginner units, practical learning objectives, short lessons, vocabulary/grammar in context, and unit recaps: Phases 3, 4, and 7.
- Searchable grammar guides, authored explanations, everyday scenarios, cultural/register notes, and guided conversations: Phase 7; real Japanese reference audio and speaking practice: Phase 8.
- Flashcard, typed-writing, listening, and speaking review, personal vocabulary collections, and personalized due practice: Phases 7-9, using actual FSRS for scheduling.
- Optional explanation/roleplay assistance, with authored fallback and no AI grading of core exercises: Phase 7.

See Babbel's [Grammar Guide](https://support.babbel.com/hc/en-us/articles/19260489559058-Grammar-guide) and [Guided Conversations](https://support.babbel.com/hc/en-gb/articles/19188554247186-Guided-Conversations) for the broad feature concepts. This is original Japanese content; product feature availability in another language does not supply a Japanese course for this project.

## 3. Architecture and authority

- Frontend: React, strict TypeScript, Vite, Tailwind CSS, Zod, and lightweight routing.
- Backend: Python 3.11+, FastAPI, Pydantic, SQLAlchemy, Alembic.
- Persistence: migration-controlled SQLite. Do not keep important learning state only in localStorage.
- Scheduling: real FSRS in the backend using a maintained implementation selected and pinned during foundation work. Persist library-required state, parameters/version, due dates, and immutable logs. No browser-authoritative schedule submissions.
- Optional explanations: disabled provider plus LM Studio/generic OpenAI-compatible adapters. AI cannot grade normal exercises or award progress.
- Audio: prefer the user's existing Kokoro TTS through an adapter after local verification. [Upstream Kokoro](https://github.com/hexgrad/kokoro) documents Japanese `lang_code='j'` and `misaki[ja]`; confirm the installed wrapper and available Japanese voice. STT is an independent provider; audio endpoints need not be OpenAI-compatible.
- Configuration: one backend settings source, validated frontend API configuration, `.env.example`, and no committed secrets. Use a supported Node LTS compatible with the chosen Vite version; do not assume the observed Node 25 installation is the support target.
- Local operation: frontend/backend run natively on Windows; Docker is optional for provider services. Authored lessons work without external internet after installation while the local backend is running. Browser-only offline operation/sync is a separately gated extension.

Use content -> generic learning engine -> reusable exercise renderer -> authoritative progress/review. All new exercise types require a validated discriminated schema, dedicated renderer, server policy where graded, and meaningful tests.

The backend owns grades, eligibility, XP ledger, hearts, unlocks, streaks, achievements, and FSRS. The client supplies answers, identifiers, and explicitly supported learner ratings. A client-provided correctness flag, XP amount, due date, or mastery claim is never authoritative.

Use `/api/v1` consistently, thin routes, typed public schemas, explicit error codes, UTC event/due timestamps, preserved profile-local activity dates, transactions, and idempotency. Changes to persistent schema require migrations and clean-DB verification. Content must be original, versioned, validated, and separate from UI code.

## 4. Ten phase files and implementation tracking

Each phase file includes goal, actionable tasks, intended implementation areas, data/API contracts, tests/manual checks, and completion criteria. All checkboxes below refer to implementation, not drafting.

1. [Phase 01 — Foundation and technical decisions](docs/plans/PHASE_01_FOUNDATION.md): audit, Windows setup, frontend/backend skeleton, configuration, initial DB migration, contracts, isolated tests, and early provider discovery.
   - [ ] Verified implementation complete.
2. [Phase 02 — Interface and design system](docs/plans/PHASE_02_INTERFACE.md): required UI/UX skills, original visual direction/tokens, responsive navigation/path shell, reusable controls, accessible states, and rendered design review.
   - [ ] Verified implementation complete.
3. [Phase 03 — Japanese curriculum and content model](docs/plans/PHASE_03_CURRICULUM.md): staged curriculum metadata, first-release beginner syllabus, versioned schemas/APIs/seeds, and reviewed content inventory.
   - [ ] Verified implementation complete.
4. [Phase 04 — Lesson engine and progression](docs/plans/PHASE_04_LESSON_ENGINE.md): reusable exercises, attempts/resume, server grades, game rules, unlocks, placement, unit checkpoints, and mastery challenges.
   - [ ] Verified implementation complete.
5. [Phase 05 — Kana, kanji, and reading](docs/plans/PHASE_05_READING.md): script libraries, contextual readings, aids, passages, original interactive stories, and reading evidence.
   - [ ] Verified implementation complete.
6. [Phase 06 — Typing and handwriting](docs/plans/PHASE_06_WRITING.md): IME, guided handwriting, beginner draft saving/guided paragraphs, and later staged writing workshops with revision/rubric evidence.
   - [ ] Verified implementation complete.
7. [Phase 07 — Grammar and practical dialogues](docs/plans/PHASE_07_GRAMMAR_DIALOGUES.md): unit guides, branching situations, recaps/collections, optional explanation adapters.
   - [ ] Verified implementation complete.
8. [Phase 08 — Japanese audio and speaking](docs/plans/PHASE_08_AUDIO_SPEAKING.md): Kokoro Japanese setup/verification, listening/audio stories, recording, Japanese STT, shadowing, privacy/fallbacks.
   - [ ] Verified implementation complete, including real-provider checks.
9. [Phase 09 — Review, quests, and personal progress](docs/plans/PHASE_09_REVIEW_PROGRESS.md): FSRS, practice modes, daily/monthly quests, streak protection, cosmetic rewards, timed challenges, levels, badges, personal bests, and truthful stats.
   - [ ] Verified implementation complete.
10. [Phase 10 — Reliability, backup, and local release](docs/plans/PHASE_10_RELEASE.md): audited course/features, safe backup/restore, local reminders, security/performance, Windows launch, full regression and manual release flow.
    - [ ] Verified implementation complete.

Follow the numbered sequence for the main implementation. TTS discovery may run in Phase 1. Tests, accessibility, migrations, and data safety belong in every phase; Phase 10 verifies them comprehensively. Dependencies refer to needed contracts/features. If optional hardware/providers cannot be exercised, record that phase as partial and continue independent work; do not let it imply the final speaking release gate is satisfied.

## 5. Milestones and acceptance

### First playable slice — through Phase 4

- [ ] Real frontend/backend launch with AI/audio disabled.
- [ ] First original Japanese slice has at least two units, three lessons per unit, five useful exercises per lesson, and at least three supported types; the engine supports the four core text types plus matching.
- [ ] New learner can start, make/correct a mistake, lose a heart, finish, earn XP once, and unlock the next lesson.
- [ ] Refresh/restart preserves attempts and learning state; direct API manipulation cannot bypass rules.
- [ ] Basic mistakes/practice work but are not labeled FSRS before Phase 9.
- [ ] Unit checkpoints, optional placement, and optional mastery use server-graded attempts with distinct placement/completion evidence and no double rewards.

### Japanese skills feature set — through Phase 9

- [ ] Kana and reviewed beginner kanji/passages can be read with adjustable aids.
- [ ] IME input and guided handwriting practice work with truthful evidence labels.
- [ ] Stage A character/word/first-sentence tasks and at least three Stage B guided compositions, reviewed models/alternatives, a simple revision example, persisted drafts, and self-review work without AI. Open writing is not graded as an exact-string answer; C-F have their own task/rubric/workshop gates.
- [ ] Original grammar guides and everyday dialogues are usable without AI.
- [ ] Real Japanese TTS and STT/microphone paths are verified on the target computer; listening and speaking failures have usable fallbacks.
- [ ] Actual FSRS persists ratings, states, due dates, and history; skill evidence and stats are based on stored data.
- [ ] Stories/audio stories, daily quests/monthly badges, timed and untimed practice, optional streak protection, cosmetic rewards, and weekly personal bests work with persisted server-validated state.

### Personal release — Phase 10

- [ ] Published beginner course inventory matches what the app claims.
- [ ] Full A-B inventory reaches 92 basic kana with taught patterns, 300 distinct contextual kanji, and 2,000 unique reviewed core word entries; smaller beta/technical slices disclose their partial counts and do not claim full coverage.
- [ ] Both quality gates, clean migrations, API smoke, manual critical flow, accessible/mobile checks, local restart, and backup/restore round trip pass.
- [ ] README launch/update/provider/troubleshooting instructions are tested.
- [ ] Reminder controls, the combined personal feature inventory, and backup coverage of quests/rewards/protection are verified; no social results are fabricated.
- [ ] UI skill workflow, shared design decisions, representative screenshots, keyboard/IME checks, and resolved major visual/interaction findings are recorded; first-release claims stay within published Stages A-B.
- [ ] Every limitation is recorded; unchecked required gates keep the release incomplete.

### Later intermediate and advanced curriculum releases

- [ ] Stages C-D publish reviewed connected writing/opinion tasks, appropriate language/reading/listening/speaking instruction, and a versioned writing/revision workshop.
- [ ] Stages E-F publish reviewed extended/complex essay tasks, source synthesis/register instruction, models/rubrics, and a durable portfolio with feedback provenance.
- [ ] Each release passes its content inventory, accessibility/design, migrations/tests, provider-disabled workflow, and backup/restore gates. Show self-review/unassessed status when no qualified writing review exists; do not certify mastery from AI scores, XP, or character count.

Audio and Japanese writing are required planned capabilities for this user's release, replacing the old plan's late P2 prioritization. Runtime provider optionality means learning can continue when unavailable; it does not mean skipping implementation or verification of speaking.

## 6. Verification contract

These are planned commands for the app after Phase 1 creates its manifests/scripts and dependencies. They were not run as app validation during this documentation task. Update names if implementation establishes an equivalent convention, and report actual commands/results each session.

Frontend, from `frontend/`:

```text
npm run lint
npm run typecheck
npm run test -- --run
npm run build
```

Backend, from `backend/` with its environment active:

```text
python -m pytest
python -m alembic upgrade head
python -m alembic check
```

Migration upgrade/drift checks must use a disposable database configured through the selected test configuration, never the personal learning DB. Also test forward upgrades from a previous populated schema whenever migrations change. Use isolated fixtures for every learning/progression test.

API smoke check, after launching the backend and setting `TRILINGO_API_BASE_URL` to its configured origin without a trailing slash:

```powershell
Invoke-RestMethod -Uri ($env:TRILINGO_API_BASE_URL + '/api/v1/health')
```

Add the chosen content validation and end-to-end commands when their scripts exist; record them in README. Full-stack phase completion also requires manual critical-flow checks. Real TTS synthesis/listening and microphone/STT evidence are required for Phase 8; mocked adapter tests alone are insufficient.

Business logic tests must include grades/variants, prerequisite bypass, placement versus completion, mastery/checkpoints, double/stale submission, XP ledger/caps, heart recovery, streak protection/timezones/DST, goal and quest periods, reward ledger integrity, timed challenge deadlines, achievement uniqueness, real FSRS transitions, migrations, and backup integrity. For each new page, check narrow mobile, tablet, desktop, and keyboard behavior.

Do not disable or weaken tests to pass. Do not bulk-check tasks because files or components exist. Re-read the diff or compare to a preserved baseline, update relevant docs, and state exactly which checks remain open.

## 7. Carryover from the original roadmap

No original core requirement is considered implemented by this reorganization. The old scopes map to the active phases as follows:

- Original audit/foundation (0-1) -> Phase 1.
- Original content model (2) -> Phase 3, with Japanese content extending through Phases 5-7 and final content audit in 10.
- Original map/visual polish (3, 21) -> Phase 2 shell, Phase 4 live state, then Phase 10 audit.
- Original session/exercise types (4-5) -> Phase 4, extended through Phases 5-8.
- Original hearts/XP/streak/goals (6-8) -> Phase 4 with ongoing regression coverage.
- Original mistakes/FSRS/achievements/stats (9-12) -> Phase 4 initial mistakes, Phase 9 full review and personal progress.
- Original AI (13) -> Phase 7 optional provider layer.
- Original audio/speech (14-15) -> Phase 8, promoted for the user's Japanese goal.
- Original settings/accessibility/testing/security/performance (16-20) -> ongoing work in each phase and final audit in 10.
- Original backup/packaging (22-23) -> Phase 10.

Intermediate/advanced Japanese through complex essays is approved staged scope in the curriculum roadmap. Multiple course/profile management screens, advanced adaptive difficulty beyond the evidence-based practice selector, authoring tools, specialized phoneme assessment, and PWA synchronization remain separate future extensions. Real social competition remains outside the user's confirmed personal scope.

## 8. End-of-task reporting

Report what changed and why, files changed, data/migrations, exact commands/results, manual checks, remaining limitations, verified checklist updates, and the next implementation task. For documentation-only work, say so explicitly; never claim app tests or real audio checks ran when no executable app/provider was available.

## 9. Initial documentation validation record — 2026-10-22

This record covers creation of the roadmap only. No application phase, migration, or real audio integration was completed.

- `python -` (local documentation validator) — PASS: ten consecutively numbered phase files, all required sections/dependencies, valid Markdown structure, 45 resolving local file links, and 228 unchecked implementation tasks across the active documents.
- `rg --files -g '!node_modules' -g '!.git'` — initial inspection found only AGENTS.md and the original implementation plan; no source/test/migration files existed.
- `git status --short` — unavailable as a repository check: this directory is not a Git repository.
- `docker ps -a --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}'` — FAILED: Docker Linux engine named pipe was unreachable. No claim of Japanese compatibility can be made from this result.
- `python --version` and `node --version` — observed Python 3.14.0 and Node.js 25.2.1; these are inspection facts, not a verified application runtime baseline.
- Application lint/typecheck/tests/build, database migrations, and API smoke checks — NOT RUN: no executable app or dependency manifests exist.
- Manual checks — reviewed the sequence, beginner scope, requirement carryover, evidence labels, provider fallbacks, and release gates. No UI or audio playback could be manually exercised.

The archived original master has 32,990 bytes and SHA256 `89dd622830d106a65e90028e5c1dd9f9a7fc851c53d642c4c7cf0bb6e6fdf367`. It was copied before the master rewrite. AGENTS.md was not edited. These initial validation counts predate the combined-feature/Kokoro revision below. The next implementation task is Phase 1.

## 10. Combined-feature and Kokoro revision — 2026-10-22

User clarification: reuse the existing Docker-based Kokoro TTS, include both Duolingo and Babbel learning features, and keep quests/badges/challenges/personal bests personal. The ten-phase structure is retained; no implementation phase is complete.

- Updated this master, README, and Phases 1-5 and 7-10. The typing/handwriting plan in Phase 6 is unchanged. AGENTS.md and the original archive are unchanged.
- `python -` (local documentation validator) — PASS: ten ordered phase files, twelve active documents, 45 resolving local links, required sections/Markdown structure, all 266 implementation tasks unchecked, explicit combined scope/Kokoro reuse, and unchanged SHA256 for AGENTS.md/archive.
- `docker context show` — returned `desktop-linux`.
- `docker ps -a --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}'` — FAILED again because `dockerDesktopLinuxEngine` was unreachable. Existing Kokoro is recorded from user identification; its container name/port/configuration and playback remain unverified. No container was created, started, changed, or removed.
- Reader review — resolved partial-progress audio quest replacement and explicit point-in-time inventory rollback on restore; reviewed reward, placement, protection, fallback, and completion rules.
- Application tests/build/migrations/audio playback — NOT RUN: this remains a planning-only repository. No application code, database, or provider deployment was changed. Begin implementation with Phase 1.

## 11. Staged essay curriculum and UI/UX rules revision — 2026-10-22

The user approved a staged path from beginner Japanese through complex essays and asked for UI/UX skills to avoid generic generated design. Added `docs/CURRICULUM_ROADMAP.md` and `docs/DESIGN_BRIEF.md`, updated the master/README and relevant phases, and added the UI skill workflow to AGENTS.md section 27. Earlier AGENTS rules are preserved; the original master archive is unchanged.

- `python -` (documentation validator) — PASS: ten ordered phase files, fourteen active planning documents, 65 resolving local links, required sections/Markdown structure, all 318 implementation tasks unchecked, A-F release boundaries, writing evidence/persistence rules, and persistent UI skill bindings.
- `python -` (AGENTS comparison to the in-memory baseline) — PASS: removing only the new UI workflow reproduces the previous AGENTS.md content exactly.
- `python 'C:\Users\Administrator\.agents\skills\ui-ux-pro-max\scripts\search.py' 'Japanese learning web app' --design-system -p 'Trilingo' -f markdown` — ran; preset was not a verified fit and was not persisted.
- `python 'C:\Users\Administrator\.agents\skills\ui-ux-pro-max\scripts\search.py' 'study workspace dashboard' --design-system -p 'Trilingo' -f markdown` — narrower retry ran; still not a verified whole-app fit. The project-specific design brief is explicitly a fallback direction, not claimed database output.
- `python 'C:\Users\Administrator\.agents\skills\ui-ux-pro-max\scripts\search.py' 'focus not obscured' --domain ux` — returned relevant accessibility guidance for future rendered checks.
- Reader review — aligned Stage A input tasks, Stage B's three guided compositions/models/revision example/checklist, and later C-F rubric/workshop gates; clarified early component previews versus later live UI reviews.
- Application lint/typecheck/tests/build, migrations, real writing/audio use, screenshots, and design detector — NOT RUN: no executable app or rendered UI exists. These planning changes complete no implementation phase or published curriculum stage. First-release implementation remains Stages A-B; advanced stages require later reviewed content and release gates.
