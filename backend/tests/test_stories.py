from copy import deepcopy
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from test_learning import act, action_body, start
from test_learning import course as course

from app.config import Config
from app.db import sessions
from app.main import create_app
from app.services import import_content

pytestmark = pytest.mark.usefixtures("course")
STORY = "ja-story-drink"


def test_story_draft_guard_private_keys_and_contextual_aids(client):
    denied = client.post(
        "/api/v1/courses/ja-starter/sessions",
        json={
            "request_id": str(uuid4()),
            "source_kind": "story",
            "source_id": STORY,
        },
    )
    assert denied.status_code == 404
    client.patch("/api/v1/settings", json={"furigana": "hidden"})
    session = start(client, STORY, source_kind="story", preview_draft=True)
    assert session["kind"] == "reading" and session["story"]
    assert all(segment["reading"] is None for segment in session["story"]["current"]["text"])
    assert all(
        word["reading"] is None and word["gloss"] is None for word in session["story"]["glossary"]
    )
    assert all(
        not {"answer", "answers", "hint", "explanation"} & e.keys() for e in session["exercises"]
    )
    assert not session["story"]["assisted_turn_ids"]
    session = act(client, session, "show_readings")
    assert session["story"]["current"]["text"][0]["reading"] == "みず"
    assert session["evidence"]["ja-story-drink-water"]["assisted"]
    session = act(client, session, "hide_readings")
    assert all(segment["reading"] is None for segment in session["story"]["current"]["text"])
    assert session["evidence"]["ja-story-drink-water"]["assisted"]
    session = act(client, session, "answer", "ja-story-drink-water", answer="c1")
    assert session["evidence"]["ja-story-drink-water"]["first_assisted"]
    assert session["initial_correct"] == 0 and session["assessed_count"] == 0


def test_unfamiliar_readings_use_explicit_familiarity_not_mastery(client):
    client.patch("/api/v1/settings", json={"furigana": "unfamiliar"})
    client.patch(
        "/api/v1/courses/ja-starter/reading/items/word/ja-word-water",
        json={"familiar": True, "preview_draft": True},
    )
    session = start(client, STORY, source_kind="story", preview_draft=True)
    assert session["story"]["current"]["text"][0]["reading"] is None
    assert not session["evidence"]["ja-story-drink-water"]["assisted"]
    session = act(client, session, "story_visit", turn_id="drink-haru")
    assert session["story"]["current"]["text"][0]["reading"] == "おちゃ"
    assert session["evidence"]["ja-story-drink-tea"]["assisted"]


def test_story_wrong_answers_skips_glossary_unlimited_replays_and_receipts(client):
    session = start(client, STORY, source_kind="story", preview_draft=True, mode="unassisted")
    assert not session["story"]["reading_aids"]
    session = act(client, session, "answer", "ja-story-drink-water", answer="c0")
    assert session["feedback"]["kind"] == "incorrect"
    session = act(client, session, "story_continue")
    assert session["story"]["current"]["id"] == "drink-haru"
    session = act(client, session, "glossary", vocabulary_id="ja-word-tea")
    assert (
        next(w for w in session["story"]["glossary"] if w["id"] == "ja-word-tea")["gloss"] == "tea"
    )
    session = act(client, session, "story_continue")
    assert session["evidence"]["ja-story-drink-tea"]["skipped"]
    assert session["story"]["current"]["id"] == "drink-thanks"
    session = act(client, session, "pause")
    assert session["status"] == "paused"
    session = act(client, session, "resume")
    session = act(client, session, "story_continue")
    assert session["story"]["at_end"]
    request = action_body(session, "finish")
    url = "/api/v1/sessions/" + session["id"] + "/actions"
    finished = client.post(url, json=request).json()
    assert finished["xp_awarded"] == 5
    assert client.post(url, json=request).json() == finished
    for _ in range(3):
        replay = start(client, STORY, source_kind="story", preview_draft=True)
        # Explicit finish honestly skips untouched checks without a prerequisite.
        assert act(client, replay, "finish")["xp_awarded"] == 5
    assert client.get("/api/v1/progress").json()["total_xp"] == 20
    recap = start(client, STORY, source_kind="story_recap", preview_draft=True)
    assert recap["story"] is None and len(recap["exercises"]) == 2


