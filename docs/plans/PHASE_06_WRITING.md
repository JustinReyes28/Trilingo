# Phase 06 — Japanese Typing, Handwriting, and Composition

Status: Draft-scope engineering implemented and verified. Versioned drafts/conflicts/submissions, checked typing, kana input aid and formation modes pass backend/frontend and real-browser checks. The official IME guide is documentation-verified; qualified task/stroke review and physical hardware checks remain open. Depends on: [Phase 05](PHASE_05_READING.md). Next: [Phase 07](PHASE_07_GRAMMAR_DIALOGUES.md).

## Goal

Teach Japanese input/character formation and build a staged composition workflow from guided beginner messages to complex essays, following the [curriculum roadmap](../CURRICULUM_ROADMAP.md).

## Release scope

The first release implements IME, handwriting practice, guided short paragraphs, basic draft saving, and self-review for Stages A-B. Intermediate Stages C-D add the fuller writing/revision workshop; advanced Stages E-F add source-based essays and portfolios. Later features below are contracts for their own releases, not conditions that must delay the beginner release or claims that advanced content exists now.

## Deliverables

- [x] Add a concise Windows Japanese keyboard/IME guide verified against current official documentation during implementation, plus a check that lets the learner try input.
- [x] Add typed kana, word, sentence, and constrained message exercises through the shared renderer.
- [x] Handle IME composition correctly: Enter confirms conversion during composition and does not prematurely submit an answer.
- [x] Provide a labeled on-screen kana input aid and keyboard-accessible alternatives where needed; it must not force romaji in place of Japanese.
- [ ] Add guided stroke demonstrations, trace practice, and freehand self-check for a reviewed kana set and the first taught kanji words/characters.
- [ ] Support mouse, touch, and stylus pointer input, undo, clear with confirmation when a substantial unsaved drawing exists, and replay of the learner's strokes.
- [ ] Present stroke order, direction, and start-point guidance from reviewed, licensed assets. Record asset source/version/license and required attribution.
- [x] Use a standard grid and scalable normalized coordinates so canvas size/device pixel ratio does not corrupt input.
- [x] Label geometric trace feedback as guided tracing feedback. Freehand v1 is self-assessed after reference reveal, not handwriting recognition or a calligraphy grade.
- [x] Provide a keyboard-accessible stroke-sequence/character-selection practice alternative; record its mode rather than claiming it measures handwriting.
- [x] Let the learner keep optional local writing samples and delete them. Do not require saving raw stroke data for normal progress.
- [x] Store constrained-writing grades separately from open-ended journal practice. Open-ended content can be saved for practice without claiming a validated correct answer.
- [ ] Provide Stage A character/word/first-sentence tasks and at least three Stage B guided composition tasks with reviewed models/alternatives, one simple annotated revision example, and a self-review checklist. Beginner content aids do not require the later workshop UI.
- [x] Add a labeled multi-line Japanese editor with basic backend draft autosave/recovery, saved/unsaved/error states, and revision identity. Drafting/self-review must work with AI disabled.
- [x] Complete the required UI/UX skill workflow and inspect Japanese IME, long input, feedback, and unsaved/retry states against the shared design brief.

## Intended implementation areas

Writing/IME feature components, typed exercise graders, stroke asset loader, writing content, backend evidence services, and migrations for durable writing attempts/sample references.

## Data and API contracts

- Reuse text answer policies from Phase 3. Canonical Unicode normalization is explicit; width folding and script equivalence are allowed only by that exercise's policy.
- Never globally equate small/full-size kana, strip dakuten, collapse meaningful long vowels, or accept any kanji sharing the same reading.
- Accepted alternate sentence orders or kanji/kana renderings must be authored where semantically appropriate. The expected script depends on the objective.
- Distinguish `typed_response`, `guided_trace`, `freehand_self_check`, and the accessible alternative as evidence modes.
- Typed answers can be authoritatively graded. Guided trace criteria can be checked on the backend if rewards depend on them; freehand confidence is explicitly learner-reported.
- Store character ID/content version, exercise ID, mode, assistance, completion evidence, and optional sample reference. Never trust a client `is_correct` flag.
- Self-assessed tracing/freehand activity retains an honest evidence label rather than objective correctness/mastery. It never controls access to typing, later lessons, or any other published activity.
- Apply bounds to point count, coordinate values, duration, and uploaded file types/sizes; do not accept arbitrary file paths from the client.
- Add versioned writing-task/draft/submission/checklist evidence through migrations, and explicit `/api/v1` writing resources. Use expected revision IDs for autosave/update conflicts; preserve both texts rather than silently overwriting a newer draft. Show Saved only after backend acknowledgement.
- For open writing, validate a nonempty intended submission without inferring correctness from length or imposing a language-score threshold. A committed submitted practice session earns Phase 4's uncapped session XP; self-review is optional, autosaves earn nothing, and retrying the same submission cannot duplicate XP.
- Open writing and all other published activities remain directly accessible. Self/AI feedback is advisory, never an access rule or automatic authoritative FSRS error. Objective-correctness and writing-workflow quest evidence remain distinct without restricting study.

