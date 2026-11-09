# AI_IMPLEMENTATION_PLAN.md

# Duolingo-Inspired Local Learning App — AI Implementation Plan

> **Purpose:** This is the master execution file for AI coding agents working on this project.
>
> The agent MUST use this file as a phase-by-phase implementation contract. It may not mark a phase complete until all required checks and acceptance criteria for that phase pass.
>
> This project is **ONLY** the local Duolingo-inspired learning application. It does **not** include the document/PDF-to-flashcard project.

---

## 0. Project Mission

Build a polished, local-first language-learning web application inspired by the learning mechanics of Duolingo while using original branding, original UI assets, and original course content.

The product should eventually support most major learning mechanics expected from a modern gamified language-learning application:

- course → unit → lesson progression
- multiple-choice exercises
- translation exercises
- fill-in-the-blank exercises
- matching exercises
- sentence ordering
- lesson completion scoring
- XP
- streaks
- hearts/lives
- daily goals
- levels
- achievements
- progress visualization
- spaced repetition
- mistake review
- listening exercises
- text-to-speech
- speech/pronunciation practice
- optional AI-generated explanations
- optional adaptive difficulty

The app is intended to run locally first on Windows.

---

# 1. Non-Negotiable Architecture

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Zod for runtime validation
- React Router or equivalent lightweight routing
- A predictable client-side state solution only where needed

## Backend

- Python
- FastAPI
- Pydantic
- SQLAlchemy or SQLModel
- Alembic or equivalent migrations

## Database

- SQLite
- Database must be migration-controlled
- No business-critical state stored only in browser localStorage

## Review Scheduling

- FSRS-compatible review scheduling
- Prefer `ts-fsrs` if review scheduling is performed in the frontend
- If FSRS is implemented server-side, maintain equivalent review state and deterministic tests

## Optional AI Provider

AI is an enhancement, not a hard dependency.

Provider layer must support:

- disabled/no-AI mode
- LM Studio
- generic OpenAI-compatible endpoint
- future providers without rewriting lesson logic

Suggested abstraction:

```ts
interface AIProvider {
  isAvailable(): Promise<boolean>;
  generateExplanation(input: ExplanationRequest): Promise<ExplanationResult>;
}
```

## Audio

Not required for first MVP.

Later phases may add:

- local text-to-speech
- local speech-to-text
- pronunciation comparison/scoring

---

# 2. Core Design Principle

## Separate the Learning Engine from Course Content

The application MUST NOT hard-code one language or one lesson path into React components.

Use this conceptual split:

```text
COURSE CONTENT
     ↓
LEARNING ENGINE
     ↓
EXERCISE RENDERER
     ↓
PROGRESS / XP / REVIEW
```

Course data defines:

- language
- units
- lessons
- concepts
- vocabulary
- exercises
- answers
- explanations
- difficulty
- prerequisites

The learning engine decides:

- what is unlocked
- which exercise appears
- how an answer is graded
- progress earned
- hearts lost
- XP awarded
- whether an item enters review
- what happens after lesson completion

The renderer displays an exercise based on its type.

---

# 3. Exercise Schema First

Every exercise MUST conform to a validated schema.

Example conceptual model:

```ts
type ExerciseType =
  | "multiple_choice"
  | "translation"
  | "fill_blank"
  | "matching"
  | "sentence_order"
  | "listening"
  | "speaking";

interface BaseExercise {
  id: string;
  type: ExerciseType;
  prompt: string;
  instruction?: string;
  difficulty: "easy" | "medium" | "hard";
  explanation?: string;
  conceptIds: string[];
}
```

Each exercise subtype gets its own strict schema.

Do not use large components full of `if/else` business logic.

Preferred pattern:

```text
ExerciseSession
   ↓
ExerciseRenderer
   ├── MultipleChoiceExercise
   ├── TranslationExercise
   ├── FillBlankExercise
   ├── MatchingExercise
   ├── SentenceOrderExercise
   ├── ListeningExercise
   └── SpeakingExercise
```

---

# 4. Priority Levels

## P0 — Required MVP

The app is not considered usable until these are finished.

