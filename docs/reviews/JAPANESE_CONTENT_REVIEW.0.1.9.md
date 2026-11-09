# Japanese content review packet

Source: content/courses/ja/starter.json · ja-starter version 0.1.9
SHA-256 of the exact source file: c005f6b1e01db9d7739bad15accfa3b1609cc6c1f288439d28f8965df2b46907

Status: pending qualified Japanese-language and stroke review. This packet contains authoring keys and draft references; it is not an approval or proficiency assessment.

User decision: no reviewer is available. Keep new material draft and the existing slice labeled technical practice. No qualified-review gate is closed.

Reviewer: pending
Qualifications: pending
Review date: pending
Reviewed source version/hash: pending

## Review scope and instructions

Published technical practice remains2units/6lessons/30exercises/8core words/5expressions. Draft extensions:92basic kana,135variants/combinations/marks,18contextual kanji,16core words,2stories,4passages,2audio scripts,7writing tasks and6original stroke templates. Standalone practice definitions:218. Targets300kanji/2000core words are not current coverage.

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
