import json
import os
from urllib.parse import urlparse
from urllib.request import urlopen


def qa_api() -> str:
    base = os.environ.get("TRILINGO_QA_API_BASE_URL", "http://127.0.0.1:8002/api/v1").rstrip("/")
    if urlparse(base).hostname not in {"127.0.0.1", "localhost"}:
        raise RuntimeError("Browser QA only supports a loopback API")
    with urlopen(base + "/health", timeout=5) as response:
        health = json.load(response)
    if not health.get("qa_mode"):
        raise RuntimeError("Refusing browser QA: start a backend with QA_MODE=true and a disposable DB")
    return base


def api_matches(url: str, expected: str) -> bool:
    parsed = urlparse(url)
    return "/api/v1/" not in parsed.path or parsed.netloc == urlparse(expected).netloc
