import base64
import json
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select
from test_grammar_audio import wav
from test_learning import act, action_body, start
from test_learning import course as course
from test_listening import audio

from app import providers
from app.config import Config
from app.db import sessions
from app.learning_models import StudyEvent, XpEntry
from app.main import create_app
from app.schemas import Provider
from app.services import import_content

pytestmark = pytest.mark.usefixtures("course")


def speaking(client):
    return start(client, "dialogue-food", source_kind="speaking", preview_draft=True)


def speech(client, session, exercise=None, body=None):
    exercise = exercise or session["exercises"][0]["id"]
    body = body or {
        "request_id": session["next_action_id"],
        "expected_revision": session["revision"],
        "audio_base64": base64.b64encode(wav()).decode(),
    }
    return client.post(f"/api/v1/sessions/{session['id']}/exercises/{exercise}/speech", json=body)


def enable_stt(client):
    response = client.patch(
        "/api/v1/settings",
        json={
            "stt": Provider(
                enabled=True, provider="openai-compatible", model="test-stt"
            ).model_dump()
        },
    )
    assert response.status_code == 200


def quest(client):
    response = client.post(
        "/api/v1/quests",
        json={
            "request_id": str(uuid4()),
            "kind": "speaking",
            "target": 2,
        },
    )
    assert response.status_code == 200, response.text
    return response.json()


def test_disabled_speaking_typed_fallback_skip_finish_replay_and_no_audio_credit(client):
    denied = client.post(
        "/api/v1/courses/ja-starter/sessions",
        json={
            "request_id": str(uuid4()),
            "source_kind": "speaking",
            "source_id": "dialogue-food",
        },
    )
    assert denied.status_code == 404
    assignment = quest(client)
    session = speaking(client)
    first, second = [e["id"] for e in session["exercises"]]
    assert session["exercises"][0]["reference_text"] == "水をください。"
    assert "pronunciation_override" not in str(session["exercises"])
    assert speech(client, session).status_code == 503
    session = act(client, session, "answer", first, answer="水をください。")
    assert session["feedback"]["kind"] == "recorded"
    assert session["evidence"][first]["typed_fallbacks"] == 1
    assert session["evidence"][first]["speech_attempts"] == 0
    assert session["assessed_count"] == session["initial_correct"] == 0
    session = act(client, session, "pause")
    assert client.get(f"/api/v1/sessions/{session['id']}").json() == session
    session = act(client, session, "resume")
    session = act(client, session, "skip", second)
    body = action_body(session, "finish")
    path = f"/api/v1/sessions/{session['id']}/actions"
    saved = client.post(path, json=body).json()
    assert saved["xp_awarded"] == 5
    assert client.post(path, json=body).json() == saved
    replay = speaking(client)
    for exercise in replay["exercises"]:
        replay = act(client, replay, "skip", exercise["id"])
    assert act(client, replay, "finish")["xp_awarded"] == 5
    stats = client.get("/api/v1/personal").json()
    assert stats["skill_evidence"]["speaking"]["objective_checks"] == 0
    assert stats["skill_evidence"]["speaking"]["typed_fallbacks"] == 1
    assert client.get("/api/v1/quests").json()[0]["source_ids"] == []
    assert client.get("/api/v1/progress").json()["total_xp"] == 10
    fallback_body = {"request_id": str(uuid4()), "expected_revision": assignment["revision"]}
    fallback = client.post(f"/api/v1/quests/{assignment['id']}/fallback", json=fallback_body)
    assert fallback.status_code == 200
    assert fallback.json()["original_kind"] == "speaking"
    assert (
        client.post(f"/api/v1/quests/{assignment['id']}/fallback", json=fallback_body).json()
        == fallback.json()
    )


