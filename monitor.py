"""NoizySelf++ Performance Monitor"""
import psutil

def get_performance():
    return {"cpu": psutil.cpu_percent(), "memory": psutil.virtual_memory().percent, "disk": psutil.disk_usage("/").percent}

def check_health():
    perf = get_performance()
    issues = []
    if perf["cpu"] > 90: issues.append("CPU overload")
    if perf["memory"] > 90: issues.append("Memory pressure")
    if perf["disk"] > 95: issues.append("Disk full")
    return {"healthy": len(issues) == 0, "issues": issues, "metrics": perf}

