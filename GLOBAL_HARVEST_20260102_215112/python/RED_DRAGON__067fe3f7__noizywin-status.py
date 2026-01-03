import subprocess

VM_NAME = "NOIZYWIN"

def check_vm_status():
    print("🧭 Checking VM status...")
    subprocess.run(["prlctl", "list", "--all"])

def check_drive_info():
    print("💽 Checking VM drive info...")
    subprocess.run(["prlctl", "list", "-i", VM_NAME])

def check_os_version():
    print("🧠 Checking Windows version...")
    subprocess.run(["prlctl", "exec", VM_NAME, "ver"])
    subprocess.run(["prlctl", "exec", VM_NAME, "systeminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\""])

if __name__ == "__main__":
    check_vm_status()
    check_drive_info()
    check_os_version()