def test_durable_transcripts_exact_retry_snapshot_and_genuine_audio_quest(
    client, database, fixture_audio_pack, monkeypatch, course
):
    enable_stt(client)
    calls = []

    def transcribe(provider, encoded):
        calls.append(provider.model)
        return "水をください。" if len(calls) <= 2 else "すみません、もう一度お願いします。"

    monkeypatch.setattr(providers, "transcribe", transcribe)
    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
                stt_enabled=True,
            )
        )
    ) as enabled:
        assignment = quest(enabled)
        session = speaking(enabled)
        # A later content import must not change this session's comparison reference.
        changed = course.model_copy(deep=True)
        major, minor, patch = map(int, course.version.split("."))
        changed.version = f"{major}.{minor}.{patch + 1}"
        next(e for e in changed.practice_exercises if e.id == "dialogue-food-speaking-1").audio[
            0
        ].transcript = "別のモデル。"
        with sessions(enabled.app.state.engine)() as db:
            import_content(db, changed)
        for index, exercise in enumerate(session["exercises"]):
            session = audio(enabled, session, exercise=exercise["id"]).json()["session"]
            body = {
                "request_id": session["next_action_id"],
                "expected_revision": session["revision"],
                "audio_base64": base64.b64encode(wav()).decode(),
            }
            response = speech(enabled, session, exercise["id"], body)
            assert response.status_code == 200, response.text
            saved = response.json()
            assert speech(enabled, session, exercise["id"], body).json() == saved
            assert (
                speech(
                    enabled, session, exercise["id"], {**body, "expected_revision": 100}
                ).status_code
                == 409
            )
            session = saved
            if index == 0:
                # Another intentional attempt is distinct from duplicate request delivery.
                session = speech(enabled, session, exercise["id"]).json()
        assert len(calls) == 3
        assert session["assessed_count"] == 0
        assert all(e["first_correct"] is None for e in session["evidence"].values())
        session = act(enabled, session, "finish")
        assert session["xp_awarded"] == 5
        saved_quest = enabled.get("/api/v1/quests").json()[0]
        assert saved_quest["source_ids"] == [session["id"]]
        stats = enabled.get("/api/v1/personal").json()["skill_evidence"]["speaking"]
        assert stats["speech_attempts"] == stats["transcript_matches"] == 3
        assert stats["objective_checks"] == 0
        with sessions(enabled.app.state.engine)() as db:
            events = db.scalars(
                select(StudyEvent).where(StudyEvent.session_id == session["id"])
            ).all()
            assert all("audio_base64" not in json.dumps(e.request) for e in events)
            assert sum(e.request.get("action") == "speech" for e in events) == 3
            assert len(db.scalars(select(XpEntry)).all()) == 1
        fallback = enabled.post(
            f"/api/v1/quests/{assignment['id']}/fallback",
            json={
                "request_id": str(uuid4()),
                "expected_revision": saved_quest["revision"],
            },
        ).json()
        assert fallback["source_ids"] == [session["id"]]
        assert fallback["definition_history"][0]["prior_source_ids"] == [session["id"]]


def test_invalid_media_failures_and_interleaved_action_preserve_saved_work(
    client, database, monkeypatch
):
    enable_stt(client)
    with TestClient(create_app(Config(database_url=database, stt_enabled=True))) as enabled:
        session = speaking(enabled)
        for encoded in [
            "not-base64",
            base64.b64encode(wav(silent=True)).decode(),
            base64.b64encode(wav()[:-100]).decode(),
        ]:
            body = {
                "request_id": session["next_action_id"],
                "expected_revision": 0,
                "audio_base64": encoded,
            }
            assert speech(enabled, session, body=body).status_code == 422
        oversized = {
            "request_id": session["next_action_id"],
            "expected_revision": 0,
            "audio_base64": "A" * 1_400_001,
        }
        assert speech(enabled, session, body=oversized).status_code == 413

        def unavailable(*args):
            raise ValueError("incompatible provider")

        monkeypatch.setattr(providers, "transcribe", unavailable)
        assert speech(enabled, session).status_code == 503
        assert enabled.get(f"/api/v1/sessions/{session['id']}").json() == session

        def interleaved(*args):
            act(client, session, "pause")
            return "水をください。"

        monkeypatch.setattr(providers, "transcribe", interleaved)
        assert speech(enabled, session).status_code == 409
        saved = enabled.get(f"/api/v1/sessions/{session['id']}").json()
        assert saved["status"] == "paused"
        assert all(e["speech_attempts"] == 0 for e in saved["evidence"].values())


def test_missing_reference_or_typed_fallback_never_earns_speaking_credit(
    client, database, fixture_audio_pack, monkeypatch
):
    enable_stt(client)
    monkeypatch.setattr(providers, "transcribe", lambda *a: "水をください。")
    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
                stt_enabled=True,
            )
        )
    ) as enabled:
        quest(enabled)
        for mode in ["missing_reference", "typed_fallback", "skip"]:
            session = speaking(enabled)
            for exercise in session["exercises"]:
                if mode != "missing_reference":
                    session = audio(enabled, session, exercise=exercise["id"]).json()["session"]
                session = speech(enabled, session, exercise["id"]).json()
                if mode == "typed_fallback":
                    session = act(
                        enabled, session, "answer", exercise["id"], answer="text practice"
                    )
                if mode == "skip":
                    session = act(enabled, session, "skip", exercise["id"])
            assert act(enabled, session, "finish")["xp_awarded"] == 5
        assert enabled.get("/api/v1/quests").json()[0]["progress"] == 0


def test_changed_stt_configuration_discards_inflight_feedback(client, database, monkeypatch):
    enable_stt(client)
    with TestClient(create_app(Config(database_url=database, stt_enabled=True))) as enabled:
        session = speaking(enabled)

        def changed_provider(*args):
            assert (
                client.patch(
                    "/api/v1/settings",
                    json={
                        "stt": Provider(
                            enabled=True, provider="openai-compatible", model="replacement"
                        ).model_dump()
                    },
                ).status_code
                == 200
            )
            return "水をください。"

        monkeypatch.setattr(providers, "transcribe", changed_provider)
        response = speech(enabled, session)
        assert (
            response.status_code == 409 and response.json()["error"]["code"] == "provider_changed"
        )
        assert enabled.get(f"/api/v1/sessions/{session['id']}").json() == session
        first = session["exercises"][0]["id"]
        revealed = act(enabled, session, "reveal", first)
        assert revealed["feedback"]["answer"] == "水をください。"
        assert revealed["assessed_count"] == 0
