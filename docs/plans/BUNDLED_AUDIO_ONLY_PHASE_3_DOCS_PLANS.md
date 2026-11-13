# Bundled-Audio-Only Plan — Phase 3: Tooling Scope, Docs/Plans & Integrated Verification

Status: **Complete & Verified (2026-11-13; Phases 1–3 and §3.4 integrated verification passed; uncommitted awaiting explicit user commit approval)**.  
Applies the user decision (`2026-11-13`): align repository tooling notes, setup docs, project plans, and checklists around **bundled-only reference audio with zero runtime TTS and zero TTS model downloads**, then run final integrated validation.

**Sequence:** [Phase 1](BUNDLED_AUDIO_ONLY_PHASE_1_BACKEND.md) → [Phase 2](BUNDLED_AUDIO_ONLY_PHASE_2_FRONTEND.md) → Phase 3 (this file).

---

## Goal & Boundaries

- Keep the already-generated pack under [`content/audio/ja-starter/0.1.21/`](../../content/audio/ja-starter/0.1.21/manifest.json) as the sole source of authored Japanese/English audio, with zero runtime TTS services, model downloads, or Kokoro packaging instructions in user/developer/release workflows.
- Preserve optional local **STT** (microphone transcription feedback) and optional local **AI** (ephemeral coaching/explanations) where documented, while keeping all core learning offline with zero external providers.
- Preserve historical run logs verbatim as dated records (`docs/PLAN_09_2_CURRICULUM.md`, historical audit notes) instead of rewriting past evidence; update active guidance, open checklists, and setup instructions only.

---

## Detailed Tasks

### 3.1 Scripts, Notices & Environment Config Cleanup
**Files:** `.env.example`, `THIRD_PARTY_NOTICES.md`, `scripts/build_audio_pack.py`, `scripts/check_audio_pack.py`, `backend/requirements.in` / `requirements.lock` (unchanged; `mutagen` retained strictly for offline/CI pack scripts), `.github/workflows/ci.yml` (unchanged)

- [x] **`.env.example`:** Removed `TTS_ENABLED` and `AUDIO_CACHE_DIR`; kept `AI_ENABLED`, `STT_ENABLED`, `AUDIO_PACK_DIR`, and `AUDIO_PACK_ENABLED`.
- [x] **`scripts/` tooling stance:**
  - `scripts/check_audio_pack.py` and `scripts/audio_pack_common.py` stay active in CI and validation so bundled MP3 integrity/coverage stays enforced.
  - `scripts/build_audio_pack.py` docstring and [docs/AUDIO_PACK.md](../AUDIO_PACK.md) explicitly document that `0.1.21` is committed and `build_audio_pack.py` stays solely as an optional maintainer tool for regenerating future `0.1.22+` packs (end-users, learners, testers, and CI never run Kokoro or download TTS models).
- [x] **`THIRD_PARTY_NOTICES.md`:** Retained CC BY 4.0 / Kokoro-82M / Kokoro-FastAPI build-time attribution for the committed MP3 clips and script-only note for `mutagen`, clarifying zero runtime TTS adapters or runtime dependencies exist.

