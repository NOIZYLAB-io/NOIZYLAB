#!/usr/bin/env python3
import shutil, json
from pathlib import Path

# Paths
WS = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
DESKTOP = Path.home() / "Desktop"
CFG = WS / "bubba_config.json"

# Load config
def load_cfg():
    if CFG.exists():
        try:
            return json.loads(CFG.read_text())
        except Exception:
            pass
    return {"desktop_sorting": {}}

def get_project_for_file(file, cats):
    ext = file.suffix.lower()
    for folder, exts in cats.items():
        if ext in exts:
            return folder
    return None

def move_to_project(file, project_folder):
    dest_dir = WS / project_folder
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / file.name
    i = 1
    while dest_file.exists():
        dest_file = dest_dir / f"{file.stem} ({i}){file.suffix}"
        i += 1
    shutil.move(str(file), str(dest_file))
    print(f"Moved: {file} -> {dest_file}")

def scan_desktop_folders(cats):
    for folder in DESKTOP.iterdir():
        if folder.is_dir():
            for file in folder.rglob("*"):
                if file.is_file() and file.suffix.lower() in {".py", ".sh", ".json"}:
                    project = get_project_for_file(file, cats)
                    if project:
                        move_to_project(file, project)

def main():
    cfg = load_cfg()
    cats = cfg.get("desktop_sorting", {})
    print("Scanning Desktop folders for relevant project files...")
    scan_desktop_folders(cats)
    print("✅ Relevant files moved into Noizy Workspace project folders.")

if __name__ == "__main__":
    main()