# Phase 09 — Review, Quests, and Personal Progress

Status: Partial engineering implementation (2026-10-23); qualified content and/or real-provider gates remain open. Depends on: [Phase 08](PHASE_08_AUDIO_SPEAKING.md). Next: [Phase 10](PHASE_10_RELEASE.md).

Completion handoff: [Plan 9.2](PLAN_09_2_COMPLETION.md) tracks unfinished beginner work across Phases 1–9 before Phase 10. It supplements this phase without changing its existing task status or completion gate.

## Goal

Provide genuine FSRS and useful personal feedback while allowing unlimited self-directed study. Review suggestions, optional quests, badges, goals, and personal records never control access or continuation.

## Deliverables

- [x] Integrate a maintained Python FSRS implementation behind a backend scheduler; persist actual state, parameters/version, due dates, and immutable logs.
- [x] Convert/deduplicate the early mistake queue without losing history. Unscheduled items remain explicitly unscheduled until the learner uses the defined review workflow.
- [ ] Keep separate recall directions and evidence for reading, meaning, typing, listening, and speaking; handwriting self-check remains distinct from objective production.
- [ ] Add due review, voluntary mistake review, collection practice, and flashcard/writing/listening/speaking modes where content/providers exist.
- [x] Support Again/Hard/Good/Easy with accessible reveal/rating controls and explicit self-report labels. Allow study ahead, browsing, skipping, and practice without requiring due reviews first.
- [x] Store committed scheduler output and review logs. No daily new-card quota, maximum study count, or due-date restriction prevents starting another activity.
- [x] Use editable batch sizes as convenience controls, with Show more/all and freely selectable material. Retention settings and due ordering guide scheduling rather than restrict learning.
- [x] Build a practice hub with mistakes, words, kana/kanji, stories, typing/writing, listening, and speaking filters, plus a suggested next task the learner can override.
- [x] Add optional daily/personal quests and monthly badges with repeatable/new assignments on demand. Suggested goal counts are adjustable or hideable; there is no daily assignment quota or lost learning access.
- [x] Add weekly personal bests and history comparisons from real XP/activity/result records, with no fake peers or ranks.
- [x] Add optional elapsed-time matching/recall displays with pause/resume and a hidden-timer option. Activities never expire or fail because time passed.
- [x] Offer every available original cosmetic choice directly; do not require tokens, spending, a shop, or an achievement.
- [x] Add optional levels, evidence-based badges, activity calendars, and current/longest consecutive-day statistics. These are descriptive and hideable, never a curriculum gate or penalty.
- [x] Show honest totals, accuracy, mistakes, reviews, published coverage, completed workflows, and separate skill evidence; missing assessment is labeled as such.
- [ ] Preserve the beginner/later-stage curriculum distinction and self/human/AI feedback provenance. XP and text length do not imply advanced proficiency.
- [x] Persist preferences for reading aids, practice batches, goals, reminder/stat visibility, sound, motion, timezone, and providers. Sound/animation failures never affect learning.

## Intended implementation areas

Review/practice/quests/challenges/achievements/stats/profile/settings features, backend scheduler/statistics/activity services, migrations, and data-driven optional quest/badge definitions. Reuse session/grading services; do not build separate restrictive game systems.

## Personal feedback rules

