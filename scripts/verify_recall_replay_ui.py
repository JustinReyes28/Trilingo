"""Verify completed recall replay with installed Edge and disposable loopback QA.

No browser installation, provider call, or external file transfer is performed.
"""

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright
from qa_helpers import api_matches, qa_api


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="http://127.0.0.1:5192")
    parser.add_argument("--api", default="http://127.0.0.1:8022/api/v1")
    args = parser.parse_args()
    if urlparse(args.base).hostname not in {"localhost", "127.0.0.1"}:
        raise RuntimeError("Use a loopback QA frontend")
    os.environ["TRILINGO_QA_API_BASE_URL"] = args.api
    api = qa_api()
    output = Path(__file__).resolve().parents[1] / "artifacts/recall-replay-extension-20261025"
    output.mkdir(parents=True, exist_ok=True)
    errors, external, unsupported, layouts = [], [], [], []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
            args=[
                "--disable-background-networking",
                "--disable-component-update",
                "--no-first-run",
            ],
        )
        context = browser.new_context(viewport={"width": 390, "height": 900})

        def local_only(route):
            parsed = urlparse(route.request.url)
            if (
                parsed.hostname in {"127.0.0.1", "localhost"}
                and parsed.port in {urlparse(args.base).port, urlparse(api).port}
                and api_matches(route.request.url, api)
            ):
                route.continue_()
            else:
                external.append(route.request.url)
                route.abort()

        context.route("**/*", local_only)
        page = context.new_page()
        page.set_default_timeout(15000)
        page.on("pageerror", lambda error: errors.append(str(error)))

        def track_start(request):
            if request.method == "POST" and request.url.endswith("/courses/ja-starter/sessions"):
                if request.post_data_json.get("source_kind") == "review":
                    unsupported.append(request.post_data_json)

        page.on("request", track_start)

        def call(method, path, data=None):
            response = context.request.fetch(api + path, method=method, data=data)
            assert response.ok, (path, response.status, response.text())
            return response.json()

        def capture(label, locator):
            for width in (320, 390, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                locator.scroll_into_view_if_needed()
                assert not page.evaluate("document.documentElement.scrollWidth > innerWidth"), (
                    label,
                    width,
                )
                page.screenshot(path=str(output / f"{label}-{width}.png"))
                layouts.append({"screen": label, "width": width, "overflow": False})
            page.set_viewport_size({"width": 390, "height": 900})

        health = call("GET", "/health")
        assert health["qa_mode"] and not any(
            health["features"][key] for key in ("ai", "tts", "stt")
        )
        version = call("GET", "/courses/ja-starter")["version"]
        assert call("GET", "/progress")["total_xp"] == 0, "Use a new disposable QA DB"
        card = call(
            "POST",
            "/courses/ja-starter/review/cards",
            {"item_id": "ja-word-school", "direction": "reading"},
        )
        timer = call("POST", f"/review/cards/{card['id']}/session", {"request_id": str(uuid4())})
        card = call(
            "POST",
            f"/review/cards/{card['id']}/ratings",
            {
                "request_id": str(uuid4()),
                "expected_revision": card["revision"],
                "rating": "Easy",
                "recall_session_id": timer["id"],
            },
        )
        assert datetime.fromisoformat(card["due"]) > datetime.now(timezone.utc)
        saved = call("GET", f"/sessions/{timer['id']}")
        assert saved["status"] == "completed" and saved["xp_awarded"] == 5
        page.goto(args.base + "/#session/" + timer["id"])
        expect(page.get_by_role("heading", name="Session saved", exact=True)).to_be_visible()
        completion = page.locator(".completion-panel")
        expect(completion).to_contain_text("Self-rated recall saved.")
        expect(completion).not_to_contain_text("unassisted checks")
        expect(page.get_by_role("button", name="Start a new replay", exact=True)).to_have_count(0)
        replay = page.get_by_role("link", name="Review this card again", exact=True)
        expect(replay).to_have_attribute("href", "#review?session=" + timer["id"])
        replay.focus()
        expect(replay).to_be_focused()
        capture("recall-completed", completion)
        replay.press("Enter")
        page.wait_for_url("**/#review?session=" + timer["id"])
        sheet = page.locator(".recall-sheet")
        expect(sheet.get_by_role("heading", name=card["prompt"], exact=True)).to_be_visible()
        expect(sheet).to_contain_text("reading")
        expect(sheet).to_contain_text("Saved content " + card["content_version"])
        expect(
            sheet.get_by_role("button", name="Start optional recall timer", exact=True)
        ).to_be_visible()
        capture("same-card-early-replay", sheet)

        def rate_from_ui(rating):
            sheet.get_by_role("button", name="Reveal answer", exact=True).click()
            button = sheet.get_by_role("button", name=rating, exact=True)
            button.focus()
            with page.expect_response(
                lambda response: (
                    response.request.method == "POST"
                    and response.url == api + f"/review/cards/{card['id']}/ratings"
                )
            ) as pending:
                button.press("Enter")
            response = pending.value
            assert response.ok, response.text()
            expect(page.get_by_role("status").filter(has_text="Review saved.")).to_be_visible()
            result, body = response.json(), response.request.post_data_json
            assert call("POST", f"/review/cards/{card['id']}/ratings", body) == result
            return result, body

        early, early_body = rate_from_ui("Good")
        assert "recall_session_id" not in early_body, "Completed timer must not be reused"
        assert early["id"] == card["id"] and early["direction"] == card["direction"]
        assert early["content_version"] == card["content_version"]
        assert early["revision"] == card["revision"] + 1
        assert call("GET", "/progress")["total_xp"] == 10
        with page.expect_response(
            lambda response: (
                response.request.method == "POST"
                and response.url == api + f"/review/cards/{card['id']}/session"
            )
        ) as pending:
            sheet.get_by_role("button", name="Start optional recall timer", exact=True).click()
        new_timer = pending.value.json()
        assert pending.value.ok and new_timer["id"] != timer["id"]
        final_card, final_body = rate_from_ui("Hard")
        assert final_body["recall_session_id"] == new_timer["id"]
        assert final_card["revision"] == early["revision"] + 1
        assert call("GET", f"/sessions/{new_timer['id']}")["status"] == "completed"
        assert call("GET", "/progress")["total_xp"] == 15
        sheet.get_by_role("button", name="Skip card · keep schedule", exact=True).click()
        expect(sheet).to_have_count(0)
        assert call("GET", f"/review/cards/{card['id']}") == final_card
        assert call("GET", "/progress")["total_xp"] == 15
        personal = call("GET", "/personal")
        assert personal["review_count"] == 3 and personal["objective_checks"] == 0
        assert len(call("GET", f"/review/cards/{card['id']}/history")) == 3
        assert not errors and not external and not unsupported, (errors, external, unsupported)
        result = {
            "status": "pass",
            "content_version": version,
            "qa_mode": True,
            "card_id": card["id"],
            "direction": card["direction"],
            "source_content_version": card["content_version"],
            "completed_session_id": timer["id"],
            "new_timer_session_id": new_timer["id"],
            "keyboard_replay_and_ratings": True,
            "layouts": layouts,
            "same_card_early_review": True,
            "exact_rating_retries_idempotent": True,
            "completed_timer_not_reused": True,
            "new_timer_completes": True,
            "skip_preserves_card_and_xp": True,
            "total_xp": 15,
            "review_count": 3,
            "objective_checks": 0,
            "unsupported_review_start_requests": unsupported,
            "javascript_errors": errors,
            "external_page_requests": external,
            "limitations": ["Physical IME/screen reader/touch and human/provider audio unverified"],
        }
        (output / "report.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(json.dumps(result, ensure_ascii=False))
        browser.close()


if __name__ == "__main__":
    main()
