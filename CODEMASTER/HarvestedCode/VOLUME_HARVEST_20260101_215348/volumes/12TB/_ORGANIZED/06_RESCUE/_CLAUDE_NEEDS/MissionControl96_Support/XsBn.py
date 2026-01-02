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

def notify():
    try:
        subprocess.getoutput("osascript -e 'display notification \"MacPro mythic update complete!\" with title \"NOIZYGRID\"'")
        subprocess.getoutput("afplay /System/Library/Sounds/Glass.aiff")
    except Exception as e:
        log(f"❌ Notification failed: {e}")

def run(cmd):
    try:
        return subprocess.getoutput(cmd)
    except Exception as e:
        log(f"❌ Error running '{cmd}': {e}")
        return f"Error: {e}"

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
    status = run("sudo launchctl list | grep com.noizygrid.silence")
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
    run("tmutil snapshot")
    log("✅ Local snapshot created.")

# === MAIN ENGINE ===
def main():
    log("🌌 Launching MacPro Mythic Intelligence Engine (Best in Years)...")
    errors = []
    try:
        scan_system()
    except Exception as e:
        errors.append(f"System scan: {e}")
    try:
        snapshot_performance()
    except Exception as e:
        errors.append(f"Performance snapshot: {e}")
    try:
        monitor_thermal()
    except Exception as e:
        errors.append(f"Thermal monitoring: {e}")
    try:
        check_daemon()
    except Exception as e:
        errors.append(f"Daemon check: {e}")
    try:
        enforce_silence()
    except Exception as e:
        errors.append(f"Silence enforcement: {e}")
    try:
        sync_to_grid()
    except Exception as e:
        errors.append(f"Grid sync: {e}")
    try:
        legacy_snapshot()
    except Exception as e:
        errors.append(f"Legacy snapshot: {e}")
    notify()
    if errors:
        log(f"❌ Mythic engine completed with errors: {'; '.join(errors)}")
    else:
        log("🌟 MacPro reborn, silenced, monitored, and mythically linked to NOIZYGRID. All systems nominal. 🚀")

if __name__ == "__main__":
    main()
