# AGENTS.md — Trilingo

Mandatory guidance for every agent working in this repository, both orchestrators and subagents. Explicit user instructions come first. After that, follow the most specific project rule while preserving working behavior.

## Start here

- Read [README.md](README.md), [HANDOFF.md](HANDOFF.md), [AI_IMPLEMENTATION_PLAN.md](AI_IMPLEMENTATION_PLAN.md) and the owning phase/track. The next-work order is in [the remaining-work execution plan](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md). Open other plans only when the task depends on them.
- Inspect affected source, tests, API contracts, models and migrations. Search for existing implementations before adding anything.
- Loop: inspect → smallest coherent change → targeted test → review diff → update docs/checklists. Fix root causes and add regression coverage. Refactors preserve behavior unless the user requests a change.
- Optimize for speed: finish one coherent deliverable, run the relevant checks once, fix real failures and report. Do not overextend scope, repeat unchanged full suites or re-run broad reviews without cause.

## Quick commands

Use Windows PowerShell from the repository root unless noted. The backend uses the root `.venv`.

| Task | Command |
| --- | --- |
| Launch full app | `.\scripts\start.ps1` (migrates, imports course, backend `:8000`, frontend `:5173`) |
| Frontend gates (`frontend/`) | `npm run lint` · `npm run typecheck` · `npm test -- --run` · `npm run build` |
| Backend gates (`backend/`) | `..\.venv\Scripts\python.exe -m ruff check app migrations tests` · `..\.venv\Scripts\python.exe -m pytest -q` · `..\.venv\Scripts\python.exe -m app.cli validate` |
| Migration/import checks | Use the isolated QA script in [Verification commands](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md#verification-commands-and-report-contract) (`QA_MODE=true` with a disposable `DATABASE_URL`) and never point it at the learner DB. |

## Orchestration and subagent delegation

The primary agent orchestrates. It owns understanding the request, planning, splitting work, integration, final review and the report to the user. Delegate execution to subagents using `inherit` (**Gemini 4 Hydrogen**).

- **Delegate by default:** implementation, writing and running tests/quality gates, codebase/doc research, content batch drafting and validation, browser/screenshot checks, QA-database migration checks and doc/checklist updates.
- **Keep with the orchestrator:** ambiguous requirement or product decisions, architecture/schema design, anything touching the learner's real database, destructive or reset actions, publishing and final sign-off. A trivial edit of a few lines can be done directly when that is faster than writing a brief.
- **Parallelize safely:** run independent packages concurrently and dependent ones in sequence. Give each concurrent subagent disjoint file ownership or an isolated `branch`/`share` workspace, so no two subagents edit the same file at once. Run mutating browser/QA scripts one at a time per QA profile/port.
- **Write self-contained briefs** covering: the goal and acceptance criteria, files in and out of scope, the AGENTS.md rules that apply (subagents must read this file), the exact commands to run, and what to return (changed files, commands and results, failures, open questions). Tell subagents to stop and report instead of guessing when they are blocked or a change would threaten data or these rules.
- **Verify, don't relay:** review every subagent diff and re-run targeted gates on the integrated result, either yourself or with a fresh verification subagent. Never report a subagent's claim as verified without evidence. Send corrections back to the same subagent instead of spawning duplicates. Don't poll; do other work until a subagent reports, and kill stalled or redundant ones.

## Network and external actions

- The connection is no longer metered (user instruction, 2026-11-09). Web search, documentation reads and dependency/runtime/browser/model downloads need no size estimate or transfer approval. Older cellular-data and size-approval rules in plans and evidence logs are superseded, and those logs stay as historical records.
- Install dependencies reproducibly (`npm ci`, pinned Python requirements) and respect lockfiles. Adding a new dependency still follows the architecture rules below.
- These still need explicit user instruction: `git push`, remote repository or visibility changes, release/asset publication, social posts, messages, and sending files to reviewers or other external destinations. Never put secrets or learner data in searches, external provider prompts or uploads.

## Product rules

- Build a local-first personal language-learning app with original Trilingo branding, assets, sounds and course content. Follow the Japanese curriculum/release scope in the plan, and do not copy proprietary Duolingo material.
- **Study is unrestricted.** All published lessons, units, stages, modes, explanations and available cosmetics are directly accessible. Suggested order is advisory.
- Never add hearts/lives/energy, forced recovery, cooldowns, waiting periods, paid/earned access, prerequisite/pass-score locks, daily/session quotas, XP ceilings, mandatory countdowns or forced review queues.
- Keep jump-ahead, skip, hint/reveal, retry, replay, pause/resume, finish and continuation after mistakes available. Batch sizes are freely adjustable conveniences with Show more/all, and new-word counts never limit study.
- Assessments, goals, quests, badges, streaks, reminders and elapsed-time records are optional feedback. Missing a day or goal removes no earned XP, work or access. There is no freeze inventory or repair requirement.
- Keep evidence honest. Skipped/assisted answers and unassessed writing need not count as correct or mastered, but they never block continuation. Keep publication checks, validation, idempotency and safe timeouts.
- Never fake provider success, saved progress, statistics, database-backed data or working controls. Clearly label incomplete or unpublished features and content.

## Architecture and code

- Use the established stack. Frontend: React, strict TypeScript, Vite, Tailwind, Zod. Backend: Python, FastAPI, Pydantic, SQLAlchemy, Alembic, SQLite. Preserve intentional equivalents, use supported runtimes (Node 24 LTS, Python 3.11+) and respect lockfiles. Docker remains optional.
- Keep the learning engine generic. Language-specific behavior and course order/content belong in validated content/configuration, seeds or APIs, never in page components. Each exercise needs a clear objective, validated answers/alternates, concept linkage, difficulty and a useful explanation.
- Route exercises through a reusable renderer with dedicated components, validated discriminated unions and exhaustive handling. Keep fetching, rendering, grading and persistence separate.
- Use strict types and validate external data. No casual `any`, undocumented or unnecessary `@ts-ignore`, or dead code. Public Python and service functions need type hints. Public API schemas stay separate from ORM models.
- Keep routes thin and business logic in services. APIs need consistent validated contracts, appropriate status codes, explicit errors and FastAPI documentation. Never expose stack traces.
- Component state owns transient UI, and client state holds limited caches/session context. Persist progress, attempts, completion, XP, streaks, achievements, review schedules and durable settings in the backend database, never only in localStorage.
- Reuse existing utilities, components, tokens and dependencies. Justify new dependencies and refactors. Avoid speculative infrastructure, N+1 queries, unbounded histories, repeated fetches and eager audio loading.

## Progress and data safety

- Backend services calculate and verify grades, completion, XP, streaks, achievements and review schedules. Never trust client correctness flags, XP amounts, mastery claims or due dates.
- Wrap related writes in one transaction: answers/attempts/evidence, completion/XP/activity, ratings/FSRS/logs, and awards/timestamps.
- Prevent duplicate rewards with idempotency/state checks, and keep an XP ledger where practical. Every genuinely completed new session earns its defined XP with no daily or replay limit. Duplicate network requests count as one event.
- Every persistent schema change needs an Alembic migration. Check whether a migration changes what an existing column means. Update models, review/apply migrations, test, and verify both the clean-database and populated forward-upgrade paths. Never use manual DB edits or runtime table creation instead.
- Use real FSRS state, persisted due dates and review logs, Again/Hard/Good/Easy ratings and deterministic tests. Scheduling stays in the backend, and early review remains available.
- Tests and migration checks use isolated databases and must never modify the learner's real database.
- Require explicit confirmation before resetting or deleting progress, and offer backup/export first. Keep development reset scripts separate from normal workflows.
- If a change threatens progress, conflicts with working progression, reveals committed secrets or corruption, or exposes a fundamental architecture mismatch: preserve the data, report the issue and choose a safe fix.

## Providers and failures

- Core learning, normal grading, XP, progression and review must work with `AI_ENABLED=false`. Optional LM Studio/OpenAI-compatible assistance stays behind provider adapters.
- Keep environment/provider configuration in one place: API URLs, ports, DB path, provider, base URL, model and timeout. Commit `.env.example`, never secrets.
- Give useful recovery guidance for offline/unloaded/incompatible providers, timeouts, malformed responses, network/API failures, stale attempts, missing records, invalid exercises and DB conflicts. Log actionable startup/database/provider/service failures without secrets. Never silently swallow broad exceptions.
- Unavailable bundled audio, disabled `AUDIO_PACK_ENABLED`, missing optional STT, or denied microphone access needs a usable fallback (text alternatives, typed practice, and HTTP `503` `audio_unavailable`). Label transcript comparison as transcript feedback, never as phoneme-level pronunciation assessment.
- Authored reference audio comes solely from the bundled versioned `content/audio/<course>/<version>/` MP3 pack; there is no runtime TTS synthesis or model/voice downloading. Keep AI (`AI_ENABLED`) and STT (`STT_ENABLED`) as the only optional runtime local providers (AI scenario coaching is text-only plus optional STT). Maintainers regenerate and validate the pack with `scripts/build_audio_pack.py` and `scripts/check_audio_pack.py` after text, pronunciation-override, or voice changes; never claim reviewed teaching audio until the manifest records qualified review. The pack is content, not learner data, and model weights/voice packs are never bundled.

## UI workflow

For user-facing work (not backend-only tasks):

- Read [docs/DESIGN_BRIEF.md](docs/DESIGN_BRIEF.md) and [design-system/trilingo/MASTER.md](design-system/trilingo/MASTER.md) if present. Reuse shared tokens/components and documented page overrides, and do not create a competing design system.
- Use `ui-ux-pro-max` for design, interaction, accessibility and stack guidance, and check that search results fit before saving presets. Use `frontend-design` to set a Trilingo-specific direction before coding. Preserve the playful course path and clear Japanese reading/composition.
- Apply `design-skill` detect/audit to actual rendered screens. Record findings and fix major generic-pattern, hierarchy and interaction issues.
- Use semantic controls, accessible names/labels, visible focus, descriptive errors and full keyboard access, including alternatives to drag/reorder. Convey feedback with text or icons as well as color.
- Make these states clear: suggested/available/unpublished, current/complete/skipped/assisted, selection, grading, disabled, loading, error and empty. Keep essential actions reachable.
- Before calling UI work complete, inspect real screens at narrow mobile (320–390px), tablet and desktop widths. Check keyboard/IME, accessibility and loading/error/feedback behavior, record the evidence and fix major issues.
- Invoking a skill does not prove visual quality. Keep unverified or no-UI audit items open. If a skill is unavailable, report it and continue unaffected work.

## Verification and reporting

- Test changed behavior, especially grading, unrestricted access/continuation/retries/replays, uncapped genuine-session XP versus idempotent retries, goals, achievements, streaks and FSRS.
- Streak tests cover the first day, consecutive days, repeated same-day activity, missed days, timezone boundaries and relevant DST behavior.
- Run targeted tests first, then the relevant gates once on the final candidate. Frontend work: lint, typecheck, tests and build. Backend work: tests, Ruff, content validation, migration checks and API smoke. Full-stack work needs both plus one manual critical flow. Documentation-only edits need link/reference checks, not application suites.
- Never hide failures by skipping or deleting tests, weakening assertions, swallowing test errors or relabeling failures as success.
- Review for regressions, duplication, hard-coded assumptions, unhandled errors and style mismatch. Update setup/behavior docs, HANDOFF and the owning plan when affected, and only check off verified work. Stop QA services you started.
- Report the changes and files, data/migration impact, exact commands and results, manual verification, delegated work and how it was verified, limitations, checklist updates and next steps. State what was not run and why. Any unmet required gate means the work is only partially complete.
