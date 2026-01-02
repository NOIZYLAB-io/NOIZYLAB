import json
import os
from pathlib import Path
import shutil

EXPORT_BASE = Path.home() / "Desktop" / "FishNetScans"
XLN_DOCS_FOLDER = Path.home() / "Desktop" / "XLN_Audio_Docs"
target_folder = Path.home() / "Desktop" / "NoizyFish_Scripts"

XLN_DOCS_FOLDER.mkdir(exist_ok=True)
target_folder.mkdir(exist_ok=True)

# Find the latest scan folder
latest_scan = sorted(EXPORT_BASE.glob("Scan_*"))[-1]
json_path = latest_scan / "sound_inventory.json"

# XLN Audio keywords
xln_keywords = [
    "xln audio", "addictive", "xo", "rc-20", "retro color", "electric", "keys", "drums"
]

with open(json_path) as f:
    data = json.load(f)

docs = data.get("docs", [])
matches = []

for doc_path in docs:
    try:
        with open(doc_path, "r", errors="ignore") as doc_file:
            content = doc_file.read().lower()
            if any(keyword in content for keyword in xln_keywords):
                matches.append(doc_path)
                shutil.copy2(doc_path, XLN_DOCS_FOLDER)
    except Exception:
        continue

if matches:
    print("XLN Audio documentation files moved to:")
    print(f"  {XLN_DOCS_FOLDER}")
    for m in matches:
        print(f"  {m}")
else:
    print("No XLN Audio documentation found in the latest scan.")

desktop = Path.home() / "Desktop"

for script in desktop.glob("*.py"):
    shutil.move(str(script), str(target_folder / script.name))

print(f"All Python scripts moved to {target_folder}")