import json

import pytest

from app.config import ROOT
from app.content_audit import LexicalIdentities, inventory, lexical_mapping, write_review_packet
from app.services import load_content

SOURCE = ROOT / "content/courses/ja/starter.json"
IDENTITIES = SOURCE.with_name("lexical-identities.json")


def test_semantic_inventory_counts_spellings_once_and_homophones_separately():
    report = inventory(SOURCE, IDENTITIES)
    baseline_source = ROOT / "docs/reviews/ja-starter-0.1.20/source.json"
    baseline = inventory(baseline_source, baseline_source.with_name("lexical-identities.json"))
    original_ids = {word.id for word in load_content(baseline_source).vocabulary}
    current = load_content(SOURCE)
    new_words = [word for word in current.vocabulary if word.id not in original_ids]
    assert all(word.entry_kind == "word" and word.status == "draft" for word in new_words)
    assert report["counts"]["word"]["authored"] == baseline["counts"]["word"]["authored"] + len(
        new_words
    )
    assert report["canonical_word_count"] == baseline["canonical_word_count"] + len(new_words)
    assert report["counts"]["phrase"]["authored"] == 15
    assert report["counts"]["basic_kana"]["authored"] == 92
    assert report["counts"]["kanji"]["authored"] == 300
    words = {row["id"]: row for row in report["records"] if row["kind"] == "word"}
    assert (
        words["ja-word-school"]["canonical_lexical_id"]
        == words["ja-word-school-kanji"]["canonical_lexical_id"]
    )
    assert (
        words["ja-word-kanji-82b1"]["canonical_lexical_id"]
        != words["ja-word-kanji-9f3b"]["canonical_lexical_id"]
    )
    assert report["units_without_lessons"] == []
    old_lessons = {
        lesson.id for unit in load_content(baseline_source).units for lesson in unit.lessons
    }
    new_lessons = [
        lesson for unit in current.units for lesson in unit.lessons if lesson.id not in old_lessons
    ]
    assert all(lesson.status == "draft" for lesson in new_lessons)
    assert report["counts"]["lesson"]["status"] == {"published": 6, "draft": 120 + len(new_lessons)}
    assert len(report["guide_unit_ids"]) == 10
    assert len(report["reading_collisions"]) == 20
    assert all(item["decision_recorded"] for item in report["reading_collisions"])
    assert all(row["qualified_review"] == "pending" for row in report["records"])
    assert all(count["independently_reviewed"] == 0 for count in report["counts"].values())


def test_stale_and_overlapping_identity_decisions_rejected(tmp_path):
    data = json.loads(IDENTITIES.read_text(encoding="utf-8"))
    data["source_version"] = "0.0.0"
    stale = tmp_path / "identities.json"
    stale.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError, match="exact source"):
        inventory(SOURCE, stale)
    data["groups"].append(data["groups"][0])
    with pytest.raises(ValueError, match="distinct existing"):
        lexical_mapping(load_content(SOURCE), LexicalIdentities.model_validate(data))


def test_review_packet_contains_exact_source_assets_and_pending_decisions(tmp_path):
    result = write_review_packet(SOURCE, IDENTITIES, tmp_path)
    assert (tmp_path / "source.json").read_bytes() == SOURCE.read_bytes()
    assert load_content(tmp_path / "source.json").version == result["source_version"]
    queue = json.loads((tmp_path / "review-queue.json").read_text(encoding="utf-8"))
    assert len(queue["decisions"]) == result["review_items"]
    assert all(
        row["reviewer"] is None and row["decision"] == "pending" for row in queue["decisions"]
    )
    assert write_review_packet(SOURCE, IDENTITIES, tmp_path) == result
    # A human's work must survive an attempted regeneration, without partial writes.
    queue["decisions"][0]["notes"] = "Reviewer correction to preserve"
    amended = json.dumps(queue)
    (tmp_path / "review-queue.json").write_text(amended, encoding="utf-8")
    before = {path: path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}
    with pytest.raises(ValueError, match="Preserve"):
        write_review_packet(SOURCE, IDENTITIES, tmp_path)
    assert all(path.read_bytes() == data for path, data in before.items())