- Every published item, mode, collection, and assessment is directly selectable. The learner can study new material before due review, repeat a just-reviewed item, request more new words, skip, or switch activities at any time.
- Distinguish Browse/Practice from an intentional Review now rating. Browsing or skipping preserves schedule state; an explicit review at any time computes a valid next FSRS state and logs the actual event. Do not reject a deliberate review solely because the card is not due.
- New genuine completed sessions use Phase 4's uncapped XP policy. Retry delivery of one already-committed event does not award it again. No once-per-day or replay-frequency reward restriction is added here.
- Optional quests use stable assignment/source-event IDs and truthful predicates. Learners can choose/add/repeat new assignments without a daily maximum. A completion badge/goal tracks its own criteria without controlling lessons, other quests, or cosmetic access.
- A writing-workflow quest can count a committed intended composition submission as practice completion, with optional self-review recorded separately. It cannot substitute for objective correctness; autosaves, character counts, and AI scores alone do not establish mastery.
- If a provider fails, any unfinished audio-specific quest can switch to a core task under the same assignment identity. Record the definition change, preserve real evidence, and recompute only valid progress; already credited completion events are not duplicated and unperformed speech is never counted.
- Monthly badges can use an optional editable target such as 20 completed personal quests. Missing that goal has no effect on earned XP, work, access, or future practice; there is no expiring consumable or repair requirement.
- Weekly records compare the learner only with their own stored local-date history. An elapsed-time result records actual active/pause intervals and assistance; invalid timing omits that personal timing record while preserving learning evidence and normal continuation.
- Cosmetic preferences are simple durable selections from installed assets. Badges may celebrate an observed result, but selecting a theme/accent never requires earning or spending anything.
- Optional streak statistics describe actual activity. Missing a day may start a new consecutive-day count, while longest streak and total active days remain visible; no XP, lesson, portfolio, or access is lost. No freeze inventory or recovery activity is required.
- Individual objective grades and unaided/assisted evidence stay honest. Badge/score criteria never become lesson-entry, continuation, hint, retry, or resource-access rules.

## Data and API contracts

- Persist actual FSRS card state and scheduler version/parameters, UTC due instants, last review, and immutable transitions/logs. The server computes schedules; the browser cannot submit an arbitrary due date.
- Use stable profile/content/objective/direction IDs and an intentional review event identity. Rating a real review twice due to network retry cannot apply the transition twice; a new learner-requested review is a new event even on the same day.
- Offer explicit `/api/v1` review/session/rating, quest/assignment, optional badge, personal record, activity/statistics, and cosmetic-preference resources. Do not add access tokens, balances, freeze stock, cooldown, or prerequisite APIs.
- Validate records, supported ratings, revision conflicts, and transaction consistency without imposing due-only or score-based study eligibility. Stale changes return actionable recovery options while other learning remains accessible.
- Keep answer reveal/hints freely available and mark the resulting assistance. A voluntary unaided check records only actual unaided answers; switching modes never prevents continuation.
- Use Phase 4 session XP and event idempotency for all study modes. Optional goals/quests/badges are computed from committed events and cannot recursively award the same event.
- Add migrations only for required scheduler, assignment/event, badge/result, activity, and preference state. No learner-resource or purchasing schema is needed.
- Group rating+schedule+log, session finish+XP+activity, and optional quest/badge credit atomically. Do not trust client correctness, XP, completed-quest flags, or fabricated timing.
- Activity dates use preserved profile-local event dates and UTC timestamps. Test current/longest statistics without rewriting history after a timezone change.
- Select recommendations from due work, mistakes, and published topics under documented ordering/cold-start behavior; learner selection always overrides the recommendation.
- Paginate large histories and use efficient aggregates without limiting how much the learner can access through subsequent pages. Skill/coverage counts come from real evidence, never a fabricated fluent meter.
- Later essay portfolios retain rubric/reviewer provenance; only validated authored vocabulary/concept mappings enter FSRS. AI suggestions are not authoritative errors.

## Tests and manual verification

