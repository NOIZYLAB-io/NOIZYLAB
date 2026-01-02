#!/usr/bin/env python3
"""
RSP Utilities Master Runner
Chains all key utility scripts for autosave, scan, orchestration, and logging.
"""
import subprocess
from pathlib import Path

UTILITIES = [
    "rsp_master_autosave_autorun.py",
    "musicvault_fullscan.py",
    "rsp_orchestrator_core.py",
    "ignite_autosave_stack.py",
    "rsp_post_render.py",
    "auto_save_and_run.py",
    "request_move_to_main.py"
]
UTILS_DIR = Path.home() / "WORK_OF_TODAY/utilities"

def run_util(script):
    script_path = UTILS_DIR / script
    if script_path.exists():
        print(f"Running: {script}")
        subprocess.run(["python3", str(script_path)])
    else:
        print(f"Not found: {script}")

if __name__ == "__main__":
    for util in UTILITIES:
        run_util(util)
    print("All utilities executed.")
