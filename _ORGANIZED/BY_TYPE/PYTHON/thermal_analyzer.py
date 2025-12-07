def analyze_temps(temps: dict) -> dict:
    """
    Detects thermal issues based on universal CPU/GPU temperature ranges.
    """

    if not temps:
        return {"status": "no_data", "issue": "No temperature data provided."}

    cpu = temps.get("cpu", 0)
    gpu = temps.get("gpu", 0)
    issues = []

    if cpu >= 95:
        issues.append(f"CPU overheating ({cpu}°C)")
    elif cpu >= 85:
        issues.append(f"CPU running hot ({cpu}°C)")

    if gpu >= 95:
        issues.append(f"GPU overheating ({gpu}°C)")
    elif gpu >= 85:
        issues.append(f"GPU running hot ({gpu}°C)")

    if issues:
        return {
            "status": "warning",
            "issues": issues,
            "recommended_action": "Improve cooling / clean system / adjust airflow."
        }

    return {"status": "healthy", "info": "Temperatures normal"}
