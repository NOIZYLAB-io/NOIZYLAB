import os
import json
from pathlib import Path

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"
OUTPUT = Path.home() / "Desktop" / "KTK_Rebuilds_Metadata.json"
METADATA_EXTS = [".json", ".txt", ".xml", ".nfo", ".md", ".rtf"]

def find_metadata_files(root):
    metadata = []
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in METADATA_EXTS:
                file_path = Path(dirpath) / fname
                # Try to extract some crumbs: parent folder, extension, maybe first line
                parent = Path(dirpath).name
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        first_line = f.readline().strip()
                except Exception:
                    first_line = ""
                metadata.append({
                    "file": str(file_path),
                    "parent_folder": parent,
                    "extension": ext,
                    "first_line": first_line
                })
    return metadata

if __name__ == "__main__":
    crumbs = find_metadata_files(KTK_REBUILDS)
    with open(OUTPUT, "w") as f:
        json.dump(crumbs, f, indent=2)
    print(f"✅ Library metadata (crumbs) saved to: {OUTPUT}")