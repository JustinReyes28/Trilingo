# Phase 07 — Grammar and Practical Dialogues

Status: Partial engineering implementation (2026-10-23); qualified content and/or real-provider gates remain open. Depends on: [Phase 06](PHASE_06_WRITING.md). Next: [Phase 08](PHASE_08_AUDIO_SPEAKING.md).

## Goal

Add the requested Babbel-style depth: explain patterns, practice them in context, and use them in everyday exchanges rather than relying on isolated translation drills.

## Deliverables

- [ ] Add authored unit guides with short English grammar notes, Japanese examples, contextual readings, common mistakes, register, and cultural usage notes.
- [ ] Add a searchable grammar reference with links from mistakes and examples to targeted practice; browsing a guide does not mark its skill mastered.
- [x] Teach は/が/を/に/で/へ through explicit, scoped objectives instead of declaring them freely interchangeable.
- [ ] Cover the beginner unit topics from Phase 3 using only grammar already introduced or deliberately scaffolded.
- [x] Add dialogue-completion, response-selection, and constrained roleplay types through shared schemas/renderer and server-owned grading.
- [x] Build original situations: meeting someone, ordering food, a small purchase, asking directions, talking about routines, and making a simple invitation.
- [x] Use authored branching turns with task goals, multiple valid response variants, optional hints, replay, and a text-first fallback.
- [ ] Show politeness/register expectations and distinguish a valid alternative from an answer that is understandable but outside the taught task.
- [x] Add unit recaps, review links, bookmarked words/grammar, and personal vocabulary collections built from learned content.
- [x] Store learner interests and preferred practice focus as settings that select existing content without making arbitrary provider-generated lessons authoritative.
- [ ] Publish the remaining beginner units only after linguistic/content validation. Maintain a reviewed inventory and identify any unfinished content.
- [x] Add an optional explanation provider interface with disabled and OpenAI-compatible adapters, including configurable LM Studio support.
- [x] Add optional AI scenario practice only after deterministic authored dialogues work; clearly label generated material and uncertain feedback.
- [ ] Add answer-specific authored "why this works" and "why that answer differs" explanations, with optional local AI elaboration and voice roleplay built on the same scenario context in Phase 8.

## Intended implementation areas

Grammar/library/dialogue features, authored grammar/scenario content, backend dialogue services, `backend/app/ai`, provider configuration, and migrations for scenario attempts/bookmarks/collections if needed.

## Data and API contracts

- Grammar notes are structured content linked to concepts and lessons, with original text and versioned examples.
- A scenario stores roles, permitted transitions, objective checkpoints, response policy, hints, explanation, and optional audio cues.
- Backend validates each dialogue transition and objective completion. Answer selection uses stable IDs; free-text acceptance uses explicit variants/strategies.
- Text participation is sufficient for the core authored scenario. Phase 8 adds listening and recorded responses without changing its core state machine.
- An explanation request references an exercise/attempt and bounded context; backend retrieves the authoritative answer rather than trusting a client-provided answer key.
- Provider settings contain enabled/provider/base URL/model/timeout. Keep credentials server-side, validate structured responses, limit input size, and time out cleanly.
- Optional AI never grades core exercises, awards XP, controls lesson access, modifies FSRS state, or silently publishes generated content. Guides/hints and every published dialogue are freely available; responses can be retried/revealed/skipped without blocking continuation.
- On disabled/unavailable/malformed provider responses, show the authored explanation and continue learning. Do not fake a successful model response.

## Tests and manual verification

- [ ] Test accepted/rejected dialogue transitions, response alternatives, task completion, hints, resume, and duplicate submissions.
- [ ] Test guide/bookmark/collection persistence and references after a content revision.
- [ ] Test grammar search/filter behavior, direct links from mistakes to the correct concept, and authored explanation fallback without AI.
- [ ] Validate all published unit exercises and review grammar/register consistency with the content checklist.
- [ ] Test AI disabled, endpoint unreachable, timeout, no model loaded, malformed response, configuration swap, and authored fallback.
- [ ] Test that model text cannot be used to mutate authoritative progression or inject executable HTML.
- [ ] Manually complete three practical authored scenarios with AI entirely disabled; revisit the grammar explanations and resume an interrupted dialogue.
- [ ] When a real provider is available, verify one real explanation call; otherwise record integration as unverified rather than claiming local success.
- [ ] Run relevant frontend/backend gates, content validation, and migrations.

