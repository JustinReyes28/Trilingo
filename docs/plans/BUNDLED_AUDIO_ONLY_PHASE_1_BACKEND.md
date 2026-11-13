# Bundled-Audio-Only Plan — Phase 1: Backend Runtime-TTS Removal & Pack-Only Audio Contract

Status: **Complete & Verified (2026-11-13; uncommitted awaiting user review)**.  
Applies the user decision (`2026-11-13`): **no more runtime TTS and no downloading TTS models/containers**, because reference audio is already pre-generated in [`content/audio/ja-starter/0.1.21/`](../../content/audio/ja-starter/0.1.21/manifest.json).

**Implementation & verification status (2026-11-13):**
- Implemented in `backend/migrations/versions/0014_remove_tts_settings.py` (head `0014`), `backend/app/{config,main,public_schemas,schemas,services,backup_service,providers,audio_pack,audio_api,audio_learning,review_media,scenario_practice,speaking}.py`, and updated `backend/tests/`.
- `TTS_ENABLED`, `AUDIO_CACHE_DIR`, `POST /api/v1/scenarios/speech`, `GET /api/v1/audio/voices`, and runtime `voices()`/`synthesize()` adapters are removed. `GET /api/v1/health` returns `features: {lessons, ai, stt}`; `GET /api/v1/providers/status` returns `{ai, stt, audio_pack}`; authored audio routes return `source="pack"`, `mime="audio/mpeg"`, or HTTP `503 audio_unavailable`.
- Step 4 post-Phase-1–3 integrated verification passed (`238 passed` in `pytest`, Ruff, `app.cli validate`, `check_audio_pack.py --strict`, isolated clean & populated `0013 -> 0014` migrations, and HTTP contract smoke; see [Phase 3 §3.4](BUNDLED_AUDIO_ONLY_PHASE_3_DOCS_PLANS.md#34-final-integrated-verification-pass-pre-commit-sign-off)).

**Sequence:** Phase 1 (this file) → [Phase 2: Frontend UI, Schemas & Test Alignment](BUNDLED_AUDIO_ONLY_PHASE_2_FRONTEND.md) → [Phase 3: Tooling Scope, Docs/Plans & Integrated Verification](BUNDLED_AUDIO_ONLY_PHASE_3_DOCS_PLANS.md).

---

## Goal & Boundaries

Remove all runtime TTS synthesis (`Kokoro` HTTP/voice-list adapters, `TTS_ENABLED`, `.data/audio-cache` runtime WAV synthesis, `Settings.tts`, and `POST /api/v1/scenarios/speech`) from the backend while preserving:

- Pre-generated authored MP3 delivery from `content/audio/<course>/<version>/` (`audio_pack.py`) with `source="pack"` and `mime="audio/mpeg"`.
- Optional local AI explanations/coaching (`AI_ENABLED`, `Settings.ai`) and optional local Japanese speech-to-text (`STT_ENABLED`, `Settings.stt`), with core study continuing normally when both are disabled.
- Backward compatibility with existing learner SQLite databases (`.data/trilingo.db`) and exported `.zip` backups (`backup_service.py`), which currently store `"tts"` inside `preferences.data` and fail `StrictModel(extra="forbid")` validation unless explicitly migrated/sanitized.
- All product/data-safety rules in [AGENTS.md](../../AGENTS.md): no learner-DB mutation in tests, single-transaction writes, idempotent `AudioDelivery` receipts, and zero study/skip/retry locks.

---

## Detailed Tasks

### 1.1 Schema Migration & Legacy Settings Compatibility
**Files:** `backend/migrations/versions/` (new migration `0014_*`), `backend/app/schemas.py`, `backend/app/services.py`, `backend/app/backup_service.py`

1. **Pydantic schemas (`backend/app/schemas.py`):**
   - Remove `tts: Provider` from `Settings` (currently line 91) and `SettingsPatch` (line 113) plus its `"tts"` entry in `SettingsPatch.no_explicit_null`.
   - Keep `ai` and `stt` on `Provider`; check whether `Provider.voice` is still used anywhere once `tts` is gone (only `providers.synthesize` / `providers.voices` read `provider.voice`). If `Provider.voice` is removed too, normalize legacy `"voice"` keys alongside `"tts"` in both the migration and restore sanitization.
2. **Alembic migration (`0014`):**
   - Add a forward Alembic migration rewriting any existing `preferences.data` JSON row to strip `"tts"` (and legacy `"voice"` inside `ai`/`stt` if removed from `Provider`) without touching XP, FSRS cards, sessions, collections, or writing drafts.
   - Verify empty (`alembic upgrade head` + `alembic check`) and populated forward-upgrade paths on isolated `.tools/` QA databases.
3. **Backup restore compatibility (`backend/app/backup_service.py`, `backend/app/services.py`):**
   - In backup import/restore (and/or a pre-validation sanitizer for `preferences` JSON), strip deprecated `"tts"` (and legacy `"voice"` if dropped) before `Settings.model_validate(...)` runs, so older W7 `.zip` backup archives restore cleanly into the updated schema.

### 1.2 Runtime Configuration, Health & Startup Logging
**Files:** `backend/app/config.py`, `backend/app/main.py`, `backend/app/public_schemas.py`

1. Remove `tts_enabled: bool` (`TTS_ENABLED`) and `audio_cache_dir: Path` (`AUDIO_CACHE_DIR`) from `Config` in `backend/app/config.py` (keep `audio_pack_dir` and `audio_pack_enabled`).
2. Update `lifespan` startup logging in `backend/app/main.py` from `AI=%s TTS=%s STT=%s` to `AI=%s STT=%s`.
3. Update `HealthFeatures` (`backend/app/public_schemas.py`) and `/api/v1/health` (`backend/app/main.py`) to remove `tts: False` (keep `lessons`, `ai`, `stt`).
4. In `backup_service.py`, verify any existing `"audio_cache"` exclusion reference remains harmless if `.data/audio-cache/` still exists on disk from prior runs.

### 1.3 Strip Runtime TTS Adapter Logic
**Files:** `backend/app/providers.py`

1. Remove `voices()` and `synthesize()` (including Kokoro `/audio/voices`, `/audio/speech`, WAV synthesis caching under `.data/audio-cache`, and `jf_`/`jm_` voice checks).
2. Keep `endpoint()`, `provider_json()`, `validate_wav()`, `transcribe()`, `explain_text()`, `provider_failure()`, `require_enabled()` (for `"ai"` and `"stt"` only), and `PROVIDER_ERRORS` intact for optional local AI and STT.

### 1.4 Pack-Only Audio Endpoints & Scenario Coaching Simplification
**Files:** `backend/app/audio_pack.py`, `backend/app/audio_api.py`, `backend/app/audio_learning.py`, `backend/app/review_media.py`, `backend/app/scenario_practice.py`

1. **Authored reference speech (`audio_api.py` `POST /api/v1/audio/speech`):**
   - Remove the runtime fallback (`get_settings(db).tts`, `providers.require_enabled(..., "tts")`, `providers.synthesize`).
   - When `audio_pack.lookup(...)` returns `None`, raise `DomainError(503, "audio_unavailable", "Bundled reference audio is unavailable for this item. Use the text alternative.")`.
   - Update `AudioOut` contract cleanly for bundled-only playback (`mime: Literal["audio/mpeg"]`, `source: Literal["pack"]`).
2. **Listening / speaking cue delivery (`audio_learning.py` `prepare`):**
   - Look up from `audio_pack`; if `clip is None`, raise `DomainError(503, "audio_unavailable", "Bundled reference audio is unavailable for this cue. Use the text alternative.")` *before* writing an `AudioDelivery` row, so missing audio never fabricates `speech_reference_delivered=True` and preserves typed/text fallback and continuation.
3. **Saved review card media (`review_media.py` `prepare`):**
   - Look up from `audio_pack`; on miss, raise `DomainError(503, "audio_unavailable", "Bundled saved-card audio is unavailable. Reveal text or self-rate directly.")`.
4. **Scenario practice (`audio_api.py`, `scenario_practice.py`):**
   - Remove `POST /api/v1/scenarios/speech`, `ScenarioVoiceRequest`, and `scenario_practice.voice_reply()`. Dynamic AI coaching replies (`POST /api/v1/scenarios/practice`) remain text-only, and optional voice input (`POST /api/v1/scenarios/transcriptions`) stays available via optional `STT_ENABLED`.
5. **Provider & pack status endpoint (`GET /api/v1/providers/status` in `audio_api.py`):**
   - Remove the `"tts"` entry from `ProviderStatus` (keeping `"ai"` and `"stt"` as `ProviderCapability`) and expose bundled pack status under an explicit top-level `audio_pack` status object (`bundled_reference: bool`, `bundled_reviewed: bool`, `course_version: str | None`, `message: str`) so the API no longer advertises a runtime TTS capability or Kokoro configuration.
6. **`audio_pack.py` runtime docstrings/comments:**
   - Update module docstrings that mention falling back to runtime TTS to state that misses fall back cleanly to UI text/transcript alternatives.

### 1.5 Backend Test Updates & Regression Coverage
**Files:** `backend/tests/conftest.py`, `test_audio_pack.py`, `test_foundation.py`, `test_grammar_audio.py`, `test_listening.py`, `test_quest_fallback.py`, `test_review_media.py`, `test_scenario_practice.py`, `test_speaking.py`, `test_backup_restore.py`, plus new migration forward-upgrade test coverage.

- Remove obsolete runtime-TTS / Kokoro / `/scenarios/speech` mock-synthesis tests and replace them with:
  - Pack-hit tests confirming MP3 delivery across words, glosses, cues, story turns, and saved review cards with zero external providers.
  - Clean `audio_unavailable` (`503`) fallback tests when `AUDIO_PACK_ENABLED=false` or a clip is missing/corrupt, verifying `AudioDelivery` is not recorded on failure and skip/text/typing/XP progression stays unblocked.
  - `/api/v1/providers/status` contract test covering `ai`, `stt`, and `audio_pack` (`bundled_reference` / `bundled_reviewed`) with no `tts` block.
  - `POST /api/v1/scenarios/speech` absence check (`404`/`405`), while confirming `/scenarios/practice` and `/scenarios/transcriptions` still function normally.
  - Migration `0014` populated-upgrade test and W7 backup-restore test proving legacy `preferences.data` containing `"tts"` migrates/restores without error.

---

## Verification Gate (Phase 1 Exit Criteria)

From `backend/` (using isolated `.tools/` pytest temp/cache dirs and a disposable `.tools/` SQLite DB with `QA_MODE=true`; never touching `.data/trilingo.db`):

1. `..\.venv\Scripts\python.exe -m ruff check --config pyproject.toml app migrations tests` → exit `0`.
2. `..\.venv\Scripts\python.exe -m alembic upgrade head` and `alembic check` on both an empty `.tools/` DB and a copy of a pre-0014 populated DB containing `"tts"` preferences → exit `0`, zero schema drift.
3. `..\.venv\Scripts\python.exe -m pytest -q --basetemp=../.tools/pytest-tts-removal-p1 -o cache_dir=../.tools/pytest-cache-tts-removal-p1` → all backend tests pass.
4. `..\.venv\Scripts\python.exe -m app.cli validate` → exit `0`.

**Next:** Proceed to [Phase 2: Frontend UI, Schemas & Test Alignment](BUNDLED_AUDIO_ONLY_PHASE_2_FRONTEND.md).
