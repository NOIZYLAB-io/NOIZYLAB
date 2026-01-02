import os
import subprocess
from datetime import datetime

# === CONFIG ===
LOG_PATH = "/usr/local/var/log/noizygrid"
DAEMON_PATH = "/usr/local/bin/noizy_silence.sh"
USERNAME = "rsp_ms"
HOSTNAME = subprocess.getoutput("scutil --get LocalHostName")

# === UTILS ===
def log(msg):
    os.makedirs(LOG_PATH, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{LOG_PATH}/macpro_rebirth.log", "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"🧾 {msg}")

# === 1. SYSTEM SCAN ===
def scan_system():
    log("🔍 Scanning MacPro hardware...")
    specs = subprocess.getoutput("system_profiler SPHardwareDataType SPSoftwareDataType")
    log(specs)

# === 2. PERFORMANCE SNAPSHOT ===
def snapshot_performance():
    log("📊 Capturing performance metrics...")
    metrics = subprocess.getoutput("top -l 1 -n 10")
    log(metrics)

# === 3. SILENCE ENFORCEMENT DAEMON ===
def install_silence_daemon():
    log("🔇 Installing silence daemon...")
    script = f"""#!/bin/bash
pkill -f "VoiceOver"
pkill -f "say"
pkill -f "speechsynth"
echo "$(date) 🔇 {HOSTNAME} silenced" >> {LOG_PATH}/silence.log
"""
    os.makedirs(os.path.dirname(DAEMON_PATH), exist_ok=True)
    with open(DAEMON_PATH, "w") as f:
        f.write(script)
    os.chmod(DAEMON_PATH, 0o755)

    plist = f"""
<?xml version="1.0" encoding="UTF-8"?>
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
    with open("/Library/LaunchDaemons/com.noizygrid.silence.plist", "w") as f:
        f.write(plist)
    subprocess.run(["sudo", "launchctl", "load", "-w", "/Library/LaunchDaemons/com.noizygrid.silence.plist"])
    log("✅ Silence daemon installed and scheduled every 30 minutes.")

# === 4. GRID LINKING ===
def link_to_grid():
    log("🌐 Linking MacPro to NOIZYGRID...")
    result = subprocess.getoutput(f"ssh {USERNAME}@macstudio.local 'echo {HOSTNAME} joined the grid >> ~/NOIZYGRID/nodes.log'")
    log(result)

# === MAIN RITUAL ===
def main():
    log("🌌 Initiating MacPro Rebirth Sequence...")
    scan_system()
    snapshot_performance()
    install_silence_daemon()
    link_to_grid()
    log("🌟 MacPro reborn and linked to NOIZYGRID.")

if __name__ == "__main__":
    main()
