from copy import deepcopy
from uuid import uuid4

import pytest
from test_learning import course as course

from app.db import sessions
from app.services import import_content

pytestmark = pytest.mark.usefixtures("course")
BASE = "/api/v1/courses/ja-starter/collections"


def test_collection_idempotency_membership_snapshot_and_no_rewards(client, course):
    body = {"request_id": str(uuid4()), "name": "My first phrases"}
    created = client.post(BASE, json=body)
    assert created.status_code == 200, created.text
    collection = created.json()
    assert client.post(BASE, json=body).json() == collection
    assert client.post(BASE, json={**body, "name": "Other intent"}).status_code == 409
    url = "/api/v1/collections/" + collection["id"] + "/members"
    member = {"item_id": "ja-word-hello", "saved": True}
    assert client.patch(url, json=member).json()["item_count"] == 1
    assert client.patch(url, json=member).json()["item_count"] == 1
    assert client.get(BASE).json()[0]["item_count"] == 1
    first = client.get(url).json()["items"][0]
    updated = deepcopy(course)
    updated.version = "99.0.0"
    next(word for word in updated.vocabulary if word.id == "ja-word-hello").gloss = "Changed later"
    with sessions(client.app.state.engine)() as db:
        import_content(db, updated)
    assert client.get(url).json()["items"][0] == first
    assert client.patch(url, json={**member, "saved": False}).json()["item_count"] == 0
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert client.post(BASE, json={"request_id": str(uuid4()), "name": "   "}).status_code == 422


def test_collection_recall_uses_saved_snapshot_and_preserves_existing_schedule(client, course):
    collection = client.post(
        BASE, json={"request_id": str(uuid4()), "name": "Saved meanings"}
    ).json()
    route = f"/api/v1/collections/{collection['id']}"
    for word in ("ja-word-hello", "ja-word-school", "ja-word-house"):
        assert (
            client.patch(route + "/members", json={"item_id": word, "saved": True}).status_code
            == 200
        )
    # Nothing has been scheduled or rewarded by bookmarking/preparing cards.
    first = client.post(route + "/recall?limit=1", json={"direction": "meaning"}).json()
    assert first["total"] == 3 and first["has_more"] and len(first["cards"]) == 1
    card = first["cards"][0]
    assert not card["scheduled"] and card["content_version"] == course.version
    rating = {"request_id": str(uuid4()), "expected_revision": 0, "rating": "Good"}
    saved = client.post(f"/api/v1/review/cards/{card['id']}/ratings", json=rating).json()
    updated = deepcopy(course)
    updated.version = "99.1.0"
    for word in updated.vocabulary:
        if word.id in {"ja-word-hello", "ja-word-school", "ja-word-house"}:
            word.gloss = "Changed after bookmark"
            word.status = "draft"
    with sessions(client.app.state.engine)() as db:
        import_content(db, updated)
    prepared = client.post(route + "/recall?limit=10", json={"direction": "meaning"}).json()
    assert len(prepared["cards"]) == 3 and not prepared["has_more"]
    assert next(item for item in prepared["cards"] if item["id"] == saved["id"]) == saved
    assert all(item["content_version"] == course.version for item in prepared["cards"])
    assert all(item["answer"] != "Changed after bookmark" for item in prepared["cards"])
    typed = client.post(route + "/recall", json={"direction": "typing"}).json()
    assert len(typed["cards"]) == 3 and all(not item["scheduled"] for item in typed["cards"])
    assert all(item["prompt"] != "Changed after bookmark" for item in typed["cards"])
    assert client.get("/api/v1/progress").json()["total_xp"] == 5
    assert client.post(route + "/recall", json={"item_id": "not-a-member"}).status_code == 404
    spoken = client.post(route + "/recall", json={"direction": "speaking"})
    assert spoken.status_code == 200
    assert all(
        item["direction"] == "speaking"
        and item["audio_cues"] == [{"id": "reference", "label": "saved word reference"}]
        and "supports_recording" not in item
        and not item["scheduled"]
        for item in spoken.json()["cards"]
    )
    assert client.post(route + "/recall", json={"direction": "recognition"}).status_code == 422


def test_collection_recall_batches_and_listing_have_bounded_queries(client, course):
    from sqlalchemy import event

    collections = []
    for index in range(45):
        collection = client.post(
            BASE, json={"request_id": str(uuid4()), "name": f"QA set {index}"}
        ).json()
        collections.append(collection)
    route = f"/api/v1/collections/{collections[-1]['id']}"
    words = [word.id for word in course.vocabulary if word.status == "published"]
    for word_id in words:
        client.patch(route + "/members", json={"item_id": word_id, "saved": True})
    queries = []

    def track(_connection, _cursor, statement, _parameters, _context, _many):
        queries.append(statement)

    event.listen(client.app.state.engine, "before_cursor_execute", track)
    try:
        result = client.post(route + "/recall?limit=100", json={"direction": "reading"})
    finally:
        event.remove(client.app.state.engine, "before_cursor_execute", track)
    assert result.status_code == 200, result.text
    assert len(result.json()["cards"]) == len(words)
    assert len(queries) <= 12, "Prepare a batch without querying each word or snapshot separately"
    repeated = client.post(route + "/recall?limit=100", json={"direction": "reading"}).json()
    assert repeated == result.json()
    first = client.post(route + "/recall?limit=2", json={"direction": "reading"}).json()
    tail = client.post(
        route + f"/recall?offset=2&limit={len(words)}", json={"direction": "reading"}
    ).json()
    assert len({row["id"] for row in first["cards"] + tail["cards"]}) == len(words)
    assert not tail["has_more"]
    final_collections = client.get(BASE + "?offset=40&limit=20").json()
    assert len(final_collections) == 5 and final_collections[-1]["id"] == collections[-1]["id"]
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
