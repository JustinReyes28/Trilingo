# Phase 04 — Lesson Engine and Unrestricted Study

Status: Implemented and verified for the technical-practice starter slice. Qualified content review remains pending. Depends on: [Phase 03](PHASE_03_CURRICULUM.md). Next: [Phase 05](PHASE_05_READING.md).

## Goal

Deliver playable Japanese lessons with a reusable renderer, durable attempts, honest server grading, and unrestricted access to every published activity.

## Deliverables

- [x] Implement ExerciseSession and ExerciseRenderer with dedicated multiple-choice, translation, fill-blank, sentence-ordering, and matching components.
- [x] Support click/tap and keyboard reorder controls with stable token IDs, including repeated words. Do not depend on Japanese whitespace tokenization.
- [x] Create transactional start, answer, resume, skip, reveal, finish, and replay services; keep route handlers thin.
- [x] Persist lesson/exercise attempts, answer revisions, assistance/skips, mistakes, XP ledger, daily activity, optional streak statistics, goals, and studied/completion evidence.
- [x] Give committed actions a server-issued identity and idempotency key. Return the existing result for a lost-response retry instead of applying its side effects again.
- [x] Show authoritative feedback after a committed grade, with an explanation and freely available Retry, Reveal, Skip, and Continue actions.
- [x] Support refresh/resume, pause/exit, direct lesson selection, unlimited new attempts/replays, and recovery of pending submissions without an artificial session expiry.
- [x] Make all published units, lessons, recaps, placement checks, and mastery exercises directly accessible in both UI and API, regardless of history or score.
- [x] Present suggested order and preparation as advice. Keep course browsing and a learner-selected next activity available after any mistake, skipped prompt, assessment result, or missed goal.
- [x] Reuse the same attempt/grading engine for optional recaps, placement recommendations, and mastery practice. No assessment is required before continuing or jumping ahead.
- [x] Build an early mistake list and voluntary practice flow; Phase 9 adds genuine FSRS without making due reviews mandatory.
- [x] Connect the real course path and completion screen to persisted state, with available/suggested/visited/studied/assisted states instead of prerequisite locks.

## Unrestricted learning and reward rules

- No hearts, lives, energy, forced recovery sessions, cooldowns, paid access, attempt quotas, daily XP ceilings, or once-per-day replay rewards.
- A wrong answer records useful feedback and a mistake. It never deducts XP, ends a session, removes access, or forces corrective practice. The learner can retry, reveal, skip, continue, or choose another activity immediately.
- Suggested learning order, vocabulary batches, daily goals, quests, and due reviews are advisory. Every published activity is accessible from the beginning, including later-stage material once published.
- Finish is an explicit learner action after working through or explicitly skipping the session prompts. Record responses, skips, revealed answers, and assistance separately. Studying/completing a session does not claim every answer was correct or every objective was mastered.
- Award 20 XP for the first committed studied completion of a lesson, and 5 XP for each genuinely completed new replay/practice/review/assessment session. There is no daily or replay-frequency cap. Definitions are centralized and explainable; achievement XP is not a substitute for language evidence.
- An exact retry of the same completion request receives its original result and cannot duplicate XP. Starting and completing a new genuine session is a new event and can earn XP normally. Arbitrary client-supplied XP is rejected.
- Corrected answers use explicit revisions and retain the initial result. Corrections are optional; neither retries nor an incorrect final answer block another activity.
- Daily goals are optional, editable, and hideable; 20 XP can be a suggested starting goal, never a limit or prerequisite. Earned XP and saved work remain after a missed day or goal.
- Activity dates use the profile timezone at event time. Optional current/longest consecutive-day statistics describe actual activity; missing a day changes only that statistic, not learning access, XP, or completed work. No consumable protection inventory is needed.
- All installed/published cosmetic choices are selectable without a token balance or earned-access requirement.
- Core lessons have no countdown. Phase 9 may offer an optional elapsed-time display for personal records, with pause/resume and no expiry, timeout failure, or forced end.

## Optional assessment and assistance rules

