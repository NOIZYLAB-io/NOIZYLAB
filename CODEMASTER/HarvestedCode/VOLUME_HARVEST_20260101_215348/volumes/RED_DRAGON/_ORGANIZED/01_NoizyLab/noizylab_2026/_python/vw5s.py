import os
import shutil

source_folder = os.path.expanduser("~/Documents/_NOIZYBITZ")
destination_folder = os.path.expanduser("/Users/rsp_ms/Documents/_2026_WDC/_NOIZYBITZ")

if os.path.exists(source_folder):
    if os.path.exists(destination_folder):
        print("⚠️ Destination _NOIZYBITZ already exists in _2026_WDC. Merging contents.")
    shutil.move(source_folder, destination_folder)
    print(f"✅ Moved _NOIZYBITZ to {destination_folder}")
else:
    print("❌ Source _NOIZYBITZ folder not found in Documents.")

print("🎉 All files are now in your _2026_WDC folder. Ready to move forward!")