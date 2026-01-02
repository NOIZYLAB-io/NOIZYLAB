import os
import shutil
import subprocess

# Paths
ISO_ORIG = os.path.expanduser("~/Downloads/Win11_25H2_ARM64.iso")
ISO_NEW = os.path.expanduser("~/Desktop/NOIZYWIN.iso")
BUILD_DIR = os.path.expanduser("~/NOIZYWIN_BUILD")
MOUNT_DIR = "/Volumes/NOIZYISO"

ASSET_DIR = os.path.expanduser("~/NOIZYWIN_ASSETS")
ASSETS = {
    "autounattend.xml": os.path.join(ASSET_DIR, "autounattend.xml"),
    "SetupComplete.cmd": os.path.join(ASSET_DIR, "SetupComplete.cmd"),
    "noizy_slab_rebirth.ps1": os.path.join(ASSET_DIR, "noizy_slab_rebirth.ps1"),
    "NOIZY.jpg": os.path.join(ASSET_DIR, "NOIZY.jpg")
}

def mount_iso():
    subprocess.run(["hdiutil", "mount", ISO_ORIG, "-mountpoint", MOUNT_DIR], check=True)

def unmount_iso():
    subprocess.run(["hdiutil", "unmount", MOUNT_DIR], check=True)

def copy_iso_contents():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    shutil.copytree(MOUNT_DIR, BUILD_DIR)

def inject_assets():
    oem_path = os.path.join(BUILD_DIR, "sources", "$OEM$", "$1")
    os.makedirs(oem_path, exist_ok=True)
    for name, path in ASSETS.items():
        shutil.copy(path, oem_path)

def build_new_iso():
    subprocess.run([
        "hdiutil", "makehybrid",
        "-o", ISO_NEW,
        BUILD_DIR,
        "-iso", "-joliet"
    ], check=True)

def main():
    print("🔮 Starting NOIZYWIN ISO build...")
    mount_iso()
    copy_iso_contents()
    unmount_iso()
    inject_assets()
    build_new_iso()
    print(f"✅ Mythic ISO built: {ISO_NEW}")

if __name__ == "__main__":
    main()
