# Trilingo — What Is Left to Do

Updated: **2026-11-13** · Schema: **`0015`** · Course source: **`ja-starter 0.1.21`** · Audio pack: **Bundled MP3s (`4,394` clips, `90.4 MB`, human review pending)**

This is the shared checklist for **you (the maintainer)** and **AI agents** picking up Trilingo in a new session. If you are an AI agent, read [AGENTS.md](AGENTS.md), [HANDOFF.md](HANDOFF.md), and the owning plan linked beside the task you are asked to run.

---

## Where Things Stand Today (Already Built & Verified)

- **Core local-first Japanese app (Phases 1–9):** React 19 + strict TypeScript frontend, FastAPI + SQLAlchemy + Alembic SQLite (`WAL`) backend, unrestricted lesson access, five checked exercise types, FSRS spaced repetition, Reading Studio (92 kana, 135 variants/combinations, 300 contextual kanji contexts), Writing Studio (composition drafts/revisions/conflicts, stroke-order canvas), deterministic dialogues/stories, custom vocabulary collections, quests, and badges.
- **Data safety (Phase 10 / W7):** Live WAL-consistent `.zip` backup export, manifest/checksum validation, pre-restore/pre-reset safety snapshots, atomic restore, and safe reset.
- **Bundled reference audio (`0014` + `0015`):** All `4,394` Japanese/English clips (`content/audio/ja-starter/0.1.21/`) play offline via browser `Audio` (`0.75x` slow with `preservesPitch=true`), with clean `503 audio_unavailable` text fallbacks when disabled or missing.
- **100% local architecture:** Zero external/cloud calls, zero runtime TTS (`0014`), and zero local AI coaching, Whisper STT, or microphone capture (`0015`). Speaking exercises and 5-direction recall use bundled MP3 model playback + unassessed typed practice/notes + self-rating.
- **Latest automated verification (schema `0015`):** Backend Ruff + `app.cli validate` + **`223` pytest tests**, clean & populated `0014 -> 0015` Alembic migration checks, `check_audio_pack.py --strict` (`4,394` clips, `0` errors), Frontend ESLint + TypeScript + **`54` Vitest tests (`11` files)** + Vite production build (`2,068` modules), and `24` headless Edge responsive layouts (`0` overflows/errors/external requests).

---

## 1. Local Release Engineering — You Can Delegate Most of This to an AI Agent

Owning plans: [Phase 10 Release Plan](docs/plans/PHASE_10_RELEASE.md) · [Remaining-Work Execution Plan (`W8`)](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md) · [Plan 9.2 (`A` / `H` / `I`)](docs/plans/PLAN_09_2_COMPLETION.md)

- [ ] **Local study reminders & quiet hours (`W8` / `Phase 10`):** Add configurable in-app reminder timing/quiet-hours settings, opt-out toggles, and honest running/closed-app availability notes (replacing the current simple toggle).
- [ ] **1,200-session query & aggregation benchmark (`H6` / `W8`):** Run and extend the large-history benchmark around [test_large_history.py](backend/tests/test_large_history.py) to measure latency/payloads across `1,200` historical sessions and confirm no N+1 regressions across map, stats, timing history, collections, and FSRS queues (plus timezone/DST checks).
- [ ] **Fresh clean-environment install test (`A2` / `Phase 10`):** Follow [README.md](README.md) from a clean temporary checkout/environment using Node 24 LTS and Python 3.11+ to verify migrations, import, launcher error handling, and clean offline run (with `.data/trilingo.db` isolated).
- [ ] **Remaining local hardening & release evidence (`R3` / `R4` / `Phase 10`):** Complete API/input/CORS/static hardening review and capture frozen release evidence under `docs/verification/local-release/<candidate>/` (`readiness.md`, `backup-contract.md`, `verification.md`, `release-notes.md`).
- [ ] **FSRS & collection edge-case sign-off (`H2` / `H5` / `G2` / `G6`):** Finish any remaining collection/FSRS deterministic regression tests and explicit `AUDIO_PACK_ENABLED=false` core lesson mid-session fallback verification.
- [ ] **15-step manual critical flow (`Phase 10`):** Execute all 15 end-to-end steps offline on the frozen candidate (`docs/plans/PHASE_10_RELEASE.md#manual-critical-flow`), with AI assistance or final human walkthrough.

---

## 2. Physical Hardware & Assistive Tech Checks — Requires Real Devices (Human / You)

Owning plan: [Plan 9.2 (`C4`, `D4`, `D5`, `W6`)](docs/plans/PLAN_09_2_COMPLETION.md)

- [ ] **Physical Windows Japanese IME (`D4`):** On a physical keyboard with Windows Japanese IME active, verify kana input, kanji candidate conversion (`Enter` commits candidate without submitting the form), composition autosave, paste/focus, and multi-tab conflict recovery.
- [ ] **Real screen reader check (`C4`):** Test reading pages and exercises with **NVDA** or **Windows Narrator** to verify `<ruby>`/`<rt>` pronunciation order, landmark/heading structure, focus restoration, and live feedback announcements.
- [ ] **Touchscreen / stylus test (`D5`):** If target hardware has touch or stylus input, test stroke-drawing canvas scaling/DPI and confirm strokes do not trigger unwanted page scrolling.

---

## 3. Qualified Japanese Language & Audio Review — Requires Qualified Reviewer

Owning plan: [Plan 9.2 (`B1`–`B6`, `C1`–`C2`, `D2`–`D3`, `E1`–`E2`, `F3`, `G1`, `G4`)](docs/plans/PLAN_09_2_COMPLETION.md) · [Audio Pack Guide](docs/AUDIO_PACK.md)

