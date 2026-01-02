import subprocess
import time

VM_NAME = "NOIZYWIND"

def get_vm_info():
    subprocess.run(["prlctl", "list", "--info", VM_NAME])

def start_vm():
    subprocess.run(["prlctl", "start", VM_NAME])

def install_guest_tools():
    subprocess.run(["prlctl", "installtools", VM_NAME])
    print("Please complete Parallels Tools installation inside Windows.")

def wait_for_tools():
    for _ in range(12):
        result = subprocess.getoutput(f"prlctl list --info {VM_NAME}")
        if "GuestTools: state=installed" in result:
            print("✅ Parallels Tools installed.")
            return True
        time.sleep(30)
    print("❌ Parallels Tools not detected. Please install inside Windows.")
    return False

def check_windows_version():
    try:
        result = subprocess.getoutput(f"prlctl exec {VM_NAME} ver")
        print("Windows version output:\n", result)
        if "Microsoft Windows [Version 10" in result:
            print("✅ Windows 10 is installed and detected.")
        else:
            print("❌ Windows 10 not detected. Please verify inside VM.")
    except Exception as e:
        print(f"Error checking Windows version: {e}")

def main():
    get_vm_info()
    start_vm()
    install_guest_tools()
    if wait_for_tools():
        check_windows_version()
    else:
        print("Cannot check Windows version until Parallels Tools are installed.")

if __name__ == "__main__":
    main()
