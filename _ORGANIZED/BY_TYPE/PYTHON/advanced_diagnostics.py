import psutil
import shutil
import socket
import time
from .system_exec import run_cmd


def disk_smart():
    # Placeholder until SMARTCTL is wired in
    return {"status": "ok", "temp": "normal", "wear": "low"}


def thermal_check():
    try:
        temps = psutil.sensors_temperatures()
        return {"status": "ok", "temps": temps}
    except:
        return {"status": "unknown"}


def memory_check():
    mem = psutil.virtual_memory()
    return {
        "status": "ok" if mem.percent < 85 else "warning",
        "percent": mem.percent,
        "available": mem.available,
    }


def network_check():
    try:
        socket.gethostbyname("google.com")
        return {"status": "ok", "latency": _ping_latency()}
    except:
        return {"status": "error"}


def _ping_latency():
    res = run_cmd("ping -c 1 google.com")
    if not res["ok"]:
        return None

    out = res["output"]
    if "time=" in out:
        return float(out.split("time=")[1].split(" ms")[0])

    return None


def run_full_suite():
    return {
        "smart": disk_smart(),
        "thermal": thermal_check(),
        "memory": memory_check(),
        "network": network_check(),
        "timestamp": time.time(),
    }