### 3.2 Root, Architecture & Authoring Documentation Sync
**Files:** `README.md`, `AGENTS.md`, `HANDOFF.md`, `AI_IMPLEMENTATION_PLAN.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `docs/AGENT_CONTINUATION_GUIDE.md`, `docs/AUDIO_PACK.md`, `docs/TECHNICAL_DECISIONS.md`, `docs/PROJECT_STATUS_AND_REMAINING_WORK.md`, `docs/CONTENT_AUTHORING.md`, `docs/CURRICULUM_ROADMAP.md`, `docs/DESIGN_BRIEF.md`

- [x] **`AGENTS.md`:** Updated `Providers and failures` so authored audio is bundled-only (`content/audio/<course>/<version>/`), text/transcript alternatives + `503 audio_unavailable` cover unavailable audio, and zero runtime TTS or model downloads exist (preserving `inherit` / **Gemini 4 Hydrogen**).
- [x] **`README.md`, `CONTRIBUTING.md` & `.env.example`:** Removed runtime Kokoro/TTS setup steps and environment flags from quick-start and optional-provider instructions (kept optional AI and optional STT sections).
- [x] **`docs/AUDIO_PACK.md`, `docs/TECHNICAL_DECISIONS.md`, `docs/CONTENT_AUTHORING.md`, `docs/CURRICULUM_ROADMAP.md`, `docs/DESIGN_BRIEF.md`, `docs/PROJECT_STATUS_AND_REMAINING_WORK.md`, `AI_IMPLEMENTATION_PLAN.md`, `HANDOFF.md`, `CHANGELOG.md`, `docs/AGENT_CONTINUATION_GUIDE.md`:** Removed active "runtime TTS / Kokoro fallback" wording, documented `503 audio_unavailable` + text fallback, text-only AI scenario replies, `/api/v1/health` (`{lessons, ai, stt}`), `/api/v1/providers/status` (`{ai, stt, audio_pack}`), and schema `0014` preference cleanup while preserving historical logs/metrics verbatim.

### 3.3 Phase Checklists & Remaining-Work / Platform Plans Update
**Files:** `docs/plans/PHASE_01_FOUNDATION.md`, `docs/plans/PHASE_08_AUDIO_SPEAKING.md`, `docs/plans/PHASE_10_RELEASE.md`, `docs/plans/PHASE_11_OPEN_SOURCE_LAUNCH.md`, `docs/plans/PLAN_09_2_COMPLETION.md`, `docs/plans/REMAINING_WORK_EXECUTION_PLAN.md`, `docs/plans/WINDOWS_EXE_SETUP_PLAN.md`, `docs/plans/ANDROID_PORT_PLAN.md`

- [x] **`PHASE_01_FOUNDATION.md`, `PHASE_08_AUDIO_SPEAKING.md`, `PLAN_09_2_COMPLETION.md`, `REMAINING_WORK_EXECUTION_PLAN.md`:** Marked runtime Kokoro setup, discovery, and dynamic TTS items (`F1`, `F2`, `G4` voice) superseded (`2026-11-13 bundled-audio-only`) while keeping `F3` human listening review of `0.1.21` (`bundled_reviewed` remains `false`), `F4`/`F5` optional STT, `E4` optional local AI coaching, `G1` story/episode review, and physical IME/accessibility checks explicitly open.
- [x] **`PHASE_10_RELEASE.md`, `PHASE_11_OPEN_SOURCE_LAUNCH.md`, `WINDOWS_EXE_SETUP_PLAN.md`, `ANDROID_PORT_PLAN.md`:** Removed instructions to bundle/download/troubleshoot runtime TTS/Kokoro/weights or runtime audio caches, kept `90.4 MB` `content/audio/` MP3 pack bundling and `0.75x` playback, and excluded script-only `mutagen` (`GPL-2.0-or-later`) from runtime bundles.

### 3.4 Final Integrated Verification Pass (Pre-Commit Sign-Off)
Run all gates sequentially in Step 4 after doc/plan completion (never touching `.data/trilingo.db` or `content/audio/` clips):

- [x] **Migration & DB compatibility checks (isolated `.tools/` DB with `QA_MODE=true`):**
  - Clean DB (`.tools/bundled-only-qa-20261113/clean.db`): `alembic upgrade head` (`0014`), `alembic check` (`No new upgrade operations detected.`), repeat `python -m app.cli import` (`imported_new_version: true` then `false`).
  - Populated DB (`.tools/bundled-only-qa-20261113/populated.db`): upgraded pre-`0014` (`0013`) DB containing legacy `"tts"` and `"ai.voice"`/`"stt.voice"` to `0014`; verified `"tts"`/`"voice"` keys stripped, learner counts and XP (`15`) preserved, and `GET /api/v1/settings` + `GET /api/v1/progress` returned HTTP `200`.
- [x] **Backend gates (`backend/`):**
  - `..\.venv\Scripts\python.exe -m ruff check --config pyproject.toml app migrations tests ..\scripts\audio_pack_common.py ..\scripts\build_audio_pack.py ..\scripts\check_audio_pack.py` (`All checks passed!`)
  - `..\.venv\Scripts\python.exe -m pytest -q --basetemp=../.tools/bundled-only-qa-20261113/pytest-tmp -o cache_dir=../.tools/pytest-cache-bundled-only` (`238 passed, 1 warning in 659.63s`)
  - `..\.venv\Scripts\python.exe -m app.cli validate` (`ja-starter 0.1.21`, `6` published lessons, `30` checks)
  - `..\.venv\Scripts\python.exe ..\scripts\check_audio_pack.py --pack ..\content\audio\ja-starter\0.1.21 --strict` (`4,394` expected/manifest, `0` errors/warnings)
- [x] **Frontend gates (`frontend/`):**
  - `npm run lint`, `npm run typecheck`, `npm test -- --run` (`53 passed`, `11` files), and `npm run build` (`2,071` modules).
- [x] **End-to-end QA smoke flow:**
  - Isolated QA backend (`127.0.0.1:8029`) + Vite (`127.0.0.1:5199`, `AI_ENABLED=false`, `STT_ENABLED=false`, `AUDIO_PACK_ENABLED=true`, plus `AUDIO_PACK_ENABLED=false` `503 audio_unavailable` `TestClient` check): exercised Profile (AI/STT only + `Tab` focus), Audio (`ja`+`en` MP3 `0.75x` with `preservesPitch=true`), Listening, Speaking, Story, Collections, text-only Scenario Coaching, and Backup export/restore (after waiting for background requests to settle before restore due to pre-existing Windows SQLite `WinError 5` locking in `backend/app/backup_service.py:486`); confirmed `0` overflows across `28` viewport layouts (`320`/`390`/`768`/`1280`), `0` JS/page errors, `0` external requests, and `0` calls to `/scenarios/speech`, `/audio/voices`, or `:8880` across `169` requests; stopped QA services and left `.data/trilingo.db` untouched.
- [x] **Post-verification doc record update:**
  - Recorded Step 4 verified counts and sign-off in `CHANGELOG.md`, `HANDOFF.md`, `docs/AUDIO_PACK.md`, `docs/AGENT_CONTINUATION_GUIDE.md`, `.design-skill/audit-report.md`, and `docs/plans/BUNDLED_AUDIO_ONLY_PHASE_{1,2,3}_*.md`; all changes remain uncommitted awaiting user review.
