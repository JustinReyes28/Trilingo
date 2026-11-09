# Japanese content review packet

Source: content/courses/ja/starter.json · ja-starter version 0.1.10
SHA-256 of the exact source file: 692a193b63efbc134eb473dc7bc47daed1521ea9c2f1c14db44a785478895680

Status: pending qualified Japanese-language and stroke review. This packet contains authoring keys and draft references; it is not an approval or proficiency assessment.

User decision: no reviewer is available. Keep new material draft and the existing slice labeled technical practice. No qualified-review gate is closed.

Reviewer: pending
Qualifications: pending
Review date: pending
Reviewed source version/hash: pending

## Review scope and instructions

Published technical practice remains2units/6lessons/30exercises/8core words/5expressions. Draft extensions:92basic kana,135variants/combinations/marks,300contextual kanji (100 Stage A +200 additional Stage B),278 draft word records,2stories,4passages,2audio scripts,7writing tasks and6original stroke templates. Standalone practice definitions:481. The 300-kanji authoring target is present as draft; qualified review/publication and the 2,000 unique-core-word target remain open. There are 286 total word records plus 5 expressions; record counts do not certify semantic uniqueness (the older 学校/がっこう records still share one lexical meaning).

Check naturalness, meaning, register, spelling, contextual readings, every key/alternate/distractor, learning objectives and aid policy by stable ID. Models for open writing are examples; they are not exact-string keys. Audio scripts are text-only. Review stroke count/order/direction/start/shape independently; all original schematic paths remain draft. Record corrections and reviewer identity/qualifications/date/version/hash before publication. The prior0.1.5packet is preserved in reviews/.

## Concepts and guides

### greeting — Greetings

Choose a greeting for the time and situation. こんにちは is used during the day.

- [ ] Qualified review; notes: pending

### politeness — Polite first exchanges

です and ございます help create polite everyday exchanges.

- [ ] Qualified review; notes: pending

### kana — Hiragana sound patterns

A normal kana generally represents one mora. Small っ and long vowels affect timing.

- [ ] Qualified review; notes: pending

### kana-small — Small kana change the sound

きゃ is one combined mora (kya); きや has two morae (ki-ya). Small ゃ/ゅ/ょ combine after an i-row kana. Small っ marks a held consonant before the next sound: きって (stamp), not きて. Audio examples arrive with audio practice.

- [ ] Qualified review; notes: pending

### kana-n — The independent ん

ん counts as one mora. It can occur inside or at the end of a word: ほん (book). Its sound changes with neighboring sounds; do not delete it or confuse it with a following vowel.

- [ ] Qualified review; notes: pending

### kana-length — Keep long vowels

Vowel length can distinguish words. おばさん (aunt) and おばあさん (grandmother) differ in length. In hiragana, long vowels use authored spellings: おかあさん and がっこう. Katakana commonly uses ー: コーヒー. Do not shorten these spellings. Audio contrasts are not available yet.

- [ ] Qualified review; notes: pending

### kana-voicing — Voicing and similar shapes

Dakuten changes a kana: か→が and は→ば. Handakuten gives は→ぱ. Katakana シ/ツ and ソ/ン have similar shapes; notice the orientation and placement of the short strokes. A font sample is a reading aid, not stroke-order instruction.

- [ ] Qualified review; notes: pending

### reading-context — Read a kanji inside a word

Kanji readings depend on the word. 日 is に in 日本 (にほん), but にち in 日曜日 (にちようび). Study the whole contextual word. One recognition answer does not prove every reading or handwriting skill.

- [ ] Qualified review; notes: pending

## Unit guides and lesson keys

### ja-unit-1 — First sounds and greetings (published)

こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.

ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.

A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.

### ja-greetings-hello — Say hello

Objective: Recognize and use a daytime greeting.

#### ja-greetings-hello-choice

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and use a daytime greeting.
- Prompt: Choose the daytime greeting.
- Choices: c0: こんにちは | c1: ありがとう | c2: さようなら
- Expected/accepted: こんにちは [c0]
- Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: greeting
- Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-greetings-hello-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and use a daytime greeting.
- Prompt: Write “hello” as a daytime greeting in Japanese.
- Expected/accepted: こんにちは
- Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: greeting
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-greetings-hello-blank

- [ ] Qualified review; corrections/notes: pending
- Type/skill: fill_blank / typing
- Objective: Recognize and use a daytime greeting.
- Prompt: Complete the greeting: こんに＿＿
- Expected/accepted: ちは
- Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: greeting
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-greetings-hello-order

- [ ] Qualified review; corrections/notes: pending
- Type/skill: sentence_ordering / recognition
- Objective: Recognize and use a daytime greeting.
- Prompt: Arrange the parts into the taught expression.
- Tokens: t1: 。 | t0: こんにちは
- Expected/accepted: こんにちは。 [t0, t1]
- Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: greeting
- Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-greetings-hello-match

- [ ] Qualified review; corrections/notes: pending
- Type/skill: matching / meaning
- Objective: Recognize and use a daytime greeting.
- Prompt: Match each Japanese expression with its English meaning.
- Expected/accepted: こんにちは → Hello | さようなら → Goodbye
- Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: greeting
- Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

### ja-greetings-thanks — Say thank you

Objective: Recognize thanks and a polite thank-you.

#### ja-greetings-thanks-choice

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize thanks and a polite thank-you.
- Prompt: Which phrase means “thank you” in a casual exchange?
- Choices: c0: ありがとう | c1: こんばんは | c2: さようなら
- Expected/accepted: ありがとう [c0]
- Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-greetings-thanks-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize thanks and a polite thank-you.
- Prompt: Write a casual “thank you” in Japanese.
- Expected/accepted: ありがとう
- Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-greetings-thanks-blank

- [ ] Qualified review; corrections/notes: pending
- Type/skill: fill_blank / typing
- Objective: Recognize thanks and a polite thank-you.
- Prompt: Complete the polite thank-you: ありがとう［　］
- Expected/accepted: ございます
- Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-greetings-thanks-order

- [ ] Qualified review; corrections/notes: pending
- Type/skill: sentence_ordering / recognition
- Objective: Recognize thanks and a polite thank-you.
- Prompt: Arrange the parts into the taught expression.
- Tokens: t2: 。 | t1: ございます | t0: ありがとう
- Expected/accepted: ありがとうございます。 [t0, t1, t2]
- Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-greetings-thanks-match

- [ ] Qualified review; corrections/notes: pending
- Type/skill: matching / meaning
- Objective: Recognize thanks and a polite thank-you.
- Prompt: Match each Japanese expression with its English meaning.
- Expected/accepted: ありがとう → Thank you | ありがとうございます → Thank you (polite)
- Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

### ja-greetings-names — Introduce yourself

Objective: Use a simple introduction with です.

#### ja-greetings-names-choice

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Use a simple introduction with です.
- Prompt: You meet someone for the first time. Choose “Nice to meet you.”
- Choices: c0: はじめまして | c1: おやすみなさい | c2: ありがとう
- Expected/accepted: はじめまして [c0]
- Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-greetings-names-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Use a simple introduction with です.
- Prompt: Write “I am Aki.” Use アキ and polite です.
- Expected/accepted: アキです。 | アキです
- Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-greetings-names-blank

- [ ] Qualified review; corrections/notes: pending
- Type/skill: fill_blank / typing
- Objective: Use a simple introduction with です.
- Prompt: Complete “I am Aki”: アキ＿＿
- Expected/accepted: です
- Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-greetings-names-order

- [ ] Qualified review; corrections/notes: pending
- Type/skill: sentence_ordering / recognition
- Objective: Use a simple introduction with です.
- Prompt: Arrange the parts into the taught expression.
- Tokens: t2: 。 | t1: です | t0: アキ
- Expected/accepted: アキです。 [t0, t1, t2]
- Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-greetings-names-match

- [ ] Qualified review; corrections/notes: pending
- Type/skill: matching / meaning
- Objective: Use a simple introduction with です.
- Prompt: Match each Japanese expression with its English meaning.
- Expected/accepted: はじめまして → Nice to meet you | アキです → I am Aki
- Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
- Hint: Look at the phrase parts and the politeness requested.
- Concepts: politeness
- Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

### ja-unit-2 — Hiragana foundations (published)

The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.

The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.

Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.

### ja-hiragana-vowels — Meet the vowels

Objective: Recognize the first five hiragana and read simple vowel words.

#### ja-hiragana-vowels-choice

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize the first five hiragana and read simple vowel words.
- Prompt: Which hiragana represents the sound a?
- Choices: c0: あ | c1: い | c2: う
- Expected/accepted: あ [c0]
- Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-hiragana-vowels-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize the first five hiragana and read simple vowel words.
- Prompt: Write the hiragana for the sound i.
- Expected/accepted: い
- Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-hiragana-vowels-blank

- [ ] Qualified review; corrections/notes: pending
- Type/skill: fill_blank / typing
- Objective: Recognize the first five hiragana and read simple vowel words.
- Prompt: Complete the vowel row: あ・い・う・＿＿・お
- Expected/accepted: え
- Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-hiragana-vowels-order

- [ ] Qualified review; corrections/notes: pending
- Type/skill: sentence_ordering / recognition
- Objective: Recognize the first five hiragana and read simple vowel words.
- Prompt: Arrange the five vowel kana in chart order.
- Tokens: t4: お | t3: え | t2: う | t1: い | t0: あ
- Expected/accepted: あいうえお [t0, t1, t2, t3, t4]
- Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-hiragana-vowels-match

- [ ] Qualified review; corrections/notes: pending
- Type/skill: matching / meaning
- Objective: Recognize the first five hiragana and read simple vowel words.
- Prompt: Match each Japanese expression with its English meaning.
- Expected/accepted: あい → Love | いえ → House
- Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

### ja-hiragana-k — Read the k row

Objective: Read k-row kana in short everyday words.

#### ja-hiragana-k-choice

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Read k-row kana in short everyday words.
- Prompt: Which kana represents the sound ki?
- Choices: c0: き | c1: か | c2: こ
- Expected/accepted: き [c0]
- Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-hiragana-k-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Read k-row kana in short everyday words.
- Prompt: Write the word “here” using hiragana: koko.
- Expected/accepted: ここ
- Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-hiragana-k-blank

- [ ] Qualified review; corrections/notes: pending
- Type/skill: fill_blank / typing
- Objective: Read k-row kana in short everyday words.
- Prompt: Complete “face”: か＿＿
- Expected/accepted: お
- Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-hiragana-k-order

- [ ] Qualified review; corrections/notes: pending
- Type/skill: sentence_ordering / recognition
- Objective: Read k-row kana in short everyday words.
- Prompt: Arrange the k-row kana in chart order.
- Tokens: t4: こ | t3: け | t2: く | t1: き | t0: か
- Expected/accepted: かきくけこ [t0, t1, t2, t3, t4]
- Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-hiragana-k-match

- [ ] Qualified review; corrections/notes: pending
- Type/skill: matching / meaning
- Objective: Read k-row kana in short everyday words.
- Prompt: Match each Japanese expression with its English meaning.
- Expected/accepted: かお → Face | こえ → Voice
- Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

### ja-hiragana-sounds — Notice sound differences

Objective: Notice voicing, vowel length and small っ in authored word examples.

#### ja-hiragana-sounds-choice

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Notice voicing, vowel length and small っ in authored word examples.
- Prompt: Which spelling means “stamp” (kitte)?
- Choices: c0: きって | c1: きて | c2: きいて
- Expected/accepted: きって [c0]
- Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-hiragana-sounds-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Notice voicing, vowel length and small っ in authored word examples.
- Prompt: Write the voiced counterpart of か.
- Expected/accepted: が
- Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-hiragana-sounds-blank

- [ ] Qualified review; corrections/notes: pending
- Type/skill: fill_blank / typing
- Objective: Notice voicing, vowel length and small っ in authored word examples.
- Prompt: Complete the word for “stamp”: き＿＿て
- Expected/accepted: っ
- Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-hiragana-sounds-order

- [ ] Qualified review; corrections/notes: pending
- Type/skill: sentence_ordering / recognition
- Objective: Notice voicing, vowel length and small っ in authored word examples.
- Prompt: Build the word for “school” (gakkō).
- Tokens: t3: う | t2: こ | t1: っ | t0: が
- Expected/accepted: がっこう [t0, t1, t2, t3]
- Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

#### ja-hiragana-sounds-match

- [ ] Qualified review; corrections/notes: pending
- Type/skill: matching / meaning
- Objective: Notice voicing, vowel length and small っ in authored word examples.
- Prompt: Match each Japanese expression with its English meaning.
- Expected/accepted: がっこう → School | きって → Postage stamp
- Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
- Hint: Check the shape, voicing marks, and kana size.
- Concepts: kana
- Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}

### ja-unit-3 — Katakana and familiar words (draft)

Learn the basic katakana set, combinations, loanwords, and long vowels.

### ja-unit-4 — People and things (draft)

Use は, です, questions and demonstratives in simple descriptions.

### ja-unit-5 — Numbers, time, and purchases (draft)

Use explicitly taught number, time, date and counter readings.

### ja-unit-6 — Food and ordering (draft)

Use polite requests, を and common menu words.

### ja-unit-7 — Places and directions (draft)

Use に, で and へ in taught location and movement contexts.

### ja-unit-8 — Daily routines (draft)

Describe schedules using polite present, past and negative forms.

### ja-unit-9 — Descriptions and preferences (draft)

Use introductory adjectives, preferences and taught comparisons.

### ja-unit-10 — Everyday connections (draft)

Write short messages, make invitations and revisit practical exchanges.

## Vocabulary

### ja-word-hello — こんにちは

- [ ] Qualified review; notes: pending
- Status/kind: published / phrase
- Reading: こんにちは
- Meaning/register: Hello (daytime) / neutral
- Examples: [{"surface":"こんにちは。アキです。"}]
- Related drills: 

### ja-word-goodbye — さようなら

- [ ] Qualified review; notes: pending
- Status/kind: published / phrase
- Reading: さようなら
- Meaning/register: Goodbye / neutral
- Examples: [{"surface":"さようなら。またあした。"}]
- Related drills: 

### ja-word-thanks — ありがとう

- [ ] Qualified review; notes: pending
- Status/kind: published / phrase
- Reading: ありがとう
- Meaning/register: Thank you / casual
- Examples: [{"surface":"ありがとう。うれしいです。"}]
- Related drills: 

### ja-word-polite-thanks — ありがとうございます

- [ ] Qualified review; notes: pending
- Status/kind: published / phrase
- Reading: ありがとうございます
- Meaning/register: Thank you (polite) / polite
- Examples: [{"surface":"ありがとうございます。たすかりました。"}]
- Related drills: 

### ja-word-first-meeting — はじめまして

- [ ] Qualified review; notes: pending
- Status/kind: published / phrase
- Reading: はじめまして
- Meaning/register: Nice to meet you / neutral
- Examples: [{"surface":"はじめまして。アキです。"}]
- Related drills: 

### ja-word-copula — です

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: です
- Meaning/register: Polite copula / polite
- Examples: [{"surface":"アキです。"}]
- Related drills: 

### ja-word-love — あい

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: あい
- Meaning/register: Love / neutral
- Examples: [{"surface":"あいはたいせつです。"}]
- Related drills: 

### ja-word-house — いえ

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: いえ
- Meaning/register: House / neutral
- Examples: [{"surface":"これはいえです。"}]
- Related drills: ja-hiragana-vowels-choice, ja-hiragana-vowels-type, ja-hiragana-vowels-blank, ja-hiragana-vowels-order, ja-hiragana-vowels-match

### ja-word-here — ここ

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: ここ
- Meaning/register: Here / neutral
- Examples: [{"surface":"ここです。"}]
- Related drills: 

### ja-word-face — かお

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: かお
- Meaning/register: Face / neutral
- Examples: [{"surface":"かおをあらいます。"}]
- Related drills: 

### ja-word-voice — こえ

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: こえ
- Meaning/register: Voice / neutral
- Examples: [{"surface":"いいこえですね。"}]
- Related drills: 

### ja-word-school — がっこう

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: がっこう
- Meaning/register: School / neutral
- Examples: [{"surface":"がっこうにいきます。"}]
- Related drills: 

### ja-word-stamp — きって

- [ ] Qualified review; notes: pending
- Status/kind: published / word
- Reading: きって
- Meaning/register: Postage stamp / neutral
- Examples: [{"surface":"きってをください。"}]
- Related drills: 

### ja-word-japan — 日本

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: にほん
- Meaning/register: Japan / neutral
- Examples: [{"surface":"日本","reading":"にほん","vocabulary_id":"ja-word-japan"}]
- Related drills: ja-reading-japan

### ja-word-sunday — 日曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: にちようび
- Meaning/register: Sunday / neutral
- Examples: [{"surface":"日曜日","reading":"にちようび","vocabulary_id":"ja-word-sunday"}]
- Related drills: ja-reading-sunday

### ja-word-water — 水

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: みず
- Meaning/register: water / neutral
- Examples: [{"surface":"水","reading":"みず","vocabulary_id":"ja-word-water"}]
- Related drills: ja-reading-water

### ja-word-tea — お茶

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: おちゃ
- Meaning/register: tea / neutral
- Examples: [{"surface":"お茶","reading":"おちゃ","vocabulary_id":"ja-word-tea"}]
- Related drills: ja-reading-tea

### ja-word-station — 駅

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: えき
- Meaning/register: station / neutral
- Examples: [{"surface":"駅","reading":"えき","vocabulary_id":"ja-word-station"}]
- Related drills: ja-reading-station

### ja-word-entrance — 入口

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: いりぐち
- Meaning/register: entrance / neutral
- Examples: [{"surface":"入口","reading":"いりぐち","vocabulary_id":"ja-word-entrance"}]
- Related drills: ja-reading-entrance

### ja-word-exit — 出口

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: でぐち
- Meaning/register: exit / neutral
- Examples: [{"surface":"出口","reading":"でぐち","vocabulary_id":"ja-word-exit"}]
- Related drills: ja-reading-exit

### ja-word-school-kanji — 学校

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: がっこう
- Meaning/register: school / neutral
- Examples: [{"surface":"学校","reading":"がっこう","vocabulary_id":"ja-word-school-kanji"}]
- Related drills: ja-reading-school-kanji

### ja-word-book — 本

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: ほん
- Meaning/register: book / neutral
- Examples: [{"surface":"本","reading":"ほん","vocabulary_id":"ja-word-book"}]
- Related drills: ja-reading-book

### ja-word-time — 時間

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: じかん
- Meaning/register: time / neutral
- Examples: [{"surface":"時間","reading":"じかん","vocabulary_id":"ja-word-time"}]
- Related drills: ja-reading-time

### ja-word-monday — 月曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: げつようび
- Meaning/register: Monday / neutral
- Examples: [{"surface":"月曜日","reading":"げつようび","vocabulary_id":"ja-word-monday"}]
- Related drills: ja-reading-monday

### ja-word-tuesday — 火曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: かようび
- Meaning/register: Tuesday / neutral
- Examples: [{"surface":"火曜日","reading":"かようび","vocabulary_id":"ja-word-tuesday"}]
- Related drills: ja-reading-tuesday

### ja-word-wednesday — 水曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: すいようび
- Meaning/register: Wednesday / neutral
- Examples: [{"surface":"水曜日","reading":"すいようび","vocabulary_id":"ja-word-wednesday"}]
- Related drills: ja-reading-wednesday

### ja-word-thursday — 木曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: もくようび
- Meaning/register: Thursday / neutral
- Examples: [{"surface":"木曜日","reading":"もくようび","vocabulary_id":"ja-word-thursday"}]
- Related drills: ja-reading-thursday

### ja-word-friday — 金曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: きんようび
- Meaning/register: Friday / neutral
- Examples: [{"surface":"金曜日","reading":"きんようび","vocabulary_id":"ja-word-friday"}]
- Related drills: ja-reading-friday

### ja-word-saturday — 土曜日

- [ ] Qualified review; notes: pending
- Status/kind: draft / word
- Reading: どようび
- Meaning/register: Saturday / neutral
- Examples: [{"surface":"土曜日","reading":"どようび","vocabulary_id":"ja-word-saturday"}]
- Related drills: ja-reading-saturday

## Character inventory

### ja-char-a — あ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: a
- Optional romaji: a
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-a-recognize, ja-char-a-type
- Stroke reference: none

### ja-char-hiragana-3044 — い

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: i
- Optional romaji: i
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3044-recognize, ja-char-hiragana-3044-type
- Stroke reference: ja-stroke-3044-v1

### ja-char-hiragana-3046 — う

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: u
- Optional romaji: u
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3046-recognize, ja-char-hiragana-3046-type
- Stroke reference: ja-stroke-3046-v1

### ja-char-hiragana-3048 — え

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: e
- Optional romaji: e
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3048-recognize, ja-char-hiragana-3048-type
- Stroke reference: none

### ja-char-hiragana-304a — お

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: o
- Optional romaji: o
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-304a-recognize, ja-char-hiragana-304a-type
- Stroke reference: none

### ja-char-hiragana-304b — か

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ka
- Optional romaji: ka
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-304b-recognize, ja-char-hiragana-304b-type
- Stroke reference: none

### ja-char-hiragana-304d — き

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ki
- Optional romaji: ki
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-304d-recognize, ja-char-hiragana-304d-type
- Stroke reference: none

### ja-char-hiragana-304f — く

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ku
- Optional romaji: ku
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-304f-recognize, ja-char-hiragana-304f-type
- Stroke reference: none

### ja-char-hiragana-3051 — け

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ke
- Optional romaji: ke
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3051-recognize, ja-char-hiragana-3051-type
- Stroke reference: none

### ja-char-hiragana-3053 — こ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ko
- Optional romaji: ko
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3053-recognize, ja-char-hiragana-3053-type
- Stroke reference: ja-stroke-3053-v1

### ja-char-hiragana-3055 — さ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: sa
- Optional romaji: sa
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3055-recognize, ja-char-hiragana-3055-type
- Stroke reference: none

### ja-char-hiragana-3057 — し

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: shi
- Optional romaji: shi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3057-recognize, ja-char-hiragana-3057-type
- Stroke reference: none

### ja-char-hiragana-3059 — す

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: su
- Optional romaji: su
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3059-recognize, ja-char-hiragana-3059-type
- Stroke reference: none

### ja-char-hiragana-305b — せ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: se
- Optional romaji: se
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-305b-recognize, ja-char-hiragana-305b-type
- Stroke reference: none

### ja-char-hiragana-305d — そ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: so
- Optional romaji: so
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-305d-recognize, ja-char-hiragana-305d-type
- Stroke reference: none

### ja-char-hiragana-305f — た

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ta
- Optional romaji: ta
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-305f-recognize, ja-char-hiragana-305f-type
- Stroke reference: none

### ja-char-hiragana-3061 — ち

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: chi
- Optional romaji: chi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3061-recognize, ja-char-hiragana-3061-type
- Stroke reference: none

### ja-char-hiragana-3064 — つ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: tsu
- Optional romaji: tsu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3064-recognize, ja-char-hiragana-3064-type
- Stroke reference: none

### ja-char-hiragana-3066 — て

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: te
- Optional romaji: te
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3066-recognize, ja-char-hiragana-3066-type
- Stroke reference: none

### ja-char-hiragana-3068 — と

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: to
- Optional romaji: to
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3068-recognize, ja-char-hiragana-3068-type
- Stroke reference: none

### ja-char-hiragana-306a — な

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: na
- Optional romaji: na
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-306a-recognize, ja-char-hiragana-306a-type
- Stroke reference: none

### ja-char-hiragana-306b — に

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ni
- Optional romaji: ni
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-306b-recognize, ja-char-hiragana-306b-type
- Stroke reference: none

### ja-char-hiragana-306c — ぬ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: nu
- Optional romaji: nu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-306c-recognize, ja-char-hiragana-306c-type
- Stroke reference: none

### ja-char-hiragana-306d — ね

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ne
- Optional romaji: ne
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-306d-recognize, ja-char-hiragana-306d-type
- Stroke reference: none

### ja-char-hiragana-306e — の

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: no
- Optional romaji: no
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-306e-recognize, ja-char-hiragana-306e-type
- Stroke reference: none

### ja-char-hiragana-306f — は

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ha
- Optional romaji: ha
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-306f-recognize, ja-char-hiragana-306f-type
- Stroke reference: none

### ja-char-hiragana-3072 — ひ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: hi
- Optional romaji: hi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3072-recognize, ja-char-hiragana-3072-type
- Stroke reference: none

### ja-char-hiragana-3075 — ふ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: fu
- Optional romaji: fu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3075-recognize, ja-char-hiragana-3075-type
- Stroke reference: none

### ja-char-hiragana-3078 — へ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: he
- Optional romaji: he
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3078-recognize, ja-char-hiragana-3078-type
- Stroke reference: none

### ja-char-hiragana-307b — ほ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ho
- Optional romaji: ho
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-307b-recognize, ja-char-hiragana-307b-type
- Stroke reference: none

### ja-char-hiragana-307e — ま

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ma
- Optional romaji: ma
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-307e-recognize, ja-char-hiragana-307e-type
- Stroke reference: none

### ja-char-hiragana-307f — み

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: mi
- Optional romaji: mi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-307f-recognize, ja-char-hiragana-307f-type
- Stroke reference: none

### ja-char-hiragana-3080 — む

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: mu
- Optional romaji: mu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3080-recognize, ja-char-hiragana-3080-type
- Stroke reference: none

### ja-char-hiragana-3081 — め

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: me
- Optional romaji: me
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3081-recognize, ja-char-hiragana-3081-type
- Stroke reference: none

### ja-char-hiragana-3082 — も

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: mo
- Optional romaji: mo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3082-recognize, ja-char-hiragana-3082-type
- Stroke reference: none

### ja-char-hiragana-3084 — や

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ya
- Optional romaji: ya
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3084-recognize, ja-char-hiragana-3084-type
- Stroke reference: none

### ja-char-hiragana-3086 — ゆ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: yu
- Optional romaji: yu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3086-recognize, ja-char-hiragana-3086-type
- Stroke reference: none

### ja-char-hiragana-3088 — よ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: yo
- Optional romaji: yo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3088-recognize, ja-char-hiragana-3088-type
- Stroke reference: none

### ja-char-hiragana-3089 — ら

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ra
- Optional romaji: ra
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3089-recognize, ja-char-hiragana-3089-type
- Stroke reference: none

### ja-char-hiragana-308a — り

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ri
- Optional romaji: ri
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-308a-recognize, ja-char-hiragana-308a-type
- Stroke reference: none

### ja-char-hiragana-308b — る

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ru
- Optional romaji: ru
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-308b-recognize, ja-char-hiragana-308b-type
- Stroke reference: none

### ja-char-hiragana-308c — れ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: re
- Optional romaji: re
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-308c-recognize, ja-char-hiragana-308c-type
- Stroke reference: none

### ja-char-hiragana-308d — ろ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: ro
- Optional romaji: ro
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-308d-recognize, ja-char-hiragana-308d-type
- Stroke reference: none

### ja-char-hiragana-308f — わ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: wa
- Optional romaji: wa
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-308f-recognize, ja-char-hiragana-308f-type
- Stroke reference: none

### ja-char-hiragana-3092 — を

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: wo
- Optional romaji: wo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3092-recognize, ja-char-hiragana-3092-type
- Stroke reference: none

### ja-char-hiragana-3093 — ん

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / basic
- Contextual readings: n
- Optional romaji: n
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-hiragana-3093-recognize, ja-char-hiragana-3093-type, ja-contrast-n
- Stroke reference: none

### ja-char-hiragana-304c — が

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: ga
- Optional romaji: ga
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-304e — ぎ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: gi
- Optional romaji: gi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3050 — ぐ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: gu
- Optional romaji: gu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3052 — げ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: ge
- Optional romaji: ge
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3054 — ご

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: go
- Optional romaji: go
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3056 — ざ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: za
- Optional romaji: za
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3058 — じ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: ji
- Optional romaji: ji
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-305a — ず

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: zu
- Optional romaji: zu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-305c — ぜ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: ze
- Optional romaji: ze
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-305e — ぞ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: zo
- Optional romaji: zo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3060 — だ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: da
- Optional romaji: da
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3062 — ぢ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: ji
- Optional romaji: ji
- Context/notes:  This is a d-row voiced form. A shared romanization does not make spellings interchangeable; learn their word context.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3065 — づ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: zu
- Optional romaji: zu
- Context/notes:  This is a d-row voiced form. A shared romanization does not make spellings interchangeable; learn their word context.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3067 — で

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: de
- Optional romaji: de
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3069 — ど

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: do
- Optional romaji: do
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3070 — ば

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: ba
- Optional romaji: ba
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3073 — び

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: bi
- Optional romaji: bi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3076 — ぶ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: bu
- Optional romaji: bu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3079 — べ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: be
- Optional romaji: be
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-307c — ぼ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / voiced
- Contextual readings: bo
- Optional romaji: bo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3071 — ぱ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / semi_voiced
- Contextual readings: pa
- Optional romaji: pa
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3074 — ぴ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / semi_voiced
- Contextual readings: pi
- Optional romaji: pi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-3077 — ぷ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / semi_voiced
- Contextual readings: pu
- Optional romaji: pu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-307a — ぺ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / semi_voiced
- Contextual readings: pe
- Optional romaji: pe
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-307d — ぽ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / semi_voiced
- Contextual readings: po
- Optional romaji: po
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-hiragana-304d3083 — きゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: kya
- Optional romaji: kya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-304d, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-304d3085 — きゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: kyu
- Optional romaji: kyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-304d, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-304d3087 — きょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: kyo
- Optional romaji: kyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-304d, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-304e3083 — ぎゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: gya
- Optional romaji: gya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-304e, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-304e3085 — ぎゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: gyu
- Optional romaji: gyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-304e, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-304e3087 — ぎょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: gyo
- Optional romaji: gyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-304e, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30573083 — しゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: sha
- Optional romaji: sha
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3057, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30573085 — しゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: shu
- Optional romaji: shu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3057, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30573087 — しょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: sho
- Optional romaji: sho
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3057, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30583083 — じゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: ja
- Optional romaji: ja
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3058, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30583085 — じゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: ju
- Optional romaji: ju
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3058, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30583087 — じょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: jo
- Optional romaji: jo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3058, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30613083 — ちゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: cha
- Optional romaji: cha
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3061, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30613085 — ちゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: chu
- Optional romaji: chu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3061, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30613087 — ちょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: cho
- Optional romaji: cho
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3061, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-306b3083 — にゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: nya
- Optional romaji: nya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-306b, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-306b3085 — にゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: nyu
- Optional romaji: nyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-306b, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-306b3087 — にょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: nyo
- Optional romaji: nyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-306b, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30723083 — ひゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: hya
- Optional romaji: hya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3072, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30723085 — ひゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: hyu
- Optional romaji: hyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3072, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30723087 — ひょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: hyo
- Optional romaji: hyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3072, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30733083 — びゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: bya
- Optional romaji: bya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3073, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30733085 — びゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: byu
- Optional romaji: byu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3073, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30733087 — びょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: byo
- Optional romaji: byo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3073, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30743083 — ぴゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: pya
- Optional romaji: pya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3074, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30743085 — ぴゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: pyu
- Optional romaji: pyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3074, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-30743087 — ぴょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: pyo
- Optional romaji: pyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-3074, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-307f3083 — みゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: mya
- Optional romaji: mya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-307f, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-307f3085 — みゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: myu
- Optional romaji: myu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-307f, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-307f3087 — みょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: myo
- Optional romaji: myo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-307f, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-308a3083 — りゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: rya
- Optional romaji: rya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-308a, ja-char-hiragana-3083
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-308a3085 — りゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: ryu
- Optional romaji: ryu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-308a, ja-char-hiragana-3085
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-308a3087 — りょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / combination
- Contextual readings: ryo
- Optional romaji: ryo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-hiragana-308a, ja-char-hiragana-3087
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3041 — ぁ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ぁ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3043 — ぃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ぃ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3045 — ぅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ぅ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3047 — ぇ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ぇ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3049 — ぉ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ぉ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3083 — ゃ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ゃ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3085 — ゅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ゅ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3087 — ょ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: ょ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-hiragana-3063 — っ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / hiragana / small
- Contextual readings: っ
- Optional romaji: none
- Context/notes:  Small tsu marks a following consonant closure/doubling in taught contexts; it is distinct from full-size tsu.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30a2 — ア

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: a
- Optional romaji: a
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30a2-recognize, ja-char-katakana-30a2-type
- Stroke reference: none

### ja-char-katakana-30a4 — イ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: i
- Optional romaji: i
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30a4-recognize, ja-char-katakana-30a4-type
- Stroke reference: none

### ja-char-katakana-30a6 — ウ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: u
- Optional romaji: u
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30a6-recognize, ja-char-katakana-30a6-type
- Stroke reference: none

### ja-char-katakana-30a8 — エ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: e
- Optional romaji: e
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30a8-recognize, ja-char-katakana-30a8-type
- Stroke reference: none

### ja-char-katakana-30aa — オ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: o
- Optional romaji: o
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30aa-recognize, ja-char-katakana-30aa-type
- Stroke reference: none

### ja-char-katakana-30ab — カ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ka
- Optional romaji: ka
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ab-recognize, ja-char-katakana-30ab-type
- Stroke reference: none

### ja-char-katakana-30ad — キ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ki
- Optional romaji: ki
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ad-recognize, ja-char-katakana-30ad-type
- Stroke reference: none

### ja-char-katakana-30af — ク

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ku
- Optional romaji: ku
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30af-recognize, ja-char-katakana-30af-type
- Stroke reference: none

### ja-char-katakana-30b1 — ケ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ke
- Optional romaji: ke
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30b1-recognize, ja-char-katakana-30b1-type
- Stroke reference: none

### ja-char-katakana-30b3 — コ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ko
- Optional romaji: ko
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30b3-recognize, ja-char-katakana-30b3-type
- Stroke reference: none

### ja-char-katakana-30b5 — サ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: sa
- Optional romaji: sa
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30b5-recognize, ja-char-katakana-30b5-type
- Stroke reference: none

### ja-char-katakana-30b7 — シ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: shi
- Optional romaji: shi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30b7-recognize, ja-char-katakana-30b7-type
- Stroke reference: none

### ja-char-katakana-30b9 — ス

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: su
- Optional romaji: su
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30b9-recognize, ja-char-katakana-30b9-type
- Stroke reference: none

### ja-char-katakana-30bb — セ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: se
- Optional romaji: se
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30bb-recognize, ja-char-katakana-30bb-type
- Stroke reference: none

### ja-char-katakana-30bd — ソ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: so
- Optional romaji: so
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30bd-recognize, ja-char-katakana-30bd-type
- Stroke reference: none

### ja-char-katakana-30bf — タ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ta
- Optional romaji: ta
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30bf-recognize, ja-char-katakana-30bf-type
- Stroke reference: none

### ja-char-katakana-30c1 — チ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: chi
- Optional romaji: chi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30c1-recognize, ja-char-katakana-30c1-type
- Stroke reference: none

### ja-char-katakana-30c4 — ツ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: tsu
- Optional romaji: tsu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30c4-recognize, ja-char-katakana-30c4-type
- Stroke reference: none

### ja-char-katakana-30c6 — テ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: te
- Optional romaji: te
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30c6-recognize, ja-char-katakana-30c6-type
- Stroke reference: none

### ja-char-katakana-30c8 — ト

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: to
- Optional romaji: to
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30c8-recognize, ja-char-katakana-30c8-type
- Stroke reference: none

### ja-char-katakana-30ca — ナ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: na
- Optional romaji: na
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ca-recognize, ja-char-katakana-30ca-type
- Stroke reference: none

### ja-char-katakana-30cb — ニ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ni
- Optional romaji: ni
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30cb-recognize, ja-char-katakana-30cb-type
- Stroke reference: none

### ja-char-katakana-30cc — ヌ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: nu
- Optional romaji: nu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30cc-recognize, ja-char-katakana-30cc-type
- Stroke reference: none

### ja-char-katakana-30cd — ネ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ne
- Optional romaji: ne
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30cd-recognize, ja-char-katakana-30cd-type
- Stroke reference: none

### ja-char-katakana-30ce — ノ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: no
- Optional romaji: no
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ce-recognize, ja-char-katakana-30ce-type
- Stroke reference: none

### ja-char-katakana-30cf — ハ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ha
- Optional romaji: ha
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30cf-recognize, ja-char-katakana-30cf-type
- Stroke reference: none

### ja-char-katakana-30d2 — ヒ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: hi
- Optional romaji: hi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30d2-recognize, ja-char-katakana-30d2-type
- Stroke reference: none

### ja-char-katakana-30d5 — フ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: fu
- Optional romaji: fu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30d5-recognize, ja-char-katakana-30d5-type
- Stroke reference: none

### ja-char-katakana-30d8 — ヘ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: he
- Optional romaji: he
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30d8-recognize, ja-char-katakana-30d8-type
- Stroke reference: none

### ja-char-katakana-30db — ホ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ho
- Optional romaji: ho
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30db-recognize, ja-char-katakana-30db-type
- Stroke reference: none

### ja-char-katakana-30de — マ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ma
- Optional romaji: ma
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30de-recognize, ja-char-katakana-30de-type
- Stroke reference: none

### ja-char-katakana-30df — ミ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: mi
- Optional romaji: mi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30df-recognize, ja-char-katakana-30df-type
- Stroke reference: none

### ja-char-katakana-30e0 — ム

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: mu
- Optional romaji: mu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e0-recognize, ja-char-katakana-30e0-type
- Stroke reference: none

### ja-char-katakana-30e1 — メ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: me
- Optional romaji: me
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e1-recognize, ja-char-katakana-30e1-type
- Stroke reference: none

### ja-char-katakana-30e2 — モ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: mo
- Optional romaji: mo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e2-recognize, ja-char-katakana-30e2-type
- Stroke reference: none

### ja-char-katakana-30e4 — ヤ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ya
- Optional romaji: ya
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e4-recognize, ja-char-katakana-30e4-type
- Stroke reference: none

### ja-char-katakana-30e6 — ユ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: yu
- Optional romaji: yu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e6-recognize, ja-char-katakana-30e6-type
- Stroke reference: none

### ja-char-katakana-30e8 — ヨ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: yo
- Optional romaji: yo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e8-recognize, ja-char-katakana-30e8-type
- Stroke reference: none

### ja-char-katakana-30e9 — ラ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ra
- Optional romaji: ra
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30e9-recognize, ja-char-katakana-30e9-type
- Stroke reference: none

### ja-char-katakana-30ea — リ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ri
- Optional romaji: ri
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ea-recognize, ja-char-katakana-30ea-type
- Stroke reference: none

### ja-char-katakana-30eb — ル

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ru
- Optional romaji: ru
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30eb-recognize, ja-char-katakana-30eb-type
- Stroke reference: none

### ja-char-katakana-30ec — レ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: re
- Optional romaji: re
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ec-recognize, ja-char-katakana-30ec-type
- Stroke reference: none

### ja-char-katakana-30ed — ロ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: ro
- Optional romaji: ro
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ed-recognize, ja-char-katakana-30ed-type
- Stroke reference: none

### ja-char-katakana-30ef — ワ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: wa
- Optional romaji: wa
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30ef-recognize, ja-char-katakana-30ef-type
- Stroke reference: none

### ja-char-katakana-30f2 — ヲ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: wo
- Optional romaji: wo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30f2-recognize, ja-char-katakana-30f2-type
- Stroke reference: none

### ja-char-katakana-30f3 — ン

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / basic
- Contextual readings: n
- Optional romaji: n
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-char-katakana-30f3-recognize, ja-char-katakana-30f3-type, ja-contrast-n
- Stroke reference: none

### ja-char-katakana-30ac — ガ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: ga
- Optional romaji: ga
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30ae — ギ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: gi
- Optional romaji: gi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30b0 — グ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: gu
- Optional romaji: gu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30b2 — ゲ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: ge
- Optional romaji: ge
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30b4 — ゴ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: go
- Optional romaji: go
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30b6 — ザ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: za
- Optional romaji: za
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30b8 — ジ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: ji
- Optional romaji: ji
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30ba — ズ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: zu
- Optional romaji: zu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30bc — ゼ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: ze
- Optional romaji: ze
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30be — ゾ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: zo
- Optional romaji: zo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30c0 — ダ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: da
- Optional romaji: da
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30c2 — ヂ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: ji
- Optional romaji: ji
- Context/notes:  This is a d-row voiced form. A shared romanization does not make spellings interchangeable; learn their word context.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30c5 — ヅ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: zu
- Optional romaji: zu
- Context/notes:  This is a d-row voiced form. A shared romanization does not make spellings interchangeable; learn their word context.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30c7 — デ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: de
- Optional romaji: de
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30c9 — ド

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: do
- Optional romaji: do
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d0 — バ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: ba
- Optional romaji: ba
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d3 — ビ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: bi
- Optional romaji: bi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d6 — ブ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: bu
- Optional romaji: bu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d9 — ベ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: be
- Optional romaji: be
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30dc — ボ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / voiced
- Contextual readings: bo
- Optional romaji: bo
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d1 — パ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / semi_voiced
- Contextual readings: pa
- Optional romaji: pa
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d4 — ピ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / semi_voiced
- Contextual readings: pi
- Optional romaji: pi
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30d7 — プ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / semi_voiced
- Contextual readings: pu
- Optional romaji: pu
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30da — ペ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / semi_voiced
- Contextual readings: pe
- Optional romaji: pe
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30dd — ポ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / semi_voiced
- Contextual readings: po
- Optional romaji: po
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-voicing, ja-contrast-similar-shi, ja-contrast-similar-so
- Stroke reference: none

### ja-char-katakana-30ad30e3 — キャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: kya
- Optional romaji: kya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ad, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ad30e5 — キュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: kyu
- Optional romaji: kyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ad, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ad30e7 — キョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: kyo
- Optional romaji: kyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ad, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ae30e3 — ギャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: gya
- Optional romaji: gya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ae, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ae30e5 — ギュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: gyu
- Optional romaji: gyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ae, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ae30e7 — ギョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: gyo
- Optional romaji: gyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ae, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30b730e3 — シャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: sha
- Optional romaji: sha
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30b7, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30b730e5 — シュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: shu
- Optional romaji: shu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30b7, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30b730e7 — ショ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: sho
- Optional romaji: sho
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30b7, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30b830e3 — ジャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: ja
- Optional romaji: ja
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30b8, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30b830e5 — ジュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: ju
- Optional romaji: ju
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30b8, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30b830e7 — ジョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: jo
- Optional romaji: jo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30b8, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30c130e3 — チャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: cha
- Optional romaji: cha
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30c1, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30c130e5 — チュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: chu
- Optional romaji: chu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30c1, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30c130e7 — チョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: cho
- Optional romaji: cho
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30c1, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30cb30e3 — ニャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: nya
- Optional romaji: nya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30cb, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30cb30e5 — ニュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: nyu
- Optional romaji: nyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30cb, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30cb30e7 — ニョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: nyo
- Optional romaji: nyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30cb, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d230e3 — ヒャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: hya
- Optional romaji: hya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d2, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d230e5 — ヒュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: hyu
- Optional romaji: hyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d2, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d230e7 — ヒョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: hyo
- Optional romaji: hyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d2, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d330e3 — ビャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: bya
- Optional romaji: bya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d3, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d330e5 — ビュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: byu
- Optional romaji: byu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d3, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d330e7 — ビョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: byo
- Optional romaji: byo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d3, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d430e3 — ピャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: pya
- Optional romaji: pya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d4, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d430e5 — ピュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: pyu
- Optional romaji: pyu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d4, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30d430e7 — ピョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: pyo
- Optional romaji: pyo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30d4, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30df30e3 — ミャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: mya
- Optional romaji: mya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30df, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30df30e5 — ミュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: myu
- Optional romaji: myu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30df, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30df30e7 — ミョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: myo
- Optional romaji: myo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30df, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ea30e3 — リャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: rya
- Optional romaji: rya
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ea, ja-char-katakana-30e3
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ea30e5 — リュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: ryu
- Optional romaji: ryu
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ea, ja-char-katakana-30e5
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30ea30e7 — リョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / combination
- Contextual readings: ryo
- Optional romaji: ryo
- Context/notes:  The second kana is small. Keep it distinct from the two full-size kana sequence.
- Component IDs: ja-char-katakana-30ea, ja-char-katakana-30e7
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30a1 — ァ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ァ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30a3 — ィ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ィ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30a5 — ゥ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ゥ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30a7 — ェ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ェ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30a9 — ォ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ォ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30e3 — ャ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ャ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30e5 — ュ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ュ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30e7 — ョ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ョ
- Optional romaji: none
- Context/notes:  
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-katakana-30c3 — ッ

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / small
- Contextual readings: ッ
- Optional romaji: none
- Context/notes:  Small tsu marks a following consonant closure/doubling in taught contexts; it is distinct from full-size tsu.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-small-ya, ja-contrast-small-tsu
- Stroke reference: none

### ja-char-long-mark — ー

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / katakana / mark
- Contextual readings: long-vowel mark
- Optional romaji: none
- Context/notes: Lengthens the preceding vowel in katakana Read it as vowel length, not a separate syllable. Example: コーヒー.
- Component IDs: 
- Vocabulary: 
- Drills: ja-contrast-long-vowel, ja-contrast-long-mark
- Stroke reference: none

### ja-kanji-65e5 — 日

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 日本（にほん） | 日曜日（にちようび） | 月曜日（げつようび） | 火曜日（かようび） | 水曜日（すいようび） | 木曜日（もくようび） | 金曜日（きんようび） | 土曜日（どようび）
- Optional romaji: none
- Context/notes: Contextual words: Japan, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-japan, ja-word-sunday, ja-word-monday, ja-word-tuesday, ja-word-wednesday, ja-word-thursday, ja-word-friday, ja-word-saturday
- Drills: ja-reading-japan, ja-reading-sunday, ja-reading-monday, ja-reading-tuesday, ja-reading-wednesday, ja-reading-thursday, ja-reading-friday, ja-reading-saturday
- Stroke reference: ja-stroke-65e5-v1

### ja-kanji-672c — 本

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 日本（にほん） | 本（ほん）
- Optional romaji: none
- Context/notes: Contextual words: Japan, book Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-japan, ja-word-book
- Drills: ja-reading-japan, ja-reading-book
- Stroke reference: none

### ja-kanji-66dc — 曜

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 日曜日（にちようび） | 月曜日（げつようび） | 火曜日（かようび） | 水曜日（すいようび） | 木曜日（もくようび） | 金曜日（きんようび） | 土曜日（どようび）
- Optional romaji: none
- Context/notes: Contextual words: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-sunday, ja-word-monday, ja-word-tuesday, ja-word-wednesday, ja-word-thursday, ja-word-friday, ja-word-saturday
- Drills: ja-reading-sunday, ja-reading-monday, ja-reading-tuesday, ja-reading-wednesday, ja-reading-thursday, ja-reading-friday, ja-reading-saturday
- Stroke reference: none

### ja-kanji-6c34 — 水

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 水（みず） | 水曜日（すいようび）
- Optional romaji: none
- Context/notes: Contextual words: water, Wednesday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-water, ja-word-wednesday
- Drills: ja-reading-water, ja-reading-wednesday
- Stroke reference: none

### ja-kanji-8336 — 茶

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: お茶（おちゃ）
- Optional romaji: none
- Context/notes: Contextual words: tea Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-tea
- Drills: ja-reading-tea
- Stroke reference: none

### ja-kanji-99c5 — 駅

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 駅（えき）
- Optional romaji: none
- Context/notes: Contextual words: station Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-station
- Drills: ja-reading-station
- Stroke reference: none

### ja-kanji-5165 — 入

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 入口（いりぐち）
- Optional romaji: none
- Context/notes: Contextual words: entrance Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-entrance
- Drills: ja-reading-entrance
- Stroke reference: ja-stroke-5165-v1

### ja-kanji-53e3 — 口

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 入口（いりぐち） | 出口（でぐち）
- Optional romaji: none
- Context/notes: Contextual words: entrance, exit Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-entrance, ja-word-exit
- Drills: ja-reading-entrance, ja-reading-exit
- Stroke reference: ja-stroke-53e3-v1

### ja-kanji-51fa — 出

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 出口（でぐち）
- Optional romaji: none
- Context/notes: Contextual words: exit Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-exit
- Drills: ja-reading-exit
- Stroke reference: none

### ja-kanji-5b66 — 学

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 学校（がっこう）
- Optional romaji: none
- Context/notes: Contextual words: school Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-school-kanji
- Drills: ja-reading-school-kanji
- Stroke reference: none

### ja-kanji-6821 — 校

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 学校（がっこう）
- Optional romaji: none
- Context/notes: Contextual words: school Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-school-kanji
- Drills: ja-reading-school-kanji
- Stroke reference: none

### ja-kanji-6642 — 時

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 時間（じかん）
- Optional romaji: none
- Context/notes: Contextual words: time Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-time
- Drills: ja-reading-time
- Stroke reference: none

### ja-kanji-9593 — 間

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 時間（じかん）
- Optional romaji: none
- Context/notes: Contextual words: time Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-time
- Drills: ja-reading-time
- Stroke reference: none

### ja-kanji-6708 — 月

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 月曜日（げつようび）
- Optional romaji: none
- Context/notes: Contextual words: Monday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-monday
- Drills: ja-reading-monday
- Stroke reference: none

### ja-kanji-706b — 火

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 火曜日（かようび）
- Optional romaji: none
- Context/notes: Contextual words: Tuesday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-tuesday
- Drills: ja-reading-tuesday
- Stroke reference: none

### ja-kanji-6728 — 木

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 木曜日（もくようび）
- Optional romaji: none
- Context/notes: Contextual words: Thursday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-thursday
- Drills: ja-reading-thursday
- Stroke reference: none

### ja-kanji-91d1 — 金

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 金曜日（きんようび）
- Optional romaji: none
- Context/notes: Contextual words: Friday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-friday
- Drills: ja-reading-friday
- Stroke reference: none

### ja-kanji-571f — 土

- [ ] Qualified reading/stroke review; notes: pending
- Status/script/form: draft / kanji / kanji
- Contextual readings: 土曜日（どようび）
- Optional romaji: none
- Context/notes: Contextual words: Saturday Read this character inside the listed whole words. These are contextual examples, not a list of every reading.
- Component IDs: 
- Vocabulary: ja-word-saturday
- Drills: ja-reading-saturday
- Stroke reference: none

## Standalone draft practice keys

#### ja-char-a-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for a.
- Prompt: Choose the hiragana for a.
- Choices: c0: あ | c1: い | c2: く
- Expected/accepted: あ [c0]
- Explanation: The taught hiragana form for a is あ.
- Hint: Look for the taught hiragana form for a.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-a-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for a.
- Prompt: Type the hiragana for a.
- Expected/accepted: あ
- Explanation: The taught hiragana form for a is あ.
- Hint: Look for the taught hiragana form for a.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3044-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for i.
- Prompt: Choose the hiragana for i.
- Choices: c0: う | c1: け | c2: い
- Expected/accepted: い [c2]
- Explanation: The taught hiragana form for i is い.
- Hint: Look for the taught hiragana form for i.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3044-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for i.
- Prompt: Type the hiragana for i.
- Expected/accepted: い
- Explanation: The taught hiragana form for i is い.
- Hint: Look for the taught hiragana form for i.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3046-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for u.
- Prompt: Choose the hiragana for u.
- Choices: c0: こ | c1: う | c2: え
- Expected/accepted: う [c1]
- Explanation: The taught hiragana form for u is う.
- Hint: Look for the taught hiragana form for u.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3046-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for u.
- Prompt: Type the hiragana for u.
- Expected/accepted: う
- Explanation: The taught hiragana form for u is う.
- Hint: Look for the taught hiragana form for u.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3048-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for e.
- Prompt: Choose the hiragana for e.
- Choices: c0: え | c1: お | c2: さ
- Expected/accepted: え [c0]
- Explanation: The taught hiragana form for e is え.
- Hint: Look for the taught hiragana form for e.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3048-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for e.
- Prompt: Type the hiragana for e.
- Expected/accepted: え
- Explanation: The taught hiragana form for e is え.
- Hint: Look for the taught hiragana form for e.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-304a-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for o.
- Prompt: Choose the hiragana for o.
- Choices: c0: か | c1: し | c2: お
- Expected/accepted: お [c2]
- Explanation: The taught hiragana form for o is お.
- Hint: Look for the taught hiragana form for o.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-304a-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for o.
- Prompt: Type the hiragana for o.
- Expected/accepted: お
- Explanation: The taught hiragana form for o is お.
- Hint: Look for the taught hiragana form for o.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-304b-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ka.
- Prompt: Choose the hiragana for ka.
- Choices: c0: す | c1: か | c2: き
- Expected/accepted: か [c1]
- Explanation: The taught hiragana form for ka is か.
- Hint: Look for the taught hiragana form for ka.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-304b-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ka.
- Prompt: Type the hiragana for ka.
- Expected/accepted: か
- Explanation: The taught hiragana form for ka is か.
- Hint: Look for the taught hiragana form for ka.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-304d-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ki.
- Prompt: Choose the hiragana for ki.
- Choices: c0: き | c1: く | c2: せ
- Expected/accepted: き [c0]
- Explanation: The taught hiragana form for ki is き.
- Hint: Look for the taught hiragana form for ki.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-304d-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ki.
- Prompt: Type the hiragana for ki.
- Expected/accepted: き
- Explanation: The taught hiragana form for ki is き.
- Hint: Look for the taught hiragana form for ki.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-304f-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ku.
- Prompt: Choose the hiragana for ku.
- Choices: c0: け | c1: そ | c2: く
- Expected/accepted: く [c2]
- Explanation: The taught hiragana form for ku is く.
- Hint: Look for the taught hiragana form for ku.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-304f-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ku.
- Prompt: Type the hiragana for ku.
- Expected/accepted: く
- Explanation: The taught hiragana form for ku is く.
- Hint: Look for the taught hiragana form for ku.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3051-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ke.
- Prompt: Choose the hiragana for ke.
- Choices: c0: た | c1: け | c2: こ
- Expected/accepted: け [c1]
- Explanation: The taught hiragana form for ke is け.
- Hint: Look for the taught hiragana form for ke.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3051-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ke.
- Prompt: Type the hiragana for ke.
- Expected/accepted: け
- Explanation: The taught hiragana form for ke is け.
- Hint: Look for the taught hiragana form for ke.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3053-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ko.
- Prompt: Choose the hiragana for ko.
- Choices: c0: こ | c1: さ | c2: ち
- Expected/accepted: こ [c0]
- Explanation: The taught hiragana form for ko is こ.
- Hint: Look for the taught hiragana form for ko.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3053-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ko.
- Prompt: Type the hiragana for ko.
- Expected/accepted: こ
- Explanation: The taught hiragana form for ko is こ.
- Hint: Look for the taught hiragana form for ko.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3055-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for sa.
- Prompt: Choose the hiragana for sa.
- Choices: c0: し | c1: つ | c2: さ
- Expected/accepted: さ [c2]
- Explanation: The taught hiragana form for sa is さ.
- Hint: Look for the taught hiragana form for sa.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3055-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for sa.
- Prompt: Type the hiragana for sa.
- Expected/accepted: さ
- Explanation: The taught hiragana form for sa is さ.
- Hint: Look for the taught hiragana form for sa.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3057-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for shi.
- Prompt: Choose the hiragana for shi.
- Choices: c0: て | c1: し | c2: す
- Expected/accepted: し [c1]
- Explanation: The taught hiragana form for shi is し.
- Hint: Look for the taught hiragana form for shi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3057-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for shi.
- Prompt: Type the hiragana for shi.
- Expected/accepted: し
- Explanation: The taught hiragana form for shi is し.
- Hint: Look for the taught hiragana form for shi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3059-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for su.
- Prompt: Choose the hiragana for su.
- Choices: c0: す | c1: せ | c2: と
- Expected/accepted: す [c0]
- Explanation: The taught hiragana form for su is す.
- Hint: Look for the taught hiragana form for su.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3059-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for su.
- Prompt: Type the hiragana for su.
- Expected/accepted: す
- Explanation: The taught hiragana form for su is す.
- Hint: Look for the taught hiragana form for su.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-305b-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for se.
- Prompt: Choose the hiragana for se.
- Choices: c0: そ | c1: な | c2: せ
- Expected/accepted: せ [c2]
- Explanation: The taught hiragana form for se is せ.
- Hint: Look for the taught hiragana form for se.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-305b-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for se.
- Prompt: Type the hiragana for se.
- Expected/accepted: せ
- Explanation: The taught hiragana form for se is せ.
- Hint: Look for the taught hiragana form for se.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-305d-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for so.
- Prompt: Choose the hiragana for so.
- Choices: c0: に | c1: そ | c2: た
- Expected/accepted: そ [c1]
- Explanation: The taught hiragana form for so is そ.
- Hint: Look for the taught hiragana form for so.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-305d-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for so.
- Prompt: Type the hiragana for so.
- Expected/accepted: そ
- Explanation: The taught hiragana form for so is そ.
- Hint: Look for the taught hiragana form for so.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-305f-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ta.
- Prompt: Choose the hiragana for ta.
- Choices: c0: た | c1: ち | c2: ぬ
- Expected/accepted: た [c0]
- Explanation: The taught hiragana form for ta is た.
- Hint: Look for the taught hiragana form for ta.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-305f-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ta.
- Prompt: Type the hiragana for ta.
- Expected/accepted: た
- Explanation: The taught hiragana form for ta is た.
- Hint: Look for the taught hiragana form for ta.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3061-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for chi.
- Prompt: Choose the hiragana for chi.
- Choices: c0: つ | c1: ね | c2: ち
- Expected/accepted: ち [c2]
- Explanation: The taught hiragana form for chi is ち.
- Hint: Look for the taught hiragana form for chi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3061-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for chi.
- Prompt: Type the hiragana for chi.
- Expected/accepted: ち
- Explanation: The taught hiragana form for chi is ち.
- Hint: Look for the taught hiragana form for chi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3064-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for tsu.
- Prompt: Choose the hiragana for tsu.
- Choices: c0: の | c1: つ | c2: て
- Expected/accepted: つ [c1]
- Explanation: The taught hiragana form for tsu is つ.
- Hint: Look for the taught hiragana form for tsu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3064-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for tsu.
- Prompt: Type the hiragana for tsu.
- Expected/accepted: つ
- Explanation: The taught hiragana form for tsu is つ.
- Hint: Look for the taught hiragana form for tsu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3066-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for te.
- Prompt: Choose the hiragana for te.
- Choices: c0: て | c1: と | c2: は
- Expected/accepted: て [c0]
- Explanation: The taught hiragana form for te is て.
- Hint: Look for the taught hiragana form for te.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3066-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for te.
- Prompt: Type the hiragana for te.
- Expected/accepted: て
- Explanation: The taught hiragana form for te is て.
- Hint: Look for the taught hiragana form for te.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3068-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for to.
- Prompt: Choose the hiragana for to.
- Choices: c0: な | c1: ひ | c2: と
- Expected/accepted: と [c2]
- Explanation: The taught hiragana form for to is と.
- Hint: Look for the taught hiragana form for to.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3068-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for to.
- Prompt: Type the hiragana for to.
- Expected/accepted: と
- Explanation: The taught hiragana form for to is と.
- Hint: Look for the taught hiragana form for to.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-306a-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for na.
- Prompt: Choose the hiragana for na.
- Choices: c0: ふ | c1: な | c2: に
- Expected/accepted: な [c1]
- Explanation: The taught hiragana form for na is な.
- Hint: Look for the taught hiragana form for na.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-306a-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for na.
- Prompt: Type the hiragana for na.
- Expected/accepted: な
- Explanation: The taught hiragana form for na is な.
- Hint: Look for the taught hiragana form for na.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-306b-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ni.
- Prompt: Choose the hiragana for ni.
- Choices: c0: に | c1: ぬ | c2: へ
- Expected/accepted: に [c0]
- Explanation: The taught hiragana form for ni is に.
- Hint: Look for the taught hiragana form for ni.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-306b-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ni.
- Prompt: Type the hiragana for ni.
- Expected/accepted: に
- Explanation: The taught hiragana form for ni is に.
- Hint: Look for the taught hiragana form for ni.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-306c-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for nu.
- Prompt: Choose the hiragana for nu.
- Choices: c0: ね | c1: ほ | c2: ぬ
- Expected/accepted: ぬ [c2]
- Explanation: The taught hiragana form for nu is ぬ.
- Hint: Look for the taught hiragana form for nu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-306c-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for nu.
- Prompt: Type the hiragana for nu.
- Expected/accepted: ぬ
- Explanation: The taught hiragana form for nu is ぬ.
- Hint: Look for the taught hiragana form for nu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-306d-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ne.
- Prompt: Choose the hiragana for ne.
- Choices: c0: ま | c1: ね | c2: の
- Expected/accepted: ね [c1]
- Explanation: The taught hiragana form for ne is ね.
- Hint: Look for the taught hiragana form for ne.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-306d-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ne.
- Prompt: Type the hiragana for ne.
- Expected/accepted: ね
- Explanation: The taught hiragana form for ne is ね.
- Hint: Look for the taught hiragana form for ne.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-306e-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for no.
- Prompt: Choose the hiragana for no.
- Choices: c0: の | c1: は | c2: み
- Expected/accepted: の [c0]
- Explanation: The taught hiragana form for no is の.
- Hint: Look for the taught hiragana form for no.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-306e-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for no.
- Prompt: Type the hiragana for no.
- Expected/accepted: の
- Explanation: The taught hiragana form for no is の.
- Hint: Look for the taught hiragana form for no.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-306f-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ha.
- Prompt: Choose the hiragana for ha.
- Choices: c0: ひ | c1: む | c2: は
- Expected/accepted: は [c2]
- Explanation: The taught hiragana form for ha is は.
- Hint: Look for the taught hiragana form for ha.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-306f-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ha.
- Prompt: Type the hiragana for ha.
- Expected/accepted: は
- Explanation: The taught hiragana form for ha is は.
- Hint: Look for the taught hiragana form for ha.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3072-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for hi.
- Prompt: Choose the hiragana for hi.
- Choices: c0: め | c1: ひ | c2: ふ
- Expected/accepted: ひ [c1]
- Explanation: The taught hiragana form for hi is ひ.
- Hint: Look for the taught hiragana form for hi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3072-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for hi.
- Prompt: Type the hiragana for hi.
- Expected/accepted: ひ
- Explanation: The taught hiragana form for hi is ひ.
- Hint: Look for the taught hiragana form for hi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3075-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for fu.
- Prompt: Choose the hiragana for fu.
- Choices: c0: ふ | c1: へ | c2: も
- Expected/accepted: ふ [c0]
- Explanation: The taught hiragana form for fu is ふ.
- Hint: Look for the taught hiragana form for fu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3075-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for fu.
- Prompt: Type the hiragana for fu.
- Expected/accepted: ふ
- Explanation: The taught hiragana form for fu is ふ.
- Hint: Look for the taught hiragana form for fu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3078-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for he.
- Prompt: Choose the hiragana for he.
- Choices: c0: ほ | c1: や | c2: へ
- Expected/accepted: へ [c2]
- Explanation: The taught hiragana form for he is へ.
- Hint: Look for the taught hiragana form for he.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3078-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for he.
- Prompt: Type the hiragana for he.
- Expected/accepted: へ
- Explanation: The taught hiragana form for he is へ.
- Hint: Look for the taught hiragana form for he.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-307b-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ho.
- Prompt: Choose the hiragana for ho.
- Choices: c0: ゆ | c1: ほ | c2: ま
- Expected/accepted: ほ [c1]
- Explanation: The taught hiragana form for ho is ほ.
- Hint: Look for the taught hiragana form for ho.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-307b-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ho.
- Prompt: Type the hiragana for ho.
- Expected/accepted: ほ
- Explanation: The taught hiragana form for ho is ほ.
- Hint: Look for the taught hiragana form for ho.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-307e-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ma.
- Prompt: Choose the hiragana for ma.
- Choices: c0: ま | c1: み | c2: よ
- Expected/accepted: ま [c0]
- Explanation: The taught hiragana form for ma is ま.
- Hint: Look for the taught hiragana form for ma.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-307e-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ma.
- Prompt: Type the hiragana for ma.
- Expected/accepted: ま
- Explanation: The taught hiragana form for ma is ま.
- Hint: Look for the taught hiragana form for ma.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-307f-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for mi.
- Prompt: Choose the hiragana for mi.
- Choices: c0: む | c1: ら | c2: み
- Expected/accepted: み [c2]
- Explanation: The taught hiragana form for mi is み.
- Hint: Look for the taught hiragana form for mi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-307f-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for mi.
- Prompt: Type the hiragana for mi.
- Expected/accepted: み
- Explanation: The taught hiragana form for mi is み.
- Hint: Look for the taught hiragana form for mi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3080-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for mu.
- Prompt: Choose the hiragana for mu.
- Choices: c0: り | c1: む | c2: め
- Expected/accepted: む [c1]
- Explanation: The taught hiragana form for mu is む.
- Hint: Look for the taught hiragana form for mu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3080-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for mu.
- Prompt: Type the hiragana for mu.
- Expected/accepted: む
- Explanation: The taught hiragana form for mu is む.
- Hint: Look for the taught hiragana form for mu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3081-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for me.
- Prompt: Choose the hiragana for me.
- Choices: c0: め | c1: も | c2: る
- Expected/accepted: め [c0]
- Explanation: The taught hiragana form for me is め.
- Hint: Look for the taught hiragana form for me.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3081-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for me.
- Prompt: Type the hiragana for me.
- Expected/accepted: め
- Explanation: The taught hiragana form for me is め.
- Hint: Look for the taught hiragana form for me.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3082-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for mo.
- Prompt: Choose the hiragana for mo.
- Choices: c0: や | c1: れ | c2: も
- Expected/accepted: も [c2]
- Explanation: The taught hiragana form for mo is も.
- Hint: Look for the taught hiragana form for mo.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3082-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for mo.
- Prompt: Type the hiragana for mo.
- Expected/accepted: も
- Explanation: The taught hiragana form for mo is も.
- Hint: Look for the taught hiragana form for mo.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3084-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ya.
- Prompt: Choose the hiragana for ya.
- Choices: c0: ろ | c1: や | c2: ゆ
- Expected/accepted: や [c1]
- Explanation: The taught hiragana form for ya is や.
- Hint: Look for the taught hiragana form for ya.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3084-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ya.
- Prompt: Type the hiragana for ya.
- Expected/accepted: や
- Explanation: The taught hiragana form for ya is や.
- Hint: Look for the taught hiragana form for ya.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3086-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for yu.
- Prompt: Choose the hiragana for yu.
- Choices: c0: ゆ | c1: よ | c2: わ
- Expected/accepted: ゆ [c0]
- Explanation: The taught hiragana form for yu is ゆ.
- Hint: Look for the taught hiragana form for yu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3086-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for yu.
- Prompt: Type the hiragana for yu.
- Expected/accepted: ゆ
- Explanation: The taught hiragana form for yu is ゆ.
- Hint: Look for the taught hiragana form for yu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3088-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for yo.
- Prompt: Choose the hiragana for yo.
- Choices: c0: ら | c1: を | c2: よ
- Expected/accepted: よ [c2]
- Explanation: The taught hiragana form for yo is よ.
- Hint: Look for the taught hiragana form for yo.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3088-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for yo.
- Prompt: Type the hiragana for yo.
- Expected/accepted: よ
- Explanation: The taught hiragana form for yo is よ.
- Hint: Look for the taught hiragana form for yo.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3089-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ra.
- Prompt: Choose the hiragana for ra.
- Choices: c0: ん | c1: ら | c2: り
- Expected/accepted: ら [c1]
- Explanation: The taught hiragana form for ra is ら.
- Hint: Look for the taught hiragana form for ra.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3089-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ra.
- Prompt: Type the hiragana for ra.
- Expected/accepted: ら
- Explanation: The taught hiragana form for ra is ら.
- Hint: Look for the taught hiragana form for ra.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-308a-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ri.
- Prompt: Choose the hiragana for ri.
- Choices: c0: り | c1: る | c2: あ
- Expected/accepted: り [c0]
- Explanation: The taught hiragana form for ri is り.
- Hint: Look for the taught hiragana form for ri.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-308a-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ri.
- Prompt: Type the hiragana for ri.
- Expected/accepted: り
- Explanation: The taught hiragana form for ri is り.
- Hint: Look for the taught hiragana form for ri.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-308b-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ru.
- Prompt: Choose the hiragana for ru.
- Choices: c0: れ | c1: い | c2: る
- Expected/accepted: る [c2]
- Explanation: The taught hiragana form for ru is る.
- Hint: Look for the taught hiragana form for ru.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-308b-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ru.
- Prompt: Type the hiragana for ru.
- Expected/accepted: る
- Explanation: The taught hiragana form for ru is る.
- Hint: Look for the taught hiragana form for ru.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-308c-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for re.
- Prompt: Choose the hiragana for re.
- Choices: c0: う | c1: れ | c2: ろ
- Expected/accepted: れ [c1]
- Explanation: The taught hiragana form for re is れ.
- Hint: Look for the taught hiragana form for re.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-308c-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for re.
- Prompt: Type the hiragana for re.
- Expected/accepted: れ
- Explanation: The taught hiragana form for re is れ.
- Hint: Look for the taught hiragana form for re.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-308d-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for ro.
- Prompt: Choose the hiragana for ro.
- Choices: c0: ろ | c1: わ | c2: え
- Expected/accepted: ろ [c0]
- Explanation: The taught hiragana form for ro is ろ.
- Hint: Look for the taught hiragana form for ro.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-308d-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for ro.
- Prompt: Type the hiragana for ro.
- Expected/accepted: ろ
- Explanation: The taught hiragana form for ro is ろ.
- Hint: Look for the taught hiragana form for ro.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-308f-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for wa.
- Prompt: Choose the hiragana for wa.
- Choices: c0: を | c1: お | c2: わ
- Expected/accepted: わ [c2]
- Explanation: The taught hiragana form for wa is わ.
- Hint: Look for the taught hiragana form for wa.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-308f-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for wa.
- Prompt: Type the hiragana for wa.
- Expected/accepted: わ
- Explanation: The taught hiragana form for wa is わ.
- Hint: Look for the taught hiragana form for wa.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3092-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for wo.
- Prompt: Choose the hiragana for wo.
- Choices: c0: か | c1: を | c2: ん
- Expected/accepted: を [c1]
- Explanation: The taught hiragana form for wo is を.
- Hint: Look for the taught hiragana form for wo.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3092-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for wo.
- Prompt: Type the hiragana for wo.
- Expected/accepted: を
- Explanation: The taught hiragana form for wo is を.
- Hint: Look for the taught hiragana form for wo.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-hiragana-3093-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the hiragana form for n.
- Prompt: Choose the hiragana for n.
- Choices: c0: ん | c1: あ | c2: き
- Expected/accepted: ん [c0]
- Explanation: The taught hiragana form for n is ん.
- Hint: Look for the taught hiragana form for n.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-hiragana-3093-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the hiragana form for n.
- Prompt: Type the hiragana for n.
- Expected/accepted: ん
- Explanation: The taught hiragana form for n is ん.
- Hint: Look for the taught hiragana form for n.
- Concepts: kana
- Policy: {"strategy":"exact","script":"hiragana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30a2-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for a.
- Prompt: Choose the katakana for a.
- Choices: c0: ア | c1: イ | c2: ク
- Expected/accepted: ア [c0]
- Explanation: The taught katakana form for a is ア.
- Hint: Look for the taught katakana form for a.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30a2-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for a.
- Prompt: Type the katakana for a.
- Expected/accepted: ア
- Explanation: The taught katakana form for a is ア.
- Hint: Look for the taught katakana form for a.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30a4-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for i.
- Prompt: Choose the katakana for i.
- Choices: c0: ウ | c1: ケ | c2: イ
- Expected/accepted: イ [c2]
- Explanation: The taught katakana form for i is イ.
- Hint: Look for the taught katakana form for i.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30a4-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for i.
- Prompt: Type the katakana for i.
- Expected/accepted: イ
- Explanation: The taught katakana form for i is イ.
- Hint: Look for the taught katakana form for i.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30a6-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for u.
- Prompt: Choose the katakana for u.
- Choices: c0: コ | c1: ウ | c2: エ
- Expected/accepted: ウ [c1]
- Explanation: The taught katakana form for u is ウ.
- Hint: Look for the taught katakana form for u.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30a6-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for u.
- Prompt: Type the katakana for u.
- Expected/accepted: ウ
- Explanation: The taught katakana form for u is ウ.
- Hint: Look for the taught katakana form for u.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30a8-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for e.
- Prompt: Choose the katakana for e.
- Choices: c0: エ | c1: オ | c2: サ
- Expected/accepted: エ [c0]
- Explanation: The taught katakana form for e is エ.
- Hint: Look for the taught katakana form for e.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30a8-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for e.
- Prompt: Type the katakana for e.
- Expected/accepted: エ
- Explanation: The taught katakana form for e is エ.
- Hint: Look for the taught katakana form for e.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30aa-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for o.
- Prompt: Choose the katakana for o.
- Choices: c0: カ | c1: シ | c2: オ
- Expected/accepted: オ [c2]
- Explanation: The taught katakana form for o is オ.
- Hint: Look for the taught katakana form for o.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30aa-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for o.
- Prompt: Type the katakana for o.
- Expected/accepted: オ
- Explanation: The taught katakana form for o is オ.
- Hint: Look for the taught katakana form for o.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ab-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ka.
- Prompt: Choose the katakana for ka.
- Choices: c0: ス | c1: カ | c2: キ
- Expected/accepted: カ [c1]
- Explanation: The taught katakana form for ka is カ.
- Hint: Look for the taught katakana form for ka.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ab-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ka.
- Prompt: Type the katakana for ka.
- Expected/accepted: カ
- Explanation: The taught katakana form for ka is カ.
- Hint: Look for the taught katakana form for ka.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ad-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ki.
- Prompt: Choose the katakana for ki.
- Choices: c0: キ | c1: ク | c2: セ
- Expected/accepted: キ [c0]
- Explanation: The taught katakana form for ki is キ.
- Hint: Look for the taught katakana form for ki.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ad-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ki.
- Prompt: Type the katakana for ki.
- Expected/accepted: キ
- Explanation: The taught katakana form for ki is キ.
- Hint: Look for the taught katakana form for ki.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30af-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ku.
- Prompt: Choose the katakana for ku.
- Choices: c0: ケ | c1: ソ | c2: ク
- Expected/accepted: ク [c2]
- Explanation: The taught katakana form for ku is ク.
- Hint: Look for the taught katakana form for ku.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30af-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ku.
- Prompt: Type the katakana for ku.
- Expected/accepted: ク
- Explanation: The taught katakana form for ku is ク.
- Hint: Look for the taught katakana form for ku.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30b1-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ke.
- Prompt: Choose the katakana for ke.
- Choices: c0: タ | c1: ケ | c2: コ
- Expected/accepted: ケ [c1]
- Explanation: The taught katakana form for ke is ケ.
- Hint: Look for the taught katakana form for ke.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30b1-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ke.
- Prompt: Type the katakana for ke.
- Expected/accepted: ケ
- Explanation: The taught katakana form for ke is ケ.
- Hint: Look for the taught katakana form for ke.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30b3-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ko.
- Prompt: Choose the katakana for ko.
- Choices: c0: コ | c1: サ | c2: チ
- Expected/accepted: コ [c0]
- Explanation: The taught katakana form for ko is コ.
- Hint: Look for the taught katakana form for ko.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30b3-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ko.
- Prompt: Type the katakana for ko.
- Expected/accepted: コ
- Explanation: The taught katakana form for ko is コ.
- Hint: Look for the taught katakana form for ko.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30b5-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for sa.
- Prompt: Choose the katakana for sa.
- Choices: c0: シ | c1: ツ | c2: サ
- Expected/accepted: サ [c2]
- Explanation: The taught katakana form for sa is サ.
- Hint: Look for the taught katakana form for sa.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30b5-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for sa.
- Prompt: Type the katakana for sa.
- Expected/accepted: サ
- Explanation: The taught katakana form for sa is サ.
- Hint: Look for the taught katakana form for sa.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30b7-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for shi.
- Prompt: Choose the katakana for shi.
- Choices: c0: テ | c1: シ | c2: ス
- Expected/accepted: シ [c1]
- Explanation: The taught katakana form for shi is シ.
- Hint: Look for the taught katakana form for shi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30b7-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for shi.
- Prompt: Type the katakana for shi.
- Expected/accepted: シ
- Explanation: The taught katakana form for shi is シ.
- Hint: Look for the taught katakana form for shi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30b9-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for su.
- Prompt: Choose the katakana for su.
- Choices: c0: ス | c1: セ | c2: ト
- Expected/accepted: ス [c0]
- Explanation: The taught katakana form for su is ス.
- Hint: Look for the taught katakana form for su.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30b9-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for su.
- Prompt: Type the katakana for su.
- Expected/accepted: ス
- Explanation: The taught katakana form for su is ス.
- Hint: Look for the taught katakana form for su.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30bb-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for se.
- Prompt: Choose the katakana for se.
- Choices: c0: ソ | c1: ナ | c2: セ
- Expected/accepted: セ [c2]
- Explanation: The taught katakana form for se is セ.
- Hint: Look for the taught katakana form for se.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30bb-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for se.
- Prompt: Type the katakana for se.
- Expected/accepted: セ
- Explanation: The taught katakana form for se is セ.
- Hint: Look for the taught katakana form for se.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30bd-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for so.
- Prompt: Choose the katakana for so.
- Choices: c0: ニ | c1: ソ | c2: タ
- Expected/accepted: ソ [c1]
- Explanation: The taught katakana form for so is ソ.
- Hint: Look for the taught katakana form for so.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30bd-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for so.
- Prompt: Type the katakana for so.
- Expected/accepted: ソ
- Explanation: The taught katakana form for so is ソ.
- Hint: Look for the taught katakana form for so.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30bf-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ta.
- Prompt: Choose the katakana for ta.
- Choices: c0: タ | c1: チ | c2: ヌ
- Expected/accepted: タ [c0]
- Explanation: The taught katakana form for ta is タ.
- Hint: Look for the taught katakana form for ta.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30bf-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ta.
- Prompt: Type the katakana for ta.
- Expected/accepted: タ
- Explanation: The taught katakana form for ta is タ.
- Hint: Look for the taught katakana form for ta.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30c1-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for chi.
- Prompt: Choose the katakana for chi.
- Choices: c0: ツ | c1: ネ | c2: チ
- Expected/accepted: チ [c2]
- Explanation: The taught katakana form for chi is チ.
- Hint: Look for the taught katakana form for chi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30c1-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for chi.
- Prompt: Type the katakana for chi.
- Expected/accepted: チ
- Explanation: The taught katakana form for chi is チ.
- Hint: Look for the taught katakana form for chi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30c4-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for tsu.
- Prompt: Choose the katakana for tsu.
- Choices: c0: ノ | c1: ツ | c2: テ
- Expected/accepted: ツ [c1]
- Explanation: The taught katakana form for tsu is ツ.
- Hint: Look for the taught katakana form for tsu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30c4-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for tsu.
- Prompt: Type the katakana for tsu.
- Expected/accepted: ツ
- Explanation: The taught katakana form for tsu is ツ.
- Hint: Look for the taught katakana form for tsu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30c6-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for te.
- Prompt: Choose the katakana for te.
- Choices: c0: テ | c1: ト | c2: ハ
- Expected/accepted: テ [c0]
- Explanation: The taught katakana form for te is テ.
- Hint: Look for the taught katakana form for te.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30c6-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for te.
- Prompt: Type the katakana for te.
- Expected/accepted: テ
- Explanation: The taught katakana form for te is テ.
- Hint: Look for the taught katakana form for te.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30c8-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for to.
- Prompt: Choose the katakana for to.
- Choices: c0: ナ | c1: ヒ | c2: ト
- Expected/accepted: ト [c2]
- Explanation: The taught katakana form for to is ト.
- Hint: Look for the taught katakana form for to.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30c8-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for to.
- Prompt: Type the katakana for to.
- Expected/accepted: ト
- Explanation: The taught katakana form for to is ト.
- Hint: Look for the taught katakana form for to.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ca-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for na.
- Prompt: Choose the katakana for na.
- Choices: c0: フ | c1: ナ | c2: ニ
- Expected/accepted: ナ [c1]
- Explanation: The taught katakana form for na is ナ.
- Hint: Look for the taught katakana form for na.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ca-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for na.
- Prompt: Type the katakana for na.
- Expected/accepted: ナ
- Explanation: The taught katakana form for na is ナ.
- Hint: Look for the taught katakana form for na.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30cb-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ni.
- Prompt: Choose the katakana for ni.
- Choices: c0: ニ | c1: ヌ | c2: ヘ
- Expected/accepted: ニ [c0]
- Explanation: The taught katakana form for ni is ニ.
- Hint: Look for the taught katakana form for ni.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30cb-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ni.
- Prompt: Type the katakana for ni.
- Expected/accepted: ニ
- Explanation: The taught katakana form for ni is ニ.
- Hint: Look for the taught katakana form for ni.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30cc-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for nu.
- Prompt: Choose the katakana for nu.
- Choices: c0: ネ | c1: ホ | c2: ヌ
- Expected/accepted: ヌ [c2]
- Explanation: The taught katakana form for nu is ヌ.
- Hint: Look for the taught katakana form for nu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30cc-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for nu.
- Prompt: Type the katakana for nu.
- Expected/accepted: ヌ
- Explanation: The taught katakana form for nu is ヌ.
- Hint: Look for the taught katakana form for nu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30cd-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ne.
- Prompt: Choose the katakana for ne.
- Choices: c0: マ | c1: ネ | c2: ノ
- Expected/accepted: ネ [c1]
- Explanation: The taught katakana form for ne is ネ.
- Hint: Look for the taught katakana form for ne.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30cd-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ne.
- Prompt: Type the katakana for ne.
- Expected/accepted: ネ
- Explanation: The taught katakana form for ne is ネ.
- Hint: Look for the taught katakana form for ne.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ce-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for no.
- Prompt: Choose the katakana for no.
- Choices: c0: ノ | c1: ハ | c2: ミ
- Expected/accepted: ノ [c0]
- Explanation: The taught katakana form for no is ノ.
- Hint: Look for the taught katakana form for no.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ce-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for no.
- Prompt: Type the katakana for no.
- Expected/accepted: ノ
- Explanation: The taught katakana form for no is ノ.
- Hint: Look for the taught katakana form for no.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30cf-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ha.
- Prompt: Choose the katakana for ha.
- Choices: c0: ヒ | c1: ム | c2: ハ
- Expected/accepted: ハ [c2]
- Explanation: The taught katakana form for ha is ハ.
- Hint: Look for the taught katakana form for ha.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30cf-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ha.
- Prompt: Type the katakana for ha.
- Expected/accepted: ハ
- Explanation: The taught katakana form for ha is ハ.
- Hint: Look for the taught katakana form for ha.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30d2-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for hi.
- Prompt: Choose the katakana for hi.
- Choices: c0: メ | c1: ヒ | c2: フ
- Expected/accepted: ヒ [c1]
- Explanation: The taught katakana form for hi is ヒ.
- Hint: Look for the taught katakana form for hi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30d2-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for hi.
- Prompt: Type the katakana for hi.
- Expected/accepted: ヒ
- Explanation: The taught katakana form for hi is ヒ.
- Hint: Look for the taught katakana form for hi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30d5-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for fu.
- Prompt: Choose the katakana for fu.
- Choices: c0: フ | c1: ヘ | c2: モ
- Expected/accepted: フ [c0]
- Explanation: The taught katakana form for fu is フ.
- Hint: Look for the taught katakana form for fu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30d5-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for fu.
- Prompt: Type the katakana for fu.
- Expected/accepted: フ
- Explanation: The taught katakana form for fu is フ.
- Hint: Look for the taught katakana form for fu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30d8-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for he.
- Prompt: Choose the katakana for he.
- Choices: c0: ホ | c1: ヤ | c2: ヘ
- Expected/accepted: ヘ [c2]
- Explanation: The taught katakana form for he is ヘ.
- Hint: Look for the taught katakana form for he.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30d8-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for he.
- Prompt: Type the katakana for he.
- Expected/accepted: ヘ
- Explanation: The taught katakana form for he is ヘ.
- Hint: Look for the taught katakana form for he.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30db-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ho.
- Prompt: Choose the katakana for ho.
- Choices: c0: ユ | c1: ホ | c2: マ
- Expected/accepted: ホ [c1]
- Explanation: The taught katakana form for ho is ホ.
- Hint: Look for the taught katakana form for ho.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30db-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ho.
- Prompt: Type the katakana for ho.
- Expected/accepted: ホ
- Explanation: The taught katakana form for ho is ホ.
- Hint: Look for the taught katakana form for ho.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30de-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ma.
- Prompt: Choose the katakana for ma.
- Choices: c0: マ | c1: ミ | c2: ヨ
- Expected/accepted: マ [c0]
- Explanation: The taught katakana form for ma is マ.
- Hint: Look for the taught katakana form for ma.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30de-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ma.
- Prompt: Type the katakana for ma.
- Expected/accepted: マ
- Explanation: The taught katakana form for ma is マ.
- Hint: Look for the taught katakana form for ma.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30df-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for mi.
- Prompt: Choose the katakana for mi.
- Choices: c0: ム | c1: ラ | c2: ミ
- Expected/accepted: ミ [c2]
- Explanation: The taught katakana form for mi is ミ.
- Hint: Look for the taught katakana form for mi.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30df-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for mi.
- Prompt: Type the katakana for mi.
- Expected/accepted: ミ
- Explanation: The taught katakana form for mi is ミ.
- Hint: Look for the taught katakana form for mi.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e0-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for mu.
- Prompt: Choose the katakana for mu.
- Choices: c0: リ | c1: ム | c2: メ
- Expected/accepted: ム [c1]
- Explanation: The taught katakana form for mu is ム.
- Hint: Look for the taught katakana form for mu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e0-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for mu.
- Prompt: Type the katakana for mu.
- Expected/accepted: ム
- Explanation: The taught katakana form for mu is ム.
- Hint: Look for the taught katakana form for mu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e1-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for me.
- Prompt: Choose the katakana for me.
- Choices: c0: メ | c1: モ | c2: ル
- Expected/accepted: メ [c0]
- Explanation: The taught katakana form for me is メ.
- Hint: Look for the taught katakana form for me.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e1-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for me.
- Prompt: Type the katakana for me.
- Expected/accepted: メ
- Explanation: The taught katakana form for me is メ.
- Hint: Look for the taught katakana form for me.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e2-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for mo.
- Prompt: Choose the katakana for mo.
- Choices: c0: ヤ | c1: レ | c2: モ
- Expected/accepted: モ [c2]
- Explanation: The taught katakana form for mo is モ.
- Hint: Look for the taught katakana form for mo.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e2-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for mo.
- Prompt: Type the katakana for mo.
- Expected/accepted: モ
- Explanation: The taught katakana form for mo is モ.
- Hint: Look for the taught katakana form for mo.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e4-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ya.
- Prompt: Choose the katakana for ya.
- Choices: c0: ロ | c1: ヤ | c2: ユ
- Expected/accepted: ヤ [c1]
- Explanation: The taught katakana form for ya is ヤ.
- Hint: Look for the taught katakana form for ya.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e4-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ya.
- Prompt: Type the katakana for ya.
- Expected/accepted: ヤ
- Explanation: The taught katakana form for ya is ヤ.
- Hint: Look for the taught katakana form for ya.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e6-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for yu.
- Prompt: Choose the katakana for yu.
- Choices: c0: ユ | c1: ヨ | c2: ワ
- Expected/accepted: ユ [c0]
- Explanation: The taught katakana form for yu is ユ.
- Hint: Look for the taught katakana form for yu.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e6-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for yu.
- Prompt: Type the katakana for yu.
- Expected/accepted: ユ
- Explanation: The taught katakana form for yu is ユ.
- Hint: Look for the taught katakana form for yu.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e8-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for yo.
- Prompt: Choose the katakana for yo.
- Choices: c0: ラ | c1: ヲ | c2: ヨ
- Expected/accepted: ヨ [c2]
- Explanation: The taught katakana form for yo is ヨ.
- Hint: Look for the taught katakana form for yo.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e8-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for yo.
- Prompt: Type the katakana for yo.
- Expected/accepted: ヨ
- Explanation: The taught katakana form for yo is ヨ.
- Hint: Look for the taught katakana form for yo.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30e9-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ra.
- Prompt: Choose the katakana for ra.
- Choices: c0: ン | c1: ラ | c2: リ
- Expected/accepted: ラ [c1]
- Explanation: The taught katakana form for ra is ラ.
- Hint: Look for the taught katakana form for ra.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30e9-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ra.
- Prompt: Type the katakana for ra.
- Expected/accepted: ラ
- Explanation: The taught katakana form for ra is ラ.
- Hint: Look for the taught katakana form for ra.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ea-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ri.
- Prompt: Choose the katakana for ri.
- Choices: c0: リ | c1: ル | c2: ア
- Expected/accepted: リ [c0]
- Explanation: The taught katakana form for ri is リ.
- Hint: Look for the taught katakana form for ri.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ea-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ri.
- Prompt: Type the katakana for ri.
- Expected/accepted: リ
- Explanation: The taught katakana form for ri is リ.
- Hint: Look for the taught katakana form for ri.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30eb-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ru.
- Prompt: Choose the katakana for ru.
- Choices: c0: レ | c1: イ | c2: ル
- Expected/accepted: ル [c2]
- Explanation: The taught katakana form for ru is ル.
- Hint: Look for the taught katakana form for ru.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30eb-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ru.
- Prompt: Type the katakana for ru.
- Expected/accepted: ル
- Explanation: The taught katakana form for ru is ル.
- Hint: Look for the taught katakana form for ru.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ec-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for re.
- Prompt: Choose the katakana for re.
- Choices: c0: ウ | c1: レ | c2: ロ
- Expected/accepted: レ [c1]
- Explanation: The taught katakana form for re is レ.
- Hint: Look for the taught katakana form for re.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ec-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for re.
- Prompt: Type the katakana for re.
- Expected/accepted: レ
- Explanation: The taught katakana form for re is レ.
- Hint: Look for the taught katakana form for re.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ed-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for ro.
- Prompt: Choose the katakana for ro.
- Choices: c0: ロ | c1: ワ | c2: エ
- Expected/accepted: ロ [c0]
- Explanation: The taught katakana form for ro is ロ.
- Hint: Look for the taught katakana form for ro.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ed-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for ro.
- Prompt: Type the katakana for ro.
- Expected/accepted: ロ
- Explanation: The taught katakana form for ro is ロ.
- Hint: Look for the taught katakana form for ro.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30ef-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for wa.
- Prompt: Choose the katakana for wa.
- Choices: c0: ヲ | c1: オ | c2: ワ
- Expected/accepted: ワ [c2]
- Explanation: The taught katakana form for wa is ワ.
- Hint: Look for the taught katakana form for wa.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30ef-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for wa.
- Prompt: Type the katakana for wa.
- Expected/accepted: ワ
- Explanation: The taught katakana form for wa is ワ.
- Hint: Look for the taught katakana form for wa.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30f2-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for wo.
- Prompt: Choose the katakana for wo.
- Choices: c0: カ | c1: ヲ | c2: ン
- Expected/accepted: ヲ [c1]
- Explanation: The taught katakana form for wo is ヲ.
- Hint: Look for the taught katakana form for wo.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30f2-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for wo.
- Prompt: Type the katakana for wo.
- Expected/accepted: ヲ
- Explanation: The taught katakana form for wo is ヲ.
- Hint: Look for the taught katakana form for wo.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-char-katakana-30f3-recognize

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / recognition
- Objective: Recognize and type the katakana form for n.
- Prompt: Choose the katakana for n.
- Choices: c0: ン | c1: ア | c2: キ
- Expected/accepted: ン [c0]
- Explanation: The taught katakana form for n is ン.
- Hint: Look for the taught katakana form for n.
- Concepts: kana
- Policy: {"strategy":"choice"}

#### ja-char-katakana-30f3-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recognize and type the katakana form for n.
- Prompt: Type the katakana for n.
- Expected/accepted: ン
- Explanation: The taught katakana form for n is ン.
- Hint: Look for the taught katakana form for n.
- Concepts: kana
- Policy: {"strategy":"exact","script":"katakana","normalization":"NFC","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-contrast-small-ya

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the spelling with one combined kya sound.
- Prompt: Choose the spelling with one combined kya sound.
- Choices: c0: きや | c1: きゃ | c2: きゅ
- Expected/accepted: きゃ [c1]
- Explanation: きゃ combines き and small ゃ. きや keeps a full-size や.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-small
- Policy: {"strategy":"choice"}

#### ja-contrast-small-tsu

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the word for a postage stamp, with a held consonant.
- Prompt: Choose the word for a postage stamp, with a held consonant.
- Choices: c0: きて | c1: きって | c2: きつて
- Expected/accepted: きって [c1]
- Explanation: きって contains small っ; きて is a different form.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-small
- Policy: {"strategy":"choice"}

#### ja-contrast-n

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the spelling hon, keeping the final ん.
- Prompt: Choose the spelling hon, keeping the final ん.
- Choices: c0: ほ | c1: ほん | c2: ほう
- Expected/accepted: ほん [c1]
- Explanation: ほん keeps the independent ん mora.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-n
- Policy: {"strategy":"choice"}

#### ja-contrast-long-vowel

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the spelling for grandmother (obaasan).
- Prompt: Choose the spelling for grandmother (obaasan).
- Choices: c0: おばさん | c1: おばあさん | c2: おばさ
- Expected/accepted: おばあさん [c1]
- Explanation: おばあさん has a long あ; おばさん means aunt.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-length
- Policy: {"strategy":"choice"}

#### ja-contrast-long-mark

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the standard katakana spelling for coffee.
- Prompt: Choose the standard katakana spelling for coffee.
- Choices: c0: コヒ | c1: コーヒー | c2: コヒー
- Expected/accepted: コーヒー [c1]
- Explanation: コーヒー has two long vowels, each written with ー.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-length
- Policy: {"strategy":"choice"}

#### ja-contrast-voicing

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose ga in hiragana.
- Prompt: Choose ga in hiragana.
- Choices: c0: か | c1: が | c2: ぱ
- Expected/accepted: が [c1]
- Explanation: が keeps the dakuten; か and ぱ are different sounds.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-voicing
- Policy: {"strategy":"choice"}

#### ja-contrast-similar-shi

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose shi in katakana.
- Prompt: Choose shi in katakana.
- Choices: c0: ツ | c1: シ | c2: ン
- Expected/accepted: シ [c1]
- Explanation: シ represents shi; compare its short-stroke direction with ツ.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-voicing
- Policy: {"strategy":"choice"}

#### ja-contrast-similar-so

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose so in katakana.
- Prompt: Choose so in katakana.
- Choices: c0: ン | c1: ソ | c2: ノ
- Expected/accepted: ソ [c1]
- Explanation: ソ represents so. ン represents the independent n mora.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: kana-voicing
- Policy: {"strategy":"choice"}

#### ja-reading-japan

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 日本 (Japan).
- Prompt: Choose the reading of 日本 (Japan).
- Choices: c0: にほん | c1: ここ | c2: かお
- Expected/accepted: にほん [c0]
- Explanation: 日本 is read にほん in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-sunday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 日曜日 (Sunday).
- Prompt: Choose the reading of 日曜日 (Sunday).
- Choices: c0: にちようび | c1: ここ | c2: かお
- Expected/accepted: にちようび [c0]
- Explanation: 日曜日 is read にちようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-water

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 水 (water).
- Prompt: Choose the reading of 水 (water).
- Choices: c0: みず | c1: ここ | c2: かお
- Expected/accepted: みず [c0]
- Explanation: 水 is read みず in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-tea

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of お茶 (tea).
- Prompt: Choose the reading of お茶 (tea).
- Choices: c0: おちゃ | c1: ここ | c2: かお
- Expected/accepted: おちゃ [c0]
- Explanation: お茶 is read おちゃ in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-station

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 駅 (station).
- Prompt: Choose the reading of 駅 (station).
- Choices: c0: えき | c1: ここ | c2: かお
- Expected/accepted: えき [c0]
- Explanation: 駅 is read えき in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-entrance

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 入口 (entrance).
- Prompt: Choose the reading of 入口 (entrance).
- Choices: c0: いりぐち | c1: ここ | c2: かお
- Expected/accepted: いりぐち [c0]
- Explanation: 入口 is read いりぐち in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-exit

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 出口 (exit).
- Prompt: Choose the reading of 出口 (exit).
- Choices: c0: でぐち | c1: ここ | c2: かお
- Expected/accepted: でぐち [c0]
- Explanation: 出口 is read でぐち in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-school-kanji

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 学校 (school).
- Prompt: Choose the reading of 学校 (school).
- Choices: c0: がっこう | c1: ここ | c2: かお
- Expected/accepted: がっこう [c0]
- Explanation: 学校 is read がっこう in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-book

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 本 (book).
- Prompt: Choose the reading of 本 (book).
- Choices: c0: ほん | c1: ここ | c2: かお
- Expected/accepted: ほん [c0]
- Explanation: 本 is read ほん in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-time

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 時間 (time).
- Prompt: Choose the reading of 時間 (time).
- Choices: c0: じかん | c1: ここ | c2: かお
- Expected/accepted: じかん [c0]
- Explanation: 時間 is read じかん in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-monday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 月曜日 (Monday).
- Prompt: Choose the reading of 月曜日 (Monday).
- Choices: c0: げつようび | c1: ここ | c2: かお
- Expected/accepted: げつようび [c0]
- Explanation: 月曜日 is read げつようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-tuesday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 火曜日 (Tuesday).
- Prompt: Choose the reading of 火曜日 (Tuesday).
- Choices: c0: かようび | c1: ここ | c2: かお
- Expected/accepted: かようび [c0]
- Explanation: 火曜日 is read かようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-wednesday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 水曜日 (Wednesday).
- Prompt: Choose the reading of 水曜日 (Wednesday).
- Choices: c0: すいようび | c1: ここ | c2: かお
- Expected/accepted: すいようび [c0]
- Explanation: 水曜日 is read すいようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-thursday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 木曜日 (Thursday).
- Prompt: Choose the reading of 木曜日 (Thursday).
- Choices: c0: もくようび | c1: ここ | c2: かお
- Expected/accepted: もくようび [c0]
- Explanation: 木曜日 is read もくようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-friday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 金曜日 (Friday).
- Prompt: Choose the reading of 金曜日 (Friday).
- Choices: c0: きんようび | c1: ここ | c2: かお
- Expected/accepted: きんようび [c0]
- Explanation: 金曜日 is read きんようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-reading-saturday

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Choose the reading of 土曜日 (Saturday).
- Prompt: Choose the reading of 土曜日 (Saturday).
- Choices: c0: どようび | c1: ここ | c2: かお
- Expected/accepted: どようび [c0]
- Explanation: 土曜日 is read どようび in this word.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-story-intro-name

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Who introduces themself as Aki?
- Prompt: Who introduces themself as Aki?
- Choices: c0: The first speaker | c1: The second speaker | c2: Neither speaker
- Expected/accepted: The first speaker [c0]
- Explanation: The first turn says アキです。
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: greeting
- Policy: {"strategy":"choice"}

#### ja-story-intro-reply

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: What does Haru say at this first meeting?
- Prompt: What does Haru say at this first meeting?
- Choices: c0: Goodbye | c1: Nice to meet you | c2: Thank you
- Expected/accepted: Nice to meet you [c1]
- Explanation: はじめまして is used at a first meeting.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: greeting
- Policy: {"strategy":"choice"}

#### ja-story-drink-water

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Which drink does Aki ask for?
- Prompt: Which drink does Aki ask for?
- Choices: c0: Tea | c1: Water | c2: Coffee
- Expected/accepted: Water [c1]
- Explanation: 水をください asks for water.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-story-drink-tea

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Which drink is named in Haru's turn?
- Prompt: Which drink is named in Haru's turn?
- Choices: c0: Water | c1: Coffee | c2: Tea
- Expected/accepted: Tea [c2]
- Explanation: お茶 is tea.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-passage-exit

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: Which sign points to the way out?
- Prompt: Which sign points to the way out?
- Choices: c0: 入口 | c1: 出口 | c2: 学校
- Expected/accepted: 出口 [c1]
- Explanation: 出口 means exit; 入口 means entrance.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-passage-schedule-day

- [ ] Qualified review; corrections/notes: pending
- Type/skill: multiple_choice / reading
- Objective: On which listed day does class start at 10:00?
- Prompt: On which listed day does class start at 10:00?
- Choices: c0: Monday | c1: Tuesday | c2: Sunday
- Expected/accepted: Tuesday [c1]
- Explanation: The Tuesday row lists 10:00. The Monday row lists 9:00.
- Hint: Use the accompanying context or reveal the answer when useful.
- Concepts: reading-context
- Policy: {"strategy":"choice"}

#### ja-writing-fixed-message-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Produce the specified greeting and polite name sentence in Japanese.
- Prompt: Write a daytime hello followed by “I am Aki” using アキ and です.
- Expected/accepted: こんにちは。アキです。
- Explanation: こんにちは is the daytime hello; アキです introduces Aki politely. This constrained task specifies the name, rather than assessing an unrestricted personal introduction.
- Hint: Use the daytime greeting, then the specified name and polite ending. Reveal the model when useful.
- Concepts: greeting, politeness
- Policy: {"strategy":"exact","normalization":"NFC","script":"japanese","punctuation":"ignore_terminal","spacing":"ignore","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

#### ja-writing-house-type

- [ ] Qualified review; corrections/notes: pending
- Type/skill: translation / typing
- Objective: Recall the taught hiragana word いえ from its meaning.
- Prompt: Write the word “house” in hiragana.
- Expected/accepted: いえ
- Explanation: いえ is the taught hiragana spelling for house. This task requests hiragana, so 家 is outside this script objective.
- Hint: The word uses two full-size hiragana. Reveal it if useful.
- Concepts: kana
- Policy: {"strategy":"exact","normalization":"NFC","script":"hiragana","punctuation":"exact","spacing":"preserve","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}

## Narrative scripts

### ja-story-first-meeting — A first meeting

- [ ] Qualified review; notes: pending
- story / draft / stage-a
- Objectives: Recognize a greeting and a name in a brief exchange.
- Glossary: ja-word-hello, ja-word-first-meeting, ja-word-copula
- Optional recap: ja-story-intro-name, ja-story-intro-reply

#### story-greet — Aki

[{"surface":"こんにちは","vocabulary_id":"ja-word-hello"},{"surface":"。アキです。"}]
- Next turns: story-reply
- Optional checks: ja-story-intro-name

#### story-reply — Haru

[{"surface":"はじめまして。ハルです。"}]
- Next turns: 
- Optional checks: ja-story-intro-reply

### ja-audio-first-introduction — A first introduction

- [ ] Qualified review; notes: pending
- audio_episode / draft / stage-a
- Objectives: Recognize a daytime greeting, a first-meeting expression and two names.
- Glossary: ja-word-hello, ja-word-first-meeting, ja-word-copula
- Optional recap: ja-greetings-names-match

#### audio-intro-aki — Aki

[{"surface":"こんにちは。はじめまして。アキです。"}]
- Next turns: audio-intro-haru
- Optional checks: 

#### audio-intro-haru — Haru

[{"surface":"はじめまして。ハルです。"}]
- Next turns: 
- Optional checks: ja-greetings-names-choice

### ja-audio-thanks-contexts — Thanks in two settings

- [ ] Qualified review; notes: pending
- audio_episode / draft / stage-a
- Objectives: Distinguish the casual and polite thank-you expressions in two short reference clips.
- Glossary: ja-word-thanks, ja-word-polite-thanks
- Optional recap: ja-greetings-thanks-match

#### audio-thanks-friend — Aki, thanking a friend

[{"surface":"ありがとう。"}]
- Next turns: audio-thanks-polite
- Optional checks: 

#### audio-thanks-polite — Aki, in a polite exchange

[{"surface":"ありがとうございます。"}]
- Next turns: 
- Optional checks: ja-greetings-thanks-choice

### ja-story-drink — Water or tea?

- [ ] Qualified review; notes: pending
- story / draft / stage-a
- Objectives: Follow two short drink requests.
- Glossary: ja-word-water, ja-word-tea, ja-word-polite-thanks
- Optional recap: ja-story-drink-water, ja-story-drink-tea

#### drink-aki — Aki

[{"surface":"水","reading":"みず","vocabulary_id":"ja-word-water"},{"surface":"をください。"}]
- Next turns: drink-haru
- Optional checks: ja-story-drink-water

#### drink-haru — Haru

[{"surface":"お茶","reading":"おちゃ","vocabulary_id":"ja-word-tea"},{"surface":"をください。"}]
- Next turns: drink-thanks
- Optional checks: ja-story-drink-tea

#### drink-thanks — Aki

[{"surface":"ありがとうございます","vocabulary_id":"ja-word-polite-thanks"},{"surface":"。"}]
- Next turns: 
- Optional checks: 

### ja-passage-signs — At the station

- [ ] Qualified review; notes: pending
- reading_passage / draft / stage-a
- Objectives: Distinguish entrance and exit signs.
- Glossary: ja-word-station, ja-word-entrance, ja-word-exit
- Optional recap: ja-passage-exit

#### sign-station — Station sign

[{"surface":"駅","reading":"えき","vocabulary_id":"ja-word-station"},{"surface":"　"},{"surface":"入口","reading":"いりぐち","vocabulary_id":"ja-word-entrance"},{"surface":" →　"},{"surface":"出口","reading":"でぐち","vocabulary_id":"ja-word-exit"},{"surface":" ←"}]
- Next turns: 
- Optional checks: ja-passage-exit

### ja-passage-schedule — A two-day class schedule

- [ ] Qualified review; notes: pending
- reading_passage / draft / stage-a
- Objectives: Find a day and time in a small schedule.
- Glossary: ja-word-monday, ja-word-tuesday
- Optional recap: ja-passage-schedule-day

#### schedule-days — Class schedule

[{"surface":"月曜日","reading":"げつようび","vocabulary_id":"ja-word-monday"},{"surface":" 9:00–10:00\n"},{"surface":"火曜日","reading":"かようび","vocabulary_id":"ja-word-tuesday"},{"surface":" 10:00–11:00"}]
- Next turns: 
- Optional checks: ja-passage-schedule-day

## Writing references

### ja-write-character-a — constrained character practice

- [ ] Qualified review; notes: pending
- stage-a / draft / rubric beginner-1
- Prompt: Enter the full-size hiragana for the sound a.
- Model: あ
- Alternatives: 
- Self-review: Use full-size あ, rather than small ぁ. | Treat this as a character-production reference; no handwriting or pronunciation assessment is implied.
- Constrained checked-drill IDs: ja-char-a-type

### ja-write-word-house — constrained word practice

- [ ] Qualified review; notes: pending
- stage-a / draft / rubric beginner-1
- Prompt: Write the word house in hiragana.
- Model: いえ
- Alternatives: 
- Self-review: Use い followed by え. | Use hiragana for this task; a kanji rendering is outside this script objective.
- Constrained checked-drill IDs: ja-writing-house-type

### ja-write-first — first sentence

- [ ] Qualified review; notes: pending
- stage-a / draft / rubric beginner-1
- Prompt: Introduce yourself with your name and です.
- Model: アキです。
- Alternatives: ハルです。
- Self-review: Use your name. | Finish with polite です.
- Constrained checked-drill IDs: 

### ja-write-intro — introduction

- [ ] Qualified review; notes: pending
- stage-b / draft / rubric beginner-1
- Prompt: Write three short sentences: your name, where you live, and one thing you like.
- Model: アキです。シンガポールに住んでいます。コーヒーが好きです。
- Alternatives: ハルです。東京に住んでいます。お茶が好きです。
- Self-review: Give your name. | Name where you live. | Say what you like. | Keep polite endings consistent.
- Constrained checked-drill IDs: 

Before: アキです。シンガポール。コーヒー。
After: アキです。シンガポールに住んでいます。コーヒーが好きです。
Annotation: Add predicates to turn the place and preference into complete statements.

### ja-write-routine — routine

- [ ] Qualified review; notes: pending
- stage-b / draft / rubric beginner-1
- Prompt: Write three to five sentences about your morning and one evening activity.
- Model: 毎朝七時に起きます。朝ごはんを食べます。コーヒーを飲みます。夜は日本語を勉強します。
- Alternatives: 毎朝八時に起きます。お茶を飲みます。夜は本を読みます。
- Self-review: Put events in a clear order. | Use times you know. | Use polite verbs consistently.
- Constrained checked-drill IDs: 

### ja-write-message — invitation

- [ ] Qualified review; notes: pending
- stage-b / draft / rubric beginner-1
- Prompt: Write a short message inviting a friend to have tea tomorrow. Suggest a time.
- Model: こんにちは。あした、お茶を飲みませんか。三時はどうですか。
- Alternatives: こんにちは。あした、コーヒーを飲みませんか。二時はどうですか。
- Self-review: Greet the reader. | Make an invitation. | Suggest a time. | Check politeness.
- Constrained checked-drill IDs: 

### ja-write-fixed-message — constrained short message

- [ ] Qualified review; notes: pending
- stage-a / draft / rubric beginner-1
- Prompt: Write a daytime hello followed by “I am Aki” using アキ and です.
- Model: こんにちは。アキです。
- Alternatives: 
- Self-review: Use the conventional spelling こんにちは. | Use アキ as the name and finish the introduction with です.
- Constrained checked-drill IDs: ja-writing-fixed-message-type

## Stroke asset provenance

### ja-stroke-3044-v1

- [ ] Qualified stroke review; notes: pending
- File: [original normalized path data](../content/courses/ja/assets/strokes/ja-stroke-3044-v1.json)
- Version/status: 1.0.0-draft / draft
- SHA-256: d47053dd055de814ae9a85755447c25a47d1469399b8e846f04443d351536fa2
- License: trilingo-original
- Source: Original Trilingo schematic normalized paths; Japanese stroke review pending. Not traced from a font or third-party diagram.
- Stroke 1: Curve down the left side, then finish with a short lift.
- Stroke 2: Begin on the upper right and curve down.

### ja-stroke-3053-v1

- [ ] Qualified stroke review; notes: pending
- File: [original normalized path data](../content/courses/ja/assets/strokes/ja-stroke-3053-v1.json)
- Version/status: 1.0.0-draft / draft
- SHA-256: ac2b61320902ce132e603f21305d829be1eb9b3449b071af8894d68a57859cdc
- License: trilingo-original
- Source: Original Trilingo schematic normalized paths; Japanese stroke review pending. Not traced from a font or third-party diagram.
- Stroke 1: Move across the upper part, with a short finishing turn.
- Stroke 2: Sweep across the lower part.

### ja-stroke-3046-v1

- [ ] Qualified stroke review; notes: pending
- File: [original normalized path data](../content/courses/ja/assets/strokes/ja-stroke-3046-v1.json)
- Version/status: 1.0.0-draft / draft
- SHA-256: 554ab7d07821cc9cb473c7c8275c59c572548a926c2900ae044ef0eb7e4ff100
- License: trilingo-original
- Source: Original Trilingo schematic normalized paths; Japanese stroke review pending. Not traced from a font or third-party diagram.
- Stroke 1: Make the short upper stroke.
- Stroke 2: Start below it, curve to the right and down toward the lower left.

### ja-stroke-65e5-v1

- [ ] Qualified stroke review; notes: pending
- File: [original normalized path data](../content/courses/ja/assets/strokes/ja-stroke-65e5-v1.json)
- Version/status: 1.0.0-draft / draft
- SHA-256: 1e385740f3fd6245dd726491d41d7053816457899a4d0f07e0360ed24d386b91
- License: trilingo-original
- Source: Original Trilingo schematic normalized paths; Japanese stroke review pending. Not traced from a font or third-party diagram.
- Stroke 1: Draw the left vertical downward.
- Stroke 2: Move right across the top, turn and continue down the right.
- Stroke 3: Draw the middle horizontal from left to right.
- Stroke 4: Close the bottom from left to right.

### ja-stroke-53e3-v1

- [ ] Qualified stroke review; notes: pending
- File: [original normalized path data](../content/courses/ja/assets/strokes/ja-stroke-53e3-v1.json)
- Version/status: 1.0.0-draft / draft
- SHA-256: cd98b944d521a1ac58638a35d69e18ab2e22eb31858588ca15cf28d73ade2ca2
- License: trilingo-original
- Source: Original Trilingo schematic normalized paths; Japanese stroke review pending. Not traced from a font or third-party diagram.
- Stroke 1: Draw the left vertical downward.
- Stroke 2: Move right across the top, turn and continue down the right.
- Stroke 3: Close the bottom from left to right.

### ja-stroke-5165-v1

- [ ] Qualified stroke review; notes: pending
- File: [original normalized path data](../content/courses/ja/assets/strokes/ja-stroke-5165-v1.json)
- Version/status: 1.0.0-draft / draft
- SHA-256: fbcf3157475594afa0f89304199021857e5b1627a42b27d7a94f8f243553b966
- License: trilingo-original
- Source: Original Trilingo schematic normalized paths; Japanese stroke review pending. Not traced from a font or third-party diagram.
- Stroke 1: Begin high and move down toward the lower left.
- Stroke 2: Begin near the upper meeting point and move down toward the lower right.

## Optional assessment banks

- [ ] ja-recap-greetings (draft): ja-greetings-hello-choice, ja-greetings-thanks-choice, ja-greetings-names-choice · Count actual unaided answers separately from assisted answers and skips. Results suggest practice only; no pass score controls access.
- [ ] ja-placement-first-steps (draft): ja-greetings-hello-choice, ja-greetings-thanks-type, ja-hiragana-vowels-choice, ja-hiragana-sounds-blank · Use your first unassisted responses as a practice snapshot. Revisit missed concepts in any order; every lesson remains available. This draft does not certify a level.
- [ ] ja-mastery-first-steps (draft): ja-greetings-names-type, ja-greetings-thanks-match, ja-hiragana-k-type, ja-hiragana-sounds-choice · Report first-answer accuracy and concept coverage, with assistance and skips separate. A result is optional feedback; no score grants or removes access or certifies mastery.

## Attribution

trilingo-original: Original Trilingo authored text; no third-party lesson text or artwork imported. CC-BY-4.0 · Trilingo original course contributors



## Version 0.1.9 draft additions

These two missing formats remain pending qualified review. No published lesson or word was changed.

### ja-passage-menu — A small café menu

- [ ] Qualified review; notes: pending
- Stage/status: stage-a / draft
- Structured text: [{"surface":"お茶","reading":"おちゃ","vocabulary_id":"ja-word-tea"},{"surface":"　¥200\n"},{"surface":"水","reading":"みず","vocabulary_id":"ja-word-water"},{"surface":"　¥0"}]
- Glossary: ja-word-tea, ja-word-water
- Check: ja-passage-menu-price — Which drink is listed at ¥200?
- Choices: c0: Water | c1: Coffee | c2: Tea
- Key: c2
- Explanation: The menu lists お茶 (tea) at ¥200 and 水 (water) at ¥0.

### ja-passage-message — A short invitation message

- [ ] Qualified review; notes: pending
- Stage/status: stage-b / draft
- Structured text: [{"surface":"ハルさんへ\n"},{"surface":"こんにちは","vocabulary_id":"ja-word-hello"},{"surface":"。アキです。\n"},{"surface":"月曜日","reading":"げつようび","vocabulary_id":"ja-word-monday"},{"surface":"、10:00に"},{"surface":"お茶","reading":"おちゃ","vocabulary_id":"ja-word-tea"},{"surface":"を飲みませんか。","reading":"をのみませんか。"}]
- Glossary: ja-word-hello, ja-word-monday, ja-word-tea
- Check: ja-passage-message-when — When does Aki suggest having tea?
- Choices: c0: Monday at 10:00 | c1: Tuesday at 10:00 | c2: Monday at 9:00
- Key: c0
- Explanation: The invitation names 月曜日 (Monday) and 10:00. 飲みませんか offers an invitation to have a drink.


## Source 0.1.10 — contextual kanji expansion (all draft)

This additive revision keeps the earlier published lesson text and stable IDs. It adds 282 distinct target characters to the existing 18, sharing 263 whole-word reading checks and 262 new vocabulary records. 家 reuses the existing canonical ja-word-house entry rather than counting the kana/kanji spelling twice. Shared compounds reuse one word/drill across target characters. No handwriting or proficiency is inferred.
Authoring manifest: content/authoring/ja/kanji-contexts-draft.json. Every new row has an original example and a contextual word/reading/gloss. These examples may introduce grammar beyond the individual target character; review sequencing, register, naturalness and contextual ambiguity before publication. Distractors and answer positions need qualified review.
### Added character contexts

#### ja-kanji-4e00 — 一 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 一つ · ひとつ · one thing
- Context: 一つください。
- Vocabulary: ja-word-kanji-4e00-3064
- Related checks: ja-context-4e00-3064-reading

#### ja-kanji-4e8c — 二 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 二つ · ふたつ · two things
- Context: 二つください。
- Vocabulary: ja-word-kanji-4e8c-3064
- Related checks: ja-context-4e8c-3064-reading

#### ja-kanji-4e09 — 三 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 三つ · みっつ · three things
- Context: 三つください。
- Vocabulary: ja-word-kanji-4e09-3064
- Related checks: ja-context-4e09-3064-reading

#### ja-kanji-56db — 四 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 四つ · よっつ · four things
- Context: 四つあります。
- Vocabulary: ja-word-kanji-56db-3064
- Related checks: ja-context-56db-3064-reading

#### ja-kanji-4e94 — 五 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 五つ · いつつ · five things
- Context: 五つあります。
- Vocabulary: ja-word-kanji-4e94-3064
- Related checks: ja-context-4e94-3064-reading

#### ja-kanji-516d — 六 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 六つ · むっつ · six things
- Context: 六つあります。
- Vocabulary: ja-word-kanji-516d-3064
- Related checks: ja-context-516d-3064-reading

#### ja-kanji-4e03 — 七 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 七つ · ななつ · seven things
- Context: 七つあります。
- Vocabulary: ja-word-kanji-4e03-3064
- Related checks: ja-context-4e03-3064-reading

#### ja-kanji-516b — 八 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 八つ · やっつ · eight things
- Context: 八つあります。
- Vocabulary: ja-word-kanji-516b-3064
- Related checks: ja-context-516b-3064-reading

#### ja-kanji-4e5d — 九 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 九つ · ここのつ · nine things
- Context: 九つあります。
- Vocabulary: ja-word-kanji-4e5d-3064
- Related checks: ja-context-4e5d-3064-reading

#### ja-kanji-5341 — 十 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 十 · じゅう · ten
- Context: 十まで数えます。
- Vocabulary: ja-word-kanji-5341
- Related checks: ja-context-5341-reading

#### ja-kanji-767e — 百 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 百 · ひゃく · one hundred
- Context: 百まで数えます。
- Vocabulary: ja-word-kanji-767e
- Related checks: ja-context-767e-reading

#### ja-kanji-5343 — 千 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 千円 · せんえん · one thousand yen
- Context: 千円です。
- Vocabulary: ja-word-kanji-5343-5186
- Related checks: ja-context-5343-5186-reading

#### ja-kanji-5186 — 円 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 円 · えん · yen
- Context: 円で払います。
- Vocabulary: ja-word-kanji-5186
- Related checks: ja-context-5186-reading

#### ja-kanji-5e74 — 年 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 一年 · いちねん · one year
- Context: 一年かかります。
- Vocabulary: ja-word-kanji-4e00-5e74
- Related checks: ja-context-4e00-5e74-reading

#### ja-kanji-4eca — 今 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 今 · いま · now
- Context: 今、行きます。
- Vocabulary: ja-word-kanji-4eca
- Related checks: ja-context-4eca-reading

#### ja-kanji-6bce — 毎 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 毎日 · まいにち · every day
- Context: 毎日読みます。
- Vocabulary: ja-word-kanji-6bce-65e5
- Related checks: ja-context-6bce-65e5-reading

#### ja-kanji-9031 — 週 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 来週 · らいしゅう · next week
- Context: 来週、会いましょう。
- Vocabulary: ja-word-kanji-6765-9031
- Related checks: ja-context-6765-9031-reading

#### ja-kanji-5206 — 分 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 五分 · ごふん · five minutes
- Context: 五分かかります。
- Vocabulary: ja-word-kanji-4e94-5206
- Related checks: ja-context-4e94-5206-reading

#### ja-kanji-534a — 半 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 半分 · はんぶん · half
- Context: 半分ください。
- Vocabulary: ja-word-kanji-534a-5206
- Related checks: ja-context-534a-5206-reading

#### ja-kanji-5348 — 午 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 午前 · ごぜん · morning; a.m.
- Context: 午前に行きます。
- Vocabulary: ja-word-kanji-5348-524d
- Related checks: ja-context-5348-524d-reading

#### ja-kanji-524d — 前 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 前 · まえ · front; before
- Context: 駅の前です。
- Vocabulary: ja-word-kanji-524d
- Related checks: ja-context-524d-reading

#### ja-kanji-5f8c — 後 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 後ろ · うしろ · behind; the back
- Context: 家の後ろです。
- Vocabulary: ja-word-kanji-5f8c-308d
- Related checks: ja-context-5f8c-308d-reading

#### ja-kanji-671d — 朝 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 朝 · あさ · morning
- Context: 朝、お茶を飲みます。
- Vocabulary: ja-word-kanji-671d
- Related checks: ja-context-671d-reading

#### ja-kanji-663c — 昼 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 昼 · ひる · daytime; noon
- Context: 昼に会いましょう。
- Vocabulary: ja-word-kanji-663c
- Related checks: ja-context-663c-reading

#### ja-kanji-591c — 夜 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 夜 · よる · night
- Context: 夜、本を読みます。
- Vocabulary: ja-word-kanji-591c
- Related checks: ja-context-591c-reading

#### ja-kanji-4eba — 人 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 人 · ひと · person
- Context: 人がいます。
- Vocabulary: ja-word-kanji-4eba
- Related checks: ja-context-4eba-reading

#### ja-kanji-7537 — 男 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 男の子 · おとこのこ · boy
- Context: 男の子がいます。
- Vocabulary: ja-word-kanji-7537-306e-5b50
- Related checks: ja-context-7537-306e-5b50-reading

#### ja-kanji-5973 — 女 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 女の子 · おんなのこ · girl
- Context: 女の子がいます。
- Vocabulary: ja-word-kanji-5973-306e-5b50
- Related checks: ja-context-5973-306e-5b50-reading

#### ja-kanji-5b50 — 子 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 子ども · こども · child
- Context: 子どもがいます。
- Vocabulary: ja-word-kanji-5b50-3069-3082
- Related checks: ja-context-5b50-3069-3082-reading

#### ja-kanji-7236 — 父 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 父 · ちち · my father
- Context: 父は家にいます。
- Vocabulary: ja-word-kanji-7236
- Related checks: ja-context-7236-reading

#### ja-kanji-6bcd — 母 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 母 · はは · my mother
- Context: 母は家にいます。
- Vocabulary: ja-word-kanji-6bcd
- Related checks: ja-context-6bcd-reading

#### ja-kanji-53cb — 友 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 友達 · ともだち · friend
- Context: 友達と行きます。
- Vocabulary: ja-word-kanji-53cb-9054
- Related checks: ja-context-53cb-9054-reading

#### ja-kanji-5148 — 先 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 先生 · せんせい · teacher
- Context: 先生に聞きます。
- Vocabulary: ja-word-kanji-5148-751f
- Related checks: ja-context-5148-751f-reading

#### ja-kanji-751f — 生 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 学生 · がくせい · student
- Context: 私は学生です。
- Vocabulary: ja-word-kanji-5b66-751f
- Related checks: ja-context-5b66-751f-reading

#### ja-kanji-540d — 名 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 名前 · なまえ · name
- Context: 名前を書きます。
- Vocabulary: ja-word-kanji-540d-524d
- Related checks: ja-context-540d-524d-reading

#### ja-kanji-79c1 — 私 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 私 · わたし · I; me
- Context: 私はアキです。
- Vocabulary: ja-word-kanji-79c1
- Related checks: ja-context-79c1-reading

#### ja-kanji-5bb6 — 家 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 家 · いえ · house; home
- Context: 家に帰ります。
- Vocabulary: ja-word-house
- Related checks: ja-context-5bb6-reading

#### ja-kanji-5c71 — 山 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 山 · やま · mountain
- Context: 山が見えます。
- Vocabulary: ja-word-kanji-5c71
- Related checks: ja-context-5c71-reading

#### ja-kanji-5ddd — 川 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 川 · かわ · river
- Context: 川があります。
- Vocabulary: ja-word-kanji-5ddd
- Related checks: ja-context-5ddd-reading

#### ja-kanji-7a7a — 空 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 空 · そら · sky
- Context: 空が青いです。
- Vocabulary: ja-word-kanji-7a7a
- Related checks: ja-context-7a7a-reading

#### ja-kanji-96e8 — 雨 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 雨 · あめ · rain
- Context: 雨が降っています。
- Vocabulary: ja-word-kanji-96e8
- Related checks: ja-context-96e8-reading

#### ja-kanji-5929 — 天 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 天気 · てんき · weather
- Context: 天気がいいです。
- Vocabulary: ja-word-kanji-5929-6c17
- Related checks: ja-context-5929-6c17-reading

#### ja-kanji-6c17 — 気 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 元気 · げんき · healthy; in good spirits
- Context: 元気です。
- Vocabulary: ja-word-kanji-5143-6c17
- Related checks: ja-context-5143-6c17-reading

#### ja-kanji-82b1 — 花 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 花 · はな · flower
- Context: 花を見ます。
- Vocabulary: ja-word-kanji-82b1
- Related checks: ja-context-82b1-reading

#### ja-kanji-72ac — 犬 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 犬 · いぬ · dog
- Context: 犬がいます。
- Vocabulary: ja-word-kanji-72ac
- Related checks: ja-context-72ac-reading

#### ja-kanji-732b — 猫 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 猫 · ねこ · cat
- Context: 猫がいます。
- Vocabulary: ja-word-kanji-732b
- Related checks: ja-context-732b-reading

#### ja-kanji-9ce5 — 鳥 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 鳥 · とり · bird
- Context: 鳥がいます。
- Vocabulary: ja-word-kanji-9ce5
- Related checks: ja-context-9ce5-reading

#### ja-kanji-9b5a — 魚 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 魚 · さかな · fish
- Context: 魚を食べます。
- Vocabulary: ja-word-kanji-9b5a
- Related checks: ja-context-9b5a-reading

#### ja-kanji-8eca — 車 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 車 · くるま · car
- Context: 車で行きます。
- Vocabulary: ja-word-kanji-8eca
- Related checks: ja-context-8eca-reading

#### ja-kanji-96fb — 電 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 電車 · でんしゃ · train
- Context: 電車で行きます。
- Vocabulary: ja-word-kanji-96fb-8eca
- Related checks: ja-context-96fb-8eca-reading

#### ja-kanji-9053 — 道 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 道 · みち · road; way
- Context: この道を行きます。
- Vocabulary: ja-word-kanji-9053
- Related checks: ja-context-9053-reading

#### ja-kanji-5e97 — 店 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 店 · みせ · shop
- Context: 店に入ります。
- Vocabulary: ja-word-kanji-5e97
- Related checks: ja-context-5e97-reading

#### ja-kanji-4f1a — 会 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 会社 · かいしゃ · company
- Context: 会社に行きます。
- Vocabulary: ja-word-kanji-4f1a-793e
- Related checks: ja-context-4f1a-793e-reading

#### ja-kanji-793e — 社 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 会社 · かいしゃ · company
- Context: 会社に行きます。
- Vocabulary: ja-word-kanji-4f1a-793e
- Related checks: ja-context-4f1a-793e-reading

#### ja-kanji-56fd — 国 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 国 · くに · country
- Context: どの国ですか。
- Vocabulary: ja-word-kanji-56fd
- Related checks: ja-context-56fd-reading

#### ja-kanji-5916 — 外 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 外 · そと · outside
- Context: 外に出ます。
- Vocabulary: ja-word-kanji-5916
- Related checks: ja-context-5916-reading

#### ja-kanji-4e2d — 中 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 中 · なか · inside
- Context: 中に入ります。
- Vocabulary: ja-word-kanji-4e2d
- Related checks: ja-context-4e2d-reading

#### ja-kanji-4e0a — 上 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 上 · うえ · above; on top
- Context: 机の上です。
- Vocabulary: ja-word-kanji-4e0a
- Related checks: ja-context-4e0a-reading

#### ja-kanji-4e0b — 下 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 下 · した · below; underneath
- Context: 机の下です。
- Vocabulary: ja-word-kanji-4e0b
- Related checks: ja-context-4e0b-reading

#### ja-kanji-5de6 — 左 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 左 · ひだり · left
- Context: 左に曲がります。
- Vocabulary: ja-word-kanji-5de6
- Related checks: ja-context-5de6-reading

#### ja-kanji-53f3 — 右 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 右 · みぎ · right
- Context: 右に曲がります。
- Vocabulary: ja-word-kanji-53f3
- Related checks: ja-context-53f3-reading

#### ja-kanji-5317 — 北 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 北 · きた · north
- Context: 北へ行きます。
- Vocabulary: ja-word-kanji-5317
- Related checks: ja-context-5317-reading

#### ja-kanji-5357 — 南 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 南 · みなみ · south
- Context: 南へ行きます。
- Vocabulary: ja-word-kanji-5357
- Related checks: ja-context-5357-reading

#### ja-kanji-6771 — 東 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 東 · ひがし · east
- Context: 東へ行きます。
- Vocabulary: ja-word-kanji-6771
- Related checks: ja-context-6771-reading

#### ja-kanji-897f — 西 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 西 · にし · west
- Context: 西へ行きます。
- Vocabulary: ja-word-kanji-897f
- Related checks: ja-context-897f-reading

#### ja-kanji-5927 — 大 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 大きい · おおきい · big
- Context: 大きい家です。
- Vocabulary: ja-word-kanji-5927-304d-3044
- Related checks: ja-context-5927-304d-3044-reading

#### ja-kanji-5c0f — 小 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 小さい · ちいさい · small
- Context: 小さい店です。
- Vocabulary: ja-word-kanji-5c0f-3055-3044
- Related checks: ja-context-5c0f-3055-3044-reading

#### ja-kanji-9577 — 長 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 長い · ながい · long
- Context: 長い道です。
- Vocabulary: ja-word-kanji-9577-3044
- Related checks: ja-context-9577-3044-reading

#### ja-kanji-9ad8 — 高 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 高い · たかい · high; expensive
- Context: この本は高いです。
- Vocabulary: ja-word-kanji-9ad8-3044
- Related checks: ja-context-9ad8-3044-reading

#### ja-kanji-5b89 — 安 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 安い · やすい · inexpensive
- Context: この本は安いです。
- Vocabulary: ja-word-kanji-5b89-3044
- Related checks: ja-context-5b89-3044-reading

#### ja-kanji-65b0 — 新 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 新しい · あたらしい · new
- Context: 新しい本です。
- Vocabulary: ja-word-kanji-65b0-3057-3044
- Related checks: ja-context-65b0-3057-3044-reading

#### ja-kanji-53e4 — 古 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 古い · ふるい · old
- Context: 古い家です。
- Vocabulary: ja-word-kanji-53e4-3044
- Related checks: ja-context-53e4-3044-reading

#### ja-kanji-767d — 白 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 白い · しろい · white
- Context: 白い紙です。
- Vocabulary: ja-word-kanji-767d-3044
- Related checks: ja-context-767d-3044-reading

#### ja-kanji-9ed2 — 黒 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 黒い · くろい · black
- Context: 黒い車です。
- Vocabulary: ja-word-kanji-9ed2-3044
- Related checks: ja-context-9ed2-3044-reading

#### ja-kanji-8d64 — 赤 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 赤い · あかい · red
- Context: 赤い花です。
- Vocabulary: ja-word-kanji-8d64-3044
- Related checks: ja-context-8d64-3044-reading

#### ja-kanji-9752 — 青 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 青い · あおい · blue
- Context: 青い空です。
- Vocabulary: ja-word-kanji-9752-3044
- Related checks: ja-context-9752-3044-reading

#### ja-kanji-597d — 好 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 好き · すき · liked; favorite
- Context: お茶が好きです。
- Vocabulary: ja-word-kanji-597d-304d
- Related checks: ja-context-597d-304d-reading

#### ja-kanji-98df — 食 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 食べる · たべる · to eat
- Context: 何を食べるか決めます。
- Vocabulary: ja-word-kanji-98df-3079-308b
- Related checks: ja-context-98df-3079-308b-reading

#### ja-kanji-98f2 — 飲 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 飲む · のむ · to drink
- Context: 何を飲むか決めます。
- Vocabulary: ja-word-kanji-98f2-3080
- Related checks: ja-context-98f2-3080-reading

#### ja-kanji-898b — 見 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 見る · みる · to see; to watch
- Context: 映画を見るのが好きです。
- Vocabulary: ja-word-kanji-898b-308b
- Related checks: ja-context-898b-308b-reading

#### ja-kanji-884c — 行 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 行く · いく · to go
- Context: どこへ行くか決めます。
- Vocabulary: ja-word-kanji-884c-304f
- Related checks: ja-context-884c-304f-reading

#### ja-kanji-6765 — 来 (stage-a)

- [ ] Qualified review; notes: pending
- Word: 来る · くる · to come
- Context: 友達が来る日です。
- Vocabulary: ja-word-kanji-6765-308b
- Related checks: ja-context-6765-308b-reading

#### ja-kanji-4e07 — 万 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 一万円 · いちまんえん · ten thousand yen
- Context: 一万円です。
- Vocabulary: ja-word-kanji-4e00-4e07-5186
- Related checks: ja-context-4e00-4e07-5186-reading

#### ja-kanji-8349 — 草 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 草 · くさ · grass
- Context: 草が生えています。
- Vocabulary: ja-word-kanji-8349
- Related checks: ja-context-8349-reading

#### ja-kanji-7530 — 田 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 田んぼ · たんぼ · rice field
- Context: 田んぼが見えます。
- Vocabulary: ja-word-kanji-7530-3093-307c
- Related checks: ja-context-7530-3093-307c-reading

#### ja-kanji-4ed5 — 仕 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 仕事 · しごと · work; job
- Context: 仕事に行きます。
- Vocabulary: ja-word-kanji-4ed5-4e8b
- Related checks: ja-context-4ed5-4e8b-reading

#### ja-kanji-4e8b — 事 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 仕事 · しごと · work; job
- Context: 仕事に行きます。
- Vocabulary: ja-word-kanji-4ed5-4e8b
- Related checks: ja-context-4ed5-4e8b-reading

#### ja-kanji-54e1 — 員 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 店員 · てんいん · shop assistant
- Context: 店員に聞きます。
- Vocabulary: ja-word-kanji-5e97-54e1
- Related checks: ja-context-5e97-54e1-reading

#### ja-kanji-5de5 — 工 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 工場 · こうじょう · factory
- Context: 工場で働きます。
- Vocabulary: ja-word-kanji-5de5-5834
- Related checks: ja-context-5de5-5834-reading

#### ja-kanji-5834 — 場 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 工場 · こうじょう · factory
- Context: 工場で働きます。
- Vocabulary: ja-word-kanji-5de5-5834
- Related checks: ja-context-5de5-5834-reading

#### ja-kanji-50cd — 働 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 働く · はたらく · to work
- Context: ここで働く人です。
- Vocabulary: ja-word-kanji-50cd-304f
- Related checks: ja-context-50cd-304f-reading

#### ja-kanji-4f11 — 休 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 休む · やすむ · to rest; to take time off
- Context: 今日は休むことにします。
- Vocabulary: ja-word-kanji-4f11-3080
- Related checks: ja-context-4f11-3080-reading

#### ja-kanji-5fd9 — 忙 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 忙しい · いそがしい · busy
- Context: 今日は忙しいです。
- Vocabulary: ja-word-kanji-5fd9-3057-3044
- Related checks: ja-context-5fd9-3057-3044-reading

#### ja-kanji-7d66 — 給 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 給料 · きゅうりょう · salary; wages
- Context: 給料を受け取ります。
- Vocabulary: ja-word-kanji-7d66-6599
- Related checks: ja-context-7d66-6599-reading

#### ja-kanji-6599 — 料 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 給料 · きゅうりょう · salary; wages
- Context: 給料を受け取ります。
- Vocabulary: ja-word-kanji-7d66-6599
- Related checks: ja-context-7d66-6599-reading

#### ja-kanji-4f4f — 住 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 住む · すむ · to live; to reside
- Context: ここに住む人です。
- Vocabulary: ja-word-kanji-4f4f-3080
- Related checks: ja-context-4f4f-3080-reading

#### ja-kanji-6240 — 所 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 住所 · じゅうしょ · address
- Context: 住所を書きます。
- Vocabulary: ja-word-kanji-4f4f-6240
- Related checks: ja-context-4f4f-6240-reading

#### ja-kanji-753a — 町 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 町 · まち · town
- Context: 静かな町です。
- Vocabulary: ja-word-kanji-753a
- Related checks: ja-context-753a-reading

#### ja-kanji-6751 — 村 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 村 · むら · village
- Context: 小さい村です。
- Vocabulary: ja-word-kanji-6751
- Related checks: ja-context-6751-reading

#### ja-kanji-5e02 — 市 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 市 · し · city; municipality
- Context: この市に住んでいます。
- Vocabulary: ja-word-kanji-5e02
- Related checks: ja-context-5e02-reading

#### ja-kanji-770c — 県 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 県 · けん · prefecture
- Context: どの県ですか。
- Vocabulary: ja-word-kanji-770c
- Related checks: ja-context-770c-reading

#### ja-kanji-90fd — 都 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 東京都 · とうきょうと · Tokyo Metropolis
- Context: 東京都に住んでいます。
- Vocabulary: ja-word-kanji-6771-4eac-90fd
- Related checks: ja-context-6771-4eac-90fd-reading

#### ja-kanji-4eac — 京 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 東京 · とうきょう · Tokyo
- Context: 東京に行きます。
- Vocabulary: ja-word-kanji-6771-4eac
- Related checks: ja-context-6771-4eac-reading

#### ja-kanji-533a — 区 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 区 · く · ward; district
- Context: どの区ですか。
- Vocabulary: ja-word-kanji-533a
- Related checks: ja-context-533a-reading

#### ja-kanji-696d — 業 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 授業 · じゅぎょう · class; lesson
- Context: 授業が始まります。
- Vocabulary: ja-word-kanji-6388-696d
- Related checks: ja-context-6388-696d-reading

#### ja-kanji-8fd1 — 近 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 近い · ちかい · near
- Context: 駅は近いです。
- Vocabulary: ja-word-kanji-8fd1-3044
- Related checks: ja-context-8fd1-3044-reading

#### ja-kanji-9060 — 遠 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 遠い · とおい · far
- Context: 駅は遠いです。
- Vocabulary: ja-word-kanji-9060-3044
- Related checks: ja-context-9060-3044-reading

#### ja-kanji-901a — 通 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 通る · とおる · to pass through
- Context: この道を通るバスです。
- Vocabulary: ja-word-kanji-901a-308b
- Related checks: ja-context-901a-308b-reading

#### ja-kanji-4ea4 — 交 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 交通 · こうつう · traffic; transportation
- Context: 交通の便がいいです。
- Vocabulary: ja-word-kanji-4ea4-901a
- Related checks: ja-context-4ea4-901a-reading

#### ja-kanji-5730 — 地 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 地図 · ちず · map
- Context: 地図を見ます。
- Vocabulary: ja-word-kanji-5730-56f3
- Related checks: ja-context-5730-56f3-reading

#### ja-kanji-56f3 — 図 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 地図 · ちず · map
- Context: 地図を見ます。
- Vocabulary: ja-word-kanji-5730-56f3
- Related checks: ja-context-5730-56f3-reading

#### ja-kanji-6d77 — 海 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 海 · うみ · sea
- Context: 海が見えます。
- Vocabulary: ja-word-kanji-6d77
- Related checks: ja-context-6d77-reading

#### ja-kanji-6e2f — 港 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 港 · みなと · port; harbor
- Context: 港に行きます。
- Vocabulary: ja-word-kanji-6e2f
- Related checks: ja-context-6e2f-reading

#### ja-kanji-6c60 — 池 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 池 · いけ · pond
- Context: 池があります。
- Vocabulary: ja-word-kanji-6c60
- Related checks: ja-context-6c60-reading

#### ja-kanji-6a4b — 橋 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 橋 · はし · bridge
- Context: 橋を渡ります。
- Vocabulary: ja-word-kanji-6a4b
- Related checks: ja-context-6a4b-reading

#### ja-kanji-5efa — 建 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 建物 · たてもの · building
- Context: 大きい建物です。
- Vocabulary: ja-word-kanji-5efa-7269
- Related checks: ja-context-5efa-7269-reading

#### ja-kanji-7269 — 物 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 建物 · たてもの · building
- Context: 大きい建物です。
- Vocabulary: ja-word-kanji-5efa-7269
- Related checks: ja-context-5efa-7269-reading

#### ja-kanji-90e8 — 部 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 部屋 · へや · room
- Context: 部屋に入ります。
- Vocabulary: ja-word-kanji-90e8-5c4b
- Related checks: ja-context-90e8-5c4b-reading

#### ja-kanji-5c4b — 屋 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 部屋 · へや · room
- Context: 部屋に入ります。
- Vocabulary: ja-word-kanji-90e8-5c4b
- Related checks: ja-context-90e8-5c4b-reading

#### ja-kanji-5ba4 — 室 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 教室 · きょうしつ · classroom
- Context: 教室に入ります。
- Vocabulary: ja-word-kanji-6559-5ba4
- Related checks: ja-context-6559-5ba4-reading

#### ja-kanji-53f0 — 台 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 台所 · だいどころ · kitchen
- Context: 台所にいます。
- Vocabulary: ja-word-kanji-53f0-6240
- Related checks: ja-context-53f0-6240-reading

#### ja-kanji-968e — 階 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 二階 · にかい · second floor
- Context: 二階に行きます。
- Vocabulary: ja-word-kanji-4e8c-968e
- Related checks: ja-context-4e8c-968e-reading

#### ja-kanji-7a93 — 窓 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 窓 · まど · window
- Context: 窓を開けます。
- Vocabulary: ja-word-kanji-7a93
- Related checks: ja-context-7a93-reading

#### ja-kanji-6238 — 戸 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 戸 · と · door; sliding door
- Context: 戸を開けます。
- Vocabulary: ja-word-kanji-6238
- Related checks: ja-context-6238-reading

#### ja-kanji-9580 — 門 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 門 · もん · gate
- Context: 門の前です。
- Vocabulary: ja-word-kanji-9580
- Related checks: ja-context-9580-reading

#### ja-kanji-5ead — 庭 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 庭 · にわ · garden; yard
- Context: 庭に花があります。
- Vocabulary: ja-word-kanji-5ead
- Related checks: ja-context-5ead-reading

#### ja-kanji-516c — 公 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 公園 · こうえん · park
- Context: 公園に行きます。
- Vocabulary: ja-word-kanji-516c-5712
- Related checks: ja-context-516c-5712-reading

#### ja-kanji-5712 — 園 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 公園 · こうえん · park
- Context: 公園に行きます。
- Vocabulary: ja-word-kanji-516c-5712
- Related checks: ja-context-516c-5712-reading

#### ja-kanji-9928 — 館 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 図書館 · としょかん · library
- Context: 図書館で本を借ります。
- Vocabulary: ja-word-kanji-56f3-66f8-9928
- Related checks: ja-context-56f3-66f8-9928-reading

#### ja-kanji-65cf — 族 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 家族 · かぞく · family
- Context: 家族と話します。
- Vocabulary: ja-word-kanji-5bb6-65cf
- Related checks: ja-context-5bb6-65cf-reading

#### ja-kanji-5144 — 兄 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 兄 · あに · my older brother
- Context: 兄は家にいます。
- Vocabulary: ja-word-kanji-5144
- Related checks: ja-context-5144-reading

#### ja-kanji-5f1f — 弟 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 弟 · おとうと · younger brother
- Context: 弟は学生です。
- Vocabulary: ja-word-kanji-5f1f
- Related checks: ja-context-5f1f-reading

#### ja-kanji-59c9 — 姉 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 姉 · あね · my older sister
- Context: 姉は家にいます。
- Vocabulary: ja-word-kanji-59c9
- Related checks: ja-context-59c9-reading

#### ja-kanji-59b9 — 妹 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 妹 · いもうと · younger sister
- Context: 妹は学生です。
- Vocabulary: ja-word-kanji-59b9
- Related checks: ja-context-59b9-reading

#### ja-kanji-592b — 夫 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 夫 · おっと · my husband
- Context: 夫と出かけます。
- Vocabulary: ja-word-kanji-592b
- Related checks: ja-context-592b-reading

#### ja-kanji-59bb — 妻 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 妻 · つま · my wife
- Context: 妻と出かけます。
- Vocabulary: ja-word-kanji-59bb
- Related checks: ja-context-59bb-reading

#### ja-kanji-89aa — 親 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 親 · おや · parent
- Context: 親と話します。
- Vocabulary: ja-word-kanji-89aa
- Related checks: ja-context-89aa-reading

#### ja-kanji-4e21 — 両 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 両親 · りょうしん · both parents; parents
- Context: 両親と住んでいます。
- Vocabulary: ja-word-kanji-4e21-89aa
- Related checks: ja-context-4e21-89aa-reading

#### ja-kanji-7956 — 祖 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 祖母 · そぼ · my grandmother
- Context: 祖母に会います。
- Vocabulary: ja-word-kanji-7956-6bcd
- Related checks: ja-context-7956-6bcd-reading

#### ja-kanji-6b73 — 歳 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 二十歳 · はたち · twenty years old
- Context: 二十歳です。
- Vocabulary: ja-word-kanji-4e8c-5341-6b73
- Related checks: ja-context-4e8c-5341-6b73-reading

#### ja-kanji-8a95 — 誕 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 誕生日 · たんじょうび · birthday
- Context: 今日は誕生日です。
- Vocabulary: ja-word-kanji-8a95-751f-65e5
- Related checks: ja-context-8a95-751f-65e5-reading

#### ja-kanji-7d50 — 結 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 結婚 · けっこん · marriage
- Context: 結婚しています。
- Vocabulary: ja-word-kanji-7d50-5a5a
- Related checks: ja-context-7d50-5a5a-reading

#### ja-kanji-5a5a — 婚 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 結婚 · けっこん · marriage
- Context: 結婚しています。
- Vocabulary: ja-word-kanji-7d50-5a5a
- Related checks: ja-context-7d50-5a5a-reading

#### ja-kanji-5f7c — 彼 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 彼 · かれ · he; him
- Context: 彼は友達です。
- Vocabulary: ja-word-kanji-5f7c
- Related checks: ja-context-5f7c-reading

#### ja-kanji-96a3 — 隣 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 隣 · となり · next door; beside
- Context: 隣の家です。
- Vocabulary: ja-word-kanji-96a3
- Related checks: ja-context-96a3-reading

#### ja-kanji-4f55 — 何 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 何 · なに · what
- Context: 何が好きですか。
- Vocabulary: ja-word-kanji-4f55
- Related checks: ja-context-4f55-reading

#### ja-kanji-8ab0 — 誰 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 誰 · だれ · who
- Context: 誰が来ますか。
- Vocabulary: ja-word-kanji-8ab0
- Related checks: ja-context-8ab0-reading

#### ja-kanji-4f53 — 体 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 体 · からだ · body
- Context: 体を動かします。
- Vocabulary: ja-word-kanji-4f53
- Related checks: ja-context-4f53-reading

#### ja-kanji-982d — 頭 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 頭 · あたま · head
- Context: 頭が痛いです。
- Vocabulary: ja-word-kanji-982d
- Related checks: ja-context-982d-reading

#### ja-kanji-76ee — 目 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 目 · め · eye
- Context: 目を閉じます。
- Vocabulary: ja-word-kanji-76ee
- Related checks: ja-context-76ee-reading

#### ja-kanji-8033 — 耳 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 耳 · みみ · ear
- Context: 耳が痛いです。
- Vocabulary: ja-word-kanji-8033
- Related checks: ja-context-8033-reading

#### ja-kanji-9f3b — 鼻 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 鼻 · はな · nose
- Context: 鼻をかみます。
- Vocabulary: ja-word-kanji-9f3b
- Related checks: ja-context-9f3b-reading

#### ja-kanji-6b6f — 歯 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 歯 · は · tooth; teeth
- Context: 歯を磨きます。
- Vocabulary: ja-word-kanji-6b6f
- Related checks: ja-context-6b6f-reading

#### ja-kanji-8db3 — 足 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 足 · あし · foot; leg
- Context: 足が痛いです。
- Vocabulary: ja-word-kanji-8db3
- Related checks: ja-context-8db3-reading

#### ja-kanji-624b — 手 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 手 · て · hand
- Context: 手を洗います。
- Vocabulary: ja-word-kanji-624b
- Related checks: ja-context-624b-reading

#### ja-kanji-6307 — 指 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 指 · ゆび · finger
- Context: 指で示します。
- Vocabulary: ja-word-kanji-6307
- Related checks: ja-context-6307-reading

#### ja-kanji-5fc3 — 心 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 心 · こころ · heart; mind
- Context: 心が落ち着きます。
- Vocabulary: ja-word-kanji-5fc3
- Related checks: ja-context-5fc3-reading

#### ja-kanji-5143 — 元 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 元気 · げんき · healthy; in good spirits
- Context: 元気です。
- Vocabulary: ja-word-kanji-5143-6c17
- Related checks: ja-context-5143-6c17-reading

#### ja-kanji-529b — 力 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 力 · ちから · strength; power
- Context: 力を合わせます。
- Vocabulary: ja-word-kanji-529b
- Related checks: ja-context-529b-reading

#### ja-kanji-75c5 — 病 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 病院 · びょういん · hospital
- Context: 病院に行きます。
- Vocabulary: ja-word-kanji-75c5-9662
- Related checks: ja-context-75c5-9662-reading

#### ja-kanji-9662 — 院 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 病院 · びょういん · hospital
- Context: 病院に行きます。
- Vocabulary: ja-word-kanji-75c5-9662
- Related checks: ja-context-75c5-9662-reading

#### ja-kanji-533b — 医 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 医者 · いしゃ · doctor
- Context: 医者に相談します。
- Vocabulary: ja-word-kanji-533b-8005
- Related checks: ja-context-533b-8005-reading

#### ja-kanji-8005 — 者 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 医者 · いしゃ · doctor
- Context: 医者に相談します。
- Vocabulary: ja-word-kanji-533b-8005
- Related checks: ja-context-533b-8005-reading

#### ja-kanji-85ac — 薬 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 薬 · くすり · medicine
- Context: 薬を飲みます。
- Vocabulary: ja-word-kanji-85ac
- Related checks: ja-context-85ac-reading

#### ja-kanji-5c40 — 局 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 薬局 · やっきょく · pharmacy
- Context: 薬局に行きます。
- Vocabulary: ja-word-kanji-85ac-5c40
- Related checks: ja-context-85ac-5c40-reading

#### ja-kanji-75db — 痛 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 痛い · いたい · painful; sore
- Context: 頭が痛いです。
- Vocabulary: ja-word-kanji-75db-3044
- Related checks: ja-context-75db-3044-reading

#### ja-kanji-71b1 — 熱 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 熱 · ねつ · fever; heat
- Context: 熱があります。
- Vocabulary: ja-word-kanji-71b1
- Related checks: ja-context-71b1-reading

#### ja-kanji-7d19 — 紙 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 紙 · かみ · paper
- Context: 紙に書きます。
- Vocabulary: ja-word-kanji-7d19
- Related checks: ja-context-7d19-reading

#### ja-kanji-5b57 — 字 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 字 · じ · character; written letter
- Context: 字を書きます。
- Vocabulary: ja-word-kanji-5b57
- Related checks: ja-context-5b57-reading

#### ja-kanji-6587 — 文 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 文 · ぶん · sentence
- Context: 短い文を書きます。
- Vocabulary: ja-word-kanji-6587
- Related checks: ja-context-6587-reading

#### ja-kanji-8a9e — 語 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 日本語 · にほんご · Japanese language
- Context: 日本語を勉強します。
- Vocabulary: ja-word-kanji-65e5-672c-8a9e
- Related checks: ja-context-65e5-672c-8a9e-reading

#### ja-kanji-82f1 — 英 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 英語 · えいご · English language
- Context: 英語を話します。
- Vocabulary: ja-word-kanji-82f1-8a9e
- Related checks: ja-context-82f1-8a9e-reading

#### ja-kanji-6f22 — 漢 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 漢字 · かんじ · kanji; Chinese-derived character
- Context: 漢字を読みます。
- Vocabulary: ja-word-kanji-6f22-5b57
- Related checks: ja-context-6f22-5b57-reading

#### ja-kanji-8aad — 読 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 読む · よむ · to read
- Context: 本を読む時間です。
- Vocabulary: ja-word-kanji-8aad-3080
- Related checks: ja-context-8aad-3080-reading

#### ja-kanji-66f8 — 書 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 書く · かく · to write
- Context: 名前を書く場所です。
- Vocabulary: ja-word-kanji-66f8-304f
- Related checks: ja-context-66f8-304f-reading

#### ja-kanji-805e — 聞 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 聞く · きく · to listen; to ask
- Context: 音楽を聞く時間です。
- Vocabulary: ja-word-kanji-805e-304f
- Related checks: ja-context-805e-304f-reading

#### ja-kanji-8a71 — 話 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 話す · はなす · to speak
- Context: 日本語で話す練習です。
- Vocabulary: ja-word-kanji-8a71-3059
- Related checks: ja-context-8a71-3059-reading

#### ja-kanji-8a00 — 言 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 言う · いう · to say
- Context: 何と言うか考えます。
- Vocabulary: ja-word-kanji-8a00-3046
- Related checks: ja-context-8a00-3046-reading

#### ja-kanji-601d — 思 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 思う · おもう · to think; to feel
- Context: どう思うか教えてください。
- Vocabulary: ja-word-kanji-601d-3046
- Related checks: ja-context-601d-3046-reading

#### ja-kanji-77e5 — 知 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 知る · しる · to find out; to know
- Context: 町のことを知るために歩きます。
- Vocabulary: ja-word-kanji-77e5-308b
- Related checks: ja-context-77e5-308b-reading

#### ja-kanji-8003 — 考 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 考える · かんがえる · to think; to consider
- Context: 答えを考える時間です。
- Vocabulary: ja-word-kanji-8003-3048-308b
- Related checks: ja-context-8003-3048-308b-reading

#### ja-kanji-6559 — 教 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 教える · おしえる · to teach; to tell
- Context: 日本語を教える仕事です。
- Vocabulary: ja-word-kanji-6559-3048-308b
- Related checks: ja-context-6559-3048-308b-reading

#### ja-kanji-7fd2 — 習 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 習う · ならう · to learn; to take lessons
- Context: 日本語を習う予定です。
- Vocabulary: ja-word-kanji-7fd2-3046
- Related checks: ja-context-7fd2-3046-reading

#### ja-kanji-52c9 — 勉 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 勉強 · べんきょう · study
- Context: 日本語の勉強をします。
- Vocabulary: ja-word-kanji-52c9-5f37
- Related checks: ja-context-52c9-5f37-reading

#### ja-kanji-5f37 — 強 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 強い · つよい · strong
- Context: 風が強いです。
- Vocabulary: ja-word-kanji-5f37-3044
- Related checks: ja-context-5f37-3044-reading

#### ja-kanji-7df4 — 練 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 練習 · れんしゅう · practice
- Context: 毎日練習します。
- Vocabulary: ja-word-kanji-7df4-7fd2
- Related checks: ja-context-7df4-7fd2-reading

#### ja-kanji-7b54 — 答 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 答え · こたえ · answer
- Context: 答えを書きます。
- Vocabulary: ja-word-kanji-7b54-3048
- Related checks: ja-context-7b54-3048-reading

#### ja-kanji-554f — 問 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 質問 · しつもん · question
- Context: 質問があります。
- Vocabulary: ja-word-kanji-8cea-554f
- Related checks: ja-context-8cea-554f-reading

#### ja-kanji-984c — 題 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 問題 · もんだい · question; problem
- Context: 問題を読みます。
- Vocabulary: ja-word-kanji-554f-984c
- Related checks: ja-context-554f-984c-reading

#### ja-kanji-8a66 — 試 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 試験 · しけん · test; examination
- Context: 試験を受けます。
- Vocabulary: ja-word-kanji-8a66-9a13
- Related checks: ja-context-8a66-9a13-reading

#### ja-kanji-9a13 — 験 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 試験 · しけん · test; examination
- Context: 試験を受けます。
- Vocabulary: ja-word-kanji-8a66-9a13
- Related checks: ja-context-8a66-9a13-reading

#### ja-kanji-5bbf — 宿 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 宿題 · しゅくだい · homework
- Context: 宿題をします。
- Vocabulary: ja-word-kanji-5bbf-984c
- Related checks: ja-context-5bbf-984c-reading

#### ja-kanji-5fd8 — 忘 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 忘れる · わすれる · to forget
- Context: 名前を忘れることがあります。
- Vocabulary: ja-word-kanji-5fd8-308c-308b
- Related checks: ja-context-5fd8-308c-308b-reading

#### ja-kanji-899a — 覚 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 覚える · おぼえる · to remember; to learn by heart
- Context: 新しい言葉を覚える練習です。
- Vocabulary: ja-word-kanji-899a-3048-308b
- Related checks: ja-context-899a-3048-308b-reading

#### ja-kanji-5f85 — 待 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 待つ · まつ · to wait
- Context: ここで待つことにします。
- Vocabulary: ja-word-kanji-5f85-3064
- Related checks: ja-context-5f85-3064-reading

#### ja-kanji-6301 — 持 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 持つ · もつ · to hold; to carry
- Context: 荷物を持つ人です。
- Vocabulary: ja-word-kanji-6301-3064
- Related checks: ja-context-6301-3064-reading

#### ja-kanji-53d6 — 取 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 取る · とる · to take
- Context: 本を取る前に聞きます。
- Vocabulary: ja-word-kanji-53d6-308b
- Related checks: ja-context-53d6-308b-reading

#### ja-kanji-4f7f — 使 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 使う · つかう · to use
- Context: これを使う予定です。
- Vocabulary: ja-word-kanji-4f7f-3046
- Related checks: ja-context-4f7f-3046-reading

#### ja-kanji-4f5c — 作 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 作る · つくる · to make
- Context: 料理を作る時間です。
- Vocabulary: ja-word-kanji-4f5c-308b
- Related checks: ja-context-4f5c-308b-reading

#### ja-kanji-8cb7 — 買 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 買う · かう · to buy
- Context: 本を買う予定です。
- Vocabulary: ja-word-kanji-8cb7-3046
- Related checks: ja-context-8cb7-3046-reading

#### ja-kanji-58f2 — 売 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 売る · うる · to sell
- Context: パンを売る店です。
- Vocabulary: ja-word-kanji-58f2-308b
- Related checks: ja-context-58f2-308b-reading

#### ja-kanji-501f — 借 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 借りる · かりる · to borrow
- Context: 本を借りる予定です。
- Vocabulary: ja-word-kanji-501f-308a-308b
- Related checks: ja-context-501f-308a-308b-reading

#### ja-kanji-8cb8 — 貸 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 貸す · かす · to lend
- Context: 本を貸す前に名前を聞きます。
- Vocabulary: ja-word-kanji-8cb8-3059
- Related checks: ja-context-8cb8-3059-reading

#### ja-kanji-8fd4 — 返 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 返す · かえす · to return something
- Context: 本を返す日です。
- Vocabulary: ja-word-kanji-8fd4-3059
- Related checks: ja-context-8fd4-3059-reading

#### ja-kanji-9001 — 送 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 送る · おくる · to send
- Context: 手紙を送る予定です。
- Vocabulary: ja-word-kanji-9001-308b
- Related checks: ja-context-9001-308b-reading

#### ja-kanji-53d7 — 受 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 受ける · うける · to receive; to take a test
- Context: 試験を受ける予定です。
- Vocabulary: ja-word-kanji-53d7-3051-308b
- Related checks: ja-context-53d7-3051-308b-reading

#### ja-kanji-958b — 開 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 開ける · あける · to open something
- Context: 窓を開ける前に聞きます。
- Vocabulary: ja-word-kanji-958b-3051-308b
- Related checks: ja-context-958b-3051-308b-reading

#### ja-kanji-9589 — 閉 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 閉める · しめる · to close something
- Context: 店を閉める時間です。
- Vocabulary: ja-word-kanji-9589-3081-308b
- Related checks: ja-context-9589-3081-308b-reading

#### ja-kanji-59cb — 始 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 始まる · はじまる · to begin
- Context: 授業が始まる時間です。
- Vocabulary: ja-word-kanji-59cb-307e-308b
- Related checks: ja-context-59cb-307e-308b-reading

#### ja-kanji-7d42 — 終 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 終わる · おわる · to end; to finish
- Context: 仕事が終わる時間です。
- Vocabulary: ja-word-kanji-7d42-308f-308b
- Related checks: ja-context-7d42-308f-308b-reading

#### ja-kanji-6b62 — 止 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 止まる · とまる · to stop
- Context: ここで止まるバスです。
- Vocabulary: ja-word-kanji-6b62-307e-308b
- Related checks: ja-context-6b62-307e-308b-reading

#### ja-kanji-6b69 — 歩 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 歩く · あるく · to walk
- Context: 歩くのが好きです。
- Vocabulary: ja-word-kanji-6b69-304f
- Related checks: ja-context-6b69-304f-reading

#### ja-kanji-8d70 — 走 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 走る · はしる · to run
- Context: 走るのが好きです。
- Vocabulary: ja-word-kanji-8d70-308b
- Related checks: ja-context-8d70-308b-reading

#### ja-kanji-6cf3 — 泳 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 泳ぐ · およぐ · to swim
- Context: 泳ぐのが好きです。
- Vocabulary: ja-word-kanji-6cf3-3050
- Related checks: ja-context-6cf3-3050-reading

#### ja-kanji-904a — 遊 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 遊ぶ · あそぶ · to play; to spend leisure time
- Context: 友達と遊ぶ予定です。
- Vocabulary: ja-word-kanji-904a-3076
- Related checks: ja-context-904a-3076-reading

#### ja-kanji-7acb — 立 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 立つ · たつ · to stand
- Context: ここに立つ人です。
- Vocabulary: ja-word-kanji-7acb-3064
- Related checks: ja-context-7acb-3064-reading

#### ja-kanji-5ea7 — 座 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 座る · すわる · to sit
- Context: ここに座ることにします。
- Vocabulary: ja-word-kanji-5ea7-308b
- Related checks: ja-context-5ea7-308b-reading

#### ja-kanji-4e57 — 乗 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 乗る · のる · to ride; to board
- Context: 電車に乗る予定です。
- Vocabulary: ja-word-kanji-4e57-308b
- Related checks: ja-context-4e57-308b-reading

#### ja-kanji-964d — 降 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 降りる · おりる · to get off; to descend
- Context: 次の駅で降りる予定です。
- Vocabulary: ja-word-kanji-964d-308a-308b
- Related checks: ja-context-964d-308a-308b-reading

#### ja-kanji-5e30 — 帰 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 帰る · かえる · to go home; to return
- Context: 家に帰る時間です。
- Vocabulary: ja-word-kanji-5e30-308b
- Related checks: ja-context-5e30-308b-reading

#### ja-kanji-62bc — 押 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 押す · おす · to push; to press
- Context: このボタンを押すと開きます。
- Vocabulary: ja-word-kanji-62bc-3059
- Related checks: ja-context-62bc-3059-reading

#### ja-kanji-5f15 — 引 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 引く · ひく · to pull
- Context: この戸は引くと開きます。
- Vocabulary: ja-word-kanji-5f15-304f
- Related checks: ja-context-5f15-304f-reading

#### ja-kanji-5c11 — 少 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 少ない · すくない · few; little
- Context: 人が少ないです。
- Vocabulary: ja-word-kanji-5c11-306a-3044
- Related checks: ja-context-5c11-306a-3044-reading

#### ja-kanji-591a — 多 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 多い · おおい · many; much
- Context: 人が多いです。
- Vocabulary: ja-word-kanji-591a-3044
- Related checks: ja-context-591a-3044-reading

#### ja-kanji-5168 — 全 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 全部 · ぜんぶ · all; everything
- Context: 全部ください。
- Vocabulary: ja-word-kanji-5168-90e8
- Related checks: ja-context-5168-90e8-reading

#### ja-kanji-540c — 同 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 同じ · おなじ · the same
- Context: 同じ本です。
- Vocabulary: ja-word-kanji-540c-3058
- Related checks: ja-context-540c-3058-reading

#### ja-kanji-5225 — 別 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 別 · べつ · different; separate
- Context: 別の本です。
- Vocabulary: ja-word-kanji-5225
- Related checks: ja-context-5225-reading

#### ja-kanji-4ed6 — 他 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 他 · ほか · other; another
- Context: 他の店に行きます。
- Vocabulary: ja-word-kanji-4ed6
- Related checks: ja-context-4ed6-reading

#### ja-kanji-6709 — 有 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 有名 · ゆうめい · famous
- Context: 有名な店です。
- Vocabulary: ja-word-kanji-6709-540d
- Related checks: ja-context-6709-540d-reading

#### ja-kanji-7121 — 無 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 無料 · むりょう · free of charge
- Context: ここは無料です。
- Vocabulary: ja-word-kanji-7121-6599
- Related checks: ja-context-7121-6599-reading

#### ja-kanji-5fc5 — 必 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 必要 · ひつよう · necessary
- Context: 予約が必要です。
- Vocabulary: ja-word-kanji-5fc5-8981
- Related checks: ja-context-5fc5-8981-reading

#### ja-kanji-8981 — 要 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 必要 · ひつよう · necessary
- Context: 予約が必要です。
- Vocabulary: ja-word-kanji-5fc5-8981
- Related checks: ja-context-5fc5-8981-reading

#### ja-kanji-5229 — 利 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 便利 · べんり · convenient
- Context: この町は便利です。
- Vocabulary: ja-word-kanji-4fbf-5229
- Related checks: ja-context-4fbf-5229-reading

#### ja-kanji-4fbf — 便 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 便利 · べんり · convenient
- Context: この町は便利です。
- Vocabulary: ja-word-kanji-4fbf-5229
- Related checks: ja-context-4fbf-5229-reading

#### ja-kanji-4e0d — 不 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 不便 · ふべん · inconvenient
- Context: ここは少し不便です。
- Vocabulary: ja-word-kanji-4e0d-4fbf
- Related checks: ja-context-4e0d-4fbf-reading

#### ja-kanji-60aa — 悪 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 悪い · わるい · bad
- Context: 天気が悪いです。
- Vocabulary: ja-word-kanji-60aa-3044
- Related checks: ja-context-60aa-3044-reading

#### ja-kanji-91cd — 重 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 重い · おもい · heavy
- Context: この本は重いです。
- Vocabulary: ja-word-kanji-91cd-3044
- Related checks: ja-context-91cd-3044-reading

#### ja-kanji-8efd — 軽 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 軽い · かるい · light in weight
- Context: この本は軽いです。
- Vocabulary: ja-word-kanji-8efd-3044
- Related checks: ja-context-8efd-3044-reading

#### ja-kanji-5e83 — 広 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 広い · ひろい · spacious; wide
- Context: 広い部屋です。
- Vocabulary: ja-word-kanji-5e83-3044
- Related checks: ja-context-5e83-3044-reading

#### ja-kanji-72ed — 狭 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 狭い · せまい · narrow; cramped
- Context: 狭い部屋です。
- Vocabulary: ja-word-kanji-72ed-3044
- Related checks: ja-context-72ed-3044-reading

#### ja-kanji-77ed — 短 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 短い · みじかい · short
- Context: 短い文です。
- Vocabulary: ja-word-kanji-77ed-3044
- Related checks: ja-context-77ed-3044-reading

#### ja-kanji-4f4e — 低 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 低い · ひくい · low
- Context: 低い山です。
- Vocabulary: ja-word-kanji-4f4e-3044
- Related checks: ja-context-4f4e-3044-reading

#### ja-kanji-65e9 — 早 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 早い · はやい · early
- Context: 今日は早い電車に乗ります。
- Vocabulary: ja-word-kanji-65e9-3044
- Related checks: ja-context-65e9-3044-reading

#### ja-kanji-9045 — 遅 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 遅い · おそい · late; slow
- Context: 今日は帰りが遅いです。
- Vocabulary: ja-word-kanji-9045-3044
- Related checks: ja-context-9045-3044-reading

#### ja-kanji-901f — 速 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 速い · はやい · fast
- Context: 速い電車です。
- Vocabulary: ja-word-kanji-901f-3044
- Related checks: ja-context-901f-3044-reading

#### ja-kanji-6625 — 春 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 春 · はる · spring
- Context: 春に花が咲きます。
- Vocabulary: ja-word-kanji-6625
- Related checks: ja-context-6625-reading

#### ja-kanji-590f — 夏 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 夏 · なつ · summer
- Context: 夏は暑いです。
- Vocabulary: ja-word-kanji-590f
- Related checks: ja-context-590f-reading

#### ja-kanji-79cb — 秋 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 秋 · あき · autumn
- Context: 秋は涼しいです。
- Vocabulary: ja-word-kanji-79cb
- Related checks: ja-context-79cb-reading

#### ja-kanji-51ac — 冬 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 冬 · ふゆ · winter
- Context: 冬は寒いです。
- Vocabulary: ja-word-kanji-51ac
- Related checks: ja-context-51ac-reading

#### ja-kanji-96ea — 雪 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 雪 · ゆき · snow
- Context: 雪が降っています。
- Vocabulary: ja-word-kanji-96ea
- Related checks: ja-context-96ea-reading

#### ja-kanji-98a8 — 風 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 風 · かぜ · wind
- Context: 風が強いです。
- Vocabulary: ja-word-kanji-98a8
- Related checks: ja-context-98a8-reading

#### ja-kanji-96f2 — 雲 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 雲 · くも · cloud
- Context: 雲が見えます。
- Vocabulary: ja-word-kanji-96f2
- Related checks: ja-context-96f2-reading

#### ja-kanji-6674 — 晴 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 晴れ · はれ · clear weather
- Context: 今日は晴れです。
- Vocabulary: ja-word-kanji-6674-308c
- Related checks: ja-context-6674-308c-reading

#### ja-kanji-6697 — 暗 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 暗い · くらい · dark
- Context: 部屋が暗いです。
- Vocabulary: ja-word-kanji-6697-3044
- Related checks: ja-context-6697-3044-reading

#### ja-kanji-660e — 明 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 明るい · あかるい · bright
- Context: 明るい部屋です。
- Vocabulary: ja-word-kanji-660e-308b-3044
- Related checks: ja-context-660e-308b-3044-reading

#### ja-kanji-5915 — 夕 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 夕方 · ゆうがた · early evening
- Context: 夕方に会いましょう。
- Vocabulary: ja-word-kanji-5915-65b9
- Related checks: ja-context-5915-65b9-reading

#### ja-kanji-6669 — 晩 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 今晩 · こんばん · this evening; tonight
- Context: 今晩、電話します。
- Vocabulary: ja-word-kanji-4eca-6669
- Related checks: ja-context-4eca-6669-reading

#### ja-kanji-4e88 — 予 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 予約 · よやく · reservation
- Context: 予約をします。
- Vocabulary: ja-word-kanji-4e88-7d04
- Related checks: ja-context-4e88-7d04-reading

#### ja-kanji-7d04 — 約 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 予約 · よやく · reservation
- Context: 予約をします。
- Vocabulary: ja-word-kanji-4e88-7d04
- Related checks: ja-context-4e88-7d04-reading

#### ja-kanji-8a08 — 計 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 計画 · けいかく · plan
- Context: 旅行の計画を立てます。
- Vocabulary: ja-word-kanji-8a08-753b
- Related checks: ja-context-8a08-753b-reading

#### ja-kanji-753b — 画 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 計画 · けいかく · plan
- Context: 旅行の計画を立てます。
- Vocabulary: ja-word-kanji-8a08-753b
- Related checks: ja-context-8a08-753b-reading

#### ja-kanji-5ea6 — 度 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 一度 · いちど · once; one time
- Context: 一度行きました。
- Vocabulary: ja-word-kanji-4e00-5ea6
- Related checks: ja-context-4e00-5ea6-reading

#### ja-kanji-98ef — 飯 (stage-b)

- [ ] Qualified review; notes: pending
- Word: ご飯 · ごはん · cooked rice; meal
- Context: ご飯を食べます。
- Vocabulary: ja-word-kanji-3054-98ef
- Related checks: ja-context-3054-98ef-reading

#### ja-kanji-8089 — 肉 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 肉 · にく · meat
- Context: 肉を食べます。
- Vocabulary: ja-word-kanji-8089
- Related checks: ja-context-8089-reading

#### ja-kanji-7c73 — 米 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 米 · こめ · uncooked rice
- Context: 米を洗います。
- Vocabulary: ja-word-kanji-7c73
- Related checks: ja-context-7c73-reading

#### ja-kanji-725b — 牛 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 牛乳 · ぎゅうにゅう · milk
- Context: 牛乳を飲みます。
- Vocabulary: ja-word-kanji-725b-4e73
- Related checks: ja-context-725b-4e73-reading

#### ja-kanji-8c5a — 豚 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 豚肉 · ぶたにく · pork
- Context: 豚肉を買います。
- Vocabulary: ja-word-kanji-8c5a-8089
- Related checks: ja-context-8c5a-8089-reading

#### ja-kanji-9d8f — 鶏 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 鶏肉 · とりにく · chicken meat
- Context: 鶏肉を買います。
- Vocabulary: ja-word-kanji-9d8f-8089
- Related checks: ja-context-9d8f-8089-reading

#### ja-kanji-5375 — 卵 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 卵 · たまご · egg
- Context: 卵を買います。
- Vocabulary: ja-word-kanji-5375
- Related checks: ja-context-5375-reading

#### ja-kanji-91ce — 野 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 野菜 · やさい · vegetables
- Context: 野菜を食べます。
- Vocabulary: ja-word-kanji-91ce-83dc
- Related checks: ja-context-91ce-83dc-reading

#### ja-kanji-83dc — 菜 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 野菜 · やさい · vegetables
- Context: 野菜を食べます。
- Vocabulary: ja-word-kanji-91ce-83dc
- Related checks: ja-context-91ce-83dc-reading

#### ja-kanji-679c — 果 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 果物 · くだもの · fruit
- Context: 果物を食べます。
- Vocabulary: ja-word-kanji-679c-7269
- Related checks: ja-context-679c-7269-reading

#### ja-kanji-5869 — 塩 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 塩 · しお · salt
- Context: 塩を入れます。
- Vocabulary: ja-word-kanji-5869
- Related checks: ja-context-5869-reading

#### ja-kanji-7802 — 砂 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 砂糖 · さとう · sugar
- Context: 砂糖を入れます。
- Vocabulary: ja-word-kanji-7802-7cd6
- Related checks: ja-context-7802-7cd6-reading

#### ja-kanji-7cd6 — 糖 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 砂糖 · さとう · sugar
- Context: 砂糖を入れます。
- Vocabulary: ja-word-kanji-7802-7cd6
- Related checks: ja-context-7802-7cd6-reading

#### ja-kanji-6cb9 — 油 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 油 · あぶら · oil
- Context: 油を使います。
- Vocabulary: ja-word-kanji-6cb9
- Related checks: ja-context-6cb9-reading

#### ja-kanji-5473 — 味 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 味 · あじ · taste; flavor
- Context: 味を見ます。
- Vocabulary: ja-word-kanji-5473
- Related checks: ja-context-5473-reading

#### ja-kanji-7518 — 甘 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 甘い · あまい · sweet
- Context: 甘いお菓子です。
- Vocabulary: ja-word-kanji-7518-3044
- Related checks: ja-context-7518-3044-reading

#### ja-kanji-8f9b — 辛 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 辛い · からい · spicy; hot in taste
- Context: 辛い料理です。
- Vocabulary: ja-word-kanji-8f9b-3044
- Related checks: ja-context-8f9b-3044-reading

#### ja-kanji-9178 — 酸 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 酸っぱい · すっぱい · sour
- Context: 酸っぱい味です。
- Vocabulary: ja-word-kanji-9178-3063-3071-3044
- Related checks: ja-context-9178-3063-3071-3044-reading

#### ja-kanji-82e6 — 苦 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 苦い · にがい · bitter
- Context: 苦い薬です。
- Vocabulary: ja-word-kanji-82e6-3044
- Related checks: ja-context-82e6-3044-reading

#### ja-kanji-76bf — 皿 (stage-b)

- [ ] Qualified review; notes: pending
- Word: 皿 · さら · plate; dish
- Context: 皿を洗います。
- Vocabulary: ja-word-kanji-76bf
- Related checks: ja-context-76bf-reading

### Added vocabulary records

#### ja-word-kanji-4e00-3064

- [ ] Qualified review; notes: pending
- 一つ · ひとつ · one thing
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 一つください。
- Structured reading segments: [{"surface":"一つ","reading":"ひとつ","vocabulary_id":"ja-word-kanji-4e00-3064"},{"surface":"ください。"}]

#### ja-word-kanji-4e8c-3064

- [ ] Qualified review; notes: pending
- 二つ · ふたつ · two things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 二つください。
- Structured reading segments: [{"surface":"二つ","reading":"ふたつ","vocabulary_id":"ja-word-kanji-4e8c-3064"},{"surface":"ください。"}]

#### ja-word-kanji-4e09-3064

- [ ] Qualified review; notes: pending
- 三つ · みっつ · three things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 三つください。
- Structured reading segments: [{"surface":"三つ","reading":"みっつ","vocabulary_id":"ja-word-kanji-4e09-3064"},{"surface":"ください。"}]

#### ja-word-kanji-56db-3064

- [ ] Qualified review; notes: pending
- 四つ · よっつ · four things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 四つあります。
- Structured reading segments: [{"surface":"四つ","reading":"よっつ","vocabulary_id":"ja-word-kanji-56db-3064"},{"surface":"あります。"}]

#### ja-word-kanji-4e94-3064

- [ ] Qualified review; notes: pending
- 五つ · いつつ · five things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 五つあります。
- Structured reading segments: [{"surface":"五つ","reading":"いつつ","vocabulary_id":"ja-word-kanji-4e94-3064"},{"surface":"あります。"}]

#### ja-word-kanji-516d-3064

- [ ] Qualified review; notes: pending
- 六つ · むっつ · six things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 六つあります。
- Structured reading segments: [{"surface":"六つ","reading":"むっつ","vocabulary_id":"ja-word-kanji-516d-3064"},{"surface":"あります。"}]

#### ja-word-kanji-4e03-3064

- [ ] Qualified review; notes: pending
- 七つ · ななつ · seven things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 七つあります。
- Structured reading segments: [{"surface":"七つ","reading":"ななつ","vocabulary_id":"ja-word-kanji-4e03-3064"},{"surface":"あります。"}]

#### ja-word-kanji-516b-3064

- [ ] Qualified review; notes: pending
- 八つ · やっつ · eight things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 八つあります。
- Structured reading segments: [{"surface":"八つ","reading":"やっつ","vocabulary_id":"ja-word-kanji-516b-3064"},{"surface":"あります。"}]

#### ja-word-kanji-4e5d-3064

- [ ] Qualified review; notes: pending
- 九つ · ここのつ · nine things
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 九つあります。
- Structured reading segments: [{"surface":"九つ","reading":"ここのつ","vocabulary_id":"ja-word-kanji-4e5d-3064"},{"surface":"あります。"}]

#### ja-word-kanji-5341

- [ ] Qualified review; notes: pending
- 十 · じゅう · ten
- Part of speech/register: numeral / neutral
- Stage/status: stage-a / draft
- Example: 十まで数えます。
- Structured reading segments: [{"surface":"十","reading":"じゅう","vocabulary_id":"ja-word-kanji-5341"},{"surface":"まで数えます。"}]

#### ja-word-kanji-767e

- [ ] Qualified review; notes: pending
- 百 · ひゃく · one hundred
- Part of speech/register: numeral / neutral
- Stage/status: stage-a / draft
- Example: 百まで数えます。
- Structured reading segments: [{"surface":"百","reading":"ひゃく","vocabulary_id":"ja-word-kanji-767e"},{"surface":"まで数えます。"}]

#### ja-word-kanji-5343-5186

- [ ] Qualified review; notes: pending
- 千円 · せんえん · one thousand yen
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 千円です。
- Structured reading segments: [{"surface":"千円","reading":"せんえん","vocabulary_id":"ja-word-kanji-5343-5186"},{"surface":"です。"}]

#### ja-word-kanji-5186

- [ ] Qualified review; notes: pending
- 円 · えん · yen
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 円で払います。
- Structured reading segments: [{"surface":"円","reading":"えん","vocabulary_id":"ja-word-kanji-5186"},{"surface":"で払います。"}]

#### ja-word-kanji-4e00-5e74

- [ ] Qualified review; notes: pending
- 一年 · いちねん · one year
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 一年かかります。
- Structured reading segments: [{"surface":"一年","reading":"いちねん","vocabulary_id":"ja-word-kanji-4e00-5e74"},{"surface":"かかります。"}]

#### ja-word-kanji-4eca

- [ ] Qualified review; notes: pending
- 今 · いま · now
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 今、行きます。
- Structured reading segments: [{"surface":"今","reading":"いま","vocabulary_id":"ja-word-kanji-4eca"},{"surface":"、行きます。"}]

#### ja-word-kanji-6bce-65e5

- [ ] Qualified review; notes: pending
- 毎日 · まいにち · every day
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 毎日読みます。
- Structured reading segments: [{"surface":"毎日","reading":"まいにち","vocabulary_id":"ja-word-kanji-6bce-65e5"},{"surface":"読みます。"}]

#### ja-word-kanji-6765-9031

- [ ] Qualified review; notes: pending
- 来週 · らいしゅう · next week
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 来週、会いましょう。
- Structured reading segments: [{"surface":"来週","reading":"らいしゅう","vocabulary_id":"ja-word-kanji-6765-9031"},{"surface":"、会いましょう。"}]

#### ja-word-kanji-4e94-5206

- [ ] Qualified review; notes: pending
- 五分 · ごふん · five minutes
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 五分かかります。
- Structured reading segments: [{"surface":"五分","reading":"ごふん","vocabulary_id":"ja-word-kanji-4e94-5206"},{"surface":"かかります。"}]

#### ja-word-kanji-534a-5206

- [ ] Qualified review; notes: pending
- 半分 · はんぶん · half
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 半分ください。
- Structured reading segments: [{"surface":"半分","reading":"はんぶん","vocabulary_id":"ja-word-kanji-534a-5206"},{"surface":"ください。"}]

#### ja-word-kanji-5348-524d

- [ ] Qualified review; notes: pending
- 午前 · ごぜん · morning; a.m.
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 午前に行きます。
- Structured reading segments: [{"surface":"午前","reading":"ごぜん","vocabulary_id":"ja-word-kanji-5348-524d"},{"surface":"に行きます。"}]

#### ja-word-kanji-524d

- [ ] Qualified review; notes: pending
- 前 · まえ · front; before
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 駅の前です。
- Structured reading segments: [{"surface":"駅の"},{"surface":"前","reading":"まえ","vocabulary_id":"ja-word-kanji-524d"},{"surface":"です。"}]

#### ja-word-kanji-5f8c-308d

- [ ] Qualified review; notes: pending
- 後ろ · うしろ · behind; the back
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 家の後ろです。
- Structured reading segments: [{"surface":"家の"},{"surface":"後ろ","reading":"うしろ","vocabulary_id":"ja-word-kanji-5f8c-308d"},{"surface":"です。"}]

#### ja-word-kanji-671d

- [ ] Qualified review; notes: pending
- 朝 · あさ · morning
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 朝、お茶を飲みます。
- Structured reading segments: [{"surface":"朝","reading":"あさ","vocabulary_id":"ja-word-kanji-671d"},{"surface":"、お茶を飲みます。"}]

#### ja-word-kanji-663c

- [ ] Qualified review; notes: pending
- 昼 · ひる · daytime; noon
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 昼に会いましょう。
- Structured reading segments: [{"surface":"昼","reading":"ひる","vocabulary_id":"ja-word-kanji-663c"},{"surface":"に会いましょう。"}]

#### ja-word-kanji-591c

- [ ] Qualified review; notes: pending
- 夜 · よる · night
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 夜、本を読みます。
- Structured reading segments: [{"surface":"夜","reading":"よる","vocabulary_id":"ja-word-kanji-591c"},{"surface":"、本を読みます。"}]

#### ja-word-kanji-4eba

- [ ] Qualified review; notes: pending
- 人 · ひと · person
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 人がいます。
- Structured reading segments: [{"surface":"人","reading":"ひと","vocabulary_id":"ja-word-kanji-4eba"},{"surface":"がいます。"}]

#### ja-word-kanji-7537-306e-5b50

- [ ] Qualified review; notes: pending
- 男の子 · おとこのこ · boy
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 男の子がいます。
- Structured reading segments: [{"surface":"男の子","reading":"おとこのこ","vocabulary_id":"ja-word-kanji-7537-306e-5b50"},{"surface":"がいます。"}]

#### ja-word-kanji-5973-306e-5b50

- [ ] Qualified review; notes: pending
- 女の子 · おんなのこ · girl
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 女の子がいます。
- Structured reading segments: [{"surface":"女の子","reading":"おんなのこ","vocabulary_id":"ja-word-kanji-5973-306e-5b50"},{"surface":"がいます。"}]

#### ja-word-kanji-5b50-3069-3082

- [ ] Qualified review; notes: pending
- 子ども · こども · child
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 子どもがいます。
- Structured reading segments: [{"surface":"子ども","reading":"こども","vocabulary_id":"ja-word-kanji-5b50-3069-3082"},{"surface":"がいます。"}]

#### ja-word-kanji-7236

- [ ] Qualified review; notes: pending
- 父 · ちち · my father
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 父は家にいます。
- Structured reading segments: [{"surface":"父","reading":"ちち","vocabulary_id":"ja-word-kanji-7236"},{"surface":"は家にいます。"}]

#### ja-word-kanji-6bcd

- [ ] Qualified review; notes: pending
- 母 · はは · my mother
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 母は家にいます。
- Structured reading segments: [{"surface":"母","reading":"はは","vocabulary_id":"ja-word-kanji-6bcd"},{"surface":"は家にいます。"}]

#### ja-word-kanji-53cb-9054

- [ ] Qualified review; notes: pending
- 友達 · ともだち · friend
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 友達と行きます。
- Structured reading segments: [{"surface":"友達","reading":"ともだち","vocabulary_id":"ja-word-kanji-53cb-9054"},{"surface":"と行きます。"}]

#### ja-word-kanji-5148-751f

- [ ] Qualified review; notes: pending
- 先生 · せんせい · teacher
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 先生に聞きます。
- Structured reading segments: [{"surface":"先生","reading":"せんせい","vocabulary_id":"ja-word-kanji-5148-751f"},{"surface":"に聞きます。"}]

#### ja-word-kanji-5b66-751f

- [ ] Qualified review; notes: pending
- 学生 · がくせい · student
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 私は学生です。
- Structured reading segments: [{"surface":"私は"},{"surface":"学生","reading":"がくせい","vocabulary_id":"ja-word-kanji-5b66-751f"},{"surface":"です。"}]

#### ja-word-kanji-540d-524d

- [ ] Qualified review; notes: pending
- 名前 · なまえ · name
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 名前を書きます。
- Structured reading segments: [{"surface":"名前","reading":"なまえ","vocabulary_id":"ja-word-kanji-540d-524d"},{"surface":"を書きます。"}]

#### ja-word-kanji-79c1

- [ ] Qualified review; notes: pending
- 私 · わたし · I; me
- Part of speech/register: pronoun / neutral
- Stage/status: stage-a / draft
- Example: 私はアキです。
- Structured reading segments: [{"surface":"私","reading":"わたし","vocabulary_id":"ja-word-kanji-79c1"},{"surface":"はアキです。"}]

#### ja-word-kanji-5c71

- [ ] Qualified review; notes: pending
- 山 · やま · mountain
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 山が見えます。
- Structured reading segments: [{"surface":"山","reading":"やま","vocabulary_id":"ja-word-kanji-5c71"},{"surface":"が見えます。"}]

#### ja-word-kanji-5ddd

- [ ] Qualified review; notes: pending
- 川 · かわ · river
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 川があります。
- Structured reading segments: [{"surface":"川","reading":"かわ","vocabulary_id":"ja-word-kanji-5ddd"},{"surface":"があります。"}]

#### ja-word-kanji-7a7a

- [ ] Qualified review; notes: pending
- 空 · そら · sky
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 空が青いです。
- Structured reading segments: [{"surface":"空","reading":"そら","vocabulary_id":"ja-word-kanji-7a7a"},{"surface":"が青いです。"}]

#### ja-word-kanji-96e8

- [ ] Qualified review; notes: pending
- 雨 · あめ · rain
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 雨が降っています。
- Structured reading segments: [{"surface":"雨","reading":"あめ","vocabulary_id":"ja-word-kanji-96e8"},{"surface":"が降っています。"}]

#### ja-word-kanji-5929-6c17

- [ ] Qualified review; notes: pending
- 天気 · てんき · weather
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 天気がいいです。
- Structured reading segments: [{"surface":"天気","reading":"てんき","vocabulary_id":"ja-word-kanji-5929-6c17"},{"surface":"がいいです。"}]

#### ja-word-kanji-5143-6c17

- [ ] Qualified review; notes: pending
- 元気 · げんき · healthy; in good spirits
- Part of speech/register: na-adjective / neutral
- Stage/status: stage-a / draft
- Example: 元気です。
- Structured reading segments: [{"surface":"元気","reading":"げんき","vocabulary_id":"ja-word-kanji-5143-6c17"},{"surface":"です。"}]

#### ja-word-kanji-82b1

- [ ] Qualified review; notes: pending
- 花 · はな · flower
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 花を見ます。
- Structured reading segments: [{"surface":"花","reading":"はな","vocabulary_id":"ja-word-kanji-82b1"},{"surface":"を見ます。"}]

#### ja-word-kanji-72ac

- [ ] Qualified review; notes: pending
- 犬 · いぬ · dog
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 犬がいます。
- Structured reading segments: [{"surface":"犬","reading":"いぬ","vocabulary_id":"ja-word-kanji-72ac"},{"surface":"がいます。"}]

#### ja-word-kanji-732b

- [ ] Qualified review; notes: pending
- 猫 · ねこ · cat
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 猫がいます。
- Structured reading segments: [{"surface":"猫","reading":"ねこ","vocabulary_id":"ja-word-kanji-732b"},{"surface":"がいます。"}]

#### ja-word-kanji-9ce5

- [ ] Qualified review; notes: pending
- 鳥 · とり · bird
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 鳥がいます。
- Structured reading segments: [{"surface":"鳥","reading":"とり","vocabulary_id":"ja-word-kanji-9ce5"},{"surface":"がいます。"}]

#### ja-word-kanji-9b5a

- [ ] Qualified review; notes: pending
- 魚 · さかな · fish
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 魚を食べます。
- Structured reading segments: [{"surface":"魚","reading":"さかな","vocabulary_id":"ja-word-kanji-9b5a"},{"surface":"を食べます。"}]

#### ja-word-kanji-8eca

- [ ] Qualified review; notes: pending
- 車 · くるま · car
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 車で行きます。
- Structured reading segments: [{"surface":"車","reading":"くるま","vocabulary_id":"ja-word-kanji-8eca"},{"surface":"で行きます。"}]

#### ja-word-kanji-96fb-8eca

- [ ] Qualified review; notes: pending
- 電車 · でんしゃ · train
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 電車で行きます。
- Structured reading segments: [{"surface":"電車","reading":"でんしゃ","vocabulary_id":"ja-word-kanji-96fb-8eca"},{"surface":"で行きます。"}]

#### ja-word-kanji-9053

- [ ] Qualified review; notes: pending
- 道 · みち · road; way
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: この道を行きます。
- Structured reading segments: [{"surface":"この"},{"surface":"道","reading":"みち","vocabulary_id":"ja-word-kanji-9053"},{"surface":"を行きます。"}]

#### ja-word-kanji-5e97

- [ ] Qualified review; notes: pending
- 店 · みせ · shop
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 店に入ります。
- Structured reading segments: [{"surface":"店","reading":"みせ","vocabulary_id":"ja-word-kanji-5e97"},{"surface":"に入ります。"}]

#### ja-word-kanji-4f1a-793e

- [ ] Qualified review; notes: pending
- 会社 · かいしゃ · company
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 会社に行きます。
- Structured reading segments: [{"surface":"会社","reading":"かいしゃ","vocabulary_id":"ja-word-kanji-4f1a-793e"},{"surface":"に行きます。"}]

#### ja-word-kanji-56fd

- [ ] Qualified review; notes: pending
- 国 · くに · country
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: どの国ですか。
- Structured reading segments: [{"surface":"どの"},{"surface":"国","reading":"くに","vocabulary_id":"ja-word-kanji-56fd"},{"surface":"ですか。"}]

#### ja-word-kanji-5916

- [ ] Qualified review; notes: pending
- 外 · そと · outside
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 外に出ます。
- Structured reading segments: [{"surface":"外","reading":"そと","vocabulary_id":"ja-word-kanji-5916"},{"surface":"に出ます。"}]

#### ja-word-kanji-4e2d

- [ ] Qualified review; notes: pending
- 中 · なか · inside
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 中に入ります。
- Structured reading segments: [{"surface":"中","reading":"なか","vocabulary_id":"ja-word-kanji-4e2d"},{"surface":"に入ります。"}]

#### ja-word-kanji-4e0a

- [ ] Qualified review; notes: pending
- 上 · うえ · above; on top
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 机の上です。
- Structured reading segments: [{"surface":"机の"},{"surface":"上","reading":"うえ","vocabulary_id":"ja-word-kanji-4e0a"},{"surface":"です。"}]

#### ja-word-kanji-4e0b

- [ ] Qualified review; notes: pending
- 下 · した · below; underneath
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 机の下です。
- Structured reading segments: [{"surface":"机の"},{"surface":"下","reading":"した","vocabulary_id":"ja-word-kanji-4e0b"},{"surface":"です。"}]

#### ja-word-kanji-5de6

- [ ] Qualified review; notes: pending
- 左 · ひだり · left
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 左に曲がります。
- Structured reading segments: [{"surface":"左","reading":"ひだり","vocabulary_id":"ja-word-kanji-5de6"},{"surface":"に曲がります。"}]

#### ja-word-kanji-53f3

- [ ] Qualified review; notes: pending
- 右 · みぎ · right
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 右に曲がります。
- Structured reading segments: [{"surface":"右","reading":"みぎ","vocabulary_id":"ja-word-kanji-53f3"},{"surface":"に曲がります。"}]

#### ja-word-kanji-5317

- [ ] Qualified review; notes: pending
- 北 · きた · north
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 北へ行きます。
- Structured reading segments: [{"surface":"北","reading":"きた","vocabulary_id":"ja-word-kanji-5317"},{"surface":"へ行きます。"}]

#### ja-word-kanji-5357

- [ ] Qualified review; notes: pending
- 南 · みなみ · south
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 南へ行きます。
- Structured reading segments: [{"surface":"南","reading":"みなみ","vocabulary_id":"ja-word-kanji-5357"},{"surface":"へ行きます。"}]

#### ja-word-kanji-6771

- [ ] Qualified review; notes: pending
- 東 · ひがし · east
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 東へ行きます。
- Structured reading segments: [{"surface":"東","reading":"ひがし","vocabulary_id":"ja-word-kanji-6771"},{"surface":"へ行きます。"}]

#### ja-word-kanji-897f

- [ ] Qualified review; notes: pending
- 西 · にし · west
- Part of speech/register: noun / neutral
- Stage/status: stage-a / draft
- Example: 西へ行きます。
- Structured reading segments: [{"surface":"西","reading":"にし","vocabulary_id":"ja-word-kanji-897f"},{"surface":"へ行きます。"}]

#### ja-word-kanji-5927-304d-3044

- [ ] Qualified review; notes: pending
- 大きい · おおきい · big
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 大きい家です。
- Structured reading segments: [{"surface":"大きい","reading":"おおきい","vocabulary_id":"ja-word-kanji-5927-304d-3044"},{"surface":"家です。"}]

#### ja-word-kanji-5c0f-3055-3044

- [ ] Qualified review; notes: pending
- 小さい · ちいさい · small
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 小さい店です。
- Structured reading segments: [{"surface":"小さい","reading":"ちいさい","vocabulary_id":"ja-word-kanji-5c0f-3055-3044"},{"surface":"店です。"}]

#### ja-word-kanji-9577-3044

- [ ] Qualified review; notes: pending
- 長い · ながい · long
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 長い道です。
- Structured reading segments: [{"surface":"長い","reading":"ながい","vocabulary_id":"ja-word-kanji-9577-3044"},{"surface":"道です。"}]

#### ja-word-kanji-9ad8-3044

- [ ] Qualified review; notes: pending
- 高い · たかい · high; expensive
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: この本は高いです。
- Structured reading segments: [{"surface":"この本は"},{"surface":"高い","reading":"たかい","vocabulary_id":"ja-word-kanji-9ad8-3044"},{"surface":"です。"}]

#### ja-word-kanji-5b89-3044

- [ ] Qualified review; notes: pending
- 安い · やすい · inexpensive
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: この本は安いです。
- Structured reading segments: [{"surface":"この本は"},{"surface":"安い","reading":"やすい","vocabulary_id":"ja-word-kanji-5b89-3044"},{"surface":"です。"}]

#### ja-word-kanji-65b0-3057-3044

- [ ] Qualified review; notes: pending
- 新しい · あたらしい · new
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 新しい本です。
- Structured reading segments: [{"surface":"新しい","reading":"あたらしい","vocabulary_id":"ja-word-kanji-65b0-3057-3044"},{"surface":"本です。"}]

#### ja-word-kanji-53e4-3044

- [ ] Qualified review; notes: pending
- 古い · ふるい · old
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 古い家です。
- Structured reading segments: [{"surface":"古い","reading":"ふるい","vocabulary_id":"ja-word-kanji-53e4-3044"},{"surface":"家です。"}]

#### ja-word-kanji-767d-3044

- [ ] Qualified review; notes: pending
- 白い · しろい · white
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 白い紙です。
- Structured reading segments: [{"surface":"白い","reading":"しろい","vocabulary_id":"ja-word-kanji-767d-3044"},{"surface":"紙です。"}]

#### ja-word-kanji-9ed2-3044

- [ ] Qualified review; notes: pending
- 黒い · くろい · black
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 黒い車です。
- Structured reading segments: [{"surface":"黒い","reading":"くろい","vocabulary_id":"ja-word-kanji-9ed2-3044"},{"surface":"車です。"}]

#### ja-word-kanji-8d64-3044

- [ ] Qualified review; notes: pending
- 赤い · あかい · red
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 赤い花です。
- Structured reading segments: [{"surface":"赤い","reading":"あかい","vocabulary_id":"ja-word-kanji-8d64-3044"},{"surface":"花です。"}]

#### ja-word-kanji-9752-3044

- [ ] Qualified review; notes: pending
- 青い · あおい · blue
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-a / draft
- Example: 青い空です。
- Structured reading segments: [{"surface":"青い","reading":"あおい","vocabulary_id":"ja-word-kanji-9752-3044"},{"surface":"空です。"}]

#### ja-word-kanji-597d-304d

- [ ] Qualified review; notes: pending
- 好き · すき · liked; favorite
- Part of speech/register: na-adjective / neutral
- Stage/status: stage-a / draft
- Example: お茶が好きです。
- Structured reading segments: [{"surface":"お茶が"},{"surface":"好き","reading":"すき","vocabulary_id":"ja-word-kanji-597d-304d"},{"surface":"です。"}]

#### ja-word-kanji-98df-3079-308b

- [ ] Qualified review; notes: pending
- 食べる · たべる · to eat
- Part of speech/register: verb / neutral
- Stage/status: stage-a / draft
- Example: 何を食べるか決めます。
- Structured reading segments: [{"surface":"何を"},{"surface":"食べる","reading":"たべる","vocabulary_id":"ja-word-kanji-98df-3079-308b"},{"surface":"か決めます。"}]

#### ja-word-kanji-98f2-3080

- [ ] Qualified review; notes: pending
- 飲む · のむ · to drink
- Part of speech/register: verb / neutral
- Stage/status: stage-a / draft
- Example: 何を飲むか決めます。
- Structured reading segments: [{"surface":"何を"},{"surface":"飲む","reading":"のむ","vocabulary_id":"ja-word-kanji-98f2-3080"},{"surface":"か決めます。"}]

#### ja-word-kanji-898b-308b

- [ ] Qualified review; notes: pending
- 見る · みる · to see; to watch
- Part of speech/register: verb / neutral
- Stage/status: stage-a / draft
- Example: 映画を見るのが好きです。
- Structured reading segments: [{"surface":"映画を"},{"surface":"見る","reading":"みる","vocabulary_id":"ja-word-kanji-898b-308b"},{"surface":"のが好きです。"}]

#### ja-word-kanji-884c-304f

- [ ] Qualified review; notes: pending
- 行く · いく · to go
- Part of speech/register: verb / neutral
- Stage/status: stage-a / draft
- Example: どこへ行くか決めます。
- Structured reading segments: [{"surface":"どこへ"},{"surface":"行く","reading":"いく","vocabulary_id":"ja-word-kanji-884c-304f"},{"surface":"か決めます。"}]

#### ja-word-kanji-6765-308b

- [ ] Qualified review; notes: pending
- 来る · くる · to come
- Part of speech/register: verb / neutral
- Stage/status: stage-a / draft
- Example: 友達が来る日です。
- Structured reading segments: [{"surface":"友達が"},{"surface":"来る","reading":"くる","vocabulary_id":"ja-word-kanji-6765-308b"},{"surface":"日です。"}]

#### ja-word-kanji-4e00-4e07-5186

- [ ] Qualified review; notes: pending
- 一万円 · いちまんえん · ten thousand yen
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 一万円です。
- Structured reading segments: [{"surface":"一万円","reading":"いちまんえん","vocabulary_id":"ja-word-kanji-4e00-4e07-5186"},{"surface":"です。"}]

#### ja-word-kanji-8349

- [ ] Qualified review; notes: pending
- 草 · くさ · grass
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 草が生えています。
- Structured reading segments: [{"surface":"草","reading":"くさ","vocabulary_id":"ja-word-kanji-8349"},{"surface":"が生えています。"}]

#### ja-word-kanji-7530-3093-307c

- [ ] Qualified review; notes: pending
- 田んぼ · たんぼ · rice field
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 田んぼが見えます。
- Structured reading segments: [{"surface":"田んぼ","reading":"たんぼ","vocabulary_id":"ja-word-kanji-7530-3093-307c"},{"surface":"が見えます。"}]

#### ja-word-kanji-4ed5-4e8b

- [ ] Qualified review; notes: pending
- 仕事 · しごと · work; job
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 仕事に行きます。
- Structured reading segments: [{"surface":"仕事","reading":"しごと","vocabulary_id":"ja-word-kanji-4ed5-4e8b"},{"surface":"に行きます。"}]

#### ja-word-kanji-5e97-54e1

- [ ] Qualified review; notes: pending
- 店員 · てんいん · shop assistant
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 店員に聞きます。
- Structured reading segments: [{"surface":"店員","reading":"てんいん","vocabulary_id":"ja-word-kanji-5e97-54e1"},{"surface":"に聞きます。"}]

#### ja-word-kanji-5de5-5834

- [ ] Qualified review; notes: pending
- 工場 · こうじょう · factory
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 工場で働きます。
- Structured reading segments: [{"surface":"工場","reading":"こうじょう","vocabulary_id":"ja-word-kanji-5de5-5834"},{"surface":"で働きます。"}]

#### ja-word-kanji-50cd-304f

- [ ] Qualified review; notes: pending
- 働く · はたらく · to work
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: ここで働く人です。
- Structured reading segments: [{"surface":"ここで"},{"surface":"働く","reading":"はたらく","vocabulary_id":"ja-word-kanji-50cd-304f"},{"surface":"人です。"}]

#### ja-word-kanji-4f11-3080

- [ ] Qualified review; notes: pending
- 休む · やすむ · to rest; to take time off
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 今日は休むことにします。
- Structured reading segments: [{"surface":"今日は"},{"surface":"休む","reading":"やすむ","vocabulary_id":"ja-word-kanji-4f11-3080"},{"surface":"ことにします。"}]

#### ja-word-kanji-5fd9-3057-3044

- [ ] Qualified review; notes: pending
- 忙しい · いそがしい · busy
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 今日は忙しいです。
- Structured reading segments: [{"surface":"今日は"},{"surface":"忙しい","reading":"いそがしい","vocabulary_id":"ja-word-kanji-5fd9-3057-3044"},{"surface":"です。"}]

#### ja-word-kanji-7d66-6599

- [ ] Qualified review; notes: pending
- 給料 · きゅうりょう · salary; wages
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 給料を受け取ります。
- Structured reading segments: [{"surface":"給料","reading":"きゅうりょう","vocabulary_id":"ja-word-kanji-7d66-6599"},{"surface":"を受け取ります。"}]

#### ja-word-kanji-4f4f-3080

- [ ] Qualified review; notes: pending
- 住む · すむ · to live; to reside
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: ここに住む人です。
- Structured reading segments: [{"surface":"ここに"},{"surface":"住む","reading":"すむ","vocabulary_id":"ja-word-kanji-4f4f-3080"},{"surface":"人です。"}]

#### ja-word-kanji-4f4f-6240

- [ ] Qualified review; notes: pending
- 住所 · じゅうしょ · address
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 住所を書きます。
- Structured reading segments: [{"surface":"住所","reading":"じゅうしょ","vocabulary_id":"ja-word-kanji-4f4f-6240"},{"surface":"を書きます。"}]

#### ja-word-kanji-753a

- [ ] Qualified review; notes: pending
- 町 · まち · town
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 静かな町です。
- Structured reading segments: [{"surface":"静かな"},{"surface":"町","reading":"まち","vocabulary_id":"ja-word-kanji-753a"},{"surface":"です。"}]

#### ja-word-kanji-6751

- [ ] Qualified review; notes: pending
- 村 · むら · village
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 小さい村です。
- Structured reading segments: [{"surface":"小さい"},{"surface":"村","reading":"むら","vocabulary_id":"ja-word-kanji-6751"},{"surface":"です。"}]

#### ja-word-kanji-5e02

- [ ] Qualified review; notes: pending
- 市 · し · city; municipality
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: この市に住んでいます。
- Structured reading segments: [{"surface":"この"},{"surface":"市","reading":"し","vocabulary_id":"ja-word-kanji-5e02"},{"surface":"に住んでいます。"}]

#### ja-word-kanji-770c

- [ ] Qualified review; notes: pending
- 県 · けん · prefecture
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: どの県ですか。
- Structured reading segments: [{"surface":"どの"},{"surface":"県","reading":"けん","vocabulary_id":"ja-word-kanji-770c"},{"surface":"ですか。"}]

#### ja-word-kanji-6771-4eac-90fd

- [ ] Qualified review; notes: pending
- 東京都 · とうきょうと · Tokyo Metropolis
- Part of speech/register: proper noun / neutral
- Stage/status: stage-b / draft
- Example: 東京都に住んでいます。
- Structured reading segments: [{"surface":"東京都","reading":"とうきょうと","vocabulary_id":"ja-word-kanji-6771-4eac-90fd"},{"surface":"に住んでいます。"}]

#### ja-word-kanji-6771-4eac

- [ ] Qualified review; notes: pending
- 東京 · とうきょう · Tokyo
- Part of speech/register: proper noun / neutral
- Stage/status: stage-b / draft
- Example: 東京に行きます。
- Structured reading segments: [{"surface":"東京","reading":"とうきょう","vocabulary_id":"ja-word-kanji-6771-4eac"},{"surface":"に行きます。"}]

#### ja-word-kanji-533a

- [ ] Qualified review; notes: pending
- 区 · く · ward; district
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: どの区ですか。
- Structured reading segments: [{"surface":"どの"},{"surface":"区","reading":"く","vocabulary_id":"ja-word-kanji-533a"},{"surface":"ですか。"}]

#### ja-word-kanji-6388-696d

- [ ] Qualified review; notes: pending
- 授業 · じゅぎょう · class; lesson
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 授業が始まります。
- Structured reading segments: [{"surface":"授業","reading":"じゅぎょう","vocabulary_id":"ja-word-kanji-6388-696d"},{"surface":"が始まります。"}]

#### ja-word-kanji-8fd1-3044

- [ ] Qualified review; notes: pending
- 近い · ちかい · near
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 駅は近いです。
- Structured reading segments: [{"surface":"駅は"},{"surface":"近い","reading":"ちかい","vocabulary_id":"ja-word-kanji-8fd1-3044"},{"surface":"です。"}]

#### ja-word-kanji-9060-3044

- [ ] Qualified review; notes: pending
- 遠い · とおい · far
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 駅は遠いです。
- Structured reading segments: [{"surface":"駅は"},{"surface":"遠い","reading":"とおい","vocabulary_id":"ja-word-kanji-9060-3044"},{"surface":"です。"}]

#### ja-word-kanji-901a-308b

- [ ] Qualified review; notes: pending
- 通る · とおる · to pass through
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: この道を通るバスです。
- Structured reading segments: [{"surface":"この道を"},{"surface":"通る","reading":"とおる","vocabulary_id":"ja-word-kanji-901a-308b"},{"surface":"バスです。"}]

#### ja-word-kanji-4ea4-901a

- [ ] Qualified review; notes: pending
- 交通 · こうつう · traffic; transportation
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 交通の便がいいです。
- Structured reading segments: [{"surface":"交通","reading":"こうつう","vocabulary_id":"ja-word-kanji-4ea4-901a"},{"surface":"の便がいいです。"}]

#### ja-word-kanji-5730-56f3

- [ ] Qualified review; notes: pending
- 地図 · ちず · map
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 地図を見ます。
- Structured reading segments: [{"surface":"地図","reading":"ちず","vocabulary_id":"ja-word-kanji-5730-56f3"},{"surface":"を見ます。"}]

#### ja-word-kanji-6d77

- [ ] Qualified review; notes: pending
- 海 · うみ · sea
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 海が見えます。
- Structured reading segments: [{"surface":"海","reading":"うみ","vocabulary_id":"ja-word-kanji-6d77"},{"surface":"が見えます。"}]

#### ja-word-kanji-6e2f

- [ ] Qualified review; notes: pending
- 港 · みなと · port; harbor
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 港に行きます。
- Structured reading segments: [{"surface":"港","reading":"みなと","vocabulary_id":"ja-word-kanji-6e2f"},{"surface":"に行きます。"}]

#### ja-word-kanji-6c60

- [ ] Qualified review; notes: pending
- 池 · いけ · pond
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 池があります。
- Structured reading segments: [{"surface":"池","reading":"いけ","vocabulary_id":"ja-word-kanji-6c60"},{"surface":"があります。"}]

#### ja-word-kanji-6a4b

- [ ] Qualified review; notes: pending
- 橋 · はし · bridge
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 橋を渡ります。
- Structured reading segments: [{"surface":"橋","reading":"はし","vocabulary_id":"ja-word-kanji-6a4b"},{"surface":"を渡ります。"}]

#### ja-word-kanji-5efa-7269

- [ ] Qualified review; notes: pending
- 建物 · たてもの · building
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 大きい建物です。
- Structured reading segments: [{"surface":"大きい"},{"surface":"建物","reading":"たてもの","vocabulary_id":"ja-word-kanji-5efa-7269"},{"surface":"です。"}]

#### ja-word-kanji-90e8-5c4b

- [ ] Qualified review; notes: pending
- 部屋 · へや · room
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 部屋に入ります。
- Structured reading segments: [{"surface":"部屋","reading":"へや","vocabulary_id":"ja-word-kanji-90e8-5c4b"},{"surface":"に入ります。"}]

#### ja-word-kanji-6559-5ba4

- [ ] Qualified review; notes: pending
- 教室 · きょうしつ · classroom
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 教室に入ります。
- Structured reading segments: [{"surface":"教室","reading":"きょうしつ","vocabulary_id":"ja-word-kanji-6559-5ba4"},{"surface":"に入ります。"}]

#### ja-word-kanji-53f0-6240

- [ ] Qualified review; notes: pending
- 台所 · だいどころ · kitchen
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 台所にいます。
- Structured reading segments: [{"surface":"台所","reading":"だいどころ","vocabulary_id":"ja-word-kanji-53f0-6240"},{"surface":"にいます。"}]

#### ja-word-kanji-4e8c-968e

- [ ] Qualified review; notes: pending
- 二階 · にかい · second floor
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 二階に行きます。
- Structured reading segments: [{"surface":"二階","reading":"にかい","vocabulary_id":"ja-word-kanji-4e8c-968e"},{"surface":"に行きます。"}]

#### ja-word-kanji-7a93

- [ ] Qualified review; notes: pending
- 窓 · まど · window
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 窓を開けます。
- Structured reading segments: [{"surface":"窓","reading":"まど","vocabulary_id":"ja-word-kanji-7a93"},{"surface":"を開けます。"}]

#### ja-word-kanji-6238

- [ ] Qualified review; notes: pending
- 戸 · と · door; sliding door
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 戸を開けます。
- Structured reading segments: [{"surface":"戸","reading":"と","vocabulary_id":"ja-word-kanji-6238"},{"surface":"を開けます。"}]

#### ja-word-kanji-9580

- [ ] Qualified review; notes: pending
- 門 · もん · gate
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 門の前です。
- Structured reading segments: [{"surface":"門","reading":"もん","vocabulary_id":"ja-word-kanji-9580"},{"surface":"の前です。"}]

#### ja-word-kanji-5ead

- [ ] Qualified review; notes: pending
- 庭 · にわ · garden; yard
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 庭に花があります。
- Structured reading segments: [{"surface":"庭","reading":"にわ","vocabulary_id":"ja-word-kanji-5ead"},{"surface":"に花があります。"}]

#### ja-word-kanji-516c-5712

- [ ] Qualified review; notes: pending
- 公園 · こうえん · park
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 公園に行きます。
- Structured reading segments: [{"surface":"公園","reading":"こうえん","vocabulary_id":"ja-word-kanji-516c-5712"},{"surface":"に行きます。"}]

#### ja-word-kanji-56f3-66f8-9928

- [ ] Qualified review; notes: pending
- 図書館 · としょかん · library
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 図書館で本を借ります。
- Structured reading segments: [{"surface":"図書館","reading":"としょかん","vocabulary_id":"ja-word-kanji-56f3-66f8-9928"},{"surface":"で本を借ります。"}]

#### ja-word-kanji-5bb6-65cf

- [ ] Qualified review; notes: pending
- 家族 · かぞく · family
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 家族と話します。
- Structured reading segments: [{"surface":"家族","reading":"かぞく","vocabulary_id":"ja-word-kanji-5bb6-65cf"},{"surface":"と話します。"}]

#### ja-word-kanji-5144

- [ ] Qualified review; notes: pending
- 兄 · あに · my older brother
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 兄は家にいます。
- Structured reading segments: [{"surface":"兄","reading":"あに","vocabulary_id":"ja-word-kanji-5144"},{"surface":"は家にいます。"}]

#### ja-word-kanji-5f1f

- [ ] Qualified review; notes: pending
- 弟 · おとうと · younger brother
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 弟は学生です。
- Structured reading segments: [{"surface":"弟","reading":"おとうと","vocabulary_id":"ja-word-kanji-5f1f"},{"surface":"は学生です。"}]

#### ja-word-kanji-59c9

- [ ] Qualified review; notes: pending
- 姉 · あね · my older sister
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 姉は家にいます。
- Structured reading segments: [{"surface":"姉","reading":"あね","vocabulary_id":"ja-word-kanji-59c9"},{"surface":"は家にいます。"}]

#### ja-word-kanji-59b9

- [ ] Qualified review; notes: pending
- 妹 · いもうと · younger sister
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 妹は学生です。
- Structured reading segments: [{"surface":"妹","reading":"いもうと","vocabulary_id":"ja-word-kanji-59b9"},{"surface":"は学生です。"}]

#### ja-word-kanji-592b

- [ ] Qualified review; notes: pending
- 夫 · おっと · my husband
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 夫と出かけます。
- Structured reading segments: [{"surface":"夫","reading":"おっと","vocabulary_id":"ja-word-kanji-592b"},{"surface":"と出かけます。"}]

#### ja-word-kanji-59bb

- [ ] Qualified review; notes: pending
- 妻 · つま · my wife
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 妻と出かけます。
- Structured reading segments: [{"surface":"妻","reading":"つま","vocabulary_id":"ja-word-kanji-59bb"},{"surface":"と出かけます。"}]

#### ja-word-kanji-89aa

- [ ] Qualified review; notes: pending
- 親 · おや · parent
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 親と話します。
- Structured reading segments: [{"surface":"親","reading":"おや","vocabulary_id":"ja-word-kanji-89aa"},{"surface":"と話します。"}]

#### ja-word-kanji-4e21-89aa

- [ ] Qualified review; notes: pending
- 両親 · りょうしん · both parents; parents
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 両親と住んでいます。
- Structured reading segments: [{"surface":"両親","reading":"りょうしん","vocabulary_id":"ja-word-kanji-4e21-89aa"},{"surface":"と住んでいます。"}]

#### ja-word-kanji-7956-6bcd

- [ ] Qualified review; notes: pending
- 祖母 · そぼ · my grandmother
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 祖母に会います。
- Structured reading segments: [{"surface":"祖母","reading":"そぼ","vocabulary_id":"ja-word-kanji-7956-6bcd"},{"surface":"に会います。"}]

#### ja-word-kanji-4e8c-5341-6b73

- [ ] Qualified review; notes: pending
- 二十歳 · はたち · twenty years old
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 二十歳です。
- Structured reading segments: [{"surface":"二十歳","reading":"はたち","vocabulary_id":"ja-word-kanji-4e8c-5341-6b73"},{"surface":"です。"}]

#### ja-word-kanji-8a95-751f-65e5

- [ ] Qualified review; notes: pending
- 誕生日 · たんじょうび · birthday
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 今日は誕生日です。
- Structured reading segments: [{"surface":"今日は"},{"surface":"誕生日","reading":"たんじょうび","vocabulary_id":"ja-word-kanji-8a95-751f-65e5"},{"surface":"です。"}]

#### ja-word-kanji-7d50-5a5a

- [ ] Qualified review; notes: pending
- 結婚 · けっこん · marriage
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 結婚しています。
- Structured reading segments: [{"surface":"結婚","reading":"けっこん","vocabulary_id":"ja-word-kanji-7d50-5a5a"},{"surface":"しています。"}]

#### ja-word-kanji-5f7c

- [ ] Qualified review; notes: pending
- 彼 · かれ · he; him
- Part of speech/register: pronoun / neutral
- Stage/status: stage-b / draft
- Example: 彼は友達です。
- Structured reading segments: [{"surface":"彼","reading":"かれ","vocabulary_id":"ja-word-kanji-5f7c"},{"surface":"は友達です。"}]

#### ja-word-kanji-96a3

- [ ] Qualified review; notes: pending
- 隣 · となり · next door; beside
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 隣の家です。
- Structured reading segments: [{"surface":"隣","reading":"となり","vocabulary_id":"ja-word-kanji-96a3"},{"surface":"の家です。"}]

#### ja-word-kanji-4f55

- [ ] Qualified review; notes: pending
- 何 · なに · what
- Part of speech/register: pronoun / neutral
- Stage/status: stage-b / draft
- Example: 何が好きですか。
- Structured reading segments: [{"surface":"何","reading":"なに","vocabulary_id":"ja-word-kanji-4f55"},{"surface":"が好きですか。"}]

#### ja-word-kanji-8ab0

- [ ] Qualified review; notes: pending
- 誰 · だれ · who
- Part of speech/register: pronoun / neutral
- Stage/status: stage-b / draft
- Example: 誰が来ますか。
- Structured reading segments: [{"surface":"誰","reading":"だれ","vocabulary_id":"ja-word-kanji-8ab0"},{"surface":"が来ますか。"}]

#### ja-word-kanji-4f53

- [ ] Qualified review; notes: pending
- 体 · からだ · body
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 体を動かします。
- Structured reading segments: [{"surface":"体","reading":"からだ","vocabulary_id":"ja-word-kanji-4f53"},{"surface":"を動かします。"}]

#### ja-word-kanji-982d

- [ ] Qualified review; notes: pending
- 頭 · あたま · head
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 頭が痛いです。
- Structured reading segments: [{"surface":"頭","reading":"あたま","vocabulary_id":"ja-word-kanji-982d"},{"surface":"が痛いです。"}]

#### ja-word-kanji-76ee

- [ ] Qualified review; notes: pending
- 目 · め · eye
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 目を閉じます。
- Structured reading segments: [{"surface":"目","reading":"め","vocabulary_id":"ja-word-kanji-76ee"},{"surface":"を閉じます。"}]

#### ja-word-kanji-8033

- [ ] Qualified review; notes: pending
- 耳 · みみ · ear
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 耳が痛いです。
- Structured reading segments: [{"surface":"耳","reading":"みみ","vocabulary_id":"ja-word-kanji-8033"},{"surface":"が痛いです。"}]

#### ja-word-kanji-9f3b

- [ ] Qualified review; notes: pending
- 鼻 · はな · nose
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 鼻をかみます。
- Structured reading segments: [{"surface":"鼻","reading":"はな","vocabulary_id":"ja-word-kanji-9f3b"},{"surface":"をかみます。"}]

#### ja-word-kanji-6b6f

- [ ] Qualified review; notes: pending
- 歯 · は · tooth; teeth
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 歯を磨きます。
- Structured reading segments: [{"surface":"歯","reading":"は","vocabulary_id":"ja-word-kanji-6b6f"},{"surface":"を磨きます。"}]

#### ja-word-kanji-8db3

- [ ] Qualified review; notes: pending
- 足 · あし · foot; leg
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 足が痛いです。
- Structured reading segments: [{"surface":"足","reading":"あし","vocabulary_id":"ja-word-kanji-8db3"},{"surface":"が痛いです。"}]

#### ja-word-kanji-624b

- [ ] Qualified review; notes: pending
- 手 · て · hand
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 手を洗います。
- Structured reading segments: [{"surface":"手","reading":"て","vocabulary_id":"ja-word-kanji-624b"},{"surface":"を洗います。"}]

#### ja-word-kanji-6307

- [ ] Qualified review; notes: pending
- 指 · ゆび · finger
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 指で示します。
- Structured reading segments: [{"surface":"指","reading":"ゆび","vocabulary_id":"ja-word-kanji-6307"},{"surface":"で示します。"}]

#### ja-word-kanji-5fc3

- [ ] Qualified review; notes: pending
- 心 · こころ · heart; mind
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 心が落ち着きます。
- Structured reading segments: [{"surface":"心","reading":"こころ","vocabulary_id":"ja-word-kanji-5fc3"},{"surface":"が落ち着きます。"}]

#### ja-word-kanji-529b

- [ ] Qualified review; notes: pending
- 力 · ちから · strength; power
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 力を合わせます。
- Structured reading segments: [{"surface":"力","reading":"ちから","vocabulary_id":"ja-word-kanji-529b"},{"surface":"を合わせます。"}]

#### ja-word-kanji-75c5-9662

- [ ] Qualified review; notes: pending
- 病院 · びょういん · hospital
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 病院に行きます。
- Structured reading segments: [{"surface":"病院","reading":"びょういん","vocabulary_id":"ja-word-kanji-75c5-9662"},{"surface":"に行きます。"}]

#### ja-word-kanji-533b-8005

- [ ] Qualified review; notes: pending
- 医者 · いしゃ · doctor
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 医者に相談します。
- Structured reading segments: [{"surface":"医者","reading":"いしゃ","vocabulary_id":"ja-word-kanji-533b-8005"},{"surface":"に相談します。"}]

#### ja-word-kanji-85ac

- [ ] Qualified review; notes: pending
- 薬 · くすり · medicine
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 薬を飲みます。
- Structured reading segments: [{"surface":"薬","reading":"くすり","vocabulary_id":"ja-word-kanji-85ac"},{"surface":"を飲みます。"}]

#### ja-word-kanji-85ac-5c40

- [ ] Qualified review; notes: pending
- 薬局 · やっきょく · pharmacy
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 薬局に行きます。
- Structured reading segments: [{"surface":"薬局","reading":"やっきょく","vocabulary_id":"ja-word-kanji-85ac-5c40"},{"surface":"に行きます。"}]

#### ja-word-kanji-75db-3044

- [ ] Qualified review; notes: pending
- 痛い · いたい · painful; sore
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 頭が痛いです。
- Structured reading segments: [{"surface":"頭が"},{"surface":"痛い","reading":"いたい","vocabulary_id":"ja-word-kanji-75db-3044"},{"surface":"です。"}]

#### ja-word-kanji-71b1

- [ ] Qualified review; notes: pending
- 熱 · ねつ · fever; heat
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 熱があります。
- Structured reading segments: [{"surface":"熱","reading":"ねつ","vocabulary_id":"ja-word-kanji-71b1"},{"surface":"があります。"}]

#### ja-word-kanji-7d19

- [ ] Qualified review; notes: pending
- 紙 · かみ · paper
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 紙に書きます。
- Structured reading segments: [{"surface":"紙","reading":"かみ","vocabulary_id":"ja-word-kanji-7d19"},{"surface":"に書きます。"}]

#### ja-word-kanji-5b57

- [ ] Qualified review; notes: pending
- 字 · じ · character; written letter
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 字を書きます。
- Structured reading segments: [{"surface":"字","reading":"じ","vocabulary_id":"ja-word-kanji-5b57"},{"surface":"を書きます。"}]

#### ja-word-kanji-6587

- [ ] Qualified review; notes: pending
- 文 · ぶん · sentence
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 短い文を書きます。
- Structured reading segments: [{"surface":"短い"},{"surface":"文","reading":"ぶん","vocabulary_id":"ja-word-kanji-6587"},{"surface":"を書きます。"}]

#### ja-word-kanji-65e5-672c-8a9e

- [ ] Qualified review; notes: pending
- 日本語 · にほんご · Japanese language
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 日本語を勉強します。
- Structured reading segments: [{"surface":"日本語","reading":"にほんご","vocabulary_id":"ja-word-kanji-65e5-672c-8a9e"},{"surface":"を勉強します。"}]

#### ja-word-kanji-82f1-8a9e

- [ ] Qualified review; notes: pending
- 英語 · えいご · English language
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 英語を話します。
- Structured reading segments: [{"surface":"英語","reading":"えいご","vocabulary_id":"ja-word-kanji-82f1-8a9e"},{"surface":"を話します。"}]

#### ja-word-kanji-6f22-5b57

- [ ] Qualified review; notes: pending
- 漢字 · かんじ · kanji; Chinese-derived character
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 漢字を読みます。
- Structured reading segments: [{"surface":"漢字","reading":"かんじ","vocabulary_id":"ja-word-kanji-6f22-5b57"},{"surface":"を読みます。"}]

#### ja-word-kanji-8aad-3080

- [ ] Qualified review; notes: pending
- 読む · よむ · to read
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 本を読む時間です。
- Structured reading segments: [{"surface":"本を"},{"surface":"読む","reading":"よむ","vocabulary_id":"ja-word-kanji-8aad-3080"},{"surface":"時間です。"}]

#### ja-word-kanji-66f8-304f

- [ ] Qualified review; notes: pending
- 書く · かく · to write
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 名前を書く場所です。
- Structured reading segments: [{"surface":"名前を"},{"surface":"書く","reading":"かく","vocabulary_id":"ja-word-kanji-66f8-304f"},{"surface":"場所です。"}]

#### ja-word-kanji-805e-304f

- [ ] Qualified review; notes: pending
- 聞く · きく · to listen; to ask
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 音楽を聞く時間です。
- Structured reading segments: [{"surface":"音楽を"},{"surface":"聞く","reading":"きく","vocabulary_id":"ja-word-kanji-805e-304f"},{"surface":"時間です。"}]

#### ja-word-kanji-8a71-3059

- [ ] Qualified review; notes: pending
- 話す · はなす · to speak
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 日本語で話す練習です。
- Structured reading segments: [{"surface":"日本語で"},{"surface":"話す","reading":"はなす","vocabulary_id":"ja-word-kanji-8a71-3059"},{"surface":"練習です。"}]

#### ja-word-kanji-8a00-3046

- [ ] Qualified review; notes: pending
- 言う · いう · to say
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 何と言うか考えます。
- Structured reading segments: [{"surface":"何と"},{"surface":"言う","reading":"いう","vocabulary_id":"ja-word-kanji-8a00-3046"},{"surface":"か考えます。"}]

#### ja-word-kanji-601d-3046

- [ ] Qualified review; notes: pending
- 思う · おもう · to think; to feel
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: どう思うか教えてください。
- Structured reading segments: [{"surface":"どう"},{"surface":"思う","reading":"おもう","vocabulary_id":"ja-word-kanji-601d-3046"},{"surface":"か教えてください。"}]

#### ja-word-kanji-77e5-308b

- [ ] Qualified review; notes: pending
- 知る · しる · to find out; to know
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 町のことを知るために歩きます。
- Structured reading segments: [{"surface":"町のことを"},{"surface":"知る","reading":"しる","vocabulary_id":"ja-word-kanji-77e5-308b"},{"surface":"ために歩きます。"}]

#### ja-word-kanji-8003-3048-308b

- [ ] Qualified review; notes: pending
- 考える · かんがえる · to think; to consider
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 答えを考える時間です。
- Structured reading segments: [{"surface":"答えを"},{"surface":"考える","reading":"かんがえる","vocabulary_id":"ja-word-kanji-8003-3048-308b"},{"surface":"時間です。"}]

#### ja-word-kanji-6559-3048-308b

- [ ] Qualified review; notes: pending
- 教える · おしえる · to teach; to tell
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 日本語を教える仕事です。
- Structured reading segments: [{"surface":"日本語を"},{"surface":"教える","reading":"おしえる","vocabulary_id":"ja-word-kanji-6559-3048-308b"},{"surface":"仕事です。"}]

#### ja-word-kanji-7fd2-3046

- [ ] Qualified review; notes: pending
- 習う · ならう · to learn; to take lessons
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 日本語を習う予定です。
- Structured reading segments: [{"surface":"日本語を"},{"surface":"習う","reading":"ならう","vocabulary_id":"ja-word-kanji-7fd2-3046"},{"surface":"予定です。"}]

#### ja-word-kanji-52c9-5f37

- [ ] Qualified review; notes: pending
- 勉強 · べんきょう · study
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 日本語の勉強をします。
- Structured reading segments: [{"surface":"日本語の"},{"surface":"勉強","reading":"べんきょう","vocabulary_id":"ja-word-kanji-52c9-5f37"},{"surface":"をします。"}]

#### ja-word-kanji-5f37-3044

- [ ] Qualified review; notes: pending
- 強い · つよい · strong
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 風が強いです。
- Structured reading segments: [{"surface":"風が"},{"surface":"強い","reading":"つよい","vocabulary_id":"ja-word-kanji-5f37-3044"},{"surface":"です。"}]

#### ja-word-kanji-7df4-7fd2

- [ ] Qualified review; notes: pending
- 練習 · れんしゅう · practice
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 毎日練習します。
- Structured reading segments: [{"surface":"毎日"},{"surface":"練習","reading":"れんしゅう","vocabulary_id":"ja-word-kanji-7df4-7fd2"},{"surface":"します。"}]

#### ja-word-kanji-7b54-3048

- [ ] Qualified review; notes: pending
- 答え · こたえ · answer
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 答えを書きます。
- Structured reading segments: [{"surface":"答え","reading":"こたえ","vocabulary_id":"ja-word-kanji-7b54-3048"},{"surface":"を書きます。"}]

#### ja-word-kanji-8cea-554f

- [ ] Qualified review; notes: pending
- 質問 · しつもん · question
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 質問があります。
- Structured reading segments: [{"surface":"質問","reading":"しつもん","vocabulary_id":"ja-word-kanji-8cea-554f"},{"surface":"があります。"}]

#### ja-word-kanji-554f-984c

- [ ] Qualified review; notes: pending
- 問題 · もんだい · question; problem
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 問題を読みます。
- Structured reading segments: [{"surface":"問題","reading":"もんだい","vocabulary_id":"ja-word-kanji-554f-984c"},{"surface":"を読みます。"}]

#### ja-word-kanji-8a66-9a13

- [ ] Qualified review; notes: pending
- 試験 · しけん · test; examination
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 試験を受けます。
- Structured reading segments: [{"surface":"試験","reading":"しけん","vocabulary_id":"ja-word-kanji-8a66-9a13"},{"surface":"を受けます。"}]

#### ja-word-kanji-5bbf-984c

- [ ] Qualified review; notes: pending
- 宿題 · しゅくだい · homework
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 宿題をします。
- Structured reading segments: [{"surface":"宿題","reading":"しゅくだい","vocabulary_id":"ja-word-kanji-5bbf-984c"},{"surface":"をします。"}]

#### ja-word-kanji-5fd8-308c-308b

- [ ] Qualified review; notes: pending
- 忘れる · わすれる · to forget
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 名前を忘れることがあります。
- Structured reading segments: [{"surface":"名前を"},{"surface":"忘れる","reading":"わすれる","vocabulary_id":"ja-word-kanji-5fd8-308c-308b"},{"surface":"ことがあります。"}]

#### ja-word-kanji-899a-3048-308b

- [ ] Qualified review; notes: pending
- 覚える · おぼえる · to remember; to learn by heart
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 新しい言葉を覚える練習です。
- Structured reading segments: [{"surface":"新しい言葉を"},{"surface":"覚える","reading":"おぼえる","vocabulary_id":"ja-word-kanji-899a-3048-308b"},{"surface":"練習です。"}]

#### ja-word-kanji-5f85-3064

- [ ] Qualified review; notes: pending
- 待つ · まつ · to wait
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: ここで待つことにします。
- Structured reading segments: [{"surface":"ここで"},{"surface":"待つ","reading":"まつ","vocabulary_id":"ja-word-kanji-5f85-3064"},{"surface":"ことにします。"}]

#### ja-word-kanji-6301-3064

- [ ] Qualified review; notes: pending
- 持つ · もつ · to hold; to carry
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 荷物を持つ人です。
- Structured reading segments: [{"surface":"荷物を"},{"surface":"持つ","reading":"もつ","vocabulary_id":"ja-word-kanji-6301-3064"},{"surface":"人です。"}]

#### ja-word-kanji-53d6-308b

- [ ] Qualified review; notes: pending
- 取る · とる · to take
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 本を取る前に聞きます。
- Structured reading segments: [{"surface":"本を"},{"surface":"取る","reading":"とる","vocabulary_id":"ja-word-kanji-53d6-308b"},{"surface":"前に聞きます。"}]

#### ja-word-kanji-4f7f-3046

- [ ] Qualified review; notes: pending
- 使う · つかう · to use
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: これを使う予定です。
- Structured reading segments: [{"surface":"これを"},{"surface":"使う","reading":"つかう","vocabulary_id":"ja-word-kanji-4f7f-3046"},{"surface":"予定です。"}]

#### ja-word-kanji-4f5c-308b

- [ ] Qualified review; notes: pending
- 作る · つくる · to make
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 料理を作る時間です。
- Structured reading segments: [{"surface":"料理を"},{"surface":"作る","reading":"つくる","vocabulary_id":"ja-word-kanji-4f5c-308b"},{"surface":"時間です。"}]

#### ja-word-kanji-8cb7-3046

- [ ] Qualified review; notes: pending
- 買う · かう · to buy
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 本を買う予定です。
- Structured reading segments: [{"surface":"本を"},{"surface":"買う","reading":"かう","vocabulary_id":"ja-word-kanji-8cb7-3046"},{"surface":"予定です。"}]

#### ja-word-kanji-58f2-308b

- [ ] Qualified review; notes: pending
- 売る · うる · to sell
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: パンを売る店です。
- Structured reading segments: [{"surface":"パンを"},{"surface":"売る","reading":"うる","vocabulary_id":"ja-word-kanji-58f2-308b"},{"surface":"店です。"}]

#### ja-word-kanji-501f-308a-308b

- [ ] Qualified review; notes: pending
- 借りる · かりる · to borrow
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 本を借りる予定です。
- Structured reading segments: [{"surface":"本を"},{"surface":"借りる","reading":"かりる","vocabulary_id":"ja-word-kanji-501f-308a-308b"},{"surface":"予定です。"}]

#### ja-word-kanji-8cb8-3059

- [ ] Qualified review; notes: pending
- 貸す · かす · to lend
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 本を貸す前に名前を聞きます。
- Structured reading segments: [{"surface":"本を"},{"surface":"貸す","reading":"かす","vocabulary_id":"ja-word-kanji-8cb8-3059"},{"surface":"前に名前を聞きます。"}]

#### ja-word-kanji-8fd4-3059

- [ ] Qualified review; notes: pending
- 返す · かえす · to return something
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 本を返す日です。
- Structured reading segments: [{"surface":"本を"},{"surface":"返す","reading":"かえす","vocabulary_id":"ja-word-kanji-8fd4-3059"},{"surface":"日です。"}]

#### ja-word-kanji-9001-308b

- [ ] Qualified review; notes: pending
- 送る · おくる · to send
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 手紙を送る予定です。
- Structured reading segments: [{"surface":"手紙を"},{"surface":"送る","reading":"おくる","vocabulary_id":"ja-word-kanji-9001-308b"},{"surface":"予定です。"}]

#### ja-word-kanji-53d7-3051-308b

- [ ] Qualified review; notes: pending
- 受ける · うける · to receive; to take a test
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 試験を受ける予定です。
- Structured reading segments: [{"surface":"試験を"},{"surface":"受ける","reading":"うける","vocabulary_id":"ja-word-kanji-53d7-3051-308b"},{"surface":"予定です。"}]

#### ja-word-kanji-958b-3051-308b

- [ ] Qualified review; notes: pending
- 開ける · あける · to open something
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 窓を開ける前に聞きます。
- Structured reading segments: [{"surface":"窓を"},{"surface":"開ける","reading":"あける","vocabulary_id":"ja-word-kanji-958b-3051-308b"},{"surface":"前に聞きます。"}]

#### ja-word-kanji-9589-3081-308b

- [ ] Qualified review; notes: pending
- 閉める · しめる · to close something
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 店を閉める時間です。
- Structured reading segments: [{"surface":"店を"},{"surface":"閉める","reading":"しめる","vocabulary_id":"ja-word-kanji-9589-3081-308b"},{"surface":"時間です。"}]

#### ja-word-kanji-59cb-307e-308b

- [ ] Qualified review; notes: pending
- 始まる · はじまる · to begin
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 授業が始まる時間です。
- Structured reading segments: [{"surface":"授業が"},{"surface":"始まる","reading":"はじまる","vocabulary_id":"ja-word-kanji-59cb-307e-308b"},{"surface":"時間です。"}]

#### ja-word-kanji-7d42-308f-308b

- [ ] Qualified review; notes: pending
- 終わる · おわる · to end; to finish
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 仕事が終わる時間です。
- Structured reading segments: [{"surface":"仕事が"},{"surface":"終わる","reading":"おわる","vocabulary_id":"ja-word-kanji-7d42-308f-308b"},{"surface":"時間です。"}]

#### ja-word-kanji-6b62-307e-308b

- [ ] Qualified review; notes: pending
- 止まる · とまる · to stop
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: ここで止まるバスです。
- Structured reading segments: [{"surface":"ここで"},{"surface":"止まる","reading":"とまる","vocabulary_id":"ja-word-kanji-6b62-307e-308b"},{"surface":"バスです。"}]

#### ja-word-kanji-6b69-304f

- [ ] Qualified review; notes: pending
- 歩く · あるく · to walk
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 歩くのが好きです。
- Structured reading segments: [{"surface":"歩く","reading":"あるく","vocabulary_id":"ja-word-kanji-6b69-304f"},{"surface":"のが好きです。"}]

#### ja-word-kanji-8d70-308b

- [ ] Qualified review; notes: pending
- 走る · はしる · to run
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 走るのが好きです。
- Structured reading segments: [{"surface":"走る","reading":"はしる","vocabulary_id":"ja-word-kanji-8d70-308b"},{"surface":"のが好きです。"}]

#### ja-word-kanji-6cf3-3050

- [ ] Qualified review; notes: pending
- 泳ぐ · およぐ · to swim
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 泳ぐのが好きです。
- Structured reading segments: [{"surface":"泳ぐ","reading":"およぐ","vocabulary_id":"ja-word-kanji-6cf3-3050"},{"surface":"のが好きです。"}]

#### ja-word-kanji-904a-3076

- [ ] Qualified review; notes: pending
- 遊ぶ · あそぶ · to play; to spend leisure time
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 友達と遊ぶ予定です。
- Structured reading segments: [{"surface":"友達と"},{"surface":"遊ぶ","reading":"あそぶ","vocabulary_id":"ja-word-kanji-904a-3076"},{"surface":"予定です。"}]

#### ja-word-kanji-7acb-3064

- [ ] Qualified review; notes: pending
- 立つ · たつ · to stand
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: ここに立つ人です。
- Structured reading segments: [{"surface":"ここに"},{"surface":"立つ","reading":"たつ","vocabulary_id":"ja-word-kanji-7acb-3064"},{"surface":"人です。"}]

#### ja-word-kanji-5ea7-308b

- [ ] Qualified review; notes: pending
- 座る · すわる · to sit
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: ここに座ることにします。
- Structured reading segments: [{"surface":"ここに"},{"surface":"座る","reading":"すわる","vocabulary_id":"ja-word-kanji-5ea7-308b"},{"surface":"ことにします。"}]

#### ja-word-kanji-4e57-308b

- [ ] Qualified review; notes: pending
- 乗る · のる · to ride; to board
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 電車に乗る予定です。
- Structured reading segments: [{"surface":"電車に"},{"surface":"乗る","reading":"のる","vocabulary_id":"ja-word-kanji-4e57-308b"},{"surface":"予定です。"}]

#### ja-word-kanji-964d-308a-308b

- [ ] Qualified review; notes: pending
- 降りる · おりる · to get off; to descend
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 次の駅で降りる予定です。
- Structured reading segments: [{"surface":"次の駅で"},{"surface":"降りる","reading":"おりる","vocabulary_id":"ja-word-kanji-964d-308a-308b"},{"surface":"予定です。"}]

#### ja-word-kanji-5e30-308b

- [ ] Qualified review; notes: pending
- 帰る · かえる · to go home; to return
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: 家に帰る時間です。
- Structured reading segments: [{"surface":"家に"},{"surface":"帰る","reading":"かえる","vocabulary_id":"ja-word-kanji-5e30-308b"},{"surface":"時間です。"}]

#### ja-word-kanji-62bc-3059

- [ ] Qualified review; notes: pending
- 押す · おす · to push; to press
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: このボタンを押すと開きます。
- Structured reading segments: [{"surface":"このボタンを"},{"surface":"押す","reading":"おす","vocabulary_id":"ja-word-kanji-62bc-3059"},{"surface":"と開きます。"}]

#### ja-word-kanji-5f15-304f

- [ ] Qualified review; notes: pending
- 引く · ひく · to pull
- Part of speech/register: verb / neutral
- Stage/status: stage-b / draft
- Example: この戸は引くと開きます。
- Structured reading segments: [{"surface":"この戸は"},{"surface":"引く","reading":"ひく","vocabulary_id":"ja-word-kanji-5f15-304f"},{"surface":"と開きます。"}]

#### ja-word-kanji-5c11-306a-3044

- [ ] Qualified review; notes: pending
- 少ない · すくない · few; little
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 人が少ないです。
- Structured reading segments: [{"surface":"人が"},{"surface":"少ない","reading":"すくない","vocabulary_id":"ja-word-kanji-5c11-306a-3044"},{"surface":"です。"}]

#### ja-word-kanji-591a-3044

- [ ] Qualified review; notes: pending
- 多い · おおい · many; much
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 人が多いです。
- Structured reading segments: [{"surface":"人が"},{"surface":"多い","reading":"おおい","vocabulary_id":"ja-word-kanji-591a-3044"},{"surface":"です。"}]

#### ja-word-kanji-5168-90e8

- [ ] Qualified review; notes: pending
- 全部 · ぜんぶ · all; everything
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 全部ください。
- Structured reading segments: [{"surface":"全部","reading":"ぜんぶ","vocabulary_id":"ja-word-kanji-5168-90e8"},{"surface":"ください。"}]

#### ja-word-kanji-540c-3058

- [ ] Qualified review; notes: pending
- 同じ · おなじ · the same
- Part of speech/register: adjectival noun / neutral
- Stage/status: stage-b / draft
- Example: 同じ本です。
- Structured reading segments: [{"surface":"同じ","reading":"おなじ","vocabulary_id":"ja-word-kanji-540c-3058"},{"surface":"本です。"}]

#### ja-word-kanji-5225

- [ ] Qualified review; notes: pending
- 別 · べつ · different; separate
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 別の本です。
- Structured reading segments: [{"surface":"別","reading":"べつ","vocabulary_id":"ja-word-kanji-5225"},{"surface":"の本です。"}]

#### ja-word-kanji-4ed6

- [ ] Qualified review; notes: pending
- 他 · ほか · other; another
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 他の店に行きます。
- Structured reading segments: [{"surface":"他","reading":"ほか","vocabulary_id":"ja-word-kanji-4ed6"},{"surface":"の店に行きます。"}]

#### ja-word-kanji-6709-540d

- [ ] Qualified review; notes: pending
- 有名 · ゆうめい · famous
- Part of speech/register: na-adjective / neutral
- Stage/status: stage-b / draft
- Example: 有名な店です。
- Structured reading segments: [{"surface":"有名","reading":"ゆうめい","vocabulary_id":"ja-word-kanji-6709-540d"},{"surface":"な店です。"}]

#### ja-word-kanji-7121-6599

- [ ] Qualified review; notes: pending
- 無料 · むりょう · free of charge
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: ここは無料です。
- Structured reading segments: [{"surface":"ここは"},{"surface":"無料","reading":"むりょう","vocabulary_id":"ja-word-kanji-7121-6599"},{"surface":"です。"}]

#### ja-word-kanji-5fc5-8981

- [ ] Qualified review; notes: pending
- 必要 · ひつよう · necessary
- Part of speech/register: na-adjective / neutral
- Stage/status: stage-b / draft
- Example: 予約が必要です。
- Structured reading segments: [{"surface":"予約が"},{"surface":"必要","reading":"ひつよう","vocabulary_id":"ja-word-kanji-5fc5-8981"},{"surface":"です。"}]

#### ja-word-kanji-4fbf-5229

- [ ] Qualified review; notes: pending
- 便利 · べんり · convenient
- Part of speech/register: na-adjective / neutral
- Stage/status: stage-b / draft
- Example: この町は便利です。
- Structured reading segments: [{"surface":"この町は"},{"surface":"便利","reading":"べんり","vocabulary_id":"ja-word-kanji-4fbf-5229"},{"surface":"です。"}]

#### ja-word-kanji-4e0d-4fbf

- [ ] Qualified review; notes: pending
- 不便 · ふべん · inconvenient
- Part of speech/register: na-adjective / neutral
- Stage/status: stage-b / draft
- Example: ここは少し不便です。
- Structured reading segments: [{"surface":"ここは少し"},{"surface":"不便","reading":"ふべん","vocabulary_id":"ja-word-kanji-4e0d-4fbf"},{"surface":"です。"}]

#### ja-word-kanji-60aa-3044

- [ ] Qualified review; notes: pending
- 悪い · わるい · bad
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 天気が悪いです。
- Structured reading segments: [{"surface":"天気が"},{"surface":"悪い","reading":"わるい","vocabulary_id":"ja-word-kanji-60aa-3044"},{"surface":"です。"}]

#### ja-word-kanji-91cd-3044

- [ ] Qualified review; notes: pending
- 重い · おもい · heavy
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: この本は重いです。
- Structured reading segments: [{"surface":"この本は"},{"surface":"重い","reading":"おもい","vocabulary_id":"ja-word-kanji-91cd-3044"},{"surface":"です。"}]

#### ja-word-kanji-8efd-3044

- [ ] Qualified review; notes: pending
- 軽い · かるい · light in weight
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: この本は軽いです。
- Structured reading segments: [{"surface":"この本は"},{"surface":"軽い","reading":"かるい","vocabulary_id":"ja-word-kanji-8efd-3044"},{"surface":"です。"}]

#### ja-word-kanji-5e83-3044

- [ ] Qualified review; notes: pending
- 広い · ひろい · spacious; wide
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 広い部屋です。
- Structured reading segments: [{"surface":"広い","reading":"ひろい","vocabulary_id":"ja-word-kanji-5e83-3044"},{"surface":"部屋です。"}]

#### ja-word-kanji-72ed-3044

- [ ] Qualified review; notes: pending
- 狭い · せまい · narrow; cramped
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 狭い部屋です。
- Structured reading segments: [{"surface":"狭い","reading":"せまい","vocabulary_id":"ja-word-kanji-72ed-3044"},{"surface":"部屋です。"}]

#### ja-word-kanji-77ed-3044

- [ ] Qualified review; notes: pending
- 短い · みじかい · short
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 短い文です。
- Structured reading segments: [{"surface":"短い","reading":"みじかい","vocabulary_id":"ja-word-kanji-77ed-3044"},{"surface":"文です。"}]

#### ja-word-kanji-4f4e-3044

- [ ] Qualified review; notes: pending
- 低い · ひくい · low
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 低い山です。
- Structured reading segments: [{"surface":"低い","reading":"ひくい","vocabulary_id":"ja-word-kanji-4f4e-3044"},{"surface":"山です。"}]

#### ja-word-kanji-65e9-3044

- [ ] Qualified review; notes: pending
- 早い · はやい · early
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 今日は早い電車に乗ります。
- Structured reading segments: [{"surface":"今日は"},{"surface":"早い","reading":"はやい","vocabulary_id":"ja-word-kanji-65e9-3044"},{"surface":"電車に乗ります。"}]

#### ja-word-kanji-9045-3044

- [ ] Qualified review; notes: pending
- 遅い · おそい · late; slow
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 今日は帰りが遅いです。
- Structured reading segments: [{"surface":"今日は帰りが"},{"surface":"遅い","reading":"おそい","vocabulary_id":"ja-word-kanji-9045-3044"},{"surface":"です。"}]

#### ja-word-kanji-901f-3044

- [ ] Qualified review; notes: pending
- 速い · はやい · fast
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 速い電車です。
- Structured reading segments: [{"surface":"速い","reading":"はやい","vocabulary_id":"ja-word-kanji-901f-3044"},{"surface":"電車です。"}]

#### ja-word-kanji-6625

- [ ] Qualified review; notes: pending
- 春 · はる · spring
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 春に花が咲きます。
- Structured reading segments: [{"surface":"春","reading":"はる","vocabulary_id":"ja-word-kanji-6625"},{"surface":"に花が咲きます。"}]

#### ja-word-kanji-590f

- [ ] Qualified review; notes: pending
- 夏 · なつ · summer
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 夏は暑いです。
- Structured reading segments: [{"surface":"夏","reading":"なつ","vocabulary_id":"ja-word-kanji-590f"},{"surface":"は暑いです。"}]

#### ja-word-kanji-79cb

- [ ] Qualified review; notes: pending
- 秋 · あき · autumn
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 秋は涼しいです。
- Structured reading segments: [{"surface":"秋","reading":"あき","vocabulary_id":"ja-word-kanji-79cb"},{"surface":"は涼しいです。"}]

#### ja-word-kanji-51ac

- [ ] Qualified review; notes: pending
- 冬 · ふゆ · winter
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 冬は寒いです。
- Structured reading segments: [{"surface":"冬","reading":"ふゆ","vocabulary_id":"ja-word-kanji-51ac"},{"surface":"は寒いです。"}]

#### ja-word-kanji-96ea

- [ ] Qualified review; notes: pending
- 雪 · ゆき · snow
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 雪が降っています。
- Structured reading segments: [{"surface":"雪","reading":"ゆき","vocabulary_id":"ja-word-kanji-96ea"},{"surface":"が降っています。"}]

#### ja-word-kanji-98a8

- [ ] Qualified review; notes: pending
- 風 · かぜ · wind
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 風が強いです。
- Structured reading segments: [{"surface":"風","reading":"かぜ","vocabulary_id":"ja-word-kanji-98a8"},{"surface":"が強いです。"}]

#### ja-word-kanji-96f2

- [ ] Qualified review; notes: pending
- 雲 · くも · cloud
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 雲が見えます。
- Structured reading segments: [{"surface":"雲","reading":"くも","vocabulary_id":"ja-word-kanji-96f2"},{"surface":"が見えます。"}]

#### ja-word-kanji-6674-308c

- [ ] Qualified review; notes: pending
- 晴れ · はれ · clear weather
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 今日は晴れです。
- Structured reading segments: [{"surface":"今日は"},{"surface":"晴れ","reading":"はれ","vocabulary_id":"ja-word-kanji-6674-308c"},{"surface":"です。"}]

#### ja-word-kanji-6697-3044

- [ ] Qualified review; notes: pending
- 暗い · くらい · dark
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 部屋が暗いです。
- Structured reading segments: [{"surface":"部屋が"},{"surface":"暗い","reading":"くらい","vocabulary_id":"ja-word-kanji-6697-3044"},{"surface":"です。"}]

#### ja-word-kanji-660e-308b-3044

- [ ] Qualified review; notes: pending
- 明るい · あかるい · bright
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 明るい部屋です。
- Structured reading segments: [{"surface":"明るい","reading":"あかるい","vocabulary_id":"ja-word-kanji-660e-308b-3044"},{"surface":"部屋です。"}]

#### ja-word-kanji-5915-65b9

- [ ] Qualified review; notes: pending
- 夕方 · ゆうがた · early evening
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 夕方に会いましょう。
- Structured reading segments: [{"surface":"夕方","reading":"ゆうがた","vocabulary_id":"ja-word-kanji-5915-65b9"},{"surface":"に会いましょう。"}]

#### ja-word-kanji-4eca-6669

- [ ] Qualified review; notes: pending
- 今晩 · こんばん · this evening; tonight
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 今晩、電話します。
- Structured reading segments: [{"surface":"今晩","reading":"こんばん","vocabulary_id":"ja-word-kanji-4eca-6669"},{"surface":"、電話します。"}]

#### ja-word-kanji-4e88-7d04

- [ ] Qualified review; notes: pending
- 予約 · よやく · reservation
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 予約をします。
- Structured reading segments: [{"surface":"予約","reading":"よやく","vocabulary_id":"ja-word-kanji-4e88-7d04"},{"surface":"をします。"}]

#### ja-word-kanji-8a08-753b

- [ ] Qualified review; notes: pending
- 計画 · けいかく · plan
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 旅行の計画を立てます。
- Structured reading segments: [{"surface":"旅行の"},{"surface":"計画","reading":"けいかく","vocabulary_id":"ja-word-kanji-8a08-753b"},{"surface":"を立てます。"}]

#### ja-word-kanji-4e00-5ea6

- [ ] Qualified review; notes: pending
- 一度 · いちど · once; one time
- Part of speech/register: adverb / neutral
- Stage/status: stage-b / draft
- Example: 一度行きました。
- Structured reading segments: [{"surface":"一度","reading":"いちど","vocabulary_id":"ja-word-kanji-4e00-5ea6"},{"surface":"行きました。"}]

#### ja-word-kanji-3054-98ef

- [ ] Qualified review; notes: pending
- ご飯 · ごはん · cooked rice; meal
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: ご飯を食べます。
- Structured reading segments: [{"surface":"ご飯","reading":"ごはん","vocabulary_id":"ja-word-kanji-3054-98ef"},{"surface":"を食べます。"}]

#### ja-word-kanji-8089

- [ ] Qualified review; notes: pending
- 肉 · にく · meat
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 肉を食べます。
- Structured reading segments: [{"surface":"肉","reading":"にく","vocabulary_id":"ja-word-kanji-8089"},{"surface":"を食べます。"}]

#### ja-word-kanji-7c73

- [ ] Qualified review; notes: pending
- 米 · こめ · uncooked rice
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 米を洗います。
- Structured reading segments: [{"surface":"米","reading":"こめ","vocabulary_id":"ja-word-kanji-7c73"},{"surface":"を洗います。"}]

#### ja-word-kanji-725b-4e73

- [ ] Qualified review; notes: pending
- 牛乳 · ぎゅうにゅう · milk
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 牛乳を飲みます。
- Structured reading segments: [{"surface":"牛乳","reading":"ぎゅうにゅう","vocabulary_id":"ja-word-kanji-725b-4e73"},{"surface":"を飲みます。"}]

#### ja-word-kanji-8c5a-8089

- [ ] Qualified review; notes: pending
- 豚肉 · ぶたにく · pork
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 豚肉を買います。
- Structured reading segments: [{"surface":"豚肉","reading":"ぶたにく","vocabulary_id":"ja-word-kanji-8c5a-8089"},{"surface":"を買います。"}]

#### ja-word-kanji-9d8f-8089

- [ ] Qualified review; notes: pending
- 鶏肉 · とりにく · chicken meat
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 鶏肉を買います。
- Structured reading segments: [{"surface":"鶏肉","reading":"とりにく","vocabulary_id":"ja-word-kanji-9d8f-8089"},{"surface":"を買います。"}]

#### ja-word-kanji-5375

- [ ] Qualified review; notes: pending
- 卵 · たまご · egg
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 卵を買います。
- Structured reading segments: [{"surface":"卵","reading":"たまご","vocabulary_id":"ja-word-kanji-5375"},{"surface":"を買います。"}]

#### ja-word-kanji-91ce-83dc

- [ ] Qualified review; notes: pending
- 野菜 · やさい · vegetables
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 野菜を食べます。
- Structured reading segments: [{"surface":"野菜","reading":"やさい","vocabulary_id":"ja-word-kanji-91ce-83dc"},{"surface":"を食べます。"}]

#### ja-word-kanji-679c-7269

- [ ] Qualified review; notes: pending
- 果物 · くだもの · fruit
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 果物を食べます。
- Structured reading segments: [{"surface":"果物","reading":"くだもの","vocabulary_id":"ja-word-kanji-679c-7269"},{"surface":"を食べます。"}]

#### ja-word-kanji-5869

- [ ] Qualified review; notes: pending
- 塩 · しお · salt
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 塩を入れます。
- Structured reading segments: [{"surface":"塩","reading":"しお","vocabulary_id":"ja-word-kanji-5869"},{"surface":"を入れます。"}]

#### ja-word-kanji-7802-7cd6

- [ ] Qualified review; notes: pending
- 砂糖 · さとう · sugar
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 砂糖を入れます。
- Structured reading segments: [{"surface":"砂糖","reading":"さとう","vocabulary_id":"ja-word-kanji-7802-7cd6"},{"surface":"を入れます。"}]

#### ja-word-kanji-6cb9

- [ ] Qualified review; notes: pending
- 油 · あぶら · oil
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 油を使います。
- Structured reading segments: [{"surface":"油","reading":"あぶら","vocabulary_id":"ja-word-kanji-6cb9"},{"surface":"を使います。"}]

#### ja-word-kanji-5473

- [ ] Qualified review; notes: pending
- 味 · あじ · taste; flavor
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 味を見ます。
- Structured reading segments: [{"surface":"味","reading":"あじ","vocabulary_id":"ja-word-kanji-5473"},{"surface":"を見ます。"}]

#### ja-word-kanji-7518-3044

- [ ] Qualified review; notes: pending
- 甘い · あまい · sweet
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 甘いお菓子です。
- Structured reading segments: [{"surface":"甘い","reading":"あまい","vocabulary_id":"ja-word-kanji-7518-3044"},{"surface":"お菓子です。"}]

#### ja-word-kanji-8f9b-3044

- [ ] Qualified review; notes: pending
- 辛い · からい · spicy; hot in taste
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 辛い料理です。
- Structured reading segments: [{"surface":"辛い","reading":"からい","vocabulary_id":"ja-word-kanji-8f9b-3044"},{"surface":"料理です。"}]

#### ja-word-kanji-9178-3063-3071-3044

- [ ] Qualified review; notes: pending
- 酸っぱい · すっぱい · sour
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 酸っぱい味です。
- Structured reading segments: [{"surface":"酸っぱい","reading":"すっぱい","vocabulary_id":"ja-word-kanji-9178-3063-3071-3044"},{"surface":"味です。"}]

#### ja-word-kanji-82e6-3044

- [ ] Qualified review; notes: pending
- 苦い · にがい · bitter
- Part of speech/register: i-adjective / neutral
- Stage/status: stage-b / draft
- Example: 苦い薬です。
- Structured reading segments: [{"surface":"苦い","reading":"にがい","vocabulary_id":"ja-word-kanji-82e6-3044"},{"surface":"薬です。"}]

#### ja-word-kanji-76bf

- [ ] Qualified review; notes: pending
- 皿 · さら · plate; dish
- Part of speech/register: noun / neutral
- Stage/status: stage-b / draft
- Example: 皿を洗います。
- Structured reading segments: [{"surface":"皿","reading":"さら","vocabulary_id":"ja-word-kanji-76bf"},{"surface":"を洗います。"}]

### Added whole-word reading keys

#### ja-context-4e00-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 一つ in context.
- Prompt: Choose the reading of 一つ (one thing).
- Choices: c0: ひとつ | c1: あおい | c2: あかい
- Expected: ひとつ [c0]
- Explanation: 一つ is read ひとつ here and means one thing. Context: 一つください。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e8c-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 二つ in context.
- Prompt: Choose the reading of 二つ (two things).
- Choices: c0: あかい | c1: ふたつ | c2: あける
- Expected: ふたつ [c1]
- Explanation: 二つ is read ふたつ here and means two things. Context: 二つください。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e09-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 三つ in context.
- Prompt: Choose the reading of 三つ (three things).
- Choices: c0: あける | c1: あそぶ | c2: みっつ
- Expected: みっつ [c2]
- Explanation: 三つ is read みっつ here and means three things. Context: 三つください。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-56db-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 四つ in context.
- Prompt: Choose the reading of 四つ (four things).
- Choices: c0: よっつ | c1: あそぶ | c2: あたま
- Expected: よっつ [c0]
- Explanation: 四つ is read よっつ here and means four things. Context: 四つあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e94-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 五つ in context.
- Prompt: Choose the reading of 五つ (five things).
- Choices: c0: あたま | c1: いつつ | c2: あぶら
- Expected: いつつ [c1]
- Explanation: 五つ is read いつつ here and means five things. Context: 五つあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-516d-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 六つ in context.
- Prompt: Choose the reading of 六つ (six things).
- Choices: c0: あぶら | c1: あまい | c2: むっつ
- Expected: むっつ [c2]
- Explanation: 六つ is read むっつ here and means six things. Context: 六つあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e03-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 七つ in context.
- Prompt: Choose the reading of 七つ (seven things).
- Choices: c0: ななつ | c1: あまい | c2: あるく
- Expected: ななつ [c0]
- Explanation: 七つ is read ななつ here and means seven things. Context: 七つあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-516b-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 八つ in context.
- Prompt: Choose the reading of 八つ (eight things).
- Choices: c0: あるく | c1: やっつ | c2: いしゃ
- Expected: やっつ [c1]
- Explanation: 八つ is read やっつ here and means eight things. Context: 八つあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e5d-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 九つ in context.
- Prompt: Choose the reading of 九つ (nine things).
- Choices: c0: あかるい | c1: いちねん | c2: ここのつ
- Expected: ここのつ [c2]
- Explanation: 九つ is read ここのつ here and means nine things. Context: 九つあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5341-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 十 in context.
- Prompt: Choose the reading of 十 (ten).
- Choices: c0: じゅう | c1: あかい | c2: あける
- Expected: じゅう [c0]
- Explanation: 十 is read じゅう here and means ten. Context: 十まで数えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-767e-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 百 in context.
- Prompt: Choose the reading of 百 (one hundred).
- Choices: c0: あける | c1: ひゃく | c2: あそぶ
- Expected: ひゃく [c1]
- Explanation: 百 is read ひゃく here and means one hundred. Context: 百まで数えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5343-5186-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 千円 in context.
- Prompt: Choose the reading of 千円 (one thousand yen).
- Choices: c0: おおきい | c1: おしえる | c2: せんえん
- Expected: せんえん [c2]
- Explanation: 千円 is read せんえん here and means one thousand yen. Context: 千円です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5186-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 円 in context.
- Prompt: Choose the reading of 円 (yen).
- Choices: c0: えん | c1: あに | c2: あね
- Expected: えん [c0]
- Explanation: 円 is read えん here and means yen. Context: 円で払います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e00-5e74-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 一年 in context.
- Prompt: Choose the reading of 一年 (one year).
- Choices: c0: おぼえる | c1: いちねん | c2: かいしゃ
- Expected: いちねん [c1]
- Explanation: 一年 is read いちねん here and means one year. Context: 一年かかります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4eca-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 今 in context.
- Prompt: Choose the reading of 今 (now).
- Choices: c0: あめ | c1: いう | c2: いま
- Expected: いま [c2]
- Explanation: 今 is read いま here and means now. Context: 今、行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6bce-65e5-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 毎日 in context.
- Prompt: Choose the reading of 毎日 (every day).
- Choices: c0: まいにち | c1: かいしゃ | c2: がくせい
- Expected: まいにち [c0]
- Explanation: 毎日 is read まいにち here and means every day. Context: 毎日読みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6765-9031-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 来週 in context.
- Prompt: Choose the reading of 来週 (next week).
- Choices: c0: あたらしい | c1: らいしゅう | c2: いそがしい
- Expected: らいしゅう [c1]
- Explanation: 来週 is read らいしゅう here and means next week. Context: 来週、会いましょう。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e94-5206-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 五分 in context.
- Prompt: Choose the reading of 五分 (five minutes).
- Choices: c0: あかい | c1: あける | c2: ごふん
- Expected: ごふん [c2]
- Explanation: 五分 is read ごふん here and means five minutes. Context: 五分かかります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-534a-5206-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 半分 in context.
- Prompt: Choose the reading of 半分 (half).
- Choices: c0: はんぶん | c1: いもうと | c2: おおきい
- Expected: はんぶん [c0]
- Explanation: 半分 is read はんぶん here and means half. Context: 半分ください。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5348-524d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 午前 in context.
- Prompt: Choose the reading of 午前 (morning; a.m.).
- Choices: c0: あそぶ | c1: ごぜん | c2: あたま
- Expected: ごぜん [c1]
- Explanation: 午前 is read ごぜん here and means morning; a.m.. Context: 午前に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-524d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 前 in context.
- Prompt: Choose the reading of 前 (front; before).
- Choices: c0: あに | c1: あね | c2: まえ
- Expected: まえ [c2]
- Explanation: 前 is read まえ here and means front; before. Context: 駅の前です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5f8c-308d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 後ろ in context.
- Prompt: Choose the reading of 後ろ (behind; the back).
- Choices: c0: うしろ | c1: あぶら | c2: あまい
- Expected: うしろ [c0]
- Explanation: 後ろ is read うしろ here and means behind; the back. Context: 家の後ろです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-671d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 朝 in context.
- Prompt: Choose the reading of 朝 (morning).
- Choices: c0: いう | c1: あさ | c2: いえ
- Expected: あさ [c1]
- Explanation: 朝 is read あさ here and means morning. Context: 朝、お茶を飲みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-663c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 昼 in context.
- Prompt: Choose the reading of 昼 (daytime; noon).
- Choices: c0: いう | c1: いえ | c2: ひる
- Expected: ひる [c2]
- Explanation: 昼 is read ひる here and means daytime; noon. Context: 昼に会いましょう。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-591c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 夜 in context.
- Prompt: Choose the reading of 夜 (night).
- Choices: c0: よる | c1: あき | c2: あさ
- Expected: よる [c0]
- Explanation: 夜 is read よる here and means night. Context: 夜、本を読みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4eba-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 人 in context.
- Prompt: Choose the reading of 人 (person).
- Choices: c0: あさ | c1: ひと | c2: あし
- Expected: ひと [c1]
- Explanation: 人 is read ひと here and means person. Context: 人がいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7537-306e-5b50-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 男の子 in context.
- Prompt: Choose the reading of 男の子 (boy).
- Choices: c0: おんなのこ | c1: かんがえる | c2: おとこのこ
- Expected: おとこのこ [c2]
- Explanation: 男の子 is read おとこのこ here and means boy. Context: 男の子がいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5973-306e-5b50-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 女の子 in context.
- Prompt: Choose the reading of 女の子 (girl).
- Choices: c0: おんなのこ | c1: かんがえる | c2: きょうしつ
- Expected: おんなのこ [c0]
- Explanation: 女の子 is read おんなのこ here and means girl. Context: 女の子がいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5b50-3069-3082-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 子ども in context.
- Prompt: Choose the reading of 子ども (child).
- Choices: c0: あたま | c1: こども | c2: あぶら
- Expected: こども [c1]
- Explanation: 子ども is read こども here and means child. Context: 子どもがいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7236-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 父 in context.
- Prompt: Choose the reading of 父 (my father).
- Choices: c0: あね | c1: あめ | c2: ちち
- Expected: ちち [c2]
- Explanation: 父 is read ちち here and means my father. Context: 父は家にいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6bcd-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 母 in context.
- Prompt: Choose the reading of 母 (my mother).
- Choices: c0: はは | c1: あめ | c2: いう
- Expected: はは [c0]
- Explanation: 母 is read はは here and means my mother. Context: 母は家にいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-53cb-9054-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 友達 in context.
- Prompt: Choose the reading of 友達 (friend).
- Choices: c0: かいしゃ | c1: ともだち | c2: がくせい
- Expected: ともだち [c1]
- Explanation: 友達 is read ともだち here and means friend. Context: 友達と行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5148-751f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 先生 in context.
- Prompt: Choose the reading of 先生 (teacher).
- Choices: c0: あかるい | c1: いちねん | c2: せんせい
- Expected: せんせい [c2]
- Explanation: 先生 is read せんせい here and means teacher. Context: 先生に聞きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5b66-751f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 学生 in context.
- Prompt: Choose the reading of 学生 (student).
- Choices: c0: がくせい | c1: いちねん | c2: いもうと
- Expected: がくせい [c0]
- Explanation: 学生 is read がくせい here and means student. Context: 私は学生です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-540d-524d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 名前 in context.
- Prompt: Choose the reading of 名前 (name).
- Choices: c0: あける | c1: なまえ | c2: あそぶ
- Expected: なまえ [c1]
- Explanation: 名前 is read なまえ here and means name. Context: 名前を書きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-79c1-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 私 in context.
- Prompt: Choose the reading of 私 (I; me).
- Choices: c0: あそぶ | c1: あたま | c2: わたし
- Expected: わたし [c2]
- Explanation: 私 is read わたし here and means I; me. Context: 私はアキです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5bb6-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 家 in context.
- Prompt: Choose the reading of 家 (house; home).
- Choices: c0: いえ | c1: あに | c2: あね
- Expected: いえ [c0]
- Explanation: 家 is read いえ here and means house; home. Context: 家に帰ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5c71-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 山 in context.
- Prompt: Choose the reading of 山 (mountain).
- Choices: c0: あね | c1: やま | c2: あめ
- Expected: やま [c1]
- Explanation: 山 is read やま here and means mountain. Context: 山が見えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5ddd-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 川 in context.
- Prompt: Choose the reading of 川 (river).
- Choices: c0: あめ | c1: いう | c2: かわ
- Expected: かわ [c2]
- Explanation: 川 is read かわ here and means river. Context: 川があります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7a7a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 空 in context.
- Prompt: Choose the reading of 空 (sky).
- Choices: c0: そら | c1: いう | c2: いえ
- Expected: そら [c0]
- Explanation: 空 is read そら here and means sky. Context: 空が青いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-96e8-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 雨 in context.
- Prompt: Choose the reading of 雨 (rain).
- Choices: c0: あき | c1: あめ | c2: あさ
- Expected: あめ [c1]
- Explanation: 雨 is read あめ here and means rain. Context: 雨が降っています。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5929-6c17-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 天気 in context.
- Prompt: Choose the reading of 天気 (weather).
- Choices: c0: あかい | c1: あける | c2: てんき
- Expected: てんき [c2]
- Explanation: 天気 is read てんき here and means weather. Context: 天気がいいです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5143-6c17-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 元気 in context.
- Prompt: Choose the reading of 元気 (healthy; in good spirits).
- Choices: c0: げんき | c1: あける | c2: あそぶ
- Expected: げんき [c0]
- Explanation: 元気 is read げんき here and means healthy; in good spirits. Context: 元気です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-82b1-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 花 in context.
- Prompt: Choose the reading of 花 (flower).
- Choices: c0: あじ | c1: はな | c2: あに
- Expected: はな [c1]
- Explanation: 花 is read はな here and means flower. Context: 花を見ます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-72ac-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 犬 in context.
- Prompt: Choose the reading of 犬 (dog).
- Choices: c0: あに | c1: あね | c2: いぬ
- Expected: いぬ [c2]
- Explanation: 犬 is read いぬ here and means dog. Context: 犬がいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-732b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 猫 in context.
- Prompt: Choose the reading of 猫 (cat).
- Choices: c0: ねこ | c1: あね | c2: あめ
- Expected: ねこ [c0]
- Explanation: 猫 is read ねこ here and means cat. Context: 猫がいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9ce5-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 鳥 in context.
- Prompt: Choose the reading of 鳥 (bird).
- Choices: c0: あめ | c1: とり | c2: いう
- Expected: とり [c1]
- Explanation: 鳥 is read とり here and means bird. Context: 鳥がいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9b5a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 魚 in context.
- Prompt: Choose the reading of 魚 (fish).
- Choices: c0: あるく | c1: いしゃ | c2: さかな
- Expected: さかな [c2]
- Explanation: 魚 is read さかな here and means fish. Context: 魚を食べます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8eca-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 車 in context.
- Prompt: Choose the reading of 車 (car).
- Choices: c0: くるま | c1: あおい | c2: あかい
- Expected: くるま [c0]
- Explanation: 車 is read くるま here and means car. Context: 車で行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-96fb-8eca-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 電車 in context.
- Prompt: Choose the reading of 電車 (train).
- Choices: c0: いちねん | c1: でんしゃ | c2: いもうと
- Expected: でんしゃ [c1]
- Explanation: 電車 is read でんしゃ here and means train. Context: 電車で行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9053-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 道 in context.
- Prompt: Choose the reading of 道 (road; way).
- Choices: c0: あし | c1: あじ | c2: みち
- Expected: みち [c2]
- Explanation: 道 is read みち here and means road; way. Context: この道を行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5e97-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 店 in context.
- Prompt: Choose the reading of 店 (shop).
- Choices: c0: みせ | c1: あじ | c2: あに
- Expected: みせ [c0]
- Explanation: 店 is read みせ here and means shop. Context: 店に入ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f1a-793e-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 会社 in context.
- Prompt: Choose the reading of 会社 (company).
- Choices: c0: おしえる | c1: かいしゃ | c2: おとうと
- Expected: かいしゃ [c1]
- Explanation: 会社 is read かいしゃ here and means company. Context: 会社に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-56fd-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 国 in context.
- Prompt: Choose the reading of 国 (country).
- Choices: c0: あね | c1: あめ | c2: くに
- Expected: くに [c2]
- Explanation: 国 is read くに here and means country. Context: どの国ですか。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5916-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 外 in context.
- Prompt: Choose the reading of 外 (outside).
- Choices: c0: そと | c1: あめ | c2: いう
- Expected: そと [c0]
- Explanation: 外 is read そと here and means outside. Context: 外に出ます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e2d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 中 in context.
- Prompt: Choose the reading of 中 (inside).
- Choices: c0: いう | c1: なか | c2: いえ
- Expected: なか [c1]
- Explanation: 中 is read なか here and means inside. Context: 中に入ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e0a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 上 in context.
- Prompt: Choose the reading of 上 (above; on top).
- Choices: c0: あき | c1: あさ | c2: うえ
- Expected: うえ [c2]
- Explanation: 上 is read うえ here and means above; on top. Context: 机の上です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e0b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 下 in context.
- Prompt: Choose the reading of 下 (below; underneath).
- Choices: c0: した | c1: あさ | c2: あし
- Expected: した [c0]
- Explanation: 下 is read した here and means below; underneath. Context: 机の下です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5de6-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 左 in context.
- Prompt: Choose the reading of 左 (left).
- Choices: c0: あける | c1: ひだり | c2: あそぶ
- Expected: ひだり [c1]
- Explanation: 左 is read ひだり here and means left. Context: 左に曲がります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-53f3-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 右 in context.
- Prompt: Choose the reading of 右 (right).
- Choices: c0: あじ | c1: あに | c2: みぎ
- Expected: みぎ [c2]
- Explanation: 右 is read みぎ here and means right. Context: 右に曲がります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5317-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 北 in context.
- Prompt: Choose the reading of 北 (north).
- Choices: c0: きた | c1: あに | c2: あね
- Expected: きた [c0]
- Explanation: 北 is read きた here and means north. Context: 北へ行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5357-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 南 in context.
- Prompt: Choose the reading of 南 (south).
- Choices: c0: あぶら | c1: みなみ | c2: あまい
- Expected: みなみ [c1]
- Explanation: 南 is read みなみ here and means south. Context: 南へ行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6771-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 東 in context.
- Prompt: Choose the reading of 東 (east).
- Choices: c0: あまい | c1: あるく | c2: ひがし
- Expected: ひがし [c2]
- Explanation: 東 is read ひがし here and means east. Context: 東へ行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-897f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 西 in context.
- Prompt: Choose the reading of 西 (west).
- Choices: c0: にし | c1: いう | c2: いえ
- Expected: にし [c0]
- Explanation: 西 is read にし here and means west. Context: 西へ行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5927-304d-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 大きい in context.
- Prompt: Choose the reading of 大きい (big).
- Choices: c0: あかるい | c1: おおきい | c2: いちねん
- Expected: おおきい [c1]
- Explanation: 大きい is read おおきい here and means big. Context: 大きい家です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5c0f-3055-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 小さい in context.
- Prompt: Choose the reading of 小さい (small).
- Choices: c0: いちねん | c1: いもうと | c2: ちいさい
- Expected: ちいさい [c2]
- Explanation: 小さい is read ちいさい here and means small. Context: 小さい店です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9577-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 長い in context.
- Prompt: Choose the reading of 長い (long).
- Choices: c0: ながい | c1: あける | c2: あそぶ
- Expected: ながい [c0]
- Explanation: 長い is read ながい here and means long. Context: 長い道です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9ad8-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 高い in context.
- Prompt: Choose the reading of 高い (high; expensive).
- Choices: c0: あそぶ | c1: たかい | c2: あたま
- Expected: たかい [c1]
- Explanation: 高い is read たかい here and means high; expensive. Context: この本は高いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5b89-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 安い in context.
- Prompt: Choose the reading of 安い (inexpensive).
- Choices: c0: あたま | c1: あぶら | c2: やすい
- Expected: やすい [c2]
- Explanation: 安い is read やすい here and means inexpensive. Context: この本は安いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-65b0-3057-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 新しい in context.
- Prompt: Choose the reading of 新しい (new).
- Choices: c0: あたらしい | c1: こうじょう | c2: じゅうしょ
- Expected: あたらしい [c0]
- Explanation: 新しい is read あたらしい here and means new. Context: 新しい本です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-53e4-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 古い in context.
- Prompt: Choose the reading of 古い (old).
- Choices: c0: あまい | c1: ふるい | c2: あるく
- Expected: ふるい [c1]
- Explanation: 古い is read ふるい here and means old. Context: 古い家です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-767d-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 白い in context.
- Prompt: Choose the reading of 白い (white).
- Choices: c0: あるく | c1: いしゃ | c2: しろい
- Expected: しろい [c2]
- Explanation: 白い is read しろい here and means white. Context: 白い紙です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9ed2-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 黒い in context.
- Prompt: Choose the reading of 黒い (black).
- Choices: c0: くろい | c1: あおい | c2: あかい
- Expected: くろい [c0]
- Explanation: 黒い is read くろい here and means black. Context: 黒い車です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8d64-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 赤い in context.
- Prompt: Choose the reading of 赤い (red).
- Choices: c0: あける | c1: あかい | c2: あそぶ
- Expected: あかい [c1]
- Explanation: 赤い is read あかい here and means red. Context: 赤い花です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9752-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 青い in context.
- Prompt: Choose the reading of 青い (blue).
- Choices: c0: あそぶ | c1: あたま | c2: あおい
- Expected: あおい [c2]
- Explanation: 青い is read あおい here and means blue. Context: 青い空です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-597d-304d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 好き in context.
- Prompt: Choose the reading of 好き (liked; favorite).
- Choices: c0: すき | c1: あじ | c2: あに
- Expected: すき [c0]
- Explanation: 好き is read すき here and means liked; favorite. Context: お茶が好きです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-98df-3079-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 食べる in context.
- Prompt: Choose the reading of 食べる (to eat).
- Choices: c0: あたま | c1: たべる | c2: あぶら
- Expected: たべる [c1]
- Explanation: 食べる is read たべる here and means to eat. Context: 何を食べるか決めます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-98f2-3080-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 飲む in context.
- Prompt: Choose the reading of 飲む (to drink).
- Choices: c0: あね | c1: あめ | c2: のむ
- Expected: のむ [c2]
- Explanation: 飲む is read のむ here and means to drink. Context: 何を飲むか決めます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-898b-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 見る in context.
- Prompt: Choose the reading of 見る (to see; to watch).
- Choices: c0: みる | c1: あめ | c2: いう
- Expected: みる [c0]
- Explanation: 見る is read みる here and means to see; to watch. Context: 映画を見るのが好きです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-884c-304f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 行く in context.
- Prompt: Choose the reading of 行く (to go).
- Choices: c0: いう | c1: いく | c2: いえ
- Expected: いく [c1]
- Explanation: 行く is read いく here and means to go. Context: どこへ行くか決めます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6765-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 1
- Objective: Recognize the whole-word reading of 来る in context.
- Prompt: Choose the reading of 来る (to come).
- Choices: c0: あき | c1: あさ | c2: くる
- Expected: くる [c2]
- Explanation: 来る is read くる here and means to come. Context: 友達が来る日です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e00-4e07-5186-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 一万円 in context.
- Prompt: Choose the reading of 一万円 (ten thousand yen).
- Choices: c0: いちまんえん | c1: きゅうりょう | c2: たんじょうび
- Expected: いちまんえん [c0]
- Explanation: 一万円 is read いちまんえん here and means ten thousand yen. Context: 一万円です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8349-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 草 in context.
- Prompt: Choose the reading of 草 (grass).
- Choices: c0: あし | c1: くさ | c2: あじ
- Expected: くさ [c1]
- Explanation: 草 is read くさ here and means grass. Context: 草が生えています。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7530-3093-307c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 田んぼ in context.
- Prompt: Choose the reading of 田んぼ (rice field).
- Choices: c0: あそぶ | c1: あたま | c2: たんぼ
- Expected: たんぼ [c2]
- Explanation: 田んぼ is read たんぼ here and means rice field. Context: 田んぼが見えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4ed5-4e8b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 仕事 in context.
- Prompt: Choose the reading of 仕事 (work; job).
- Choices: c0: しごと | c1: あたま | c2: あぶら
- Expected: しごと [c0]
- Explanation: 仕事 is read しごと here and means work; job. Context: 仕事に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5e97-54e1-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 店員 in context.
- Prompt: Choose the reading of 店員 (shop assistant).
- Choices: c0: おとうと | c1: てんいん | c2: おぼえる
- Expected: てんいん [c1]
- Explanation: 店員 is read てんいん here and means shop assistant. Context: 店員に聞きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5de5-5834-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 工場 in context.
- Prompt: Choose the reading of 工場 (factory).
- Choices: c0: じゅうしょ | c1: じゅぎょう | c2: こうじょう
- Expected: こうじょう [c2]
- Explanation: 工場 is read こうじょう here and means factory. Context: 工場で働きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-50cd-304f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 働く in context.
- Prompt: Choose the reading of 働く (to work).
- Choices: c0: はたらく | c1: かいしゃ | c2: がくせい
- Expected: はたらく [c0]
- Explanation: 働く is read はたらく here and means to work. Context: ここで働く人です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f11-3080-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 休む in context.
- Prompt: Choose the reading of 休む (to rest; to take time off).
- Choices: c0: あおい | c1: やすむ | c2: あかい
- Expected: やすむ [c1]
- Explanation: 休む is read やすむ here and means to rest; to take time off. Context: 今日は休むことにします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5fd9-3057-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 忙しい in context.
- Prompt: Choose the reading of 忙しい (busy).
- Choices: c0: おとこのこ | c1: おんなのこ | c2: いそがしい
- Expected: いそがしい [c2]
- Explanation: 忙しい is read いそがしい here and means busy. Context: 今日は忙しいです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7d66-6599-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 給料 in context.
- Prompt: Choose the reading of 給料 (salary; wages).
- Choices: c0: きゅうりょう | c1: たんじょうび | c2: とうきょうと
- Expected: きゅうりょう [c0]
- Explanation: 給料 is read きゅうりょう here and means salary; wages. Context: 給料を受け取ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f4f-3080-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 住む in context.
- Prompt: Choose the reading of 住む (to live; to reside).
- Choices: c0: あじ | c1: すむ | c2: あに
- Expected: すむ [c1]
- Explanation: 住む is read すむ here and means to live; to reside. Context: ここに住む人です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f4f-6240-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 住所 in context.
- Prompt: Choose the reading of 住所 (address).
- Choices: c0: かんがえる | c1: きょうしつ | c2: じゅうしょ
- Expected: じゅうしょ [c2]
- Explanation: 住所 is read じゅうしょ here and means address. Context: 住所を書きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-753a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 町 in context.
- Prompt: Choose the reading of 町 (town).
- Choices: c0: まち | c1: あね | c2: あめ
- Expected: まち [c0]
- Explanation: 町 is read まち here and means town. Context: 静かな町です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6751-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 村 in context.
- Prompt: Choose the reading of 村 (village).
- Choices: c0: あめ | c1: むら | c2: いう
- Expected: むら [c1]
- Explanation: 村 is read むら here and means village. Context: 小さい村です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5e02-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 市 in context.
- Prompt: Choose the reading of 市 (city; municipality).
- Choices: c0: あさ | c1: あし | c2: し
- Expected: し [c2]
- Explanation: 市 is read し here and means city; municipality. Context: この市に住んでいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-770c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 県 in context.
- Prompt: Choose the reading of 県 (prefecture).
- Choices: c0: けん | c1: あき | c2: あさ
- Expected: けん [c0]
- Explanation: 県 is read けん here and means prefecture. Context: どの県ですか。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6771-4eac-90fd-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 東京都 in context.
- Prompt: Choose the reading of 東京都 (Tokyo Metropolis).
- Choices: c0: ぎゅうにゅう | c1: とうきょうと | c2: きゅうりょう
- Expected: とうきょうと [c1]
- Explanation: 東京都 is read とうきょうと here and means Tokyo Metropolis. Context: 東京都に住んでいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6771-4eac-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 東京 in context.
- Prompt: Choose the reading of 東京 (Tokyo).
- Choices: c0: おとこのこ | c1: おんなのこ | c2: とうきょう
- Expected: とうきょう [c2]
- Explanation: 東京 is read とうきょう here and means Tokyo. Context: 東京に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-533a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 区 in context.
- Prompt: Choose the reading of 区 (ward; district).
- Choices: c0: く | c1: と | c2: は
- Expected: く [c0]
- Explanation: 区 is read く here and means ward; district. Context: どの区ですか。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6388-696d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 授業 in context.
- Prompt: Choose the reading of 授業 (class; lesson).
- Choices: c0: かんがえる | c1: じゅぎょう | c2: きょうしつ
- Expected: じゅぎょう [c1]
- Explanation: 授業 is read じゅぎょう here and means class; lesson. Context: 授業が始まります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8fd1-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 近い in context.
- Prompt: Choose the reading of 近い (near).
- Choices: c0: あぶら | c1: あまい | c2: ちかい
- Expected: ちかい [c2]
- Explanation: 近い is read ちかい here and means near. Context: 駅は近いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9060-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 遠い in context.
- Prompt: Choose the reading of 遠い (far).
- Choices: c0: とおい | c1: あまい | c2: あるく
- Expected: とおい [c0]
- Explanation: 遠い is read とおい here and means far. Context: 駅は遠いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-901a-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 通る in context.
- Prompt: Choose the reading of 通る (to pass through).
- Choices: c0: あるく | c1: とおる | c2: いしゃ
- Expected: とおる [c1]
- Explanation: 通る is read とおる here and means to pass through. Context: この道を通るバスです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4ea4-901a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 交通 in context.
- Prompt: Choose the reading of 交通 (traffic; transportation).
- Choices: c0: あかるい | c1: いちねん | c2: こうつう
- Expected: こうつう [c2]
- Explanation: 交通 is read こうつう here and means traffic; transportation. Context: 交通の便がいいです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5730-56f3-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 地図 in context.
- Prompt: Choose the reading of 地図 (map).
- Choices: c0: ちず | c1: あさ | c2: あし
- Expected: ちず [c0]
- Explanation: 地図 is read ちず here and means map. Context: 地図を見ます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6d77-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 海 in context.
- Prompt: Choose the reading of 海 (sea).
- Choices: c0: あし | c1: うみ | c2: あじ
- Expected: うみ [c1]
- Explanation: 海 is read うみ here and means sea. Context: 海が見えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6e2f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 港 in context.
- Prompt: Choose the reading of 港 (port; harbor).
- Choices: c0: あそぶ | c1: あたま | c2: みなと
- Expected: みなと [c2]
- Explanation: 港 is read みなと here and means port; harbor. Context: 港に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6c60-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 池 in context.
- Prompt: Choose the reading of 池 (pond).
- Choices: c0: いけ | c1: あに | c2: あね
- Expected: いけ [c0]
- Explanation: 池 is read いけ here and means pond. Context: 池があります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6a4b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 橋 in context.
- Prompt: Choose the reading of 橋 (bridge).
- Choices: c0: あね | c1: はし | c2: あめ
- Expected: はし [c1]
- Explanation: 橋 is read はし here and means bridge. Context: 橋を渡ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5efa-7269-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 建物 in context.
- Prompt: Choose the reading of 建物 (building).
- Choices: c0: おぼえる | c1: かいしゃ | c2: たてもの
- Expected: たてもの [c2]
- Explanation: 建物 is read たてもの here and means building. Context: 大きい建物です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-90e8-5c4b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 部屋 in context.
- Prompt: Choose the reading of 部屋 (room).
- Choices: c0: へや | c1: いう | c2: いえ
- Expected: へや [c0]
- Explanation: 部屋 is read へや here and means room. Context: 部屋に入ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6559-5ba4-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 教室 in context.
- Prompt: Choose the reading of 教室 (classroom).
- Choices: c0: あたらしい | c1: きょうしつ | c2: いそがしい
- Expected: きょうしつ [c1]
- Explanation: 教室 is read きょうしつ here and means classroom. Context: 教室に入ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-53f0-6240-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 台所 in context.
- Prompt: Choose the reading of 台所 (kitchen).
- Choices: c0: いそがしい | c1: おとこのこ | c2: だいどころ
- Expected: だいどころ [c2]
- Explanation: 台所 is read だいどころ here and means kitchen. Context: 台所にいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e8c-968e-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 二階 in context.
- Prompt: Choose the reading of 二階 (second floor).
- Choices: c0: にかい | c1: あける | c2: あそぶ
- Expected: にかい [c0]
- Explanation: 二階 is read にかい here and means second floor. Context: 二階に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7a93-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 窓 in context.
- Prompt: Choose the reading of 窓 (window).
- Choices: c0: あじ | c1: まど | c2: あに
- Expected: まど [c1]
- Explanation: 窓 is read まど here and means window. Context: 窓を開けます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6238-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 戸 in context.
- Prompt: Choose the reading of 戸 (door; sliding door).
- Choices: c0: は | c1: め | c2: と
- Expected: と [c2]
- Explanation: 戸 is read と here and means door; sliding door. Context: 戸を開けます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9580-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 門 in context.
- Prompt: Choose the reading of 門 (gate).
- Choices: c0: もん | c1: あね | c2: あめ
- Expected: もん [c0]
- Explanation: 門 is read もん here and means gate. Context: 門の前です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5ead-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 庭 in context.
- Prompt: Choose the reading of 庭 (garden; yard).
- Choices: c0: あめ | c1: にわ | c2: いう
- Expected: にわ [c1]
- Explanation: 庭 is read にわ here and means garden; yard. Context: 庭に花があります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-516c-5712-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 公園 in context.
- Prompt: Choose the reading of 公園 (park).
- Choices: c0: かいしゃ | c1: がくせい | c2: こうえん
- Expected: こうえん [c2]
- Explanation: 公園 is read こうえん here and means park. Context: 公園に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-56f3-66f8-9928-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 図書館 in context.
- Prompt: Choose the reading of 図書館 (library).
- Choices: c0: としょかん | c1: あたらしい | c2: いそがしい
- Expected: としょかん [c0]
- Explanation: 図書館 is read としょかん here and means library. Context: 図書館で本を借ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5bb6-65cf-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 家族 in context.
- Prompt: Choose the reading of 家族 (family).
- Choices: c0: あかい | c1: かぞく | c2: あける
- Expected: かぞく [c1]
- Explanation: 家族 is read かぞく here and means family. Context: 家族と話します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5144-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 兄 in context.
- Prompt: Choose the reading of 兄 (my older brother).
- Choices: c0: あし | c1: あじ | c2: あに
- Expected: あに [c2]
- Explanation: 兄 is read あに here and means my older brother. Context: 兄は家にいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5f1f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 弟 in context.
- Prompt: Choose the reading of 弟 (younger brother).
- Choices: c0: おとうと | c1: おおきい | c2: おしえる
- Expected: おとうと [c0]
- Explanation: 弟 is read おとうと here and means younger brother. Context: 弟は学生です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-59c9-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 姉 in context.
- Prompt: Choose the reading of 姉 (my older sister).
- Choices: c0: あに | c1: あね | c2: あめ
- Expected: あね [c1]
- Explanation: 姉 is read あね here and means my older sister. Context: 姉は家にいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-59b9-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 妹 in context.
- Prompt: Choose the reading of 妹 (younger sister).
- Choices: c0: おぼえる | c1: かいしゃ | c2: いもうと
- Expected: いもうと [c2]
- Explanation: 妹 is read いもうと here and means younger sister. Context: 妹は学生です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-592b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 夫 in context.
- Prompt: Choose the reading of 夫 (my husband).
- Choices: c0: おっと | c1: あまい | c2: あるく
- Expected: おっと [c0]
- Explanation: 夫 is read おっと here and means my husband. Context: 夫と出かけます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-59bb-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 妻 in context.
- Prompt: Choose the reading of 妻 (my wife).
- Choices: c0: いう | c1: つま | c2: いえ
- Expected: つま [c1]
- Explanation: 妻 is read つま here and means my wife. Context: 妻と出かけます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-89aa-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 親 in context.
- Prompt: Choose the reading of 親 (parent).
- Choices: c0: あき | c1: あさ | c2: おや
- Expected: おや [c2]
- Explanation: 親 is read おや here and means parent. Context: 親と話します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e21-89aa-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 両親 in context.
- Prompt: Choose the reading of 両親 (both parents; parents).
- Choices: c0: りょうしん | c1: いそがしい | c2: おとこのこ
- Expected: りょうしん [c0]
- Explanation: 両親 is read りょうしん here and means both parents; parents. Context: 両親と住んでいます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7956-6bcd-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 祖母 in context.
- Prompt: Choose the reading of 祖母 (my grandmother).
- Choices: c0: あし | c1: そぼ | c2: あじ
- Expected: そぼ [c1]
- Explanation: 祖母 is read そぼ here and means my grandmother. Context: 祖母に会います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e8c-5341-6b73-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 二十歳 in context.
- Prompt: Choose the reading of 二十歳 (twenty years old).
- Choices: c0: あそぶ | c1: あたま | c2: はたち
- Expected: はたち [c2]
- Explanation: 二十歳 is read はたち here and means twenty years old. Context: 二十歳です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8a95-751f-65e5-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 誕生日 in context.
- Prompt: Choose the reading of 誕生日 (birthday).
- Choices: c0: たんじょうび | c1: あたらしい | c2: いそがしい
- Expected: たんじょうび [c0]
- Explanation: 誕生日 is read たんじょうび here and means birthday. Context: 今日は誕生日です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7d50-5a5a-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 結婚 in context.
- Prompt: Choose the reading of 結婚 (marriage).
- Choices: c0: おとうと | c1: けっこん | c2: おぼえる
- Expected: けっこん [c1]
- Explanation: 結婚 is read けっこん here and means marriage. Context: 結婚しています。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5f7c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 彼 in context.
- Prompt: Choose the reading of 彼 (he; him).
- Choices: c0: あめ | c1: いう | c2: かれ
- Expected: かれ [c2]
- Explanation: 彼 is read かれ here and means he; him. Context: 彼は友達です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-96a3-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 隣 in context.
- Prompt: Choose the reading of 隣 (next door; beside).
- Choices: c0: となり | c1: あるく | c2: いしゃ
- Expected: となり [c0]
- Explanation: 隣 is read となり here and means next door; beside. Context: 隣の家です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f55-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 何 in context.
- Prompt: Choose the reading of 何 (what).
- Choices: c0: あき | c1: なに | c2: あさ
- Expected: なに [c1]
- Explanation: 何 is read なに here and means what. Context: 何が好きですか。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8ab0-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 誰 in context.
- Prompt: Choose the reading of 誰 (who).
- Choices: c0: あさ | c1: あし | c2: だれ
- Expected: だれ [c2]
- Explanation: 誰 is read だれ here and means who. Context: 誰が来ますか。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f53-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 体 in context.
- Prompt: Choose the reading of 体 (body).
- Choices: c0: からだ | c1: あける | c2: あそぶ
- Expected: からだ [c0]
- Explanation: 体 is read からだ here and means body. Context: 体を動かします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-982d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 頭 in context.
- Prompt: Choose the reading of 頭 (head).
- Choices: c0: あそぶ | c1: あたま | c2: あぶら
- Expected: あたま [c1]
- Explanation: 頭 is read あたま here and means head. Context: 頭が痛いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-76ee-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 目 in context.
- Prompt: Choose the reading of 目 (eye).
- Choices: c0: と | c1: は | c2: め
- Expected: め [c2]
- Explanation: 目 is read め here and means eye. Context: 目を閉じます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8033-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 耳 in context.
- Prompt: Choose the reading of 耳 (ear).
- Choices: c0: みみ | c1: あね | c2: あめ
- Expected: みみ [c0]
- Explanation: 耳 is read みみ here and means ear. Context: 耳が痛いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9f3b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 鼻 in context.
- Prompt: Choose the reading of 鼻 (nose).
- Choices: c0: あめ | c1: はな | c2: いう
- Expected: はな [c1]
- Explanation: 鼻 is read はな here and means nose. Context: 鼻をかみます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6b6f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 歯 in context.
- Prompt: Choose the reading of 歯 (tooth; teeth).
- Choices: c0: あさ | c1: あし | c2: は
- Expected: は [c2]
- Explanation: 歯 is read は here and means tooth; teeth. Context: 歯を磨きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8db3-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 足 in context.
- Prompt: Choose the reading of 足 (foot; leg).
- Choices: c0: あし | c1: あき | c2: あさ
- Expected: あし [c0]
- Explanation: 足 is read あし here and means foot; leg. Context: 足が痛いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-624b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 手 in context.
- Prompt: Choose the reading of 手 (hand).
- Choices: c0: し | c1: て | c2: じ
- Expected: て [c1]
- Explanation: 手 is read て here and means hand. Context: 手を洗います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6307-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 指 in context.
- Prompt: Choose the reading of 指 (finger).
- Choices: c0: あし | c1: あじ | c2: ゆび
- Expected: ゆび [c2]
- Explanation: 指 is read ゆび here and means finger. Context: 指で示します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5fc3-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 心 in context.
- Prompt: Choose the reading of 心 (heart; mind).
- Choices: c0: こころ | c1: あそぶ | c2: あたま
- Expected: こころ [c0]
- Explanation: 心 is read こころ here and means heart; mind. Context: 心が落ち着きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-529b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 力 in context.
- Prompt: Choose the reading of 力 (strength; power).
- Choices: c0: あたま | c1: ちから | c2: あぶら
- Expected: ちから [c1]
- Explanation: 力 is read ちから here and means strength; power. Context: 力を合わせます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-75c5-9662-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 病院 in context.
- Prompt: Choose the reading of 病院 (hospital).
- Choices: c0: きょうしつ | c1: こうじょう | c2: びょういん
- Expected: びょういん [c2]
- Explanation: 病院 is read びょういん here and means hospital. Context: 病院に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-533b-8005-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 医者 in context.
- Prompt: Choose the reading of 医者 (doctor).
- Choices: c0: いしゃ | c1: あまい | c2: あるく
- Expected: いしゃ [c0]
- Explanation: 医者 is read いしゃ here and means doctor. Context: 医者に相談します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-85ac-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 薬 in context.
- Prompt: Choose the reading of 薬 (medicine).
- Choices: c0: あるく | c1: くすり | c2: いしゃ
- Expected: くすり [c1]
- Explanation: 薬 is read くすり here and means medicine. Context: 薬を飲みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-85ac-5c40-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 薬局 in context.
- Prompt: Choose the reading of 薬局 (pharmacy).
- Choices: c0: あたらしい | c1: いそがしい | c2: やっきょく
- Expected: やっきょく [c2]
- Explanation: 薬局 is read やっきょく here and means pharmacy. Context: 薬局に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-75db-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 痛い in context.
- Prompt: Choose the reading of 痛い (painful; sore).
- Choices: c0: いたい | c1: あかい | c2: あける
- Expected: いたい [c0]
- Explanation: 痛い is read いたい here and means painful; sore. Context: 頭が痛いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-71b1-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 熱 in context.
- Prompt: Choose the reading of 熱 (fever; heat).
- Choices: c0: あし | c1: ねつ | c2: あじ
- Expected: ねつ [c1]
- Explanation: 熱 is read ねつ here and means fever; heat. Context: 熱があります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7d19-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 紙 in context.
- Prompt: Choose the reading of 紙 (paper).
- Choices: c0: あじ | c1: あに | c2: かみ
- Expected: かみ [c2]
- Explanation: 紙 is read かみ here and means paper. Context: 紙に書きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5b57-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 字 in context.
- Prompt: Choose the reading of 字 (character; written letter).
- Choices: c0: じ | c1: は | c2: め
- Expected: じ [c0]
- Explanation: 字 is read じ here and means character; written letter. Context: 字を書きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6587-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 文 in context.
- Prompt: Choose the reading of 文 (sentence).
- Choices: c0: あね | c1: ぶん | c2: あめ
- Expected: ぶん [c1]
- Explanation: 文 is read ぶん here and means sentence. Context: 短い文を書きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-65e5-672c-8a9e-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 日本語 in context.
- Prompt: Choose the reading of 日本語 (Japanese language).
- Choices: c0: おぼえる | c1: かいしゃ | c2: にほんご
- Expected: にほんご [c2]
- Explanation: 日本語 is read にほんご here and means Japanese language. Context: 日本語を勉強します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-82f1-8a9e-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 英語 in context.
- Prompt: Choose the reading of 英語 (English language).
- Choices: c0: えいご | c1: あるく | c2: いしゃ
- Expected: えいご [c0]
- Explanation: 英語 is read えいご here and means English language. Context: 英語を話します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6f22-5b57-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 漢字 in context.
- Prompt: Choose the reading of 漢字 (kanji; Chinese-derived character).
- Choices: c0: あおい | c1: かんじ | c2: あかい
- Expected: かんじ [c1]
- Explanation: 漢字 is read かんじ here and means kanji; Chinese-derived character. Context: 漢字を読みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8aad-3080-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 読む in context.
- Prompt: Choose the reading of 読む (to read).
- Choices: c0: あさ | c1: あし | c2: よむ
- Expected: よむ [c2]
- Explanation: 読む is read よむ here and means to read. Context: 本を読む時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-66f8-304f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 書く in context.
- Prompt: Choose the reading of 書く (to write).
- Choices: c0: かく | c1: あし | c2: あじ
- Expected: かく [c0]
- Explanation: 書く is read かく here and means to write. Context: 名前を書く場所です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-805e-304f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 聞く in context.
- Prompt: Choose the reading of 聞く (to listen; to ask).
- Choices: c0: あじ | c1: きく | c2: あに
- Expected: きく [c1]
- Explanation: 聞く is read きく here and means to listen; to ask. Context: 音楽を聞く時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8a71-3059-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 話す in context.
- Prompt: Choose the reading of 話す (to speak).
- Choices: c0: あたま | c1: あぶら | c2: はなす
- Expected: はなす [c2]
- Explanation: 話す is read はなす here and means to speak. Context: 日本語で話す練習です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8a00-3046-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 言う in context.
- Prompt: Choose the reading of 言う (to say).
- Choices: c0: いう | c1: あね | c2: あめ
- Expected: いう [c0]
- Explanation: 言う is read いう here and means to say. Context: 何と言うか考えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-601d-3046-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 思う in context.
- Prompt: Choose the reading of 思う (to think; to feel).
- Choices: c0: あまい | c1: おもう | c2: あるく
- Expected: おもう [c1]
- Explanation: 思う is read おもう here and means to think; to feel. Context: どう思うか教えてください。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-77e5-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 知る in context.
- Prompt: Choose the reading of 知る (to find out; to know).
- Choices: c0: いう | c1: いえ | c2: しる
- Expected: しる [c2]
- Explanation: 知る is read しる here and means to find out; to know. Context: 町のことを知るために歩きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8003-3048-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 考える in context.
- Prompt: Choose the reading of 考える (to think; to consider).
- Choices: c0: かんがえる | c1: あたらしい | c2: いそがしい
- Expected: かんがえる [c0]
- Explanation: 考える is read かんがえる here and means to think; to consider. Context: 答えを考える時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6559-3048-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 教える in context.
- Prompt: Choose the reading of 教える (to teach; to tell).
- Choices: c0: いちねん | c1: おしえる | c2: いもうと
- Expected: おしえる [c1]
- Explanation: 教える is read おしえる here and means to teach; to tell. Context: 日本語を教える仕事です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7fd2-3046-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 習う in context.
- Prompt: Choose the reading of 習う (to learn; to take lessons).
- Choices: c0: あける | c1: あそぶ | c2: ならう
- Expected: ならう [c2]
- Explanation: 習う is read ならう here and means to learn; to take lessons. Context: 日本語を習う予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-52c9-5f37-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 勉強 in context.
- Prompt: Choose the reading of 勉強 (study).
- Choices: c0: べんきょう | c1: おんなのこ | c2: かんがえる
- Expected: べんきょう [c0]
- Explanation: 勉強 is read べんきょう here and means study. Context: 日本語の勉強をします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5f37-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 強い in context.
- Prompt: Choose the reading of 強い (strong).
- Choices: c0: あたま | c1: つよい | c2: あぶら
- Expected: つよい [c1]
- Explanation: 強い is read つよい here and means strong. Context: 風が強いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7df4-7fd2-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 練習 in context.
- Prompt: Choose the reading of 練習 (practice).
- Choices: c0: きょうしつ | c1: こうじょう | c2: れんしゅう
- Expected: れんしゅう [c2]
- Explanation: 練習 is read れんしゅう here and means practice. Context: 毎日練習します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7b54-3048-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 答え in context.
- Prompt: Choose the reading of 答え (answer).
- Choices: c0: こたえ | c1: あまい | c2: あるく
- Expected: こたえ [c0]
- Explanation: 答え is read こたえ here and means answer. Context: 答えを書きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8cea-554f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 質問 in context.
- Prompt: Choose the reading of 質問 (question).
- Choices: c0: かいしゃ | c1: しつもん | c2: がくせい
- Expected: しつもん [c1]
- Explanation: 質問 is read しつもん here and means question. Context: 質問があります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-554f-984c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 問題 in context.
- Prompt: Choose the reading of 問題 (question; problem).
- Choices: c0: あかるい | c1: いちねん | c2: もんだい
- Expected: もんだい [c2]
- Explanation: 問題 is read もんだい here and means question; problem. Context: 問題を読みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8a66-9a13-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 試験 in context.
- Prompt: Choose the reading of 試験 (test; examination).
- Choices: c0: しけん | c1: あかい | c2: あける
- Expected: しけん [c0]
- Explanation: 試験 is read しけん here and means test; examination. Context: 試験を受けます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5bbf-984c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 宿題 in context.
- Prompt: Choose the reading of 宿題 (homework).
- Choices: c0: おとこのこ | c1: しゅくだい | c2: おんなのこ
- Expected: しゅくだい [c1]
- Explanation: 宿題 is read しゅくだい here and means homework. Context: 宿題をします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5fd8-308c-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 忘れる in context.
- Prompt: Choose the reading of 忘れる (to forget).
- Choices: c0: おおきい | c1: おしえる | c2: わすれる
- Expected: わすれる [c2]
- Explanation: 忘れる is read わすれる here and means to forget. Context: 名前を忘れることがあります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-899a-3048-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 覚える in context.
- Prompt: Choose the reading of 覚える (to remember; to learn by heart).
- Choices: c0: おぼえる | c1: おしえる | c2: おとうと
- Expected: おぼえる [c0]
- Explanation: 覚える is read おぼえる here and means to remember; to learn by heart. Context: 新しい言葉を覚える練習です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5f85-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 待つ in context.
- Prompt: Choose the reading of 待つ (to wait).
- Choices: c0: あね | c1: まつ | c2: あめ
- Expected: まつ [c1]
- Explanation: 待つ is read まつ here and means to wait. Context: ここで待つことにします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6301-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 持つ in context.
- Prompt: Choose the reading of 持つ (to hold; to carry).
- Choices: c0: あめ | c1: いう | c2: もつ
- Expected: もつ [c2]
- Explanation: 持つ is read もつ here and means to hold; to carry. Context: 荷物を持つ人です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-53d6-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 取る in context.
- Prompt: Choose the reading of 取る (to take).
- Choices: c0: とる | c1: いう | c2: いえ
- Expected: とる [c0]
- Explanation: 取る is read とる here and means to take. Context: 本を取る前に聞きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f7f-3046-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 使う in context.
- Prompt: Choose the reading of 使う (to use).
- Choices: c0: あおい | c1: つかう | c2: あかい
- Expected: つかう [c1]
- Explanation: 使う is read つかう here and means to use. Context: これを使う予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f5c-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 作る in context.
- Prompt: Choose the reading of 作る (to make).
- Choices: c0: あかい | c1: あける | c2: つくる
- Expected: つくる [c2]
- Explanation: 作る is read つくる here and means to make. Context: 料理を作る時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8cb7-3046-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 買う in context.
- Prompt: Choose the reading of 買う (to buy).
- Choices: c0: かう | c1: あし | c2: あじ
- Expected: かう [c0]
- Explanation: 買う is read かう here and means to buy. Context: 本を買う予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-58f2-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 売る in context.
- Prompt: Choose the reading of 売る (to sell).
- Choices: c0: あじ | c1: うる | c2: あに
- Expected: うる [c1]
- Explanation: 売る is read うる here and means to sell. Context: パンを売る店です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-501f-308a-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 借りる in context.
- Prompt: Choose the reading of 借りる (to borrow).
- Choices: c0: あたま | c1: あぶら | c2: かりる
- Expected: かりる [c2]
- Explanation: 借りる is read かりる here and means to borrow. Context: 本を借りる予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8cb8-3059-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 貸す in context.
- Prompt: Choose the reading of 貸す (to lend).
- Choices: c0: かす | c1: あね | c2: あめ
- Expected: かす [c0]
- Explanation: 貸す is read かす here and means to lend. Context: 本を貸す前に名前を聞きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8fd4-3059-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 返す in context.
- Prompt: Choose the reading of 返す (to return something).
- Choices: c0: あまい | c1: かえす | c2: あるく
- Expected: かえす [c1]
- Explanation: 返す is read かえす here and means to return something. Context: 本を返す日です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9001-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 送る in context.
- Prompt: Choose the reading of 送る (to send).
- Choices: c0: あるく | c1: いしゃ | c2: おくる
- Expected: おくる [c2]
- Explanation: 送る is read おくる here and means to send. Context: 手紙を送る予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-53d7-3051-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 受ける in context.
- Prompt: Choose the reading of 受ける (to receive; to take a test).
- Choices: c0: うける | c1: あおい | c2: あかい
- Expected: うける [c0]
- Explanation: 受ける is read うける here and means to receive; to take a test. Context: 試験を受ける予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-958b-3051-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 開ける in context.
- Prompt: Choose the reading of 開ける (to open something).
- Choices: c0: あかい | c1: あける | c2: あそぶ
- Expected: あける [c1]
- Explanation: 開ける is read あける here and means to open something. Context: 窓を開ける前に聞きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9589-3081-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 閉める in context.
- Prompt: Choose the reading of 閉める (to close something).
- Choices: c0: あける | c1: あそぶ | c2: しめる
- Expected: しめる [c2]
- Explanation: 閉める is read しめる here and means to close something. Context: 店を閉める時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-59cb-307e-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 始まる in context.
- Prompt: Choose the reading of 始まる (to begin).
- Choices: c0: はじまる | c1: おおきい | c2: おしえる
- Expected: はじまる [c0]
- Explanation: 始まる is read はじまる here and means to begin. Context: 授業が始まる時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7d42-308f-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 終わる in context.
- Prompt: Choose the reading of 終わる (to end; to finish).
- Choices: c0: あたま | c1: おわる | c2: あぶら
- Expected: おわる [c1]
- Explanation: 終わる is read おわる here and means to end; to finish. Context: 仕事が終わる時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6b62-307e-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 止まる in context.
- Prompt: Choose the reading of 止まる (to stop).
- Choices: c0: あぶら | c1: あまい | c2: とまる
- Expected: とまる [c2]
- Explanation: 止まる is read とまる here and means to stop. Context: ここで止まるバスです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6b69-304f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 歩く in context.
- Prompt: Choose the reading of 歩く (to walk).
- Choices: c0: あるく | c1: あまい | c2: いしゃ
- Expected: あるく [c0]
- Explanation: 歩く is read あるく here and means to walk. Context: 歩くのが好きです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8d70-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 走る in context.
- Prompt: Choose the reading of 走る (to run).
- Choices: c0: あるく | c1: はしる | c2: いしゃ
- Expected: はしる [c1]
- Explanation: 走る is read はしる here and means to run. Context: 走るのが好きです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6cf3-3050-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 泳ぐ in context.
- Prompt: Choose the reading of 泳ぐ (to swim).
- Choices: c0: あおい | c1: あかい | c2: およぐ
- Expected: およぐ [c2]
- Explanation: 泳ぐ is read およぐ here and means to swim. Context: 泳ぐのが好きです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-904a-3076-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 遊ぶ in context.
- Prompt: Choose the reading of 遊ぶ (to play; to spend leisure time).
- Choices: c0: あそぶ | c1: あかい | c2: あける
- Expected: あそぶ [c0]
- Explanation: 遊ぶ is read あそぶ here and means to play; to spend leisure time. Context: 友達と遊ぶ予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7acb-3064-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 立つ in context.
- Prompt: Choose the reading of 立つ (to stand).
- Choices: c0: あし | c1: たつ | c2: あじ
- Expected: たつ [c1]
- Explanation: 立つ is read たつ here and means to stand. Context: ここに立つ人です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5ea7-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 座る in context.
- Prompt: Choose the reading of 座る (to sit).
- Choices: c0: あそぶ | c1: あたま | c2: すわる
- Expected: すわる [c2]
- Explanation: 座る is read すわる here and means to sit. Context: ここに座ることにします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e57-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 乗る in context.
- Prompt: Choose the reading of 乗る (to ride; to board).
- Choices: c0: のる | c1: あに | c2: あね
- Expected: のる [c0]
- Explanation: 乗る is read のる here and means to ride; to board. Context: 電車に乗る予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-964d-308a-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 降りる in context.
- Prompt: Choose the reading of 降りる (to get off; to descend).
- Choices: c0: あぶら | c1: おりる | c2: あまい
- Expected: おりる [c1]
- Explanation: 降りる is read おりる here and means to get off; to descend. Context: 次の駅で降りる予定です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5e30-308b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 帰る in context.
- Prompt: Choose the reading of 帰る (to go home; to return).
- Choices: c0: あまい | c1: あるく | c2: かえる
- Expected: かえる [c2]
- Explanation: 帰る is read かえる here and means to go home; to return. Context: 家に帰る時間です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-62bc-3059-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 押す in context.
- Prompt: Choose the reading of 押す (to push; to press).
- Choices: c0: おす | c1: いう | c2: いえ
- Expected: おす [c0]
- Explanation: 押す is read おす here and means to push; to press. Context: このボタンを押すと開きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5f15-304f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 引く in context.
- Prompt: Choose the reading of 引く (to pull).
- Choices: c0: あき | c1: ひく | c2: あさ
- Expected: ひく [c1]
- Explanation: 引く is read ひく here and means to pull. Context: この戸は引くと開きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5c11-306a-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 少ない in context.
- Prompt: Choose the reading of 少ない (few; little).
- Choices: c0: いちねん | c1: いもうと | c2: すくない
- Expected: すくない [c2]
- Explanation: 少ない is read すくない here and means few; little. Context: 人が少ないです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-591a-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 多い in context.
- Prompt: Choose the reading of 多い (many; much).
- Choices: c0: おおい | c1: あける | c2: あそぶ
- Expected: おおい [c0]
- Explanation: 多い is read おおい here and means many; much. Context: 人が多いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5168-90e8-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 全部 in context.
- Prompt: Choose the reading of 全部 (all; everything).
- Choices: c0: あそぶ | c1: ぜんぶ | c2: あたま
- Expected: ぜんぶ [c1]
- Explanation: 全部 is read ぜんぶ here and means all; everything. Context: 全部ください。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-540c-3058-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 同じ in context.
- Prompt: Choose the reading of 同じ (the same).
- Choices: c0: あたま | c1: あぶら | c2: おなじ
- Expected: おなじ [c2]
- Explanation: 同じ is read おなじ here and means the same. Context: 同じ本です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5225-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 別 in context.
- Prompt: Choose the reading of 別 (different; separate).
- Choices: c0: べつ | c1: あね | c2: あめ
- Expected: べつ [c0]
- Explanation: 別 is read べつ here and means different; separate. Context: 別の本です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4ed6-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 他 in context.
- Prompt: Choose the reading of 他 (other; another).
- Choices: c0: あめ | c1: ほか | c2: いう
- Expected: ほか [c1]
- Explanation: 他 is read ほか here and means other; another. Context: 他の店に行きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6709-540d-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 有名 in context.
- Prompt: Choose the reading of 有名 (famous).
- Choices: c0: かいしゃ | c1: がくせい | c2: ゆうめい
- Expected: ゆうめい [c2]
- Explanation: 有名 is read ゆうめい here and means famous. Context: 有名な店です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7121-6599-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 無料 in context.
- Prompt: Choose the reading of 無料 (free of charge).
- Choices: c0: むりょう | c1: あかるい | c2: いちねん
- Expected: むりょう [c0]
- Explanation: 無料 is read むりょう here and means free of charge. Context: ここは無料です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5fc5-8981-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 必要 in context.
- Prompt: Choose the reading of 必要 (necessary).
- Choices: c0: いちねん | c1: ひつよう | c2: いもうと
- Expected: ひつよう [c1]
- Explanation: 必要 is read ひつよう here and means necessary. Context: 予約が必要です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4fbf-5229-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 便利 in context.
- Prompt: Choose the reading of 便利 (convenient).
- Choices: c0: あける | c1: あそぶ | c2: べんり
- Expected: べんり [c2]
- Explanation: 便利 is read べんり here and means convenient. Context: この町は便利です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e0d-4fbf-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 不便 in context.
- Prompt: Choose the reading of 不便 (inconvenient).
- Choices: c0: ふべん | c1: あそぶ | c2: あたま
- Expected: ふべん [c0]
- Explanation: 不便 is read ふべん here and means inconvenient. Context: ここは少し不便です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-60aa-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 悪い in context.
- Prompt: Choose the reading of 悪い (bad).
- Choices: c0: あたま | c1: わるい | c2: あぶら
- Expected: わるい [c1]
- Explanation: 悪い is read わるい here and means bad. Context: 天気が悪いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-91cd-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 重い in context.
- Prompt: Choose the reading of 重い (heavy).
- Choices: c0: あぶら | c1: あまい | c2: おもい
- Expected: おもい [c2]
- Explanation: 重い is read おもい here and means heavy. Context: この本は重いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8efd-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 軽い in context.
- Prompt: Choose the reading of 軽い (light in weight).
- Choices: c0: かるい | c1: あまい | c2: あるく
- Expected: かるい [c0]
- Explanation: 軽い is read かるい here and means light in weight. Context: この本は軽いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5e83-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 広い in context.
- Prompt: Choose the reading of 広い (spacious; wide).
- Choices: c0: あるく | c1: ひろい | c2: いしゃ
- Expected: ひろい [c1]
- Explanation: 広い is read ひろい here and means spacious; wide. Context: 広い部屋です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-72ed-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 狭い in context.
- Prompt: Choose the reading of 狭い (narrow; cramped).
- Choices: c0: あおい | c1: あかい | c2: せまい
- Expected: せまい [c2]
- Explanation: 狭い is read せまい here and means narrow; cramped. Context: 狭い部屋です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-77ed-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 短い in context.
- Prompt: Choose the reading of 短い (short).
- Choices: c0: みじかい | c1: いちねん | c2: いもうと
- Expected: みじかい [c0]
- Explanation: 短い is read みじかい here and means short. Context: 短い文です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4f4e-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 低い in context.
- Prompt: Choose the reading of 低い (low).
- Choices: c0: あける | c1: ひくい | c2: あそぶ
- Expected: ひくい [c1]
- Explanation: 低い is read ひくい here and means low. Context: 低い山です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-65e9-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 早い in context.
- Prompt: Choose the reading of 早い (early).
- Choices: c0: あそぶ | c1: あたま | c2: はやい
- Expected: はやい [c2]
- Explanation: 早い is read はやい here and means early. Context: 今日は早い電車に乗ります。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9045-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 遅い in context.
- Prompt: Choose the reading of 遅い (late; slow).
- Choices: c0: おそい | c1: あたま | c2: あぶら
- Expected: おそい [c0]
- Explanation: 遅い is read おそい here and means late; slow. Context: 今日は帰りが遅いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-901f-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 速い in context.
- Prompt: Choose the reading of 速い (fast).
- Choices: c0: あぶら | c1: はやい | c2: あまい
- Expected: はやい [c1]
- Explanation: 速い is read はやい here and means fast. Context: 速い電車です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6625-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 春 in context.
- Prompt: Choose the reading of 春 (spring).
- Choices: c0: あめ | c1: いう | c2: はる
- Expected: はる [c2]
- Explanation: 春 is read はる here and means spring. Context: 春に花が咲きます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-590f-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 夏 in context.
- Prompt: Choose the reading of 夏 (summer).
- Choices: c0: なつ | c1: いう | c2: いえ
- Expected: なつ [c0]
- Explanation: 夏 is read なつ here and means summer. Context: 夏は暑いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-79cb-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 秋 in context.
- Prompt: Choose the reading of 秋 (autumn).
- Choices: c0: あさ | c1: あき | c2: あし
- Expected: あき [c1]
- Explanation: 秋 is read あき here and means autumn. Context: 秋は涼しいです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-51ac-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 冬 in context.
- Prompt: Choose the reading of 冬 (winter).
- Choices: c0: あさ | c1: あし | c2: ふゆ
- Expected: ふゆ [c2]
- Explanation: 冬 is read ふゆ here and means winter. Context: 冬は寒いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-96ea-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 雪 in context.
- Prompt: Choose the reading of 雪 (snow).
- Choices: c0: ゆき | c1: あし | c2: あじ
- Expected: ゆき [c0]
- Explanation: 雪 is read ゆき here and means snow. Context: 雪が降っています。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-98a8-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 風 in context.
- Prompt: Choose the reading of 風 (wind).
- Choices: c0: あじ | c1: かぜ | c2: あに
- Expected: かぜ [c1]
- Explanation: 風 is read かぜ here and means wind. Context: 風が強いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-96f2-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 雲 in context.
- Prompt: Choose the reading of 雲 (cloud).
- Choices: c0: あに | c1: あね | c2: くも
- Expected: くも [c2]
- Explanation: 雲 is read くも here and means cloud. Context: 雲が見えます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6674-308c-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 晴れ in context.
- Prompt: Choose the reading of 晴れ (clear weather).
- Choices: c0: はれ | c1: あね | c2: あめ
- Expected: はれ [c0]
- Explanation: 晴れ is read はれ here and means clear weather. Context: 今日は晴れです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6697-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 暗い in context.
- Prompt: Choose the reading of 暗い (dark).
- Choices: c0: あまい | c1: くらい | c2: あるく
- Expected: くらい [c1]
- Explanation: 暗い is read くらい here and means dark. Context: 部屋が暗いです。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-660e-308b-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 明るい in context.
- Prompt: Choose the reading of 明るい (bright).
- Choices: c0: がくせい | c1: くだもの | c2: あかるい
- Expected: あかるい [c2]
- Explanation: 明るい is read あかるい here and means bright. Context: 明るい部屋です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5915-65b9-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 夕方 in context.
- Prompt: Choose the reading of 夕方 (early evening).
- Choices: c0: ゆうがた | c1: あかるい | c2: いちねん
- Expected: ゆうがた [c0]
- Explanation: 夕方 is read ゆうがた here and means early evening. Context: 夕方に会いましょう。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4eca-6669-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 今晩 in context.
- Prompt: Choose the reading of 今晩 (this evening; tonight).
- Choices: c0: いちねん | c1: こんばん | c2: いもうと
- Expected: こんばん [c1]
- Explanation: 今晩 is read こんばん here and means this evening; tonight. Context: 今晩、電話します。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e88-7d04-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 予約 in context.
- Prompt: Choose the reading of 予約 (reservation).
- Choices: c0: あける | c1: あそぶ | c2: よやく
- Expected: よやく [c2]
- Explanation: 予約 is read よやく here and means reservation. Context: 予約をします。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8a08-753b-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 計画 in context.
- Prompt: Choose the reading of 計画 (plan).
- Choices: c0: けいかく | c1: おおきい | c2: おしえる
- Expected: けいかく [c0]
- Explanation: 計画 is read けいかく here and means plan. Context: 旅行の計画を立てます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-4e00-5ea6-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 一度 in context.
- Prompt: Choose the reading of 一度 (once; one time).
- Choices: c0: あたま | c1: いちど | c2: あぶら
- Expected: いちど [c1]
- Explanation: 一度 is read いちど here and means once; one time. Context: 一度行きました。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-3054-98ef-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of ご飯 in context.
- Prompt: Choose the reading of ご飯 (cooked rice; meal).
- Choices: c0: あぶら | c1: あまい | c2: ごはん
- Expected: ごはん [c2]
- Explanation: ご飯 is read ごはん here and means cooked rice; meal. Context: ご飯を食べます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8089-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 肉 in context.
- Prompt: Choose the reading of 肉 (meat).
- Choices: c0: にく | c1: あめ | c2: いう
- Expected: にく [c0]
- Explanation: 肉 is read にく here and means meat. Context: 肉を食べます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7c73-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 米 in context.
- Prompt: Choose the reading of 米 (uncooked rice).
- Choices: c0: いう | c1: こめ | c2: いえ
- Expected: こめ [c1]
- Explanation: 米 is read こめ here and means uncooked rice. Context: 米を洗います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-725b-4e73-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 牛乳 in context.
- Prompt: Choose the reading of 牛乳 (milk).
- Choices: c0: いちまんえん | c1: きゅうりょう | c2: ぎゅうにゅう
- Expected: ぎゅうにゅう [c2]
- Explanation: 牛乳 is read ぎゅうにゅう here and means milk. Context: 牛乳を飲みます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8c5a-8089-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 豚肉 in context.
- Prompt: Choose the reading of 豚肉 (pork).
- Choices: c0: ぶたにく | c1: いちねん | c2: いもうと
- Expected: ぶたにく [c0]
- Explanation: 豚肉 is read ぶたにく here and means pork. Context: 豚肉を買います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9d8f-8089-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 鶏肉 in context.
- Prompt: Choose the reading of 鶏肉 (chicken meat).
- Choices: c0: いもうと | c1: とりにく | c2: おおきい
- Expected: とりにく [c1]
- Explanation: 鶏肉 is read とりにく here and means chicken meat. Context: 鶏肉を買います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5375-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 卵 in context.
- Prompt: Choose the reading of 卵 (egg).
- Choices: c0: あそぶ | c1: あたま | c2: たまご
- Expected: たまご [c2]
- Explanation: 卵 is read たまご here and means egg. Context: 卵を買います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-91ce-83dc-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 野菜 in context.
- Prompt: Choose the reading of 野菜 (vegetables).
- Choices: c0: やさい | c1: あたま | c2: あぶら
- Expected: やさい [c0]
- Explanation: 野菜 is read やさい here and means vegetables. Context: 野菜を食べます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-679c-7269-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 果物 in context.
- Prompt: Choose the reading of 果物 (fruit).
- Choices: c0: おとうと | c1: くだもの | c2: おぼえる
- Expected: くだもの [c1]
- Explanation: 果物 is read くだもの here and means fruit. Context: 果物を食べます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5869-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 塩 in context.
- Prompt: Choose the reading of 塩 (salt).
- Choices: c0: あめ | c1: いう | c2: しお
- Expected: しお [c2]
- Explanation: 塩 is read しお here and means salt. Context: 塩を入れます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7802-7cd6-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 砂糖 in context.
- Prompt: Choose the reading of 砂糖 (sugar).
- Choices: c0: さとう | c1: あるく | c2: いしゃ
- Expected: さとう [c0]
- Explanation: 砂糖 is read さとう here and means sugar. Context: 砂糖を入れます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-6cb9-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 油 in context.
- Prompt: Choose the reading of 油 (oil).
- Choices: c0: あおい | c1: あぶら | c2: あかい
- Expected: あぶら [c1]
- Explanation: 油 is read あぶら here and means oil. Context: 油を使います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-5473-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 味 in context.
- Prompt: Choose the reading of 味 (taste; flavor).
- Choices: c0: あさ | c1: あし | c2: あじ
- Expected: あじ [c2]
- Explanation: 味 is read あじ here and means taste; flavor. Context: 味を見ます。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-7518-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 甘い in context.
- Prompt: Choose the reading of 甘い (sweet).
- Choices: c0: あまい | c1: あける | c2: あそぶ
- Expected: あまい [c0]
- Explanation: 甘い is read あまい here and means sweet. Context: 甘いお菓子です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-8f9b-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 辛い in context.
- Prompt: Choose the reading of 辛い (spicy; hot in taste).
- Choices: c0: あそぶ | c1: からい | c2: あたま
- Expected: からい [c1]
- Explanation: 辛い is read からい here and means spicy; hot in taste. Context: 辛い料理です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-9178-3063-3071-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 酸っぱい in context.
- Prompt: Choose the reading of 酸っぱい (sour).
- Choices: c0: おしえる | c1: おとうと | c2: すっぱい
- Expected: すっぱい [c2]
- Explanation: 酸っぱい is read すっぱい here and means sour. Context: 酸っぱい味です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-82e6-3044-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 苦い in context.
- Prompt: Choose the reading of 苦い (bitter).
- Choices: c0: にがい | c1: あぶら | c2: あまい
- Expected: にがい [c0]
- Explanation: 苦い is read にがい here and means bitter. Context: 苦い薬です。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}

#### ja-context-76bf-reading

- [ ] Qualified review; notes: pending
- Type/skill/difficulty: multiple_choice / reading / 2
- Objective: Recognize the whole-word reading of 皿 in context.
- Prompt: Choose the reading of 皿 (plate; dish).
- Choices: c0: あめ | c1: さら | c2: いう
- Expected: さら [c1]
- Explanation: 皿 is read さら here and means plate; dish. Context: 皿を洗います。 This checks this whole word, not every reading of its characters.
- Hint: Use the word context, or reveal the answer when useful.
- Policy: {"strategy":"choice"}
