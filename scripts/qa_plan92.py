"""Run Plan 9.2 QA using separate ports and database; uses bundled MP3 pack only."""

import argparse
import os
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=Path(".tools/plan-9-2-qa.db"))
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    database = (root / args.database).resolve()
    if not database.is_relative_to((root / ".tools").resolve()):
        parser.error("QA databases must stay inside this project's .tools directory")
    database.parent.mkdir(parents=True, exist_ok=True)
    os.environ.update(
        {
            "DATABASE_URL": "sqlite:///" + database.as_posix(),
            "QA_MODE": "true",
            "PORT": "8022",
            "AUDIO_PACK_ENABLED": "true",
            "CORS_ORIGINS": '["http://127.0.0.1:5192"]',
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

    migration = AlembicConfig(str(root / "backend/alembic.ini"))
    command.upgrade(migration, "head")
    command.check(migration)
    engine = make_engine(Config().database_url)
    with sessions(engine)() as db:
        content = load_content(root / "content/courses/ja/starter.json")
        first = import_content(db, content)
        assert not import_content(db, content)
    engine.dispose()
    print("Isolated Plan 9.2 QA database: " + str(database), flush=True)
    print(f"Content {content.version}; first import new={first}; repeat import new=False", flush=True)
    if args.check_only:
        return
    uvicorn.run(create_app(Config()), host="127.0.0.1", port=8022)


if __name__ == "__main__":
    main()
