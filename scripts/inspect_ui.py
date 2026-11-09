import json
import os
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
from qa_helpers import qa_api, api_matches

ROOT = Path(__file__).resolve().parents[1]
BASE = os.environ.get("TRILINGO_UI_URL", "http://127.0.0.1:5173")
output = ROOT / "artifacts" / "screenshots"
output.mkdir(parents=True, exist_ok=True)
QA_API = qa_api()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.route("**/*", lambda route: route.continue_() if urlparse(route.request.url).hostname in {"127.0.0.1", "localhost"} and api_matches(route.request.url, QA_API) else route.abort())
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(BASE)
    page.wait_for_load_state("networkidle")
    print(page.locator("body").inner_text())
    (ROOT / "artifacts" / "learn-rendered.html").write_text(page.content(), encoding="utf-8")
    results = []
    for width in [320, 390, 768, 1440]:
        page.set_viewport_size({"width": width, "height": 900})
        page.screenshot(path=str(output / f"learn-{width}.png"), full_page=True)
        results.append({"width": width, "overflow": page.evaluate("document.documentElement.scrollWidth > innerWidth")})
    print(json.dumps({"layouts": results, "errors": errors}))
    browser.close()
