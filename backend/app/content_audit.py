"""Reproducible source-bound inventories and qualified-review queues, without DB writes."""

import argparse
import hashlib
import json
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from pydantic import Field

from app.config import ROOT
from app.content_schema import ID, CourseContent
from app.schemas import StrictModel
from app.services import load_content


class IdentityGroup(StrictModel):
    canonical_id: ID
    member_ids: list[ID] = Field(min_length=2)
    reason: str = Field(min_length=1)


class DistinctGroup(StrictModel):
    member_ids: list[ID] = Field(min_length=2)
    reason: str = Field(min_length=1)


class LexicalIdentities(StrictModel):
    course_id: ID
    source_version: str
    source_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    review_status: str
    groups: list[IdentityGroup]
    distinct_homophones: list[DistinctGroup]
    policy: str


def lexical_mapping(content: CourseContent, identities: LexicalIdentities) -> dict[str, str]:
    words = {word.id: word for word in content.vocabulary if word.entry_kind == "word"}
    mapping = {key: key for key in words}
    used: set[str] = set()
    for group in identities.groups:
        members = set(group.member_ids)
        if (
            len(members) != len(group.member_ids)
            or not members <= words.keys()
            or group.canonical_id not in members
            or members & used
        ):
            raise ValueError(
                "Lexical groups require distinct existing word IDs and one member canonical ID"
            )
        used.update(members)
        for key in members:
            mapping[key] = group.canonical_id
    for group in identities.distinct_homophones:
        if not set(group.member_ids) <= words.keys():
            raise ValueError("Distinct lexical decisions must reference existing words")
        if len({mapping[key] for key in group.member_ids}) != len(group.member_ids):
            raise ValueError("Distinct homophones cannot share a canonical lexical identity")
    return mapping


def inventory(source: Path, identity_file: Path) -> dict:
    content = load_content(source)
    source_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    identities = LexicalIdentities.model_validate_json(identity_file.read_text(encoding="utf-8"))
    if (identities.course_id, identities.source_version, identities.source_sha256) != (
        content.id,
        content.version,
        source_digest,
    ):
        raise ValueError(
            "Lexical decisions do not match this exact source; audit the changed version"
        )
    canonical = lexical_mapping(content, identities)
    exercises = {
        exercise.id: exercise
        for unit in content.units
        for lesson in unit.lessons
        for exercise in lesson.exercises
    }
    exercises.update({exercise.id: exercise for exercise in content.practice_exercises})
    unit_concepts = {
        unit.id: {
            concept
            for lesson in unit.lessons
            for exercise in lesson.exercises
            for concept in exercise.concepts
        }
        for unit in content.units
    }
    lesson_units = {
        exercise.id: unit.id
        for unit in content.units
        for lesson in unit.lessons
        for exercise in lesson.exercises
    }
    records: list[dict] = []

    def record(kind: str, item: dict, stage: str | None = None, status: str | None = None) -> None:
        concepts = item.get("concepts", [])
        direct = item.get("unit_ids", [])
        practice_ids = list(
            dict.fromkeys(item.get("practice_exercise_ids", item.get("exercise_ids", [])))
        )
        if kind in {"story", "dialogue", "audio_episode", "reading_passage"}:
            practice_ids = list(
                dict.fromkeys(
                    [
                        *practice_ids,
                        *item.get("recap_exercise_ids", []),
                        *item.get("speaking_exercise_ids", []),
                        *(key for turn in item.get("turns", []) for key in turn["exercise_ids"]),
                    ]
                )
            )
        linked_units = sorted({lesson_units[key] for key in practice_ids if key in lesson_units})
        records.append(
            {
                "id": item["id"],
                "kind": kind,
                "stage": item.get("stage", stage),
                "status": item.get("status", status or "draft"),
                "status_origin": "explicit"
                if "status" in item
                else "inherited"
                if status
                else "unreviewed; no independent status field",
                "qualified_review": "pending",
                "concepts": concepts,
                "unit_ids": direct
                or linked_units
                or [key for key, values in unit_concepts.items() if set(concepts) & values],
                "unit_mapping": "explicit"
                if direct
                else "linked lesson exercises"
                if linked_units
                else "concept overlap only; authoring placement pending",
                "objectives": item.get(
                    "objectives", [item["objective"]] if "objective" in item else []
                ),
                "practice_exercise_ids": practice_ids,
                "practice_directions": sorted({exercises[key].skill for key in practice_ids}),
                **(
                    {"canonical_lexical_id": canonical[item["id"]]}
                    if item["id"] in canonical
                    else {}
                ),
            }
        )

    for unit in content.units:
        record("unit", unit.model_dump())
        for lesson in unit.lessons:
            record("lesson", {**lesson.model_dump(), "unit_ids": [unit.id]}, unit.stage)
            for exercise in lesson.exercises:
                record(
                    "exercise",
                    {
                        **exercise.model_dump(),
                        "unit_ids": [unit.id],
                        "practice_exercise_ids": [exercise.id],
                    },
                    unit.stage,
                    lesson.status,
                )
    for exercise in content.practice_exercises:
        record(
            "practice_exercise", {**exercise.model_dump(), "practice_exercise_ids": [exercise.id]}
        )
    for word in content.vocabulary:
        record(word.entry_kind, word.model_dump())
    for character in content.characters:
        kind = (
            "kanji"
            if character.script == "kanji"
            else "basic_kana"
            if character.form == "basic"
            else "kana_variant"
        )
        record(kind, character.model_dump())
    for kind, collection in [
        ("grammar_guide", content.grammar_notes),
        ("writing_task", content.writing_tasks),
        ("asset", content.assets),
        ("pattern", content.concepts),
    ]:
        for item in collection:
            record(kind, item.model_dump())
    for item in content.narratives:
        record(item.kind, item.model_dump())
    counts: dict[str, dict] = {}
    for kind in sorted({row["kind"] for row in records}):
        selected = [row for row in records if row["kind"] == kind]
        counts[kind] = {
            "authored": len(selected),
            "status": dict(Counter(row["status"] for row in selected)),
            "independently_reviewed": 0,
        }
    stage_order = {stage.id: index for index, stage in enumerate(content.stages)}
    introduced: dict[str, str] = {}
    for word in sorted(content.vocabulary, key=lambda word: stage_order[word.stage]):
        if word.entry_kind == "word":
            introduced.setdefault(canonical[word.id], word.stage)
    by_reading: dict[str, list[str]] = defaultdict(list)
    for word in content.vocabulary:
        if word.entry_kind == "word":
            by_reading[unicodedata.normalize("NFC", word.reading)].append(word.id)
    decisions = [set(group.member_ids) for group in identities.groups] + [
        set(group.member_ids) for group in identities.distinct_homophones
    ]
    collisions = [
        {
            "reading": reading,
            "ids": keys,
            "decision_recorded": any(set(keys) <= group for group in decisions),
        }
        for reading, keys in sorted(by_reading.items())
        if len(keys) > 1
    ]
    return {
        "schema_version": 1,
        "course": content.id,
        "source_version": content.version,
        "source_sha256": source_digest,
        "identity_sha256": hashlib.sha256(identity_file.read_bytes()).hexdigest(),
        "review_status": (
            "Qualified review pending for every record; publication is not independent review."
        ),
        "counts": counts,
        "canonical_word_count": len(set(canonical.values())),
        "canonical_words_by_introduction_stage": dict(Counter(introduced.values())),
        "targets": [
            {"stage": stage.id, "new_words": stage.word_target, "new_kanji": stage.kanji_target}
            for stage in content.stages
        ],
        "lexical_decisions": identities.model_dump(),
        "reading_collisions": collisions,
        "units_without_lessons": [unit.id for unit in content.units if not unit.lessons],
        "guide_unit_ids": sorted({key for note in content.grammar_notes for key in note.unit_ids}),
        "records": records,
    }


