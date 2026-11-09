"""Draft topic coverage is usable without promoting it to reviewed publication."""

from uuid import uuid4

import pytest
from test_learning import act, complete, start
from test_learning import course as course
from test_writing import create as create_writing_draft
from test_writing import save as save_writing_draft
from test_writing import save_body as writing_save_body

from app.config import ROOT
from app.db import sessions
from app.grading import grade
from app.services import import_content, load_content


def test_ten_topics_have_scaffolded_draft_guides_and_valid_checks(client, course):
    notes = client.get("/api/v1/courses/ja-starter/grammar?include_drafts=true").json()["notes"]
    assert {unit for note in notes for unit in note["unit_ids"]} == {
        unit.id for unit in course.units
    }
    assert len(notes) == 16
    assert all(note["status"] == "draft" for note in notes)
    assert all(note["explanation"] and note["examples"] and note["register_note"] for note in notes)
    assert client.get("/api/v1/courses/ja-starter/grammar").json()["notes"] == []
    for note in [note for note in notes if note["id"].startswith("ja-guide-unit-")]:
        saved = start(client, note["id"], source_kind="grammar", preview_draft=True)
        assert saved["preview_draft"] and saved["exercises"]
        for exercise in saved["exercises"]:
            assert (
                not {"answer", "answers", "response_feedback", "hint", "explanation"}
                & exercise.keys()
            )
    invitation = (
        next(unit for unit in course.units if unit.id == "ja-unit-10").lessons[0].exercises[0]
    )
    assert not grade(
        invitation, "option-1"
    )  # Understandable acceptance is outside this refusal task.
    assert "valid acceptance" in invitation.response_feedback["option-1"]
    assert (
        len(
            [
                lesson
                for unit in course.units
                for lesson in unit.lessons
                if lesson.status == "published"
            ]
        )
        == 6
    )


@pytest.mark.parametrize("previous_version", ["0.1.14", "0.1.16", "0.1.20"])
def test_content_upgrade_preserves_real_saved_work_and_receipts(client, previous_version):
    previous = load_content(ROOT / f"docs/reviews/ja-starter-{previous_version}/source.json")
    current = load_content(ROOT / "content/courses/ja/starter.json")
    with sessions(client.app.state.engine)() as db:
        assert import_content(db, previous)
    finished = complete(client)
    active = start(client, "ja-hiragana-sounds")
    active = act(client, active, "reveal", active["exercises"][0]["id"])
    card = client.post(
        "/api/v1/courses/ja-starter/review/cards",
        json={"item_id": "ja-word-school", "direction": "reading"},
    ).json()
    rating = {"request_id": str(uuid4()), "expected_revision": 0, "rating": "Hard"}
    route = f"/api/v1/review/cards/{card['id']}/ratings"
    rated = client.post(route, json=rating).json()
    before_progress = client.get("/api/v1/progress").json()
    history = client.get(f"/api/v1/review/cards/{card['id']}/history").json()
    with sessions(client.app.state.engine)() as db:
        assert import_content(db, current)
        assert not import_content(db, current)
    assert client.get(f"/api/v1/sessions/{finished['id']}").json() == finished
    assert client.get(f"/api/v1/sessions/{active['id']}").json() == active
    assert client.get("/api/v1/progress").json() == before_progress
    assert client.get(f"/api/v1/review/cards/{card['id']}").json() == rated
    assert client.post(route, json=rating).json() == rated
    assert client.get(f"/api/v1/review/cards/{card['id']}/history").json() == history


def test_020_upgrade_preserves_collection_snapshots_and_writing_revisions(client):
    previous = load_content(ROOT / "docs/reviews/ja-starter-0.1.20/source.json")
    current = load_content(ROOT / "content/courses/ja/starter.json")
    with sessions(client.app.state.engine)() as db:
        assert import_content(db, previous)

    collection_base = "/api/v1/courses/ja-starter/collections"
    collection_body = {"request_id": str(uuid4()), "name": "Words kept before expansion"}
    response = client.post(collection_base, json=collection_body)
    assert response.status_code == 200, response.text
    collection = response.json()
    collection_route = f"/api/v1/collections/{collection['id']}"
    for item_id in ("ja-word-hello", "ja-word-school"):
        response = client.patch(
            collection_route + "/members", json={"item_id": item_id, "saved": True}
        )
        assert response.status_code == 200, response.text
    before_members = client.get(collection_route + "/members").json()
    before_collections = client.get(collection_base).json()
    before_recall = client.post(collection_route + "/recall", json={"direction": "meaning"}).json()
    assert len(before_members["items"]) == before_recall["total"] == 2
    assert all(
        card["content_version"] == previous.version and not card["scheduled"]
        for card in before_recall["cards"]
    )

    draft = create_writing_draft(client)
    draft_route = f"/api/v1/writing/drafts/{draft['id']}"
    revision_body = writing_save_body(
        draft,
        "私は学生です。",
        checklist=[draft["task"]["checklist"][0]],
        model_revealed=True,
    )
    response = client.post(draft_route + "/revisions", json=revision_body)
    assert response.status_code == 200, response.text
    first_revision = response.json()
    saved_draft = save_writing_draft(
        client, first_revision, "私は学生です。日本語を勉強しています。", model_revealed=False
    )
    before_history = client.get(draft_route + "/history").json()
    assert saved_draft["content_version"] == previous.version
    assert saved_draft["current"]["model_revealed"]
    assert [revision["text"] for revision in before_history["revisions"]] == [
        "私は学生です。日本語を勉強しています。",
        "私は学生です。",
        "",
    ]
    before_progress = client.get("/api/v1/progress").json()
    assert before_progress["total_xp"] == 0

    with sessions(client.app.state.engine)() as db:
        assert import_content(db, current)
        assert not import_content(db, current)

    assert client.get(collection_base).json() == before_collections
    assert client.get(collection_route + "/members").json() == before_members
    assert (
        client.post(collection_route + "/recall", json={"direction": "meaning"}).json()
        == before_recall
    )
    assert client.get(draft_route).json() == saved_draft
    assert client.get(draft_route + "/history").json() == before_history
    # A retried old autosave returns its original receipt without replacing newer work.
    assert client.post(draft_route + "/revisions", json=revision_body).json() == first_revision
    assert client.get(draft_route).json() == saved_draft
    assert client.get("/api/v1/progress").json() == before_progress

    continued = save_writing_draft(
        client,
        saved_draft,
        "私は学生です。日本語を勉強しています。明日も日本語を勉強します。",
        model_revealed=False,
    )
    assert continued["content_version"] == previous.version
    assert continued["task"] == draft["task"]
    assert continued["current"]["number"] == saved_draft["current"]["number"] + 1
    assert continued["current"]["model_revealed"]
    after_history = client.get(draft_route + "/history").json()
    assert after_history["revisions"][1:] == before_history["revisions"]
    assert create_writing_draft(client)["content_version"] == current.version
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
