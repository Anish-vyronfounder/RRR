from __future__ import annotations

from dataclasses import dataclass

from backend.config import VISION_MODEL_NAME, VISION_MODEL_PATH


@dataclass
class ModelAdapter:
    model_name: str = VISION_MODEL_NAME
    loaded: bool = False

    def load(self) -> None:
        # A real TensorFlow model is loaded only when a trained model path is supplied.
        # This keeps the API usable during dataset/model development without pretending
        # that an untrained classifier is production-ready.
        self.loaded = bool(VISION_MODEL_PATH)

    def is_loaded(self) -> bool:
        return self.loaded


class VisionService:
    def __init__(self) -> None:
        self.model = ModelAdapter()

    def load_model(self) -> None:
        self.model.load()

    def analyze(self, array, original_shape, image_name: str) -> dict:
        # Until the RRR training dataset and trained weights exist, return an explicit
        # non-production result instead of inventing a component classification.
        height, width, channels = original_shape
        return {
            "object": "unknown",
            "confidence": 0.0,
            "model": self.model.model_name,
            "image": {"width": width, "height": height, "channels": channels},
            "classification": {
                "status": "model_not_ready",
                "message": "No trained RRR component classifier is configured yet.",
            },
            "detections": [],
            "features": {"input_shape": list(array.shape)},
            "stage": "preprocessed",
        }
