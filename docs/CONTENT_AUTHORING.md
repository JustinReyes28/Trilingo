# Course content and publication

The course graph lives in content/courses/ja/starter.json and is imported into versioned SQLite storage. React consumes public APIs rather than embedding a production lesson array. Inspect app/content_schema.py and app/content_extensions.py for exact Pydantic contracts. Frontend public exercise/map/library contracts are in frontend/src/schemas.ts.

## Core structure
Course -> stages/concepts/vocabulary/units -> lessons -> exercises. Stable IDs are unique across core entities. Each lesson has an objective, advisory order/preparation, status and exercises. Each exercise has objective, difficulty, concept/skill links, a grading policy, validated private answers, hint and explanation. The shared discriminated union has twelve types: the original five objective types, response_selection, dialogue_completion, constrained_roleplay, listening_selection, dictation, audio_contrast and speaking. Speaking records attempts/transcripts or unassessed typed practice; it never produces an objective pronunciation grade.

Stage/release/can-do and writing genre/rubric-version metadata are content, not language branches in core services. Stages A-B target the beginner release; C-F are planned later releases. Current draft writing metadata includes Stage A character, word and first-sentence tasks, plus three Stage B guided compositions with models/alternatives, a revision example and self-review checklists. Two draft mini audio episodes contain scripts and text-exercise references for later adaptation; no audio assets or assessed listening are claimed.

Character/stroke assets, grammar notes, passages/stories/dialogues/audio-script turns and optional recap/placement/mastery banks also have validated contracts. Initial examples remain draft while their renderers/instruction are developed. Narrative Japanese text uses authored surface/reading segments; no guessed readings or arbitrary source HTML. Missing/broken transitions, concepts, vocabulary, checkpoints, stage IDs and asset-license references fail validation. Declared asset files must exist inside their content directory.

## Counting and review
Report core lexical words and useful fixed expressions separately. Current published technical slice: 8 word records, 5 expressions and 0 contextual kanji. Source 0.1.21 has 2,169 word records (2,167 provisional lexical identities: 541 Stage A +1,626 additional Stage B), 15 expressions and 300 draft contextual kanji. Both separate word-authoring targets are exceeded; semantic corrections may change counts. Inflections, variants, repeated cards and alternate kana/kanji spellings do not create additional lexical words. Exact duplicate surface/reading/part-of-speech entries are rejected; semantic deduplication still requires qualified review. Character coverage and typed/handwritten/listening/speaking evidence remain distinct.

All supplied text is original and attributed under the course's CC-BY-4.0 content license record. OS fonts and installed library code are not redistributed as authored course assets. No Duolingo/Babbel text/art/audio is imported.

The first30 exercises were internally checked for answer consistency, kana size/voicing, conventional spelling, polite forms, prompt ambiguity, repeated token IDs and authored alternatives. Independent qualified Japanese-language review remains pending. [The review packet](JAPANESE_CONTENT_REVIEW.md) assembles exact source 0.1.21, answer keys, models and scripts with its source hash and 6,848 pending items. No reviewer is available; keep additions draft and existing material labeled practice. Neither published status nor browsing constitutes proficiency certification. Full-stage publication and advanced rubric claims still require qualified review.

## Additive Stage B authoring — source 0.1.21

`scripts/author_stage_b.py` applies the [source-bound manifest](../content/authoring/ja/stage-b-expansion-20261025.json) to the exact archived 0.1.20 snapshot. It never opens a database and refuses a changed base hash, backwards version or conflicting output/report. It preserves original definitions, appends only draft lessons/words/checks, and binds lexical decisions and input/output hashes to the new source. The older beginner builder remains specific to its archived 0.1.16 base and must not be used to overwrite later changes.

Three original authoring files contain 1,100 candidate rows. Conservative spelling/kana-width/reading and noun/する-family selection accepts 1,060 and reports 40 omissions in [the immutable result](../content/authoring/ja/stage-b-expansion-20261025-result.json). A same-reading omission means a semantic decision is needed, not that the words were merged or proved identical. Genuine homophones may be restored in a later reviewed/versioned batch. No saved IDs/cards are merged. Japanese text corruption/non-kana readings fail validation; all generated keys must pass the authoritative grader before output. Loanword compounds retaining ー use an exact Japanese-script key and an explicit kana prompt, leaving global hiragana-only grading unchanged.

