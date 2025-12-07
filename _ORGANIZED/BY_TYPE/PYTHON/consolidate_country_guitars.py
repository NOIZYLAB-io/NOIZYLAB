import os
import shutil
import hashlib

# Source folders
base = '/Volumes/RED DRAGON/ BFA Libraries'
sources = [
    'BFA - Country Guitars',
    'BFA - Country Guitars - KLI',
    'BFA - Country Roots',
    'BFA - Country Roots - KLI',
    'BFA - Country Roots - KLIa',
    'BFA - Country Roots - KLIb'
]
master = os.path.join(base, 'BFA - COUNTRY_GUITARS')
os.makedirs(master, exist_ok=True)

# Helper: get file hash
def file_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

# Track seen files by hash
seen = {}

# Move and deduplicate
for src in sources:
    src_path = os.path.join(base, src)
    for root, dirs, files in os.walk(src_path):
        for file in files:
            fpath = os.path.join(root, file)
            try:
                h = file_hash(fpath)
            except Exception:
                continue
            if h in seen:
                # Duplicate, delete
                os.remove(fpath)
                print(f"Deleted duplicate: {fpath}")
            else:
                # Move to master, preserve subfolder structure
                rel = os.path.relpath(root, src_path)
                dest_dir = os.path.join(master, rel)
                os.makedirs(dest_dir, exist_ok=True)
                dest = os.path.join(dest_dir, file)
                shutil.move(fpath, dest)
                seen[h] = dest
                print(f"Moved: {fpath} -> {dest}")

# Remove empty folders
for src in sources:
    src_path = os.path.join(base, src)
    for root, dirs, files in os.walk(src_path, topdown=False):
        for d in dirs:
            dpath = os.path.join(root, d)
            if not os.listdir(dpath):
                os.rmdir(dpath)
                print(f"Deleted empty folder: {dpath}")
    # Remove source folder if empty
    if not os.listdir(src_path):
        os.rmdir(src_path)
        print(f"Deleted empty source folder: {src_path}")

print("Consolidation complete. All unique files are in BFA - COUNTRY_GUITARS.")
