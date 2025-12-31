# OMEN_Sentinel Agent
# Remote control, healing, silence enforcement, and log sync

import os
import subprocess
import requests
from datetime import datetime

DASHBOARD_URL = "http://localhost:5000/api/status"
LOG_PATH = "C:/OMEN_Sentinel/logs/omen_agent.log"

# === UTILS ===
def log(msg):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"🧾 {msg}")

def sync_status():
    try:
        status = {
            "sentinel": "online",
            "healing": "active",
            "silence": "enforced",
            "timestamp": datetime.now().isoformat()
        }
        requests.post(DASHBOARD_URL, json=status)
        log("Status synced to dashboard.")
    except Exception as e:
        log(f"Dashboard sync failed: {e}")

def enforce_silence():
    # Example: mute system sound
    try:
        subprocess.run(["nircmd.exe", "mutesysvolume", "1"])
        log("Silence enforced.")
    except Exception as e:
        log(f"Silence enforcement failed: {e}")

def heal():
    # Example: restart a service
    try:
        subprocess.run(["powershell", "Restart-Service", "WinRM"])
        log("Healing triggered.")
    except Exception as e:
        log(f"Healing failed: {e}")

if __name__ == "__main__":
    log("OMEN_Sentinel agent started.")
    enforce_silence()
    heal()
    sync_status()
    log("OMEN_Sentinel agent completed.")
