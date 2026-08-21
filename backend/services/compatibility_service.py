from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompatibilityResult:
    compatible: bool | None
    confidence: str
    reasons: list[str]


def _norm(value: object) -> str:
    return str(value or "").strip().lower()


def _unknown(message: str) -> CompatibilityResult:
    return CompatibilityResult(None, "low", [message])


def check_compatibility(a: dict, b: dict) -> CompatibilityResult:
    """Conservative PC compatibility rules.

    Missing specifications always produce an explicit unknown result. RRR must
    never turn incomplete data into a confident compatibility claim.
    """
    ca, cb = _norm(a.get("category")), _norm(b.get("category"))
    pair = {ca, cb}
    reasons: list[str] = []

    if pair == {"cpu", "motherboard"}:
        cpu = a if ca == "cpu" else b
        board = b if ca == "cpu" else a
        left, right = cpu.get("socket_or_standard"), board.get("socket_or_standard")
        if not left or not right:
            return _unknown("Exact CPU socket and motherboard socket are required.")
        ok = _norm(left) == _norm(right)
        reasons.append(f"CPU socket {_norm(left)} vs motherboard socket {_norm(right)}.")
        bios = cpu.get("bios_requirement")
        supported_bios = board.get("supported_bios")
        if bios and supported_bios and _norm(bios) not in _norm(supported_bios):
            ok = False
            reasons.append(f"CPU BIOS requirement {bios} is not listed in motherboard BIOS support {supported_bios}.")
        elif bios and not supported_bios:
            reasons.append("BIOS requirement exists but motherboard BIOS support is not specified.")
            return CompatibilityResult(ok, "medium" if ok else "high", reasons)
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"ram", "motherboard"}:
        ram = a if ca == "ram" else b
        board = b if ca == "ram" else a
        left, right = ram.get("socket_or_standard"), board.get("socket_or_standard")
        if not left or not right:
            return _unknown("Exact RAM generation/standard and motherboard memory support are required.")
        ok = _norm(left) == _norm(right)
        reasons.append(f"RAM standard {_norm(left)} vs motherboard memory standard {_norm(right)}.")
        ram_form = _norm(ram.get("form_factor"))
        board_form = _norm(board.get("memory_form_factor"))
        if ram_form and board_form and ram_form != board_form:
            ok = False
            reasons.append(f"RAM form factor {ram_form} does not match motherboard memory form factor {board_form}.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"storage", "motherboard"}:
        drive = a if ca == "storage" else b
        board = b if ca == "storage" else a
        interface, supported = drive.get("interface"), board.get("storage_interfaces") or board.get("interface")
        if not interface or not supported:
            return _unknown("Exact storage interface and motherboard storage support are required.")
        ok = _norm(interface) in _norm(supported)
        reasons.append(f"Storage interface {interface} checked against motherboard support {supported}.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"gpu", "motherboard"}:
        gpu = a if ca == "gpu" else b
        board = b if ca == "gpu" else a
        gpu_interface, slots = gpu.get("interface"), board.get("pcie_slots") or board.get("interface")
        if not gpu_interface or not slots:
            return _unknown("GPU interface and motherboard PCIe slot support are required.")
        ok = _norm(gpu_interface) in _norm(slots) or _norm(gpu_interface).replace(" ", "") in _norm(slots).replace(" ", "")
        reasons.append(f"GPU interface {gpu_interface} checked against motherboard PCIe support {slots}.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"gpu", "power supply"}:
        gpu = a if ca == "gpu" else b
        psu = b if ca == "gpu" else a
        gpu_w = gpu.get("power_watts")
        psu_w = psu.get("wattage") or psu.get("power_watts")
        if gpu_w is None or psu_w is None:
            return _unknown("GPU power requirement and PSU wattage are required.")
        try:
            required = float(gpu_w) + float(psu.get("headroom_watts", 150))
            available = float(psu_w)
        except (TypeError, ValueError):
            return _unknown("GPU power and PSU wattage must be numeric.")
        ok = available >= required
        reasons.append(f"PSU {available:g}W vs GPU requirement plus safety headroom {required:g}W.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"cpu", "cooler"}:
        cpu = a if ca == "cpu" else b
        cooler = b if ca == "cpu" else a
        cpu_socket, sockets = cpu.get("socket_or_standard"), cooler.get("supported_sockets")
        if not cpu_socket or not sockets:
            return _unknown("CPU socket and cooler socket support are required.")
        ok = _norm(cpu_socket) in _norm(sockets)
        reasons.append(f"CPU socket {cpu_socket} checked against cooler support {sockets}.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"motherboard", "case"}:
        board = a if ca == "motherboard" else b
        case = b if ca == "motherboard" else a
        board_form, supported = board.get("form_factor"), case.get("supported_form_factors")
        if not board_form or not supported:
            return _unknown("Motherboard form factor and case-supported form factors are required.")
        ok = _norm(board_form) in _norm(supported)
        reasons.append(f"Motherboard form factor {board_form} checked against case support {supported}.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"gpu", "case"}:
        gpu = a if ca == "gpu" else b
        case = b if ca == "gpu" else a
        gpu_len, max_len = gpu.get("length_mm"), case.get("max_gpu_length_mm")
        if gpu_len is None or max_len is None:
            return _unknown("GPU length and case maximum GPU clearance are required.")
        ok = float(gpu_len) <= float(max_len)
        reasons.append(f"GPU length {gpu_len}mm vs case clearance {max_len}mm.")
        return CompatibilityResult(ok, "high", reasons)

    if pair == {"cooler", "case"}:
        cooler = a if ca == "cooler" else b
        case = b if ca == "cooler" else a
        height, max_height = cooler.get("height_mm"), case.get("max_cpu_cooler_height_mm")
        if height is None or max_height is None:
            return _unknown("CPU cooler height and case clearance are required.")
        ok = float(height) <= float(max_height)
        reasons.append(f"Cooler height {height}mm vs case clearance {max_height}mm.")
        return CompatibilityResult(ok, "high", reasons)

    return _unknown(f"No deterministic compatibility rule exists for {ca or 'unknown'} and {cb or 'unknown'}.")
