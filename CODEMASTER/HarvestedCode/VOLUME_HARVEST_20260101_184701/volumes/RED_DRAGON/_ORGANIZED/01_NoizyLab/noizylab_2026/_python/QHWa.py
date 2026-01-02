import os
import shutil

# Paths
base_dir = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium/00_Noizy_Workspace/GitHub/Projects"
main_scripts_dir = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium/Code/Main_Scripts"
templates_dir = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium/Code/Templates"
history_dir = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium/Code/History"

# Keywords for grouping
main_keywords = ["noizyfish", "noizy.ai"]
template_keywords = ["template"]
history_folder = ".history"

# Helper function to move files
def move_file(src, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)
    dst = os.path.join(dst_folder, os.path.basename(src))
    shutil.move(src, dst)
    print(f"Moved {src} to {dst_folder}")

# Organize main scripts and templates
for root, dirs, files in os.walk(base_dir):
    for file in files:
        file_lower = file.lower()
        src_path = os.path.join(root, file)
        if history_folder in root:
            move_file(src_path, history_dir)
        elif any(kw in file_lower for kw in main_keywords):
            move_file(src_path, main_scripts_dir)
        elif any(kw in file_lower for kw in template_keywords):
            move_file(src_path, templates_dir)

print("Noizyfish organization complete. All scripts are grouped and ready.")
