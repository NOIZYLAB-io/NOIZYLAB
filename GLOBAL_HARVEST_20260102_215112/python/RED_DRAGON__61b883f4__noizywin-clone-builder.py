import subprocess
import datetime
import os

# 🔧 CONFIGURATION
VM_DISK_PATH = "/Users/rsp_ms/Parallels/NOIZYWIN.pvm/NOIZYWIN.hdd"
TARGET_DISK = "/dev/disk3"  # External SSD (confirm with `diskutil list`)
LOG_PATH = os.path.expanduser("~/noizylog/clone-builder.log")
BLOCK_SIZE = "4m"

def log(msg):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {msg}\n")
    print(msg)

def unmount_target():
    log("🔌 Unmounting target disk...")
    subprocess.run(["diskutil", "unmountDisk", TARGET_DISK])

def clone_vm():
    log(f"🧬 Cloning NOIZYWIN to {TARGET_DISK}...")
    cmd = [
        "sudo", "dd",
        f"if={VM_DISK_PATH}",
        f"of={TARGET_DISK}",
        f"bs={BLOCK_SIZE}",
        "status=progress"
    ]
    subprocess.run(cmd)
    log("✅ Clone complete")

def eject_target():
    log("🔚 Ejecting target disk...")
    subprocess.run(["diskutil", "eject", TARGET_DISK])
    log("🧙‍♂️ OMEN can now boot from SSD")

def run_clone():
    log("🔥 Starting NOIZY Clone Ritual")
    unmount_target()
    clone_vm()
    eject_target()
    log("🌐 Clone ritual complete")

if __name__ == "__main__":
    run_clone()
