import os
import subprocess
import time

# CONFIGURATION
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

def run_setup():
    launch_parallels()
    create_vm()
    configure_vm()
    start_vm()
    check_boot_manager()
    install_parallels_tools()
    print("✅ Ritual complete. Windows 10 is now running inside Parallels.")

if __name__ == "__main__":
    run_setup()