def write_review_packet(source: Path, identity_file: Path, output: Path) -> dict:
    report = inventory(source, identity_file)
    content = load_content(source)
    artifacts = {
        "inventory.json": report,
        "lexical-identities.json": json.loads(identity_file.read_text(encoding="utf-8")),
    }
    files: dict[Path, bytes] = {output / "source.json": source.read_bytes()}
    assets = []
    for asset in content.assets:
        path = source.parent / asset.path
        files[output / asset.path] = path.read_bytes()
        assets.append(
            {**asset.model_dump(), "actual_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        )
    queue = [
        {
            "id": row["id"],
            "kind": row["kind"],
            "decision": "pending",
            "reviewer": None,
            "qualifications": None,
            "reviewed_at": None,
            "corrections": [],
            "notes": "",
        }
        for row in report["records"]
    ]
    artifacts["review-queue.json"] = {
        "source_version": content.version,
        "source_sha256": report["source_sha256"],
        "assets": assets,
        "decisions": queue,
    }
    for filename, data in artifacts.items():
        destination = output / filename
        files[destination] = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    # Preflight the entire packet before writing; never clobber a reviewer correction.
    for destination, encoded in files.items():
        if destination.exists() and destination.read_bytes() != encoded:
            raise ValueError(
                f"Preserve the existing review artifact; choose a new output folder: {destination}"
            )
    for destination, encoded in files.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(encoded)
    return {
        "source_version": content.version,
        "source_sha256": report["source_sha256"],
        "canonical_words": report["canonical_word_count"],
        "review_items": len(queue),
        "output": str(output),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "content/courses/ja/starter.json")
    parser.add_argument(
        "--identities", type=Path, default=ROOT / "content/courses/ja/lexical-identities.json"
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            write_review_packet(args.source, args.identities, args.output),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
