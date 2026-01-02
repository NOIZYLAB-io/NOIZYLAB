import os
import subprocess
from datetime import datetime
import sys

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

def run(cmd, require_sudo=False):
    try:
        if require_sudo:
            cmd = f"sudo {cmd}"
        result = subprocess.getoutput(cmd)
        return result
    except Exception as e:
        log(f"❌ Error running '{cmd}': {e}")
        return f"Error: {e}"

# === 1. SYSTEM SCAN ===
def scan_system():
    log("🔍 Scanning MacPro hardware and OS...")
    hw = run("system_profiler SPHardwareDataType SPSoftwareDataType")
    log(hw if hw else "No hardware info found.")

# === 2. PERFORMANCE SNAPSHOT ===
def snapshot_performance():
    log("📊 Capturing performance metrics...")
    top_out = run("top -l 1 -n 10")
    log(top_out if top_out else "No top output.")
    powermetrics_out = run("powermetrics --samplers cpu_power,gpu_power --duration 5", require_sudo=True)
    log(powermetrics_out if powermetrics_out else "No powermetrics output.")

# === 3. SILENCE ENFORCEMENT DAEMON ===
def install_silence_daemon():
    log("🔇 Installing silence daemon...")
    script = f"""#!/bin/bash
pkill -f "VoiceOver"
pkill -f "say"
pkill -f "speechsynth"
echo \"$(date) 🔇 {HOSTNAME} silenced\" >> {LOG_DIR}/silence.log
"""
    try:
        os.makedirs(os.path.dirname(DAEMON_PATH), exist_ok=True)
        with open(DAEMON_PATH, "w") as f:
            f.write(script)
        os.chmod(DAEMON_PATH, 0o755)
    except Exception as e:
        log(f"❌ Failed to create silence daemon: {e}")
        return
    plist = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
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
    try:
        with open(PLIST_PATH, "w") as f:
            f.write(plist)
        run(f"launchctl unload {PLIST_PATH}", require_sudo=True)  # Unload first for idempotency
        run(f"launchctl load -w {PLIST_PATH}", require_sudo=True)
        log("✅ Silence daemon installed and scheduled every 30 minutes.")
    except Exception as e:
        log(f"❌ Failed to install/load plist: {e}")

# === 4. GRID LINKING ===
def link_to_grid():
    log("🌐 Linking MacPro to NOIZYGRID...")
    try:
        os.makedirs(os.path.dirname(REMOTE_LOG), exist_ok=True)
        with open(REMOTE_LOG, "a") as f:
            f.write(f"{datetime.now()} — {HOSTNAME} joined the grid\n")
        log("✅ Grid link confirmed.")
    except Exception as e:
        log(f"❌ Grid link failed: {e}")

# === 5. LEGACY SNAPSHOT ===
def legacy_snapshot():
    log("📦 Capturing legacy snapshot...")
    snapshot = run("tmutil listbackups | tail -1")
    log(f"🗂️ Last Time Machine backup: {snapshot}")
    snap_result = run("tmutil snapshot")
    log(f"✅ Local snapshot created. {snap_result}")

# === 6. NOTIFICATION ===
def notify():
    try:
        run(f"osascript -e 'display notification \"MacPro rebirth complete!\" with title \"NOIZYGRID\"'", require_sudo=False)
        run(f"afplay /System/Library/Sounds/Glass.aiff", require_sudo=False)
    except Exception as e:
        log(f"❌ Notification failed: {e}")

# === MAIN RITUAL ===
def main():
    log("🌌 Initiating MacPro Rebirth Sequence v3 (Best)...")
    scan_system()
    snapshot_performance()
    install_silence_daemon()
    link_to_grid()
    legacy_snapshot()
    notify()
    log("🌟 MacPro reborn, silenced, and mythically linked to NOIZYGRID.")

if __name__ == "__main__":
    main()
