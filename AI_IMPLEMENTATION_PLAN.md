# Trilingo — Eleven-Phase Japanese Implementation Plan

This is the active execution contract for the project. Read [AGENTS.md](AGENTS.md), this file, [README.md](README.md), and the current phase before editing code.

The [definitive remaining-work execution plan](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md), created 2026-10-25, consolidates the next-work order, dependencies, prerequisites and acceptance evidence for Plan 9.2, Phases 10–11 and later C–F releases. Use it for execution sequencing while preserving the owning phase requirements and exactly eleven numbered phases. Plan creation closed no gate; subsequent bounded execution is recorded below and remains partial.

The later planning request adds [a future-agent continuation guide](docs/AGENT_CONTINUATION_GUIDE.md), [Windows EXE setup](docs/plans/WINDOWS_EXE_SETUP_PLAN.md) and [standalone offline Android](docs/plans/ANDROID_PORT_PLAN.md). Android independence from a PC/internet is user-confirmed. These platform supplements add delivery milestones without creating Phases12/13 or replacing the existing course/release gates. Isolated packaging/engine feasibility may start alongside content review; full Windows/Android releases require their own persistent-data, installer/device and shared content evidence. No installer/port implementation or new application-QA run is authorized merely by this documentation request.

Current connectivity instruction: **cellular data; focused web search is allowed, but ask before any download or upload with its exact scope and estimated total network size in MB/GB**. Prefer installed/local resources and follow the transfer protocol in that execution plan. Publication authorization does not waive transfer approval.

Confirmed project identity: **Trilingo** (exact spelling and capitalization). All remaining implementation and release work must use Trilingo in the app, README/documentation, repository identity, release titles/assets and launch materials. Lowercase `trilingo` is appropriate for technical slugs and filename prefixes; descriptive subtitles or version numbers must retain the Trilingo name. Do not substitute a template name or silently rename the project.

The user requested both Duolingo-style interface/learning features and Babbel-style learning features for personal Japanese reading, writing, and speaking. The user confirmed a beginner starting point, a staged path through complex essays, and personal quests/badges/challenges/bests. English explanations are the initial teaching language.

Confirmed study policy: learning is unrestricted. Every published activity is directly accessible, suggestions are optional, and mistakes never stop study. This overrides earlier game-resource, reward-quota, prerequisite, and mandatory-assessment designs.

The former 24-phase plan is preserved verbatim in [the archive](docs/plans/archive/AI_IMPLEMENTATION_PLAN.original.md). It is historical reference. This eleven-phase sequence replaces its phase numbering and priorities; AGENTS.md remains mandatory. Phase 11 was added at the user’s request for an open-source GitHub release and launch posts on LinkedIn, Reddit and X.

## 1. Current implementation status

Inspection/update date: 2026-10-25.

Latest bounded work: [the 2026-10-25 continuation](docs/PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25) executes the remaining-work plan under a **maximum two hours /18 check-review rounds** allowance, including the five-check extension and final three-check/30-minute writing/grammar batch ending by12:40:00UTC. Start remains 11:05:34 UTC; hard stop remains 13:05:34 UTC. Source **0.1.21** adds **1,060 provisional Stage B words, 110 draft lessons, 1,874 lesson checks and 24 particle contrasts**. Current inventory has **2,167 provisional lexical identities (541 A +1,626 additional B)**, 15 expressions, 92 basic kana and 300 contextual kanji. Both separate word-authoring targets are exceeded; qualified semantic/content review remains pending for **6,848 items**. Saved-item navigation, stale collection loads/actions and completed self-rated recall replay have focused fixes. Existing dependencies pass frontend quality gates on an installed embedded Node24.21.0 runtime; fresh independent setup remains open. The full backend run reports 211 passes and one expanded-guide fixture failure, with focused recovery recorded separately. All additions remain draft; the full Plan 9.2 gate is **partial**, with qualified review, supported setup, real providers/devices and broader verification open. Schema remains **0013**; no learner-data rewrite or migration was needed. Installed tools and loopback services only; no web access, downloads or uploads.

The dated records below describe earlier milestones and do not override this current-source summary.

