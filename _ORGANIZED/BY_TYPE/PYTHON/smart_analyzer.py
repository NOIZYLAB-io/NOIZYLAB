def analyze_smart(smart_data: dict) -> dict:
    """
    OS-agnostic SMART evaluator.
    Flags disk failure risks using the most universal attributes.
    """

    if not smart_data:
        return {"status": "no_data", "issue": "SMART data missing."}

    issues = []

    reallocated = smart_data.get("reallocated_sectors", 0)
    pending = smart_data.get("pending_sectors", 0)
    temp = smart_data.get("temperature", 0)
    hours = smart_data.get("power_on_hours", 0)

    if reallocated > 0:
        issues.append(f"Reallocated sectors: {reallocated}")

    if pending > 0:
        issues.append(f"Pending sectors: {pending}")

    if temp >= 70:
        issues.append(f"Drive too hot: {temp}°C")

    if hours > 30000:
        issues.append(f"Drive aged: {hours} hours")

    if issues:
        return {
            "status": "warning",
            "issues": issues,
            "recommended_action": "Backup now and schedule replacement."
        }

    return {"status": "healthy", "info": "SMART values normal"}
