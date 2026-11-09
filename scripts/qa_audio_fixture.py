"""Explicit local test-tone fixture. This never verifies Japanese TTS or STT."""

import argparse
import io
import json
import math
import struct
import wave
from http.server import BaseHTTPRequestHandler, HTTPServer


def tone() -> bytes:
    output = io.BytesIO()
    with wave.open(output, "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(16000)
        audio.writeframes(
            b"".join(struct.pack("<h", int(1800 * math.sin(i / 8))) for i in range(4000))
        )
    return output.getvalue()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path != "/v1/audio/voices":
            self.send_error(404)
            return
        data = json.dumps({"voices": [{"id": "jf_alpha"}, {"id": "af_heart"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self) -> None:
        if self.path != "/v1/audio/speech":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400)
            return
        if not 0 < length <= 16384:
            self.send_error(413)
            return
        self.rfile.read(length)
        self.send_response(200)
        self.send_header("Content-Type", "audio/wav")
        self.end_headers()
        self.wfile.write(tone())

    def log_message(self, format: str, *args: object) -> None:
        pass  # Fixture requests contain private learning text; do not echo them.


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=18179)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("Choose a valid local port")
    print(
        "QA fixture: non-linguistic test tones only. No Japanese speech verification.", flush=True
    )
    HTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
