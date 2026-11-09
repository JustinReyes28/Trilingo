import logging

import uvicorn

from app.config import Config

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    config = Config()
    uvicorn.run("app.main:app", host=config.host, port=config.port)
