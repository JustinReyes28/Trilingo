# Foundation decisions — 2026-10-23

## Product and scope
One local learner on Windows, Japanese with English explanations. First personal release is A-B; C-F remain approved later curriculum releases. Personal quests, badges, stories, challenges and records are planned; no public social service or fabricated competitors. All published activities are directly available; order/goals/review are suggestions. No resource balances, quotas, XP ceilings or access prerequisites.

Phase 1-3 delivers the connected shell, settings and content browsing. Lessons/grading/sessions/XP start in Phase 4. Reading/writing/audio/review modes are explicitly Upcoming. Development fixtures never write learning evidence.

## Runtime and dependencies
Supported target: Node 24 LTS and Python 3.11+. Actual checks here used the existing Node 25.2.1 and Python 3.14.0; a supported-Node validation run remains open because the runtime download was interrupted to respect cellular-data limits. Vite requires at least Node 20.19/22.12 ([official guide](https://vite.dev/guide/)). No system runtime was changed.

React/strict TypeScript/Vite/Tailwind/Zod; FastAPI/Pydantic/SQLAlchemy/Alembic; SQLite. Frontend exact versions and the lockfile are retained. To respect the user's cellular cap, installed local development tools and verified cached archives were reused. Rolldown1.2.14 is explicitly pinned to its already available compatible Windows binding. An offline npm-ci dry run validates manifest/lock consistency; it does not establish a complete fresh dependency install.

Python requirements.lock pins the successfully installed isolated environment. requirements.in describes direct requirements; update the lock deliberately after future dependency changes. Dependencies were installed only into .venv, never into the user's global Python.

## Persistence and content
Migrations0001 and 0002 create profile/preferences and versioned courses/enrollment/assistance respectively. Runtime never calls create_all. Relative DB URLs resolve against the project root. Tests use disposable migrated databases; QA/launcher use separate .data databases.

The small local course is an immutable validated JSON graph stored in CourseVersion, with Course pointing to its current version. Pydantic supplies course/unit/lesson/concept/lexical/exercise/stage/task and extension models. This preserves complete historical content without dozens of premature relational tables. Import rejects changed bytes under an existing version, preserves older snapshots and assistance references, and is idempotent. Phase 4 adds durable session/answer/evidence models rather than reusing assistance as a correctness claim.

Answer keys/hints/explanations are excluded from ordinary lesson responses. Explicit hint/reveal records a server-validated idempotent assistance event; it never grants or revokes access. Frontend validates external data with Zod. OpenAPI describes typed public responses separately from ORM/private content.

UTC event timestamps and profile-local timezone are distinct. Initial browser connection supplies its detected IANA zone; Asia/Singapore is offered and all valid IANA zones are accepted. Concurrent first setup is atomic. There is no streak/progression logic yet.

## FSRS and providers
Selected [py-fsrs6.3.2](https://github.com/open-spaced-repetition/py-fsrs) (MIT, Python>=3.10). Foundation smoke tests verify deterministic public review transitions with fuzzing disabled. Phase 9 will own persisted card states, parameters/version, due dates and logs; no current queue is labeled FSRS.

Provider preferences are disabled by default and independent for AI/TTS/STT. Local URL/model/voice/timeout configuration is durable; adapters arrive in Phases 7-8. No secrets are exposed. No provider calls occur today, even if an enabled flag is supplied. Health reports actual implemented capabilities.

Docker inspection on2026-10-23 still cannot reach dockerDesktopLinuxEngine. Kokoro wrapper/image/voice/endpoint/playback remain unverified. No containers were started, models downloaded, or VHDX data touched. This does not block foundation/content work.

## Bundled-audio-only amendment — 2026-11-13

- The historical 2026-10-23 provider note above is superseded for TTS: runtime TTS providers, `TTS_ENABLED`, `AUDIO_CACHE_DIR`, `preferences.data.tts`, and `voice` subfields were removed in schema `0014` (2026-11-13).
- Reference audio is served strictly from the bundled `content/audio/<course>/<version>/` MP3 pack (`AUDIO_PACK_DIR` / `AUDIO_PACK_ENABLED`); AI (`AI_ENABLED`) and STT (`STT_ENABLED`) are the only optional local runtime providers, and `GET /api/v1/health` reports `features: {lessons, ai, stt}`.

## Local security and data use
Loopback defaults, explicit local CORS, 64KiB JSON request bounds, field validation, structured errors and secret-free startup logging. Provider URLs cannot act as arbitrary per-request proxies. AI/audio disabled operation is the baseline. No remote fonts, telemetry, images or browser downloads are required. Local browser verification blocks all non-loopback requests.

After the user's10MB allowance, the metered dependency process stopped at 9,794,938 counted body bytes (conservative decompressed accounting). No allowance increase was assumed; repeated metadata retrieval was detected and bounded. All subsequent tooling reuse, browser checks and builds were local. The earlier incomplete runtime file was discarded.
