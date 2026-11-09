# Phase 02 — Interface and Design System

Status: Verified for the current shell/component/fixture scope. Depends on: [Phase 01](PHASE_01_FOUNDATION.md). Next: [Phase 03](PHASE_03_CURRICULUM.md).

## Goal

Build the recognizable learning flow requested by the user: a friendly course path, clear lesson states, short focused exercises, and visible progress, using Trilingo's own identity.

## Deliverables

- [x] Read and apply `ui-ux-pro-max`, `frontend-design`, and `design-skill` using the [design brief](../DESIGN_BRIEF.md). Run an appropriately scoped search, assess fit, and record the product-specific direction before coding.
- [x] Establish `design-system/trilingo/MASTER.md` with verified palette/type/layout/token decisions and justified page overrides. Avoid generic marketing presets or competing design systems.
- [x] Define reusable tokens for color, spacing, typography, focus, borders, elevation, motion, and feedback states.
- [x] Select readable Latin and Japanese fonts with documented licensing and local fallback; ensure kana, kanji, and ruby text remain legible.
- [x] Create shared Button, Card, Badge, ProgressBar, Dialog, FeedbackPanel, PageContainer, and LessonNode components where actually reused.
- [x] Build desktop side navigation, central path area, and an optional progress sidebar that collapses on smaller screens.
- [x] Build mobile navigation with Learn, Practice, Library, and Profile destinations. Expose Reading, Writing, and Speaking within Practice.
- [x] Define a scrolling unit path with large directly selectable published lesson nodes, suggested/current/visited/studied states, and unit guide access. Suggested order is advisory; unpublished content is labeled honestly.
- [x] Design freely available replay, optional recaps/placement/mastery, and choose-any-lesson actions, with assessed results distinct from studied completion.
- [x] Design story/audio-episode cards, practice filters, optional quests/badges/statistics, personal bests, and freely selectable cosmetic preferences. No fictional rank or consumable-resource display.
- [x] Define the lesson frame: exit/resume, progress, prompt, input, Check, feedback, Retry, Reveal/Hint, Skip, Continue, and Finish, with clear direct navigation.
- [x] Define a quiet beginner draft-writing surface and later editor/feedback layout that preserve Japanese text readability and IME behavior; advanced controls remain outside the initial beginner flow.
- [x] Define studied/completed/assisted/skipped, empty course, provider unavailable, loading, retry, and saved-input recovery states. An incorrect answer never disables continuation.
- [x] Wire existing profile/settings/health actions to actual APIs. Keep feature destinations without an implementation explicitly marked Upcoming or disabled.
- [x] Put temporary fixture previews only in a clearly labeled development preview/test area. Never show invented XP, streaks, or learning statistics as saved progress.
- [x] Write original interface copy, icons/illustrations, and completion treatments. Use familiar mechanics without copying Duolingo artwork or proprietary screens verbatim.

## Intended implementation areas

`frontend/src/components`, `frontend/src/styles`, `frontend/src/app`, and feature page shells. Later phases supply API-backed content and behavior; this phase must not hard-code a production lesson database in components.

## Data and API contracts

- No new persistent schema is required solely for a design system. Reuse settings from Phase 1 for reduced motion, sound effects, and reading aids.
- LessonNode receives explicit published/learning states and an accessible label; it never infers a prerequisite lock or awards XP.
- FeedbackPanel receives the server's graded result and authored explanation, and displays a textual result with an icon.
- API failures keep the user's input where appropriate and offer a safe retry. Submission controls show pending state and prevent accidental double activation.
- Reading aids will support Japanese `lang` metadata and semantic ruby markup. Exercise instructions declare when answers/readings should be hidden until submission.

## Tests and manual verification

- [x] Component tests cover disabled, pending, focus, feedback, and lesson node states.
- [x] Dialog tests verify focus containment, Escape behavior where safe, and focus restoration.
- [x] Keyboard-only review verifies navigation, answer selection, dialogs, and primary actions.
- [x] Check representative pages at 320px, 390px, approximately 768px, and desktop widths; no essential action is off-screen or hidden under sticky navigation.
- [x] Check long English errors, long Japanese prompts, browser zoom, high text size, and ruby line height.
- [x] Check contrast, meaningful labels, non-color correctness cues, reduced motion, and touch targets.
- [x] Verify optional elapsed-time displays can be hidden/paused, never expire an activity, and never control study access. Test direct later-lesson selection and continuation after repeated errors/skips.
- [x] Inspect rendered shell/component previews for path, exercise/feedback, Japanese reading, and basic writing against the design brief, using clearly labeled fixtures where live features do not exist yet. Record screenshots, relevant design-skill findings, fixes, and limitations. Repeat the review against real feature behavior in its owning phase; these previews do not require Phase 5/6 features to exist early.
- [x] Run the frontend gate from the master plan; repeat backend checks only if backend behavior changed.

## Completion gate

Complete when the required skill workflow/design decisions are recorded, real shell/components/interactions work, and rendered responsive/keyboard/Japanese typography reviews have no unresolved major findings. Course learning remains unimplemented until later phases. Do not describe a visual shell as a complete learning app or mark a visual audit passed before a UI exists.


## Implementation evidence — 2026-10-23

[Design system](../../design-system/trilingo/MASTER.md), [verification](../PHASE_01_03_VERIFICATION.md), and [.design-skill audit](../../.design-skill/audit-report.md) record the direction, screenshots, findings and fixes. Responsive/keyboard/dialog/IME-event/error/recovery checks ran on real rendered screens. Later feature designs are explicitly labeled fixtures; they do not save grades, XP or drafts. Physical IME and screen-reader sessions remain documented limits and must be repeated in their owning skill phases.
