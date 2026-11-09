import os
import shutil
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient

from app.config import ROOT, Config
from app.main import create_app


@pytest.fixture(scope="session")
def _migrated_template_db(tmp_path_factory: pytest.TempPathFactory) -> Path:
    temp_dir = tmp_path_factory.mktemp("db_template")
    template_path = temp_dir / "template.db"
    url = f"sqlite:///{template_path.as_posix()}"
    old_env = os.environ.get("DATABASE_URL")
    os.environ["DATABASE_URL"] = url
    try:
        ini_path = str(ROOT / "backend" / "alembic.ini")
        alembic = AlembicConfig(ini_path if Path(ini_path).is_file() else "alembic.ini")
        command.upgrade(alembic, "head")
    finally:
        if old_env is not None:
            os.environ["DATABASE_URL"] = old_env
        else:
            os.environ.pop("DATABASE_URL", None)
    return template_path


@pytest.fixture
def database(tmp_path: Path, monkeypatch, _migrated_template_db: Path) -> str:
    target = tmp_path / "isolated.db"
    shutil.copyfile(_migrated_template_db, target)
    url = f"sqlite:///{target.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    return url


@pytest.fixture
def client(database):
    app = create_app(Config(database_url=database))
    with TestClient(app) as client:
        yield client
