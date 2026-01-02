import subprocess
import os

VM_NAME = "Windows10"
ISO_PATH = "/Users/rsp_ms/Desktop/Win10_22H2_EnglishInternational_x64v1.iso"

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd)}\n{e.stderr}")
        return None

def prlctl_exists():
    try:
        subprocess.run(['prlctl', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception:
        return False

def iso_exists():
    return os.path.isfile(ISO_PATH)

def vm_exists():
    vms = run_cmd(['prlctl', 'list', '--all'])
    return VM_NAME in vms if vms else False

def get_vm_status(vm_name):
    try:
        result = subprocess.run(['prlctl', 'list', '--all'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if vm_name in line:
                parts = line.split()
                if len(parts) >= 3:
                    return parts[2]  # status column
        return "Not Found"
    except Exception as e:
        return f"Error: {e}"

def create_vm():
    print("Creating VM...")
    run_cmd(['prlctl', 'create', VM_NAME, '--distribution', 'win-10'])

def attach_iso():
    print("Attaching ISO...")
    run_cmd(['prlctl', 'set', VM_NAME, '--device-set', 'cdrom0', '--image', ISO_PATH])

def start_vm():
    print("Starting VM...")
    run_cmd(['prlctl', 'start', VM_NAME])

def main():
    print("=== Parallels Desktop Windows 10 VM Automation ===")
    if not prlctl_exists():
        print("❌ Parallels CLI (prlctl) not found. Please install Parallels Desktop.")
        return
    if not iso_exists():
        print(f"❌ Windows 10 ISO not found at {ISO_PATH}")
        print("Download it from https://www.microsoft.com/software-download/windows10ISO")
        return
    if not vm_exists():
        create_vm()
        attach_iso()
    else:
        print(f"VM '{VM_NAME}' already exists.")
        attach_iso()
    status = get_vm_status(VM_NAME)
    if status == "running":
        print(f"VM '{VM_NAME}' is already running.")
    else:
        start_vm()
    print("\n✅ VM setup automated. Complete Windows installation inside the Parallels window.")

if __name__ == "__main__":
    main()
    os.system('python3 check_parallels_vm_status.py')