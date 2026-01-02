#!/usr/bin/env python3
import os, subprocess, json, time
from datetime import datetime

SLABS = {
    "StudioSlab": "192.168.2.10",
    "PowerSlab": "192.168.2.20",
    "NOIZYWIND": "192.168.2.30",
    "VisionSlab": "192.168.2.40"
}

RITUALS = {
    "activate_sequoia": "~/NoizyFish/Triggers/activate_sequoia.py",
    "run_pcie_scan": "~/NoizyFish/Triggers/pcie_health_check.py",
    "capture_memory": "~/NoizyFish/Triggers/love_bucket.py",
    "launch_overlay": "~/NoizyFish/Overlays/planar_eyelevel.html"
}

def speak(msg): subprocess.run(["say", msg])
def check_slab(ip): return subprocess.run(["ping", "-c", "1", ip], capture_output=True).returncode == 0
def trigger_ritual(name):
    path = os.path.expanduser(RITUALS.get(name, ""))
    if os.path.exists(path): subprocess.run(["python3", path]); speak(f"{name} triggered.")
    else: speak(f"Ritual {name} not found.")

def launch_overlay():
    subprocess.run(["open", os.path.expanduser(RITUALS["launch_overlay"])])
    speak("EyeLevel overlay launched.")

def build_capsule():
    capsule = f"Capsule_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    subprocess.run(["zip", "-r", f"~/NoizyFish/Legacy/{capsule}.zip", "~/NoizyFish/Legacy/"])
    speak(f"Legacy capsule {capsule} built.")

def main():
    log = {"timestamp": datetime.now().isoformat(), "slab_status": {}, "rituals_triggered": []}
    for slab, ip in SLABS.items():
        status = "Online" if check_slab(ip) else "Offline"
        log["slab_status"][slab] = status
        if status == "Offline": speak(f"{slab} offline. Resurrection initiated.")
    for ritual in RITUALS: trigger_ritual(ritual); log["rituals_triggered"].append(ritual)
    build_capsule()
    with open(os.path.expanduser("~/NoizyFish/Legacy/cockpit_log.json"), "w") as f: json.dump(log, f, indent=4)
    print("🧞 Rituals complete. Slabs are glowing.")

if __name__ == "__main__": main()