- local frontend + backend launch
- SQLite persistence
- course map
- units
- lessons
- exercise session
- multiple choice
- translation
- fill-in-the-blank
- sentence ordering
- answer grading
- lesson completion
- progress saving
- XP
- hearts
- streak
- daily goal
- basic profile
- mistake tracking
- basic review queue
- responsive UI
- core tests

## P1 — Strong Feature Set

- matching exercise
- achievements
- level system
- course progress percentages
- lesson replay
- mistake review screen
- FSRS review scheduling
- settings
- sound effects
- keyboard accessibility
- improved animations
- statistics dashboard
- AI explanation provider abstraction
- LM Studio support

## P2 — Advanced

- text-to-speech
- listening exercises
- speech-to-text
- pronunciation practice
- adaptive difficulty
- AI-assisted exercise authoring
- multiple courses
- multiple user profiles
- course authoring tools
- richer analytics
- offline install/PWA
- import/export backup

P2 must not delay P0 or P1 stabilization.

---

# 5. Definition of Done

A task is **NOT DONE** because code exists.

A feature is DONE only when all applicable conditions are true:

- [ ] feature is implemented
- [ ] expected happy path works
- [ ] invalid input is handled
- [ ] loading state exists where needed
- [ ] error state exists where needed
- [ ] empty state exists where needed
- [ ] persistence works after refresh/restart
- [ ] backend validation exists
- [ ] frontend validation exists where applicable
- [ ] no known console errors
- [ ] no known unhandled backend exceptions
- [ ] type checking passes
- [ ] linting passes
- [ ] automated tests pass
- [ ] manual acceptance test passes
- [ ] mobile layout remains usable
- [ ] keyboard interaction works for interactive controls
- [ ] implementation does not duplicate an existing abstraction
- [ ] documentation/checklist is updated

The agent MUST NOT check a box merely because it wrote code.

---

# 6. Required Project Layout

Use this as the default target layout unless the existing repository already has a clean equivalent.

```text
/
├── AGENTS.md
├── AI_IMPLEMENTATION_PLAN.md
├── README.md
├── .env.example
├── .gitignore
├── frontend/
│   ├── package.json
│   ├── vite.config.ts
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── features/
│   │   │   ├── auth-or-profile/
│   │   │   ├── course-map/
│   │   │   ├── lessons/
│   │   │   ├── exercises/
│   │   │   ├── progress/
│   │   │   ├── hearts/
│   │   │   ├── streaks/
│   │   │   ├── xp/
│   │   │   ├── review/
│   │   │   ├── achievements/
│   │   │   └── settings/
│   │   ├── lib/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── types/
│   │   └── styles/
│   └── tests/
├── backend/
│   ├── pyproject.toml
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── repositories/
│   │   └── ai/
│   ├── migrations/
│   └── tests/
├── content/
│   ├── courses/
│   └── seeds/
└── scripts/
```

---

# 7. Database Domain Model

The exact schema may evolve, but the project should support these concepts.

## Core tables/entities

- profiles
- languages
- courses
- course_enrollments
- units
- lessons
- lesson_prerequisites
- exercises
- exercise_choices
- vocabulary
- concepts
- exercise_concepts
- user_progress
- lesson_attempts
- exercise_attempts
- mistake_log
- xp_history
- streaks
- daily_goals
- hearts
- achievements
- user_achievements
- review_items
- review_logs
- settings

## Required rules

- IDs must be stable
- ordering must be explicit
- completion must be queryable
- attempts must preserve history
- XP must use a ledger/history instead of only a mutable total
- streak calculations must use dates, not fragile counters alone
- hearts changes should be auditable enough to debug
- review state must store enough information for FSRS
- deleting/reordering content must not silently corrupt progress

---

# 8. API Design Goals

Prefer clear resource-oriented endpoints.

Illustrative routes:

