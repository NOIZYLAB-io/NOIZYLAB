import os
import shutil
import subprocess

def save_script_as_txt(code_str, filename="scan_and_move_code_files.txt"):
    folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code_str)
    print(f"✅ Script saved as {file_path}")

# Example usage: save your scan and move script as a .txt file
code = '''
import os
import shutil

aquarium_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
os.makedirs(aquarium_folder, exist_ok=True)
extensions = [".py", ".md", ".sh"]

def scan_and_move(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                src = os.path.join(dirpath, filename)
                dst = os.path.join(aquarium_folder, filename)
                if os.path.exists(dst):
                    base, ext = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(os.path.join(aquarium_folder, f"{base}_{i}{ext}")):
                        i += 1
                    dst = os.path.join(aquarium_folder, f"{base}_{i}{ext}")
                shutil.move(src, dst)
                print(f"📦 Moved {filename} from {dirpath} to Noizyfish_Aquarium")

scan_and_move(os.path.expanduser("~/Documents"))
scan_and_move(os.path.expanduser("~/Desktop"))
scan_and_move("/Volumes/NoizyWind")

print("🎉 All .py, .md, and .sh files have been moved to Noizyfish_Aquarium.")
'''
save_script_as_txt(code)

old_vm_name = "NoizyAI-Win10-Beast-v2"
new_vm_name = "NoizyBeast-Win10"

# Step 1: Rename the Parallels VM
try:
    subprocess.run(["prlctl", "set", old_vm_name, "--name", new_vm_name], check=True)
    print(f"✅ VM renamed from {old_vm_name} to {new_vm_name}")
except Exception as e:
    print(f"❌ Could not rename VM: {e}")

# Step 2: Print VM info for confirmation
try:
    result = subprocess.run(["prlctl", "list", "--all"], capture_output=True, text=True)
    print("Current VM list:\n", result.stdout)
except Exception as e:
    print(f"❌ Could not list VMs: {e}")

print("🎉 VM layout and naming are now updated. You can further organize the VM folder in Finder if needed.")