"""Apply the original beginner vocabulary batch to its immutable 0.1.16 source.

Local only; writes content JSON, never the learner database. All additions stay draft.
"""

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app.content_schema import CourseContent
from app.grading import grade

GUIDES = [
    "ja-guide-intro",
    "ja-guide-unit-2-kana-patterns",
    "ja-guide-unit-3-katakana-length",
    "ja-guide-unit-4-things-questions",
    "ja-guide-unit-5-clock-time",
    "ja-guide-unit-6-order-request",
    "ja-guide-unit-7-ask-directions",
    "ja-guide-unit-8-polite-routine",
    "ja-guide-unit-9-descriptions-likes",
    "ja-guide-unit-10-invite-message",
]
DISTRACTORS = [
    "a railway station",
    "a mountain",
    "a newspaper",
    "a dog",
    "a hospital",
    "a bridge",
    "a kitchen",
    "a teacher",
    "a bicycle",
    "a key",
    "a cloud",
    "a fish",
    "a window",
    "a library",
    "a postage stamp",
    "a toothbrush",
    "to swim",
    "to buy",
    "to read",
    "to wait",
    "to open",
    "to sing",
    "every week",
    "sometimes",
    "immediately",
    "first; to begin with",
    "heavy",
    "narrow",
    "red",
    "expensive",
    "sweet",
    "cold weather",
]


