#!/usr/bin/env python3
import os, hashlib, shutil

# Folders to scan for dupes — start small (Desktop + NoizyWorkspace)
targets = [
    os.path.expanduser("~/Desktop"),
    "/Volumes/NoizyWind/NoizyWorkspace"
]

# Where to stash dupes (keeps originals safe)
dupe_dir = os.path.expanduser("~/Documents/_The_Aquarium/_projects/big_dupe_killer/dupes")
os.makedirs(dupe_dir, exist_ok=True)

def filehash(path, blocksize=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(blocksize), b""):
            h.update(chunk)
    return h.hexdigest()

seen = {}
for folder in targets:
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                h = filehash(path)
            except Exception as e:
                print(f"⚠️ Skipped {path}: {e}")
                continue

            if h in seen:
                base = os.path.basename(path)
                dest = os.path.join(dupe_dir, base)
                counter = 1
                while os.path.exists(dest):
                    base_name, ext = os.path.splitext(base)
                    dest = os.path.join(dupe_dir, f"{base_name}_{counter}{ext}")
                    counter += 1
                shutil.move(path, dest)
                print(f"🗑️ Duplicate moved: {path} → {dest}")
            else:
                seen[h] = path

print("✅ Big Dupe Killer finished. Check 'dupes' folder in the project.")
