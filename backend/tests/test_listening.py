from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select
from test_learning import act, start
from test_learning import course as course

from app import audio_pack
from app.audio_models import AudioDelivery
from app.config import Config
from app.db import sessions
from app.main import create_app

pytestmark = pytest.mark.usefixtures("course")


def listening(client, source="ja-audio-thanks-contexts"):
    return start(client, source, source_kind="listening", preview_draft=True)


def audio(client, session, cue="reference", exercise=None, body=None):
    exercise = exercise or session["exercises"][0]["id"]
    body = body or {
        "request_id": str(uuid4()),
        "expected_revision": session["revision"],
        "speed": 1,
    }
    return client.post(
        f"/api/v1/sessions/{session['id']}/exercises/{exercise}/audio/{cue}", json=body
    )


def test_protected_audio_and_disabled_fallback_still_finishes(client):
    denied = client.post(
        "/api/v1/courses/ja-starter/sessions",
        json={
            "request_id": str(uuid4()),
            "source_kind": "listening",
            "source_id": "ja-audio-thanks-contexts",
        },
    )
    assert denied.status_code == 404
    session = listening(client)
    assert [e["type"] for e in session["exercises"]] == ["dictation", "audio_contrast"]
    public = str(session["exercises"])
    for secret in [
        "transcript",
        "pronunciation_override",
        "answers",
        "response_feedback",
        "ありがとうございます",
    ]:
        assert secret not in public
    missing_audio = audio(client, session)
    assert missing_audio.status_code == 503
    assert missing_audio.json()["error"]["code"] == "audio_unavailable"
    assert client.get(f"/api/v1/sessions/{session['id']}").json()["revision"] == 0
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(AudioDelivery)) == 0
    first = session["exercises"][0]["id"]
    session = act(client, session, "audio_text", first)
    assert "ありがとうございます" in session["feedback"]["message"]
    session = act(client, session, "answer", first, answer="ありがとうございます")
    assert session["feedback"]["kind"] == "correct"
    assert session["evidence"][first]["first_assisted"]
    second = session["exercises"][1]["id"]
    session = act(client, session, "answer", second, answer="b")
    assert session["evidence"][second]["text_fallback"]
    session = act(client, session, "finish")
    assert session["xp_awarded"] == 5 and session["assessed_count"] == 0
    replay = listening(client)
    for item in replay["exercises"]:
        replay = act(client, replay, "skip", item["id"])
    assert act(client, replay, "finish")["xp_awarded"] == 5


def test_audio_delivery_retry_stale_and_complete_cue_evidence(database, fixture_audio_pack):
    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
            )
        )
    ) as enabled:
        session = listening(enabled)
        request = {"request_id": str(uuid4()), "expected_revision": 0, "speed": 1}
        first = audio(enabled, session, body=request)
        assert first.status_code == 200, first.text
        first_body = first.json()
        assert first_body["source"] == "pack"
        assert first_body["mime"] == "audio/mpeg"
        saved = first_body["session"]
        assert saved["revision"] == 1
        assert audio(enabled, session, body=request).json()["session"] == saved
        assert audio(enabled, session, body={**request, "speed": 0.75}).status_code == 409
        assert audio(enabled, session).status_code == 409
        item = saved["exercises"][0]["id"]
        saved = act(enabled, saved, "answer", item, answer="ありがとうございます")
        assert not saved["evidence"][item]["first_assisted"]
        contrast = saved["exercises"][1]["id"]
        saved = audio(enabled, saved, cue="a", exercise=contrast).json()["session"]
        saved = act(enabled, saved, "answer", contrast, answer="b")
        assert saved["evidence"][contrast]["first_assisted"]
        assert saved["evidence"][contrast]["text_fallback"]
        assert act(enabled, saved, "finish")["xp_awarded"] == 5


def test_pack_unavailable_and_interleaved_action_do_not_add_delivery(
    client, database, fixture_audio_pack, monkeypatch
):
    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
            )
        )
    ) as enabled:
        session = listening(enabled)

        monkeypatch.setattr(audio_pack, "lookup", lambda *args, **kwargs: None)
        unavailable = audio(enabled, session)
        assert unavailable.status_code == 503
        assert unavailable.json()["error"]["code"] == "audio_unavailable"
        assert enabled.get(f"/api/v1/sessions/{session['id']}").json()["revision"] == 0
        with sessions(enabled.app.state.engine)() as db:
            assert db.scalar(select(func.count()).select_from(AudioDelivery)) == 0

        def interleaved(*args, **kwargs):
            act(client, session, "pause")
            return audio_pack.PackClip(
                key="k",
                data=b"ID3 clip",
                mime="audio/mpeg",
                duration_seconds=0.5,
                course_version="0.1.21",
                reviewed=False,
            )

        monkeypatch.setattr(audio_pack, "lookup", interleaved)
        assert audio(enabled, session).status_code == 409
        saved = enabled.get(f"/api/v1/sessions/{session['id']}").json()
        assert saved["status"] == "paused"
        assert all(not e["audio_cue_ids"] for e in saved["evidence"].values())
        with sessions(enabled.app.state.engine)() as db:
            assert db.scalar(select(func.count()).select_from(AudioDelivery)) == 0


def test_targeted_grammar_has_private_response_feedback_and_unrestricted_retry(client):
    session = start(client, "guide-de", source_kind="grammar", preview_draft=True)
    item = session["exercises"][0]
    assert "response_feedback" not in item
    session = act(client, session, "answer", item["id"], answer="wrong")
    assert "destination" in session["feedback"]["explanation"]
    session = act(client, session, "answer", item["id"], answer="correct")
    assert session["feedback"]["kind"] == "correct"
    for remaining in session["exercises"][1:]:
        session = act(client, session, "skip", remaining["id"])
    assert act(client, session, "finish")["xp_awarded"] == 5
