from pathlib import Path

from alembic import context

from app import audio_models, learning_models, models, reading_models, review_models, writing_models  # noqa: F401
from app.config import Config
from app.db import Base, make_engine

url = Config().database_url
if not url.endswith(":memory:"):
    Path(url.removeprefix("sqlite:///")).parent.mkdir(parents=True, exist_ok=True)
if context.is_offline_mode():
    context.configure(url=url, target_metadata=Base.metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()
else:
    engine = make_engine(url)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()
    engine.dispose()