Previous bounded run: the user authorized **Phases 7, 8 and 9**, maximum one hour, on cellular data. Start approximately 04:56:28 UTC / 12:56:28 Singapore; hard stop **05:56:28 UTC / 13:56:28 Singapore** on 2026-10-23. No dependency/model/container/browser/font downloads. The prior Phases 4–6 run is historical and does not extend this allowance. This bounded run has stopped within the one-hour cap; the broader goal is paused with unverified requirements preserved. Full phase gates remain open unless every required check is proved. See [first-hour evidence](docs/PHASE_07_09_VERIFICATION.md) and [the additional authorized hour](docs/PHASE_07_09_FOLLOWUP.md).


- Engineering through Phases 4–6 plus partial Phases 7–9 now exists: React/TypeScript/Vite/Tailwind/Zod frontend; FastAPI/Pydantic/SQLAlchemy/Alembic backend; thirteen SQLite migrations; validated original practice/draft content and isolated tests. Qualified content/publication and physical verification gates remain open.
- Phase 1: current-machine launch, settings persistence, configuration, migration and quality checks pass. Full fresh frontend install on supported Node 24 LTS remains unverified under the cellular cap; the phase gate stays open.
- Phase 2: shell, shared design system, selectable path, library/settings, development fixtures and rendered responsive/keyboard/error checks are verified for this milestone's scope. This is not a playable learning engine.
- Phase 3: technical practice slice has two published units, six lessons, thirty exercise definitions, eight core words and five separately counted expressions. The ten topics now contain 230 draft lessons, with seven writing references, two stories, four passages and two audio episodes still draft. The [review packet](docs/JAPANESE_CONTENT_REVIEW.md) is current for 0.1.21; no qualified reviewer is available, so independent review/publication gates stay open.
- Content versions are immutable; ordinary lesson responses protect answers and deliberate assistance is idempotent, including retry after a course update. No real learning progress was reset.
- Git was initialized locally; no commits or remote publication were made.
- Phase 11 is now planned for open-source GitHub publication and a LinkedIn/Reddit/X launch. Repository preparation, upload and promotion remain unstarted; the new phase includes tailored draft posts and a week-one runbook. This documentation request does not resume the paused Phases 4–6 implementation goal.
- Both inspected Docker engine pipes remain unreachable. Local AI/TTS/STT adapters and recording/transcript-feedback controls now exist; Kokoro and real Japanese STT/playback remain unverified. No containers or models were downloaded or started. Phase 8 remains open.
- Current implementation evidence, actual commands, screenshots, data-safety checks and remaining limits: [verification](docs/PHASE_01_03_VERIFICATION.md). [Technical decisions](docs/TECHNICAL_DECISIONS.md) and [content authoring](docs/CONTENT_AUTHORING.md) document the contracts.
- The earlier Phases 7–9 goal used the additional authorized hour recorded below. Phase 4 is implemented and verified for the technical-practice slice: five exercise renderers, authoritative grading, durable sessions/mistakes, idempotent actions, uncapped genuine-session XP, activity statistics and optional assessment previews with advisory placement. [Phase 4 verification](docs/PHASE_04_VERIFICATION.md) records the evidence. Phases 5–6 draft engineering is implemented: kana/contextual reading, stories and durable saved items; typed checks, draft/revision/conflict/submission workflows and optional formation/sample practice. See [Phase 5 verification](docs/PHASE_05_VERIFICATION.md) and [Phase 6 verification](docs/PHASE_06_VERIFICATION.md). Earlier clean-install/runtime, qualified-content review, full content inventory and physical-device gates remain open; these phases are not claimed fully released.
- The source 0.1.11 batch added all 300 target kanji as draft (100 Stage A +200 additional Stage B), each linked to contextual words/readings and checks. Qualified review/publication remains pending. There are 286 word records plus 5 expressions; semantic deduplication and the 2,000-word target remain open. Word search and Show more/all keep this larger library directly browsable.
- Draft grammar/six practical scenarios, real FSRS, preserved mistake-card import, named collections, optional quests/badges/timing and personal records now have engineering implementations. [Phases 7–9 verification](docs/PHASE_07_09_VERIFICATION.md) separates tests from unverified content/providers and remaining requirements. All three full phase gates remain unchecked.
- First release still targets A-B; C-F remain approved later releases. No full starter word inventory or proficiency is claimed.
- [Plan 9.2 — Complete outstanding work from Phases 1–9](docs/plans/PLAN_09_2_COMPLETION.md) is the planned completion supplement before Phase 10. It covers supported setup, reviewed beginner content, remaining feature workflows, real providers/devices and phase reconciliation. Creating it does not resume implementation or close existing gates.

