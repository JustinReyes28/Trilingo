import base64
import io
import math
import struct
import wave

import httpx
import pytest
from fastapi.testclient import TestClient
from test_learning import act, action_body, start
from test_learning import course as course

from app import providers
from app.config import Config
from app.main import create_app
from app.schemas import Provider

pytestmark = pytest.mark.usefixtures("course")


def wav(silent=False):
    output = io.BytesIO()
    with wave.open(output, "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(16000)
        audio.writeframes(
            b"".join(
                struct.pack("<h", 0 if silent else int(1000 * math.sin(i / 10)))
                for i in range(1600)
            )
        )
    return output.getvalue()


def test_grammar_search_bookmarks_and_three_authored_scenarios_without_ai(client):
    url = "/api/v1/courses/ja-starter/grammar"
    assert client.get(url).json()["notes"] == []
    data = client.get(url + "?include_drafts=true&search=particle-de").json()
    assert {note["id"] for note in data["notes"]} == {
        "guide-de",
        "ja-guide-unit-7-ask-directions",
        "ja-guide-unit-8-polite-routine",
    }
    assert len(data["scenarios"]) >= 6
    unit_search = client.get(
        url + "?include_drafts=true&unit_id=ja-unit-8&search=particle-de"
    ).json()
    assert {note["id"] for note in unit_search["notes"]} == {
        "guide-de",
        "ja-guide-unit-8-polite-routine",
    }
    reading_search = client.get(url + "?include_drafts=true&search=よじ").json()
    assert {note["id"] for note in reading_search["notes"]} == {"ja-guide-unit-5-clock-time"}
    bookmark = client.patch(
        "/api/v1/courses/ja-starter/reading/items/grammar/guide-de",
        json={"saved": True, "preview_draft": True},
    )
    assert bookmark.status_code == 200, bookmark.text
    assert any(
        item["item_id"] == "guide-de" and item["saved"]
        for item in client.get("/api/v1/courses/ja-starter/reading").json()["items"]
    )
    for scenario, answer in [
        ("meeting", "polite"),
        ("food", "お水をください。"),
        ("purchase", "これをお願いします。"),
    ]:
        session = start(client, "dialogue-" + scenario, source_kind="story", preview_draft=True)
        exercise = session["exercises"][0]
        assert not {"answer", "answers", "hint", "explanation"} & exercise.keys()
        session = act(client, session, "answer", exercise["id"], answer=answer)
        assert session["feedback"]["kind"] == "correct"
        session = act(client, session, "pause")
        session = act(client, session, "resume")
        session = act(client, session, "story_continue")
        assert session["story"]["current"]["id"].endswith("-end")
        receipt = action_body(session, "finish")
        route = "/api/v1/sessions/" + session["id"] + "/actions"
        assert client.post(route, json=receipt).json() == client.post(route, json=receipt).json()
    assert client.get("/api/v1/progress").json()["total_xp"] == 15


def test_dialogue_branch_mistake_reveal_skip_and_invalid_turn(client):
    session = start(client, "dialogue-meeting", source_kind="story", preview_draft=True)
    session = act(client, session, "answer", "dialogue-meeting-response", answer="other")
    assert session["feedback"]["kind"] == "incorrect"
    session = act(client, session, "story_continue")
    assert session["story"]["current"]["id"].endswith("-help")
    invalid = client.post(
        "/api/v1/sessions/" + session["id"] + "/actions",
        json=action_body(session, "story_visit", turn_id="missing"),
    )
    assert invalid.status_code == 404
    session = act(client, session, "finish")
    assert session["xp_awarded"] == 5


def test_ai_disabled_authored_fallback_and_audio_failures_never_change_progress(client):
    session = start(client)
    exercise_id = session["exercises"][0]["id"]
    body = {"session_id": session["id"], "exercise_id": exercise_id}
    assert client.post("/api/v1/explanations", json=body).status_code == 409
    session = act(client, session, "reveal", exercise_id)
    explanation = client.post("/api/v1/explanations", json=body).json()
    assert explanation["authored"] and explanation["generated"] is None
    reference = {"course_id": "ja-starter", "item_id": "ja-word-hello"}
    assert client.post("/api/v1/audio/speech", json=reference).status_code == 503
    assert (
        client.post(
            "/api/v1/audio/transcriptions", json={**reference, "audio_base64": "invalid"}
        ).status_code
        == 503
    )
    assert (
        client.post(
            "/api/v1/audio/speech", json={**reference, "item_id": "../../secret"}
        ).status_code
        == 404
    )
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert not client.get("/api/v1/providers/status").json()["tts"]["verified"]


def test_wave_validation_and_independent_stt_format(monkeypatch):
    assert providers.validate_wav(wav()) == 0.1
    for data in [b"bad audio", wav(True), wav()[:-10], b"x" * 1_000_001]:
        with pytest.raises(ValueError):
            providers.validate_wav(data)
    with pytest.raises(ValueError):
        providers.transcribe(
            Provider(provider="kokoro", model="tts"), base64.b64encode(wav()).decode()
        )


def test_tts_japanese_voice_cache_version_and_malformed_provider(monkeypatch, tmp_path):
    calls = []

    def handle(request):
        calls.append(request.url.path)
        if request.url.path.endswith("/voices"):
            return httpx.Response(200, json={"voices": ["af_heart", "jf_alpha"]})
        return httpx.Response(200, content=wav(), headers={"content-type": "audio/wav"})

    real = httpx.Client
    monkeypatch.setattr(
        providers.httpx,
        "Client",
        lambda **kwargs: real(transport=httpx.MockTransport(handle), **kwargs),
    )
    config = Provider(provider="kokoro", model="kokoro-version-test", voice="jf_alpha")
    assert providers.synthesize(config, "こんにちは。", 1, tmp_path)[1] is False
    assert providers.synthesize(config, "こんにちは。", 1, tmp_path)[1] is True
    assert len(calls) == 2
    config.model = "new-version"
    assert providers.synthesize(config, "こんにちは。", 1, tmp_path)[1] is False
    config.voice = "af_heart"
    with pytest.raises(ValueError):
        providers.synthesize(config, "こんにちは。", 1, tmp_path)


@pytest.mark.parametrize(
    "failure",
    [httpx.ConnectError("offline"), httpx.ReadTimeout("timeout"), ValueError("malformed")],
)
def test_local_ai_failures_use_authored_fallback_without_side_effects(
    client, database, monkeypatch, failure
):
    session = start(client)
    exercise_id = session["exercises"][0]["id"]
    session = act(client, session, "reveal", exercise_id)
    provider = Provider(provider="lm-studio", enabled=True, model="local-model")
    assert client.patch("/api/v1/settings", json={"ai": provider.model_dump()}).status_code == 200

    def fail(*_args, **_kwargs):
        raise failure

    monkeypatch.setattr(providers, "explain", fail)
    with TestClient(create_app(Config(database_url=database, ai_enabled=True))) as enabled:
        result = enabled.post(
            "/api/v1/explanations", json={"session_id": session["id"], "exercise_id": exercise_id}
        ).json()
        assert result["generated"] is None and result["authored"]
        assert "fallback" in result["status"]
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert client.get("/api/v1/sessions/" + session["id"]).json() == session


def test_local_ai_advisory_html_remains_text_and_configuration_swap(client, database, monkeypatch):
    session = start(client)
    exercise_id = session["exercises"][0]["id"]
    session = act(client, session, "reveal", exercise_id)
    seen = []

    def explain(provider, _context):
        seen.append(provider.model)
        return "<script>alert('not executable')</script> Unverified model text"

    monkeypatch.setattr(providers, "explain", explain)
    with TestClient(create_app(Config(database_url=database, ai_enabled=True))) as enabled:
        for model in ["first-model", "second-model"]:
            provider = Provider(provider="openai-compatible", enabled=True, model=model)
            client.patch("/api/v1/settings", json={"ai": provider.model_dump()})
            result = enabled.post(
                "/api/v1/explanations",
                json={"session_id": session["id"], "exercise_id": exercise_id},
            ).json()
            assert result["generated"].startswith("<script>") and "advisory" in result["status"]
    assert seen == ["first-model", "second-model"]
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_stt_valid_wav_japanese_request_and_malformed_response(monkeypatch):
    calls = []

    def handle(request):
        calls.append(request.content)
        return httpx.Response(200, json={"text": "こんにちは。"})

    real = httpx.Client
    monkeypatch.setattr(
        providers.httpx,
        "Client",
        lambda **kwargs: real(transport=httpx.MockTransport(handle), **kwargs),
    )
    config = Provider(provider="openai-compatible", model="test-japanese-stt")
    assert providers.transcribe(config, base64.b64encode(wav()).decode()) == "こんにちは。"
    assert b'name="language"' in calls[0] and b"ja" in calls[0]
    with pytest.raises(ValueError):
        providers.transcribe(config, "malformed-base64")


def test_additive_dialogue_defaults_preserve_historical_import_idempotency(client, course):
    import hashlib
    import json

    from app.content_schema import CourseContent
    from app.db import sessions
    from app.models import CourseVersion
    from app.services import DomainError, import_content

    legacy = course.model_dump(mode="json")
    legacy["version"] = "0.0.1"
    legacy["narratives"] = [story for story in legacy["narratives"] if story["kind"] != "dialogue"]
    for story in legacy["narratives"]:
        for turn in story["turns"]:
            turn.pop("response_transitions", None)
    digest = hashlib.sha256(
        json.dumps(legacy, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()
    with sessions(client.app.state.engine)() as db:
        row = CourseVersion(
            id=course.id + "@0.0.1",
            course_id=course.id,
            version="0.0.1",
            digest=digest,
            data=legacy,
        )
        db.add(row)
        db.commit()
        assert import_content(db, CourseContent.model_validate(legacy)) is False
        assert row.data == legacy and row.digest == digest
        changed = CourseContent.model_validate(legacy)
        changed.title = "A different title"
        with pytest.raises(DomainError, match="Content changed"):
            import_content(db, changed)


def test_current_kokoro_voice_objects_and_pronunciation_cache(monkeypatch, tmp_path):
    import json

    calls = []

    def handle(request):
        calls.append(request)
        if request.url.path.endswith("/voices"):
            return httpx.Response(200, json={"voices": [{"id": "af_heart"}, {"id": "jf_alpha"}]})
        return httpx.Response(200, content=wav(), headers={"content-type": "audio/wav"})

    real = httpx.Client
    monkeypatch.setattr(
        providers.httpx,
        "Client",
        lambda **kwargs: real(transport=httpx.MockTransport(handle), **kwargs),
    )
    config = Provider(provider="kokoro", model="version", voice="jf_alpha")
    assert providers.voices(config) == ["jf_alpha"]
    assert not providers.synthesize(
        config,
        "私は学校へ行きます。",
        1,
        tmp_path,
        pronunciation_override="わたしはがっこうへいきます。",
    )[1]
    assert json.loads(calls[-1].content)["input"] == "わたしはがっこうへいきます。"
    assert providers.synthesize(
        config,
        "私は学校へ行きます。",
        1,
        tmp_path,
        pronunciation_override="わたしはがっこうへいきます。",
    )[1]
    assert not providers.synthesize(
        config,
        "私は学校へ行きます。",
        1,
        tmp_path,
        pronunciation_override="わたしわがっこうえいきます。",
    )[1]
    with pytest.raises(ValueError):
        providers.synthesize(config, "hello", 1, tmp_path, language="en")