The same manifest appends 24 original particle contrasts to six draft guides, each with contextual feedback for all three choices. Valid alternative meanings are distinguished from the specified teaching objective. All contrasts remain draft and require deliberate draft preview; keys stay private until assistance or committed feedback. The [current execution evidence](PLAN_09_2_CURRICULUM.md#execution-continuation--2026-10-25) records preservation, grading and isolated UI checks.

## Safe updates
From backend/ run python -m app.cli validate before python -m app.cli import (using .venv's Python). An optional JSON path can be passed after either command. Validation rejects duplicate IDs/lexical entries, invalid suggested order/cycles, broken references, incomplete objective answers, invalid matching/token maps, missing licenses and unsafe/missing asset paths.

Content versions are immutable. Bump the semantic version for any imported content change. Re-importing identical content is a no-op; a changed existing version returns an actionable conflict. New revisions preserve prior payloads and assistance references. No progress reset is part of import.

Public lesson responses omit private keys/hints/explanations. POST the explicit assistance resource with a new UUID event_id and action hint/reveal to request them deliberately. An identical retry returns the same result; reusing that ID for another action conflicts. Assistance is durable, honest and never controls published access.

Assessment criteria describe results rather than access rules. Open writing models/checklists are not exact-string answer keys or an AI grading policy. Keep optional AI generation draft until validated; AI cannot publish content, grade core answers or award progression.


## Phase 5–6 draft execution

Reading/story sessions, related character/saved-item drills and constrained writing now use the shared authoritative engine. Open compositions save immutable revisions/conflicts and remain not assessed or self-reviewed. Formation records guided_trace/freehand_self_check/accessible_sequence separately; no recognition or mastery is inferred. All 527 character entries, seven writing references and six original stroke templates remain draft. The source has 481 standalone drills in addition to the unchanged 30 published lesson definitions. Asset hashes/version/license are validated; qualified language/stroke review is still pending. See PHASE_06_VERIFICATION.md for exact commands and limits.


## Contextual kanji inventory — source 0.1.11

The original draft authoring rows are in content/authoring/ja/kanji-contexts-draft.json. They add 282 distinct target characters to the prior 18, producing 100 Stage A and 200 additional Stage B kanji. A character is taught inside an explicit whole word, with its reading, meaning, original example and related reading check; this does not imply every on/kun reading or handwriting ability. Shared compounds reuse a stable vocabulary entry/check. 家 uses the existing ja-word-house ID; its canonical kana spelling is retained.

The new rows produce 262 new vocabulary records and 263 reading checks. Source totals are 527 character records, 481 standalone practice definitions, 286 word records and 5 expressions. These are record counts, not reviewed unique lexical coverage: the older 学校/がっこう alias records still represent one word and require semantic deduplication during content review. Published coverage stays 8 core words/5 expressions/6 lessons/30 exercises, and all new material stays draft. The complete 300-kanji authoring count does not close review/publication or the 2,000-word curriculum gate.

## Grammar and listening contracts — source 0.1.14

Grammar notes may link validated unit IDs and practice exercise IDs and include scoped common mistakes and cultural/register notes. Six particle guides now link authored checks; explanations distinguish the chosen distractor from the taught answer. All seven guides and six dialogue situations remain draft. Full unit instruction and qualified review are still open.

The shared exercise union now also accepts listening_selection, dictation and audio_contrast (eleven types in total; the published starter still uses its original five). Audio cues have stable local IDs, labels, private transcripts, language and optional provider-only pronunciation overrides. Selection/dictation use one cue; a contrast uses two to four unique cues. All use listening evidence. Public exercise payloads include only cue IDs/labels, never transcripts/overrides/answers or response-specific feedback.

Text assistance deliberately reveals transcripts and persists assisted/fallback evidence. Answering without every required cue delivered also records assistance; no fallback blocks an answer, retry, continuation, skip, finish or normal practice XP. Preparing a reference is not proof of hearing it. Raw microphone recordings are never added to course content or audio-delivery receipts.

Author pronunciation overrides individually after contextual review; displayed Japanese/transcripts remain unchanged. Cache identity includes source text, override, language, engine/model/voice configuration and speed. A new text/override/engine version creates a new cache entry. The Japanese adapter rejects unsupported languages/voices; never infer correct Japanese teaching audio from a decodable WAV. The two audio episodes and three listening checks remain unreviewed drafts.


## Source-bound inventory and review packets

From backend/, run python -m app.content_audit --output ../docs/reviews/ja-starter-0.1.20. The lexical-identities.json file beside the source binds explicit alias/distinct-homophone decisions to its exact version/hash. Unlisted IDs remain distinct; same reading alone is not an identity rule. The inventory labels inferred concept-overlap placement separately from explicit unit links and reports provisional counts without independent approval.

The packet copies the exact source and assets, records their hashes, and creates a pending decision queue. It is self-contained and validates with the existing loader. Regeneration refuses to overwrite amended review artifacts; preserve them and use a new output folder. Changes to published source still require a new semantic content version and qualified publication checks. These authoring identities do not merge cards, attempts, collections or saved history; no database migration is involved in the lexical audit itself.

## Speaking contracts — source 0.1.16

Narratives may link speaking_exercise_ids to validated speaking prompts. Each has an objective, concepts, difficulty, explanation/hint and one or two unique audio cues. The first cue is the model response used for transcript comparison; an optional second cue voices the authored partner prompt. Public speaking payloads deliberately expose reference_text for shadowing, while provider pronunciation overrides stay private. Do not use speaking models as objective answer keys or add them to an assessment expecting a pronunciation score.

Six draft dialogues and two draft episodes link sixteen draft prompts. Source totals are 512 standalone drills; published lessons/words/expressions remain unchanged. The exact 0.1.16 packet contains 1,472 pending review items. Speaking and generated-reference teaching quality still require qualified review and real-provider checks.

Saved speech requires an explicit bounded WAV submission, the session's current action ID/revision and a successful local STT response. Its receipt stores a media digest, not audio. Retries return the original receipt. Transcript matches, speech attempts and typed fallbacks remain separate from objective checks and self-rated FSRS logs. Migration 0013 versions these additive JSON fields; old history/receipts are preserved and readers supply zero/null defaults.

Review directions remain deliberate: published words support meaning, reading and typing; a published exercise supports its authored skill. Speaking exercise recall reveals its authored model and remains self-rated. Draft speaking sessions do not silently create cards, change schedules or promote publication. Published saved words and collections now also support listening and speaking self-rated directions. Their audio/transcript requests use the saved card snapshot and never schedule, create speech evidence or award XP; only an intentional rating changes FSRS and normal review activity. A media failure still offers the Japanese text reference and meaning.

## Beginner unit vocabulary — source 0.1.20

`content/authoring/ja/beginner-unit-vocabulary-draft.json` holds 838 original contextual rows, stable vocabulary IDs and explicit lesson boundaries/titles across all ten units. It reuses four pre-existing word IDs and the kana/kanji pair くつ/靴 rather than counting repeated spellings as new words. `scripts/author_beginner_units.py` applies this batch to the exact archived 0.1.16 source, validates the full content graph and checks every generated key with the authoritative grader. It refuses to overwrite a different existing release. Run it with the installed virtual-environment Python from the project root; it performs no download or database write.

The batch adds 833 vocabulary records (823 words +10 expressions), 112 draft lessons and 1,363 checks. Final totals: 126 lessons (6 published +120 draft), 1,417 lesson checks (30 published +1,387 draft), plus 512 unchanged standalone checks. Meaning checks have answer-specific explanations and original translated examples; kanji-word readings have separate hiragana typing checks. Kana-only meaning prompts do not claim typed-reading evidence. All original published vocabulary and lesson definitions remain unchanged.

The audit maps vocabulary with lesson-linked exercises to those explicit units, distinct from a merely inferred concept overlap. 学校/がっこう count once, きって/切手 and くつ/靴 reuse stable IDs, and 皆さん/みんな conservatively count once. Twenty same-reading collision groups have explicit spelling/distinct-sense decisions. These are provisional authoring decisions pending qualified semantic review; no learner IDs, FSRS cards or saved records are merged.

Stage A has 541 provisional words against 500, Stage B has 566 against 1,500 additional words. The Stage B deficit is 934; Stage A overage cannot replace that target. Independent Japanese, stroke and teaching-audio review/publication remain open. The exact 0.1.20 packet contains 3,780 pending items; historical packets remain preserved. See [bounded-run evidence](PLAN_09_2_CURRICULUM.md).