def test_story_snapshot_restart_and_validation(client, course, database):
    session = start(client, STORY, source_kind="story", preview_draft=True)
    session = act(client, session, "story_visit", turn_id="drink-thanks")
    newer = deepcopy(course)
    newer.version = "99.0.0"
    next(s for s in newer.narratives if s.id == STORY).turns[0].text[0].surface = "Changed draft"
    with sessions(client.app.state.engine)() as db:
        import_content(db, newer)
    with TestClient(create_app(Config(database_url=database))) as restarted:
        saved = restarted.get("/api/v1/sessions/" + session["id"]).json()
        assert saved == session and saved["content_version"] == course.version
        saved = act(restarted, saved, "story_visit", turn_id="drink-aki")
        assert saved["story"]["current"]["text"][0]["surface"] == "水"
    for fields in [
        {"action": "story_visit"},
        {"action": "glossary"},
        {"action": "pause", "turn_id": "drink-aki"},
    ]:
        request = {
            "request_id": session["next_action_id"],
            "expected_revision": session["revision"],
            **fields,
        }
        assert (
            client.post("/api/v1/sessions/" + session["id"] + "/actions", json=request).status_code
            == 422
        )
    lesson = start(client)
    response = client.post(
        "/api/v1/sessions/" + lesson["id"] + "/actions", json=action_body(lesson, "show_readings")
    )
    assert response.status_code == 422


def test_reading_context_contrasts_and_all_authored_keys(course):
    from app.grading import grade
    from app.services import DomainError

    for exercise in course.practice_exercises:
        if exercise.type == "speaking":
            assert exercise.audio[0].transcript.strip()
            with pytest.raises(DomainError) as error:
                grade(exercise, exercise.audio[0].transcript)
            assert error.value.code == "speech_unassessed"
        else:
            answer = (
                exercise.answer
                if exercise.type
                in {
                    "multiple_choice",
                    "response_selection",
                    "listening_selection",
                    "audio_contrast",
                }
                else exercise.answers[0]
            )
            assert grade(exercise, answer)
    assert {story.id for story in course.narratives if story.kind == "story"} == {
        "ja-story-first-meeting",
        STORY,
    }
    words = {word.surface: word.reading for word in course.vocabulary}
    assert words["日本"] == "にほん" and words["日曜日"] == "にちようび"
    assert next(entry for entry in course.characters if entry.surface == "ー").form == "mark"


def test_glossary_support_is_retained_when_visible_on_later_turns(client):
    session = start(client, STORY, source_kind="story", preview_draft=True, mode="unassisted")
    session = act(client, session, "glossary", vocabulary_id="ja-word-tea")
    assert session["mode"] == "supported"
    # Revealed glossary remains available; jumping or answering later must not erase assistance.
    session = act(client, session, "answer", "ja-story-drink-tea", answer="c2")
    assert session["evidence"]["ja-story-drink-tea"]["first_assisted"]
    session = act(client, session, "story_visit", turn_id="drink-haru")
    assert "drink-haru" in session["story"]["assisted_turn_ids"]
    assert session["evidence"]["ja-story-drink-tea"]["assisted"]
    assert session["assessed_count"] == 0


@pytest.mark.parametrize(
    "passage_id,exercise_id,correct,wrong",
    [
        ("ja-passage-menu", "ja-passage-menu-price", "c2", "c0"),
        ("ja-passage-message", "ja-passage-message-when", "c0", "c1"),
    ],
)
def test_menu_and_message_passages_reuse_reading_checks_and_glossary(
    client, passage_id, exercise_id, correct, wrong
):
    session = start(client, passage_id, source_kind="story", preview_draft=True)
    assert session["preview_draft"] and session["kind"] == "reading"
    assert session["story"]["current"]["exercise_ids"] == [exercise_id]
    assert not {"answer", "answers", "hint", "explanation"} & session["exercises"][0].keys()
    session = act(client, session, "answer", exercise_id, answer=wrong)
    assert session["feedback"]["kind"] == "incorrect"
    session = act(client, session, "glossary", vocabulary_id="ja-word-tea")
    assert (
        next(word for word in session["story"]["glossary"] if word["id"] == "ja-word-tea")["gloss"]
        == "tea"
    )
    session = act(client, session, "answer", exercise_id, answer=correct)
    assert session["feedback"]["kind"] == "correct"
    assert session["evidence"][exercise_id]["assisted"]
    assert session["evidence"][exercise_id]["first_correct"] is False
    assert act(client, session, "finish")["xp_awarded"] == 5
