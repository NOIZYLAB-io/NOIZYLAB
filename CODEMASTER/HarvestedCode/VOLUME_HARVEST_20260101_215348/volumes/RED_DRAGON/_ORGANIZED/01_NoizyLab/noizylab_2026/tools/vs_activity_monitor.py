#!/usr/bin/env python3
import json, os, time, subprocess
from pathlib import Path

LOG_DIR = Path("/Users/rsp_ms/Desktop/MissionControl96/state")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "vs_activity.json"

def log_event(event, detail=""):
    entry = {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "event": event,
        "detail": detail,
    }
    logs = []
    if LOG_FILE.exists():
        try: logs = json.loads(LOG_FILE.read_text())
        except: logs = []
    logs.append(entry)
    LOG_FILE.write_text(json.dumps(logs[-200:], indent=2))

def check_processes():
    """Poll running VS Code and Python processes."""
    try:
        out = subprocess.check_output(["ps", "-A"], text=True)
        vs_running = "Visual Studio Code" in out
        py_running = any("python" in line for line in out.splitlines())
        log_event("status", {"vscode": vs_running, "python": py_running})
    except Exception as e:
        log_event("error", str(e))

if __name__ == "__main__":
    print("📡 VS Activity Monitor started — writing to", LOG_FILE)
    while True:
        check_processes()
        time.sleep(30)