def apply_batch(source: dict, manifest: dict) -> dict:
    if (
        source["id"] != manifest["course_id"]
        or source["version"] != manifest["base_version"]
    ):
        raise ValueError(
            "Use the exact archived base version; do not rewrite an existing release"
        )
    result = copy.deepcopy(source)
    words = {word["id"]: word for word in result["vocabulary"]}
    guides = {guide["id"]: guide for guide in result["grammar_notes"]}
    units = {unit["id"]: unit for unit in result["units"]}
    for group_index, group in enumerate(manifest["units"]):
        unit = units[group["unit_id"]]
        guide = guides[GUIDES[group_index]]
        offset = 0
        if sum(group["lesson_sizes"]) != len(group["rows"]):
            raise ValueError(
                "Lesson boundaries must cover every authored row exactly once"
            )
        for chunk_index, size in enumerate(group["lesson_sizes"]):
            rows = group["rows"][offset : offset + size]
            lesson_id = f"{unit['id']}-core-{chunk_index + 1:02}"
            exercises = []
            for row_index, row in enumerate(rows):
                word_id = row["word_id"]
                if word_id not in words:
                    word = {
                        "id": word_id,
                        "surface": row["surface"],
                        "reading": row["reading"],
                        "gloss": row["gloss"],
                        "part_of_speech": row["part_of_speech"],
                        "entry_kind": "phrase"
                        if row["part_of_speech"] == "phrase"
                        else "word",
                        "register": "polite"
                        if row["part_of_speech"] == "phrase"
                        and "ございます" in row["surface"]
                        else "context-dependent; see example",
                        "example": [{"surface": row["example"]}],
                        "concepts": group["concepts"],
                        "stage": unit["stage"],
                        "status": "draft",
                        "audio": None,
                        "practice_exercise_ids": [],
                    }
                    result["vocabulary"].append(word)
                    words[word_id] = word
                word = words[word_id]
                key = f"{lesson_id}-v{row_index + 1}"
                explanation = f"{row['surface']}（{row['reading']}）: {row['gloss']}. {row['example']} — {row['translation']}"
                base = {
                    "objective": f"Understand {row['surface']} in an everyday context.",
                    "concepts": group["concepts"],
                    "difficulty": 1 if unit["stage"] == "stage-a" else 2,
                    "explanation": explanation,
                    "hint": f"The reading is {row['reading']}. Use Reveal for the meaning and example translation.",
                    "preparation": [],
                }
                # Distractors name unrelated senses, rather than alternative translations
                # of a near synonym. Exact choices remain in the qualified-review queue.
                candidates = [
                    value
                    for value in DISTRACTORS
                    if not any(
                        token in value.lower().replace(";", "").split()
                        for token in row["gloss"].lower().replace(";", "").split()
                        if len(token) > 3
                    )
                ]
                start = (offset + row_index + group_index * 5) % len(candidates)
                wrong = [candidates[start], candidates[(start + 7) % len(candidates)]]
                labels = wrong[:]
                correct = (offset + row_index + group_index) % 3
                labels.insert(correct, row["gloss"])
                exercise = {
                    **base,
                    "id": key + "-meaning",
                    "type": "multiple_choice",
                    "skill": "meaning",
                    "prompt": f"{row['example']}\nIn this example, what does 「{row['surface']}」 mean?",
                    "policy": {"strategy": "choice"},
                    "choices": [
                        {"id": f"c{i + 1}", "text": label}
                        for i, label in enumerate(labels)
                    ],
                    "answer": f"c{correct + 1}",
                    "response_feedback": {
                        f"c{i + 1}": explanation
                        if i == correct
                        else f"That sense does not match 「{row['surface']}」 here. {explanation}"
                        for i in range(3)
                    },
                }
                exercises.append(exercise)
                linked = [exercise["id"]]
                # One explicit kana reading per word makes typing evidence distinct
                # from recognition, including long vowels and small kana.
                reading = {
                    **base,
                    "id": key + "-reading",
                    "type": "translation",
                    "skill": "typing",
                    "objective": f"Type the kana reading of {row['surface']}.",
                    "prompt": f"Write the reading of 「{row['surface']}」 in hiragana. Meaning in this example: {row['gloss']}.",
                    "hint": "Use the word's dictionary reading. Reveal is always available.",
                    "policy": {
                        "strategy": "exact",
                        "script": "hiragana",
                        "normalization": "NFC",
                        "spacing": "ignore",
                        "required_distinctions": [
                            "voicing",
                            "kana_size",
                            "vowel_length",
                        ],
                    },
                    "answers": [row["reading"]],
                }
                # Kana-only words already show their reading in the question;
                # those are meaning practice, not a claimed reading assessment.
                if any("一" <= char <= "鿿" for char in row["surface"]):
                    exercises.append(reading)
                    linked.append(reading["id"])
                if word["status"] == "draft":
                    word["practice_exercise_ids"] = list(
                        dict.fromkeys(word.get("practice_exercise_ids", []) + linked)
                    )
            lesson = {
                "id": lesson_id,
                "title": group["lesson_titles"][chunk_index],
                "japanese_title": "・".join(row["surface"] for row in rows[:3]),
                "objective": f"Recognize the everyday senses in {group['lesson_titles'][chunk_index].lower()}.",
                "order": len(unit["lessons"]) + 1,
                "status": "draft",
                "preparation": [],
                "exercises": exercises,
            }
            unit["lessons"].append(lesson)
            guide["practice_exercise_ids"] = list(
                dict.fromkeys(
                    guide["practice_exercise_ids"]
                    + [exercise["id"] for exercise in exercises]
                )
            )
            offset += size
    result["version"] = manifest["target_version"]
    result["review_note"] += (
        " Original ten-topic vocabulary expansion remains draft; independent Japanese review and complete 500+1500 lexical coverage are still pending."
    )
    validated = CourseContent.model_validate(result)
    for unit in validated.units:
        for lesson in unit.lessons:
            if "-core-" not in lesson.id:
                continue
            for exercise in lesson.exercises:
                answers = (
                    [exercise.answer]
                    if exercise.type == "multiple_choice"
                    else exercise.answers
                )
                if not all(grade(exercise, answer) for answer in answers):
                    raise ValueError(
                        f"{exercise.id}: an authored key is rejected by its answer policy"
                    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT / "docs/reviews/ja-starter-0.1.16/source.json",
    )
    parser.add_argument(
        "--output", type=Path, default=ROOT / "content/courses/ja/starter.json"
    )
    args = parser.parse_args()
    manifest = json.loads(
        (ROOT / "content/authoring/ja/beginner-unit-vocabulary-draft.json").read_text(
            encoding="utf-8"
        )
    )
    digest = hashlib.sha256(args.source.read_bytes()).hexdigest()
    if digest != manifest["base_sha256"]:
        raise ValueError(
            "The archived base source does not match the authoring manifest"
        )
    result = apply_batch(json.loads(args.source.read_text(encoding="utf-8")), manifest)
    encoded = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if args.output.exists():
        existing = json.loads(args.output.read_text(encoding="utf-8"))
        if (
            existing["version"] != manifest["base_version"]
            and args.output.read_bytes() != encoded
        ):
            raise ValueError(
                "Do not overwrite a different version; choose a new output path"
            )
    args.output.write_bytes(encoded)
    print(
        f"Validated {result['version']}: {len(result['vocabulary'])} vocabulary records; all new material is draft. No database touched."
    )


if __name__ == "__main__":
    main()
