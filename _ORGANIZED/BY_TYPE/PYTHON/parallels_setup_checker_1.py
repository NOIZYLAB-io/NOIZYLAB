import subprocess
import os
import sys

def check_prlctl():
    try:
        subprocess.run(['prlctl', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ Parallels Desktop CLI (prlctl) is installed.")
        return True
    except Exception:
        print("❌ Parallels Desktop CLI (prlctl) not found. Please install Parallels Desktop for Mac.")
        return False

def check_vscode_extension(extension_id):
    try:
        result = subprocess.run(['code', '--list-extensions'], capture_output=True, text=True)
        if extension_id in result.stdout:
            print(f"✅ VS Code extension '{extension_id}' is installed.")
            return True
        else:
            print(f"❌ VS Code extension '{extension_id}' is missing. Install with:")
            print(f"   code --install-extension {extension_id}")
            return False
    except Exception:
        print("⚠️ Could not check VS Code extensions. Is VS Code CLI ('code') installed and in PATH?")
        return False

def check_iso(iso_path):
    if os.path.isfile(iso_path):
        print(f"✅ Windows 10 ISO found at {iso_path}")
        return True
    else:
        print(f"❌ Windows 10 ISO not found at {iso_path}")
        print("Download it from https://www.microsoft.com/software-download/windows10ISO")
        return False

def list_vms():
    try:
        result = subprocess.run(['prlctl', 'list', '--all'], capture_output=True, text=True)
        print("🖥️ Parallels VMs:\n" + result.stdout)
    except Exception as e:
        print("⚠️ Could not list Parallels VMs:", e)

def main():
    iso_path = "/Users/yourname/Downloads/Win10.iso"  # Change this to your actual ISO path
    extension_id = "ParallelsDesktop.parallels-desktop"

    print("=== Parallels Desktop Setup Checker ===\n")

    if not check_prlctl():
        sys.exit(1)

    check_vscode_extension(extension_id)
    check_iso(iso_path)
    list_vms()

    print("\nIf you run into problems, copy any error messages here and I can help troubleshoot further!")

if __name__ == "__main__":
    main()