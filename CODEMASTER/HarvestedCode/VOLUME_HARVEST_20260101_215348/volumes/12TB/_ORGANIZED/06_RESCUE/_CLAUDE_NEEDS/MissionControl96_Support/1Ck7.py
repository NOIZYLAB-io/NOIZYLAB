#!/usr/bin/env python3
"""
Telemetry API - System monitoring and metrics collection
"""
from fastapi import FastAPI
import time
import psutil
import sys

sys.path.append('/path/to/uap_core')
from uap_core import uap, UapEvent

app = FastAPI(title="Mission Control Telemetry API")

@app.get("/api/telemetry/system")
async def get_system_metrics():
    """Get current system metrics"""
    return {
        "timestamp": time.time(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "percent": psutil.virtual_memory().percent,
            "available": psutil.virtual_memory().available,
            "total": psutil.virtual_memory().total
        },
        "disk": {
            "percent": psutil.disk_usage('/').percent,
            "free": psutil.disk_usage('/').free,
            "total": psutil.disk_usage('/').total
        },
        "network": dict(psutil.net_io_counters()._asdict())
    }

@app.get("/api/telemetry/processes")
async def get_process_info():
    """Get Mission Control process information"""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            if any(keyword in proc.info['name'].lower() for keyword in 
                   ['python', 'code', 'mission', 'noizy']):
                processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return {"processes": processes}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)