from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompatibilityResult:
    compatible: bool | None
    confidence: str
    reasons: list[str]


def check_compatibility(a: dict, b: dict) -> CompatibilityResult:
    """Conservative rule engine: unknown specifications never become a false 'compatible'."""
    reasons: list[str] = []

    # CPU socket ↔ motherboard socket
    if {a.get("category"), b.get("category")} == {"CPU", "Motherboard"}:
        cpu = a if a.get("category") == "CPU" else b
        board = b if b.get("category") == "Motherboard" else a
        left, right = cpu.get("socket_or_standard"), board.get("socket_or_standard")
        if left and right:
            ok = left == right
            reasons.append(f"CPU socket {left} vs motherboard socket {right}.")
            return CompatibilityResult(ok, "high", reasons)
        return CompatibilityResult(None, "low", ["Exact CPU and motherboard socket specifications are required."])

    # RAM generation ↔ motherboard memory standard
    if {a.get("category"), b.get("category")} == {"RAM", "Motherboard"}:
        ram = a if a.get("category") == "RAM" else b
        board = b if b.get("category") == "Motherboard" else a
        left, right = ram.get("socket_or_standard"), board.get("socket_or_standard")
        if left and right:
            ok = left == right
            reasons.append(f"RAM standard {left} vs motherboard memory standard {right}.")
            return CompatibilityResult(ok, "high", reasons)
        return CompatibilityResult(None, "low", ["Exact RAM and motherboard memory specifications are required."])

    # Storage interface ↔ motherboard storage support
    if {a.get("category"), b.get("category")} == {"Storage", "Motherboard"}:
        drive = a if a.get("category") == "Storage" else b
        board = b if b.get("category") == "Storage" else a
        if drive.get("interface") and board.get("interface"):
            ok = drive["interface"].lower() in board["interface"].lower()
            reasons.append(f"Storage interface {drive['interface']} checked against motherboard interfaces.")
            return CompatibilityResult(ok, "medium", reasons)
        return CompatibilityResult(None, "low", ["Exact motherboard storage interfaces are required."])

    return CompatibilityResult(None, "low", ["No deterministic rule exists yet for these component categories."])
