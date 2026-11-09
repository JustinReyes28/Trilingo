"""Original unit expansion: honest inventory, keys, draft access and saved IDs."""

import json

from app.config import ROOT
from app.content_audit import inventory
from app.grading import grade
from app.reading import available_exercise_ids
from app.services import load_content

# Keep the original 838-row batch's exact regression baseline immutable. The
# current additive source and full preservation contract have their own tests.
SOURCE = ROOT / "docs/reviews/ja-starter-0.1.20/source.json"
MANIFEST = ROOT / "content/authoring/ja/beginner-unit-vocabulary-draft.json"


def test_original_unit_expansion_preserves_published_slice_and_stable_words():
    before = load_content(ROOT / "docs/reviews/ja-starter-0.1.16/source.json")
    after = load_content(SOURCE)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = [row for unit in manifest["units"] for row in unit["rows"]]
    assert len(rows) == 838
    assert {unit["unit_id"] for unit in manifest["units"]} == {unit.id for unit in after.units}
    old_words = {word.id: word for word in before.vocabulary}
    words = {word.id: word for word in after.vocabulary}
    assert old_words.keys() <= words.keys()
    assert len(words.keys() - old_words.keys()) == 833
    assert all(words[key].status == "draft" for key in words.keys() - old_words.keys())
    for word in before.vocabulary:
        if word.status == "published":
            assert words[word.id] == word
        else:
            old = word.model_dump(exclude={"practice_exercise_ids"})
            assert words[word.id].model_dump(exclude={"practice_exercise_ids"}) == old
    original_lessons = {lesson.id: lesson for unit in before.units for lesson in unit.lessons}
    added = [
        lesson
        for unit in after.units
        for lesson in unit.lessons
        if lesson.id not in original_lessons
    ]
    assert len(added) == 112
    assert all(lesson.status == "draft" and lesson.exercises for lesson in added)
    for unit in after.units:
        assert all(
            lesson == original_lessons[lesson.id]
            for lesson in unit.lessons
            if lesson.id in original_lessons
        )
    assert next(row for row in rows if row["surface"] == "切手")["word_id"] == "ja-word-stamp"
    assert next(row for row in rows if row["surface"] == "卵")["word_id"] == "ja-word-kanji-5375"
    assert all(
        row["example"] and row["translation"] and words[row["word_id"]].reading == row["reading"]
        for row in rows
    )


def test_all_new_keys_grade_and_draft_checks_are_not_publicly_exposed():
    content = load_content(SOURCE)
    added = [
        exercise
        for unit in content.units
        for lesson in unit.lessons
        if "-core-" in lesson.id
        for exercise in lesson.exercises
    ]
    assert len(added) == 1363
    assert {exercise.answer for exercise in added if exercise.type == "multiple_choice"} == {
        "c1",
        "c2",
        "c3",
    }
    for exercise in added:
        if exercise.type == "multiple_choice":
            assert grade(exercise, exercise.answer)
            assert all(
                not grade(exercise, choice.id)
                for choice in exercise.choices
                if choice.id != exercise.answer
            )
            assert set(exercise.response_feedback) == {choice.id for choice in exercise.choices}
        else:
            assert exercise.type == "translation" and exercise.skill == "typing"
            assert all(grade(exercise, answer) for answer in exercise.answers)
            assert not grade(exercise, "unrelated answer")
    keys = {exercise.id for exercise in added}
    assert not keys & available_exercise_ids(content)
    assert keys <= available_exercise_ids(content, include_drafts=True)
    guide_keys = {
        key
        for note in content.grammar_notes
        if note.status == "draft"
        for key in note.practice_exercise_ids
    }
    assert keys <= guide_keys


def test_new_words_have_explicit_unit_practice_and_conservative_identity_counts():
    report = inventory(SOURCE, SOURCE.with_name("lexical-identities.json"))
    records = {row["id"]: row for row in report["records"]}
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for group in manifest["units"]:
        for row in group["rows"]:
            record = records[row["word_id"]]
            if record["status"] == "draft":
                assert group["unit_id"] in record["unit_ids"]
                assert record["unit_mapping"] == "linked lesson exercises"
                assert "meaning" in record["practice_directions"]
    assert report["canonical_words_by_introduction_stage"] == {"stage-a": 541, "stage-b": 566}
    assert all(row["decision_recorded"] for row in report["reading_collisions"])
    assert report["canonical_word_count"] == 1107
    assert report["counts"]["phrase"]["authored"] == 15
