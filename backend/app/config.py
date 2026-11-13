from pathlib import Path
from urllib.parse import urlsplit

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT / ".env", extra="ignore")
    database_url: str = f"sqlite:///{(ROOT / '.data' / 'trilingo.db').as_posix()}"
    cors_origins: list[str] = ["http://127.0.0.1:5173", "http://localhost:5173"]
    audio_pack_dir: Path = ROOT / "content" / "audio"
    audio_pack_enabled: bool = True
    backups_dir: Path = ROOT / ".data" / "backups"
    qa_mode: bool = False
    ai_enabled: bool = False
    stt_enabled: bool = False
    host: str = "127.0.0.1"
    port: int = Field(default=8000, ge=1, le=65535)

    @field_validator("audio_pack_dir", "backups_dir")
    @classmethod
    def local_directory_path(cls, value: Path) -> Path:
        return value if value.is_absolute() else ROOT / value

    @field_validator("host")
    @classmethod
    def loopback_host(cls, value: str) -> str:
        if value not in {"127.0.0.1", "localhost"}:
            raise ValueError("Bind local services to loopback")
        return value

    @field_validator("database_url")
    @classmethod
    def local_database(cls, value: str) -> str:
        if not value.startswith("sqlite:///"):
            raise ValueError("This local release requires a SQLite database URL")
        if value != "sqlite:///:memory:":
            database_path = Path(value.removeprefix("sqlite:///"))
            if not database_path.is_absolute():
                value = "sqlite:///" + (ROOT / database_path).as_posix()
        return value

    @field_validator("cors_origins")
    @classmethod
    def local_origins(cls, values: list[str]) -> list[str]:
        for value in values:
            parsed = urlsplit(value)
            if parsed.hostname not in {"localhost", "127.0.0.1", "::1"} or parsed.scheme != "http":
                raise ValueError("CORS origins must be explicit local HTTP origins")
        return values

    @model_validator(mode="after")
    def isolated_qa_database(self):
        if self.qa_mode:
            actual = Path(self.database_url.removeprefix("sqlite:///")).resolve()
            personal = (ROOT / ".data" / "trilingo.db").resolve()
            if actual == personal:
                raise ValueError("QA mode requires a separate disposable database")
        return self
