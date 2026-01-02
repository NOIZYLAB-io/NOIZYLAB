import json
import shutil
from pathlib import Path

# Folders
EXPORT_BASE = Path.home() / "Desktop" / "FishNetScans"
XLN_DOCS_FOLDER = Path.home() / "Desktop" / "XLN_Audio_Docs"
SCRIPTS_FOLDER = Path.home() / "Desktop" / "NoizyFish_Scripts"
XLN_DOCS_FOLDER.mkdir(exist_ok=True)
SCRIPTS_FOLDER.mkdir(exist_ok=True)

# Find latest FishNet scan
scan_folders = sorted(EXPORT_BASE.glob("Scan_*"))
if not scan_folders:
    print("No FishNet scan folders found.")
else:
    latest_scan = scan_folders[-1]
    json_path = latest_scan / "sound_inventory.json"
    if not json_path.exists():
        print(f"No sound_inventory.json found in {latest_scan}")
    else:
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

# Move all Python scripts from Desktop to NoizyFish_Scripts
desktop = Path.home() / "Desktop"
for script in desktop.glob("*.py"):
    if script.name != "XLN_Audio_Docs_Collector.py":  # Avoid moving itself
        shutil.move(str(script), str(SCRIPTS_FOLDER / script.name))

print(f"All Python scripts (except this one) moved to {SCRIPTS_FOLDER}")