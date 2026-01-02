#!/usr/bin/env python3
"""
Genie Mode Auto-Run Script
Runs all key orchestration, monitoring, and ritual scripts on startup.
"""
import subprocess
import threading
import time

scripts = [
    "~/NoizyFish/Triggers/genie_suite.py",
    "~/NoizyFish/Triggers/genie_super_duper_control.py",
    "~/NoizyFish/Triggers/slablink_scanner.py",
    "~/NoizyFish/Triggers/Noizy_Genie_SlabLink.py",
    "~/NoizyFish/Triggers/switch_planar_input.py",
    "~/NoizyFish/Triggers/resurrect_slab.py",
    "~/NoizyFish/Triggers/scan_pcie.py",
    "~/NoizyFish/Triggers/capture_memory.py"
]

# Expand ~ to full path
scripts = [subprocess.os.path.expanduser(s) for s in scripts]

def run_script(path):
    try:
        subprocess.run(["python3", path])
    except Exception as e:
        print(f"Error running {path}: {e}")

threads = []
for script in scripts:
    t = threading.Thread(target=run_script, args=(script,))
    t.start()
    threads.append(t)

# Optionally, run soundscape overlay
try:
    subprocess.run(["ffplay", "~/NoizyFish/Soundscapes/legacy_loop.wav"])
except Exception:
    print("ffplay not found or soundscape missing.")

# Wait for all threads to finish
for t in threads:
    t.join()

print("🧞‍♂️ Genie Mode: All automations and rituals have been launched.")
