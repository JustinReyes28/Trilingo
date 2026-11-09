# Contributing to Trilingo

Thank you for your interest in contributing to Trilingo! Trilingo is an open-source, local-first Japanese language learning application designed for autonomous, unrestricted study.

## Core Principles

1. **Unrestricted Study:** Learning is self-directed. All published lessons, units, and review modes must remain freely accessible without hearts, energy locks, timers, paid gates, or cooldowns.
2. **Honest Evidence:** Assisted, revealed, or skipped exercises must never be reported as unassisted masteries, but mistakes never block continuation.
3. **Local-First & Offline:** Core learning, persistence, and grading work 100% offline without external cloud dependencies or forced AI accounts. Optional AI or local TTS/STT are strictly advisory enhancements.

## Ways to Contribute

### 1. Code Contributions (Engine, Backend, Frontend)
- **Frontend Stack:** React 19, TypeScript (strict mode), Vite, Tailwind CSS, Zod.
- **Backend Stack:** Python 3.11+, FastAPI, SQLAlchemy, Alembic, Pydantic v2, SQLite with WAL mode.
- **Quality Gates:**
  - Frontend: `npm run lint`, `npx tsc --noEmit`, `npm test`, `npm run build`
  - Backend: `ruff check app tests migrations`, `pytest`
  - Migrations: Every database schema change requires an Alembic migration tested against clean and populated databases.

### 2. Japanese Curriculum & Content Review
Pedagogical contributions and language review are especially welcome:
- **Japanese Content:** Located under `content/courses/ja-starter/` and authored drafts under `content/authoring/ja/`.
- **Review Criteria:**
  - Grammatical accuracy and natural contemporary Japanese phrasing.
  - Accurate pitch/pronunciation readings and appropriate contextual kanji usage.
  - Distinct homophones and justifiable distractors.
  - Cultural register appropriateness (polite `-desu`/`-masu` vs. plain form distinctions).
- Qualified reviewers: When submitting corrections or reviewing vocabulary/grammar batches, please include notes on the pedagogical rationale and any regional/register nuances.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JustinReyes28/Trilingo.git
   cd Trilingo
   ```

2. **Backend setup:**
   ```bash
   cd backend
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate

   pip install -r requirements.lock
   alembic upgrade head
   python -m app.seed
   uvicorn app.main:app --reload --port 8000
   ```

3. **Frontend setup:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Pull Request Guidelines

1. Create a feature branch from `main`: `git checkout -b feature/my-feature-name`.
2. Ensure all relevant automated tests pass before opening a pull request.
3. Keep pull requests focused on a single coherent change.
4. Include regression tests for bug fixes.
5. Adhere to existing code formatting and type safety conventions.
