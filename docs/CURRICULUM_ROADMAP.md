# Japanese Curriculum — Beginner Through Complex Essays

Status: A first technical practice slice and content APIs are implemented; full A-B coverage and C-F remain planned. Independent qualified Japanese review is still pending. See [verification](PHASE_01_03_VERIFICATION.md) for actual inventory and limits.

This is the long-term learning scope approved by the user. It complements the [eleven implementation phases](../AI_IMPLEMENTATION_PLAN.md); the learning stages below are not additional implementation phases. Each content release reuses the same generic engine and undergoes the relevant phase gates.

## Release boundaries

- First personal release: Stages A-B, including the ten beginner units in [Phase 3](plans/PHASE_03_CURRICULUM.md), basic Japanese production, short guided paragraphs, and everyday conversation.
- Intermediate releases: Stages C-D, adding connected writing, summaries, opinions, longer reading, and a draft/revision workshop.
- Advanced releases: Stages E-F, adding extended and complex essays, source synthesis, argument, register, sustained discussion, and independently reviewed writing evidence.

Later stages are approved roadmap scope, not a claim that their content is authored or available in the first release. Never label an advanced stage complete because its editor or AI prompt exists. There is no fluency deadline or exam-pass promise.

## Stages A-B — Substantial starter inventory

The user wants a substantial amount of material from the beginning. Use these ambitious authoring targets for learning stages 1-2 (A-B), not software Phases 1-2:

- Stage A: all 46 basic hiragana and 46 basic katakana, common voiced/small-kana/combination patterns, 100 distinct kanji taught in useful words, and 500 unique core vocabulary entries.
- Stage B: add 200 new kanji and 1,500 new core vocabulary entries while revisiting Stage A material in sentences, messages, stories, and conversation.
- Cumulative A-B target: 92 basic kana plus their taught variants/combinations, 300 distinct kanji, and 2,000 unique core vocabulary entries. These cumulative totals include Stage A.

