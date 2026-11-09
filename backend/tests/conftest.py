from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient

from app.config import Config
from app.main import create_app


@pytest.fixture
def database(tmp_path: Path, monkeypatch):
    url = f"sqlite:///{(tmp_path / 'isolated.db').as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    alembic = AlembicConfig("alembic.ini")
    command.upgrade(alembic, "head")
    return url


@pytest.fixture
def client(database):
    app = create_app(Config(database_url=database))
    with TestClient(app) as client:
        yield client
