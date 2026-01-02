import os
import shutil
import subprocess
import traceback
import datetime

# Paths
ISO_ORIG = os.path.expanduser("~/Downloads/Win11_25H2_ARM64.iso")
ISO_NEW = os.path.expanduser("~/Desktop/NOIZYWIN.iso")
BUILD_DIR = os.path.expanduser("~/NOIZYWIN_BUILD")
MOUNT_DIR = "/Volumes/NOIZYISO"
LOG_DIR = os.path.expanduser("~/Desktop/MissionControl96/logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "isobuilder.log")
ERR_FILE = os.path.join(LOG_DIR, "isobuilder.err")

ASSET_DIR = os.path.expanduser("~/NOIZYWIN_ASSETS")
ASSETS = {
    "autounattend.xml": os.path.join(ASSET_DIR, "autounattend.xml"),
    "SetupComplete.cmd": os.path.join(ASSET_DIR, "SetupComplete.cmd"),
    "noizy_slab_rebirth.ps1": os.path.join(ASSET_DIR, "noizy_slab_rebirth.ps1"),
    "NOIZY.jpg": os.path.join(ASSET_DIR, "NOIZY.jpg")
}

def log(msg):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {msg}\n")
    print(msg)

def log_error(msg):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(ERR_FILE, "a") as f:
        f.write(f"{timestamp} {msg}\n")
    print(msg)

def mount_iso():
    try:
        log(f"Mounting ISO: {ISO_ORIG}")
        subprocess.run(["hdiutil", "mount", ISO_ORIG, "-mountpoint", MOUNT_DIR], check=True)
    except Exception as e:
        log_error(f"Failed to mount ISO: {e}\n{traceback.format_exc()}")
        raise

def unmount_iso():
    try:
        log(f"Unmounting ISO from: {MOUNT_DIR}")
        subprocess.run(["hdiutil", "unmount", MOUNT_DIR], check=True)
    except Exception as e:
        log_error(f"Failed to unmount ISO: {e}\n{traceback.format_exc()}")
        raise

def copy_iso_contents():
    try:
        log(f"Copying ISO contents to build dir: {BUILD_DIR}")
        if os.path.exists(BUILD_DIR):
            shutil.rmtree(BUILD_DIR)
        shutil.copytree(MOUNT_DIR, BUILD_DIR)
    except Exception as e:
        log_error(f"Failed to copy ISO contents: {e}\n{traceback.format_exc()}")
        raise

def inject_assets():
    try:
        oem_path = os.path.join(BUILD_DIR, "sources", "$OEM$", "$1")
        os.makedirs(oem_path, exist_ok=True)
        for name, path in ASSETS.items():
            if os.path.isfile(path):
                shutil.copy(path, oem_path)
                log(f"Injected asset: {name}")
            else:
                log_error(f"Missing asset during injection: {name}")
    except Exception as e:
        log_error(f"Failed to inject assets: {e}\n{traceback.format_exc()}")
        raise

def build_new_iso():
    try:
        log(f"Building new ISO: {ISO_NEW}")
        subprocess.run([
            "hdiutil", "makehybrid",
            "-o", ISO_NEW,
            BUILD_DIR,
            "-iso", "-joliet"
        ], check=True)
    except Exception as e:
        log_error(f"Failed to build new ISO: {e}\n{traceback.format_exc()}")
        raise

def check_assets():
    missing = []
    for name, path in ASSETS.items():
        if not os.path.isfile(path):
            missing.append(name)
    if missing:
        log_error(f"Missing assets: {', '.join(missing)}")
        return False
    return True

def optimize_mac_resources():
    try:
        log("Optimizing Mac resources for automation...")
        subprocess.run(["osascript", "-e", 'quit app "Safari"'], check=True)
        subprocess.run(["osascript", "-e", 'quit app "Mail"'], check=True)
        subprocess.run(["osascript", "-e", 'quit app "Messages"'], check=True)
        subprocess.run(["osascript", "-e", 'quit app "Photos"'], check=True)
        subprocess.run(["osascript", "-e", 'quit app "Music"'], check=True)

        for daemon in ["mdworker", "photoanalysisd", "CalendarAgent", "remindd", "AddressBookSourceSync"]:
            subprocess.run(["sudo", "pkill", "-f", daemon], check=True)

        subprocess.run(["sudo", "purge"], check=True)
        log("Mac resources optimized.")
    except Exception as e:
        log_error(f"Failed to optimize Mac resources: {e}\n{traceback.format_exc()}")

    try:
        log("Running noizygrid optimization script...")
        subprocess.run(["sudo", "bash", "noizygrid-optimize.sh"], check=True)
        log("Noizygrid optimization completed.")
    except Exception as e:
        log_error(f"Failed to run noizygrid optimization: {e}\n{traceback.format_exc()}")

def main():
    log("🔮 Starting NOIZYWIN ISO build...")
    if not check_assets():
        log_error("⚠️ Build aborted due to missing assets. Move required files to ~/NOIZYWIN_ASSETS/.")
        return
    try:
        optimize_mac_resources()
        mount_iso()
        copy_iso_contents()
        unmount_iso()
        inject_assets()
        build_new_iso()
        log(f"✅ Mythic ISO built: {ISO_NEW}")
    except Exception as e:
        log_error(f"Build failed: {e}")

if __name__ == "__main__":
    main()
