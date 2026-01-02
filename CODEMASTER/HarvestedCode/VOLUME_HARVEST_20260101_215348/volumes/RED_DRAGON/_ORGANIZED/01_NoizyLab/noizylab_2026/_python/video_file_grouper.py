import os
import shutil
import hashlib
from collections import defaultdict

VOLUMES_ROOT = '/Volumes/'
DUPES_FOLDER = '/Volumes/4TBSG/2025_NOIZYFISH/Video_Dupes'
VIDEO_EXTS = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']

if not os.path.exists(DUPES_FOLDER):
    os.makedirs(DUPES_FOLDER)

# Group files by (name, extension)
video_groups = defaultdict(list)
all_videos = []

# Helper to hash file contents
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
                key = (fname, ext)
                video_groups[key].append(fpath)

# Find and move exact dupes (by hash)
seen_hashes = set()
for group in video_groups.values():
    hashes = {}
    for fpath in group:
        h = file_hash(fpath)
        if h in seen_hashes:
            shutil.move(fpath, os.path.join(DUPES_FOLDER, os.path.basename(fpath)))
            print(f"Duplicate: {fpath} moved to {DUPES_FOLDER}")
        else:
            hashes[h] = fpath
            seen_hashes.add(h)

# Save grouped video list
with open('/Volumes/4TBSG/2025_NOIZYFISH/Python_Codes/grouped_video_files.txt', 'w') as f:
    for key, files in video_groups.items():
        f.write(f"{key}:\n")
        for fpath in files:
            f.write(f"  {fpath}\n")

print("Video files grouped and duplicates moved.")
