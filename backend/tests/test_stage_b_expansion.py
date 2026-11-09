"""Additive authoring preserves snapshots and only introduces honest draft practice."""

import copy
import json

import pytest

from app.config import ROOT
from app.content_audit import inventory
from app.grading import grade
from app.reading import available_exercise_ids
from app.services import load_content

SOURCE = ROOT / "content/courses/ja/starter.json"
BASE = ROOT / "docs/reviews/ja-starter-0.1.20/source.json"
REPORT = ROOT / "content/authoring/ja/stage-b-expansion-20261025-result.json"


@pytest.fixture
def authoring(monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    import author_stage_b

    return author_stage_b


def test_expansion_retains_every_original_definition_and_keeps_new_content_draft():
    before = json.loads(BASE.read_text(encoding="utf-8"))
    after = json.loads(SOURCE.read_text(encoding="utf-8"))
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    assert before["version"] == report["base_version"] == "0.1.20"
    assert after["version"] == report["target_version"] == "0.1.21"
    for name in before.keys() - {
        "version",
        "review_note",
        "vocabulary",
        "units",
        "grammar_notes",
        "practice_exercises",
    }:
        assert after[name] == before[name], name
    assert (
        after["practice_exercises"][: len(before["practice_exercises"])]
        == before["practice_exercises"]
    )
    original_words = {word["id"]: word for word in before["vocabulary"]}
    current_words = {word["id"]: word for word in after["vocabulary"]}
    assert all(current_words[key] == word for key, word in original_words.items())
    new_ids = current_words.keys() - original_words.keys()
    assert new_ids == {row["word_id"] for row in report["accepted"]}
    assert len(new_ids) >= 934
    for row in report["accepted"]:
        word = current_words[row["word_id"]]
        assert word["status"] == "draft" and word["stage"] == "stage-b"
        assert word["entry_kind"] == "word"
        assert word["surface"] == row["surface"]
        assert word["reading"] == row["reading"]
        assert word["example"] == [{"surface": row["example"]}]
        assert row["translation"] and word["practice_exercise_ids"]
    for original, current in zip(before["units"], after["units"], strict=True):
        assert {k: v for k, v in current.items() if k != "lessons"} == {
            k: v for k, v in original.items() if k != "lessons"
        }
        assert current["lessons"][: len(original["lessons"])] == original["lessons"]
        assert all(
            lesson["status"] == "draft" for lesson in current["lessons"][len(original["lessons"]) :]
        )
    for original, current in zip(before["grammar_notes"], after["grammar_notes"], strict=True):
        assert {k: v for k, v in current.items() if k != "practice_exercise_ids"} == {
            k: v for k, v in original.items() if k != "practice_exercise_ids"
        }
        assert (
            current["practice_exercise_ids"][: len(original["practice_exercise_ids"])]
            == original["practice_exercise_ids"]
        )


def test_new_checks_have_valid_keys_and_are_available_only_with_explicit_draft_choice():
    content = load_content(SOURCE)
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    keys = set(report["exercise_ids"])
    added = [
        exercise
        for unit in content.units
        for lesson in unit.lessons
        for exercise in lesson.exercises
        if exercise.id in keys
    ]
    assert len(added) == len(keys) and keys
    assert not keys & available_exercise_ids(content)
    assert keys <= available_exercise_ids(content, include_drafts=True)
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
    inventory_report = inventory(SOURCE, SOURCE.with_name("lexical-identities.json"))
    assert inventory_report["canonical_words_by_introduction_stage"]["stage-a"] >= 500
    assert inventory_report["canonical_words_by_introduction_stage"]["stage-b"] >= 1500
    assert inventory_report["counts"]["word"]["status"]["published"] == 8
    assert inventory_report["counts"]["phrase"]["authored"] == 15
    records = {row["id"]: row for row in inventory_report["records"]}
    for row in report["accepted"]:
        assert row["unit_id"] in records[row["word_id"]]["unit_ids"]
        assert records[row["word_id"]]["unit_mapping"] == "linked lesson exercises"


def test_particle_contrasts_explain_each_response_and_stay_behind_draft_choice():
    content = load_content(SOURCE)
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    keys = set(report["contrast_exercise_ids"])
    assert len(keys) == 24
    exercises = {
        exercise.id: exercise for exercise in content.practice_exercises if exercise.id in keys
    }
    assert set(exercises) == keys
    assert not keys & available_exercise_ids(content)
    assert keys <= available_exercise_ids(content, include_drafts=True)
    for exercise in exercises.values():
        assert exercise.type == "multiple_choice"
        assert grade(exercise, exercise.answer)
        assert set(exercise.response_feedback) == {choice.id for choice in exercise.choices}
        assert len(set(exercise.response_feedback.values())) == len(exercise.choices)
        for choice in exercise.choices:
            assert grade(exercise, choice.id) == (choice.id == exercise.answer)


def test_authoring_rejects_stale_stage_and_version_inputs_and_reports_collisions(authoring):
    base = json.loads(BASE.read_text(encoding="utf-8"))
    manifest = authoring.BatchManifest.model_validate_json(
        (ROOT / "content/authoring/ja/stage-b-expansion-20261025.json").read_text(encoding="utf-8")
    )
    file = authoring.AuthorFile.model_validate(
        {
            "status": "draft",
            "license": "CC-BY-4.0",
            "review_status": "qualified review pending",
            "groups": [
                {
                    "unit_id": "ja-unit-8",
                    "title": "Duplicate safety",
                    "concepts": ["polite-verbs"],
                    "rows": [
                        {
                            "surface": base["vocabulary"][0]["surface"],
                            "reading": base["vocabulary"][0]["reading"],
                            "gloss": "existing word",
                            "part_of_speech": "noun",
                            "example": "こんにちは。",
                            "translation": "Existing context.",
                        }
                    ],
                }
            ],
        }
    )
    untouched = copy.deepcopy(base)
    result, report = authoring.apply_groups(base, manifest, [file])
    assert base == untouched
    assert not report["accepted"] and len(report["omitted"]) == 1
    assert result["vocabulary"] == base["vocabulary"]
    stale = manifest.model_copy(update={"base_version": "0.0.0"})
    with pytest.raises(ValueError, match="exact base"):
        authoring.apply_groups(base, stale, [file])
    backwards = manifest.model_copy(update={"target_version": "0.1.19"})
    with pytest.raises(ValueError, match="newer immutable"):
        authoring.apply_groups(base, backwards, [file])
    file.groups[0].unit_id = "ja-unit-1"
    with pytest.raises(ValueError, match="only existing Stage B"):
        authoring.apply_groups(base, manifest, [file])


@pytest.mark.parametrize("reading", ["学校", "gakkou", "がっこう ", ""])
def test_authoring_does_not_accept_non_kana_or_empty_readings(authoring, reading):
    with pytest.raises(ValueError):
        authoring.AuthorRow(
            surface="学校",
            reading=reading,
            gloss="school",
            part_of_speech="noun",
            example="学校へ行きます。",
            translation="I go to school.",
        )


def test_corrupt_unicode_and_stale_hash_cannot_produce_a_new_source(
    authoring, tmp_path, monkeypatch
):
    with pytest.raises(ValueError, match="Unicode"):
        authoring.AuthorRow(
            surface="????",
            reading="がっこう",
            gloss="school",
            part_of_speech="noun",
            example="学校へ行きます。",
            translation="I go to school.",
        )
    with pytest.raises(ValueError, match="Japanese example"):
        authoring.AuthorRow(
            surface="学校",
            reading="がっこう",
            gloss="school",
            part_of_speech="noun",
            example="Only an English sentence.",
            translation="I go to school.",
        )
    stale = tmp_path / "stale.json"
    stale.write_text(BASE.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    output, identities, report = [
        tmp_path / name for name in ("source.json", "identities.json", "report.json")
    ]
    original_identities = SOURCE.with_name("lexical-identities.json").read_bytes()
    identities.write_bytes(original_identities)
    monkeypatch.setattr(
        "sys.argv",
        [
            "author_stage_b",
            "--manifest",
            str(ROOT / "content/authoring/ja/stage-b-expansion-20261025.json"),
            "--source",
            str(stale),
            "--output",
            str(output),
            "--identities",
            str(identities),
            "--report",
            str(report),
        ],
    )
    with pytest.raises(ValueError, match="exact manifest hash"):
        authoring.main()
    assert not output.exists() and not report.exists()
    assert identities.read_bytes() == original_identities
