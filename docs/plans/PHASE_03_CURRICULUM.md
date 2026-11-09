# Phase 03 — Japanese Curriculum and Content Model

Status: Technical starter slice implemented; qualified language review remains open. Depends on: [Phase 02](PHASE_02_INTERFACE.md). Next: [Phase 04](PHASE_04_LESSON_ENGINE.md).

## Goal

Establish original, validated Japanese course content that can power reading, writing, listening, and speaking without coupling the engine to Japanese.

## Curriculum scope

The first published course starts at absolute beginner level. Use these ten learning units as a content roadmap, separate from the eleven implementation phases:

1. First sounds and greetings: initial hiragana, mora awareness, introductions.
2. Hiragana foundations: remaining base characters, voiced sounds, combinations, long vowels, small っ.
3. Katakana and familiar words: the base set, combinations, loanwords, long-vowel mark.
4. People and things: names, pronouns when appropriate, は, です, questions, demonstratives.
5. Numbers, time, and simple purchases: dates/times in context and selected counters with explicitly taught readings.
6. Food and ordering: を, requests, polite verbs, common menu words.
7. Places and directions: に/で/へ in taught contexts, location words, asking where something is.
8. Daily routines: present/past and negative polite forms, activities, schedules.
9. Descriptions and preferences: introductory adjectives, likes, simple comparisons where taught.
10. Everyday connections: invitations, short messages, integrated reading/writing/dialogue tasks and recap.

Interleave kanji in useful words once the needed kana/reading support exists. These ten units form the first-release Stages A-B in the [beginner-to-complex-essay roadmap](../CURRICULUM_ROADMAP.md), not the entire long-term course or complete official JLPT coverage. Later Stages C-F add connected writing, opinions, and extended/complex essays with corresponding language/reading/speaking content.

The full starter inventory targets 500 unique words/100 kanji in Stage A, then 1,500 new words/200 new kanji in Stage B: 2,000 words and 300 kanji cumulatively, alongside 92 basic kana and taught variants. These are authoring targets, not already available content or compulsory memorization gates. Expand the ten topic outlines into sufficient lessons/subunits; the small initial seed slice remains an engine proof, not the whole course.

## Deliverables

- [x] Define language/course/unit/lesson/concept/vocabulary/exercise models with stable IDs, suggested preparation/order, and content versions. Preparation metadata never controls published-content access.
- [x] Add generic stage/release/can-do/genre/rubric metadata and review/publication status as needed. Japanese stages belong in content configuration, not language-specific branches in the learning engine.
- [x] Add migrations and validated, idempotent import/seed tooling; never overwrite user attempts when importing a new content version.
- [x] Define frontend Zod and backend Pydantic discriminated exercise unions with shared/generated contracts where practical.
- [x] Implement at least multiple choice, translation, fill blank, sentence ordering, and matching schemas. Add later types only with the corresponding renderer/service.
- [x] Keep answer keys out of ordinary unassisted-question responses, with an explicit freely available Reveal/Hint action. Record assistance honestly; revealing the answer never blocks continuation.
- [x] Model vocabulary surface form, contextual reading, gloss, part of speech, register, example, concepts, and optional audio reference.
- [x] Audit unique lexical IDs and kanji across stages against the 500+1,500-word and 100+200-kanji targets. Do not inflate totals with conjugations, spelling variants, repeated cards, or separate phrase counts; report actual publication/learning evidence independently.
- [x] Model rich Japanese text as authored segments with surface/reading data for furigana; do not guess all kanji readings at render time.
- [x] Model character/stroke assets, reading passages, grammar notes, dialogue turns, audio references, skill tags, and accepted variants as content grows.
- [x] Model optional recap/placement/mastery banks with concept coverage, scoring/badge criteria, and stable IDs. Results recommend practice and record evidence; no pass criterion or prior completion controls access.
- [ ] Model original story turns/checkpoints and mini audio-episode scripts with taught vocabulary/grammar, difficulty, reviewed transcript, comprehension objectives, and an optional recap task.
- [x] Add per-exercise answer policy: target script, required distinctions, allowed variants, punctuation/spacing treatment, hint policy, and grading strategy.
- [x] Publish a first slice of at least two units, three lessons per unit, and five meaningful exercises per lesson across at least three supported types; use four core types as they become executable in Phase 4.
- [x] Record objective, validated answer, accepted alternates, explanation, concepts, difficulty, and suggested preparation. Skipping ahead remains available.
- [x] Author the remaining unit outlines now; publish their exercises only after linguistic review and corresponding feature support.
- [ ] Include Stage A character/word/first-sentence tasks and at least three Stage B guided-writing prompts with reviewed models/alternatives, one simple annotated revision example, and self-review checklists; distinguish constrained answers from open composition.
- [x] Add content status (draft/reviewed/published), source/asset license records, and a validation command. Imported content never silently becomes published.

