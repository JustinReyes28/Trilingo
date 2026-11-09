# Phase 01 — Foundation and Technical Decisions

Status: Implemented; verification partial. Fresh frontend installation on supported Node 24 LTS remains unverified under the cellular cap. Depends on: none. Next: [Phase 02](PHASE_02_INTERFACE.md).

## Goal

Create a reliable Windows development foundation for one local learner. Resolve architectural decisions before implementing learning logic.

## Starting evidence

- On 2026-10-22, the repository contained only `AGENTS.md` and `AI_IMPLEMENTATION_PLAN.md`; the planning task adds documentation.
- Existing application features: none. Missing: frontend, backend, README at initial inspection, database, migrations, content, and tests.
- Broken/partial application features: not applicable; no app exists. Technical debt: no executable baseline or recorded contracts.
- `git status --short` reported that this directory is not a Git repository. Establish source control deliberately; do not assume previous commits exist.
- Installed runtimes observed: Python 3.14.0 and Node.js 25.2.1. These observations are not the selected support baseline. Check dependency compatibility and choose a supported Node LTS and Python 3.11+ at implementation time.
- Docker CLI and the supplied VHDX exist; the Linux engine was unreachable during the initial inspection. The user subsequently identified Kokoro TTS. Upstream Japanese support is documented; installed wrapper/version, voice/dependencies, endpoint, and playback remain unverified.

## Deliverables

- [x] Record decisions: beginner Japanese, English explanations, one local profile, everyday communication, Japanese typing plus handwriting practice.
- [x] Record first-release Stages A-B versus the approved later C-F essay path from the [curriculum roadmap](../CURRICULUM_ROADMAP.md). Keep release scope, published content, and learner skill evidence distinct.
- [x] Record the combined Duolingo/Babbel personal feature scope from the master plan, including quests, badges, challenges, stories, and personal bests. Do not add public social infrastructure or invented competitors.
- [x] Record unrestricted study as mandatory: direct published-content access, freely selected order, unlimited continuation/replay/new sessions, uncapped genuine-session XP, optional goals/review, and honest evidence without learner-resource barriers.
- [x] Default the profile timezone to the system-detected IANA timezone, offer `Asia/Singapore` for this environment, and allow changes. Do not embed the timezone in streak logic.
- [x] Offer an optional editable daily routine/goal and review suggestion that can be hidden or ignored, with no study quota, required daily activity, or promised fluency/exam schedule.
- [x] Scaffold React/TypeScript/Vite/Tailwind/Zod and FastAPI/Pydantic/SQLAlchemy/Alembic in the structure below.
- [x] Configure strict TypeScript, ESLint, frontend tests, backend tests, isolated test DBs, and a reproducible dependency lock strategy.
- [x] Choose a maintained Python FSRS library after checking its official documentation, version, license, and deterministic API. Backend owns scheduling; avoid an extra TypeScript scheduling service.
- [x] Add centralized configuration, `.env.example`, `.gitignore`, logging without secrets, consistent errors, and intentionally restricted local CORS.
- [x] Bind local services to loopback by default. Add basic input limits; provider URLs are local settings, never arbitrary per-request proxy targets.
- [x] Add initial migration for profiles and durable settings; connect SQLite through migrations, not runtime `create_all`.
- [x] Implement health/profile/settings endpoints and a frontend API client that validates responses.
- [x] Add error boundary, loading/error primitives, real health connection screen, and launch instructions actually verified on Windows.
- [ ] Record the existing Kokoro TTS wrapper/version and Phase 8's Japanese voice/dependency/playback audit when Docker becomes available. Treat the user's identification as planning input, not a completed playback test; foundation work must continue if unavailable.

## Intended implementation areas

`frontend/src/{app, components, features, lib, schemas, services, styles}`, `frontend/tests`, `backend/app/{api, core, db, models, schemas, services, repositories}`, `backend/migrations`, `backend/tests`, `content/courses/ja`, and `scripts`.

These paths are targets, not existing code. Inspect before creating later additions.

## Data and API contracts

- Use `/api/v1` consistently. Establish `GET /health`, `GET/PATCH /profile`, and `GET/PATCH /settings` under this prefix.
- Responses have explicit schemas. Errors include a stable code, user-facing message, and optional field details; unexpected failures do not expose stack traces.
- Profile stores stable ID and timezone. Settings store daily goal, reading aids, accessibility preferences, and provider preferences with explicit ownership.
- Store secrets outside public API responses and exported ordinary settings. Validate configuration changes server-side.
- Adopt UTC timestamps for events and due dates; derive activity dates using the profile timezone at the time of activity.
- Configure separate database locations for real use, tests, and temporary migration validation.
- Define `AI_ENABLED=false` and independent TTS/STT enabled/provider/base URL/model-or-voice/timeout settings. Do not assume all services use OpenAI-compatible endpoints.

## Tests and manual verification

- [x] Backend tests cover config validation, profile/settings validation, health responses, and test database isolation.
- [x] Frontend tests cover valid/invalid API data, health loading/failure/retry, and error boundaries where practical.
- [x] Apply migrations on an empty temporary DB, run migration drift check, restart, and confirm persisted settings.
- [x] Run the frontend gate and backend gate defined in the master plan; record actual commands and versions in README.
- [x] Manually launch both services using only README, call the health API, then verify a usable UI with AI/audio disabled.
- [x] Confirm no secret, personal DB, recording, model weights, or provider cache is added to source control.

## Completion gate

Complete only when a clean install can launch the real frontend/backend, health calls work, settings survive restart, migrations work from empty DB, tests are isolated, and applicable quality gates pass. An unavailable optional TTS engine must be reported honestly and must not block this phase.


## Implementation evidence — 2026-10-23

See [technical decisions](../TECHNICAL_DECISIONS.md) and [verification](../PHASE_01_03_VERIFICATION.md). Current-machine launch, persistence, migrations, isolated tests and quality gates pass. The full phase gate stays open until a fresh frontend install is verified on Node 24 LTS. Existing Node 25.2.1 was used; no system runtime was changed. A local-only cache audit found 151 Windows-compatible lock entries without archives, including mandatory TypeScript; a full offline clean install cannot currently be verified. No further downloads were attempted. Docker remains unavailable, so its conditional provider audit is still open and does not block independent work.


## Plan 9.2 follow-up — 2026-10-23

[Current execution evidence](../PLAN_09_2_VERIFICATION.md) records source 0.1.15/schema 0012, verified engineering changes and exact remaining gates. The supported fresh-install, qualified-language/stroke/audio and physical-device requirements remain open. Current improvements include verified official IME documentation, ten-topic draft guide coverage, collection-scoped saved-snapshot recall, complete timing histories and separate skill/workflow/coverage evidence. No full phase or reviewed beginner release is claimed.
