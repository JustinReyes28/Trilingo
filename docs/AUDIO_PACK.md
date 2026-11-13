# Reference Audio Pack

Trilingo plays authored reference audio exclusively from a versioned,
pre-generated static MP3 pack (`content/audio/<course>/<version>/`). There are
zero external or local AI, STT, microphone capture, runtime TTS synthesis, audio
caches, or model/voice downloads anywhere in the application.

## What is generated

The builder covers the current authored content:

- every vocabulary `surface` plus its `pronunciation_override` (draft and
  published, so draft preview and saved review cards work);
- every authored audio cue in lessons and standalone practice;
- every narrative turn (story, dialogue, reading passage, audio episode);
- every vocabulary English `gloss` for the optional meaning playback.

Examples, exercise explanations, hints, guides and UI text are not voiced.

## Layout

```
content/audio/ja-starter/0.1.21/
  manifest.json
  ja/<first-two-key-chars>/<sha256>.mp3
  en/<first-two-key-chars>/<sha256>.mp3
```

The key is a SHA-256 over the text, language, voice, model, format, speed and
pronunciation override. Identical strings share one file. The manifest records
the source hash, engine, voices, licenses, review status, counts, file hashes and
durations. Manifest paths are validated; the server never reads outside the pack
directory.

## Generate (Optional Maintainer-Only Tooling)

Normal study, local development, CI, and release builds use the committed
`0.1.21` MP3 pack directly and never run Kokoro. Maintainers only run this
build-time script when regenerating a future content version (`0.1.22+`) after
authored text, pronunciation overrides, or voices change — with a local
Kokoro-FastAPI service running on a loopback port:

```powershell
.\.venv\Scripts\python.exe scripts\build_audio_pack.py --progress
```

Useful options:

- `--voice-ja jf_alpha` and `--voice-en af_heart` select the voices.
- `--force` regenerates existing clips; without it, valid files are reused and
  the build is resumable.
- `--dry-run` reports the unique clip count.
- `--limit N` is for a small smoke test.
- `--license-*` overrides the manifest attribution.

The builder requests MP3 from Kokoro, validates size/duration with `mutagen`,
writes files atomically and updates `manifest.json` last. It never writes outside
`content/audio/`. Restart the backend after a rebuild so it reloads the manifest;
the running process caches the manifest for the life of the service.

## Validate

```powershell
.\.venv\Scripts\python.exe scripts\check_audio_pack.py `
  --pack content\audio\ja-starter\0.1.21
