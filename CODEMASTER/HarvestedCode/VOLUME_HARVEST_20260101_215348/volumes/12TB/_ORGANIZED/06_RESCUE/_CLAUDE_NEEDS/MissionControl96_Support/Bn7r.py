#!/usr/bin/env python3

import os
import subprocess
import json
import time
from datetime import datetime

# 🧞 Slab Definitions
SLABS = {
    "StudioSlab": "192.168.2.10",
    "PowerSlab": "192.168.2.20",
    "NOIZYWIND": "192.168.2.30",
    "VisionSlab": "192.168.2.40"
}

# 🧬 Ritual Triggers
RITUALS = {
    "activate_sequoia": "~/NoizyFish/Triggers/activate_sequoia.py",
    "launch_overlay": "~/NoizyFish/Overlays/planar_eyelevel.html",
    "run_pcie_scan": "~/NoizyFish/Triggers/pcie_health_check.py",
    "capture_memory": "~/NoizyFish/Triggers/love_bucket.py"
}

# 🧘 Voice Feedback
def speak(message):
    subprocess.run(["say", message])

# 🔁 Slab Scanner
def check_slab(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    return result.returncode == 0

# 🧞 Ritual Executor
def trigger_ritual(name):
    path = RITUALS.get(name)
    if not path:
        speak(f"Ritual {name} not found.")
        return
    subprocess.run(["python3", path])
    speak(f"Ritual {name} has been triggered.")

# 🧠 Overlay Launcher
def launch_overlay():
    subprocess.run(["open", RITUALS["launch_overlay"]])
    speak("EyeLevel overlay launched.")

# 🧬 Legacy Capsule Builder
def build_capsule():
    capsule_name = f"Capsule_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    capsule_path = os.path.expanduser(f"~/NoizyFish/Legacy/{capsule_name}")
    subprocess.run(["zip", "-r", capsule_path + ".zip", "~/NoizyFish/Legacy/"])
    speak(f"Legacy capsule {capsule_name} has been built.")

# 🧞‍♂️ Main Ritual Loop
def main():
    print("🧞‍♂️ Cockpit Orchestrator Activated")
    ritual_log = {
        "timestamp": datetime.now().isoformat(),
        "slab_status": {},
        "rituals_triggered": []
    }

    for slab, ip in SLABS.items():
        status = "Online" if check_slab(ip) else "Offline"
        ritual_log["slab_status"][slab] = status
        print(f"{slab}: {status}")

    # Trigger core rituals
    trigger_ritual("activate_sequoia")
    trigger_ritual("run_pcie_scan")
    launch_overlay()
    build_capsule()

    ritual_log["rituals_triggered"] = list(RITUALS.keys())

    # Log to EyeLevel
    log_path = os.path.expanduser("~/NoizyFish/Legacy/cockpit_log.json")
    with open(log_path, "w") as f:
        json.dump(ritual_log, f, indent=4)

    print("🧞 Rituals complete. Slabs are glowing.")

if __name__ == "__main__":
    main()