- Recaps, placement, and mastery practice are available directly without completing previous lessons. Placement offers a suggested starting point and never grants access that the learner did not already have.
- Record scores and concept coverage from actual submitted answers. A low score, critical mistake, or skipped item gives advice; no pass mark is required to advance, finish, retake, or open another unit.
- Hints and explanations remain available. Revealing an answer records assistance and leaves that prompt unassessed for unaided recall; it never locks or ends the exercise.
- A learner may voluntarily request an unassisted check, then switch to supported practice at any time. Preserve the evidence labels and keep continuation available.
- Optional evidence-based badges can describe a recorded result under published criteria, but the badge never controls study or cosmetic access. An unassessed essay or transcript match must not be labeled proven language mastery.
- Assessments do not silently alter FSRS. Record their results separately; review scheduling changes only through a deliberate review action.

## Intended implementation areas

Lesson/exercise/progression features, backend grading/activity/reward services and repositories, migrations, and isolated tests. Keep Japanese-specific policies out of generic session and XP functions.

## Data and API contracts

- Under `/api/v1`, provide lesson/session start, attempt detail/resume, answer, skip/reveal, finish/replay, and progress/XP/activity/daily-goal resources. Do not add a learner energy or prerequisite-eligibility resource.
- Client submits answers, supported learner actions, and identifiers. Server calculates grades, studied/completion evidence, XP, dates, and statistics; no client correctness/XP assertion is trusted.
- Use 404 for missing/unpublished content, 409 for a real stale revision or incompatible mutation, and 422 for invalid payloads. Recoverable errors preserve work and offer retry/reload/new attempt; they are not gameplay penalties.
- Snapshot content version and order at attempt start; preserve original answers, grades, assistance, skips, and corrections. A content change cannot erase historical evidence.
- Use session kinds such as `lesson`, `replay`, `practice`, `review`, and `assessment` with validated mode metadata. Story, writing, recap, placement, mastery, and elapsed-time modes share these services and the same uncapped session reward policy.
- Suggested preparation/concept links are metadata, not access checks. Published status reflects content availability and validation; unpublished work is clearly described as unavailable content rather than a locked reward.
- Use uniqueness constraints and transactions for answer+evidence+mistake and finish+XP+activity. Record optional badge awards once per earned milestone without restricting future attempts.
- Separate first-answer accuracy, assisted practice, explicit skips, studied completion, and actual reviewed skill evidence. Optional quest predicates must respect those distinctions without controlling learning access.

## Tests and manual verification

- [x] Test all graders, authored alternatives, invalid answers, duplicate labels/tokens, and honest assisted/skipped/unfinished evidence.
- [x] Test a new learner directly opening every published lesson/assessment, including a later unit, without completion history or a passing score.
- [x] Test repeated incorrect answers, reveal/hint/skip, optional corrections, finishing with mistakes/skips, and immediate continuation to another activity.
- [x] Test unlimited genuine replays/practice in the same day with normal XP, and idempotent lost-response/double-completion requests without duplicate side effects.
- [x] Test server-controlled XP, ledger totals, transaction rollback, stale revisions, and recovery of pending submissions.
- [x] Test assessment retakes and changing from unassisted to supported practice without access changes or fabricated evidence.
- [x] Test optional goals and actual-activity dates across first/consecutive/repeated/missed days, timezone boundaries/changes, and DST with a deterministic clock; XP/work/access remain intact after a missed day.
- [x] Manually jump to a later lesson, answer incorrectly several times, reveal/skip, finish, replay, restart, and verify saved evidence and immediate access.
- [x] Run both quality gates and clean/populated-database migration checks; verify mobile and keyboard lesson use.

## Completion gate

Complete when the first course slice supports unrestricted direct study and continuation, optional assessments and honest evidence work, real new sessions earn uncapped rewards, duplicate requests stay idempotent, and persisted state survives restart. Data validation and applicable test/build/migration gates remain required engineering checks. FSRS/audio arrive in their own phases.

## Implementation evidence — 2026-10-23

[Phase 4 verification](../PHASE_04_VERIFICATION.md) records the exact commands, migration and browser evidence. Five exercise controls share authoritative grading and transactional session services; attempt snapshots, action receipts, mistakes and XP/activity survive restart and content updates. Draft recap/placement/mastery banks are explicitly previewed, with unassisted/supported choices and advisory placement recommendations. No content is promoted from draft by this milestone.

Frontend lint/typecheck/15 tests/build and backend78 tests/Ruff pass. Empty and populated migrations pass. Browser checks cover56 responsive layouts, interrupted actions, IME events, save/reload/replay, all renderers, loading/empty/error recovery and keyboard use. Independent design-skill axes found no remaining scoped findings after fixes; physical IME/screen-reader sessions and qualified Japanese review remain separate limits.
