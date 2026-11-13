# Changelog

All notable changes to Trilingo are recorded here. The project is pre-release;
entries are grouped by date and describe the verified scope, not a published
release.

## Unreleased — 2026-11-13

### Bundled-Audio-Only Architecture (2026-11-13, Phases 1–3)

Following the initial pack introduction recorded below, all runtime TTS support
was removed so authored audio is strictly bundled-only (`content/audio/`):

- **Schema `0014` (`backend/migrations/versions/0014_remove_tts_settings.py`):**
  Strips legacy `tts` and `ai.voice`/`stt.voice` keys from `preferences.data`
  without modifying XP, FSRS cards, sessions, collections, or drafts;
  `restore_backup` and settings services normalize older backups identically.
- **Removed runtime TTS endpoints, settings, and adapters:** Removed
  `TTS_ENABLED`, `AUDIO_CACHE_DIR`, `POST /api/v1/scenarios/speech`,
  `GET /api/v1/audio/voices`, and runtime TTS synthesis helpers in `providers.py`
  and `audio_api.py`. `GET /api/v1/health` now returns `features: {lessons, ai, stt}`;
  `GET /api/v1/providers/status` returns `{ai, stt, audio_pack}`; authored audio
  endpoints serve `source="pack"` (`audio/mpeg`) or return HTTP `503`
  (`audio_unavailable`) on miss/disabled pack. AI scenario practice is text-only
  plus optional STT (`STT_ENABLED`).
- **Frontend & Docs:** Removed TTS provider controls from `ProfilePage.tsx`,
  removed advisory speech playback from `ScenarioPractice.tsx`, simplified
  `AudioControls` to pack-only playback with client `0.75x` (`preservesPitch=true`),
  updated Zod contracts (`schemas.ts`, `practiceSchemas.ts`), removed
  `TTS_ENABLED`/`AUDIO_CACHE_DIR` from `.env.example`, and migrated docs/plans
  and script docstrings (`build_audio_pack.py` retained as optional maintainer-only
  generator for future `0.1.22+` packs; `check_audio_pack.py` remains active in CI).
- **Verified (post-Phase-1–3 integrated pass, 2026-11-13):**
  - Backend: Ruff (`backend/{app,migrations,tests}` and
    `scripts/{audio_pack_common,build_audio_pack,check_audio_pack}.py`),
    `238 passed` in `pytest` (exit 0), `python -m app.cli validate`, and
    `check_audio_pack.py --strict` (`4,394` expected/manifest, `0` errors/warnings).
  - Isolated Alembic `0013 -> 0014` (`clean.db` + populated pre-`0014` `"tts"` /
    `voice` DB): `alembic check` clean, repeat `app.cli import` idempotent
    (`imported_new_version: false`), `"tts"` and `"voice"` keys stripped while
    learner counts and XP (`15`) preserved.
  - Frontend: ESLint, TypeScript `typecheck`, `53 passed` across `11` Vitest
    files, and production build (`2,071` modules, `986ms`).
  - Isolated Playwright UI + HTTP QA (`AI_ENABLED=false`, `STT_ENABLED=false`,
    `AUDIO_PACK_ENABLED=true`, plus `AUDIO_PACK_ENABLED=false` `503` `audio_unavailable`
    check): `28` viewport checks (`320`/`390`/`768`/`1280` across Profile, Audio,
    Grammar/Scenario, Session, Story, Listening, Collections), `0` overflows,
    `0` console/page errors, `0` external requests, `0` `/scenarios/speech`,
    `/audio/voices`, or `:8880` requests across `169` requests; Japanese/English
    MP3 playback, `0.75x` (`preservesPitch=true`), text-only coaching, Story,
    Listening, Speaking, Collections, and Backup export/restore verified (after
    waiting for background requests before restore on Windows SQLite).

### Initial Bundled Reference-Audio Pack Addition (2026-11-13, pre-removal)

### Added

- **Bundled reference-audio pack.** Authored Japanese words, audio cues, story
  turns and English vocabulary glosses now ship as versioned MP3 files under
  `content/audio/ja-starter/0.1.21/`, with a validated `manifest.json`.
  - 4,394 clips: 2,211 Japanese + 2,183 English.
  - 91.4 minutes of audio, 87.9 MB of MP3 plus a 2.4 MB manifest (90.4 MB total).
  - Generated once with Kokoro-82M (`jf_alpha` / `af_heart`), 128 kbps MP3.
  - Worked immediately with `TTS_ENABLED=false` and no Kokoro service running.
