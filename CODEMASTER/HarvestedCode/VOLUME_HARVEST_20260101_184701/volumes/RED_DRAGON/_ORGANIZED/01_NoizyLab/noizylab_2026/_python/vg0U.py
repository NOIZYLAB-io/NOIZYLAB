import os
import shutil

aquarium_folder = "/Users/rsp_ms/Documents/Noizyfish_Aquarium"
folders = {
    ".py": "PY",
    ".sh": "SH",
    ".md": "MD",
    ".txt": "TXT"
}

# Ensure destination folders exist
for folder in folders.values():
    os.makedirs(os.path.join(aquarium_folder, folder), exist_ok=True)

def move_file(src, dst_folder):
    filename = os.path.basename(src)
    dst = os.path.join(dst_folder, filename)
    # Avoid overwriting files with the same name
    if os.path.exists(dst):
        base, ext = os.path.splitext(filename)
        i = 1
        while os.path.exists(os.path.join(dst_folder, f"{base}_{i}{ext}")):
            i += 1
        dst = os.path.join(dst_folder, f"{base}_{i}{ext}")
    shutil.move(src, dst)
    print(f"📦 Moved {filename} to {dst_folder}")

# Scan all external drives in /Volumes
for volume in os.listdir("/Volumes"):
    volume_path = os.path.join("/Volumes", volume)
    if os.path.ismount(volume_path) and volume not in ("Macintosh HD", "MacintoshHD", "Macintosh HD - Data"):
        for dirpath, dirnames, filenames in os.walk(volume_path):
            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in folders:
                    src = os.path.join(dirpath, filename)
                    dst_folder = os.path.join(aquarium_folder, folders[ext])
                    move_file(src, dst_folder)

print("🎉 All .py, .sh, .md, and .txt files from all external drives have been moved to Noizyfish_Aquarium.")
