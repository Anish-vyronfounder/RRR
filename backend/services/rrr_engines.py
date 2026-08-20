"""Deterministic RRR decision engines.

These engines are intentionally rule-based. They do not fabricate technical
facts; uncertain inputs produce an explicit unknown result.
"""
from __future__ import annotations


def repair(component: dict, symptom: str) -> dict:
    if not component.get("category") or not symptom.strip():
        return {"status": "insufficient_data", "steps": []}
    return {
        "status": "guided_diagnosis",
        "component": component.get("name"),
        "symptom": symptom,
        "steps": [
            "Disconnect power before inspection.",
            "Visually inspect connectors, cables, corrosion, burns, and physical damage.",
            "Check the manufacturer's service documentation for the exact model.",
            "Measure only within the limits and procedure specified by the manufacturer.",
        ],
        "evidence_required": True,
    }


def reuse(component: dict) -> dict:
    category = (component.get("category") or "").lower()
    ideas = {
        "ram": ["memory upgrade", "test workstation", "embedded/Linux lab if electrically compatible"],
        "storage": ["secondary storage", "backup target", "test machine storage"],
        "microcontroller": ["sensor node", "automation prototype", "IoT learning project"],
        "gpu": ["graphics workstation", "compute experiment", "media workstation"],
    }
    return {"component": component.get("name"), "suggestions": ideas.get(category, ["inspect specifications before reuse"]), "grounded": False}


def build(components: list[dict]) -> dict:
    names = [c.get("name") for c in components if c.get("name")]
    if not names:
        return {"status": "insufficient_data", "projects": []}
    return {
        "status": "candidate_generation",
        "available_components": names,
        "projects": [],
        "message": "Project candidates require verified component specifications and compatibility checks before being marked buildable.",
    }
