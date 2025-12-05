"""
NoizyOS Ultra — NoizyGrid Node Agent
====================================
Install and run this on each machine in your cluster.
Exposes node info and task execution endpoints.

Usage:
    python noizygrid_node.py

Or with custom port:
    python noizygrid_node.py --port 8899
"""

from fastapi import FastAPI
import platform
import psutil
import uuid
import subprocess
import sys
from datetime import datetime
from typing import Dict, Any, Optional

app = FastAPI(title="NoizyGrid Node Agent")

# Generate unique node ID
NODE_ID = str(uuid.uuid4())[:8]
START_TIME = datetime.now()


def get_system_info() -> Dict[str, Any]:
    """Gather comprehensive system information."""
    try:
        cpu_info = platform.processor()
    except:
        cpu_info = "Unknown"
    
    try:
        temps = psutil.sensors_temperatures()
        cpu_temp = None
        for name, entries in temps.items():
            if entries:
                cpu_temp = entries[0].current
                break
    except:
        cpu_temp = None
    
    return {
        "id": NODE_ID,
        "device": platform.node(),
        "os": platform.platform(),
        "os_simple": platform.system(),
        "type": "windows" if platform.system() == "Windows" else "mac",
        "cpu_name": cpu_info,
        "cpu": psutil.cpu_percent(interval=0.1),
        "cpu_count": psutil.cpu_count(),
        "ram": psutil.virtual_memory().percent,
        "ram_total_gb": round(psutil.virtual_memory().total / (1024**3), 1),
        "disk": psutil.disk_usage('/').percent,
        "temp": cpu_temp,
        "uptime_seconds": (datetime.now() - START_TIME).seconds,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/")
def root():
    """Node status check."""
    return {
        "status": "NoizyGrid Node Active",
        "node_id": NODE_ID,
        "device": platform.node()
    }


@app.get("/info")
def info():
    """Get full node information."""
    return get_system_info()


@app.get("/health")
def health():
    """Quick health check."""
    return {
        "healthy": True,
        "node_id": NODE_ID,
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent
    }


@app.post("/run")
def run_task(payload: dict):
    """
    Execute a task on this node.
    
    Supported tasks:
    - ping: Simple connectivity test
    - system_info: Return detailed system info
    - run_command: Execute a shell command (careful!)
    - diagnostics: Run system diagnostics
    """
    task = payload.get("task", "unknown")
    task_payload = payload.get("payload", {})
    
    result = {
        "ok": True,
        "task": task,
        "node_id": NODE_ID,
        "device": platform.node(),
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        if task == "ping":
            result["result"] = "pong"
        
        elif task == "system_info":
            result["result"] = get_system_info()
        
        elif task == "diagnostics":
            result["result"] = run_diagnostics()
        
        elif task == "ai_heavy":
            # Placeholder for AI tasks
            result["result"] = f"AI task would run on {platform.node()}"
        
        elif task == "windows_diagnostics":
            if platform.system() == "Windows":
                result["result"] = run_windows_diagnostics()
            else:
                result["ok"] = False
                result["error"] = "This task requires Windows"
        
        elif task == "run_command":
            # Execute shell command (use with caution!)
            cmd = task_payload.get("command")
            if cmd:
                try:
                    output = subprocess.check_output(
                        cmd, shell=True, stderr=subprocess.STDOUT,
                        timeout=30
                    ).decode()
                    result["result"] = output
                except subprocess.TimeoutExpired:
                    result["ok"] = False
                    result["error"] = "Command timeout"
                except subprocess.CalledProcessError as e:
                    result["ok"] = False
                    result["error"] = e.output.decode() if e.output else str(e)
            else:
                result["ok"] = False
                result["error"] = "No command provided"
        
        else:
            result["result"] = f"Node {NODE_ID} received task: {task}"
    
    except Exception as e:
        result["ok"] = False
        result["error"] = str(e)
    
    return result


def run_diagnostics() -> Dict[str, Any]:
    """Run basic system diagnostics."""
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": dict(psutil.virtual_memory()._asdict()),
        "disk": dict(psutil.disk_usage('/')._asdict()),
        "network": dict(psutil.net_io_counters()._asdict()),
        "processes": len(psutil.pids()),
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat()
    }


def run_windows_diagnostics() -> Dict[str, Any]:
    """Run Windows-specific diagnostics."""
    if platform.system() != "Windows":
        return {"error": "Not Windows"}
    
    return {
        "os_version": platform.version(),
        "diagnostics": "Windows diagnostics would run here",
        # Add Windows-specific checks here
    }


if __name__ == "__main__":
    import argparse
    import uvicorn
    
    parser = argparse.ArgumentParser(description="NoizyGrid Node Agent")
    parser.add_argument("--port", type=int, default=8899, help="Port to run on")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    args = parser.parse_args()
    
    print(f"=" * 50)
    print(f"  NoizyGrid Node Agent")
    print(f"  Node ID: {NODE_ID}")
    print(f"  Device: {platform.node()}")
    print(f"  OS: {platform.system()}")
    print(f"  Port: {args.port}")
    print(f"=" * 50)
    
    uvicorn.run(app, host=args.host, port=args.port)

