from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from test_grammar_audio import wav
from test_learning import act, start
from test_learning import course as course

from app import providers
from app.config import Config
from app.main import create_app
from app.schemas import Provider

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


def enable(client):
    assert (
        client.patch(
            "/api/v1/settings",
            json={
                "tts": Provider(
                    enabled=True, provider="kokoro", model="test", voice="jf_alpha"
                ).model_dump()
            },
        ).status_code
        == 200
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
    assert audio(client, session).status_code == 503
    assert client.get(f"/api/v1/sessions/{session['id']}").json()["revision"] == 0
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


def test_audio_delivery_retry_stale_and_complete_cue_evidence(client, database, monkeypatch):
    enable(client)
    calls = []

    def synthesize(provider, text, speed, **kwargs):
        calls.append((text, speed, kwargs))
        return wav(), bool(len(calls) > 1)

    monkeypatch.setattr(providers, "synthesize", synthesize)
    with TestClient(create_app(Config(database_url=database, tts_enabled=True))) as enabled:
        session = listening(enabled)
        request = {"request_id": str(uuid4()), "expected_revision": 0, "speed": 1}
        first = audio(enabled, session, body=request)
        assert first.status_code == 200, first.text
        saved = first.json()["session"]
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
        assert len(calls) == 3


def test_provider_error_and_interleaved_action_do_not_add_delivery(client, database, monkeypatch):
    enable(client)
    with TestClient(create_app(Config(database_url=database, tts_enabled=True))) as enabled:
        session = listening(enabled)

        def unavailable(*args, **kwargs):
            raise ValueError("malformed")

        monkeypatch.setattr(providers, "synthesize", unavailable)
        assert audio(enabled, session).status_code == 503
        assert enabled.get(f"/api/v1/sessions/{session['id']}").json()["revision"] == 0

        def interleaved(*args, **kwargs):
            act(client, session, "pause")
            return wav(), False

        monkeypatch.setattr(providers, "synthesize", interleaved)
        assert audio(enabled, session).status_code == 409
        saved = enabled.get(f"/api/v1/sessions/{session['id']}").json()
        assert saved["status"] == "paused"
        assert all(not e["audio_cue_ids"] for e in saved["evidence"].values())


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
