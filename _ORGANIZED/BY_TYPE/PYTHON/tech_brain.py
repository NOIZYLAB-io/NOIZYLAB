"""
NoizyOS Ultra — GEN-3 AI Technician Brain
==========================================
Analyzes system stats, detects patterns, predicts failures,
generates human-readable conclusions and repair plans.

This is the AI that thinks like a technician but reacts instantly.
"""


def analyze_stats(stats: dict) -> dict:
    """
    Analyze system statistics and generate warnings, suggestions, predictions.
    
    Args:
        stats: Dict containing cpu_usage, ram_usage, disk_usage, temp, etc.
    
    Returns:
        Dict with warnings, suggestions, predictions, and severity level.
    """
    warnings = []
    suggestions = []
    predictions = []
    severity = "normal"  # normal, elevated, critical

    cpu = stats.get("cpu_usage", 0) or 0
    ram = stats.get("ram_usage", 0) or 0
    disk = stats.get("disk_usage", 0) or 0
    temp = stats.get("temp") or 0

    # ========================================
    # CPU ANALYSIS
    # ========================================
    if cpu > 95:
        warnings.append("🔴 CPU CRITICAL: Usage at maximum capacity")
        suggestions.append("Kill non-essential processes immediately")
        suggestions.append("Check for crypto miners or malware")
        severity = "critical"
    elif cpu > 85:
        warnings.append("🟠 CPU HIGH: Usage critically elevated")
        suggestions.append("Check background processes, possible malware or runaway app")
        suggestions.append("Consider ending heavy applications")
        if severity != "critical":
            severity = "elevated"
    elif cpu > 65:
        suggestions.append("CPU consistently elevated — consider optimization")

    # ========================================
    # RAM ANALYSIS
    # ========================================
    if ram > 95:
        warnings.append("🔴 RAM CRITICAL: Memory exhausted")
        suggestions.append("Close applications immediately to prevent crash")
        suggestions.append("Check for memory leaks")
        severity = "critical"
    elif ram > 80:
        warnings.append("🟠 RAM HIGH: Memory nearly maxed")
        suggestions.append("Disable startup apps, expand RAM, close programs")
        if severity != "critical":
            severity = "elevated"
    elif ram > 70:
        suggestions.append("RAM usage elevated — monitor for leaks")

    # ========================================
    # DISK ANALYSIS
    # ========================================
    if disk > 95:
        warnings.append("🔴 DISK CRITICAL: Storage nearly full — system may freeze")
        suggestions.append("Clear temp files immediately")
        suggestions.append("Move large files to external storage")
        suggestions.append("Empty recycle bin")
        severity = "critical"
    elif disk > 90:
        warnings.append("🟠 DISK HIGH: Storage almost full — can cause OS freezes")
        suggestions.append("Clear temp files, move media, empty recycle bin")
        if severity != "critical":
            severity = "elevated"
    elif disk > 80:
        suggestions.append("Disk space getting low — consider cleanup")

    # ========================================
    # TEMPERATURE ANALYSIS
    # ========================================
    if temp:
        if temp > 95:
            warnings.append("🔴 TEMP CRITICAL: CPU severely overheated — shutdown imminent")
            suggestions.append("Stop all heavy tasks immediately")
            suggestions.append("Check if fans are working")
            severity = "critical"
        elif temp > 85:
            warnings.append("🟠 TEMP HIGH: CPU overheated — risk of thermal throttling")
            suggestions.append("Clean dust, check fans, reapply thermal paste")
            if severity != "critical":
                severity = "elevated"
        elif temp > 75:
            suggestions.append("Temperature elevated — monitor cooling system")
        elif temp > 65:
            suggestions.append("Temperature normal but warm — ensure good airflow")

    # ========================================
    # PREDICTION ENGINE
    # ========================================
    if temp and temp > 80 and cpu > 85:
        predictions.append("⚠️ System likely to thermal throttle within minutes")
    
    if ram > 80 and disk > 85:
        predictions.append("⚠️ High chance of severe slowdowns and potential freeze")
    
    if cpu > 90 and ram > 90:
        predictions.append("⚠️ System under extreme load — crash possible")
    
    if disk > 95:
        predictions.append("⚠️ OS may become unresponsive due to disk pressure")
    
    if temp and temp > 90:
        predictions.append("⚠️ Thermal shutdown may occur to protect hardware")

    # ========================================
    # SMART REPAIR PLAN
    # ========================================
    repair_plan = []
    
    if severity == "critical":
        repair_plan.append("1. IMMEDIATE: Stop all non-essential processes")
        repair_plan.append("2. Run NoizyScan for malware/bloatware")
        repair_plan.append("3. Check Task Manager for resource hogs")
        if disk > 90:
            repair_plan.append("4. Run disk cleanup utility")
        if temp and temp > 85:
            repair_plan.append("5. Check cooling system and fans")
        repair_plan.append("6. Consider system restart after stabilization")
    elif severity == "elevated":
        repair_plan.append("1. Review running processes")
        repair_plan.append("2. Clear temporary files")
        repair_plan.append("3. Disable unnecessary startup programs")
        repair_plan.append("4. Schedule full system optimization")
    else:
        repair_plan.append("System healthy — routine maintenance recommended")

    return {
        "warnings": warnings,
        "suggestions": suggestions,
        "predictions": predictions,
        "repair_plan": repair_plan,
        "severity": severity,
        "metrics": {
            "cpu": cpu,
            "ram": ram,
            "disk": disk,
            "temp": temp
        }
    }


def generate_summary(analysis: dict) -> str:
    """Generate a human-readable summary of the analysis."""
    severity = analysis.get("severity", "normal")
    warnings = analysis.get("warnings", [])
    
    if severity == "critical":
        return f"🚨 CRITICAL: {len(warnings)} urgent issues detected. Immediate action required."
    elif severity == "elevated":
        return f"⚠️ ATTENTION: {len(warnings)} issues need attention. System performance affected."
    else:
        return "✅ System healthy. All metrics within normal range."

