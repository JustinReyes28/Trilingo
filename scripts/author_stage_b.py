"""Apply source-bound, additive draft vocabulary batches without opening a database.

Existing content is preserved. Candidate spellings/readings that need a lexical
decision are reported and omitted, never merged into a learner's saved records.
"""

import argparse
import copy
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))

# The standalone authoring CLI deliberately imports the established backend
# contracts rather than carrying a competing schema implementation.
from app.content_schema import ID, CourseContent, MultipleChoice  # noqa: E402
from app.grading import grade  # noqa: E402
from app.schemas import StrictModel  # noqa: E402

GUIDES = {
    "ja-unit-6": "ja-guide-unit-6-order-request",
    "ja-unit-7": "ja-guide-unit-7-ask-directions",
    "ja-unit-8": "ja-guide-unit-8-polite-routine",
    "ja-unit-9": "ja-guide-unit-9-descriptions-likes",
    "ja-unit-10": "ja-guide-unit-10-invite-message",
}
DISTRACTORS = [
    "a railway platform",
    "a postage stamp",
    "to swim",
    "a toothbrush",
    "heavy luggage",
    "every week",
    "a mountain path",
    "a saucepan",
    "to sing",
    "a newspaper",
    "a wooden shelf",
    "a rainy afternoon",
]


class AuthorRow(StrictModel):
    surface: str = Field(min_length=1, max_length=80)
    reading: str = Field(min_length=1, max_length=100)
    gloss: str = Field(min_length=1, max_length=300)
    part_of_speech: str = Field(min_length=1, max_length=80)
    example: str = Field(min_length=1, max_length=1000)
    translation: str = Field(min_length=1, max_length=1500)

    @field_validator("surface", "reading", "gloss", "part_of_speech", "example", "translation")
    @classmethod
    def visible_text(cls, value: str) -> str:
        if value != value.strip() or not value.strip():
            raise ValueError("Authoring fields require visible text without outer whitespace")
        if "\ufffd" in value or re.fullmatch(r"[?\s]+", value):
            raise ValueError(
                "Preserve Unicode authoring text; replacement characters are not content"
            )
        return value

    @field_validator("example")
    @classmethod
    def japanese_context(cls, value: str) -> str:
        if not re.search(r"[\u3041-\u30fa\u4e00-\u9fff]", value):
            raise ValueError("An original Japanese example is required; check file encoding")
        return value

    @field_validator("reading")
    @classmethod
    def kana_reading(cls, value: str) -> str:
        if not re.fullmatch(r"[\u3041-\u3096\u30a1-\u30fa\u30fc]+", value):
            raise ValueError(
                "Readings must use kana, not kanji, Latin text or pronunciation guesses"
            )
        return value

    @field_validator("part_of_speech")
    @classmethod
    def lexical_word(cls, value: str) -> str:
        if "phrase" in value.casefold() or "expression" in value.casefold():
            raise ValueError(
                "This batch counts lexical words; fixed expressions need a separate inventory"
            )
        return value


class AuthorGroup(StrictModel):
    unit_id: ID
    title: str = Field(min_length=1, max_length=200)
    concepts: list[ID] = Field(min_length=1)
    rows: list[AuthorRow] = Field(min_length=1, max_length=20)


class AuthorFile(StrictModel):
    status: Literal["draft"]
    license: Literal["CC-BY-4.0"]
    review_status: str = Field(min_length=1)
    groups: list[AuthorGroup] = Field(min_length=1)


class ContrastGroup(StrictModel):
    guide_id: ID
    exercises: list[MultipleChoice] = Field(min_length=1)


class ContrastFile(StrictModel):
    status: Literal["draft"]
    review_status: str = Field(min_length=1)
    groups: list[ContrastGroup] = Field(min_length=1)


class BatchManifest(StrictModel):
    course_id: ID
    base_version: str
    base_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    target_version: str
    batch_id: ID
    status: Literal["draft"]
    authoring_files: list[str] = Field(min_length=1)
    collision_policy: Literal["omit_same_surface_or_reading"]
    contrast_file: str | None = None