The basic kana count follows the [Japan Foundation's kana chart guidance](https://classroomresources.sydney.jpf.go.jp/resources/hiragana-katakana-game/). The kanji/vocabulary numbers are Trilingo's proposed content targets, not official JLPT requirements, a language-proficiency claim, or content already authored.

Counting and learning rules:

- Count stable lexical entries once across stages. Inflections, alternate spellings, duplicate examples, kana/kanji renderings of the same word, and repeated review cards do not inflate the vocabulary total. Useful fixed phrases can be taught but are reported separately from the 2,000 core word entries.
- Count distinct kanji once, with contextual word readings; do not count every reading as another character or imply that learning one word teaches every reading. Reading, typed production, and handwriting evidence remain separate.
- These are published content-inventory targets, not a requirement to memorize 500 words before starting Stage B or speaking. Introduce useful language from the first lessons and let practice/evidence determine recall needs.
- Offer an editable convenience batch with an initial suggestion of ten new words, freely expandable to more/all, plus optional due review/contextual practice. The ten topic headings expand into lessons/subunits; they do not impose a daily quota or force a batch size.
- Record actual published, introduced, reviewed, and assessed-recall counts separately. The first playable technical slice can launch with a partial inventory, clearly labeled; full A-B content coverage requires an audited 2,000-word/300-kanji inventory and the other stage gates.
- All published stages/units/items are available directly. The 500/2,000-word targets, suggested order, daily batches, review dates, essay prompt lengths, and assessment scores are not access requirements or maximum study amounts; freely request more, skip, reveal, retry, or jump ahead.
- Every core entry needs a reviewed reading/meaning, part of speech, concept/stage links, and original example/use context, with audio and response directions provided through the corresponding features. Do not bulk-publish unreviewed AI filler to hit the counts.

## Stage A — Script, sounds, and first sentences

Read hiragana/katakana, recognize the first taught kanji in useful words, and understand simple labels and sentences. Type Japanese with IME, practice character formation, and produce an introduction or basic request. Listen to reviewed short phrases and practice saying them with honest transcript feedback.

Publish suggested preparation, scripts/readings, original examples, accepted variants, and optional objective checks. Recognition does not establish handwriting/speaking skill, but every published activity remains accessible regardless of the result.

## Stage B — Everyday messages and guided paragraphs

Read notices, menus, short stories, and simple exchanges. Write messages, a short self-introduction, a routine, or a description using roughly three to five connected sentences. Speak through common situations and short supported descriptions.

Teach sentence linking, time/order, basic reasons, and consistent politeness within the taught grammar. Provide at least three reviewed guided writing tasks, model responses with alternatives, a simple annotated revision example, and a self-review checklist in the first release. These are beginner content aids; the fuller revision-comparison/rubric workshop UI arrives in C-D. Treat free writing as practice; reserve correct/incorrect grades for constrained authored checks.

## Stage C — Connected paragraphs and narratives

Read longer graded stories and practical explanatory texts. Write descriptions, diary narratives, email-style messages, and short summaries. Practice chronological order, reference between sentences, connective choices, and a consistent viewpoint. Tell a short event in speech and answer follow-up questions.

An initial writing target may be 150-400 Japanese characters, adjusted to the task. Introduce a draft -> feedback -> revision cycle, a portfolio, and a simple rubric for meaning, language, organization, and register. Distinguish the learner's original text from any suggested rewrite.

## Stage D — Opinions and multi-paragraph arguments

Read contrasting viewpoints and identify claims/reasons. Write an opinion, comparison, recommendation, or problem/solution piece with an introduction, supporting reasons/examples, and a conclusion. Practice disagreement and clarification in conversation.

An initial writing target may be 400-800 Japanese characters. Teach paragraph purpose, evidence versus assertion, transitions, summary versus opinion, and basic counterarguments. Feedback must point to a particular passage and explain a revision rather than only returning a score.

## Stage E — Extended essays and formal register

Read longer expository and argumentative texts with less reading assistance. Plan and write an extended essay, using a clear position, organized sections, evidence, a counterargument, and consistent register. Summarize the argument aloud and respond to questions.

An initial writing target may be 800-1,600 Japanese characters. Teach scope, qualification, paraphrase, source attribution, formal/plain-style consistency, and revision for cohesion. Sources must be real, accessible, and licensed/linked appropriately; generated references are not evidence.

## Stage F — Complex essays and synthesis

Read and compare several substantial sources, track assumptions, distinguish fact from interpretation, and evaluate competing arguments. Write an essay that synthesizes sources, handles counterarguments and limitations, and fits its intended audience. Defend and refine the argument in sustained discussion.

An initial writing target may be 1,600-3,000 Japanese characters, with longer projects allowed. Practice multiple revisions: outline, first draft, argument review, language/register review, final draft, and a brief reflection on changes. Retain a portfolio with feedback provenance and revision history.

Character ranges in Stages C-F are proposed prompt defaults, not official proficiency thresholds, automatic pass rules, or evidence of quality. A concise well-argued response can be stronger than a longer one. These stages do not claim coverage of every academic discipline or university writing genre.

## Writing workshop and feedback contract

- [ ] Extend [Phase 6](plans/PHASE_06_WRITING.md) incrementally: basic draft saving in the beginner release; outline/editor/revision comparison/rubric feedback for intermediate releases; source notes and complex-essay portfolios for advanced releases.
- [ ] Persist prompts, content/rubric versions, original drafts, revisions, submission events, feedback source, and learner reflection in SQLite through migrations. Show Saved only after backend acknowledgement and preserve text through refresh/retry/conflict.
- [ ] Use a rubric covering task/meaning, vocabulary/grammar, script/orthography, organization/cohesion, register/audience, and evidence/source use where relevant. Each band needs reviewed descriptors and examples; do not turn character count into a language grade.
- [ ] Keep constrained exercise grading authoritative and deterministic. Open essays have many valid answers and cannot use exact-string translation grading.
- [ ] Label self-review, human feedback, and optional AI suggestions distinctly. AI is advisory, cannot award correctness or control access, and cannot overwrite a draft without an explicit accept/edit action.
- [ ] Allow drafting, reading model texts, self-review, and revision with AI disabled. If no qualified reviewer is available, show the work as self-reviewed or unassessed rather than certified advanced writing.
- [ ] A deliberately submitted writing practice session can earn the uncapped session reward with self-review optional. Autosaves/word counts/AI scores do not establish correctness/mastery; evidence stays separate from activity rewards and never controls access.
- [ ] Keep all published writing practice available after mistakes, skips, or uncertain feedback. Create FSRS error links only from validated authored concepts, never an unverified AI allegation.

## Stage publication and learner evidence

For every newly published stage:

- [ ] Record can-do outcomes, advisory preparation, grammar/vocabulary/kanji coverage, reading/listening materials, writing genres, and speaking tasks in a versioned inventory.
- [ ] Audit the A-B lexical/kanji targets and counting rules above when claiming the full starter release; report partial published coverage honestly and keep introduced/recalled counts distinct.
- [ ] For Stage A, supply reviewed character/word/first-sentence production tasks with objective answer policies or honest handwriting references; an essay rubric is not required. For Stage B, supply at least three guided composition tasks, reviewed models/alternatives, a simple annotated revision example, and a self-review checklist. These A-B content aids do not require the later workshop UI.
- [ ] For each Stage C-F, supply at least three distinct original writing tasks at that level, reviewed models/alternatives, a revision example, and explicit rubrics with the stage's workshop support. This is a pilot minimum, not enough evidence to advertise comprehensive proficiency coverage.
- [ ] Provide reading/listening/speaking instruction and suggested preparation at matching difficulty, while allowing direct selection of any published activity.
- [ ] Have Japanese content, register, and rubric examples reviewed by a qualified Japanese-language reviewer; keep unreviewed material draft or clearly labeled practice.
- [ ] Verify drafts/revisions, backup/restore, API validation, accessibility, and provider-disabled practice using the phase gates for that release.
- [ ] Track authored-content coverage, objective exercise results, completed writing workflows, and reviewed writing quality separately. Stage availability/completion is not a language certificate.
- [ ] Keep actual learner work and the reviewer/rubric provenance for any advanced writing claim. A qualified reviewer can assess quality; without that evidence, show self-review or not assessed and still allow personal practice.

## Exam and proficiency labels

JLPT-oriented vocabulary/grammar/reading/listening tags may be added only against a documented coverage audit. Do not label a completed N-level tag as proof of essay or speaking ability: the [official JLPT FAQ](https://www.jlpt.jp/e/faq/index.html) explains that its tested skills do not include speaking/writing production. These six learning stages are Trilingo's planning structure, not an official JLPT/CEFR equivalence.

## Phase ownership

- Phase 3: inventories, suggested preparation, schemas, versions, publication/reviewer records.
- Phase 5: reading progression from graded passages to argument/source comparison.
- Phase 6: typed production, draft storage, writing workshop, revisions, rubric/portfolio evidence.
- Phase 7: language/paragraph/rhetorical instruction, authored feedback, optional explanations.
- Phase 8: level-appropriate listening, reading aloud, discussion, and existing Kokoro/local provider adapters.
- Phase 9: review of validated concepts and honest skill/activity evidence.
- Phase 10: each release's scope audit, backup/restore, quality gates, and published limitations.
- Phase 11: open-source GitHub publication and launch communications; campaign claims must match the audited release and its reviewed/draft content scope.
