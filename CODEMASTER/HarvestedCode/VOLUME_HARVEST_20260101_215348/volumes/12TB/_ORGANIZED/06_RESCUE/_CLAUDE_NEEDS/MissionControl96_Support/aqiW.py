import os
import subprocess
from datetime import datetime

# === CONFIG ===
USERNAME = "rsp_ms"
HOSTNAME = subprocess.getoutput("scutil --get LocalHostName")
LOG_DIR = f"/Users/{USERNAME}/NOIZYGRID_LOGS"
REMOTE_LOG = f"/Users/{USERNAME}/NOIZYGRID/nodes.log"
DAEMON_PATH = "/usr/local/bin/noizy_silence.sh"
PLIST_PATH = "/Library/LaunchDaemons/com.noizygrid.silence.plist"

# === UTILS ===
def log(msg):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{LOG_DIR}/macpro_mythic.log", "a") as f:
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
    log(run("sudo powermetrics --samplers cpu_power,gpu_power --duration 5"))

# === 3. THERMAL MONITORING ===
def monitor_thermal():
    log("🌡️ Monitoring thermal status...")
    temps = run("sudo powermetrics --samplers smc | grep -i 'temperature'")
    log(temps)

# === 4. SILENCE ENFORCEMENT ===
def enforce_silence():
    log("🔇 Enforcing silence now...")
    result = run(f"bash {DAEMON_PATH}")
    log(result)

# === 5. DAEMON HEALTH CHECK ===
def check_daemon():
    log("🧪 Checking silence daemon status...")
    status = run(f"sudo launchctl list | grep com.noizygrid.silence")
    if status:
        log("✅ Silence daemon is active.")
    else:
        log("❌ Silence daemon not found. Reinstalling...")
        install_silence_daemon()

# === 6. SILENCE DAEMON INSTALLER ===
def install_silence_daemon():
    script = f"""#!/bin/bash
pkill -f "VoiceOver"
pkill -f "say"
pkill -f "speechsynth"
echo \"$(date) 🔇 {HOSTNAME} silenced\" >> {LOG_DIR}/silence.log
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
    log("✅ Silence daemon installed and scheduled.")

# === 7. GRID SYNC ===
def sync_to_grid():
    log("🌐 Syncing MacPro to NOIZYGRID...")
    with open(REMOTE_LOG, "a") as f:
        f.write(f"{datetime.now()} — {HOSTNAME} status synced\n")
    log("✅ Grid sync complete.")

# === 8. LEGACY SNAPSHOT ===
def legacy_snapshot():
    log("📦 Capturing legacy snapshot...")
    snapshot = run("tmutil listbackups | tail -1")
    log(f"🗂️ Last Time Machine backup: {snapshot}")
    run(f"tmutil snapshot")
    log("✅ Local snapshot created.")

# === MAIN ENGINE ===
def main():
    log("🌌 Launching MacPro Mythic Intelligence Engine...")
    scan_system()
    snapshot_performance()
    monitor_thermal()
    check_daemon()
    enforce_silence()
    sync_to_grid()
    legacy_snapshot()
    log("🌟 MacPro reborn, silenced, monitored, and mythically linked to NOIZYGRID.")

if __name__ == "__main__":
    main()
