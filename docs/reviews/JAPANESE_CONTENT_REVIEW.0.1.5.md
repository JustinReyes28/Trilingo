# Japanese content review packet

Source: content/courses/ja/starter.json · ja-starter version 0.1.5
SHA-256 of the exact source file: 423664433d8b6627ed12276c3c8ed7c4b51f2610aa021384af95c19af538a77c

Status: pending qualified Japanese-language review. This packet assembles existing source material; it is not a review approval, proficiency assessment, or learner-facing answer response.

User decision (2026-10-23): no reviewer is available yet. Keep new material draft and the existing slice labeled technical practice; this does not close the qualified-review gate.

Reviewer: pending
Qualifications: pending
Review date: pending
Reviewed source version/hash: pending

## Review instructions

- Check meaning, naturalness, register, kana/kanji readings, spelling, accepted alternatives, and the objective of each item.
- Note corrections by stable ID. For constrained exercises, verify every accepted key and ensure distractors are unambiguous.
- For open composition, models are examples; do not turn them into exact-string answer keys.
- Review audio scripts as text only. No audio has been generated or listened to, and the checkpoint references still point to text exercises for later adaptation.
- Keep draft items unpublished until reviewed and their feature is available. Record reviewer identity, qualifications, date, source version/hash and any limitations.
- After corrections, increment the content version, validate/import it, and regenerate this packet for the final reviewed source. Do not mark the phase complete from internal AI checks alone.

## Scope

Published technical practice: 2 units, 6 lessons, 30 exercise definitions, 8 core word entries and 5 expressions.
Draft references: Stage A character/word/first-sentence tasks; three Stage B compositions; one story and two audio-episode scripts.

## Published unit guides and exercise keys

### ja-unit-1 — First sounds and greetings

こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.

ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.

A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.

#### ja-greetings-hello — Say hello

Objective: Recognize and use a daytime greeting.

- [ ] Qualified review: ja-greetings-hello-choice
  - Type/skill: multiple_choice / recognition
  - Prompt: Choose the daytime greeting.
  - Choices: c0: こんにちは | c1: ありがとう | c2: さようなら
  - Expected/accepted: こんにちは [c0]
  - Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-hello-type
  - Type/skill: translation / typing
  - Prompt: Write “hello” as a daytime greeting in Japanese.
  - Expected/accepted: こんにちは
  - Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-hello-blank
  - Type/skill: fill_blank / typing
  - Prompt: Complete the greeting: こんに＿＿
  - Expected/accepted: ちは
  - Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-hello-order
  - Type/skill: sentence_ordering / recognition
  - Prompt: Arrange the parts into the taught expression.
  - Displayed tokens: t1: 。 | t0: こんにちは
  - Expected/accepted: こんにちは。 | Token IDs: t0, t1
  - Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-hello-match
  - Type/skill: matching / meaning
  - Prompt: Match each Japanese expression with its English meaning.
  - Expected/accepted: こんにちは → Hello | さようなら → Goodbye
  - Explanation: こんにちは is a daytime greeting. Its final は is pronounced wa; keep the conventional spelling.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

#### ja-greetings-thanks — Say thank you

Objective: Recognize thanks and a polite thank-you.

- [ ] Qualified review: ja-greetings-thanks-choice
  - Type/skill: multiple_choice / recognition
  - Prompt: Which phrase means “thank you” in a casual exchange?
  - Choices: c0: ありがとう | c1: こんばんは | c2: さようなら
  - Expected/accepted: ありがとう [c0]
  - Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-thanks-type
  - Type/skill: translation / typing
  - Prompt: Write a casual “thank you” in Japanese.
  - Expected/accepted: ありがとう
  - Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-thanks-blank
  - Type/skill: fill_blank / typing
  - Prompt: Complete the polite thank-you: ありがとう［　］
  - Expected/accepted: ございます
  - Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-thanks-order
  - Type/skill: sentence_ordering / recognition
  - Prompt: Arrange the parts into the taught expression.
  - Displayed tokens: t2: 。 | t1: ございます | t0: ありがとう
  - Expected/accepted: ありがとうございます。 | Token IDs: t0, t1, t2
  - Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-thanks-match
  - Type/skill: matching / meaning
  - Prompt: Match each Japanese expression with its English meaning.
  - Expected/accepted: ありがとう → Thank you | ありがとうございます → Thank you (polite)
  - Explanation: ありがとう expresses thanks; ありがとうございます adds politeness. The longer phrase is useful with people you do not know well.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