## Later-stage writing workshop contract

For Stages C-D, extend the same feature with outline prompts, paragraph organization, model annotations, draft/revision comparison, and versioned rubric feedback. For Stages E-F add source notes/attribution, argument/counterargument review, several revision passes, and a portfolio. Every release requires reviewed tasks at its declared level, not only an editor that accepts longer text.

Persist rubric/content versions, draft/revision history, feedback provenance, and the learner's reflection. Label self-review, qualified human assessment, and optional AI suggestions distinctly. Preserve the original draft; accepting a suggested rewrite is a deliberate learner action. AI cannot be required for drafting/revision or become the authority for core progression. Without qualified review, show writing quality as self-reviewed or not assessed.

## Tests and manual verification

- [x] Test IME composition, Enter/Check behavior, paste, focus, narrow screens, and on-screen input aids.
- [x] Add positive and negative normalization tests for composed/decomposed dakuten, kana size, long vowels, width, whitespace, and accepted variants.
- [x] Test stroke coordinate scaling, undo/clear, missing assets, invalid stroke data, accessible alternative, and sample deletion.
- [x] Test honest self-report/correctness labels together with unrestricted direct access and continuation regardless of the result.
- [x] Test draft saves/recovery, IME, conflicts, idempotent submission, optional self-review, no autosave rewards, and unlimited submitted sessions with AI disabled.
- [x] Test that open-writing workflow completion remains distinct from objective writing correctness and cannot satisfy an incompatible quest/assessment predicate.
- [ ] Manually type a kana answer, convert a word to kanji, write a short constrained sentence, trace a kana, and self-check one taught kanji.
- [ ] Test pointer behavior on touch/stylus where available; record untested hardware explicitly.
- [x] Run relevant quality gates, content/asset validation, and migration checks.

## Completion gate

For the beginner release, complete when Stage A input/production tasks and at least three Stage B guided short-writing tasks work with their reviewed models, revision example, and checklist; drafts survive restart/conflict; evidence/rewards and design/keyboard checks pass; and AI-disabled practice is usable. Mark C-F work separately against its release's rubric/revision/portfolio gates; the beginner editor alone does not establish complex-essay coverage.


## Plan 9.2 follow-up — 2026-10-23

[Current execution evidence](../PLAN_09_2_VERIFICATION.md) records source 0.1.15/schema 0012, verified engineering changes and exact remaining gates. The supported fresh-install, qualified-language/stroke/audio and physical-device requirements remain open. Current improvements include verified official IME documentation, ten-topic draft guide coverage, collection-scoped saved-snapshot recall, complete timing histories and separate skill/workflow/coverage evidence. No full phase or reviewed beginner release is claimed.

## Earlier drawing receipt safety — 2026-10-25

[The three-check continuation](../PLAN_09_2_CURRICULUM.md#three-check-writinggrammar-extension--2026-10-25) separates confirmation of an earlier saved drawing from the current grid's result. A prior optional sample can no longer remove the current unsaved-grid warning. Character-scoped receipt recovery preserves other confirmations; a regression and real installed-browser flow prove current strokes survive confirmation and a canceled character switch, receipt lookup adds no XP, and a new current-grid commit earns5XP once per request. Frontend lint/typecheck/42 tests/build pass on installed Node24.21.0. Qualified stroke review, physical IME/touch/stylus and the full phase gate remain open; no checkbox is closed from scripted pointer evidence alone.
