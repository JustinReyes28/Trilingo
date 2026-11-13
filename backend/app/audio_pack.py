"""Versioned, pre-generated audio pack lookup.

The pack is authored content, never learner data. A hit works with every
runtime provider disabled; a miss falls back cleanly to UI text/transcript
alternatives.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path, PurePosixPath
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from app.config import Config

logger = logging.getLogger("trilingo.audio_pack")

PACK_FORMAT_VERSION = 1
MAX_CLIP_BYTES = 1_000_000
MAX_MANIFEST_BYTES = 50_000_000
MAX_CLIP_SECONDS = 60.0
COURSE_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,99}$")


class PackEngine(BaseModel):
    model_config = ConfigDict(extra="forbid")
    provider: Literal["kokoro"] = "kokoro"
    model: str = Field(min_length=1, max_length=150)
    voice_ja: str = Field(min_length=1, max_length=100)
    voice_en: str = Field(min_length=1, max_length=100)
    format: Literal["mp3"] = "mp3"
    sample_rate: int = Field(default=24000, ge=8000, le=48000)
    bitrate_kbps: int = Field(default=64, ge=32, le=320)


class PackLicense(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = Field(min_length=1, max_length=100)
    source: str = Field(min_length=1, max_length=500)
    license: str = Field(min_length=1, max_length=100)
    attribution: str = Field(min_length=1, max_length=1000)


class PackItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    key: str = Field(pattern=r"^[0-9a-f]{64}$")
    kind: Literal["word", "cue", "turn", "gloss"]
    item_id: str = Field(min_length=1, max_length=100)
    cue_id: str | None = Field(default=None, max_length=100)
    turn_id: str | None = Field(default=None, max_length=100)
    language: Literal["ja", "en"]
    text: str = Field(min_length=1, max_length=500)
    pronunciation_override: str | None = Field(default=None, min_length=1, max_length=500)
    file: str = Field(min_length=1, max_length=200)
    bytes: int = Field(ge=1, le=MAX_CLIP_BYTES)
    duration_seconds: float = Field(gt=0, le=MAX_CLIP_SECONDS)
    file_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")

    @field_validator("file")
    @classmethod
    def safe_mp3_path(cls, value: str) -> str:
        path = PurePosixPath(value)
        if path.is_absolute() or ".." in path.parts or ":" in value or "\\" in value:
            raise ValueError("Pack file path must stay relative to the pack directory")
        if path.suffix.lower() != ".mp3":
            raise ValueError("Pack clips must be MP3 files")
        return value


class PackManifest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    format_version: Literal[1]
    course_id: str = Field(min_length=1, max_length=100)
    course_version: str = Field(pattern=r"^\d+\.\d+\.\d+$")
    source_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    generated_at: str = Field(min_length=1, max_length=64)
    status: Literal["draft", "reviewed"]
    review: dict = Field(default_factory=dict)
    engine: PackEngine
    licenses: list[PackLicense] = Field(min_length=1)
    counts: dict = Field(default_factory=dict)
    items: list[PackItem] = Field(min_length=1)

    @model_validator(mode="after")
    def unique_keys(self) -> Self:
        keys = [item.key for item in self.items]
        if len(keys) != len(set(keys)):
            raise ValueError("Pack manifest contains duplicate keys")
        return self


@dataclass(frozen=True)
class PackClip:
    key: str
    data: bytes
    mime: str
    duration_seconds: float
    course_version: str
    reviewed: bool


@dataclass(frozen=True)
class PackSummary:
    course_id: str
    course_version: str
    status: str
    reviewed: bool
    clip_count: int
    total_bytes: int


def pack_key(
    text: str,
    language: str,
    voice: str,
    model: str,
    pronunciation_override: str | None,
) -> str:
    """Stable identity for a generated clip, independent of local endpoint settings."""
    fingerprint = json.dumps(
        {
            "text": text,
            "language": language,
            "voice": voice,
            "model": model,
            "format": "mp3",
            "speed": 1.0,
            "pronunciation_override": pronunciation_override,
        },
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha256(fingerprint.encode()).hexdigest()


def _version_key(version: str) -> tuple[tuple[int, int | str], ...]:
    return tuple(
        (0, int(part)) if (part.isascii() and part.isdigit()) else (1, part)
        for part in re.split(r"[.-]", version)
    )


def _manifest_paths(root: Path, course_id: str) -> list[Path]:
    if not COURSE_ID_PATTERN.fullmatch(course_id) or ".." in course_id:
        return []
    root_resolved = root.resolve()
    directory = (root / course_id).resolve()
    if (
        not directory.is_relative_to(root_resolved)
        or directory == root_resolved
        or not directory.is_dir()
    ):
        return []
    paths = [path / "manifest.json" for path in directory.iterdir() if path.is_dir()]
    return sorted((path for path in paths if path.is_file()), reverse=True)


@lru_cache(maxsize=32)
def _load_manifest(
    path_text: str, modified_ns: int, size: int
) -> tuple[PackManifest, dict[str, PackItem]] | None:
    if size > MAX_MANIFEST_BYTES:
        logger.warning("Audio pack manifest exceeds the local size limit; ignored")
        return None
    path = Path(path_text)
    try:
        if path.stat().st_size > MAX_MANIFEST_BYTES:
            logger.warning("Audio pack manifest exceeds the local size limit; ignored")
            return None
        manifest = PackManifest.model_validate_json(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        logger.warning("Audio pack manifest ignored (%s)", type(error).__name__)
        return None
    return manifest, {item.key: item for item in manifest.items}


@lru_cache(maxsize=64)
def _load_item_bytes(path_text: str, modified_ns: int, size: int, expected_sha256: str) -> bytes:
    path = Path(path_text)
    if path.stat().st_size > MAX_CLIP_BYTES:
        raise ValueError("Pack clip exceeds the local size limit")
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        raise ValueError("Pack clip does not match the manifest checksum")
    return data


def _manifest_for(path: Path) -> tuple[PackManifest, dict[str, PackItem]] | None:
    try:
        stat = path.stat()
    except OSError:
        return None
    if stat.st_size > MAX_MANIFEST_BYTES:
        logger.warning("Audio pack manifest exceeds the local size limit; ignored")
        return None
    return _load_manifest(str(path), stat.st_mtime_ns, stat.st_size)


@lru_cache(maxsize=32)
def _course_manifests(
    root: Path, course_id: str
) -> tuple[tuple[Path, PackManifest, dict[str, PackItem]], ...]:
    result: list[tuple[Path, PackManifest, dict[str, PackItem]]] = []
    for path in _manifest_paths(root, course_id):
        loaded = _manifest_for(path)
        if loaded is None:
            continue
        manifest, items_by_key = loaded
        if manifest.course_id != course_id or manifest.course_version != path.parent.name:
            logger.warning("Audio pack manifest does not match its directory; ignored")
            continue
        result.append((path.parent, manifest, items_by_key))
    result.sort(key=lambda item: _version_key(item[1].course_version), reverse=True)
    return tuple(result)


def clear_cache() -> None:
    _course_manifests.cache_clear()
    _load_manifest.cache_clear()
    _load_item_bytes.cache_clear()


def available(config: Config, course_id: str) -> bool:
    if not config.audio_pack_enabled or not course_id:
        return False
    return bool(_course_manifests(config.audio_pack_dir, course_id))


def summary(config: Config, course_id: str) -> PackSummary | None:
    if not config.audio_pack_enabled or not course_id:
        return None
    manifests = _course_manifests(config.audio_pack_dir, course_id)
    if not manifests:
        return None
    _, manifest, _ = manifests[0]
    return PackSummary(
        course_id=manifest.course_id,
        course_version=manifest.course_version,
        status=manifest.status,
        reviewed=manifest.status == "reviewed",
        clip_count=len(manifest.items),
        total_bytes=sum(item.bytes for item in manifest.items),
    )


def lookup(
    config: Config,
    course_id: str,
    text: str,
    language: str,
    pronunciation_override: str | None = None,
    preferred_version: str | None = None,
) -> PackClip | None:
    """Return a generated clip when the exact text/language/voice exists.

    Never raises for a missing or corrupt pack: a miss falls back cleanly to UI
    text/transcript alternatives.
    """
    if not config.audio_pack_enabled or not course_id or language not in {"ja", "en"}:
        return None
    manifests = list(_course_manifests(config.audio_pack_dir, course_id))
    if preferred_version is not None:
        manifests.sort(key=lambda item: item[1].course_version != preferred_version)
    for directory, manifest, items_by_key in manifests:
        voice = manifest.engine.voice_ja if language == "ja" else manifest.engine.voice_en
        key = pack_key(text, language, voice, manifest.engine.model, pronunciation_override)
        item = items_by_key.get(key)
        if item is None:
            continue
        path = (directory / item.file).resolve()
        if not path.is_relative_to(directory.resolve()) or not path.is_file():
            logger.warning("Audio pack clip is missing; using text alternative fallback")
            continue
        try:
            stat = path.stat()
            if stat.st_size != item.bytes:
                logger.warning(
                    "Audio pack clip size differs from manifest; using text alternative fallback"
                )
                continue
            data = _load_item_bytes(
                str(path), stat.st_mtime_ns, stat.st_size, item.file_sha256
            )
        except (OSError, ValueError):
            logger.warning("Audio pack clip could not be read; using text alternative fallback")
            continue
        return PackClip(
            key=item.key,
            data=data,
            mime="audio/mpeg",
            duration_seconds=item.duration_seconds,
            course_version=manifest.course_version,
            reviewed=manifest.status == "reviewed",
        )
    return None


def label(clip: PackClip, language: str) -> str:
    kind = "English meaning" if language == "en" else "Japanese reference"
    review = "reviewed" if clip.reviewed else "human review pending"
    return f"Bundled synthetic {kind} · {review}"
