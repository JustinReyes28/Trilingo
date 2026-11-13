from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from test_learning import course as course

from app.config import Config
from app.db import sessions
from app.main import create_app
from app.services import import_content

pytestmark = pytest.mark.usefixtures("course")


def card(client, direction):
    response = client.post(
        "/api/v1/courses/ja-starter/review/cards",
        json={
            "item_id": "ja-word-hello",
            "direction": direction,
        },
    )
    assert response.status_code == 200, response.text
    return response.json()


def test_word_audio_directions_are_self_rated_and_unavailable_pack_keeps_core_recall(client):
    listening = card(client, "listening")
    spoken = card(client, "speaking")
    assert listening["prompt"].startswith("Listen,")
    assert "こんにちは" not in listening["prompt"]
    assert listening["audio_cues"] == [{"id": "reference", "label": "saved word reference"}]
    assert spoken["audio_cues"] == [{"id": "reference", "label": "saved word reference"}]
    assert "supports_recording" not in spoken and "supports_recording" not in listening
    missing = client.post(
        f"/api/v1/review/cards/{listening['id']}/audio/reference", json={"speed": 1}
    )
    assert missing.status_code == 503
    assert missing.json()["error"]["code"] == "audio_unavailable"
    assert client.get(f"/api/v1/review/cards/{listening['id']}").json() == listening
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    rating = {"request_id": str(uuid4()), "expected_revision": 0, "rating": "Good"}
    route = f"/api/v1/review/cards/{listening['id']}/ratings"
    saved = client.post(route, json=rating)
    assert saved.status_code == 200 and saved.json()["scheduled"]
    assert client.post(route, json=rating).json() == saved.json()
    assert client.get("/api/v1/progress").json()["total_xp"] == 5
    assert client.get("/api/v1/personal").json()["objective_checks"] == 0


def test_collection_audio_uses_original_word_and_existing_fsrs_state(
    client, database, fixture_audio_pack, course
):
    collection = client.post(
        "/api/v1/courses/ja-starter/collections",
        json={
            "request_id": str(uuid4()),
            "name": "Saved audio",
        },
    ).json()
    route = f"/api/v1/collections/{collection['id']}"
    client.patch(route + "/members", json={"item_id": "ja-word-hello", "saved": True})
    first = client.post(route + "/recall", json={"direction": "listening"}).json()["cards"][0]
    rated = client.post(
        f"/api/v1/review/cards/{first['id']}/ratings",
        json={
            "request_id": str(uuid4()),
            "expected_revision": 0,
            "rating": "Hard",
        },
    ).json()
    updated = course.model_copy(deep=True)
    updated.version = "99.2.0"
    word = next(word for word in updated.vocabulary if word.id == "ja-word-hello")
    word.surface = "変わった言葉"
    word.pronunciation_override = "かわったことば"
    word.status = "draft"
    with sessions(client.app.state.engine)() as db:
        import_content(db, updated)
    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
            )
        )
    ) as enabled:
        repeated = enabled.post(route + "/recall", json={"direction": "listening"}).json()["cards"][
            0
        ]
        assert repeated == rated
        spoken = enabled.post(route + "/recall", json={"direction": "speaking"}).json()["cards"][0]
        assert spoken["content_version"] == course.version and not spoken["scheduled"]
        assert "supports_recording" not in spoken
        response = enabled.post(
            f"/api/v1/review/cards/{spoken['id']}/audio/reference", json={"speed": 0.75}
        )
        assert response.status_code == 200, response.text
        body = response.json()
        assert body["source"] == "pack"
        assert body["mime"] == "audio/mpeg"
        assert enabled.get(f"/api/v1/review/cards/{rated['id']}").json() == rated
        assert enabled.get("/api/v1/progress").json()["total_xp"] == 5


def test_speaking_review_card_transcription_route_removed_and_self_rating_works(client):
    spoken = card(client, "speaking")
    assert (
        client.post(
            "/api/v1/quests",
            json={
                "request_id": str(uuid4()),
                "kind": "speaking",
                "target": 1,
            },
        ).status_code
        == 422
    )
    route = f"/api/v1/review/cards/{spoken['id']}"
    removed = client.post(route + "/transcriptions", json={"audio_base64": "invalid"})
    assert removed.status_code == 404
    saved = client.post(
        route + "/ratings",
        json={
            "request_id": str(uuid4()),
            "expected_revision": 0,
            "rating": "Easy",
        },
    )
    assert saved.status_code == 200
    stats = client.get("/api/v1/personal").json()
    assert stats["skill_evidence"]["speaking"]["self_rated_reviews"] == 1
    assert stats["skill_evidence"]["speaking"]["speech_attempts"] == 0
    assert stats["objective_checks"] == 0


def test_recall_media_rejects_unsupported_direction_and_cue(client):
    meaning = card(client, "meaning")
    assert (
        client.post(
            f"/api/v1/review/cards/{meaning['id']}/audio/reference", json={"speed": 1}
        ).status_code
        == 422
    )
    listening = card(client, "listening")
    assert (
        client.post(
            f"/api/v1/review/cards/{listening['id']}/audio/invented", json={"speed": 1}
        ).status_code
        == 404
    )
    assert (
        client.post(
            f"/api/v1/review/cards/{listening['id']}/transcriptions",
            json={"audio_base64": "invalid"},
        ).status_code
        == 404
    )
    assert (
        client.post(
            "/api/v1/courses/ja-starter/review/cards",
            json={"item_id": "ja-word-hello", "direction": "recognition"},
        ).status_code
        == 404
    )
