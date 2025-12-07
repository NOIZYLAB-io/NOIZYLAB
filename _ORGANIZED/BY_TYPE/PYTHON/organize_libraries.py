import os
import shutil

# Destination folder on Desktop
desktop = os.path.expanduser("~/Desktop")
dest_folder = os.path.join(desktop, "Cymatics")
os.makedirs(dest_folder, exist_ok=True)

# Volumes to search
volumes_root = "/Volumes"
for volume in os.listdir(volumes_root):
    volume_path = os.path.join(volumes_root, volume)
    if os.path.isdir(volume_path):
        for root, dirs, files in os.walk(volume_path):
            # Move matching folders
            for d in dirs:
                if d.lower() == "cymatics":
                    src = os.path.join(root, d)
                    dst = os.path.join(dest_folder, d)
                    try:
                        shutil.move(src, dst)
                        print(f"Moved folder: {src} -> {dst}")
                    except Exception as e:
                        print(f"Error moving folder {src}: {e}")
            # Move matching files
            for f in files:
                if "cymatics" in f.lower():
                    src = os.path.join(root, f)
                    dst = os.path.join(dest_folder, f)
                    try:
                        shutil.move(src, dst)
                        print(f"Moved file: {src} -> {dst}")
                    except Exception as e:
                        print(f"Error moving file {src}: {e}")