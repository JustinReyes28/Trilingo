"""Focused speaking/fallback UI QA using a disposable QA app and bundled audio pack."""

import argparse
import json
import os
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
    if urlparse(args.base).hostname not in {"127.0.0.1", "localhost"}:
        raise RuntimeError("Use a loopback QA frontend")
    os.environ["TRILINGO_QA_API_BASE_URL"] = args.api
    api = qa_api()
    output = Path(__file__).resolve().parents[1] / "artifacts/plan-9-2-speaking"
    output.mkdir(parents=True, exist_ok=True)
    layouts, errors, external = [], [], []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        )
        context = browser.new_context(viewport={"width": 390, "height": 900})
        def local_only(route):
            if urlparse(route.request.url).hostname in {"127.0.0.1", "localhost"} and api_matches(route.request.url, api):
                route.continue_()
            else:
                external.append(route.request.url)
                route.abort()
        context.route("**/*", local_only)
        page = context.new_page()
        page.set_default_timeout(12000)
        page.on("pageerror", lambda error: errors.append(str(error)))
        def call(method, path, data=None):
            response = context.request.fetch(api + path, method=method, data=data)
            assert response.ok, (path, response.status, response.text())
            return response.json()
        def capture(label, target=None):
            for width in (320, 390, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                assert not page.evaluate("document.documentElement.scrollWidth > innerWidth"), (label, width)
                if target is None:
                    page.screenshot(path=str(output / f"{label}-{width}.png"), full_page=True)
                else:
                    target.screenshot(path=str(output / f"{label}-{width}.png"))
                layouts.append({"surface": label, "width": width, "overflow": False})
            page.set_viewport_size({"width": 390, "height": 900})
        baseline = call("GET", "/personal")["skill_evidence"].get("speaking", {}).get("typed_fallbacks", 0)
        health = call("GET", "/health")
        assert health["schema_version"] == "0015" and health["features"] == {"lessons": True}
        audio_pack = call("GET", "/audio/status")["audio_pack"]
        call("PATCH", "/settings", {"show_statistics": True, "show_quests": True})
        page.goto(args.base + "/#grammar")
        page.get_by_label("Show unreviewed draft guides and scenarios").check()
        scene = page.locator(".scenario-row").filter(has=page.get_by_role("heading", name="Ordering a drink", exact=True))
        expect(scene.get_by_role("button", name="Practice spoken responses")).to_be_visible()
        scene.get_by_role("button", name="Practice spoken responses").click()
        page.wait_for_url("**/#session/*")
        session_id = page.url.split("#session/")[1]
        expect(page.get_by_text("水をください。", exact=True)).to_be_visible()
        page.get_by_text("Typed practice", exact=True).click()
        typed = page.get_by_label("Typed practice · no speech assessed", exact=True)
        typed.focus()
        typed.dispatch_event("compositionstart")
        typed.fill("水をください。")
        expect(page.get_by_role("button", name="Save typed practice", exact=True)).to_be_disabled()
        typed.press("Enter")
        assert call("GET", f"/sessions/{session_id}")["revision"] == 0
        typed.dispatch_event("compositionend")
        typed.fill("水をください。")
        capture("speaking-typed")
        page.get_by_role("button", name="Prepare model response", exact=True).click()
        if audio_pack["bundled_reference"]:
            expect(page.get_by_label("model response", exact=True)).to_be_visible()
        else:
            expect(page.get_by_role("alert")).to_contain_text("unavailable")
        page.get_by_role("button", name="Save typed practice", exact=True).click()
        expect(page.get_by_text("Typed practice saved.", exact=False)).to_be_visible()
        page.get_by_role("button", name="Pause and leave", exact=True).click()
        page.wait_for_url("**/#learn")
        page.goto(args.base + "/#session/" + session_id)
        expect(page.get_by_role("button", name="Resume study", exact=True)).to_be_visible()
        page.get_by_role("button", name="Resume study", exact=True).click()
        page.get_by_role("button", name="Continue", exact=True).click()
        page.get_by_role("button", name="Skip prompt", exact=True).click()
        page.get_by_role("button", name="Finish and save session", exact=True).click()
        expect(page.get_by_role("heading", name="Session saved", exact=True)).to_be_visible()
        saved = call("GET", f"/sessions/{session_id}")
        assert saved["xp_awarded"] == 5 and saved["assessed_count"] == 0
        page.get_by_role("button", name="Start a new replay", exact=True).click()
        page.wait_for_url(lambda url: "#session/" in url and not url.endswith(session_id))
        expect(page.get_by_text("0 saved typed practice responses", exact=False)).to_be_visible()
        rejected = context.request.post(
            api + "/quests",
            data={"request_id": str(uuid4()), "kind": "speaking", "target": 3},
        )
        assert rejected.status == 422
        page.goto(args.base + "/#review")
        page.get_by_role("combobox", name="Practice to notice", exact=True).select_option("listening")
        page.get_by_role("button", name="Add personal quest", exact=True).click()
        expect(page.get_by_text("listening: 0 / 3", exact=False)).to_be_visible()
        page.get_by_text("Evidence by skill", exact=True).click()
        expect(
            page.get_by_text(
                f"{baseline + 1} typed practice responses (pronunciation unassessed)",
                exact=False,
            )
        ).to_be_visible()
        capture("speaking-records")
        page.get_by_role(
            "button",
            name="Audio unavailable · switch this quest to core sessions",
            exact=True,
        ).first.click()
        expect(page.get_by_text("Changed from listening to sessions.", exact=False)).to_be_visible()
        page.goto(args.base + "/#grammar")
        page.get_by_label("Show unreviewed draft guides and scenarios").check()
        scene = page.locator(".scenario-row").filter(has=page.get_by_role("heading", name="Ordering a drink", exact=True))
        expect(scene.get_by_text("Optional local AI scenario coaching", exact=False)).to_have_count(0)
        assert not errors, errors
        assert not external, external
        browser.close()
    report = {
        "layouts": layouts,
        "errors": errors,
        "external_requests": external,
        "audio_pack": audio_pack,
        "providers": "Zero runtime AI, STT, microphone capture, or TTS providers (schema 0015)",
    }
    (output / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"layouts": len(layouts), "errors": errors, "external": external}))


if __name__ == "__main__":
    main()
