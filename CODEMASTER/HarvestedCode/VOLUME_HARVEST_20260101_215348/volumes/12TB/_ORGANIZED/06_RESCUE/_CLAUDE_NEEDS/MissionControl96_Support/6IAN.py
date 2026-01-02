#!/usr/bin/env python3
"""
RSP Master Autosave & Autorun
Author: RSP
Purpose: Chain all autosave and autorun rituals for vault, capsule, orchestrator, and logs.
"""

import subprocess, datetime, json, os
from pathlib import Path

SCRIPTS = [
    str(Path.home() / "WORK_OF_TODAY/utilities/musicvault_fullscan.py"),
    str(Path.home() / "WORK_OF_TODAY/utilities/rsp_orchestrator_core.py"),
    str(Path.home() / "WORK_OF_TODAY/utilities/ignite_autosave_stack.py"),
    str(Path.home() / "WORK_OF_TODAY/utilities/rsp_post_render.py")
]
LOG_PATH = str(Path.home() / "RSP/Logs/master_autosave_log.jsonl")

def run_script(script):
    print(f"Running: {script}")
    try:
        result = subprocess.run(["python3", script], capture_output=True, text=True)
        log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "script": script,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(log) + "\n")
        print(f"Done: {script}")
    except Exception as e:
        print(f"Error running {script}: {e}")

if __name__ == "__main__":
    for script in SCRIPTS:
        run_script(script)
    print("RSP Master Autosave & Autorun complete.")
