"""Run an isolated phase 7–9 backend. Never migrates or imports the learner database."""

import argparse
import os
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--disable-audio-pack",
        action="store_true",
        help="Set AUDIO_PACK_ENABLED=false to test 503 audio_unavailable fallback",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    database = root / ".tools" / "phase789-isolated.db"
    database.parent.mkdir(parents=True, exist_ok=True)
    os.environ.update(
        {
            "DATABASE_URL": "sqlite:///" + database.as_posix(),
            "QA_MODE": "true",
            "PORT": "8017",
            "AUDIO_PACK_ENABLED": "false" if args.disable_audio_pack else "true",
            "CORS_ORIGINS": '["http://127.0.0.1:5187"]',
        }
    )
    sys.path.insert(0, str(root / "backend"))
    import uvicorn
    from alembic import command
    from alembic.config import Config as AlembicConfig
    from app.config import Config
    from app.db import make_engine, sessions
    from app.main import create_app
    from app.services import import_content, load_content

    configuration = Config()
    assert configuration.qa_mode
    assert configuration.database_url != "sqlite:///" + (root / ".data" / "trilingo.db").as_posix()
    migration = AlembicConfig(str(root / "backend" / "alembic.ini"))
    command.upgrade(migration, "head")
    command.check(migration)
    engine = make_engine(configuration.database_url)
    with sessions(engine)() as db:
        import_content(db, load_content(root / "content/courses/ja/starter.json"))
    engine.dispose()
    print("Isolated QA database: " + str(database), flush=True)
    uvicorn.run(create_app(configuration), host="127.0.0.1", port=8017)


if __name__ == "__main__":
    main()
