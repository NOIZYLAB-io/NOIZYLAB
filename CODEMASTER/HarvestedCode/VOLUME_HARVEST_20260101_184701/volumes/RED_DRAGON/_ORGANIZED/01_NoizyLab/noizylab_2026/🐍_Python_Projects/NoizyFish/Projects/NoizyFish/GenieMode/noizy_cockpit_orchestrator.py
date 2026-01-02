#!/usr/bin/env python3
import os, subprocess, json, time, shutil
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

def speak(msg):
    try:
        subprocess.run(["say", msg])
    except Exception:
        print(f"[Voice] {msg}")

def check_slab(ip):
    return subprocess.run(["ping", "-c", "1", ip], capture_output=True).returncode == 0

def trigger_ritual(name):
    path = os.path.expanduser(RITUALS.get(name, ""))
    if path.endswith('.html'):
        try:
            subprocess.run(["open", path])
            speak(f"{name} overlay launched.")
        except Exception as e:
            print(f"Error opening overlay: {e}")
    elif os.path.exists(path):
        try:
            if name == "capture_memory":
                # Check for 'rec' (sox)
                if not shutil.which("rec"):
                    speak("'rec' command not found. Please install sox: brew install sox")
                    return
            subprocess.run(["python3", path])
            speak(f"{name} triggered.")
        except Exception as e:
            print(f"Error running ritual {name}: {e}")
    else:
        speak(f"Ritual {name} not found.")

def build_capsule():
    capsule = f"Capsule_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    legacy_dir = os.path.expanduser("~/NoizyFish/Legacy/")
    capsule_path = os.path.join(legacy_dir, f"{capsule}.zip")
    if not os.path.exists(legacy_dir):
        os.makedirs(legacy_dir)
    # Only zip if there are files
    if os.listdir(legacy_dir):
        subprocess.run(["zip", "-r", capsule_path, legacy_dir])
        speak(f"Legacy capsule {capsule} built.")
    else:
        speak("Legacy directory is empty. Capsule not built.")

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