#### ja-greetings-names — Introduce yourself

Objective: Use a simple introduction with です.

- [ ] Qualified review: ja-greetings-names-choice
  - Type/skill: multiple_choice / recognition
  - Prompt: You meet someone for the first time. Choose “Nice to meet you.”
  - Choices: c0: はじめまして | c1: おやすみなさい | c2: ありがとう
  - Expected/accepted: はじめまして [c0]
  - Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-names-type
  - Type/skill: translation / typing
  - Prompt: Write “I am Aki.” Use アキ and polite です.
  - Expected/accepted: アキです。 | アキです
  - Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-names-blank
  - Type/skill: fill_blank / typing
  - Prompt: Complete “I am Aki”: アキ＿＿
  - Expected/accepted: です
  - Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-names-order
  - Type/skill: sentence_ordering / recognition
  - Prompt: Arrange the parts into the taught expression.
  - Displayed tokens: t2: 。 | t1: です | t0: アキ
  - Expected/accepted: アキです。 | Token IDs: t0, t1, t2
  - Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-greetings-names-match
  - Type/skill: matching / meaning
  - Prompt: Match each Japanese expression with its English meaning.
  - Expected/accepted: はじめまして → Nice to meet you | アキです → I am Aki
  - Explanation: A name followed by です is a polite introduction. Japanese can leave “I” unstated when the context is clear.
  - Hint: Look at the phrase parts and the politeness requested.
  - Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

### ja-unit-2 — Hiragana foundations

The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.

The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.

Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.

#### ja-hiragana-vowels — Meet the vowels

Objective: Recognize the first five hiragana and read simple vowel words.

- [ ] Qualified review: ja-hiragana-vowels-choice
  - Type/skill: multiple_choice / recognition
  - Prompt: Which hiragana represents the sound a?
  - Choices: c0: あ | c1: い | c2: う
  - Expected/accepted: あ [c0]
  - Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-vowels-type
  - Type/skill: translation / typing
  - Prompt: Write the hiragana for the sound i.
  - Expected/accepted: い
  - Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-vowels-blank
  - Type/skill: fill_blank / typing
  - Prompt: Complete the vowel row: あ・い・う・＿＿・お
  - Expected/accepted: え
  - Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-vowels-order
  - Type/skill: sentence_ordering / recognition
  - Prompt: Arrange the five vowel kana in chart order.
  - Displayed tokens: t4: お | t3: え | t2: う | t1: い | t0: あ
  - Expected/accepted: あいうえお | Token IDs: t0, t1, t2, t3, t4
  - Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-vowels-match
  - Type/skill: matching / meaning
  - Prompt: Match each Japanese expression with its English meaning.
  - Expected/accepted: あい → Love | いえ → House
  - Explanation: The first vowel row is あ (a), い (i), う (u), え (e), お (o). The simple words あい and いえ combine these kana.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

#### ja-hiragana-k — Read the k row

Objective: Read k-row kana in short everyday words.

