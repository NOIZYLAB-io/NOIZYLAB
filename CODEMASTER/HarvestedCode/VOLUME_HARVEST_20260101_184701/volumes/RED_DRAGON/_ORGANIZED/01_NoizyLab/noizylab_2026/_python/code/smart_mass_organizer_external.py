import os
import shutil

VOLUMES_ROOT = '/Volumes/'
EXCLUDE = ['Mission Control']
CATEGORIES = {
    'AUDIO': ['.wav', '.mp3', '.aiff', '.flac', '.ogg', '.m4a'],
    'IMAGE': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'DOCUMENT': ['.pdf', '.docx', '.txt', '.md', '.rtf', '.xlsx', '.csv'],
    'VIDEO': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'PROJECT': ['.logicx', '.als', '.flp', '.ptx', '.rpp', '.cpr'],
    'ARCHIVE': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'CODE': ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.html', '.css', '.json'],
    'OTHER': []
}

def get_category(ext):
    ext = ext.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return 'OTHER'

for volume in os.listdir(VOLUMES_ROOT):
    if volume in EXCLUDE:
        print(f"Skipping {volume} (excluded)")
        continue
    volume_path = os.path.join(VOLUMES_ROOT, volume)
    if not os.path.isdir(volume_path):
        continue
    print(f"Scanning {volume_path}...")
    for fname in os.listdir(volume_path):
        fpath = os.path.join(volume_path, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1]
            category = get_category(ext)
            target_folder = os.path.join(volume_path, f"{category}_FILES")
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(fpath, os.path.join(target_folder, fname))
            print(f"Moved {fname} to {target_folder}")

print("Mass organization complete for all external volumes.")
