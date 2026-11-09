# Trilingo: Project Status and Remaining Work

This document provides a complete, accurate breakdown of what is built, tested, and verified in Trilingo today, along with everything that remains to be completed according to the master implementation plan (excluding the standalone Windows EXE installer and Android mobile port tracks).

---

## 1. Executive Summary

Trilingo is currently a fully functional, playable, local-first Japanese study application running on React 19, FastAPI, and SQLite with Write-Ahead Logging (WAL). All core learning modes, the FSRS spaced repetition engine, the writing studio, reading practice with ruby text, data safety backup/restore, and open-source GitHub packaging are completely implemented and verified.

The remaining open work falls into four distinct categories:
1. **Local release hardening (Phase 10 / W8):** In-app study reminders with quiet hours, query performance benchmarks on 1,200-session histories, and the 15-step manual critical flow.
2. **Human pedagogical review (Plan 9.2 / W5):** Language review of the 6,848 authored draft items by a qualified Japanese speaker before full formal publication.
3. **Physical device & accessibility verification (Plan 9.2 / W6):** Physical Windows IME conversion checks, screen reader ruby pronunciation order, and touchscreen stylus testing.
4. **Optional local audio services (Plan 9.2 / F & G):** Downloading and configuring local Kokoro TTS and Whisper STT models for offline voice generation and speech recognition.
5. **Future curriculum extensions (Stages C through F):** Intermediate to advanced multi-paragraph reading and essay composition.

---

## 2. What Is 100% Complete and Verified Today

### Full-Stack Architecture & Engine (Phases 1 through 9)
- **Frontend Stack:** React 19, strict TypeScript, Vite, Tailwind CSS, and Zod runtime schema validation. Responsive across mobile (320px-390px), tablet, and desktop viewports.
- **Backend Stack:** Python 3.11+, FastAPI, SQLAlchemy 2.0, Pydantic v2, and Alembic (all 13 migrations applied through head `0013`).
- **Storage:** SQLite with Write-Ahead Logging (`PRAGMA journal_mode=WAL`) and foreign keys enabled for atomic transactions and concurrent reads.
- **Unrestricted Study:** Zero hearts/lives, zero cooldowns, no energy meters, no forced waiting periods, free lesson replays, and uncapped genuine-session XP.
- **Interactive Exercise Engine:** Five distinct exercise types (translation, fill-in-the-blank, multiple choice, sentence ordering, and vocabulary matching) with authoritative backend grading, accepted alternative answers, and explanations.
- **FSRS Spaced Repetition:** Native implementation of the Free Spaced Repetition Scheduler (`Again`, `Hard`, `Good`, `Easy`), deterministic interval calculations, review logs, and custom vocabulary collection drilling.
- **Reading Studio:** 92 basic kana, 135 variants/combinations, and 300 contextual kanji entries with toggleable furigana (ruby text) and romaji aids.
- **Writing Studio:** Native Japanese IME composition, draft autosave with multi-tab conflict preservation, unassessed free writing submissions, and a vector stroke-order canvas.
- **Dialogues & Passages:** Everyday dialogue scenarios with register contrasts (polite vs. plain form), practical reading passages (menus, train schedules, messages), and interactive stories with glossaries.
- **100% Offline Core:** All lessons, grading, FSRS scheduling, and progress persistence work with zero cloud accounts and zero external internet dependencies.

### Local Data Safety & Backup/Restore (Phase 10 / W7)
- **WAL-Consistent Backup:** Uses SQLite's native online backup API (`sqlite3.Connection.backup()`) to produce clean, byte-consistent snapshots including active WAL pages.
- **Archive Export:** Generates zip archives bundling the database and a validated `manifest.json` with app identity (`Trilingo`), schema version (`0013`), SHA-256 database checksum, and an itemized entity summary.
- **Security & Integrity Guards:** Rejects archives exceeding 50 MB compressed or 150 MB uncompressed (zip-bomb guard), blocks path traversal attempts, verifies SHA-256 checksums, and executes SQLite `PRAGMA integrity_check`.
- **Atomic Point-in-Time Restore:** Automatically saves a pre-restore safety backup to `.data/backups/`, disposes active connection pools, unlinks `-wal` and `-shm` journals, and atomically swaps the database file.
- **Safe Reset:** Clears all 20 learner data tables in strict foreign-key order while preserving installed course content, accompanied by an automatic pre-reset safety backup.
- **Profile UI:** Accessible UI card in `ProfilePage.tsx` with one-click export, file picker preview card, confirmation actions, and safety backup history.

