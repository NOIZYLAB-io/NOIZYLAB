import os
import shutil

source_folder = os.path.expanduser("~/Documents/_NOIZYBITZ")
destination_folder = os.path.expanduser("/Users/rsp_ms/Documents/_2026_WDC/_NOIZYBITZ")

noizybitz_folder = os.path.expanduser("~/Documents/_NOIZYBITZ")

if os.path.exists(noizybitz_folder):
    if not os.listdir(noizybitz_folder):  # Folder is empty
        shutil.rmtree(noizybitz_folder)
        print("✅ _NOIZYBITZ folder was empty and has been deleted.")
    else:
        print("⚠️ _NOIZYBITZ folder exists but is not empty. No action taken.")
else:
    print("ℹ️ _NOIZYBITZ folder does not exist. No action needed.")

if os.path.exists(source_folder):
    if os.path.exists(destination_folder):
        print("⚠️ Destination _NOIZYBITZ already exists in _2026_WDC. Merging contents.")
    shutil.move(source_folder, destination_folder)
    print(f"✅ Moved _NOIZYBITZ to {destination_folder}")
else:
    print("❌ Source _NOIZYBITZ folder not found in Documents.")

print("🎉 All files are now in your _2026_WDC folder. Ready to move forward!")

# Define folder paths
main_drive_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
vm_drive_folder = "/Volumes/NoizyWind/Noizyfish_Aquarium"

def check_and_create(folder_path):
    if os.path.exists(folder_path):
        print(f"✅ Folder exists: {folder_path}")
    else:
        os.makedirs(folder_path, exist_ok=True)
        print(f"📁 Folder created: {folder_path}")

print("Checking Noizyfish_Aquarium on main drive...")
check_and_create(main_drive_folder)

print("Checking Noizyfish_Aquarium on VM/external drive...")
check_and_create(vm_drive_folder)

print("🎉 Check and creation complete for Noizyfish_Aquarium on both drives.")