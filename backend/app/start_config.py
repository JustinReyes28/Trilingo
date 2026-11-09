import json

from app.config import Config

if __name__ == "__main__":
    config = Config()
    print(json.dumps({"host": config.host, "port": config.port}))
