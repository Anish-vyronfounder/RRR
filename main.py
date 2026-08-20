from __future__ import annotations

import io

import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

from backend.config import FRONTEND_ORIGINS, VISION_ALLOWED_EXTENSIONS, VISION_MAX_FILE_SIZE_MB
from backend.services.vision_service import VisionService

app = FastAPI(title="RRR API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vision_service = VisionService()


@app.on_event("startup")
def startup_event() -> None:
    vision_service.load_model()


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "rrr-api",
        "vision_model": vision_service.model.model_name,
        "vision_model_loaded": vision_service.model.is_loaded(),
    }


@app.get("/api/vision/status")
def vision_status() -> dict:
    return {
        "status": "ok",
        "loaded": vision_service.model.is_loaded(),
        "model_name": vision_service.model.model_name,
        "framework": "tensorflow",
        "production_ready": vision_service.model.is_loaded(),
    }


@app.post("/api/vision/analyze")
async def analyze_image(file: UploadFile = File(...)) -> dict:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Missing filename")

    filename = file.filename.lower()
    extension = filename.rsplit(".", 1)[-1] if "." in filename else ""
    if extension not in VISION_ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Unsupported image type: {extension}")

    contents = await file.read()
    max_bytes = VISION_MAX_FILE_SIZE_MB * 1024 * 1024
    if len(contents) > max_bytes:
        raise HTTPException(status_code=400, detail=f"File exceeds {VISION_MAX_FILE_SIZE_MB}MB limit")

    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Unable to decode image") from exc

    width, height = image.size
    array = np.asarray(image.resize((224, 224)), dtype="float32") / 255.0

    try:
        result = vision_service.analyze(
            array,
            (height, width, 3),
            image_name=file.filename,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Vision analysis failed") from exc

    return {**result, "success": True, "filename": file.filename}