```text
GET    /api/health
GET    /api/profile
PATCH  /api/profile

GET    /api/courses
GET    /api/courses/{course_id}
POST   /api/courses/{course_id}/enroll

GET    /api/courses/{course_id}/map
GET    /api/lessons/{lesson_id}
POST   /api/lessons/{lesson_id}/start
POST   /api/lesson-attempts/{attempt_id}/answer
POST   /api/lesson-attempts/{attempt_id}/complete

GET    /api/progress
GET    /api/streak
GET    /api/xp
GET    /api/hearts
GET    /api/daily-goal

GET    /api/review
POST   /api/review/{review_item_id}/grade

GET    /api/achievements
GET    /api/stats

GET    /api/settings
PATCH  /api/settings

GET    /api/ai/status
POST   /api/ai/explain
```

Do not create a huge `/api/do-everything` endpoint.

---

# 9. Phase 0 — Repository Audit and Baseline

## Goal

Understand the repository before changing it.

## Agent Tasks

- [ ] inspect the entire project tree
- [ ] identify existing frontend/backend folders
- [ ] inspect package manager files
- [ ] inspect environment configuration
- [ ] inspect current database setup
- [ ] inspect existing tests
- [ ] inspect current routes
- [ ] inspect existing data models
- [ ] identify broken/incomplete features
- [ ] identify duplicated code
- [ ] identify dead code
- [ ] identify TODO/FIXME markers
- [ ] identify security-sensitive configuration
- [ ] identify generated files that should not be edited manually

## Required Output Before Coding

Create or update a short implementation status section containing:

```text
Existing:
Missing:
Broken:
Partially implemented:
Technical debt affecting current phase:
Next phase:
```

## Completion Gate

- [ ] repository is understood well enough to avoid rebuilding existing working systems
- [ ] no destructive rewrite is planned without clear necessity
- [ ] current test/build status is known

---

# 10. Phase 1 — Project Foundation

## Goal

Establish a reliable development environment.

## Frontend Checklist

- [ ] React + TypeScript + Vite configured
- [ ] Tailwind configured
- [ ] routing configured
- [ ] strict TypeScript enabled
- [ ] ESLint configured
- [ ] formatting convention established
- [ ] environment variable handling established
- [ ] API client wrapper created
- [ ] reusable error boundary strategy exists
- [ ] reusable loading UI exists
- [ ] global layout exists

## Backend Checklist

- [ ] FastAPI project launches
- [ ] configuration module exists
- [ ] CORS is intentionally configured
- [ ] SQLite connection works
- [ ] ORM configured
- [ ] migrations configured
- [ ] health endpoint exists
- [ ] structured error responses exist
- [ ] logging configured
- [ ] tests can use an isolated database

## Root-Level Checklist

- [ ] `.env.example`
- [ ] `.gitignore`
- [ ] startup instructions
- [ ] dependency install instructions
- [ ] frontend start command
- [ ] backend start command
- [ ] test commands

## Acceptance Tests

- [ ] frontend starts from a clean install
- [ ] backend starts from a clean install
- [ ] frontend can reach `/api/health`
- [ ] database file is created in expected location
- [ ] tests do not depend on production DB file
- [ ] app can restart without losing stored data

---

# 11. Phase 2 — Course Content Model and Seed Course

## Goal

Prove content can exist independently from UI code.

## Required Content Hierarchy

```text
Language
└── Course
    ├── Unit
    │   ├── Lesson
    │   │   ├── Concept
    │   │   └── Exercise
    │   └── Lesson
    └── Unit
```

## Checklist

- [ ] language schema implemented
- [ ] course schema implemented
- [ ] unit schema implemented
- [ ] lesson schema implemented
- [ ] prerequisite/unlock model implemented
- [ ] concept schema implemented
- [ ] vocabulary schema implemented
- [ ] exercise base schema implemented
- [ ] seed loader implemented
- [ ] seed data is idempotent
- [ ] sample course uses original content
- [ ] ordering is stable
- [ ] invalid content fails validation loudly

## Seed Course Minimum

Create enough original sample content to exercise the engine:

- [ ] at least 2 units
- [ ] at least 3 lessons per unit
- [ ] at least 5 exercises per lesson
- [ ] at least 3 exercise types
- [ ] vocabulary items
- [ ] concepts
- [ ] explanations
- [ ] difficulty labels

