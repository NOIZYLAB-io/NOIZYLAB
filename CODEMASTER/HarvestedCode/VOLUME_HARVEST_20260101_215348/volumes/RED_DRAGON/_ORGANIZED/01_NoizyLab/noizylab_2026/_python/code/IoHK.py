import os
import shutil

aquarium_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
py_folder = os.path.join(aquarium_folder, "PY")
current_folder = os.path.join(aquarium_folder, "CURRENT")
master_folder = os.path.join(aquarium_folder, "PY_MASTER")

os.makedirs(current_folder, exist_ok=True)
os.makedirs(master_folder, exist_ok=True)

# Define which files are "current" and which are "master"
current_files = ["app.py", "setup_project.py", "automate_parallels_win10.py"]  # Add more as needed
master_files = ["noizy_ai_architecture.py", "volume_manager.py", "audio_api.py"]  # Add more as needed

for filename in os.listdir(py_folder):
    src = os.path.join(py_folder, filename)
    if filename in current_files:
        dst = os.path.join(current_folder, filename)
        shutil.move(src, dst)
        print(f"📦 Moved {filename} to CURRENT folder")
    elif filename in master_files:
        dst = os.path.join(master_folder, filename)
        shutil.move(src, dst)
        print(f"📦 Moved {filename} to PY_MASTER folder")
    else:
        print(f"ℹ️ {filename} left in PY folder (not classified as current or master)")

print("🎉 Python scripts have been organized into CURRENT and PY_MASTER folders as requested.")