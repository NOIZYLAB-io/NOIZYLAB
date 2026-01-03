#!/usr/bin/env python3
import subprocess
import os
import sys

def is_parallels_running():
    try:
        result = subprocess.run(["pgrep", "prl_disp_service"], capture_output=True)
        return result.returncode == 0
    except Exception:
        return False

def list_vms():
    result = subprocess.run(["prlctl", "list", "--all"], capture_output=True, text=True)
    print("Available Parallels VMs:")
    print(result.stdout)
    return result.stdout

def start_vm(vm_name):
    subprocess.run(["prlctl", "start", vm_name])

def setup_shared_folder(vm_name, folder_name, host_path):
    subprocess.run(["prlctl", "set", vm_name, "--shf-host-add", folder_name, "--path", host_path])
    subprocess.run(["prlctl", "set", vm_name, "--shf-host-on", folder_name])

def main():
    if not is_parallels_running():
        print("Parallels Desktop is not running. Please start it first.")
        sys.exit(1)
    vms = list_vms()
    # You may need to edit this VM name
    vm_name = input("Enter the VM name to use: ")
    start_vm(vm_name)
    folder_name = "Noizy_Workspace"
    host_path = os.path.expanduser("~/Documents/Noizyfish_Aquarium/Noizy_Workspace")
    setup_shared_folder(vm_name, folder_name, host_path)
    print(f"Shared folder '{folder_name}' set up for VM '{vm_name}'.")
    print("You can now open VS Code in the VM and access the shared folder.")

if __name__ == "__main__":
    main()
