import shutil, json
from pathlib import Path

# Paths
WS = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
TO_SORT = Path.home() / "Desktop" / "Python To Sort"
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

def scan_and_move(source_dir, cats):
    for file in source_dir.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".py", ".sh", ".json"}:
            project = get_project_for_file(file, cats)
            if project:
                move_to_project(file, project)

def scan_workspace_for_unsorted(cats):
    for file in WS.iterdir():
        if file.is_file() and file.suffix.lower() in {".py", ".sh", ".json"}:
            project = get_project_for_file(file, cats)
            if project:
                move_to_project(file, project)

def main():
    cfg = load_cfg()
    cats = cfg.get("desktop_sorting", {})
    print("Scanning Python To Sort for project files...")
    scan_and_move(TO_SORT, cats)
    print("Scanning Noizy Workspace for unsorted files...")
    scan_workspace_for_unsorted(cats)
    print("✅ All files sorted into project folders.")

if __name__ == "__main__":
    main()