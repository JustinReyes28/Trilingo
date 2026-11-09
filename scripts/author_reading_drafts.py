"""Offline original draft reading additions; does not publish or touch a database."""
import json
from pathlib import Path

source = Path(__file__).resolve().parents[1] / "content/courses/ja/starter.json"
content = json.loads(source.read_text(encoding="utf-8"))
if content["version"] != "0.1.6" or any(x["id"] == "kana-small" for x in content["concepts"]):
    raise SystemExit("Apply once to the original kana-only 0.1.6 draft.")
concepts = [
    ("kana-small", "Small kana change the sound", "きゃ is one combined mora (kya); きや has two morae (ki-ya). Small ゃ/ゅ/ょ combine after an i-row kana. Small っ marks a held consonant before the next sound: きって (stamp), not きて. Audio examples arrive with audio practice."),
    ("kana-n", "The independent ん", "ん counts as one mora. It can occur inside or at the end of a word: ほん (book). Its sound changes with neighboring sounds; do not delete it or confuse it with a following vowel."),
    ("kana-length", "Keep long vowels", "Vowel length can distinguish words. おばさん (aunt) and おばあさん (grandmother) differ in length. In hiragana, long vowels use authored spellings: おかあさん and がっこう. Katakana commonly uses ー: コーヒー. Do not shorten these spellings. Audio contrasts are not available yet."),
    ("kana-voicing", "Voicing and similar shapes", "Dakuten changes a kana: か→が and は→ば. Handakuten gives は→ぱ. Katakana シ/ツ and ソ/ン have similar shapes; notice the orientation and placement of the short strokes. A font sample is a reading aid, not stroke-order instruction."),
    ("reading-context", "Read a kanji inside a word", "Kanji readings depend on the word. 日 is に in 日本 (にほん), but にち in 日曜日 (にちようび). Study the whole contextual word. One recognition answer does not prove every reading or handwriting skill."),
]
content["concepts"].extend({"id": key, "title": title, "explanation": note} for key, title, note in concepts)
for char in content["characters"]:
    extra = "kana-small" if char["form"] in {"small", "combination"} else "kana-voicing" if char["form"] in {"voiced", "semi_voiced"} else "kana-n" if char["surface"] in {"ん", "ン"} else None
    if extra:
        char["concepts"].append(extra)
content["characters"].append({"id": "ja-char-long-mark", "surface": "ー", "script": "katakana", "form": "mark", "contextual_readings": ["long-vowel mark"], "romaji": None, "meaning": "Lengthens the preceding vowel in katakana", "notes": "Read it as vowel length, not a separate syllable. Example: コーヒー.", "vocabulary_ids": [], "practice_exercise_ids": [], "components": [], "stage": "stage-a", "concepts": ["kana-length"], "status": "draft"})

def choice(key, prompt, choices, answer, explanation, concept="reading-context"):
    entry = {"id": key, "type": "multiple_choice", "skill": "reading", "prompt": prompt, "objective": prompt, "concepts": [concept], "difficulty": 1, "choices": [{"id": "c"+str(i), "text": text} for i, text in enumerate(choices)], "answer": "c"+str(answer), "explanation": explanation, "hint": "Use the accompanying context or reveal the answer when useful.", "preparation": [], "policy": {"strategy": "choice"}}
    content["practice_exercises"].append(entry)
    return key

