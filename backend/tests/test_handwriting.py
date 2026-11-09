from copy import deepcopy
from uuid import uuid4

import pytest
from sqlalchemy import func, select
from test_learning import course as course

from app.db import sessions
from app.services import import_content
from app.writing_models import DrawingSample, WritingEvent

pytestmark = pytest.mark.usefixtures("course")
BASE = "/api/v1/courses/ja-starter/writing"
CHAR = "ja-char-hiragana-3044"


def guide(client):
    response = client.get(BASE + "/characters/" + CHAR + "?preview_draft=true")
    assert response.status_code == 200, response.text
    return response.json()


def body_for(client, **extra):
    data = guide(client)
    ticks = 0
    strokes = []
    for stroke in data["guide"]["strokes"]:
        points = []
        for point in stroke["points"]:
            ticks += 20
            points.append({**point, "t": ticks})
        strokes.append(points)
    return {
        "request_id": str(uuid4()),
        "character_id": CHAR,
        "preview_draft": True,
        "mode": "guided_trace",
        "strokes": strokes,
        "self_rating": "practiced",
        **extra,
    }


def test_original_draft_guide_identity_license_and_target_counts(client, course):
    assert client.get(BASE + "/characters/" + CHAR).status_code == 404
    data = guide(client)
    assert data["guide"]["status"] == "draft" and "review pending" in data["message"]
    assert data["guide"]["character_id"] == CHAR and len(data["guide"]["strokes"]) == 2
    assert data["license"]["license"] == "CC-BY-4.0"
    assert len([char for char in course.characters if char.stroke_asset_id]) == 6
    assert all(len(asset.sha256) == 64 for asset in course.assets if asset.kind == "stroke")


def test_trace_geometry_is_feedback_not_recognition_and_retry_rewards_once(client):
    body = body_for(client)
    first = client.post(BASE + "/handwriting", json=body)
    assert first.status_code == 200, first.text
    result = first.json()
    assert result["objective_correctness"] is None
    assert result["evidence"] == "self_reported_practice"
    assert "100%" in result["feedback"] and "not handwriting recognition" in result["feedback"]
    assert result["sample_id"] is None and result["xp_awarded"] == 5
    assert client.post(BASE + "/handwriting", json=body).json() == result
    for _ in range(3):
        assert (
            client.post(BASE + "/handwriting", json={**body, "request_id": str(uuid4())}).json()[
                "xp_awarded"
            ]
            == 5
        )
    assert client.get("/api/v1/progress").json()["total_xp"] == 20
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(DrawingSample)) == 0
        for event in db.scalars(select(WritingEvent)).all():
            assert event.request["strokes"] == [] and len(event.request["stroke_digest"]) == 64
            assert "strokes" not in event.response


def test_optional_sample_delete_removes_raw_strokes_but_retains_activity(client):
    body = body_for(client, keep_sample=True)
    result = client.post(BASE + "/handwriting", json=body).json()
    sample_id = result["sample_id"]
    stored = client.get("/api/v1/writing/samples").json()
    assert len(stored) == 1 and stored[0]["strokes"] == body["strokes"]
    assert stored[0]["id"] == sample_id
    for _ in range(2):
        assert client.delete("/api/v1/writing/samples/" + sample_id).json() == {"deleted": True}
    assert client.get("/api/v1/writing/samples").json() == []
    assert client.get("/api/v1/progress").json()["total_xp"] == 5
    assert client.post(BASE + "/handwriting", json=body).json() == result
    assert client.get("/api/v1/writing/samples").json() == []


def test_sequence_accessible_alternative_does_not_claim_handwriting(client):
    for sequence in ([1, 2], [2, 1]):
        body = body_for(client, mode="accessible_sequence", strokes=[], sequence=sequence)
        response = client.post(BASE + "/handwriting", json=body)
        assert response.status_code == 200, response.text
        result = response.json()
        assert result["mode"] == "accessible_sequence" and result["objective_correctness"] is None
        assert "does not measure handwriting" in result["feedback"]
        assert result["xp_awarded"] == 5
    incomplete = body_for(client, mode="accessible_sequence", strokes=[], sequence=[1])
    assert client.post(BASE + "/handwriting", json=incomplete).status_code == 422


def test_freehand_requires_honest_reference_self_check_and_never_grades(client):
    body = body_for(client, mode="freehand_self_check", reference_revealed=False)
    assert client.post(BASE + "/handwriting", json=body).status_code == 422
    body["reference_revealed"] = True
    result = client.post(BASE + "/handwriting", json=body).json()
    assert result["objective_correctness"] is None and result["self_rating"] == "practiced"
    assert "not assessed" in result["feedback"]


@pytest.mark.parametrize(
    "fault",
    ["coordinates", "time", "points", "empty", "fabricated_grade", "path", "sequence_sample"],
)
def test_invalid_strokes_and_fabricated_evidence_are_rejected(client, fault):
    body = body_for(client)
    if fault == "coordinates":
        body["strokes"][0][0]["x"] = 1.1
    elif fault == "time":
        body["strokes"][0][1]["t"] = 0
    elif fault == "points":
        body["strokes"] = [[{"x": 0.5, "y": 0.5, "t": i} for i in range(1201)]]
    elif fault == "empty":
        body["strokes"] = []
    elif fault == "fabricated_grade":
        body["is_correct"] = True
    elif fault == "path":
        body["sample_path"] = "../../personal.db"
    else:
        body.update(mode="accessible_sequence", strokes=[], sequence=[1, 2], keep_sample=True)
    assert client.post(BASE + "/handwriting", json=body).status_code == 422
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_missing_or_changed_asset_has_fallback_without_crashing_other_learning(client, course):
    newer = deepcopy(course)
    newer.version = "99.0.0"
    asset = next(
        asset
        for asset in newer.assets
        if asset.id == next(char for char in newer.characters if char.id == CHAR).stroke_asset_id
    )
    asset.path = "assets/strokes/missing-demo.json"
    with sessions(client.app.state.engine)() as db:
        import_content(db, newer)
    data = guide(client)
    assert data["guide"] is None and "remain available" in data["message"]
    body = {
        "request_id": str(uuid4()),
        "character_id": CHAR,
        "preview_draft": True,
        "mode": "freehand_self_check",
        "reference_revealed": True,
        "self_rating": "needs_practice",
        "strokes": [[{"x": 0.2, "y": 0.2, "t": 0}, {"x": 0.3, "y": 0.7, "t": 10}]],
    }
    assert client.post(BASE + "/handwriting", json=body).status_code == 200
    body.update(request_id=str(uuid4()), mode="guided_trace")
    assert client.post(BASE + "/handwriting", json=body).status_code == 409
    assert client.get("/api/v1/courses/ja-starter/map").status_code == 200
