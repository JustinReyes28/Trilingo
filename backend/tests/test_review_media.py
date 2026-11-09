import base64
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select
from test_grammar_audio import wav
from test_learning import course as course
from test_listening import enable
from test_speaking import enable_stt

from app import providers
from app.config import Config
from app.db import sessions
from app.learning_models import StudyEvent
from app.main import create_app
from app.review_models import ReviewEvent
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


def test_word_audio_directions_are_self_rated_and_provider_failure_keeps_core_recall(client):
    listening = card(client, "listening")
    spoken = card(client, "speaking")
    assert listening["prompt"].startswith("Listen,")
    assert "こんにちは" not in listening["prompt"]
    assert listening["audio_cues"] == [{"id": "reference", "label": "saved word reference"}]
    assert spoken["supports_recording"] and not listening["supports_recording"]
    assert (
        client.post(
            f"/api/v1/review/cards/{listening['id']}/audio/reference", json={"speed": 1}
        ).status_code
        == 503
    )
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
    client, database, monkeypatch, course
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
    enable(client)
    calls = []

    def synthesize(provider, text, speed, **kwargs):
        calls.append((text, speed, kwargs["pronunciation_override"]))
        return wav(), False

    monkeypatch.setattr(providers, "synthesize", synthesize)
    with TestClient(create_app(Config(database_url=database, tts_enabled=True))) as enabled:
        repeated = enabled.post(route + "/recall", json={"direction": "listening"}).json()["cards"][
            0
        ]
        assert repeated == rated
        spoken = enabled.post(route + "/recall", json={"direction": "speaking"}).json()["cards"][0]
        assert spoken["content_version"] == course.version and not spoken["scheduled"]
        response = enabled.post(
            f"/api/v1/review/cards/{spoken['id']}/audio/reference", json={"speed": 0.75}
        )
        assert response.status_code == 200, response.text
        assert calls == [("こんにちは", 0.75, None)]
        assert enabled.get(f"/api/v1/review/cards/{rated['id']}").json() == rated
        assert enabled.get("/api/v1/progress").json()["total_xp"] == 5


def test_transient_recall_transcript_cannot_award_speech_evidence_or_audio_quest(
    client, database, monkeypatch
):
    spoken = card(client, "speaking")
    assignment = client.post(
        "/api/v1/quests",
        json={
            "request_id": str(uuid4()),
            "kind": "speaking",
            "target": 1,
        },
    ).json()
    enable_stt(client)
    monkeypatch.setattr(providers, "transcribe", lambda *args: "こんにちは")
    with TestClient(create_app(Config(database_url=database, stt_enabled=True))) as enabled:
        route = f"/api/v1/review/cards/{spoken['id']}"
        response = enabled.post(
            route + "/transcriptions", json={"audio_base64": base64.b64encode(wav()).decode()}
        )
        assert response.status_code == 200, response.text
        assert response.json()["agrees"]
        assert "Transient" in response.json()["label"]
        assert enabled.get(route).json() == spoken
        with sessions(enabled.app.state.engine)() as db:
            assert db.scalar(select(func.count()).select_from(StudyEvent)) == 0
            assert db.scalar(select(func.count()).select_from(ReviewEvent)) == 0
        saved = enabled.post(
            route + "/ratings",
            json={
                "request_id": str(uuid4()),
                "expected_revision": 0,
                "rating": "Easy",
            },
        )
        assert saved.status_code == 200
        stats = enabled.get("/api/v1/personal").json()
        assert stats["skill_evidence"]["speaking"]["self_rated_reviews"] == 1
        assert stats["skill_evidence"]["speaking"]["speech_attempts"] == 0
        assert stats["objective_checks"] == 0
        assert (
            next(q for q in enabled.get("/api/v1/quests").json() if q["id"] == assignment["id"])[
                "progress"
            ]
            == 0
        )


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
        == 422
    )
    assert (
        client.post(
            "/api/v1/courses/ja-starter/review/cards",
            json={"item_id": "ja-word-hello", "direction": "recognition"},
        ).status_code
        == 404
    )