## 2. Product definition and boundaries

Build a local-first Windows application for one personal learner. The main learning loop is: learn a small concept, use it in context, produce an answer, receive clear feedback, then revisit it through scheduled practice.

The interface and feature set include an openly browsable course path, themed units, large lesson nodes, short exercises, XP, optional goals/streak statistics/quests, stories, optional mastery practice, and a practice hub. Use original Trilingo branding, artwork, wording, sounds, and course content. Adopt the useful teaching/motivation mechanics under the user's unrestricted-study policy.

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

Keep exactly eleven implementation phase files: Phases 1–10 cover the app/content and local release; Phase 11 covers open-source publication and its launch campaign. Their initial completion tracking refers to the beginner release; later stages reapply the relevant content, writing, feedback, persistence, and release gates against their declared release scope. They do not become complete automatically when the beginner app launches. JLPT tags cannot substitute for writing/speaking assessment; see the [official JLPT FAQ](https://www.jlpt.jp/e/faq/index.html).

### Required design workflow

Apply `ui-ux-pro-max`, `frontend-design`, and `design-skill` to relevant UI work, following the persistent rule in [AGENTS.md](AGENTS.md) and the [design brief](docs/DESIGN_BRIEF.md). Record a product-specific direction, verify any search result before persisting it, then inspect and improve actual rendered screens. Show suggested/available/studied states and freely reachable actions. Phase 2 establishes the design system; every UI phase checks it, and Phase 10 audits it. The shell and clearly labeled fixtures have now been rendered and reviewed; later real-feature audits remain pending.

### Unrestricted study policy

- No hearts/lives/energy, forced recovery, cooldowns, waiting periods, paid access, daily/session quotas, XP ceilings, or replay-frequency restrictions.
- All published units, lessons, stages, explanations, available modes, and installed cosmetics are directly selectable. Suggested preparation/order never controls access; unpublished content is labeled honestly.
- Retry, reveal/hint, skip, pause/resume, finish, replay, and Continue remain available after mistakes. Skipped/assisted results retain honest evidence without blocking further work.
- Placement, recaps/checkpoints, mastery practice, goals, quests, badges, reminders, and streak/timing displays are optional. No pass score, due-review completion, token balance, or prior lesson is required to study.
- Every genuinely completed new study session can earn its defined XP without daily limits. Idempotency prevents replaying one network event for duplicate rewards; it does not prevent new genuine sessions.
- Batch sizes are adjustable convenience settings with Show more/all. FSRS suggests timing; early review and freely selected new material are available. Optional elapsed-time displays never expire an activity or create a failure.
- Missing a goal or day removes no earned XP, work, or access. There are no consumable freeze inventories, token shops, or earned-access cosmetics.
- Engineering validation, truthful grading/evidence, publication quality, secure provider handling, and backup safety remain required. These are reliability checks, not artificial learner restrictions.

Initial editable suggestions: one local profile, an optional 20 XP goal, a short lesson and voluntary review when useful, and system-detected timezone with Asia/Singapore available for this computer. All suggestions may be ignored/hidden; none limits study. No fluency deadline, complete JLPT coverage, specialized pronunciation score, or handwriting-recognition capability is promised.

Public friends, shared leagues/leaderboards, and friend streaks are outside the confirmed personal scope. Use weekly personal bests drawn from the learner's own history; do not fabricate competing users. Purchases, subscriptions, live tutors, broad multilingual course catalogs, and a generic chatbot are also outside the initial release. The generic engine and data model must still avoid hard-coding a specific course/profile into core logic.

### Duolingo-inspired personal features and phase ownership

These are explicit planned features, not a claim of full commercial-product parity:

- Course path, lesson nodes, unit guides, and a dedicated practice hub: Phases 2-4; live practice filters in Phase 9.
- Short mixed exercises, committed feedback, voluntary mistake review, unlimited replay, XP, optional levels/achievements/activity statistics, and editable goals: Phases 4 and 9.
- Optional placement recommendations, recap/checkpoint practice, and mastery self-checks with freely available hints and retakes: Phase 4. All published lessons are already accessible.
- Original short interactive stories with comprehension, vocabulary, and replay: Phase 5; listen-along story/mini audio episodes and focused speaking/listening sessions: Phase 8.
- Optional personal quests/monthly badges, directly selectable cosmetics, weekly personal bests, and matching/recall practice with an optional non-expiring elapsed-time display: Phase 9.
- Optional practice suggestions based on errors/skill evidence, freely overridable by the learner: Phase 9; opt-in local reminders/notifications: Phase 10.
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

The backend owns grades, XP ledger, honest study/assessment records, activity statistics, optional badge awards, and FSRS. The client supplies answers, supported actions, identifiers, and learner ratings. A client correctness flag, XP amount, due date, or mastery claim is never authoritative. No grade, assessment, or activity history is an access prerequisite for published study material.

Use `/api/v1` consistently, thin routes, typed public schemas, explicit error codes, UTC event/due timestamps, preserved profile-local activity dates, transactions, and idempotency. Changes to persistent schema require migrations and clean-DB verification. Content must be original, versioned, validated, and separate from UI code.

## 4. Eleven phase files and implementation tracking

Each phase file includes goal, actionable tasks, intended implementation areas, data/API contracts, tests/manual checks, and completion criteria. All checkboxes below refer to implementation, not drafting.

1. [Phase 01 — Foundation and technical decisions](docs/plans/PHASE_01_FOUNDATION.md): audit, Windows setup, frontend/backend skeleton, configuration, initial DB migration, contracts, isolated tests, and early provider discovery.
   - [ ] Verified implementation complete.
2. [Phase 02 — Interface and design system](docs/plans/PHASE_02_INTERFACE.md): required UI/UX skills, original visual direction/tokens, responsive navigation/path shell, reusable controls, accessible states, and rendered design review.
   - [x] Verified implementation complete for shell/component/fixture scope; later real-feature audits remain required.
3. [Phase 03 — Japanese curriculum and content model](docs/plans/PHASE_03_CURRICULUM.md): staged curriculum metadata, first-release beginner syllabus, versioned schemas/APIs/seeds, and reviewed content inventory.
   - [ ] Verified implementation complete.
4. [Phase 04 — Lesson engine and unrestricted study](docs/plans/PHASE_04_LESSON_ENGINE.md): reusable exercises, honest grades/evidence, unlimited continuation/replay, uncapped genuine-session XP, and optional assessments.
   - [x] Verified implementation complete for the technical-practice engine; qualified content review remains open in its owning phases.
5. [Phase 05 — Kana, kanji, and reading](docs/plans/PHASE_05_READING.md): script libraries, contextual readings, aids, passages, original interactive stories, and reading evidence.
   - [ ] Verified implementation complete.
6. [Phase 06 — Typing and handwriting](docs/plans/PHASE_06_WRITING.md): IME, guided handwriting, beginner draft saving/guided paragraphs, and later staged writing workshops with revision/rubric evidence.
   - [ ] Verified implementation complete.
7. [Phase 07 — Grammar and practical dialogues](docs/plans/PHASE_07_GRAMMAR_DIALOGUES.md): unit guides, branching situations, recaps/collections, optional explanation adapters.
   - [ ] Verified implementation complete.
8. [Phase 08 — Japanese audio and speaking](docs/plans/PHASE_08_AUDIO_SPEAKING.md): Kokoro Japanese setup/verification, listening/audio stories, recording, Japanese STT, shadowing, privacy/fallbacks.
   - [ ] Verified implementation complete, including real-provider checks.
9. [Phase 09 — Review, quests, and personal progress](docs/plans/PHASE_09_REVIEW_PROGRESS.md): voluntary any-time FSRS/practice, optional quests/badges/goals, free cosmetics, non-expiring personal timing, and truthful statistics.
   - [ ] Verified implementation complete.
10. [Phase 10 — Reliability, backup, and local release](docs/plans/PHASE_10_RELEASE.md): audited course/features, safe backup/restore, local reminders, security/performance, Windows launch, full regression and manual release flow.
    - [ ] Verified implementation complete.
11. [Phase 11 — Open-source GitHub release and launch](docs/plans/PHASE_11_OPEN_SOURCE_LAUNCH.md): clean licensed repository, contribution/security documentation, CI, verified tagged release, and an organic LinkedIn/Reddit/X campaign with tailored draft posts and recorded follow-up.
    - [ ] Public repository/release and authorized campaign complete.

Follow the numbered sequence for the main implementation. Use [Plan 9.2](docs/plans/PLAN_09_2_COMPLETION.md) to close the remaining beginner Phase 1–9 work before the Phase 10 handoff; it is a supplement and leaves exactly eleven numbered phase files. TTS discovery may run in Phase 1. Tests, accessibility, migrations, and data safety belong in every phase; Phase 10 verifies them comprehensively. Dependencies refer to needed contracts/features. If optional hardware/providers cannot be exercised, record that phase as partial and continue independent work; do not let it imply the final speaking release gate is satisfied.

## 5. Milestones and acceptance

### First playable slice — through Phase 4

- [x] Real frontend/backend launch with AI/audio disabled.
- [x] First original Japanese slice has at least two units, three lessons per unit, five useful exercises per lesson, and at least three supported types; the engine supports the four core text types plus matching.
- [x] A new learner can directly choose any published lesson, make mistakes, retry/reveal/skip, finish, and choose another activity immediately.
- [x] Refresh/restart preserves attempts and evidence; new genuine same-day sessions earn XP without quotas, while duplicate network events stay idempotent.
- [x] Basic mistakes/practice work but are not labeled FSRS before Phase 9.
- [x] Optional recaps, placement, and mastery use honest evidence, unlimited retakes, and supported assistance; no result controls access or continuation.

### Japanese skills feature set — through Phase 9

- [ ] Kana and reviewed beginner kanji/passages can be read with adjustable aids.
- [ ] IME input and guided handwriting practice work with truthful evidence labels.
- [ ] Stage A character/word/first-sentence tasks and at least three Stage B guided compositions, reviewed models/alternatives, a simple revision example, persisted drafts, and self-review work without AI. Open writing is not graded as an exact-string answer; C-F have their own task/rubric/workshop gates.
- [ ] Original grammar guides and everyday dialogues are usable without AI.
- [ ] Real Japanese TTS and STT/microphone paths are verified on the target computer; listening and speaking failures have usable fallbacks.
- [ ] Actual FSRS persists ratings, states, due dates, and history; skill evidence and stats are based on stored data.
- [ ] Stories/audio stories, optional quests/badges, free cosmetic selections, non-expiring elapsed-time practice, and personal bests persist without adding access or study quotas.

### Personal release — Phase 10

- [ ] Published beginner course inventory matches what the app claims.
- [ ] Full A-B inventory reaches 92 basic kana with taught patterns, 300 distinct contextual kanji, and 2,000 unique reviewed core word entries; smaller beta/technical slices disclose their partial counts and do not claim full coverage.
- [ ] Both quality gates, clean migrations, API smoke, manual critical flow, accessible/mobile checks, local restart, and backup/restore round trip pass.
- [ ] README launch/update/provider/troubleshooting instructions are tested.
- [ ] Reminder controls, unrestricted study, and backup coverage of optional goals/quests/records/preferences are verified; no social results or skill evidence are fabricated.
- [ ] UI skill workflow, shared design decisions, representative screenshots, keyboard/IME checks, and resolved major visual/interaction findings are recorded; first-release claims stay within published Stages A-B.
- [ ] Every limitation is recorded; unchecked required gates keep the release incomplete.

### Public open-source release and launch — Phase 11

- [ ] A clean, licensed public GitHub repository, tested setup instructions, contribution/reporting guidance and CI are available.
- [ ] A verified release tag/commit, honest feature/content limitations and synthetic demonstration assets are published after authorization.
- [ ] Final LinkedIn, Reddit and X posts follow the verified release and destination rules; authorized posts and week-one feedback have recorded live links/results.

### Later intermediate and advanced curriculum releases

- [ ] Stages C-D publish reviewed connected writing/opinion tasks, appropriate language/reading/listening/speaking instruction, and a versioned writing/revision workshop.
- [ ] Stages E-F publish reviewed extended/complex essay tasks, source synthesis/register instruction, models/rubrics, and a durable portfolio with feedback provenance.
- [ ] Each release passes its content inventory, accessibility/design, migrations/tests, provider-disabled workflow, and backup/restore gates. Show self-review/unassessed status when no qualified writing review exists; do not certify mastery from AI scores, XP, or character count.

Audio and Japanese writing are required planned capabilities for this user's release, replacing the old plan's late P2 prioritization. Runtime provider optionality means learning can continue when unavailable; it does not mean skipping implementation or verification of speaking.

## 6. Verification contract

These commands now exist and were run during Phase 1-3 implementation. Current results and remaining validation limits are in the verification record. Continue reporting exact commands/results each session.

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

Business logic tests must include grades/variants, direct access to all published content, optional assessment/skip/assistance evidence, unlimited retries/replays/continuation, uncapped genuine-session rewards versus idempotent retries, activity dates/timezones/DST, optional goals/quests/badges, free cosmetics, non-expiring personal timing, early FSRS review, migrations, and backup integrity. For each new page, check narrow mobile, tablet, desktop, and keyboard behavior.

Do not disable or weaken tests to pass. Do not bulk-check tasks because files or components exist. Re-read the diff or compare to a preserved baseline, update relevant docs, and state exactly which checks remain open.

## 7. Carryover from the original roadmap

No original core requirement is considered implemented by this reorganization. The old scopes map to the active phases as follows:

- Original audit/foundation (0-1) -> Phase 1.
- Original content model (2) -> Phase 3, with Japanese content extending through Phases 5-7 and final content audit in 10.
- Original map/visual polish (3, 21) -> Phase 2 shell, Phase 4 live state, then Phase 10 audit.
- Original session/exercise types (4-5) -> Phase 4, extended through Phases 5-8.
- Original reward/activity scope (6-8) -> Phases 4 and 9 under unrestricted study; old resource restrictions are superseded.
- Original mistakes/FSRS/achievements/stats (9-12) -> Phase 4 initial mistakes, Phase 9 full review and personal progress.
- Original AI (13) -> Phase 7 optional provider layer.
- Original audio/speech (14-15) -> Phase 8, promoted for the user's Japanese goal.
- Original settings/accessibility/testing/security/performance (16-20) -> ongoing work in each phase and final audit in 10.
- Original backup/packaging (22-23) -> Phase 10.

Intermediate/advanced Japanese through complex essays is approved staged scope in the curriculum roadmap. Multiple course/profile management screens, advanced adaptive difficulty beyond the evidence-based practice selector, authoring tools, specialized phoneme assessment, and PWA synchronization remain separate future extensions. Real social competition remains outside the user's confirmed personal scope.

## 8. End-of-task reporting

Report what changed and why, files changed, data/migrations, exact commands/results, manual checks, remaining limitations, verified checklist updates, and the next implementation task. For documentation-only work, say so explicitly; never claim app tests or real audio checks ran when no executable app/provider was available.

## 9. Historical unrestricted-study planning revision and validation

The following records the earlier documentation-only revision. Current implementation status is in section1 and the linked verification record.

The user explicitly removed learner-resource mechanics and any artificial hindrance to study. The active policy and ten phase files supersede the earlier restricted design. The previous master, including historical validation records, is preserved as [historical reference](docs/plans/archive/AI_IMPLEMENTATION_PLAN.before-unrestricted-study.md); the [original generic plan](docs/plans/archive/AI_IMPLEMENTATION_PLAN.original.md) is also unchanged. Neither archive is an active execution contract.

All changes in this revision concern planning documents and persistent project guidance. No application code, database, user progress, Docker container, or provider configuration was changed. Applicable engineering checks and honest grading/evidence remain required.

- Updated AGENTS.md, README, this master, the ten phase files, curriculum roadmap, and design brief. Removed the resource/lock/quota/deadline state and its implementation tasks; no implementation checkbox was marked complete.
- `python -` (documentation validator) — PASS: ten ordered phase files, fourteen active planning documents, 67 resolving local links, required phase sections/Markdown structure, and all 316 implementation tasks unchecked.
- `python -` — PASS: unrestricted study/uncapped genuine-session rules and optional assessments/feedback/early review are explicit; obsolete positive restrictions are absent; all 52 numbered AGENTS sections, UI skill guidance, staged curriculum, and original archive SHA256 are retained.
- `rg -n -i` with targeted obsolete-rule patterns over active Markdown, excluding both archives — no old positive resource, reward-cap, mandatory prerequisite/pass, countdown-expiry, or purchase-inventory requirement remained. Remaining matching words describe prohibited mechanics, data recovery, or ordinary engineering/design concepts.
- Reader review — no substantive conflicts: mistakes/skips permit finish/continuation, new genuine sessions earn XP, duplicate requests stay idempotent, self-review is optional, and FSRS early review works without access restrictions.
- Application tests/build/migrations/UI checks — NOT RUN: no executable app exists. No real learning data was modified. The next implementation task remains Phase 1 under unrestricted study.

## Additional authorized hour — 2026-10-23

The user resumed Phases 7–9 for one additional hour, from approximately 06:16:26 UTC to a hard stop at **07:16:26 UTC** (14:16:26–15:16:26 Singapore). This supersedes the prior paused-run stop for this window only. Continue the full remaining phase scope, preserve data, use installed dependencies and avoid downloads on cellular data.

Implemented in this continuation: draft listening selection/dictation/contrast through the shared engine, protected transcripts and pronunciation overrides, idempotent audio delivery, targeted particle checks and choice feedback, optional strict scenario coaching with authored fallback, same-assignment listening quest fallback, optional server-recorded recall timing, activity calendar/reminder visibility and direct practice-mode links. Migrations 0010–0011 are additive and tested on disposable databases. Full backend regression: 175 passed. Current detailed evidence and remaining gates are in [the follow-up record](docs/PHASE_07_09_FOLLOWUP.md). The full phases remain partial; no qualified publication or real-provider success is claimed.

This additional window stopped at approximately 07:13:35 UTC, within the 07:16:26 UTC hard stop. Automated gates: 175 backend tests, 29 frontend tests, lint/typecheck/build, clean/populated migrations, 72 responsive browser layouts, concurrent audio recovery and simulated recording checks pass. Owned QA services are stopped; no real learner data was changed. The broader goal remains paused and the full phase gates remain open.


## Plan 9.2 execution — 2026-10-23

The user authorized a maximum of one hour for Plan 9.2, starting 11:59:10 UTC with a hard stop at 12:59:10 UTC. [The execution record](docs/PLAN_09_2_VERIFICATION.md) identifies current source 0.1.15/schema 0012, exact commands/results and all outstanding tasks. Full plan/phase completion is not claimed.

Added source-bound inventory/review packets, sixteen draft guides across ten topics, eight initial draft lessons/24 checks, saved-snapshot collection recall, all-history timing pagination with honest pause records, and separate objective/self-rated/workflow/publication statistics. The original published practice slice is unchanged. The provisional audit finds 285 lexical identities, not the 2,000-word reviewed target. Supported fresh setup, qualified publication, real Japanese providers/rewarded speaking and physical/accessibility checks remain open. Earlier time-window records above remain historical; the new window grants no model/dependency downloads or public release.

## Plan 9.2 speaking continuation — 2026-10-24

Within the additional two-hour allowance, implemented 16 draft speaking prompts through the shared session engine, durable transcript/fallback evidence, normal idempotent practice XP, speaking quests, explicit voiced scenario controls and five-direction self-rated word/collection recall using original snapshots. Schema 0013 versions the additive evidence contract without rewriting learner history. Source is 0.1.16; the published slice and 285 provisional lexical identities are unchanged.

[Current continuation evidence](docs/PLAN_09_2_SPEAKING.md): 197 backend tests, 31 frontend tests, lint/typecheck/build, clean/populated forward migrations/imports and 24 focused responsive layouts pass. The run used installed tools and local services, with no downloads or web browsing. Full inventory/qualified review/publication, real Japanese providers and physical/accessibility checks remain open. This does not complete Plan 9.2 or authorize Phase 10/11 release.
