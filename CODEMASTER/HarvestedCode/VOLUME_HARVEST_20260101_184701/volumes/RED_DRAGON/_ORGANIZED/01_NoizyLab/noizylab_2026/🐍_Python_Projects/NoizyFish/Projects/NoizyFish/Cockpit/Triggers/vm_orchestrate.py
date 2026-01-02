import subprocess

VM_NAME = "NOIZYWIND"

def get_vm_info():
    subprocess.run(["prlctl", "list", "--info", VM_NAME])

def start_vm():
    subprocess.run(["prlctl", "start", VM_NAME])

def install_guest_tools():
    subprocess.run(["prlctl", "installtools", VM_NAME])

def check_windows_boot():
    subprocess.run(["prlctl", "exec", VM_NAME, "systeminfo"])

def optimize_vm():
    subprocess.run(["prlctl", "set", VM_NAME, "--cpus", "2"])
    subprocess.run(["prlctl", "set", VM_NAME, "--mem", "8192"])
    subprocess.run(["prlctl", "set", VM_NAME, "--tpm", "on"])
    subprocess.run(["prlctl", "set", VM_NAME, "--autostart", "on"])

def main():
    get_vm_info()
    start_vm()
    install_guest_tools()
    check_windows_boot()
    optimize_vm()
    print("✅ Windows 10 VM orchestration complete. Please verify inside Windows.")

if __name__ == "__main__":
    main()