## Intended implementation areas

`content/courses/ja`, `content/seeds`, `backend/app/{models, schemas, services, repositories}`, `backend/migrations`, `frontend/src/schemas`, and content tests. Lesson page components consume content APIs.

## Data and API contracts

- Add `/api/v1/courses`, course detail, enrollment, course map, lesson metadata, and library read APIs.
- Map nodes expose suggested order/preparation, published availability, and honest study/assessment evidence. All published nodes are startable; unpublished material is labeled as unavailable content rather than an earned lock.
- Store Japanese normalization/grading policies in content configuration and named strategies. Generic grading dispatches by validated type/strategy.
- Distinguish script recognition, contextual kanji reading, meaning, typed production, guided handwriting, listening, and speaking evidence.
- Distinguish published curriculum coverage, objective correctness, writing workflow completion, self-review, human rubric evidence, and optional AI suggestions. Longer text or an exam-oriented content tag does not establish essay proficiency.
- Content revisions preserve historical attempt references; archive removed material or snapshot what was attempted.
- Lesson metadata distinguishes study, voluntary recaps, and optional placement/mastery. Assessment results never grant/revoke access and do not impersonate studied completion.
- Story/dialogue transcripts are structured authored content. A listening checkpoint exposes its transcript only according to the explicit reveal policy, not through an unprotected answer field.
- Reject missing IDs, broken preparation/concept references, invalid suggested order, answerless objective prompts, ambiguous choices, and missing licenses/assets. These content-quality checks do not impose learner prerequisites.

## Tests and manual verification

- [x] Empty DB import succeeds; a second import does not duplicate or reset data.
- [x] Invalid content/preparation references fail with actionable locations, while a new learner can directly start all valid published material.
- [x] Ordinary question responses protect unassisted answers, deliberate reveal returns the supported explanation/answer, and the resulting assistance never prevents continuation.
- [x] Content update tests preserve existing attempts and completion records.
- [x] Load course/unit/lesson metadata entirely from SQLite-backed APIs and confirm no production lesson array lives in React components.
- [ ] Review Japanese for naturalness, correct readings, clear register, and alternatives; do not use unreviewed model output as an answer key.
- [x] Run content validation plus relevant frontend/backend gates and clean DB migration checks.

## Completion gate

For the initial phase, complete when the first published beginner slice validates, imports repeatably, and is accessible through APIs with protected answer keys, while stage metadata and later scope are explicit. Remaining beginner units and later Stages C-F stay draft until their own reviewed content/release gates pass; a syllabus outline alone is not a finished course.


## Implementation evidence — 2026-10-23

See [content authoring](../CONTENT_AUTHORING.md) and [verification](../PHASE_01_03_VERIFICATION.md). The technical slice has two published units, six lessons and thirty exercise definitions; eight core words and five expressions are counted separately. Schemas cover all five core types, rich text, later character/grammar/narrative/assessment content, staged writing, assets and publication metadata. Current-machine import/API/assistance/history tests pass.

Language checks were internal. Independent qualified review of answer keys, transcripts and writing models remains unverified, so the overall phase gate stays open and content is labeled technical practice. One draft story and two script-only audio episodes demonstrate narrative contracts; no audio or assessed listening exists. Stage A now includes character/word/first-sentence references, alongside three Stage B writing tasks with models/checklists and a revision example. The [qualified-review packet](../JAPANESE_CONTENT_REVIEW.md) includes all source keys, models and scripts for version 0.1.5. The user confirmed that no reviewer is available; retain draft/practice labels and leave the review-dependent checkboxes open. Real audio delivery belongs to Phase 8. Existing assistance/enrollment/snapshots survive updates; Phase 4 now tests preservation of actual lesson attempts/completion and verifies pre-update completed sessions after a real QA process restart. No advanced stage or full beginner inventory is claimed.

## Bounded curriculum continuation — 2026-10-24

[Plan 9.2 curriculum evidence](../PLAN_09_2_CURRICULUM.md) records source **0.1.20**: 112 additional draft lessons, 1,363 checks and 833 vocabulary records across the ten topics, using the existing reading/grammar/session engine. The provisional lexical inventory is **541 Stage A +566 additional Stage B**; **934 Stage B words**, qualified semantic/language review and applicable publication/provider/device gates remain open. Published lesson and vocabulary definitions are unchanged. Meaning/typed-reading evidence and draft practice are not reviewed proficiency or full beginner completion. No new checkbox is closed by the raw authoring count.