Do not copy Duolingo lesson text or proprietary course content.

## Acceptance Tests

- [ ] seed import works on empty DB
- [ ] running seed twice does not duplicate data
- [ ] course map can be fetched entirely from database
- [ ] frontend contains no hard-coded lesson list
- [ ] invalid exercise content is rejected

---

# 12. Phase 3 — Course Map and Progression

## Goal

Create the main learning path.

## Features

- course header
- unit sections
- lesson nodes
- locked/unlocked/completed states
- current lesson indicator
- progress summaries
- responsive mobile/desktop layout

## Unlock Rules

At minimum:

- first lesson available by default
- completing a required lesson unlocks the next
- replaying a completed lesson remains allowed
- locked lessons cannot start via direct URL/API bypass

## Checklist

- [ ] course map endpoint
- [ ] course map page
- [ ] unit component
- [ ] lesson node component
- [ ] lock state
- [ ] current state
- [ ] completed state
- [ ] progress bar
- [ ] correct redirect/error for unavailable course
- [ ] server enforces unlock status

## Acceptance Tests

- [ ] new profile sees only valid starting lesson(s)
- [ ] completing lesson unlocks expected next lesson
- [ ] refresh preserves state
- [ ] direct navigation cannot bypass prerequisites
- [ ] course map remains usable on narrow screen

---

# 13. Phase 4 — Lesson Session Engine

## Goal

Build the reusable engine that runs all lesson exercises.

## Session Responsibilities

- create lesson attempt
- load ordered/randomized exercise set
- preserve session state
- collect answers
- grade answers
- show feedback
- update hearts
- record mistakes
- award XP
- finish lesson
- save completion

## Required UI States

- loading
- active question
- correct feedback
- incorrect feedback
- explanation
- session progress
- out-of-hearts
- completion
- network/backend error

## Checklist

- [ ] lesson attempt model
- [ ] exercise attempt model
- [ ] start endpoint
- [ ] answer endpoint
- [ ] completion endpoint
- [ ] answer cannot be submitted twice unintentionally
- [ ] grading occurs server-side for authoritative state
- [ ] frontend immediately communicates result
- [ ] progress bar updates
- [ ] accidental refresh behavior is defined
- [ ] abandoned attempt behavior is defined

## Acceptance Tests

- [ ] complete a lesson successfully
- [ ] answer incorrectly and continue
- [ ] refresh during a lesson without corrupting state
- [ ] replay completed lesson
- [ ] invalid answer payload rejected
- [ ] manipulated frontend cannot award arbitrary XP

---

# 14. Phase 5 — Exercise Types

Each exercise type is its own subphase.

---

## 5A. Multiple Choice

### Checklist

- [ ] prompt
- [ ] choices
- [ ] exactly one or supported multiple correct answers
- [ ] visual selected state
- [ ] keyboard selection
- [ ] answer validation
- [ ] correct/incorrect feedback
- [ ] explanation support

### Acceptance

- [ ] choice order may be randomized without losing answer identity
- [ ] duplicate answer labels are handled safely
- [ ] no answer revealed before submission

---

## 5B. Translation

### Checklist

- [ ] source sentence
- [ ] target answer
- [ ] normalized text comparison strategy
- [ ] accepted alternate answers
- [ ] whitespace normalization
- [ ] punctuation policy
- [ ] case-sensitivity policy
- [ ] explanation

### Important

Do not use naive exact-string equality only.

Support explicitly authored accepted answers.

---

## 5C. Fill in the Blank

### Checklist

- [ ] sentence/template
- [ ] blank representation
- [ ] accepted answers
- [ ] case policy
- [ ] punctuation policy
- [ ] feedback

---

## 5D. Sentence Ordering

### Checklist

- [ ] tokenized sentence pieces
- [ ] draggable/clickable reorder UI
- [ ] keyboard-compatible alternative
- [ ] deterministic answer sequence
- [ ] duplicate-word handling
- [ ] reset
- [ ] grading

---

## 5E. Matching

P1 unless needed earlier.

### Checklist

