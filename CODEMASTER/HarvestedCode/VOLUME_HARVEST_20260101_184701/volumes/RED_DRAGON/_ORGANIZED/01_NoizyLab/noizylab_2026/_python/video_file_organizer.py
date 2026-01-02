import os
import shutil
import hashlib

# Folders to scan for video files
VOLUMES_ROOT = '/Volumes/'
TARGET_FOLDER = '/Volumes/4TBSG/2025_NOIZYFISH/2025 Projects/Noizy Fish/Pardon Me'
DUPES_FOLDER = '/Volumes/4TBSG/2025_NOIZYFISH/Video_Dupes'
VIDEO_EXTS = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']

if not os.path.exists(TARGET_FOLDER):
    os.makedirs(TARGET_FOLDER)
if not os.path.exists(DUPES_FOLDER):
    os.makedirs(DUPES_FOLDER)

video_files = {}
all_videos = []

def file_hash(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Scan all external volumes for video files
for volume in os.listdir(VOLUMES_ROOT):
    volume_path = os.path.join(VOLUMES_ROOT, volume)
    if not os.path.isdir(volume_path):
        continue
    for root, dirs, files in os.walk(volume_path):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext in VIDEO_EXTS:
                fpath = os.path.join(root, fname)
                all_videos.append(fpath)
                h = file_hash(fpath)
                if h in video_files:
                    # Duplicate found
                    shutil.move(fpath, os.path.join(DUPES_FOLDER, fname))
                    print(f"Duplicate: {fname} moved to {DUPES_FOLDER}")
                else:
                    video_files[h] = fpath

# Move unique video files to target folder
for fpath in video_files.values():
    fname = os.path.basename(fpath)
    shutil.move(fpath, os.path.join(TARGET_FOLDER, fname))
    print(f"Moved: {fname} to {TARGET_FOLDER}")

# Save list of all video files
with open('/Volumes/4TBSG/2025_NOIZYFISH/Python_Codes/all_video_files.txt', 'w') as f:
    for fpath in all_videos:
        f.write(fpath + '\n')

print("Video file organization complete.")
