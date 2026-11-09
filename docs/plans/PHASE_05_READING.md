# Phase 05 — Kana, Kanji, and Reading

Status: Draft-scope engineering implemented and verified. Qualified publication/review and physical screen-reader gates remain open. The complete 300-character target is authored as draft. Depends on: [Phase 04](PHASE_04_LESSON_ENGINE.md). Next: [Phase 06](PHASE_06_WRITING.md).

## Goal

Teach a beginner to recognize Japanese scripts, read words in context, and understand short everyday text with gradually reduced support.

## Deliverables

- [x] Create data-driven hiragana and katakana libraries covering the 46 basic modern characters in each script, with voiced/semi-voiced forms and combinations taught separately.
- [x] Add drills for similar-looking characters, kana recognition, contextual readings, and word meaning through the existing exercise renderer.
- [x] Teach small ゃ/ゅ/ょ, small っ, ん, vowel length, and katakana ー through explicit concepts and authored contrast sets. Audio contrast becomes playable in Phase 8.
- [x] Make kana charts accessible grids of real controls, with meaningful labels and no hover-only information.
- [x] Provide furigana modes (always, unfamiliar material, hidden), stored in settings and derived from actual content/progress where required.
- [x] Use romaji only as an optional early aid; allow it to be hidden and gradually withdraw it. Never require it for later Japanese reading.
- [ ] Define reviewed kanji collections in useful words: 100 distinct Stage A kanji, then 200 additional Stage B kanji, for 300 cumulatively. Record contextual readings/meanings and actual published coverage; do not claim every reading or handwriting skill from recognition.
- [x] Add short original passages, signs, menus, schedules, and messages with comprehension questions and selectable vocabulary explanations.
- [ ] Add an original interactive story reader with short Japanese turns, staged comprehension checkpoints, vocabulary reveal, optional recap, and replay. Publish at least two reviewed stories at appropriate taught levels; Phase 8 adds listen-along audio and mini audio episodes.
- [x] Save unknown words and difficult characters to the existing mistake/practice system. Phase 9 turns eligible evidence into real scheduled review.
- [x] Track reading evidence independently from typing, handwriting, and speaking evidence.
- [ ] Expand reviewed curriculum content from Phase 3 as each needed renderer is available. Unreviewed units stay draft.

## Intended implementation areas

Reading/character library features, shared Japanese text rendering, course content files, content APIs, and migrations for character/reading evidence only where existing structures cannot hold it.

## Data and API contracts

- Introduce `character_recognition`, `reading_comprehension`, or other new exercise types only through strict schemas, server graders, and exhaustive renderer dispatch.
- A reading passage stores authored segments, per-segment readings, glossary links, comprehension prompts, difficulty, and version.
- A story stores reviewed turns, optional comprehension prompts, suggested preparation/concepts, reveal policy, and version. Reuse session services with free skip/reveal/continue and Phase 4's uncapped genuine-session reward. Record studied/assisted/skipped evidence without requiring correct answers to keep reading.
- A kanji entry may have several readings; an exercise identifies the expected contextual word reading and explicitly accepted variants.
- `ruby`/`rt` markup uses structured content. Do not render arbitrary source HTML or hide essential text from assistive technology.
- Configure meaning/reading objectives and accessible unassisted variants. Reading aids and deliberate reveal remain freely available; record assistance instead of blocking access or falsely claiming unaided recall.
- Recognition based on a visible word is not proof of unaided recall. Store assistance/hint use separately and distinguish those metrics.

## Tests and manual verification

- [x] Test character counts, referenced combinations, duplicate IDs, missing readings, and invalid rich-text segments.
- [x] Test contextual multiple readings, alternate valid answers, long vowels, small kana, and voiced/unvoiced distinctions.
- [x] Test reading aid persistence, unfamiliar-word behavior, hide/reveal behavior, and no answer leakage from ruby or accessible labels.
- [x] Test passage completion, wrong-answer feedback, unknown-word saves, repeated saves, and empty-library state.
- [x] Test story checkpoints, reveal/hint evidence, resume/replay, duplicate completion, content updates, and absence of private answer keys before submission.
- [ ] Manually read kana, a kanji word, and a short passage with aids on and off using keyboard and narrow mobile layout.
- [ ] Verify Japanese glyphs, line wrapping, zoom, and screen-reader reading order; do not rely solely on visual snapshots.
- [x] Run relevant frontend/backend gates, content validation, and migrations if schema changes.

## Completion gate

Complete when the kana libraries and published beginner reading collection, including at least two original interactive stories, are usable with accurate authored readings, adjustable aids, durable evidence, and validated content. Do not describe all kanji or an entire JLPT level as covered without an audited content inventory.

## Later-stage reading progression

For Stages C-F in the [curriculum roadmap](../CURRICULUM_ROADMAP.md), expand reviewed content from connected narratives to exposition, contrasting opinions, and multiple-source argument/synthesis. Teach inference, reference/cohesion, claims/evidence, summary/paraphrase, and source comparison before requiring them in writing. Validate source licenses, contextual readings, staged aid reduction, and comprehension evidence for each release; beginner passage completion cannot imply advanced reading proficiency.

## Current implementation work — 2026-10-23

Source 0.1.11 contains 92 basic kana, 135 separately counted variants/combinations/marks and 300 distinct draft contextual kanji (100 Stage A +200 additional Stage B). There are 481 standalone practice definitions and 291 vocabulary records (286 word records +5 expressions); semantic word deduplication and the 2,000-word target remain open. Published technical-practice coverage is unchanged at 6 lessons/30 exercises/8 core words/5 expressions. All added kanji/words remain draft, so the reviewed-collection checkbox stays open. Reading now searches across the full word library by Japanese, kana reading or meaning; the initial convenience batch can be freely expanded with Show more/all. Combined backend suite:123 PASS; frontend:24 PASS and lint/typecheck/build PASS; reading browser verification:32 layouts. See the Phase 5 verification record for commands and remaining review/device limits.

## Bounded curriculum continuation — 2026-10-24

[Plan 9.2 curriculum evidence](../PLAN_09_2_CURRICULUM.md) records source **0.1.20**: 112 additional draft lessons, 1,363 checks and 833 vocabulary records across the ten topics, using the existing reading/grammar/session engine. The provisional lexical inventory is **541 Stage A +566 additional Stage B**; **934 Stage B words**, qualified semantic/language review and applicable publication/provider/device gates remain open. Published lesson and vocabulary definitions are unchanged. Meaning/typed-reading evidence and draft practice are not reviewed proficiency or full beginner completion. No new checkbox is closed by the raw authoring count.
