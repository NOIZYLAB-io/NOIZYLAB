import os
import shutil

# Set the root directory to scan
root_dir = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
main_scripts_dir = os.path.join(root_dir, "Code/Main_Scripts")
os.makedirs(main_scripts_dir, exist_ok=True)

# Walk through all folders and move .py files
for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".py"):
            src_path = os.path.join(foldername, filename)
            dst_path = os.path.join(main_scripts_dir, filename)
            # Avoid moving files already in the destination
            if os.path.abspath(src_path) != os.path.abspath(dst_path):
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Moved {src_path} to {dst_path}")
                except Exception as e:
                    print(f"Error moving {src_path}: {e}")

print("All .py scripts have been moved to Main_Scripts.")
