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
    with open(f"{LOG_DIR}/macpro_dashboard.log", "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"🧾 {msg}")

def run(cmd):
    return subprocess.getoutput(cmd)

# === 1. STATUS SCAN ===
def scan_status():
    log("🔍 Scanning MacPro status...")
    uptime = run("uptime")
    cpu = run("sysctl -n machdep.cpu.brand_string")
    mem = run("sysctl hw.memsize")
    log(f"🧠 CPU: {cpu}")
    log(f"🧠 RAM: {int(mem)//(1024**3)} GB")
    log(f"⏱️ Uptime: {uptime}")

# === 2. DAEMON HEALTH CHECK ===
def check_daemon():
    log("🧪 Checking silence daemon status...")
    status = run(f"sudo launchctl list | grep com.noizygrid.silence")
    if status:
        log("✅ Silence daemon is active.")
    else:
        log("❌ Silence daemon not found. Reinstalling...")
        install_silence_daemon()

# === 3. SILENCE ENFORCEMENT ===
def enforce_silence():
    log("🔇 Enforcing silence now...")
    result = run(f"bash {DAEMON_PATH}")
    log(result)

# === 4. GRID SYNC ===
def sync_to_grid():
    log("🌐 Syncing MacPro to NOIZYGRID...")
    with open(REMOTE_LOG, "a") as f:
        f.write(f"{datetime.now()} — {HOSTNAME} status synced\n")
    log("✅ Grid sync complete.")

# === 5. SILENCE DAEMON INSTALLER ===
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

# === MAIN DASHBOARD ===
def main():
    log("🌌 Launching MacPro Dashboard...")
    scan_status()
    check_daemon()
    enforce_silence()
    sync_to_grid()
    log("🌟 MacPro status updated and synced to NOIZYGRID.")

if __name__ == "__main__":
    main()
