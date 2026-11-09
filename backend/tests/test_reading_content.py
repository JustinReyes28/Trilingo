import pytest
from pydantic import ValidationError

from app.config import ROOT
from app.content_schema import CourseContent
from app.grading import grade
from app.services import load_content


@pytest.fixture
def reading_content():
    return load_content(ROOT / "content/courses/ja/starter.json")


def test_basic_kana_coverage_and_separate_variants(reading_content):
    chars = reading_content.characters
    for script in ("hiragana", "katakana"):
        basic = [entry for entry in chars if entry.script == script and entry.form == "basic"]
        assert len(basic) == 46
        assert len({entry.surface for entry in basic}) == 46
        assert all(len(entry.surface) == 1 for entry in basic)
        assert all(entry.status == "draft" for entry in basic)
    lookup = {entry.surface: entry for entry in chars}
    assert lookup["が"].form == "voiced"
    assert lookup["ぱ"].form == "semi_voiced"
    assert lookup["きゃ"].form == "combination"
    assert lookup["キャ"].form == "combination"
    assert lookup["っ"].form == "small" and lookup["っ"].surface != lookup["つ"].surface
    assert lookup["シ"].romaji == "shi" and lookup["ツ"].romaji == "tsu"
    assert lookup["あ"].id == "ja-char-a"  # Preserve the pre-existing stable content ID.


def test_all_draft_kana_drills_have_valid_keys_and_owner_references(reading_content):
    exercises = {exercise.id: exercise for exercise in reading_content.practice_exercises}
    basic_drills = [
        e
        for e in exercises.values()
        if e.id.startswith("ja-char-") and e.id.endswith(("-recognize", "-type"))
    ]
    assert len(basic_drills) == 184
    for character in reading_content.characters:
        for key in character.practice_exercise_ids:
            exercise = exercises[key]
            assert exercise.concepts and exercise.objective and exercise.explanation
            if character.form != "basic" or not key.startswith(character.id + "-"):
                continue
            if exercise.type == "multiple_choice":
                expected = next(
                    choice for choice in exercise.choices if choice.id == exercise.answer
                )
                assert expected.text == character.surface
                assert grade(exercise, expected.id)
            else:
                assert exercise.type == "translation"
                assert exercise.answers == [character.surface]
                assert grade(exercise, character.surface)
                wrong_script = "ア" if character.script == "hiragana" else "あ"
                assert not grade(exercise, wrong_script)
    # Authoring drills does not silently expand published lessons or lexical coverage.
    assert (
        sum(
            lesson.status == "published"
            for unit in reading_content.units
            for lesson in unit.lessons
        )
        == 6
    )
    assert (
        sum(
            word.status == "published" and word.entry_kind == "word"
            for word in reading_content.vocabulary
        )
        == 8
    )


@pytest.mark.parametrize(
    "fault",
    ["duplicate_character", "blank_reading", "missing_drill", "blank_answer", "missing_glossary"],
)
def test_reading_graph_rejects_invalid_content(reading_content, fault):
    data = reading_content.model_dump()
    if fault == "duplicate_character":
        duplicate = dict(data["characters"][0])
        duplicate["id"] = "different-id-same-character"
        data["characters"].append(duplicate)
    if fault == "blank_reading":
        data["characters"][0]["contextual_readings"] = [" "]
    if fault == "missing_drill":
        data["characters"][0]["practice_exercise_ids"] = ["missing"]
    if fault == "blank_answer":
        data["practice_exercises"][1]["answers"] = [" "]
    if fault == "missing_glossary":
        data["narratives"][0]["turns"][0]["text"][0]["vocabulary_id"] = "missing-word"
    with pytest.raises(ValidationError):
        CourseContent.model_validate(data)


def test_contextual_kanji_inventory_is_100_a_and_200_additional_b(reading_content):
    kanji = [entry for entry in reading_content.characters if entry.form == "kanji"]
    assert len(kanji) == len({entry.surface for entry in kanji}) == 300
    assert sum(entry.stage == "stage-a" for entry in kanji) == 100
    assert sum(entry.stage == "stage-b" for entry in kanji) == 200
    assert all(entry.status == "draft" for entry in kanji)
    words = {word.id: word for word in reading_content.vocabulary}
    exercises = {exercise.id: exercise for exercise in reading_content.practice_exercises}
    for entry in kanji:
        assert entry.vocabulary_ids and entry.practice_exercise_ids
        # Kana-only canonical spellings (e.g. いえ) keep their stable word ID;
        # the contextual label and prompt still name the kanji spelling.
        assert any(entry.surface in value for value in entry.contextual_readings)
        for key in entry.practice_exercise_ids:
            exercise = exercises[key]
            assert exercise.type == "multiple_choice"
            assert entry.surface in exercise.prompt
            expected = next(
                choice.text for choice in exercise.choices if choice.id == exercise.answer
            )
            assert any(expected == words[word_id].reading for word_id in entry.vocabulary_ids)
            assert grade(exercise, exercise.answer)
            assert not grade(
                exercise,
                next(choice.id for choice in exercise.choices if choice.id != exercise.answer),
            )
    # Multiple characters in a compound reuse one lexical entry and drill.
    by_surface = {entry.surface: entry for entry in kanji}
    assert by_surface["会"].vocabulary_ids == by_surface["社"].vocabulary_ids
    assert by_surface["会"].practice_exercise_ids == by_surface["社"].practice_exercise_ids
    assert by_surface["家"].vocabulary_ids == ["ja-word-house"]
    assert by_surface["日"].id == "ja-kanji-65e5"


def test_new_kanji_authoring_manifest_matches_contexts_and_examples(reading_content):
    import json

    manifest = json.loads(
        (ROOT / "content/authoring/ja/kanji-contexts-draft.json").read_text(encoding="utf-8")
    )
    assert manifest["status"] == "draft"
    by_surface = {
        entry.surface: entry for entry in reading_content.characters if entry.form == "kanji"
    }
    words = {word.id: word for word in reading_content.vocabulary}
    assert len(manifest["entries"]) == 282
    assert len(manifest["existing_stage_a_ids"]) == 18
    for row in manifest["entries"]:
        entry = by_surface[row["character"]]
        assert entry.stage == row["stage"]
        assert row["character"] in row["word"] and row["word"] in row["example"]
        assert row["word"] + "（" + row["reading"] + "）" in entry.contextual_readings
        word = words[entry.vocabulary_ids[0]]
        assert word.reading == row["reading"]
        if word.status == "draft":
            assert "".join(segment.surface for segment in word.example) == row["example"]
            assert any(segment.vocabulary_id == word.id for segment in word.example)
    generated = [
        exercise
        for exercise in reading_content.practice_exercises
        if exercise.id.startswith("ja-context-")
    ]
    assert len(generated) == 263
    assert {exercise.answer for exercise in generated} == {"c0", "c1", "c2"}


def test_new_context_checks_require_draft_preview_even_for_canonical_word_reuse(reading_content):
    from app.reading import available_exercise_ids

    generated = {
        exercise.id
        for exercise in reading_content.practice_exercises
        if exercise.id.startswith("ja-context-")
    }
    assert not generated & available_exercise_ids(reading_content)
    assert generated <= available_exercise_ids(reading_content, include_drafts=True)
    house = next(word for word in reading_content.vocabulary if word.id == "ja-word-house")
    assert house.status == "published"
    assert not generated & set(house.practice_exercise_ids)
