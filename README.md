# Trilingo: Personal Japanese Learning

Trilingo is a local-first Japanese study app built for learners who want direct, self-directed practice without artificial friction. There are no hearts, energy meters, forced waiting periods, or daily XP quotas. Everything you study stays on your own computer in an SQLite database.

Core lessons, kanji practice, spaced repetition, and writing drafting work completely offline with zero cloud accounts and zero external AI dependencies.

---

## Why Trilingo?

Most language learning apps rely on predatory mobile gamification: losing "lives" when you make a mistake, waiting hours for energy to recharge, or getting locked out of lessons until you pay for a premium subscription.

Trilingo takes the opposite approach:

- **Unrestricted study:** Every published lesson, kanji chart, and review mode is unlocked from the start. Follow the suggested roadmap or jump directly to the topics you care about.
- **Honest spaced repetition:** Spaced repetition runs on the modern Free Spaced Repetition Scheduler (FSRS) algorithm in the backend. Early reviews are always available, and voluntary extra practice never distorts your learning history.
- **Honest evidence over fake streaks:** Assisted answers, hints, and skipped questions never get logged as unassisted mastery. Mistakes do not cost lives; they just stay in your review queue until you have practiced them.
- **True local privacy:** Your study history, writing drafts, and review schedules live locally in `.data/trilingo.db`. No trackers, no telemetry, and no third-party analytics.
- **Real input tools:** Type directly using your native Japanese IME, practice stroke order with guided templates, and compose writing drafts with autosave and conflict recovery.

---

## What's in the Box

### 1. Course Curriculum (`ja-starter`)
- **Vocabulary:** 2,167 authored core word entries across beginner Stages A and B, organized into ten real-world topics (greetings, food, daily routines, directions, travel, and practical interactions).
- **Kanji & Kana:** 92 basic kana, 135 variants and combinations, plus 300 contextual kanji entries with readings taught in whole words rather than isolated lists.
- **Interactive Exercises:** Translation, fill-in-the-blank, multiple choice, sentence ordering, and vocabulary matching. Every check has clear objectives, accepted alternative answers, and explanations.

### 2. Reading & Grammar
- **Adjustable Aids:** Toggle furigana (ruby text) and romaji aids on or off whenever you want to test your raw reading comprehension.
- **Everyday Passages & Stories:** Contextual reading exercises including restaurant menus, train schedules, practical text messages, and short stories with interactive glossaries.
- **Grammar Guides & Dialogues:** Authored scenario dialogues covering polite (`-desu`/`-masu`) and plain speech registers, with focused particle contrast explanations.

### 3. Writing Studio
- **Guided Typing:** Practice entering Japanese sentences using your physical keyboard and native Japanese IME.
- **Composition Workspace:** Save essays and short responses with automatic local drafting, revision history, and conflict preservation if you edit across multiple browser tabs.
- **Character Formation:** Practice stroke order on an interactive canvas using vector stroke templates, accompanied by keyboard alternatives.

### 4. Spaced Repetition & Reviews
- **FSRS Scheduling:** Four-button rating (`Again`, `Hard`, `Good`, `Easy`) with deterministic scheduling, memory stability, and difficulty tracking.
- **Mistake Queue:** Automatically collects questions you missed during lesson sessions so you can practice them until they stick.
- **Custom Collections:** Build your own themed vocabulary collections and drill them across multiple directions (reading, meaning, or typing).

---

## Quickstart

### Prerequisites
- **Node.js:** Node 22+ (Node 24 LTS recommended)
- **Python:** Python 3.11+
- **Platform:** Windows, macOS, or Linux (native Windows is first-class)

### One-Command Setup (Windows)

From the project root in PowerShell:

```powershell
.\scripts\start.ps1
```

This runs database migrations, imports the starter course definitions, launches the FastAPI backend (port 8000) and the Vite frontend (port 5173), and opens `http://127.0.0.1:5173` in your default browser.

Press `Ctrl+C` in the terminal to stop all services cleanly.

---

### Manual Setup & Cross-Platform

If you prefer running services manually or you are on Linux or macOS:

#### 1. Backend Setup
```bash
cd backend
python -m venv .venv

# Activate virtual environment:
# Windows:
.\.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.lock
alembic upgrade head
python -m app.cli import
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

The interactive OpenAPI documentation will be available at `http://127.0.0.1:8000/docs`.

#### 2. Frontend Setup
In a separate terminal:
```bash
cd frontend
npm ci
npm run dev
```

Open `http://127.0.0.1:5173` in your browser.

---

## Architecture

Trilingo uses a modular local-first architecture:

- **Frontend:** React 19, TypeScript (strict mode), Vite, Tailwind CSS, and Zod schemas for runtime response validation.
- **Backend:** FastAPI, Python 3.11+, SQLAlchemy 2.0, Alembic for schema migrations, and Pydantic v2 schemas.
- **Database:** SQLite with Write-Ahead Logging (WAL) enabled for clean concurrent reads and atomic writes.
- **Audio & Speech (Optional):** Pluggable local provider adapters for Kokoro TTS and Whisper STT running on loopback ports. If disabled, all exercises provide full text and transcript fallbacks without loss of practice credit.

---

## Data Safety, Backups & Reset

Your learning data belongs to you. You can export or restore complete snapshots directly from the **Profile** page or via the API:

- **Native SQLite WAL Backup:** Exports a byte-consistent zip archive containing your database and a versioned `manifest.json`.
- **What is backed up:** Study sessions, attempts, XP ledger, review cards, FSRS states, writing drafts, revisions, character drawing samples, vocabulary collections, and badges. Credentials, transient audio recordings, and temporary caches are omitted.
- **Validated Restore:** Previews snapshot timestamp, profile name, XP summary, and schema compatibility before you confirm.
- **Automatic Safety Backups:** Before performing any restore or progress reset, Trilingo automatically saves a safety copy of your current database to `.data/backups/`.
- **Clean Reset:** Lets you clear learner progress without wiping out installed course content or lesson definitions.

---

## Running Tests

### Frontend Gates
From `frontend/`:
```bash
npm run lint          # ESLint with strict TypeScript rules
npm run typecheck     # TypeScript compiler check (tsc --noEmit)
npm test              # Vitest test suite
npm run build         # Production Vite build
```

### Backend Gates
From `backend/`:
```bash
python -m ruff check app tests migrations    # Code style & linting
python -m pytest -q                          # Pytest test suite
python -m app.cli validate                   # Course content integrity check
```

---

## Contributing

We welcome contributions from developers, designers, and Japanese speakers:
- **Code:** Check out [`CONTRIBUTING.md`](CONTRIBUTING.md) for code style guidelines and testing practices.
- **Japanese Content:** If you notice a typo, an awkward translation, or a missing valid alternative answer, please open an issue using the [Content Correction template](.github/ISSUE_TEMPLATE/content_correction.md).
- **Security:** Please review [`SECURITY.md`](SECURITY.md) to report vulnerabilities privately.

---

## License & Attribution

- **Source Code:** Licensed under the [MIT License](LICENSE). Copyright (c) 2026 Justin Reyes.
- **Course Content & Curriculum:** All educational content, vocabulary entries, grammar guides, and exercise data under `content/` are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