- [ ] Qualified review: ja-hiragana-k-choice
  - Type/skill: multiple_choice / recognition
  - Prompt: Which kana represents the sound ki?
  - Choices: c0: き | c1: か | c2: こ
  - Expected/accepted: き [c0]
  - Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-k-type
  - Type/skill: translation / typing
  - Prompt: Write the word “here” using hiragana: koko.
  - Expected/accepted: ここ
  - Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-k-blank
  - Type/skill: fill_blank / typing
  - Prompt: Complete “face”: か＿＿
  - Expected/accepted: お
  - Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-k-order
  - Type/skill: sentence_ordering / recognition
  - Prompt: Arrange the k-row kana in chart order.
  - Displayed tokens: t4: こ | t3: け | t2: く | t1: き | t0: か
  - Expected/accepted: かきくけこ | Token IDs: t0, t1, t2, t3, t4
  - Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-k-match
  - Type/skill: matching / meaning
  - Prompt: Match each Japanese expression with its English meaning.
  - Expected/accepted: かお → Face | こえ → Voice
  - Explanation: The k row is か・き・く・け・こ. In かお (face), both か and the vowel お keep their sounds.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

#### ja-hiragana-sounds — Notice sound differences

Objective: Notice voicing, vowel length and small っ in authored word examples.

- [ ] Qualified review: ja-hiragana-sounds-choice
  - Type/skill: multiple_choice / recognition
  - Prompt: Which spelling means “stamp” (kitte)?
  - Choices: c0: きって | c1: きて | c2: きいて
  - Expected/accepted: きって [c0]
  - Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"choice","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-sounds-type
  - Type/skill: translation / typing
  - Prompt: Write the voiced counterpart of か.
  - Expected/accepted: が
  - Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-sounds-blank
  - Type/skill: fill_blank / typing
  - Prompt: Complete the word for “stamp”: き＿＿て
  - Expected/accepted: っ
  - Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"script":"japanese","strategy":"exact","spacing":"preserve","hint_policy":"always_available","required_distinctions":["voicing","kana_size","vowel_length","target_script"]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-sounds-order
  - Type/skill: sentence_ordering / recognition
  - Prompt: Build the word for “school” (gakkō).
  - Displayed tokens: t3: う | t2: こ | t1: っ | t0: が
  - Expected/accepted: がっこう | Token IDs: t0, t1, t2, t3
  - Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"tokens","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

- [ ] Qualified review: ja-hiragana-sounds-match
  - Type/skill: matching / meaning
  - Prompt: Match each Japanese expression with its English meaning.
  - Expected/accepted: がっこう → School | きって → Postage stamp
  - Explanation: Dakuten changes か to が. Small っ marks a pause before the next consonant: きって differs from きて. In がっこう, こう has a long vowel.
  - Hint: Check the shape, voicing marks, and kana size.
  - Policy: {"strategy":"pairs","spacing":"preserve","hint_policy":"always_available","required_distinctions":[]}
  - Corrections/notes: pending

## Vocabulary and expressions

- [ ] Qualified review: ja-word-hello
  - こんにちは / こんにちは — Hello (daytime)
  - Kind/POS/register: phrase / greeting / neutral
  - Example: こんにちは。アキです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-goodbye
  - さようなら / さようなら — Goodbye
  - Kind/POS/register: phrase / greeting / neutral
  - Example: さようなら。またあした。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-thanks
  - ありがとう / ありがとう — Thank you
  - Kind/POS/register: phrase / expression / casual
  - Example: ありがとう。うれしいです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-polite-thanks
  - ありがとうございます / ありがとうございます — Thank you (polite)
  - Kind/POS/register: phrase / expression / polite
  - Example: ありがとうございます。たすかりました。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-first-meeting
  - はじめまして / はじめまして — Nice to meet you
  - Kind/POS/register: phrase / greeting / neutral
  - Example: はじめまして。アキです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-copula
  - です / です — Polite copula
  - Kind/POS/register: word / auxiliary / polite
  - Example: アキです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-love
  - あい / あい — Love
  - Kind/POS/register: word / noun / neutral
  - Example: あいはたいせつです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-house
  - いえ / いえ — House
  - Kind/POS/register: word / noun / neutral
  - Example: これはいえです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-here
  - ここ / ここ — Here
  - Kind/POS/register: word / demonstrative / neutral
  - Example: ここです。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-face
  - かお / かお — Face
  - Kind/POS/register: word / noun / neutral
  - Example: かおをあらいます。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-voice
  - こえ / こえ — Voice
  - Kind/POS/register: word / noun / neutral
  - Example: いいこえですね。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-school
  - がっこう / がっこう — School
  - Kind/POS/register: word / noun / neutral
  - Example: がっこうにいきます。
  - Corrections/notes: pending