- [ ] left/right item sets
- [ ] shuffled layout
- [ ] pair state
- [ ] correct-match state
- [ ] incorrect-match feedback
- [ ] completion rule
- [ ] accessibility labels

---

# 15. Phase 6 — Hearts System

## Goal

Implement a transparent lives/mistake mechanic.

## Rules to Define

Before coding, write the exact rules:

- starting/max hearts
- what actions consume hearts
- whether practice can restore hearts
- whether lesson replay consumes hearts
- whether hearts regenerate with time
- local-time handling

## Checklist

- [ ] hearts persisted
- [ ] max hearts enforced
- [ ] wrong eligible answer reduces heart count
- [ ] no negative hearts
- [ ] out-of-hearts flow
- [ ] restoration method
- [ ] transaction-safe update
- [ ] UI indicator

## Acceptance Tests

- [ ] wrong answers decrement correctly
- [ ] correct answer does not decrement
- [ ] refresh cannot restore hearts accidentally
- [ ] concurrent requests cannot create invalid count

---

# 16. Phase 7 — XP and Levels

## Goal

Make progress measurable without allowing client-side cheating.

## XP Rules

Create a centralized XP policy.

Examples:

- base lesson completion XP
- correct-answer bonus if desired
- review XP
- perfect lesson bonus
- daily goal contribution

## Checklist

- [ ] XP event ledger
- [ ] current total derived or safely cached
- [ ] server calculates XP
- [ ] lesson completion awards once
- [ ] replay award policy defined
- [ ] level thresholds defined
- [ ] UI shows XP
- [ ] completion screen shows gained XP

## Acceptance Tests

- [ ] resubmitting completion cannot duplicate XP
- [ ] client cannot specify arbitrary XP amount
- [ ] ledger equals displayed total
- [ ] level changes at correct threshold

---

# 17. Phase 8 — Streak and Daily Goal

## Goal

Create reliable date-based engagement tracking.

## Required Decisions

- local day boundary
- target timezone
- what activity counts
- grace period if any
- streak freeze policy if any
- daily XP target options

## Checklist

- [ ] daily activity record
- [ ] streak calculation
- [ ] daily goal model
- [ ] today progress indicator
- [ ] streak displayed
- [ ] no double increment same day
- [ ] missed-day behavior tested

## Acceptance Tests

Use deterministic mocked dates.

- [ ] first active day = expected streak
- [ ] second consecutive day increments
- [ ] multiple activities same day do not over-increment
- [ ] missed day resets or applies defined freeze rule
- [ ] date behavior does not depend on test machine clock unpredictably

---

# 18. Phase 9 — Mistake Tracking and Review

## Goal

Wrong answers become future learning opportunities.

## Checklist

- [ ] wrong exercise recorded
- [ ] repeated mistakes counted
- [ ] mistake history query
- [ ] review queue
- [ ] dedicated mistake review UI
- [ ] successful review updates item state
- [ ] deleted/changed source content handled safely

## Acceptance Tests

- [ ] wrong answer appears in review
- [ ] same mistake does not create uncontrolled duplicates
- [ ] review result persists
- [ ] completed review can reappear later according to schedule

---

# 19. Phase 10 — FSRS Spaced Repetition

## Goal

Use a real spaced-repetition scheduler for vocabulary/concept review.

## Review Item State

Store scheduler-required state, for example:

- due date
- stability
- difficulty
- elapsed days
- scheduled days
- repetitions
- lapses
- state
- last review

Do not invent an incompatible simplified system and call it FSRS.

## Ratings

Use familiar review feedback:

- Again
- Hard
- Good
- Easy

## Checklist

- [ ] scheduler integrated
- [ ] review item creation
- [ ] due queue
- [ ] rating endpoint/action
- [ ] review log
- [ ] next due date stored
- [ ] timezone/date serialization verified
- [ ] deterministic scheduler tests

## Acceptance Tests

- [ ] new item can be reviewed
- [ ] all four ratings produce valid next state
- [ ] due items return in expected order
- [ ] review logs are preserved
- [ ] app restart preserves schedule

---

# 20. Phase 11 — Achievements