- [ ] **Bundled MP3 listening spot-check (`F3`, `G1`, `G4`):** Have a qualified speaker listen to the bundled `0.1.21` synthetic MP3 pack (`content/audio/ja-starter/0.1.21/`)—including Phase 8's five key phrases (`こんにちは。`, `日本語を勉強しています。`, `私は学校へ行きます。`, `三時にコーヒーを二杯ください。`, `きょう、きってをかいます。`), particles は/へ, counters, stories, and episodes—before updating `manifest.json` `status` from `draft` to `reviewed` (`bundled_reviewed=true`).
- [ ] **Review the `6,848` draft curriculum items (`W5` / `B1`–`B6`):** Audit the authored draft pool recorded in [inventory.json](docs/reviews/ja-starter-0.1.21/inventory.json) (covering `2,167` vocabulary entries, `300` contextual kanji, `230` draft lessons, `6` stroke assets, grammar guides, dialogues, stories, and writing tasks), resolve semantic duplicates (`B2`), apply corrections (`B4`–`B5`), and promote verified batches beyond the currently published slice (`2` units / `6` lessons / `30` checks / `8` words / `5` phrases).
- [ ] **Final Plan 9.2 reconciliation (`I1`–`I6`):** Once Sections 1–3 above are complete, run final audits and check off remaining Phase 1–9 handoff items in [PLAN_09_2_COMPLETION.md](docs/plans/PLAN_09_2_COMPLETION.md).

---

## 4. Public Open-Source Release & Launch (`Phase 11`)

Owning plan: [Phase 11 Launch Plan](docs/plans/PHASE_11_OPEN_SOURCE_LAUNCH.md) · Repo: `https://github.com/JustinReyes28/Trilingo`

*Already complete:* GitHub repo, MIT + CC BY 4.0 `LICENSE`, `.gitignore`, `.gitattributes`, `CONTRIBUTING.md`, `SECURITY.md`, `THIRD_PARTY_NOTICES.md`, GitHub Actions CI (`.github/workflows/ci.yml`), issue/PR templates, and `README.md`.

- [ ] **Synthetic release demo / screenshot & claim sheet:** Capture clean synthetic screenshot/demo matching the verified release scope under `docs/verification/public-release/<tag>/`.
- [ ] **Tag & publish official GitHub release:** Cut a version tag after Phase 10 verification and publish release notes cleanly stating what is reviewed vs. draft.
- [ ] **Social launch posts (requires explicit approval at publish time):** Finalize and post LinkedIn, Reddit, and X announcements once tagged and verified.

---

## 5. Separate Future Tracks (Optional / Post-Beginner Release)

Do **not** mix these into Phase 10 unless you intentionally start one of these tracks:

- [ ] **Windows Standalone Setup EXE (`trilingo-setup-<version>-windows-x64.exe`):** [WINDOWS_EXE_SETUP_PLAN.md](docs/plans/WINDOWS_EXE_SETUP_PLAN.md) — Next step is **`EXE-0`** (confirm packaging spike: PyInstaller `onedir` + Inno Setup, launcher mutex, capability auth, AppData separation from repo `.data/`).
- [ ] **Standalone Offline Android APK:** [ANDROID_PORT_PLAN.md](docs/plans/ANDROID_PORT_PLAN.md) — Next step is **`A0` / `A1`** (confirm device/ABI + Capacitor + Chaquopy embedded Python vs. Kotlin SQLite parity spike).
- [ ] **Intermediate & Advanced Curriculum (`Stages C–F` / `W11`):** [CURRICULUM_ROADMAP.md](docs/CURRICULUM_ROADMAP.md) — Multi-paragraph reading, guided essays, argument synthesis, and advanced register switching.

---

## Already Superseded (Do Not Build)

- **Runtime TTS / Kokoro synthesis (`0014`):** `TTS_ENABLED`, `AUDIO_CACHE_DIR`, `/api/v1/scenarios/speech`, and `/api/v1/audio/voices` are permanently removed (`build_audio_pack.py` stays maintainer-only for offline `0.1.22+` pack regeneration).
- **Optional Local AI Coaching, Whisper STT, & Microphone Capture (`0015`):** `AI_ENABLED`, `STT_ENABLED`, `Recorder.tsx`, `Explanation.tsx`, `ScenarioPractice.tsx`, `W4` AI/STT discovery, `E4`, `F4`, `F5`, and `G4` AI coaching are abandoned and permanently removed.

---

## Copyable Prompts for Starting Next Work

- **Start Phase 10 engineering hardening (`W8`):**
  > Read `AGENTS.md`, `HANDOFF.md`, `WHAT_IS_LEFT_TO_DO.md`, and `docs/plans/PHASE_10_RELEASE.md`. Implement local in-app study reminders with quiet hours, benchmark `backend/tests/test_large_history.py` at 1,200 sessions, and verify in an isolated QA DB without touching `.data/trilingo.db`.
- **Start Windows EXE packaging spike (`EXE-0`):**
  > Read `AGENTS.md`, `docs/AGENT_CONTINUATION_GUIDE.md`, and `docs/plans/WINDOWS_EXE_SETUP_PLAN.md`. Execute `EXE-0` / `EXE-1` for the local-only schema `0015` codebase and report feasibility, sizes, and exact build commands.
- **Start Android offline spike (`A0` / `A1`):**
  > Read `AGENTS.md`, `docs/AGENT_CONTINUATION_GUIDE.md`, and `docs/plans/ANDROID_PORT_PLAN.md`. Run `A0` toolchain inventory and `A1` embedded-engine feasibility check without touching desktop `.data/trilingo.db`.
