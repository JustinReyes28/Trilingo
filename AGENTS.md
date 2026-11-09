# AGENTS.md — Trilingo

Mandatory guidance for agents working in this repository.

## Start here

Read [README.md](README.md), [AI_IMPLEMENTATION_PLAN.md](AI_IMPLEMENTATION_PLAN.md), and the relevant phase before editing. Inspect affected source, tests, API contracts, models, and migrations; search for existing implementations before adding anything. Follow the most specific project rule while preserving working behavior.

Work in small steps: inspect → implement the smallest coherent change → test → review the diff → update relevant docs/checklists. Fix root causes with regression coverage; refactors preserve behavior unless a change is requested.

## Cellular data and external transfers

- The connection is cellular/metered. Prefer installed tools, local files/caches and loopback services; focused web search and ordinary documentation reads are allowed.
- Before any external download or upload, ask the user for approval with the purpose, exact source/destination, transfer scope and estimated total network size in MB/GB, including dependencies/layers. State uncertainty and disk requirements separately. This includes package/runtime/browser/model/container downloads, Git transfers, reviewer files, release assets and social media uploads.
- Wait for explicit approval of that bounded transfer/batch; stop before exceeding the approved scope/estimate. Do not auto-retry failed transfers or treat a missing cache/unknown size as permission. No remote publishing or messaging is implied.
- Local editing, builds/tests, local backup export and confirmed local-provider calls need no transfer approval. Follow the detailed protocol and next-work sequence in [the remaining-work execution plan](docs/plans/REMAINING_WORK_EXECUTION_PLAN.md).

## Product rules

- Build a local-first personal language-learning app with original Trilingo branding, assets, sounds, and course content. Follow the Japanese curriculum/release scope in the plan; do not copy proprietary Duolingo material.
- **Study is unrestricted.** All published lessons, units, stages, modes, explanations, and available cosmetics are directly accessible. Suggested order is advisory.
- Never add hearts/lives/energy, forced recovery, cooldowns, waiting periods, paid/earned access, prerequisite/pass-score locks, daily/session quotas, XP ceilings, mandatory countdowns, or forced review queues.
- Keep jump-ahead, skip, hint/reveal, retry, replay, pause/resume, finish, and continuation after mistakes available. Batch sizes are freely adjustable conveniences with Show more/all; new-word counts never limit study.
- Assessments, goals, quests, badges, streaks, reminders, and elapsed-time records are optional feedback. Missing a day/goal removes no earned XP, work, or access; no freeze inventory or repair requirement.
- Keep evidence honest: skipped/assisted answers and unassessed writing need not count as correct/mastered, but never block continuation. Retain publication checks, validation, idempotency, and safe timeouts.
- Never fake provider success, saved progress, statistics, database-backed data, or working controls. Clearly label incomplete/unpublished features and content.

## Architecture and code

- Use the established React/strict TypeScript/Vite/Tailwind/Zod frontend and Python/FastAPI/Pydantic/SQLAlchemy/Alembic/SQLite backend. Preserve intentional equivalents; use supported runtimes and respect lockfiles. Docker remains optional.
- Keep the learning engine generic. Put language-specific behavior and course order/content in validated content/configuration, seeds, or APIs, never page components. Exercises need clear objectives, validated answers/alternates, concept linkage, difficulty, and useful explanations.
- Route exercises through a reusable renderer with dedicated components, validated discriminated unions, and exhaustive handling. Keep fetching, rendering, grading, and persistence responsibilities focused.
- Use strict types and validate external data. No casual `any`, undocumented/unnecessary `@ts-ignore`, or dead code. Python public/service functions need type hints; public API schemas are separate from ORM models.
- Keep routes thin and business logic in services. APIs need consistent validated contracts, appropriate status codes, explicit errors, and FastAPI documentation; never expose stack traces.
- Component state owns transient UI; client state holds limited caches/session context. Persist progress, attempts, completion, XP, streaks, achievements, review schedules, and durable settings in the backend/database, never solely in localStorage.
- Reuse existing utilities, components, tokens, and dependencies. Justify new dependencies/refactors; prefer maintained packages only when the current stack cannot solve the problem cleanly. Avoid speculative infrastructure, N+1 queries, unbounded histories, repeated fetches, and eager audio loading.

## Progress and data safety