contrasts = [
    ("small-ya", "Choose the spelling with one combined kya sound.", ["きや", "きゃ", "きゅ"], 1, "きゃ combines き and small ゃ. きや keeps a full-size や.", "kana-small"),
    ("small-tsu", "Choose the word for a postage stamp, with a held consonant.", ["きて", "きって", "きつて"], 1, "きって contains small っ; きて is a different form.", "kana-small"),
    ("n", "Choose the spelling hon, keeping the final ん.", ["ほ", "ほん", "ほう"], 1, "ほん keeps the independent ん mora.", "kana-n"),
    ("long-vowel", "Choose the spelling for grandmother (obaasan).", ["おばさん", "おばあさん", "おばさ"], 1, "おばあさん has a long あ; おばさん means aunt.", "kana-length"),
    ("long-mark", "Choose the standard katakana spelling for coffee.", ["コヒ", "コーヒー", "コヒー"], 1, "コーヒー has two long vowels, each written with ー.", "kana-length"),
    ("voicing", "Choose ga in hiragana.", ["か", "が", "ぱ"], 1, "が keeps the dakuten; か and ぱ are different sounds.", "kana-voicing"),
    ("similar-shi", "Choose shi in katakana.", ["ツ", "シ", "ン"], 1, "シ represents shi; compare its short-stroke direction with ツ.", "kana-voicing"),
    ("similar-so", "Choose so in katakana.", ["ン", "ソ", "ノ"], 1, "ソ represents so. ン represents the independent n mora.", "kana-voicing"),
]
for suffix, prompt, choices, answer, note, concept in contrasts:
    key = choice("ja-contrast-"+suffix, prompt, choices, answer, note, concept)
    for char in content["characters"]:
        if concept in char["concepts"]:
            char["practice_exercise_ids"].append(key)

words = [
    ("japan", "日本", "にほん", "Japan"), ("sunday", "日曜日", "にちようび", "Sunday"),
    ("water", "水", "みず", "water"), ("tea", "お茶", "おちゃ", "tea"),
    ("station", "駅", "えき", "station"), ("entrance", "入口", "いりぐち", "entrance"),
    ("exit", "出口", "でぐち", "exit"), ("school-kanji", "学校", "がっこう", "school"),
    ("book", "本", "ほん", "book"), ("time", "時間", "じかん", "time"),
    ("monday", "月曜日", "げつようび", "Monday"), ("tuesday", "火曜日", "かようび", "Tuesday"),
    ("wednesday", "水曜日", "すいようび", "Wednesday"), ("thursday", "木曜日", "もくようび", "Thursday"),
    ("friday", "金曜日", "きんようび", "Friday"), ("saturday", "土曜日", "どようび", "Saturday"),
]
for suffix, surface, reading, gloss in words:
    key = "ja-word-"+suffix
    drill = choice("ja-reading-"+suffix, "Choose the reading of "+surface+" ("+gloss+").", [reading, "ここ", "かお"], 0, surface+" is read "+reading+" in this word.")
    content["vocabulary"].append({"id": key, "surface": surface, "reading": reading, "gloss": gloss, "part_of_speech": "proper noun" if suffix == "japan" else "noun", "entry_kind": "word", "register": "neutral", "example": [{"surface": surface, "reading": reading, "vocabulary_id": key}], "concepts": ["reading-context"], "stage": "stage-a", "status": "draft", "audio": None, "practice_exercise_ids": [drill]})
for word in content["vocabulary"]:
    if word["id"] == "ja-word-house":
        word["practice_exercise_ids"] = ["ja-kana-home-choice", "ja-kana-home-type"]
        # Existing stable exercise IDs are linked below using actual surfaces.
        word["practice_exercise_ids"] = [e["id"] for u in content["units"] for lesson in u["lessons"] for e in lesson["exercises"] if "いえ" in json.dumps(e, ensure_ascii=False)]
for glyph in dict.fromkeys(char for _, surface, _, _ in words for char in surface if "一" <= char <= "鿿"):
    related = [word for word in content["vocabulary"] if glyph in word["surface"] and word["status"] == "draft"]
    content["characters"].append({"id": "ja-kanji-"+format(ord(glyph), "x"), "surface": glyph, "script": "kanji", "form": "kanji", "contextual_readings": [word["surface"]+"（"+word["reading"]+"）" for word in related], "romaji": None, "meaning": "Contextual words: "+", ".join(word["gloss"] for word in related), "notes": "Read this character inside the listed whole words. These are contextual examples, not a list of every reading.", "vocabulary_ids": [word["id"] for word in related], "practice_exercise_ids": [key for word in related for key in word["practice_exercise_ids"]], "components": [], "stage": "stage-a", "concepts": ["reading-context"], "status": "draft"})