## Goal

Reward meaningful milestones.

## Architecture Rule

Achievement definitions should be data-driven.

Examples:

- first lesson completed
- 100 XP
- 7-day streak
- 10 perfect lessons
- 50 review items completed

## Checklist

- [ ] achievement definitions
- [ ] unlock conditions
- [ ] unlocked timestamp
- [ ] no duplicate unlock
- [ ] achievement screen
- [ ] unlock notification

## Acceptance Tests

- [ ] achievement unlocks exactly once
- [ ] historical progress can trigger eligible achievements if designed to do so
- [ ] locked achievements display safely

---

# 21. Phase 12 — Statistics and Progress Dashboard

## Required Metrics

- total XP
- XP today
- current streak
- longest streak
- lessons completed
- course completion
- exercises attempted
- accuracy
- mistakes
- reviews due
- reviews completed
- achievement count

## Checklist

- [ ] stats endpoints
- [ ] dashboard cards
- [ ] no division-by-zero bugs
- [ ] empty profile display
- [ ] large values format safely

---

# 22. Phase 13 — AI Explanation Layer

## Goal

Optional local AI assistance without making lessons dependent on AI.

## Rules

AI MUST NOT determine authoritative grading for normal exercises.

Primary uses:

- explain why an answer is wrong
- rephrase a grammar explanation
- give another example
- answer a learner's follow-up within bounded context

## Provider Design

Configuration should allow:

```text
AI Enabled: true/false
Provider: LM Studio / OpenAI-Compatible
Base URL
Model
Timeout
```

Secrets/API keys must never be committed.

## Checklist

- [ ] provider interface
- [ ] disabled provider
- [ ] LM Studio-compatible provider
- [ ] provider health check
- [ ] timeout
- [ ] graceful failure
- [ ] structured request/response validation
- [ ] no AI failure blocks lesson completion
- [ ] safe fallback explanation from authored content

## Acceptance Tests

- [ ] app works with AI disabled
- [ ] unavailable endpoint does not crash UI
- [ ] provider can be swapped by configuration
- [ ] invalid AI response rejected gracefully

---

# 23. Phase 14 — Audio and Listening

P2 feature.

## Text-to-Speech

- [ ] abstraction for TTS provider
- [ ] generated/cached audio strategy
- [ ] play/replay button
- [ ] speed control if useful
- [ ] missing audio fallback
- [ ] no autoplay surprise

## Listening Exercise

- [ ] audio prompt
- [ ] replay
- [ ] optional slow playback
- [ ] answer input
- [ ] grading

## Acceptance

- [ ] app remains usable without TTS installed
- [ ] missing audio engine does not break course

---

# 24. Phase 15 — Speech / Pronunciation

P2 feature.

## Pipeline

```text
Microphone
  ↓
Capture Audio
  ↓
Speech-to-Text
  ↓
Normalize Transcript
  ↓
Compare with Expected Phrase
  ↓
Feedback
```

## Important

Do not claim precise phoneme-level pronunciation scoring unless the implementation actually supports it.

A speech-to-text similarity score is not the same as true pronunciation assessment.

## Checklist

- [ ] microphone permission handling
- [ ] recording state
- [ ] cancel/retry
- [ ] STT provider abstraction
- [ ] transcript shown
- [ ] comparison logic
- [ ] privacy note
- [ ] failure fallback

---

# 25. Phase 16 — Settings

## Settings Candidates

- [ ] sound effects
- [ ] animations/reduced motion
- [ ] daily goal
- [ ] UI language
- [ ] target language/course
- [ ] AI enabled
- [ ] AI provider config
- [ ] TTS/STT config
- [ ] reset progress
- [ ] export data
- [ ] import backup

Dangerous actions need confirmation.

---

# 26. Phase 17 — Accessibility and Responsive Design

## Minimum Requirements

- [ ] usable at 320px width
- [ ] usable desktop layout
- [ ] keyboard navigation
- [ ] visible focus state
- [ ] buttons have accessible names
- [ ] form controls have labels
- [ ] no color-only correctness indicator
- [ ] sufficient contrast
- [ ] reduced-motion support where practical
- [ ] dialogs trap/restore focus properly
- [ ] error messages associated with inputs

