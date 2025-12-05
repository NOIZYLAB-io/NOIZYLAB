import os
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
OUTPUT = ROOT / "PROJECT_ORGANIZER" / "separated_by_extension.json"
EXTENSIONS = [".ncw", ".nki", ".nkm", ".nkc", ".wav", ".aiff", ".sf2", ".sfz", ".rex", ".rx2", ".mp3", ".flac"]

def scan_and_group(root, extensions):
    result = {}
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        ext_groups = defaultdict(list)
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in extensions:
                ext_groups[ext].append(fname)
        if ext_groups:
            result[rel_dir] = {ext: sorted(files) for ext, files in ext_groups.items()}
    return result

if __name__ == "__main__":
    grouped = scan_and_group(ROOT, EXTENSIONS)
    with open(OUTPUT, "w") as f:
        json.dump(grouped, f, indent=2)
    print(f"✅ Separated files by extension and saved to: {OUTPUT}")