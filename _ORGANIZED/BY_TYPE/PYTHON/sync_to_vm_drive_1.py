import os
import shutil
import subprocess

main_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
vm_folder = "/Volumes/NoizyWind/Noizyfish_Aquarium"

os.makedirs(vm_folder, exist_ok=True)

for root, dirs, files in os.walk(main_folder):
    rel_path = os.path.relpath(root, main_folder)
    target_dir = os.path.join(vm_folder, rel_path)
    os.makedirs(target_dir, exist_ok=True)
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(target_dir, file)
        if not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"📦 Synced {file} to VM drive")

print("✅ Noizyfish_Aquarium is now organized and synced on both drives.")

def play_droplet_sound():
    sound_path = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium/droplet.wav"  # Update path as needed
    subprocess.run(["afplay", sound_path])

# Example usage after successful code execution
print("✅ Code ran successfully!")
play_droplet_sound()