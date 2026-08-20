from __future__ import annotations

import os


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


VISION_MODEL_NAME = os.getenv("VISION_MODEL_NAME", "MobileNetV2")
VISION_MODEL_PATH = os.getenv("VISION_MODEL_PATH")
VISION_MAX_FILE_SIZE_MB = _env_int("VISION_MAX_FILE_SIZE_MB", 8)
VISION_ALLOWED_EXTENSIONS = tuple(
    ext.strip().lower()
    for ext in os.getenv("VISION_ALLOWED_EXTENSIONS", "jpg,jpeg,png,webp").split(",")
    if ext.strip()
)

FRONTEND_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:3000,http://localhost:5173,http://localhost:8080,http://localhost:8081",
    ).split(",")
    if origin.strip()
]
