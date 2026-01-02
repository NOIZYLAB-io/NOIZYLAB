# NOIZYGRID Orchestrator
# Entry point for fleet automation

import os
import subprocess
from datetime import datetime

LOG_PATH = "/Users/rsp_ms/NOIZYGRID/logs"
ASSET_DIR = "/Users/rsp_ms/NOIZYGRID/assets"
DAEMON_DIR = "/Users/rsp_ms/NOIZYGRID/daemons"

# === UTILS ===
def log(message):
    os.makedirs(LOG_PATH, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(os.path.join(LOG_PATH, "orchestrator.log"), "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"🧾 {message}")

# === ASSET VALIDATION ===
def validate_assets():
    required = ["autounattend.xml", "SetupComplete.cmd", "noizy_slab_rebirth.ps1", "NOIZY.jpg"]
    missing = [f for f in required if not os.path.exists(os.path.join(ASSET_DIR, f))]
    if missing:
        log(f"❌ Missing assets: {', '.join(missing)}")
        return False
    log("✅ All required assets present.")
    return True

# === DAEMON SYNC ===
def sync_daemons():
    for daemon in ["silence.ps1", "log_sync.ps1"]:
        path = os.path.join(DAEMON_DIR, daemon)
        if os.path.exists(path):
            log(f"✅ Daemon ready: {daemon}")
        else:
            log(f"❌ Missing daemon: {daemon}")

# === MAIN ORCHESTRATION ===
def main():
    log("🚦 Starting NOIZYGRID Orchestration...")
    if not validate_assets():
        log("🛑 Orchestration aborted due to missing assets.")
        return
    sync_daemons()
    log("🌟 NOIZYGRID Orchestration complete.")

if __name__ == "__main__":
    main()
