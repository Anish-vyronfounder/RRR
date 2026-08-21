"""Deterministic RRR decision engines.

The engines are deliberately conservative: incomplete specifications produce
explicit unknown/insufficient-data results instead of fabricated recommendations.
"""
from __future__ import annotations

from itertools import combinations
from typing import Iterable

from .compatibility_service import check_compatibility


PC_CATEGORIES = {"cpu", "motherboard", "ram", "gpu", "storage", "power supply", "case", "cooler"}


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


def _as_float(value: object) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def _budget_value(request: dict) -> float | None:
    value = request.get("budget")
    if isinstance(value, dict):
        value = value.get("max") or value.get("amount")
    return _as_float(value)


def plan_pc_build(request: dict, components: Iterable[dict]) -> dict:
    """Validate a PC build request against a supplied verified component catalog.

    This function does not invent missing parts or prices. It scores catalog
    candidates only when their specifications are sufficient for the requested
    role, and reports missing evidence explicitly.
    """
    budget = _budget_value(request)
    purpose = str(request.get("purpose") or "general desktop").strip()
    owned = request.get("owned_components") or []
    catalog = [dict(c) for c in components]
    available = [c for c in catalog if str(c.get("category", "")).lower() in PC_CATEGORIES]

    required = ["CPU", "Motherboard", "RAM", "Storage", "Power Supply", "Case", "Cooler"]
    if "gaming" in purpose.lower() or "gpu" in purpose.lower() or "ai" in purpose.lower():
        required.insert(4, "GPU")

    by_category: dict[str, list[dict]] = {category: [] for category in PC_CATEGORIES}
    for item in available:
        by_category.setdefault(str(item.get("category", "")).lower(), []).append(item)

    missing_catalog = [role for role in required if not by_category.get(role.lower())]
    if missing_catalog:
        return {
            "status": "insufficient_catalog",
            "purpose": purpose,
            "budget": budget,
            "required_categories": required,
            "missing_categories": missing_catalog,
            "selected": [],
            "compatibility": [],
            "warnings": [
                "RRR will not fabricate component choices when the catalog lacks required verified specifications.",
                "Add verified motherboard, case, cooler and other missing specifications before generating a build.",
            ],
        }

    selected: list[dict] = []
    for role in required:
        candidates = by_category[role.lower()]
        # Deterministic baseline: prefer the first verified candidate. A future
        # ranking layer can use workload, price and performance evidence.
        selected.append(candidates[0])

    checks = []
    compatible = True
    for left, right in combinations(selected, 2):
        result = check_compatibility(left, right)
        if result.compatible is False:
            compatible = False
        checks.append({
            "component_a": left.get("name"),
            "component_b": right.get("name"),
            "compatible": result.compatible,
            "confidence": result.confidence,
            "reasons": result.reasons,
        })

    unknown = [c for c in checks if c["compatible"] is None]
    status = "verified" if compatible and not unknown else "needs_verification" if compatible else "incompatible"
    return {
        "status": status,
        "purpose": purpose,
        "budget": budget,
        "selected": selected,
        "compatibility": checks,
        "unknown_checks": unknown,
        "warnings": [
            "Prices and performance are not asserted unless present in the component catalog.",
            "A verified build requires every relevant compatibility check to have sufficient specifications.",
        ],
    }


def build(components: list[dict]) -> dict:
    names = [c.get("name") for c in components if c.get("name")]
    if not names:
        return {"status": "insufficient_data", "projects": []}
    return {
        "status": "candidate_generation",
        "available_components": names,
        "projects": [],
        "message": "Use plan_pc_build with a purpose, budget, and verified component catalog to generate a build.",
    }
