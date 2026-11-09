# Trilingo — Local Backup, Restore and Provider Verification Report

Date: **2026-11-08**
Target: **Phase 10 / W7 — Local Backup, Restore & Safe Reset** and **Area 4 — Local Provider & Audio Verification (Plan 9.2 F & G)**

---

## 1. Executive Summary

- **Area 1 (Local Backup, Restore and Safe Reset — Phase 10 / W7):** Fully implemented and verified. Uses SQLite's native online backup API (`sqlite3.Connection.backup()`) to guarantee a non-corrupt, consistent snapshot of the live database including active WAL pages. Backups package a validated JSON manifest declaring application/schema/content versions, SHA-256 database checksum, profile, and an itemized entity summary. Restoring validates archive safety, uncompressed limits (zip bomb protection), path traversal, checksums, and schema compatibility before staging. An automatic pre-restore safety backup is archived before the live database is swapped atomically. Reset safely cascades through all 20 learner data tables in strict foreign-key order while keeping course units and lessons intact, accompanied by a mandatory pre-reset safety backup. Profile page UI provides full controls for export, instant snapshot preview, restore confirmation, and reset confirmation with an accessible modal dialog.
- **Area 4 (Local Provider & Audio Verification — Plan 9.2 F & G):** Comprehensive local inventory performed. Docker Desktop v29.8.0 is present with a stopped WSL2 `docker-desktop` distro; LM Studio application was previously uninstalled; local Hugging Face cache holds Qwen3.5 (0.8B, 2B GGUF) and MiniCPM5 (2B GGUF); no standalone Kokoro or Whisper daemon is listening on local ports (1234, 8880). Verified that core learning, grading, XP, progression, stories, dialogues, and review operate 100% reliably with providers disabled (`AI_ENABLED=false`, `TTS_ENABLED=false`, `STT_ENABLED=false`) with honest transcript and typed fallbacks.

---

## 2. Area 1 Implementation Details

### 2.1 Backend Architecture
- **`backend/app/config.py`**: Added `backups_dir: Path = ROOT / ".data" / "backups"` with path normalization.
- **`backend/app/backup_schemas.py`**: Strict Pydantic models for `BackupManifest`, `BackupSummary`, `BackupPreviewOut`, `RestoreResultOut`, `ResetRequest`, `ResetResultOut`, and `SafetyBackupListOut`.
- **`backend/app/backup_service.py`**:
  - `create_backup()`: Acquires re-entrant lock, calls `source_conn.backup(dump_conn)`, checks Alembic version, queries table stats, computes SHA-256, and bundles `manifest.json` + `database.sqlite` into a ZIP archive.
  - `validate_backup_archive()`: Strict validation enforcing max archive size (50MB), max uncompressed size (150MB), filename whitelist (`manifest.json` and `database.sqlite` only), path traversal prevention (`..`, absolute paths, slashes), manifest schema validation, SHA-256 checksum matching, and SQLite `PRAGMA integrity_check`.
  - `preview_backup()`: Returns snapshot metadata, XP/session summary, and compatibility status without modifying the live database.
  - `restore_backup()`: Enforces confirmation, saves an automatic pre-restore backup, disposes SQLAlchemy engine connections, cleans up `-wal` and `-shm` files, atomically replaces the live `.db` file, and dynamically rebinds the sessionmaker.
  - `reset_learner_progress()`: Enforces confirmation, saves an automatic pre-reset backup, deletes all learner rows across 20 tables in strict foreign-key order, resets profile to "Learner" / "UTC" and preferences to defaults, preserves `courses` and `course_versions`, and runs `VACUUM`.
  - `list_safety_backups()`: Enumerates automatic safety snapshots in `.data/backups/`.