- [ ] Test deterministic real FSRS transitions for all ratings, learning/relearning, due ordering, voluntary early review, repeated new reviews, and preserved logs.
- [ ] Test browse/skip without schedule mutation, unlimited additional batches/new items, and switching away from due reviews to any published content.
- [ ] Test concurrent/stale transitions, duplicate event delivery, rollback, content revisions, and restart persistence without turning data conflicts into study lockouts.
- [ ] Test uncapped real session/replay rewards in one day, event idempotency, ledger totals, optional goal edits, and accurate activity dates.
- [x] Test optional quest selection/new assignments, repeated genuine completions, provider fallback after partial credit, honest predicate changes, and no duplicated source-event credit.
- [ ] Test every available cosmetic can be selected by a new learner without a balance, badge, or prior activity.
- [x] Test optional elapsed-time display, pause/resume, hiding timing, long-running activity without expiry/failure, and preserved learning if timing is invalid.
- [ ] Test actual consecutive/missed-day statistics, timezone/DST, hideable goals/streaks, and unchanged earned XP/work/access after missed activity or a goal.
- [ ] Test separate skill schedules/evidence, feedback provenance, writing workflow versus correctness, unpublished-content status, and no fabricated mastery.
- [ ] Manually study a future-due card, request more new words, skip a review, choose a later lesson, complete repeated sessions, select a cosmetic, restart, and verify freedom plus persisted evidence.
- [ ] Run both quality gates, migration checks, and mobile/keyboard review flows.

## Completion gate

Complete when real FSRS and personal feedback work with unrestricted direct study, any-time voluntary review, uncapped genuine session rewards, honest evidence, and durable state. Optional goals/quests/badges/timing/streaks never restrict continuation or access. All applicable engineering checks remain required.

## Reference basis

The general course/practice/review ideas remain inspired by the sources in the master plan. The user's unrestricted-study decision overrides commercial resource limits, prerequisite locks, countdown pressure, consumable protection, and paid or earned access mechanics. FSRS remains the actual scheduling system, with recommendations freely overridable by the learner.

## Bounded implementation evidence — 2026-10-23

Checked deliverables refer to the implemented technical/draft slice and tested adapter/control contracts, not full beginner publication or real-provider success. [Verification and remaining work](../PHASE_07_09_VERIFICATION.md) records exact scope, commands, responsive evidence, migrations and limitations. All unchecked tests and the full completion gate remain open; no bulk completion is claimed.

Additional-hour scope: direct words/kana/kanji/story/mistake links, optional persisted recall timing and recent self-comparisons, a real 12-week activity calendar, in-page reminder visibility, listening quest predicates and same-assignment fallback history are implemented. Timed recall remains self-rated; audio delivery is not proof of hearing; skipped/text-assisted work never fulfills the listening-specific predicate. The broader per-skill evidence and release/large-history audits remain open. See [follow-up evidence](../PHASE_07_09_FOLLOWUP.md).


## Plan 9.2 follow-up — 2026-10-23

[Current execution evidence](../PLAN_09_2_VERIFICATION.md) records source 0.1.15/schema 0012, verified engineering changes and exact remaining gates. The supported fresh-install, qualified-language/stroke/audio and physical-device requirements remain open. Current improvements include verified official IME documentation, ten-topic draft guide coverage, collection-scoped saved-snapshot recall, complete timing histories and separate skill/workflow/coverage evidence. No full phase or reviewed beginner release is claimed.

## Speaking and collection-audio continuation — 2026-10-24

[Current evidence](../PLAN_09_2_SPEAKING.md) verifies listening/speaking saved-word and collection recall alongside meaning/reading/typing. All use immutable card snapshots and deliberate FSRS ratings; audio/transcript preparation changes no schedule or reward. Speaking-session attempts/agreements/text fallback and self-rated review counts stay separate. Speaking quests preserve same-assignment fallback history and exclude text-only, skipped or missing-reference workflows. Full qualified-content/provider and remaining broader audits are still open.

## Completed recall navigation — 2026-10-25

[The bounded execution continuation](../PLAN_09_2_CURRICULUM.md#five-check-extension--2026-10-25) fixes completed optional recall replay by reopening its saved source card instead of invoking the generic study-start contract. Self-rated completion remains distinct from objective grading. Eight responsive layouts and real loopback API/browser flow prove keyboard return, same snapshot/direction, voluntary future-due review, a new timer, idempotent exact retries, three genuine reviews/15XP and skip without schedule/XP mutation. Existing-dependency frontend gates pass on installed Node24.21.0. This focused evidence does not close the broader manual/device/provider/publication or combined phase gate; existing checkboxes are preserved.