- **English meaning playback** on the Audio page for vocabulary references.
- **Pack tooling & tests:** `scripts/build_audio_pack.py` (maintainer
  generator), `scripts/check_audio_pack.py` (coverage/hash/duration validator),
  shared content extraction in `scripts/audio_pack_common.py`, and
  fixture/schema tests in `backend/tests/test_audio_pack.py` and
  `frontend/src/audioPack.test.tsx`.
- **Documentation:** [Reference Audio Pack](docs/AUDIO_PACK.md) and
  [Third-Party Notices](THIRD_PARTY_NOTICES.md).

### Changed (initial pre-removal batch)

- Authored audio endpoints (`/audio/speech`, session exercise audio, review-card
  audio) updated to pack lookup (`AudioOut` reports `source="pack"` and `audio/mpeg`).
- `ProviderStatus` adds `audio_pack` (`bundled_reference`, `bundled_reviewed`, `course_version`).
- Slow playback for bundled clips uses browser `playbackRate=0.75` with
  `preservesPitch=true`.
- `backend/requirements.*` adds `mutagen==1.47.0` (`GPL-2.0-or-later`) solely
  for the offline pack build/check scripts (not imported by `backend/app/`
  runtime code; see [Third-Party Notices](THIRD_PARTY_NOTICES.md)).
- `.gitattributes` marks `*.mp3 binary` so Git does not attempt text/EOL
  handling on bundled MP3 files.
- `.github/workflows/ci.yml` adds Ruff checks for the audio-pack scripts,
  `python -m app.cli validate`, and `check_audio_pack.py --strict` to the
  `backend` job.
- `.env.example` adds `AUDIO_PACK_DIR` and `AUDIO_PACK_ENABLED`.

### Fixed

- Runtime-provider backend tests no longer hit the real bundled pack; an autouse
  test fixture disables the pack unless a test opts in.

### Verified (initial 2026-11-13 pack pass, pre-removal)

- **Pre-removal integrated suite (2026-11-13):**
  - Backend: **235 tests passed** (`17` tests in
    `backend/tests/test_audio_pack.py` plus **40** audio/scenario regressions
    across `test_audio_upgrades.py` [3], `test_grammar_audio.py` [12],
    `test_listening.py` [4], `test_review_media.py` [4],
    `test_speaking.py` [5], `test_scenario_practice.py` [10], and
    `test_quest_fallback.py` [2], or **35** across the 6 non-speaking files);
    Ruff passes across `backend/{app,migrations,tests}` and
    `scripts/{audio_pack_common,build_audio_pack,check_audio_pack}.py`;
    `python -m app.cli validate` passes.
  - Frontend: ESLint, TypeScript `typecheck`, **50 tests** (11 files,
    including `6` in `frontend/src/audioPack.test.tsx`), and Vite production
    build pass.
  - Pack checker (`--strict`): **4,394 expected / 4,394 present, 0 missing,
    0 missing required, 0 extra, 0 unreferenced, 0 errors, 0 warnings**.
- **Initial 2026-11-13 pack browser/API check:** Japanese and English playback,
  0.75x with pitch preservation, listening cue and saved review card via the
  pack with `TTS_ENABLED=false`, zero Kokoro/external requests, no JavaScript
  errors or overflow. *(Post-Phase-1–3 verification runs next in Step 4.)*

### Known limitations

- The manifest remains `status=draft`; qualified Japanese listening review and
  English voice spot-check are still required (`bundled_reviewed=false`).
- Runtime TTS/Kokoro is completely removed (zero runtime speech synthesis);
  optional AI (`AI_ENABLED`, text-only scenario coaching) and Whisper-compatible
  STT (`STT_ENABLED`) remain unverified with live local models/microphone.
- The pack adds 90.4 MB to the repository. No model weights or voice packs are
  bundled.
- Schema advanced to `0014` (removes legacy `tts` and `voice` preference keys);
  no content version or learner progress data changed.