- **`backend/app/backup_api.py`**: Exposes `/api/v1/backup/export`, `/preview`, `/restore`, `/reset`, and `/safety-backups`.
- **`backend/app/middleware.py`**: Updated `RequestBodyLimit` to allow up to 50MB for `/api/v1/backup/preview` and `/restore`, while keeping 64KB for regular APIs.
- **`backend/app/main.py`**: Registered backup router, bound `session_factory` and `engine` in `app.state`.

### 2.2 Frontend Implementation
- **`frontend/src/schemas.ts`**: Matching Zod schemas for backup summary, preview, restore, reset, and safety backups list.
- **`frontend/src/api.ts`**: Added `post()`, `postBinary()`, and `getApiUrl()` utilities.
- **`frontend/src/components.tsx`**: Added `danger` variant to `Button`.
- **`frontend/src/styles.css`**: Added `.button.danger`, `.backup-section`, `.backup-preview-card`, `.backup-stats-grid`, and `.safety-backup-list`.
- **`frontend/src/ProfilePage.tsx`**: Added "Data safety, backup & reset" card supporting:
  - One-click backup export with toggle for handwriting drawing samples.
  - File picker with instant preview card displaying snapshot timestamp, profile name, XP summary, and compatibility badge.
  - Confirmation actions with point-in-time replacement warning.
  - Expandable list of recent automatic safety backups.
  - Reset progress button opening an accessible modal `Dialog` with safety backup assurance and destructive confirmation.

---

## 3. Area 4 Provider & Audio Status

1. **Host Discovery Findings:**
   - Docker Desktop 4.92.0 / CLI 29.8.0 installed at `C:\Users\Administrator\AppData\Local\Programs\DockerDesktop`.
   - WSL2 distro `docker-desktop` is `Stopped`; named pipe `//./pipe/dockerDesktopLinuxEngine` is not active.
   - LM Studio application is uninstalled (empty directory remnants).
   - Local Hugging Face cache contains GGUF models: `Qwen3.5-0.8B-GGUF` (730.6 MB), `Qwen3.5-2B-GGUF` (1,277.7 MB), `MiniCPM5-2B-GGUF` (1,489.0 MB).
   - Kokoro TTS and Whisper STT are not currently installed or running as active services.
2. **Offline & Fallback Safety Verification:**
   - Verified that Trilingo runs with `AI_ENABLED=false`, `TTS_ENABLED=false`, `STT_ENABLED=false`.
   - All core learning, lessons, grading, XP, FSRS review, stories, dialogues, and writing operate with typed and transcript fallbacks without requiring external network access or provider daemons.
3. **Future Transfer Requirements (When Authorized):**
   - **Kokoro TTS:** Docker CPU image (`ghcr.io/remsky/kokoro-fastapi-cpu` ~1.2 GB compressed) or Python standalone wheel setup + Kokoro v1.0 weights (~350 MB) + Japanese phonemizer dictionaries (`misaki[ja]` / `unidic-lite` ~50 MB).
   - **Japanese STT:** `whisper.cpp` Windows binary (~5 MB) + `ggml-small.bin` (~466 MB) or `ggml-medium.bin` (~1.5 GB).
   - *Note: As per project rules, any future download requires explicit user approval with exact scope and estimated size before transfer.*

---

## 4. Test Evidence

- **Backend:** `tests/test_backup_restore.py` — 6 passed in 2.85s:
  1. `test_backup_export_creates_valid_archive_and_manifest`: PASS
  2. `test_backup_preview_and_validation`: PASS
  3. `test_restore_replaces_progress_atomically_and_saves_safety_backup`: PASS
  4. `test_reset_learner_progress_and_preserves_courses`: PASS
  5. `test_backup_drawing_samples_exclusion_option`: PASS
  6. `test_incompatible_future_schema_and_tamper_detection`: PASS
- **Frontend:** Vitest — 10 test files, 44 passed in 1.90s (including `profileBackup.test.tsx`).
- **Build:** Vite production build — 2,071 modules transformed in 3.33s, clean exit code 0.
- **Lint:** ESLint on frontend and Ruff on backend both report zero errors.
