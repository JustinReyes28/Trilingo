"""Focused five-direction collection recall QA with providers disabled."""

import json
import os
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright
from qa_helpers import api_matches, qa_api


def main() -> None:
    api = os.environ.get("TRILINGO_QA_API_BASE_URL", "http://127.0.0.1:8022/api/v1")
    os.environ["TRILINGO_QA_API_BASE_URL"] = api
    qa_api()
    output = Path(__file__).resolve().parents[1] / "artifacts/plan-9-2-audio-recall"
    output.mkdir(parents=True, exist_ok=True)
    layouts, errors = [], []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
        context = browser.new_context(viewport={"width": 390, "height": 900})
        def local_only(route):
            assert urlparse(route.request.url).hostname in {"127.0.0.1", "localhost"}
            assert api_matches(route.request.url, api)
            route.continue_()
        context.route("**/*", local_only)
        context.add_init_script("navigator.mediaDevices.getUserMedia=()=>Promise.reject(new DOMException('Microphone denied in recall QA','NotAllowedError'))")
        page = context.new_page()
        page.set_default_timeout(12000)
        page.on("pageerror", lambda error: errors.append(str(error)))
        def call(method, path, data=None):
            response = context.request.fetch(api + path, method=method, data=data)
            assert response.ok, (path, response.status, response.text())
            return response.json()
        def capture(label):
            for width in (320, 390, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                assert not page.evaluate("document.documentElement.scrollWidth > innerWidth"), (label, width)
                page.locator(".recall-sheet").screenshot(path=str(output / f"{label}-{width}.png"))
                layouts.append({"surface": label, "width": width, "overflow": False})
            page.set_viewport_size({"width": 390, "height": 900})
        baseline = call("GET", "/progress")["total_xp"]
        assert call("GET", "/health")["schema_version"] == "0013"
        assert not any(call("GET", "/health")["features"][kind] for kind in ("ai", "tts", "stt"))
        collection = call("POST", "/courses/ja-starter/collections", {"request_id": str(uuid4()), "name": "Audio recall QA " + str(uuid4())[:6]})
        for word in ("ja-word-hello", "ja-word-school"):
            call("PATCH", f"/collections/{collection['id']}/members", {"item_id": word, "saved": True})
        page.goto("http://127.0.0.1:5192/#review")
        page.get_by_text("Personal vocabulary collections", exact=True).click()
        page.get_by_role("combobox", name="Choose a collection", exact=True).select_option(collection["id"])
        page.get_by_role("button", name="Open collection recall", exact=True).click()
        page.get_by_label("Cards per batch", exact=True).fill("1")
        page.get_by_role("combobox", name="Recall direction", exact=True).select_option("listening")
        rows = page.locator(".grammar-layout > section > ul.session-list > li")
        expect(rows).to_have_count(1)
        page.get_by_role("button", name="Show all", exact=True).click()
        expect(rows).to_have_count(2)
        rows.first.get_by_role("button", name="Review now", exact=True).click()
        sheet = page.locator(".recall-sheet")
        expect(sheet.get_by_role("heading", name="Listen, then recall the meaning.", exact=False)).to_be_visible()
        expect(sheet.locator(".recall-answer")).to_have_count(0)
        expect(sheet.locator(".dialog-japanese")).to_have_count(0)
        capture("collection-listening")
        sheet.get_by_role("button", name="Prepare saved word reference", exact=True).click()
        expect(sheet.get_by_role("alert")).to_contain_text("disabled")
        sheet.get_by_role("button", name="Use text alternative", exact=True).click()
        expect(sheet.locator(".dialog-japanese")).to_be_visible()
        assert sheet.locator(".dialog-japanese").get_attribute("lang") == "ja"
        assert sheet.locator(".recall-answer").get_attribute("lang") == "en"
        capture("collection-listening-fallback")
        assert call("GET", "/progress")["total_xp"] == baseline
        sheet.get_by_role("button", name="Good", exact=True).click()
        expect(sheet.get_by_role("button", name="Reveal answer", exact=True)).to_be_visible()
        assert call("GET", "/progress")["total_xp"] == baseline + 5
        page.get_by_role("combobox", name="Recall direction", exact=True).select_option("speaking")
        expect(rows).to_have_count(1)
        rows.first.get_by_role("button", name="Review now", exact=True).click()
        sheet.get_by_text("Try a spoken recall", exact=True).click()
        sheet.get_by_role("button", name="Record microphone", exact=True).click()
        expect(sheet.get_by_role("alert")).to_contain_text("Microphone denied in recall QA")
        capture("collection-speaking-fallback")
        sheet.get_by_role("button", name="Skip card · keep schedule", exact=True).click()
        assert call("GET", "/progress")["total_xp"] == baseline + 5
        prepared = call("POST", f"/collections/{collection['id']}/recall", {"direction": "speaking"})
        assert all(not item["scheduled"] for item in prepared["cards"])
        assert not errors, errors
        browser.close()
    (output / "report.json").write_text(json.dumps({"layouts": layouts, "errors": errors, "providers": "disabled", "microphone": "emulated denial only"}, indent=2), encoding="utf-8")
    print(json.dumps({"layouts": len(layouts), "errors": errors}))


if __name__ == "__main__":
    main()
