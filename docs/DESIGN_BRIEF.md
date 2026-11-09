# Trilingo Design Brief and UI Quality Contract

Status: Implemented for the Phases 1-3 shell and development fixtures. Shared tokens and rendered evidence are recorded in the design system and phase verification record; later real-feature audits remain open.

This brief supports the UI rules in [AGENTS.md](../AGENTS.md) and [Phase 2](plans/PHASE_02_INTERFACE.md). Apply it to every user-facing surface, including later paragraph/essay tools in the [curriculum roadmap](CURRICULUM_ROADMAP.md).

## Product direction

Build a personal Japanese study app with a friendly gamified course path and a focused reading/writing workspace. It should feel encouraging during short lessons and calm during longer composition. The main screen's job is to make the next useful learning action obvious.

Keep large directly selectable published path nodes, clear progress states, tactile answer controls, and satisfying committed feedback. Show suggested study order as advice and keep Retry, Reveal/Hint, Skip, Continue, and direct navigation reachable. Establish original branding/assets. Longer reading and essay screens need clear Japanese typography, quiet surrounding controls, and enough space to compose.

Use actual learner-facing content to make layout decisions: kana, mixed kanji/kana, furigana, multi-line questions, long errors, audio transcripts, and draft feedback. No marketing hero, invented testimonials/statistics, or three interchangeable feature tiles in place of a study workflow.

## Required skill workflow

For new UI and meaningful UI changes:

1. Read the installed `ui-ux-pro-max` skill. Use a design-system search for a new overall direction or one focused domain search for a specific concern; use the project's React/Tailwind stack for relevant implementation guidance. Inspect result fit instead of accepting its first preset.
2. Read `frontend-design`. Write down the page's job, visual hierarchy, type roles, spacing/layout, palette rationale, and one coherent visual signature before building. Preserve the user's requested playful learning flow.
3. Use `design-skill` detect/audit guidance against the actual rendered target when available. Turn findings into concrete fixes with reasons; a detector score or the statement "used a skill" is not a visual quality gate.
4. Persist verified design decisions in `design-system/trilingo/MASTER.md` during Phase 2 and page-specific overrides only where needed. Read and update existing decisions deliberately; do not generate a second competing token system or overwrite a master with `--force` without authorization.
5. Implement, inspect rendered screenshots/interactions, fix issues, and record the audit evidence at the phase gate. Do not mark a visual check passed before a UI exists.

Use installed skill catalog paths, not an invented `/ui/ux` command or a repo-local script assumed to exist. Record an unavailable skill honestly and continue unaffected work; UI checks remain open until the required workflow can be verified.

## Design decisions to establish in Phase 2

- [ ] Choose a small named palette with semantic roles and verified contrast. Explain the choice for Trilingo; avoid selecting a category-default hue just because the product is software.
- [ ] Choose a complementary Latin/Japanese type system and readable scales, with Japanese glyph coverage, local font fallback, licensing, ruby height, and suitable composition line length.
- [ ] Establish spacing, density, borders, radii, elevation, focus, motion, and icon rules as reusable tokens. A playful button may have depth without every panel needing a shadow or gradient.
- [ ] Define Learn, Practice, Library, Profile, and later Writing Workshop navigation with one clear next action per surface. Advanced writing controls appear when relevant rather than overwhelming a new learner.
- [ ] Prototype the real course path, a text exercise with feedback, reading with furigana, and a writing surface. Use labeled fixtures only in development previews.
- [ ] Define suggested/available/visited/studied/assisted/skipped/unpublished states, selected/correct/incorrect/pending feedback, saved/unsaved, unavailable audio, and retry/conflict. Text/icons accompany color; no score or mistake disables continued study.
- [ ] Make optional animations explain a state change or celebrate a real saved result. Respect reduced motion and keep reading/composition steady.

## Positive alternatives to generic generated UI

- Give the current lesson or active writing task the strongest hierarchy; let secondary progress and rewards support it.
- Use page structures that fit the work: a lesson path, focused question frame, readable passage, or editor/feedback split. Do not wrap every item in the same card grid.
- Use deliberate Japanese/Latin type roles and consistent spacing instead of compensating with decorative gradients, blurred panels, or an icon above every heading.
- Keep one consistent icon family; original illustrations can add character where they help instruction or celebration. Emoji are not a substitute for usable navigation icons.
- Use direct labels such as Check answer, Continue, Save draft, and Review revision, with useful error recovery. Avoid generic promotional headings and filler copy.
- Use actual counts and honest empty states. Future stages are clearly marked planned/unpublished; visual completeness never implies their curriculum is ready.

## Visual and interaction acceptance

- [ ] Capture representative states at 320px, 390px, approximately 768px, and desktop width; primary actions remain reachable with touch/keyboard and on-screen keyboards.
- [ ] Inspect kana, kanji, furigana, longer passages, IME composition, mixed-script input, draft comments, and long validation messages with real Japanese examples.
- [ ] Check visible focus, focus not hidden under sticky UI, labels, contrast, screen-reader order, zoom/text resizing, dialog behavior, and reduced motion. Fix observed problems rather than claiming blanket compliance from a checklist.
- [ ] Compare reading/lesson/editor surfaces to the written direction and shared tokens. Resolve major hierarchy, generic-template, inconsistent spacing/type, and misleading-state findings.
- [ ] Verify interactive states with actual behavior: pending grades, committed feedback, denied microphone, missing TTS, unsaved draft/retry, and empty progress. A screenshot alone does not prove these work.
- [ ] Record screenshots/target viewports, audit findings, fixes, actual commands, and remaining limitations before a UI milestone is marked complete.

## Historical search evidence from the planning task — 2026-10-22

The `ui-ux-pro-max` design-system searches for `Japanese learning web app` and the narrower retry `study workspace dashboard` returned generic marketing/technical presets. Neither was a verified fit for this learner-facing app, so neither was persisted or treated as Trilingo's chosen palette/type system. This brief is a project-specific starting direction, not a claimed database match.

The focused `focus not obscured` UX search returned relevant guidance for persistent headers/footers and keyboard focus. Phase 2 must verify actual behavior in the rendered app. No UI, screenshot review, detector run, or final visual-quality pass occurred in this documentation task.


## Implementation evidence — 2026-10-23

See [design system](../design-system/trilingo/MASTER.md), [audit](../.design-skill/audit-report.md), and [verification](PHASE_01_03_VERIFICATION.md). Actual screens, semantic controls, Japanese text, recovery, dialogs and responsive checks were reviewed. Checkbox criteria below remain scoped to each feature release; no physical IME, screen-reader session, audio provider or advanced-writing capability is implied by the initial shell review.
