import os
import subprocess
from datetime import datetime

# === CONFIG ===
USERNAME = "rsp_ms"
HOSTNAME = subprocess.getoutput("scutil --get LocalHostName")
LOG_DIR = f"/Users/{USERNAME}/NOIZYGRID_LOGS"
DAEMON_PATH = "/usr/local/bin/noizy_silence.sh"
PLIST_PATH = "/Library/LaunchDaemons/com.noizygrid.silence.plist"
REMOTE_LOG = f"/Users/{USERNAME}/NOIZYGRID/nodes.log"

# === UTILS ===
def log(msg):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{LOG_DIR}/macpro_rebirth.log", "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"🧾 {msg}")

def run(cmd):
    return subprocess.getoutput(cmd)

# === 1. SYSTEM SCAN ===
def scan_system():
    log("🔍 Scanning MacPro hardware and OS...")
    log(run("system_profiler SPHardwareDataType SPSoftwareDataType"))

# === 2. PERFORMANCE SNAPSHOT ===
def snapshot_performance():
    log("📊 Capturing performance metrics...")
    log(run("top -l 1 -n 10"))

# === 3. SILENCE ENFORCEMENT DAEMON ===
def install_silence_daemon():
    log("🔇 Installing silence daemon...")
    script = f"""#!/bin/bash
pkill -f "VoiceOver"
pkill -f "say"
pkill -f "speechsynth"
echo "$(date) 🔇 {HOSTNAME} silenced" >> {LOG_DIR}/silence.log
"""
    os.makedirs(os.path.dirname(DAEMON_PATH), exist_ok=True)
    with open(DAEMON_PATH, "w") as f:
        f.write(script)
    os.chmod(DAEMON_PATH, 0o755)

    plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizygrid.silence</string>
    <key>ProgramArguments</key>
    <array>
        <string>{DAEMON_PATH}</string>
    </array>
    <key>StartInterval</key>
    <integer>1800</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""
    with open(PLIST_PATH, "w") as f:
        f.write(plist)
    run(f"sudo launchctl load -w {PLIST_PATH}")
    log("✅ Silence daemon installed and scheduled every 30 minutes.")

# === 4. GRID LINKING ===
def link_to_grid():
    log("🌐 Linking MacPro to NOIZYGRID...")
    with open(REMOTE_LOG, "a") as f:
        f.write(f"{datetime.now()} — {HOSTNAME} joined the grid\n")
    log("✅ Grid link confirmed.")

# === MAIN RITUAL ===
def main():
    log("🌌 Initiating MacPro Rebirth Sequence v2...")
    scan_system()
    snapshot_performance()
    install_silence_daemon()
    link_to_grid()
    log("🌟 MacPro reborn, silenced, and linked to NOIZYGRID.")

if __name__ == "__main__":
    main()
