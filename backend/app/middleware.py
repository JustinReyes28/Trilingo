from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Message, Receive, Scope, Send


class RequestBodyLimit:
    """Bound JSON requests before validation or any database mutation."""

    def __init__(self, app: ASGIApp, limit: int = 65536):
        self.app = app
        self.limit = limit

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope["method"] not in {"POST", "PATCH", "PUT"}:
            await self.app(scope, receive, send)
            return
        if scope["path"] in {"/api/v1/backup/preview", "/api/v1/backup/restore"}:
            limit = 50_000_000
        else:
            limit = self.limit
        parts = []
        size = 0
        while True:
            message = await receive()
            if message["type"] == "http.disconnect":
                return
            body = message.get("body", b"")
            size += len(body)
            if size > limit:
                response = JSONResponse(
                    status_code=413,
                    content={
                        "error": {
                            "code": "request_too_large",
                            "message": "This request is too large. Reduce the input and retry.",
                        }
                    },
                )
                await response(scope, receive, send)
                return
            parts.append(body)
            if not message.get("more_body", False):
                break
        delivered = False

        async def replay() -> Message:
            nonlocal delivered
            if not delivered:
                delivered = True
                return {"type": "http.request", "body": b"".join(parts), "more_body": False}
            return await receive()

        await self.app(scope, replay, send)
