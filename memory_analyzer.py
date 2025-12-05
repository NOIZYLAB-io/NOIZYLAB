def analyze_memory(memory: dict) -> dict:
    """
    Detects RAM saturation, swap pressure, and possible memory leaks.
    """

    if not memory:
        return {"status": "no_data", "issue": "Memory data missing."}

    total = memory.get("total", 0)
    used = memory.get("used", 0)
    swap_used = memory.get("swap_used", 0)

    if total <= 0:
        return {"status": "error", "issue": "Invalid memory metrics."}

    pct = (used / total) * 100
    issues = []

    if pct >= 92:
        issues.append(f"Memory nearly full ({pct:.1f}%)")

    if swap_used > (0.25 * total):
        issues.append("High swap use — possible leak or heavy load.")

    if issues:
        return {
            "status": "warning",
            "issues": issues,
            "recommended_action": "Close apps or upgrade RAM."
        }

    return {"status": "healthy", "info": "Memory usage normal"}
