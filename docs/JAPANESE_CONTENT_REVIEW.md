# Japanese content review packet

Exact current source: ja-starter **0.1.21**, SHA-256 **94b99042f6f6054ac51807ac5482301cd0e4923bd383aaaa3d94b7d8ff5ea9d5**. Status: **qualified review pending**. No reviewer is available and no publication/review gate is closed.

## Source and queue

- [Exact source snapshot](reviews/ja-starter-0.1.21/source.json) includes every key, alternate, distractor, explanation, model, transcript, pronunciation override, transition and license.
- [Versioned inventory](reviews/ja-starter-0.1.21/inventory.json) lists **6,848 pending stable review items**, stage/concept/unit mappings, intended practice directions, authored/publication counts and explicit gaps. Explicit guide/lesson-exercise placement and inferred concept-overlap placement are labeled separately.
- [Pending review decisions](reviews/ja-starter-0.1.21/review-queue.json) provides one entry per stable item, reviewer/qualifications/date/corrections/decision fields, and verified asset digests. The six draft stroke assets are copied beside the snapshot at their original relative paths.
- [Lexical decisions](reviews/ja-starter-0.1.21/lexical-identities.json) preserve the earlier spelling/distinct-sense groups and saved IDs. There are **2,167 provisional identities (541 A +1,626 additional B)**, 2,169 word records and 15 separately counted expressions. Both separate raw authoring targets are exceeded; qualified semantic review and reviewed publication remain open. The additive batch reports 40 omitted same-spelling/reading/する-family candidates; omission is not proof of identical meaning. No learner records are merged.

The technical published slice remains two units, six lessons, thirty exercises, eight core word records and five expressions. Drafts include **230 lessons/3,261 lesson checks**, sixteen guides, 92 basic kana/135 variants, 300 kanji, seven writing tasks, two stories, four passages, six dialogues and two audio episodes. The **536 standalone definitions** include 16 speaking prompts and 24 new particle contrasts. The latest batch adds 1,060 Stage B words, 110 lessons and 1,874 lesson checks, all unreviewed draft. Raw target completion does not imply reviewed coverage or proficiency.

## Review procedure

Review naturalness, contextual readings, register, scoped alternatives, distractors, objectives, answer-aid policy, models/revisions, audio overrides and asset rights against this exact snapshot. Open writing models are examples, not exact-string keys. Stroke assets and teaching audio require their own qualified review. Test tones or transcripts cannot prove Japanese pronunciation.

Record reviewer identity, relevant qualifications, date and source version/hash with each decision. Put corrections in the queue; apply them in a new versioned source batch, validate/import twice, and regenerate into a new folder. The generator refuses to overwrite changed reviewer artifacts. A passing schema check is not linguistic approval.

Earlier packets are preserved: [0.1.11](reviews/JAPANESE_CONTENT_REVIEW.0.1.11.md), [0.1.14](reviews/ja-starter-0.1.14/inventory.json), [0.1.15](reviews/ja-starter-0.1.15/inventory.json), [0.1.16](reviews/ja-starter-0.1.16/inventory.json), [0.1.17](reviews/ja-starter-0.1.17/inventory.json), [0.1.18](reviews/ja-starter-0.1.18/inventory.json), [0.1.19](reviews/ja-starter-0.1.19/inventory.json), [0.1.20](reviews/ja-starter-0.1.20/inventory.json) and earlier Markdown packets under reviews/.

Reproduce from backend/:

~~~powershell
..\.venv\Scripts\python.exe -m app.content_audit --output ../docs/reviews/ja-starter-0.1.21
~~~

The audit binds lexical decisions to the exact source hash, validates assets/references, copies a self-contained source snapshot, and does not open a database or publish content.
