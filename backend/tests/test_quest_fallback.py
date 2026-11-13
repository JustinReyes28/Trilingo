from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from test_learning import act, complete
from test_learning import course as course
from test_listening import audio, listening

from app.config import Config
from app.main import create_app

pytestmark = pytest.mark.usefixtures("course")


def test_audio_quest_does_not_count_text_fallback_and_switch_keeps_identity(client):
    quest_id = str(uuid4())
    body = {"request_id": quest_id, "kind": "listening", "target": 2}
    quest = client.post("/api/v1/quests", json=body).json()
    session = listening(client)
    for item in session["exercises"]:
        session = act(client, session, "skip", item["id"])
    act(client, session, "finish")
    assert client.get("/api/v1/quests").json()[0]["progress"] == 0
    fallback = {"request_id": str(uuid4()), "expected_revision": quest["revision"]}
    route = f"/api/v1/quests/{quest_id}/fallback"
    saved = client.post(route, json=fallback)
    assert saved.status_code == 200, saved.text
    value = saved.json()
    assert value["id"] == quest_id and value["kind"] == "sessions"
    assert value["original_kind"] == "listening"
    assert value["definition_history"][0]["from"] == "listening"
    assert client.post(route, json=fallback).json() == value
    assert client.post(route, json={**fallback, "request_id": str(uuid4())}).status_code == 409
    assert client.get("/api/v1/progress").json()["total_xp"] == 5
    complete(client)
    complete(client)
    saved = client.get("/api/v1/quests").json()[0]
    assert saved["progress"] == 2 and saved["completed_at"]
    assert len(set(saved["source_ids"])) == 2
    assert client.post("/api/v1/quests", json=body).json()["id"] == quest_id


def test_partial_audio_credit_retained_once_after_fallback(database, fixture_audio_pack):
    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
            )
        )
    ) as enabled:
        quest = enabled.post(
            "/api/v1/quests", json={"request_id": str(uuid4()), "kind": "listening", "target": 2}
        ).json()
        session = listening(enabled, "ja-audio-first-introduction")
        session = audio(enabled, session).json()["session"]
        exercise = session["exercises"][0]["id"]
        session = act(enabled, session, "answer", exercise, answer="haru")
        session = act(enabled, session, "finish")
        quest = enabled.get("/api/v1/quests").json()[0]
        assert quest["progress"] == 1
        fallback = enabled.post(
            f"/api/v1/quests/{quest['id']}/fallback",
            json={"request_id": str(uuid4()), "expected_revision": quest["revision"]},
        ).json()
        assert fallback["progress"] == 1 and fallback["source_ids"] == [session["id"]]
        assert fallback["definition_history"][0]["prior_source_ids"] == [session["id"]]
        complete(enabled)
        quest = enabled.get("/api/v1/quests").json()[0]
        assert quest["progress"] == 2 and quest["completed_at"]
        assert enabled.get("/api/v1/progress").json()["total_xp"] == 25
