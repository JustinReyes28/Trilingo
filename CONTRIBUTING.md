# Contributing to Trilingo

Trilingo is a local-first Japanese learning app built for people who want to study on their own terms. We built it because we wanted a clean language tool that treats learners like adults: no lives, no energy timers, no cooldowns, and no cloud tracking.

Whether you are squashing a UI bug, optimizing an SQLite query, or correcting a Japanese translation, we are glad you are here.

---

## Core Principles

Every contribution must honor these three rules:

1. **Unrestricted study:** Learning stays self-directed. All published lessons, units, and review modes must remain accessible without hearts, energy locks, timers, paid gates, or cooldowns. Never add artificial friction.
2. **Honest evidence:** Assisted, revealed, or skipped exercises must never be counted as unassisted mastery. At the same time, mistakes must never block continuation or penalize access.
3. **Local-first and private:** Core learning, data persistence, and grading must work 100% offline. No third-party tracking, telemetry, or mandatory cloud accounts. Reference audio plays from the bundled static MP3 pack, with zero external or local AI, STT, microphone capture, or runtime TTS providers.

---

## What We Need Help With

### 1. Code Contributions (Engine, Backend, Frontend)
- **Frontend Stack:** React 19, TypeScript (strict mode), Vite, Tailwind CSS, Zod.
- **Backend Stack:** Python 3.11+, FastAPI, SQLAlchemy, Alembic, Pydantic v2, SQLite with Write-Ahead Logging (WAL).
- **Quality Gates:**
  - Frontend: `npm run lint`, `npx tsc --noEmit`, `npm test`, `npm run build`
  - Backend: `ruff check app tests migrations`, `pytest -q`
  - Migrations: Every schema change requires a tested Alembic migration that runs cleanly forward.

### 2. Japanese Curriculum & Content Review
You do not need to write code to contribute. We actively welcome reviews from native speakers, teachers, and experienced learners:
- **Content Location:** Curriculum files live under `content/courses/ja-starter/` and authored drafts live in `content/authoring/ja/`.
- **What to look for:**
  - Natural, contemporary Japanese phrasing.
  - Contextual kanji readings in whole words rather than isolated character lists.
  - Distinguishing valid synonyms and homophones from actual mistakes.
  - Register nuances (e.g. polite `-desu`/`-masu` versus casual plain form).
- When submitting corrections or reviewing vocabulary batches, please include a quick explanation of the pedagogical nuance so others can learn from it.

---

## Local Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/JustinReyes28/Trilingo.git
cd Trilingo
```

### 2. Backend setup
```bash
cd backend
python -m venv .venv

# Activate:
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.lock
alembic upgrade head
python -m app.cli import
uvicorn app.main:app --reload --port 8000
```

### 3. Frontend setup
In another terminal:
```bash
cd frontend
npm ci
npm run dev
```

---

## Pull Request Guidelines

1. **Branch cleanly:** Create a feature branch off `main` (`git checkout -b fix/reading-furigana-toggle`).
2. **Keep it focused:** Small, single-purpose pull requests get reviewed and merged much faster than sprawling multi-feature refactors.
3. **Add tests:** If you are fixing a bug, add a regression test proving the fix works. If you are adding a feature, add unit tests for it.
4. **Run the quality gates:** Make sure linting, typechecking, and tests pass locally before pushing.
5. **Respect line endings:** Keep `.gitattributes` LF normalization intact.
