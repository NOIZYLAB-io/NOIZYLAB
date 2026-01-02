import os
import shutil

# Source: Mission Control code library
mission_control_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
# Destination: VM drive code library
vm_drive_folder = "/Volumes/NoizyWind/Noizyfish_Aquarium"

# Subfolders to sync
subfolders = ["PY", "TXT", "SH", "MD", "OTHER"]

# Step 1: Ensure VM drive and subfolders exist
os.makedirs(vm_drive_folder, exist_ok=True)
for subfolder in subfolders:
    os.makedirs(os.path.join(vm_drive_folder, subfolder), exist_ok=True)
print(f"✅ VM drive and subfolders created at {vm_drive_folder}")

# Step 2: Sync code files from Mission Control to VM drive
for subfolder in subfolders:
    src_subfolder = os.path.join(mission_control_folder, subfolder)
    dst_subfolder = os.path.join(vm_drive_folder, subfolder)
    if os.path.exists(src_subfolder):
        for filename in os.listdir(src_subfolder):
            src_file = os.path.join(src_subfolder, filename)
            dst_file = os.path.join(dst_subfolder, filename)
            if os.path.isfile(src_file):
                # Avoid overwriting files with the same name
                if not os.path.exists(dst_file):
                    shutil.copy2(src_file, dst_file)
                    print(f"📦 Synced {filename} to VM drive in {subfolder}")
                else:
                    print(f"⚠️ {filename} already exists in VM drive {subfolder}, skipping.")
    else:
        print(f"ℹ️ Source subfolder does not exist: {src_subfolder}")

# Step 3: Sync root-level scripts and files
for filename in os.listdir(mission_control_folder):
    src_file = os.path.join(mission_control_folder, filename)
    dst_file = os.path.join(vm_drive_folder, filename)
    if os.path.isfile(src_file) and not any(src_file.endswith(f"/{sf}") for sf in subfolders):
        if not os.path.exists(dst_file):
            shutil.copy2(src_file, dst_file)
            print(f"📦 Synced root file {filename} to VM drive")
        else:
            print(f"⚠️ Root file {filename} already exists in VM drive, skipping.")

print("🎉 VM drive is now a fully interactive partner to Mission Control. All code and scripts are synced and ready to go!")