---

# 27. Phase 18 — Testing Strategy

## Backend

Required categories:

- unit tests
- service tests
- API tests
- database tests
- progression tests
- XP tests
- hearts tests
- streak/date tests
- review scheduler tests

## Frontend

Required categories:

- schema tests
- component tests for exercise types
- state/logic tests
- critical flow tests

## End-to-End Critical Flows

At minimum test:

1. start new profile
2. open first course
3. enter unlocked lesson
4. answer correct
5. answer incorrect
6. lose heart
7. finish lesson
8. receive XP
9. unlock next lesson
10. refresh/restart
11. confirm progress persists
12. review a mistake
13. confirm review state persists

## Global Test Gate

Before marking a major phase complete:

- [ ] backend tests pass
- [ ] frontend tests pass
- [ ] typecheck passes
- [ ] lint passes
- [ ] production frontend build passes
- [ ] migrations apply from clean database
- [ ] manual smoke test passes

---

# 28. Phase 19 — Security and Data Integrity

Even though the project is local-first, do not ignore basic security.

## Checklist

- [ ] no hard-coded secrets
- [ ] `.env` ignored
- [ ] API validates all incoming data
- [ ] SQL uses ORM/parameterized queries
- [ ] path traversal not possible in any file-related feature
- [ ] unsafe HTML is not rendered directly
- [ ] CORS is not `*` without reason
- [ ] destructive operations confirmed
- [ ] XP/progression rules enforced server-side
- [ ] database migrations are reversible where practical
- [ ] backup/restore documented before destructive schema changes

---

# 29. Phase 20 — Performance

## Checklist

- [ ] no N+1 query pattern in course map
- [ ] indexes for frequently queried foreign keys/dates
- [ ] large histories paginated
- [ ] expensive stats aggregated efficiently
- [ ] components avoid needless rerenders
- [ ] audio assets lazy loaded
- [ ] course data is not repeatedly refetched without reason
- [ ] startup remains reasonable on target Windows laptop

---

# 30. Phase 21 — UI Polish

Only after core logic is correct.

## Checklist

- [ ] consistent spacing
- [ ] coherent typography
- [ ] consistent card/button variants
- [ ] smooth but restrained transitions
- [ ] correct/incorrect feedback visually distinct
- [ ] clear progress hierarchy
- [ ] empty/loading/error states polished
- [ ] mobile interaction targets large enough
- [ ] original branding/assets

Avoid spending large amounts of time mimicking Duolingo pixel-for-pixel.

---

# 31. Phase 22 — Backup, Export, and Restore

Recommended for local-first reliability.

## Minimum

- [ ] export user/progress data
- [ ] export course content if custom content exists
- [ ] backup SQLite DB
- [ ] restore documented
- [ ] schema/version validation on import
- [ ] invalid backup fails safely

---

# 32. Phase 23 — Packaging / Local Launch Experience

The end goal is a project that is easy to run.

Possible later options:

- one-command dev launcher
- PowerShell launcher
- Docker for optional reproducible environment
- desktop wrapper only if actually useful
- PWA/offline install

Do not introduce Docker merely for complexity if local native startup is already reliable.

## Acceptance

A clean machine with prerequisites should be able to follow README and launch the project without hidden steps.

---

# 33. Regression Checklist

Run this after any substantial change.

## Course and Content

- [ ] course loads
- [ ] unit order correct
- [ ] lesson order correct
- [ ] lock state correct
- [ ] original content still validates

## Lesson Engine

- [ ] lesson starts
- [ ] exercise renders
- [ ] answer submits
- [ ] feedback displays
- [ ] next question works
- [ ] completion works

## Progression

- [ ] XP correct
- [ ] hearts correct
- [ ] streak correct
- [ ] daily goal correct
- [ ] next lesson unlocks
- [ ] replay remains valid

## Review

- [ ] mistakes recorded
- [ ] review queue loads
- [ ] FSRS state valid
- [ ] due dates valid

## Technical