def lexical_text(value: str) -> str:
    """Normalize spelling width and kana script only for conservative selection."""
    normalized = unicodedata.normalize("NFKC", value).strip()
    return "".join(
        chr(ord(char) - 0x60) if "\u30a1" <= char <= "\u30f6" else char for char in normalized
    )


def version_parts(value: str) -> tuple[int, ...]:
    """Compare the validated semantic release components used by authored content."""
    if not re.fullmatch(r"\d+\.\d+\.\d+", value):
        raise ValueError("Use a three-component numeric content version")
    return tuple(int(piece) for piece in value.split("."))


def family_forms(value: str) -> set[str]:
    """Conservatively avoid treating a suru form as another copy of its noun."""
    normalized = lexical_text(value)
    return (
        {normalized, normalized[:-2]}
        if normalized.endswith("する") and len(normalized) > 2
        else {normalized}
    )


def apply_groups(
    source: dict,
    manifest: BatchManifest,
    files: list[AuthorFile],
    contrasts: ContrastFile | None = None,
) -> tuple[dict, dict]:
    """Append only new draft entities, retaining every original definition and ID."""
    if (source["id"], source["version"]) != (manifest.course_id, manifest.base_version):
        raise ValueError("Use the manifest's exact base course/version")
    if version_parts(manifest.target_version) <= version_parts(manifest.base_version):
        raise ValueError("A changed batch needs a newer immutable content version")
    result = copy.deepcopy(source)
    surfaces = {form for word in source["vocabulary"] for form in family_forms(word["surface"])}
    readings = {form for word in source["vocabulary"] for form in family_forms(word["reading"])}
    known_ids = {word["id"] for word in source["vocabulary"]}
    units = {unit["id"]: unit for unit in result["units"]}
    guides = {guide["id"]: guide for guide in result["grammar_notes"]}
    accepted, omitted, lesson_ids, exercise_ids = [], [], [], []
    for group_index, group in enumerate(group for file in files for group in file.groups):
        unit = units.get(group.unit_id)
        if unit is None or unit["stage"] != "stage-b" or group.unit_id not in GUIDES:
            raise ValueError(f"{group.unit_id}: only existing Stage B units may receive this batch")
        guide = guides[GUIDES[group.unit_id]]
        lesson_id = f"{group.unit_id}-{manifest.batch_id}-{group_index + 1:03}"
        exercises = []
        for row in group.rows:
            spelling, reading_key = lexical_text(row.surface), lexical_text(row.reading)
            spelling_forms, reading_forms = family_forms(row.surface), family_forms(row.reading)
            reason = (
                "existing/candidate spelling or suru family"
                if spelling_forms & surfaces
                else (
                    "same reading/family requires an explicit semantic decision"
                    if reading_forms & readings
                    else None
                )
            )
            if reason:
                omitted.append({"unit_id": group.unit_id, **row.model_dump(), "reason": reason})
                continue
            surfaces.update(spelling_forms)
            readings.update(reading_forms)
            identity = hashlib.sha256((spelling + "\0" + reading_key).encode()).hexdigest()[:20]
            word_id = "ja-word-b-" + identity
            if word_id in known_ids:
                raise ValueError("Unexpected lexical ID collision; preserve the existing entity")
            known_ids.add(word_id)
            prefix = f"{lesson_id}-v{len(exercises) + 1}"
            explanation = (
                f"{row.surface}（{row.reading}）: {row.gloss}. {row.example} — {row.translation}"
            )
            base = {
                "objective": f"Understand {row.surface} in an everyday context.",
                "concepts": group.concepts,
                "difficulty": 2,
                "explanation": explanation,
                "hint": f"The reading is {row.reading}. Reveal is always available.",
                "preparation": [],
            }
            gloss_tokens = set(re.findall(r"[a-z]{4,}", row.gloss.lower()))
            candidates = [
                item
                for item in DISTRACTORS
                if not gloss_tokens & set(re.findall(r"[a-z]{4,}", item))
            ]
            if len(candidates) < 2:
                raise ValueError(f"{word_id}: author explicit unrelated distractors")
            offset = (len(accepted) + group_index * 5) % len(candidates)
            wrong = [
                candidates[offset],
                candidates[(offset + len(candidates) // 2) % len(candidates)],
            ]
            position = len(accepted) % 3
            labels = wrong[:]
            labels.insert(position, row.gloss)
            meaning = {
                **base,
                "id": prefix + "-meaning",
                "type": "multiple_choice",
                "skill": "meaning",
                "prompt": f"{row.example}\nIn this example, what does 「{row.surface}」 mean?",
                "policy": {"strategy": "choice"},
                "choices": [{"id": f"c{i + 1}", "text": label} for i, label in enumerate(labels)],
                "answer": f"c{position + 1}",
                "response_feedback": {
                    f"c{i + 1}": explanation
                    if i == position
                    else f"That sense does not match 「{row.surface}」 here. {explanation}"
                    for i in range(3)
                },
            }
            exercises.append(meaning)
            linked = [meaning["id"]]
            if any("\u4e00" <= char <= "\u9fff" for char in row.surface):
                kana = lexical_text(row.reading)
                # Loanword compounds can retain the Japanese long-vowel mark.
                # Exact authored keys still govern grading; do not change the
                # engine's stricter hiragana-only policy for unrelated content.
                has_long_mark = "ー" in kana
                reading = {
                    **base,
                    "id": prefix + "-reading",
                    "objective": f"Type the kana reading of {row.surface}.",
                    "type": "translation",
                    "skill": "typing",
                    "prompt": (
                        f"Write the kana reading of 「{row.surface}」 using hiragana"
                        + (" and the long-vowel mark ー" if has_long_mark else "")
                        + f". Meaning here: {row.gloss}."
                    ),
                    "policy": {
                        "strategy": "exact",
                        "script": "japanese" if has_long_mark else "hiragana",
                        "normalization": "NFC",
                        "spacing": "ignore",
                        "required_distinctions": ["voicing", "kana_size", "vowel_length"],
                    },
                    "answers": [kana],
                }
                exercises.append(reading)
                linked.append(reading["id"])
            result["vocabulary"].append(
                {
                    "id": word_id,
                    "surface": row.surface,
                    "reading": row.reading,
                    "gloss": row.gloss,
                    "part_of_speech": row.part_of_speech,
                    "entry_kind": "word",
                    "register": "context-dependent; see example",
                    "example": [{"surface": row.example}],
                    "concepts": group.concepts,
                    "stage": "stage-b",
                    "status": "draft",
                    "audio": None,
                    "practice_exercise_ids": linked,
                }
            )
            accepted.append({"word_id": word_id, "unit_id": group.unit_id, **row.model_dump()})
        if exercises:
            unit["lessons"].append(
                {
                    "id": lesson_id,
                    "title": group.title,
                    "japanese_title": group.rows[0].surface,
                    "objective": f"Recognize the contextual word senses in {group.title.lower()}.",
                    "order": len(unit["lessons"]) + 1,
                    "status": "draft",
                    "preparation": [],
                    "exercises": exercises,
                }
            )
            linked_ids = [exercise["id"] for exercise in exercises]
            guide["practice_exercise_ids"].extend(linked_ids)
            lesson_ids.append(lesson_id)
            exercise_ids.extend(linked_ids)
    contrast_ids = []
    if contrasts is not None:
        for group in contrasts.groups:
            guide = guides.get(group.guide_id)
            if guide is None or guide["status"] != "draft":
                raise ValueError("Contrast practice requires an existing explicitly draft guide")
            for exercise in group.exercises:
                if not set(exercise.concepts) <= set(guide["concepts"]):
                    raise ValueError("Contrast concepts must match the selected guide")
                result["practice_exercises"].append(exercise.model_dump())
                guide["practice_exercise_ids"].append(exercise.id)
                contrast_ids.append(exercise.id)
    result["version"] = manifest.target_version
    result["review_note"] += (
        " Additional Stage B contextual vocabulary remains draft; qualified semantic/language "
        "review and publication remain pending."
    )
    validated = CourseContent.model_validate(result)
    for unit in validated.units:
        for lesson in unit.lessons:
            if lesson.id not in lesson_ids:
                continue
            for exercise in lesson.exercises:
                keys = [exercise.answer] if exercise.type == "multiple_choice" else exercise.answers
                if not all(grade(exercise, key) for key in keys):
                    raise ValueError(f"{exercise.id}: authored key is rejected by its policy")
    for exercise in validated.practice_exercises:
        if exercise.id in contrast_ids and not grade(exercise, exercise.answer):
            raise ValueError(f"{exercise.id}: contrast key is rejected")
    return result, {
        "base_version": manifest.base_version,
        "target_version": manifest.target_version,
        "status": "draft; not independently reviewed or published",
        "collision_policy": manifest.collision_policy,
        "accepted": accepted,
        "omitted": omitted,
        "lesson_ids": lesson_ids,
        "exercise_ids": exercise_ids,
        "contrast_exercise_ids": contrast_ids,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--identities", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    manifest = BatchManifest.model_validate_json(args.manifest.read_text(encoding="utf-8"))
    source_bytes = args.source.read_bytes()
    if hashlib.sha256(source_bytes).hexdigest() != manifest.base_sha256:
        raise ValueError("The base source does not match the exact manifest hash")
    files = []
    input_hashes = {}
    for filename in manifest.authoring_files:
        path = (ROOT / filename).resolve()
        if not path.is_relative_to((ROOT / "content/authoring").resolve()):
            raise ValueError("Authoring inputs must remain in content/authoring")
        input_hashes[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
        files.append(AuthorFile.model_validate_json(path.read_text(encoding="utf-8")))
    contrasts = None
    if manifest.contrast_file:
        contrast_path = (ROOT / manifest.contrast_file).resolve()
        if not contrast_path.is_relative_to((ROOT / "content/authoring").resolve()):
            raise ValueError("Contrast inputs must remain in content/authoring")
        input_hashes[manifest.contrast_file] = hashlib.sha256(
            contrast_path.read_bytes()
        ).hexdigest()
        contrasts = ContrastFile.model_validate_json(contrast_path.read_text(encoding="utf-8"))
    result, report = apply_groups(json.loads(source_bytes), manifest, files, contrasts)
    report["authoring_sha256"] = input_hashes
    encoded = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    identities = json.loads(args.identities.read_text(encoding="utf-8"))
    if identities["source_sha256"] not in {
        manifest.base_sha256,
        hashlib.sha256(encoded).hexdigest(),
    }:
        raise ValueError("Preserve unmatched lexical decisions; select the exact base identities")
    identities["source_version"] = manifest.target_version
    identities["source_sha256"] = hashlib.sha256(encoded).hexdigest()
    report["source_sha256"] = identities["source_sha256"]
    outputs = {
        args.output: encoded,
        args.identities: (json.dumps(identities, ensure_ascii=False, indent=2) + "\n").encode(
            "utf-8"
        ),
        args.report: (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    }
    if (
        args.output.exists()
        and args.output.read_bytes() != encoded
        and hashlib.sha256(args.output.read_bytes()).hexdigest() != manifest.base_sha256
    ):
        raise ValueError("Preserve a different current version; choose another output path")
    if args.report.exists() and args.report.read_bytes() != outputs[args.report]:
        raise ValueError("Preserve an existing batch report; choose a new report path")
    for path, data in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    contrast_count = len(report["contrast_exercise_ids"])
    print(
        json.dumps(
            {
                "version": result["version"],
                "new_words": len(report["accepted"]),
                "omitted_candidates": len(report["omitted"]),
                "new_lessons": len(report["lesson_ids"]),
                "new_checks": len(report["exercise_ids"]) + contrast_count,
                "particle_contrasts": contrast_count,
                "source_sha256": report["source_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