- [ ] Qualified review: ja-word-stamp
  - きって / きって — Postage stamp
  - Kind/POS/register: word / noun / neutral
  - Example: きってをください。
  - Corrections/notes: pending

## Draft writing references

### ja-write-character-a — constrained character practice

Stage/status: stage-a / draft

Prompt: Enter the full-size hiragana for the sound a.

Model: あ

Alternatives: None authored for this constrained reference.

Self-review checklist:
- Use full-size あ, rather than small ぁ.
- Treat this as a character-production reference; no handwriting or pronunciation assessment is implied.

- [ ] Qualified review of prompt, model, alternatives and checklist
Corrections/notes: pending

### ja-write-word-house — constrained word practice

Stage/status: stage-a / draft

Prompt: Write the word house in hiragana.

Model: いえ

Alternatives: None authored for this constrained reference.

Self-review checklist:
- Use い followed by え.
- Use hiragana for this task; a kanji rendering is outside this script objective.

- [ ] Qualified review of prompt, model, alternatives and checklist
Corrections/notes: pending

### ja-write-first — first sentence

Stage/status: stage-a / draft

Prompt: Introduce yourself with your name and です.

Model: アキです。

Alternatives: ハルです。

Self-review checklist:
- Use your name.
- Finish with polite です.

- [ ] Qualified review of prompt, model, alternatives and checklist
Corrections/notes: pending

### ja-write-intro — introduction

Stage/status: stage-b / draft

Prompt: Write three short sentences: your name, where you live, and one thing you like.

Model: アキです。シンガポールに住んでいます。コーヒーが好きです。

Alternatives: ハルです。東京に住んでいます。お茶が好きです。

Self-review checklist:
- Give your name.
- Name where you live.
- Say what you like.
- Keep polite endings consistent.

Revision before: アキです。シンガポール。コーヒー。
Revision after: アキです。シンガポールに住んでいます。コーヒーが好きです。
Reason: Add predicates to turn the place and preference into complete statements.

- [ ] Qualified review of prompt, model, alternatives and checklist
Corrections/notes: pending

### ja-write-routine — routine

Stage/status: stage-b / draft

Prompt: Write three to five sentences about your morning and one evening activity.

Model: 毎朝七時に起きます。朝ごはんを食べます。コーヒーを飲みます。夜は日本語を勉強します。

Alternatives: 毎朝八時に起きます。お茶を飲みます。夜は本を読みます。

Self-review checklist:
- Put events in a clear order.
- Use times you know.
- Use polite verbs consistently.

- [ ] Qualified review of prompt, model, alternatives and checklist
Corrections/notes: pending

### ja-write-message — invitation

Stage/status: stage-b / draft

Prompt: Write a short message inviting a friend to have tea tomorrow. Suggest a time.

Model: こんにちは。あした、お茶を飲みませんか。三時はどうですか。

Alternatives: こんにちは。あした、コーヒーを飲みませんか。二時はどうですか。

Self-review checklist:
- Greet the reader.
- Make an invitation.
- Suggest a time.
- Check politeness.

- [ ] Qualified review of prompt, model, alternatives and checklist
Corrections/notes: pending

## Draft story and audio scripts

### ja-story-first-meeting — A first meeting

Kind/status: story / draft
Objectives: Recognize a greeting and a name in a brief exchange.
Vocabulary references: ja-word-hello, ja-word-first-meeting, ja-word-copula
Advisory preparation: None
Transcript policy: visible
Audio: None; script only, not played or assessed

