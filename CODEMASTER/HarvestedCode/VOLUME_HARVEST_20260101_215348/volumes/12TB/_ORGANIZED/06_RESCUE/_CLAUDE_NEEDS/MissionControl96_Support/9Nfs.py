#!/usr/bin/env python3
import os, hashlib, shutil

def hash_file(path):
	h = hashlib.sha256()
	with open(path, "rb") as f:
		while chunk := f.read(8192):
			h.update(chunk)
	return h.hexdigest()

def kill_dupes(target_dir, action="quarantine"):
	seen = {}
	dupes = []
	quarantine = os.path.join(target_dir, "_orphans")
	os.makedirs(quarantine, exist_ok=True)

	for root, _, files in os.walk(target_dir):
		for f in files:
			fp = os.path.join(root, f)
			try:
				h = hash_file(fp)
				if h in seen:
					dupes.append(fp)
					if action == "delete":
						os.remove(fp)
					elif action == "quarantine":
						shutil.move(fp, os.path.join(quarantine, f))
				else:
					seen[h] = fp
			except Exception as e:
				print(f"Skipping {fp}: {e}")

	print(f"✅ Done. {len(dupes)} duplicates handled.")

if __name__ == "__main__":
	folder = input("Enter folder to scan: ").strip()
	mode = input("Choose action (delete/quarantine): ").strip()
	kill_dupes(folder, mode)
