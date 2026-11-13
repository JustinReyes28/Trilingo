import importlib.util

import pytest
from test_learning import act, action_body, start
from test_learning import course as course

from app.config import Config

pytestmark = pytest.mark.usefixtures("course")


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


def test_audio_failures_never_change_progress_and_removed_ai_stt_routes_return_404(client):
    session = start(client)
    exercise_id = session["exercises"][0]["id"]
    reference = {"course_id": "ja-starter", "item_id": "ja-word-hello"}
    speech_err = client.post("/api/v1/audio/speech", json=reference)
    assert speech_err.status_code == 503
    assert speech_err.json()["error"]["code"] == "audio_unavailable"
    assert (
        client.post(
            "/api/v1/audio/speech", json={**reference, "item_id": "../../secret"}
        ).status_code
        == 404
    )
    assert client.get("/api/v1/audio/voices").status_code == 404

    removed_posts = [
        ("/api/v1/explanations", {"session_id": session["id"], "exercise_id": exercise_id}),
        (
            "/api/v1/scenarios/practice",
            {
                "course_id": "ja-starter",
                "scenario_id": "dialogue-meeting",
                "preview_draft": True,
                "message": "はじめまして。",
            },
        ),
        (
            "/api/v1/scenarios/transcriptions",
            {
                "course_id": "ja-starter",
                "scenario_id": "dialogue-meeting",
                "preview_draft": True,
                "audio_base64": "invalid",
            },
        ),
        ("/api/v1/audio/transcriptions", {**reference, "audio_base64": "invalid"}),
        (
            f"/api/v1/sessions/{session['id']}/exercises/{exercise_id}/speech",
            {
                "request_id": session["next_action_id"],
                "expected_revision": session["revision"],
                "audio_base64": "invalid",
            },
        ),
        ("/api/v1/review/cards/card-1/transcriptions", {"audio_base64": "invalid"}),
    ]
    for path, body in removed_posts:
        assert client.post(path, json=body).status_code == 404, path
    assert client.get("/api/v1/providers/status").status_code == 404

    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    status = client.get("/api/v1/audio/status").json()
    assert set(status.keys()) == {"audio_pack"}
    assert not status["audio_pack"]["bundled_reference"]


def test_runtime_ai_stt_tts_removed_from_app_and_config():
    assert "ai_enabled" not in Config.model_fields
    assert "stt_enabled" not in Config.model_fields
    assert "tts_enabled" not in Config.model_fields
    assert "audio_cache_dir" not in Config.model_fields
    assert not hasattr(Config, "ai_enabled")
    assert not hasattr(Config, "stt_enabled")
    assert not hasattr(Config, "tts_enabled")
    for removed_module in ("app.providers", "app.scenario_practice", "app.speaking"):
        assert importlib.util.find_spec(removed_module) is None


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
