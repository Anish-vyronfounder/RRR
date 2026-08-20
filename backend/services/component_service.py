from __future__ import annotations

import csv
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "components.csv"


def list_components() -> list[dict[str, str]]:
    with DATA_FILE.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def get_component(component_id: str) -> dict[str, str] | None:
    for component in list_components():
        if component["component_id"] == component_id:
            return component
    return None
