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
- [x] Superseded (2026-11-13 bundled-audio-only): runtime Kokoro TTS wrapper discovery and runtime TTS setup were replaced by the committed static MP3 pack (`content/audio/ja-starter/0.1.21/`); there is no runtime TTS service. See [PHASE_08_AUDIO_SPEAKING.md](PHASE_08_AUDIO_SPEAKING.md) and [AUDIO_PACK.md](../AUDIO_PACK.md).

## Intended implementation areas

`frontend/src/{app, components, features, lib, schemas, services, styles}`, `frontend/tests`, `backend/app/{api, core, db, models, schemas, services, repositories}`, `backend/migrations`, `backend/tests`, `content/courses/ja`, and `scripts`.

These paths are targets, not existing code. Inspect before creating later additions.

## Data and API contracts

- Use `/api/v1` consistently. Establish `GET /api/v1/health`, `GET/PATCH /api/v1/profile`, `GET/PATCH /api/v1/settings`, and `GET /api/v1/audio/status` (which replaced `/api/v1/providers/status` in schema `0015`) under `/api/v1`.
- Responses have explicit schemas. Errors include a stable code, user-facing message, and optional field details; unexpected failures do not expose stack traces.
- Profile stores stable ID and timezone. Settings store daily goal, reading aids, and accessibility preferences with explicit ownership (optional provider preferences were removed in schema `0015`).
- Store secrets outside public API responses and exported ordinary settings. Validate configuration changes server-side.
- Adopt UTC timestamps for events and due dates; derive activity dates using the profile timezone at the time of activity.
- Configure separate database locations for real use, tests, and temporary migration validation.
- Define `AUDIO_PACK_DIR`/`AUDIO_PACK_ENABLED` for the bundled MP3 pack. *(Superseded 2026-11-13: `TTS_ENABLED`/`AUDIO_CACHE_DIR` were removed in schema `0014`, and `AI_ENABLED`, `STT_ENABLED`, `"ai"`, and `"stt"` preference fields were removed in schema `0015`.)*

## Tests and manual verification

- [x] Backend tests cover config validation, profile/settings validation, health responses, and test database isolation.
- [x] Frontend tests cover valid/invalid API data, health loading/failure/retry, and error boundaries where practical.
- [x] Apply migrations on an empty temporary DB, run migration drift check, restart, and confirm persisted settings.
- [x] Run the frontend gate and backend gate defined in the master plan; record actual commands and versions in README.
- [x] Manually launch both services using only README, call the health API, then verify a usable UI with bundled audio disabled (`AUDIO_PACK_ENABLED=false`).
- [x] Confirm no secret, personal DB, recording, model weights, or provider cache is added to source control.

## Completion gate

Complete only when a clean install can launch the real frontend/backend, health calls work, settings survive restart, migrations work from empty DB, tests are isolated, and applicable quality gates pass. Unavailable bundled audio must be reported honestly (`503 audio_unavailable` / `GET /api/v1/audio/status`) and must not block this phase.


## Implementation evidence — 2026-10-23

See [technical decisions](../TECHNICAL_DECISIONS.md) and [verification](../PHASE_01_03_VERIFICATION.md). Current-machine launch, persistence, migrations, isolated tests and quality gates pass. The full phase gate stays open until a fresh frontend install is verified on Node 24 LTS. Existing Node 25.2.1 was used; no system runtime was changed. A local-only cache audit found 151 Windows-compatible lock entries without archives, including mandatory TypeScript; a full offline clean install cannot currently be verified. No further downloads were attempted. Docker remains unavailable, so its conditional provider audit is still open and does not block independent work.


## Plan 9.2 follow-up — 2026-10-23

[Current execution evidence](../PLAN_09_2_VERIFICATION.md) records source 0.1.15/schema 0012, verified engineering changes and exact remaining gates. The supported fresh-install, qualified-language/stroke/audio and physical-device requirements remain open. Current improvements include verified official IME documentation, ten-topic draft guide coverage, collection-scoped saved-snapshot recall, complete timing histories and separate skill/workflow/coverage evidence. No full phase or reviewed beginner release is claimed.

## Bundled-audio-only & local-only amendments — 2026-11-13

- Schema head advanced to **`0014`** (`0014_remove_tts_settings.py`), removing `"tts"` and `ai.voice`/`stt.voice` from `preferences.data` and imported backups while preserving all learner tables.
- Schema head subsequently advanced to **`0015`** (`0015_remove_ai_stt_settings.py`, 2026-11-13), removing `"ai"`, `"stt"`, and `"tts"` from `preferences.data` and imported backups while preserving all learner progress.
- `.env.example` and `Config` retain only `AUDIO_PACK_DIR` and `AUDIO_PACK_ENABLED` (`TTS_ENABLED`, `AUDIO_CACHE_DIR`, `AI_ENABLED`, and `STT_ENABLED` removed). `GET /api/v1/health` returns `features: {lessons: true}`, and `GET /api/v1/audio/status` returns `{audio_pack}`.