## Completion gate

Complete when authored grammar and practical dialogues work without AI, reviewed content supports the intended beginner situations, and the optional provider layer fails safely. Real-provider verification is tracked separately from mock/contract tests; it must not be implied by them.

## Later-stage language and essay instruction

For Stages C-F in the [curriculum roadmap](../CURRICULUM_ROADMAP.md), add reviewed instruction for connected narration, paragraph cohesion, viewpoint/register, claims and evidence, qualification, counterargument, paraphrase, source attribution, and revision. Link feedback to the specific draft passage and taught concept; supply annotated original models and alternatives. Keep these authored materials usable without AI. AI elaboration is advisory and cannot become an automatic open-essay grade or rewrite the learner's original submission.

## Reference basis

This phase adapts contextual grammar and everyday dialogues from the broad approach in [Babbel's course overview](https://support.babbel.com/hc/en-gb/articles/205600448-Babbel-courses), [Grammar Guide](https://support.babbel.com/hc/en-us/articles/19260489559058-Grammar-guide), and [Guided Conversations](https://support.babbel.com/hc/en-gb/articles/19188554247186-Guided-Conversations), alongside the requested Duolingo-style explanation/roleplay ideas. It does not import either product's lessons or claim that Babbel provides this Japanese curriculum. Sources were reviewed on 2026-10-22 and should be checked again when implementing provider-specific capabilities.

## Bounded implementation evidence — 2026-10-23

Checked deliverables refer to the implemented technical/draft slice and tested adapter/control contracts, not full beginner publication or real-provider success. [Verification and remaining work](../PHASE_07_09_VERIFICATION.md) records exact scope, commands, responsive evidence, migrations and limitations. All unchecked tests and the full completion gate remain open; no bulk completion is claimed.

Additional-hour scope: six scoped particle checks link from their draft guides, with authored choice-specific contrast feedback. Optional scenario coaching now uses bounded structured output and authored disabled/failure fallback. These are technical draft capabilities; full unit coverage, qualified publication and real provider/voice verification remain open. See [follow-up evidence](../PHASE_07_09_FOLLOWUP.md).


## Plan 9.2 follow-up — 2026-10-23

[Current execution evidence](../PLAN_09_2_VERIFICATION.md) records source 0.1.15/schema 0012, verified engineering changes and exact remaining gates. The supported fresh-install, qualified-language/stroke/audio and physical-device requirements remain open. Current improvements include verified official IME documentation, ten-topic draft guide coverage, collection-scoped saved-snapshot recall, complete timing histories and separate skill/workflow/coverage evidence. No full phase or reviewed beginner release is claimed.

## Bounded curriculum continuation — 2026-10-24

[Plan 9.2 curriculum evidence](../PLAN_09_2_CURRICULUM.md) records source **0.1.20**: 112 additional draft lessons, 1,363 checks and 833 vocabulary records across the ten topics, using the existing reading/grammar/session engine. The provisional lexical inventory is **541 Stage A +566 additional Stage B**; **934 Stage B words**, qualified semantic/language review and applicable publication/provider/device gates remain open. Published lesson and vocabulary definitions are unchanged. Meaning/typed-reading evidence and draft practice are not reviewed proficiency or full beginner completion. No new checkbox is closed by the raw authoring count.

## Grammar view recovery — 2026-10-25

[The current continuation](../PLAN_09_2_CURRICULUM.md#three-check-writinggrammar-extension--2026-10-25) binds guides/bookmarks to the selected course and draft visibility, removes stale study controls during loading/failure and adds keyboard-accessible reload. The installed-browser flow verifies search/unit filtering, bookmark persistence, targeted practice with correct/explicitly skipped evidence and duplicate finish preservation. Three authored scenarios finish with their checkpoint graded correctly and authored alternatives accepted; one pauses/resumes, all with AI disabled. These frontend/workflow results preserve qualified content/publication and actual provider gates; existing checkboxes remain unchanged.