- [ ] no frontend console errors
- [ ] no backend tracebacks
- [ ] lint passes
- [ ] typecheck passes
- [ ] tests pass
- [ ] production build passes
- [ ] migrations apply

---

# 34. AI Agent End-of-Task Report

At the end of every implementation session, the coding agent MUST report:

```text
TASK:
What was requested?

IMPLEMENTED:
- ...

FILES CHANGED:
- ...

DATABASE/MIGRATIONS:
- ...

TESTS RUN:
- command -> result
- command -> result

MANUAL CHECKS:
- ...

KNOWN LIMITATIONS:
- ...

CHECKLIST ITEMS COMPLETED:
- ...

CHECKLIST ITEMS STILL OPEN:
- ...

NEXT RECOMMENDED TASK:
- ...
```

Never report “all done” without naming tests actually run.

---

# 35. Anti-Slop / Anti-Incomplete Checklist

Before finishing any task, verify:

- [ ] no placeholder text remains unless intentionally marked
- [ ] no fake data is presented as completed production data
- [ ] no button is visually present but nonfunctional
- [ ] no route links to a missing page
- [ ] no TODO is hidden inside a supposedly completed feature
- [ ] no duplicated component exists without reason
- [ ] no copied code block should be a shared utility
- [ ] no unexplained magic number controls progression
- [ ] no hard-coded user/profile ID in production path
- [ ] no hard-coded course ID in generic components
- [ ] no silent exception swallowing
- [ ] no empty `catch` blocks
- [ ] no `any` used merely to bypass TypeScript errors
- [ ] no disabled test used to make CI pass
- [ ] no migration skipped after schema changes
- [ ] no API contract mismatch between frontend and backend
- [ ] no stale comments contradict current behavior
- [ ] no inaccurate README instructions
- [ ] no fake "AI-powered" behavior when AI is unavailable

---

# 36. MVP Completion Gate

P0 MVP is complete only if ALL are true:

- [ ] app launches locally from documented instructions
- [ ] original sample course exists
- [ ] course map works
- [ ] lesson unlock rules work
- [ ] multiple choice works
- [ ] translation works
- [ ] fill-in-the-blank works
- [ ] sentence ordering works
- [ ] answer grading is authoritative
- [ ] progress persists
- [ ] XP persists
- [ ] hearts persist
- [ ] streak works
- [ ] daily goal works
- [ ] mistakes are recorded
- [ ] review queue works
- [ ] responsive UI works
- [ ] no critical console errors
- [ ] no critical backend errors
- [ ] automated tests pass
- [ ] production build passes
- [ ] clean DB migrations pass
- [ ] README startup steps verified

---

# 37. P1 Completion Gate

P1 is complete only if:

- [ ] matching works
- [ ] achievements work
- [ ] levels work
- [ ] statistics dashboard works
- [ ] FSRS scheduling works
- [ ] mistake review experience is polished
- [ ] settings work
- [ ] keyboard accessibility improved
- [ ] AI provider layer works
- [ ] app works with AI completely disabled
- [ ] LM Studio can be configured without code changes
- [ ] regression checklist passes

---

# 38. P2 Completion Gate

P2 is complete only if implemented features are real, not cosmetic:

- [ ] TTS/listening works if included
- [ ] STT/speaking works if included
- [ ] pronunciation claims match actual capability
- [ ] adaptive difficulty has documented logic if included
- [ ] multiple courses remain data-driven
- [ ] import/export is validated
- [ ] performance remains acceptable
- [ ] regression suite passes

---

# 39. Final Product Goal

The project should feel like a complete personal language-learning platform rather than a static Duolingo UI mockup.

A successful result has:

```text
Original Course Content
        ↓
Structured Course Model
        ↓
Course Map
        ↓
Lesson Engine
        ↓
Reusable Exercise Types
        ↓
Authoritative Grading
        ↓
XP / Hearts / Streak / Goals
        ↓
Mistake Review + FSRS
        ↓
Achievements + Statistics
        ↓
Optional AI + Audio
```

The core app must remain useful when every optional AI/audio provider is turned off.