```

The checker verifies the source hash and course version, computes every expected
key from current content, validates file paths/sizes/SHA-256/durations and
reports missing required (published) clips as errors. Draft gaps are warnings;
`--strict` promotes warnings to errors.

## Runtime behavior

- Pack hits work completely offline with zero runtime AI, STT, or TTS providers
  (there is no `AI_ENABLED`, `STT_ENABLED`, `TTS_ENABLED`, or `AUDIO_CACHE_DIR`
  setting).
- A pack miss or `AUDIO_PACK_ENABLED=false` returns HTTP `503`
  (`audio_unavailable`), and the UI falls back to text alternatives with zero
  loss of study continuation or practice credit.
- Slow playback uses browser `HTMLAudioElement.playbackRate = 0.75` with
  `preservesPitch = true` on the bundled MP3 clips.
- `GET /api/v1/audio/status` reports `{audio_pack}` where `audio_pack` declares
  `{bundled_reference, bundled_reviewed, course_version, message}` (`GET /api/v1/providers/status`
  was removed in schema `0015`). The UI label stays “human review pending”
  until `manifest.status` is changed to `reviewed` by a qualified reviewer.

## Review and licensing

The pack is synthetic reference audio, not evidence of pronunciation mastery.
Human Japanese listening review and an English voice spot-check are still
required before publication. Record reviewer identity/date in `manifest.review`
and change `status` only after approval.

Kokoro-82M is Apache-2.0. The model card lists Koniwa `tnc` (CC BY 3.0) and
SIWIS (CC BY 4.0) audio in the v1.0 training data; see
[THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). Only generated MP3 output is
bundled; model weights and voice packs stay outside the repository.

## Content changes

Any change to authored text, a pronunciation override, a voice or the model
requires maintainers to regenerate and re-validate the pack. If the content
version changes, generate the new version under
`content/audio/<course>/<new-version>/`; old review cards fall back to HTTP `503`
(`audio_unavailable`) and text alternatives when a clip is absent. Do not
silently reuse a manifest whose `source_sha256` no longer matches the course file.

## Implementation record — 2026-11-13

### Local-Only Audio Status Update (2026-11-13, schema `0015`)

Following commit `5e01b81` below, schema `0015` (`0015_remove_ai_stt_settings`) removed all optional local AI (`AI_ENABLED`), Whisper STT (`STT_ENABLED`), and microphone capture paths from Trilingo. `GET /api/v1/providers/status` was replaced by `GET /api/v1/audio/status` returning `{audio_pack}`, `GET /api/v1/health` reports `features: {lessons: true}`, and `"ai"`/`"stt"`/`"tts"` keys are stripped from `preferences.data` without modifying learner progress or backups.

### Initial Pack Addition (2026-11-13, pre-removal)

Source at initial pack generation was **ja-starter 0.1.21** (SHA-256
`94b99042f6f6054ac51807ac5482301cd0e4923bd383aaaa3d94b7d8ff5ea9d5`) on schema
**0013**. *(Historical record before Phase 1–3 removal of runtime TTS; see the
subsequent Bundled-Audio-Only Architecture section below.)*

### Added

- `backend/app/audio_pack.py` — manifest models, safe path/hash validation,
  stable synthesis key, course/version lookup, pack summary and honest labels.
- `backend/tests/test_audio_pack.py` — fixture pack, pack hits with TTS disabled,
  English gloss routing, listening/review delivery, provider-status flag,
  manifest path/duplicate rejection.
- `frontend/src/audioPack.test.tsx` — Zod audio/provider-status schemas, slow
  playback-rate, and vocabulary reference-language rendering tests.
- `scripts/build_audio_pack.py`, `scripts/audio_pack_common.py`,
  `scripts/check_audio_pack.py`.
- `content/audio/ja-starter/0.1.21/` — 4,394 MP3 clips and `manifest.json`.
- `docs/AUDIO_PACK.md`, `THIRD_PARTY_NOTICES.md`, `CHANGELOG.md`.

### Changed

- `backend/app/audio_api.py`, `backend/app/audio_pack.py`,
  `backend/app/audio_learning.py`, `backend/app/review_media.py` — pack-first
  lookup, `source`/MIME response fields, English gloss request, and
  `bundled_reference` / `bundled_reviewed` provider status.
- `backend/app/scenario_practice.py` — dynamic advisory audio remains runtime-only
  and reports `source=runtime`.
- `backend/app/config.py`, `.env.example` — `audio_pack_dir` /
  `audio_pack_enabled`.
- `frontend/src/practiceSchemas.ts` — accepts `audio/mpeg`, `source`, and
  `bundled_reviewed`.
- `frontend/src/AudioPage.tsx` — Japanese/English vocabulary reference selector,
  correct Blob MIME, pack slow playback at 0.75x.
- `frontend/src/ListeningExercise.tsx`, `ExerciseSession.tsx`,
  `ReviewMedia.tsx`, `ExerciseRenderer.tsx`, `SpeakingExercise.tsx`,
  `VocabularyCollections.tsx` — prepared audio carries its source, uses
  client-side slow playback only for pack clips, and clarifies collection-recall
  audio notes for bundled references vs. optional runtime providers.
- `backend/tests/conftest.py` — autouse fixture disables the real pack; tests opt
  in through `pack_client`.
- `backend/requirements.in` / `requirements.lock` — `mutagen==1.47.0`
  (`GPL-2.0-or-later`, used solely by the offline pack build/check scripts; not
  imported by `backend/app/` runtime code).
- `.gitattributes` — marks `*.mp3 binary` for bundled MP3 clips.
- `.github/workflows/ci.yml` — runs Ruff on the audio-pack scripts,
  `python -m app.cli validate`, and `check_audio_pack.py --strict` in the
  `backend` job.
- `README.md`, `AGENTS.md`, `AI_IMPLEMENTATION_PLAN.md`, `HANDOFF.md`,
  `docs/AGENT_CONTINUATION_GUIDE.md`, `docs/CONTENT_AUTHORING.md`,
  `docs/PLAN_09_2_CURRICULUM.md`, `docs/PROJECT_STATUS_AND_REMAINING_WORK.md`,
  `docs/plans/PLAN_09_2_COMPLETION.md`,
  `docs/plans/REMAINING_WORK_EXECUTION_PLAN.md`,
  `docs/plans/PHASE_10_RELEASE.md`, `docs/plans/PHASE_11_OPEN_SOURCE_LAUNCH.md`,
  `docs/plans/WINDOWS_EXE_SETUP_PLAN.md`, `docs/plans/ANDROID_PORT_PLAN.md` —
  describe bundled authored audio versus optional runtime providers.

### Measured output

- 4,394 unique clips: 2,211 Japanese (words, cues, turns) + 2,183 English glosses.
- 87,954,616 bytes of MP3 + 2,421,277-byte manifest = **90,375,893 bytes (90.4 MB)**.
- 5,485.1 seconds (91.4 minutes) of audio; generation spanned
  2026-11-12T23:43:23Z to 2026-11-13T00:42:10Z UTC (2026-11-13 local time) on the
  CPU Kokoro container (128 kbps MP3).
- Manifest `status=draft`; `reviewed_by`/`reviewed_at` remain null.

### Verification

Final integrated verification pass (2026-11-13, after `bundled_reviewed`, script/security hardening, frontend polish, `.gitattributes`, CI, and notice/doc updates):

- `.\.venv\Scripts\python.exe scripts\check_audio_pack.py --pack content\audio\ja-starter\0.1.21 --strict`:
  `expected=4394, manifest=4394, missing=0, missing_required=0, extra=0, unreferenced=0, errors=0, warnings=0` (`ok=true`).
- Full backend suite: **235 passed** (**17** tests in
  `backend/tests/test_audio_pack.py` and **40** audio/scenario regressions
  across `test_audio_upgrades.py` [3], `test_grammar_audio.py` [12],
  `test_listening.py` [4], `test_review_media.py` [4], `test_speaking.py` [5],
  `test_scenario_practice.py` [10], and `test_quest_fallback.py` [2], or
  **35** across the 6 files excluding `test_speaking.py`).
- Backend Ruff (`backend/app`, `migrations`, `tests`, and
  `scripts/{audio_pack_common,build_audio_pack,check_audio_pack}.py`) and
  `python -m app.cli validate` passed.
- Frontend: ESLint, TypeScript `typecheck`, **50 tests** (11 files, including
  `6` in `frontend/src/audioPack.test.tsx`), and production build passed.
- Initial 2026-11-13 pack generation browser flow at 390px: Japanese and
  English playback, duration 1.32s, slow `playbackRate=0.75` and
  `preservesPitch=true`, zero Kokoro requests, external requests, JavaScript
  errors or horizontal overflow; with `TTS_ENABLED=false`, the real pack
  served a listening cue (`audio-thanks-dictation`) and a saved word review
  card (`source=pack`, `mime=audio/mpeg`). QA backend/frontend and the
  `kokoro-tts` container were stopped after the run.

### Bundled-Audio-Only Architecture (2026-11-13)

Following the initial pack release, Phases 1–3 removed all runtime TTS support:

- **Backend & Schema (`0014`):** `backend/migrations/versions/0014_remove_tts_settings.py`
  strips `tts` and `ai.voice`/`stt.voice` from `preferences.data` (and restored
  backups are normalized identically via `backend/app/services.py`). Removed
  `TTS_ENABLED`, `AUDIO_CACHE_DIR`, `POST /api/v1/scenarios/speech`,
  `GET /api/v1/audio/voices`, and all Kokoro/Edge-TTS/Piper runtime synthesis
  helpers. `GET /api/v1/health` exposes `features: {lessons, ai, stt}`;
  `GET /api/v1/providers/status` returns `{ai, stt, audio_pack}`; `POST /api/v1/audio/speech`,
  lesson/study cues, and review-card audio serve strictly from the bundled MP3
  pack (`source="pack"`, `mime="audio/mpeg"`) or return HTTP `503` (`audio_unavailable`).
- **Frontend:** Removed TTS settings/voice controls from `ProfilePage.tsx`, removed
  advisory-speech TTS playback from `ScenarioPractice.tsx`, simplified
  `AudioControls` to pack-only playback with client `0.75x` (`preservesPitch=true`),
  and updated Zod contracts in `frontend/src/schemas.ts` and `practiceSchemas.ts`.
- **Docs & Plans:** Removed `TTS_ENABLED`/`AUDIO_CACHE_DIR` from `.env.example`,
  updated `AGENTS.md`, script docstrings, root docs, and `docs/plans/*.md`.
- **Verification (Step 4 post-Phase-1–3 integrated pass, 2026-11-13):**
  - Backend Ruff (app, migrations, tests, scripts), `238 passed` (`pytest`),
    `python -m app.cli validate`, and `check_audio_pack.py --strict` (`4,394`
    clips, `0` errors/warnings).
  - Isolated clean & populated `0013 -> 0014` migrations (`alembic check`
    clean, `imported_new_version: false` on repeat import, `"tts"` and `"voice"`
    removed, learner data intact).
  - Frontend ESLint, TypeScript `typecheck`, `53 passed` (`11` Vitest files),
    and Vite production build (`2,071` modules).
  - Isolated Playwright Edge QA (`28` viewport checks at `320`/`390`/`768`/`1280`
    across 7 views, `0` overflows/console errors/external requests, `0`
    `/scenarios/speech`, `/audio/voices`, or `:8880` calls) + `TestClient`
    `AUDIO_PACK_ENABLED=false` `503` (`audio_unavailable`) verification; QA
    servers terminated and `.data/trilingo.db` untouched.