- story-greet — Aki: こんにちは。アキです。
  - Next: story-reply; checkpoint references: None
- story-reply — Haru: はじめまして。ハルです。
  - Next: End; checkpoint references: None

Optional recap references: None
- [ ] Qualified text/transcript review; real listening review remains Phase 8 work
Corrections/notes: pending

### ja-audio-first-introduction — A first introduction

Kind/status: audio_episode / draft
Objectives: Recognize a daytime greeting, a first-meeting expression and two names.
Vocabulary references: ja-word-hello, ja-word-first-meeting, ja-word-copula
Advisory preparation: ja-greetings-hello, ja-greetings-names
Transcript policy: deliberate_reveal
Audio: None; script only, not played or assessed

- audio-intro-aki — Aki: こんにちは。はじめまして。アキです。
  - Next: audio-intro-haru; checkpoint references: None
- audio-intro-haru — Haru: はじめまして。ハルです。
  - Next: End; checkpoint references: ja-greetings-names-choice

Optional recap references: ja-greetings-names-match
- [ ] Qualified text/transcript review; real listening review remains Phase 8 work
Corrections/notes: pending

### ja-audio-thanks-contexts — Thanks in two settings

Kind/status: audio_episode / draft
Objectives: Distinguish the casual and polite thank-you expressions in two short reference clips.
Vocabulary references: ja-word-thanks, ja-word-polite-thanks
Advisory preparation: ja-greetings-thanks
Transcript policy: deliberate_reveal
Audio: None; script only, not played or assessed

- audio-thanks-friend — Aki, thanking a friend: ありがとう。
  - Next: audio-thanks-polite; checkpoint references: None
- audio-thanks-polite — Aki, in a polite exchange: ありがとうございます。
  - Next: End; checkpoint references: ja-greetings-thanks-choice

Optional recap references: ja-greetings-thanks-match
- [ ] Qualified text/transcript review; real listening review remains Phase 8 work
Corrections/notes: pending

## Review outcome

- [ ] Reviewer identity, qualifications and date recorded
- [ ] Accepted/corrected item IDs and remaining issues recorded
- [ ] Final source version/hash matches the reviewed material
- [ ] No qualified-review or mastery claim has been inferred from tests or this packet

Overall outcome: pending.

## Optional assessment drafts

All banks remain draft. They reuse the item keys above; no reviewed level, access requirement or mastery certificate is implied.

### ja-recap-greetings — First exchanges recap

- [ ] Qualified review of selection and interpretation
- Kind/status: recap / draft
- Concepts: greeting, politeness
- Question references: ja-greetings-hello-choice, ja-greetings-thanks-choice, ja-greetings-names-choice
- Interpretation: Count actual unaided answers separately from assisted answers and skips. Results suggest practice only; no pass score controls access.
- Corrections/notes: pending

### ja-placement-first-steps — Find a useful starting point

- [ ] Qualified review of selection and interpretation
- Kind/status: placement / draft
- Concepts: greeting, politeness, kana
- Question references: ja-greetings-hello-choice, ja-greetings-thanks-type, ja-hiragana-vowels-choice, ja-hiragana-sounds-blank
- Interpretation: Use your first unassisted responses as a practice snapshot. Revisit missed concepts in any order; every lesson remains available. This draft does not certify a level.
- Corrections/notes: pending

### ja-mastery-first-steps — First phrases and kana self-check

- [ ] Qualified review of selection and interpretation
- Kind/status: mastery / draft
- Concepts: greeting, politeness, kana
- Question references: ja-greetings-names-type, ja-greetings-thanks-match, ja-hiragana-k-type, ja-hiragana-sounds-choice
- Interpretation: Report first-answer accuracy and concept coverage, with assistance and skips separate. A result is optional feedback; no score grants or removes access or certifies mastery.
- Corrections/notes: pending

