import os
import shutil

# Target folder
aquarium_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
os.makedirs(aquarium_folder, exist_ok=True)

# Extensions to scan for
extensions = [".py", ".md", ".sh"]

def scan_and_move(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                src = os.path.join(dirpath, filename)
                dst = os.path.join(aquarium_folder, filename)
                # Avoid overwriting files with the same name
                if os.path.exists(dst):
                    base, ext = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(os.path.join(aquarium_folder, f"{base}_{i}{ext}")):
                        i += 1
                    dst = os.path.join(aquarium_folder, f"{base}_{i}{ext}")
                shutil.move(src, dst)
                print(f"📦 Moved {filename} from {dirpath} to Noizyfish_Aquarium")

# Scan root folders (Documents, Desktop, external drives, etc.)
scan_and_move(os.path.expanduser("~/Documents"))
scan_and_move(os.path.expanduser("~/Desktop"))
scan_and_move("/Volumes/NoizyWind")

print("🎉 All .py, .md, and .sh files have been moved to Noizyfish_Aquarium.")