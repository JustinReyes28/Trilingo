import argparse
import json
from pathlib import Path

from app.config import ROOT, Config
from app.db import make_engine, sessions
from app.services import import_content, load_content


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate/import content without resetting progress"
    )
    parser.add_argument("command", choices=["validate", "import"])
    parser.add_argument(
        "file", nargs="?", type=Path, default=ROOT / "content/courses/ja/starter.json"
    )
    args = parser.parse_args()
    content = load_content(args.file)
    lessons = [
        lesson
        for u in content.units
        for lesson in u.lessons
        if lesson.status == u.status == "published"
    ]
    report = {
        "course": content.id,
        "version": content.version,
        "published_lessons": len(lessons),
        "exercises": sum(len(lesson.exercises) for lesson in lessons),
        "unique_words": len(
            {v.id for v in content.vocabulary if v.status == "published" and v.entry_kind == "word"}
        ),
        "phrases": sum(
            v.status == "published" and v.entry_kind == "phrase" for v in content.vocabulary
        ),
        "coverage": "partial starter slice; not full A-B",
    }
    if args.command == "import":
        engine = make_engine(Config().database_url)
        with sessions(engine)() as db:
            report["imported_new_version"] = import_content(db, content)
        engine.dispose()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