### Open-Source Packaging & GitHub Setup (Phase 11)
- **Public Repository:** Live at [https://github.com/JustinReyes28/Trilingo](https://github.com/JustinReyes28/Trilingo) on branch `main`.
- **Dual Licensing:** MIT License for source code (Copyright 2026 Justin Reyes) and Creative Commons Attribution 4.0 International (CC BY 4.0) for course text and curriculum data.
- **Repository Hygiene:** Strictly audited `.gitignore` preventing SQLite files, WAL journals, backup archives, local `.env` secrets, or build caches from being committed.
- **Line Ending Normalization:** Enforced exact LF normalization via `.gitattributes` to preserve SHA-256 content hashes across Windows and Linux.
- **Community Standards:** Added `SECURITY.md`, `CONTRIBUTING.md`, issue templates (bug report, content correction, feature request), and pull request template.
- **Continuous Integration:** Automated GitHub Actions workflow (`.github/workflows/ci.yml`) running on Windows runners covering frontend lint/typecheck/vitest/build and backend ruff/alembic/pytest.

---

## 3. Remaining Work (Excluding Android and Windows EXE Tracks)

```
+-----------------------------------------------------------------------------------+
|                            TRILINGO REMAINING WORK                                |
+------------------------------------+----------------------------------------------+
| Track                              | Status & Required Action                     |
+------------------------------------+----------------------------------------------+
| 1. Phase 10 Local Hardening (W8)   | Engineering: Reminders, benchmarks, QA flow   |
| 2. Human Pedagogical Review (W5)   | External: Native Japanese speaker sign-off   |
| 3. Physical Device & Accessibility | QA / Hardware: Real IME, screen reader tests |
| 4. Optional Local Kokoro & Whisper | Infrastructure: Download ~1.6 GB models      |
| 5. Later Curriculum (Stages C-F)   | Future scope: Intermediate to advanced       |
+------------------------------------+----------------------------------------------+
```

### Track 1: Phase 10 Local Hardening ([Phase 10 / W8](plans/PHASE_10_RELEASE.md#L148-L158))
- **Local In-App Study Reminders:**
  - *Current state:* Only an in-page reminder preference toggle exists in Profile settings.
  - *Required work:* Implement configurable in-app or browser notification reminders with configurable quiet hours, opt-out toggles, and truthful running/closed-app availability notes.
- **Large-History Query Benchmarks:**
  - *Current state:* Large history fixtures exist in `backend/tests/test_large_history.py`.
  - *Required work:* Formally benchmark query latency and response payloads against 1,200 simulated historical sessions to guarantee the course map and stats pages remain fast without N+1 query bottlenecks.
- **15-Step Manual Critical Flow:**
  - *Current state:* Automated test coverage is green (218 backend tests, 44 frontend tests).
  - *Required work:* Execute the documented 15-step end-to-end manual acceptance flow on a frozen release candidate with external network disconnected:
    1. Profile setup (timezone, aids, daily goal).
    2. Direct access to a later lesson without prerequisite gating.
    3. Mistake handling, hints, reveals, and skips without penalty.
    4. Session finish and honest evidence attribution.
    5. Duplicate request idempotency verification.
    6. Contextual kana and kanji reading with aids on and off.
    7. Native IME typing and composition drafting.
    8. Dialogue completion and recording playback.
    9. Core lesson completion with all providers disabled.
    10. Mistake review and FSRS four-button rating persistence.
    11. Optional recap/mastery without access gating.
    12. Same-day session replays earning standard XP without daily caps.
    13. Goal and reminder hiding without XP loss.
    14. Guided composition submission and revision conflict preservation.
    15. Backup export, restore round trip, and cancelled reset verification.

---

### Track 2: Qualified Japanese Pedagogical Review ([Plan 9.2 / W5](plans/REMAINING_WORK_EXECUTION_PLAN.md#L110-L123))
- **The Core Distinction:**
  - *Published Technical Slice:* 2 units, 6 lessons, 30 checks, 8 words, and 5 expressions.
  - *Authored Draft Inventory:* 2,167 vocabulary entries, 300 contextual kanji, and 230 draft lessons across ten topics.
- **Pending Review Items:**
  - There are **6,848 pending draft items** documented in `docs/reviews/ja-starter-0.1.21/inventory.json`.
  - These items were programmatically generated and mechanically validated for schema consistency, but they have not yet been evaluated by a qualified Japanese speaker or teacher.
  - *Required work:* Review vocabulary definitions, pitch/reading nuances, contextual kanji usages, particle contrast explanations, and cultural register appropriateness (polite `-desu`/`-masu` vs. plain form) before formally promoting draft lessons to published status.

---

### Track 3: Physical Hardware & Accessibility Verification ([Plan 9.2 / W6](plans/REMAINING_WORK_EXECUTION_PLAN.md#L124-L135))
- **Physical Windows Japanese IME:**
  - Verify on a physical keyboard that pressing `Enter` during candidate conversion commits the selected kanji characters to the input field without accidentally triggering form submission.
- **Screen Reader Compatibility:**
  - Test with NVDA or Windows Narrator to verify that `<ruby>` and `<rt>` HTML annotations are announced in the correct reading order (kanji first, reading second) rather than scrambling words.
- **Touch & Stylus Input:**
  - Test character stroke-drawing on a physical touchscreen or stylus tablet, confirming touch events scale cleanly and do not conflict with browser scroll gestures.

---

### Track 4: Optional Local Audio & Speech Setup ([Plan 9.2 / F & G](plans/REMAINING_WORK_EXECUTION_PLAN.md#L101-L108))
- **Current State:**
  - Trilingo provides built-in adapter architecture for local Kokoro TTS and Whisper STT.
  - When disabled, the app falls back to visual text and transcript feedback without losing practice credit.
  - No models or containers are currently downloaded or running on this machine.
- **To Enable Local Audio:**
  - Would require user approval to download approximately **1.6 GB** of dependencies:
    - Kokoro-FastAPI container or Python package with Japanese voice weights (`jf_alpha`, `jm_kumo`).
    - Faster-Whisper or OpenAI-compatible local Whisper STT model weights.
  - Audio runs strictly against `127.0.0.1` loopback endpoints with a 10-second safety timeout.

---

### Track 5: Future Curriculum Releases (Stages C through F)
- The current implementation covers **Beginner Stages A & B** (CEFR A1 / JLPT N5 equivalent).
- Future planned releases (outlined in [`docs/CURRICULUM_ROADMAP.md`](CURRICULUM_ROADMAP.md)):
  - **Stages C & D (Intermediate):** Multi-paragraph reading passages, complex sentence grammar, guided paragraph essays, and practical workplace interactions.
  - **Stages E & F (Advanced):** Formal essays, competing arguments, source synthesis, and advanced register switching.

---

## 4. Recommended Next Steps

If you want to continue engineering progress without needing external human reviewers or large model downloads, the most logical next tasks are:

1. **Implement Track 1.1:** Add in-app study reminders with configurable quiet hours and local delivery controls in `frontend/src/` and backend preferences.
2. **Implement Track 1.2:** Run the 1,200-session performance benchmark script to confirm database query scaling.
3. **Execute Track 1.3:** Conduct the 15-step manual critical flow test to certify the local release candidate.