- Backend services calculate/verify grades, completion, XP, streaks, achievements, and review schedules. Never trust client correctness flags, XP amounts, mastery claims, or due dates.
- Use transactions for related writes: answers/attempts/evidence, completion/XP/activity, ratings/FSRS/logs, and awards/timestamps.
- Prevent duplicate rewards with idempotency/state checks; keep an XP ledger/history where practical. Every genuinely completed new session may earn its defined XP without daily or replay limits. Duplicate network requests are one event.
- Every persistent schema change requires a migration; assess migrations for changed column meanings. Update models, review/apply migrations, test, and verify clean-database and populated forward-upgrade paths. Never substitute manual DB edits or runtime table creation.
- Use real FSRS state, persisted due dates and review logs, Again/Hard/Good/Easy, and deterministic tests. Scheduling lives in the backend per the implementation plan; early review remains available.
- Use isolated test databases; tests and migration checks must never modify the learner's real database.
- Require explicit confirmation before resetting/deleting progress; offer backup/export and separate development reset scripts from normal workflows.
- If a change threatens progress, conflicts with working progression, reveals committed secrets/corruption, or exposes a fundamental architecture mismatch, preserve data, report the issue, and choose a safe fix.

## Providers and failures

- Core learning, normal grading, XP, progression, and review must work with `AI_ENABLED=false`. Keep optional LM Studio/OpenAI-compatible assistance behind provider adapters.
- Centralize environment/provider configuration: API URLs, ports, DB path, provider, base URL, model, and timeout. Commit `.env.example`, never secrets.
- Handle offline/unloaded/incompatible providers, timeouts, malformed responses, network/API failures, stale attempts, missing records, invalid exercises, and DB conflicts with useful recovery guidance. Log actionable startup/database/provider/service failures without secrets; do not silently swallow broad exceptions.
- Missing TTS/audio/STT or denied microphone access must have usable fallbacks. Label transcript comparison as transcript feedback, never phoneme-level pronunciation assessment.

## UI workflow

For user-facing work (not backend-only tasks):

- Read [docs/DESIGN_BRIEF.md](docs/DESIGN_BRIEF.md) and any existing `design-system/trilingo/MASTER.md`. Reuse shared tokens/components and documented page overrides; do not create a competing design system.
- Read/use `ui-ux-pro-max` for relevant design, interaction, accessibility, and stack guidance; assess search-result fit before persisting presets.
- Read/use `frontend-design` to establish a Trilingo-specific direction before coding. Preserve the playful course path and clear Japanese reading/composition.
- Apply `design-skill` detect/audit guidance to actual rendered screens; record findings and fix major generic-pattern, hierarchy, and interaction issues.
- Use semantic controls, accessible names/labels, visible focus, descriptive errors, and keyboard access, including alternatives for drag/reorder. Communicate feedback with text/icons as well as color.
- Make suggested/available/unpublished, current/complete/skipped/assisted, selection, grading, disabled, loading, error, and empty states clear. Keep essential actions reachable.
- Before UI completion, inspect real screens at narrow mobile (320–390px), tablet, and desktop widths. Check keyboard/IME, accessibility, and loading/error/feedback behavior; record evidence and fix major issues.
- Skill invocation alone does not prove visual quality. Keep unverified/no-UI audit items open; report unavailable skills and continue unaffected work.

## Verification and reporting

- Test changed behavior, especially grading, unrestricted access/continuation/retries/replays, uncapped genuine-session XP versus idempotent retries, goals, achievements, streaks, and FSRS.
- Streak tests cover first day, consecutive days, repeated same-day activity, missed days, timezone boundaries, and relevant DST behavior.
- Run targeted tests first, then relevant quality gates: frontend lint, typecheck, tests, production build; backend tests, migration checks, API smoke; full-stack work needs both plus a manual critical flow. Use the plan/README for actual commands.
- Never hide failures by skipping/deleting tests, weakening assertions, swallowing test errors, or relabeling failures as success.
- Review for regressions, duplication, hard-coded assumptions, unhandled errors, and style mismatch. Update setup/behavior docs and the plan when affected; only check off verified work.
- Report changes/files, data/migrations, exact commands/results, manual verification, limitations, checklist updates, and next steps as relevant. State what was not run and why; unmet required gates mean partial completion.