def segment(surface, reading=None, word=None):
    return {key: value for key, value in {"surface": surface, "reading": reading, "vocabulary_id": word}.items() if value is not None}

def turn(key, speaker, text, next_ids, exercise_ids):
    return {"id": key, "speaker": speaker, "text": text, "next_turn_ids": next_ids, "exercise_ids": exercise_ids}

def story(key, kind, title, objective, turns, vocabulary, recaps):
    return {"id": key, "kind": kind, "title": title, "stage": "stage-a", "difficulty": 1, "objectives": [objective], "turns": turns, "concepts": ["reading-context"], "vocabulary_ids": vocabulary, "preparation": [], "recap_exercise_ids": recaps, "transcript_policy": "visible", "audio_asset_id": None, "status": "draft"}
intro = next(x for x in content["narratives"] if x["id"] == "ja-story-first-meeting")
intro["turns"][0]["exercise_ids"] = [choice("ja-story-intro-name", "Who introduces themself as Aki?", ["The first speaker", "The second speaker", "Neither speaker"], 0, "The first turn says アキです。", "greeting")]
intro["turns"][0]["text"] = [segment("こんにちは", word="ja-word-hello"), segment("。アキです。")]
intro["turns"][1]["exercise_ids"] = [choice("ja-story-intro-reply", "What does Haru say at this first meeting?", ["Goodbye", "Nice to meet you", "Thank you"], 1, "はじめまして is used at a first meeting.", "greeting")]
intro["recap_exercise_ids"] = ["ja-story-intro-name", "ja-story-intro-reply"]
water_check = choice("ja-story-drink-water", "Which drink does Aki ask for?", ["Tea", "Water", "Coffee"], 1, "水をください asks for water.")
tea_check = choice("ja-story-drink-tea", "Which drink is named in Haru's turn?", ["Water", "Coffee", "Tea"], 2, "お茶 is tea.")
content["narratives"].append(story("ja-story-drink", "story", "Water or tea?", "Follow two short drink requests.", [turn("drink-aki", "Aki", [segment("水", "みず", "ja-word-water"), segment("をください。")], ["drink-haru"], [water_check]), turn("drink-haru", "Haru", [segment("お茶", "おちゃ", "ja-word-tea"), segment("をください。")], ["drink-thanks"], [tea_check]), turn("drink-thanks", "Aki", [segment("ありがとうございます", word="ja-word-polite-thanks"), segment("。")], [], [])], ["ja-word-water", "ja-word-tea", "ja-word-polite-thanks"], [water_check, tea_check]))
sign_check = choice("ja-passage-exit", "Which sign points to the way out?", ["入口", "出口", "学校"], 1, "出口 means exit; 入口 means entrance.")
content["narratives"].append(story("ja-passage-signs", "reading_passage", "At the station", "Distinguish entrance and exit signs.", [turn("sign-station", "Station sign", [segment("駅", "えき", "ja-word-station"), segment("　"), segment("入口", "いりぐち", "ja-word-entrance"), segment(" →　"), segment("出口", "でぐち", "ja-word-exit"), segment(" ←")], [], [sign_check])], ["ja-word-station", "ja-word-entrance", "ja-word-exit"], [sign_check]))
day_check = choice("ja-passage-schedule-day", "On which listed day does class start at 10:00?", ["Monday", "Tuesday", "Sunday"], 1, "The Tuesday row lists 10:00. The Monday row lists 9:00.")
content["narratives"].append(story("ja-passage-schedule", "reading_passage", "A two-day class schedule", "Find a day and time in a small schedule.", [turn("schedule-days", "Class schedule", [segment("月曜日", "げつようび", "ja-word-monday"), segment(" 9:00–10:00\n"), segment("火曜日", "かようび", "ja-word-tuesday"), segment(" 10:00–11:00")], [], [day_check])], ["ja-word-monday", "ja-word-tuesday"], [day_check]))
source.write_text(json.dumps(content, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print("Original reading additions remain draft; no database or published content changed.")
