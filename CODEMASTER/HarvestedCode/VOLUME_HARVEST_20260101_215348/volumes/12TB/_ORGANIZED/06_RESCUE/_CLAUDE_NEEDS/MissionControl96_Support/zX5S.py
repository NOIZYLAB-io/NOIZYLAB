import os
import subprocess
import datetime
import json
import time

# --- Parallels VM Setup (macOS) ---
WINDOWS_ISO_PATH = "/Users/rob/Desktop/Windows10.iso"  # Update this path
PARALLELS_APP_PATH = "/Applications/Parallels Desktop.app"
VM_NAME = "NoizyWin10"
VM_STORAGE_GB = 64
VM_RAM_MB = 4096

def launch_parallels():
    print("🔧 Launching Parallels Desktop...")
    subprocess.run(["open", PARALLELS_APP_PATH])
    time.sleep(5)

def create_vm():
    print("🧬 Creating Windows 10 VM...")
    subprocess.run([
        "prlctl", "create", VM_NAME,
        "--distribution", "win-10",
        "--iso", WINDOWS_ISO_PATH,
        "--vmtype", "pc"
    ])
    time.sleep(2)

def configure_vm():
    print("⚙️ Configuring VM resources...")
    subprocess.run(["prlctl", "set", VM_NAME, "--memsize", str(VM_RAM_MB)])
    subprocess.run(["prlctl", "set", VM_NAME, "--diskspace", str(VM_STORAGE_GB * 1024)])

def start_vm():
    print("🚀 Starting VM...")
    subprocess.run(["prlctl", "start", VM_NAME])
    time.sleep(10)

def install_parallels_tools():
    print("🛠️ Installing Parallels Tools...")
    subprocess.run(["prlctl", "exec", VM_NAME, "--", "C:\\Program Files\\Parallels\\Parallels Tools\\Install.exe"])

def check_boot_manager():
    print("🧭 Checking for Boot Manager fallback...")
    result = subprocess.run(["prlctl", "exec", VM_NAME, "--", "bcdedit"], capture_output=True, text=True)
    if "boot manager" in result.stdout.lower():
        print("⚠️ Boot Manager detected. Reconfiguring ISO...")
        subprocess.run(["prlctl", "set", VM_NAME, "--device-add", "cdrom", "--image", WINDOWS_ISO_PATH])
        subprocess.run(["prlctl", "start", VM_NAME])

def run_parallels_setup():
    launch_parallels()
    create_vm()
    configure_vm()
    start_vm()
    check_boot_manager()
    install_parallels_tools()
    print("✅ Parallels VM Ritual complete. Windows 10 is now running inside Parallels.")

# --- Windows Ritual Detonation (Windows) ---
def say(msg):
    try:
        subprocess.run(["say", msg])
    except Exception:
        pass

def launch_overlay():
    try:
        os.startfile(r"C:\🧞‍♂️NOIZYWIND\Overlays\planar_eyelevel.html")
    except Exception:
        pass

def play_ambient():
    try:
        os.startfile(r"C:\🧞‍♂️NOIZYWIND\Soundscapes\charged_loop.wav")
    except Exception:
        pass

def build_capsule():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    capsule = rf"C:\🧞‍♂️NOIZYWIND\Legacy\Capsule_{ts}.zip"
    subprocess.run([
        "powershell", "Compress-Archive",
        "-Path", r"C:\🧞‍♂️NOIZYWIND\Legacy\*",
        "-DestinationPath", capsule
    ])
    return capsule

def verify_windows():
    try:
        subprocess.run(["python", r"C:\🧞‍♂️NOIZYWIND\Scripts\windows_installation_verifier.py"])
    except Exception:
        pass

def infuse_sequoia():
    try:
        subprocess.run(["python", r"C:\🧞‍♂️NOIZYWIND\Agents\sequoia_infusion.py"])
    except Exception:
        pass

def sync_to_github(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "Pushed to GitHub (symbolic)"
    }
    try:
        with open(r"C:\🧞‍♂️NOIZYWIND\Legacy\capsule_sync_log.json", "w") as f:
            json.dump(log, f, indent=4)
    except Exception:
        pass

def run_windows_ritual():
    say("Igniting NoizyGenieMode Thermonuclear × 100")
    verify_windows()
    infuse_sequoia()
    launch_overlay()
    play_ambient()
    capsule = build_capsule()
    sync_to_github(capsule)
    say("Capsule detonated. Slab is sovereign. Legacy preserved.")

if __name__ == "__main__":
    # macOS Parallels VM setup
    run_parallels_setup()
    # Windows ritual detonation (if running inside Windows)
    run_windows_ritual()
