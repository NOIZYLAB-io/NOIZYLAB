#!/usr/bin/env python3
import shutil, json, hashlib, subprocess
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
    print(clean_code(dest_file))  # Clean and lint after moving

def scan_workspace_folders(cats):
    for file in WS.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".py", ".sh", ".json"}:
            project = get_project_for_file(file, cats)
            if project:
                # Only move if not already in the correct project folder
                expected_dir = WS / project
                if expected_dir not in file.parents:
                    move_to_project(file, project)

def delete_duplicates_in_projects(cats):
    for project in cats.keys():
        folder = WS / project
        if folder.exists():
            seen_hashes = {}
            for file in folder.rglob("*"):
                if file.is_file():
                    h = hashlib.sha256(file.read_bytes()).hexdigest()
                    if h in seen_hashes:
                        print(f"Deleting duplicate: {file}")
                        file.unlink()
                    else:
                        seen_hashes[h] = file

def delete_access_code(cats):
    for project in cats.keys():
        folder = WS / project
        if folder.exists():
            for file in folder.rglob("*"):
                if file.is_file() and "access" in file.name.lower():
                    print(f"Deleting access code: {file}")
                    file.unlink()

def clean_code(filepath):
    ext = Path(filepath).suffix
    report = []
    if ext == ".py":
        report.append(run_cmd(["black", str(filepath)]))
        report.append(run_cmd(["pylint", str(filepath), "--disable=all", "--enable=E,F,W,C"]))
    elif ext in (".js", ".ts"):
        report.append(run_cmd(["npx", "prettier", "--write", str(filepath)]))
        report.append(run_cmd(["npx", "eslint", str(filepath)]))
    else:
        report.append(f"No formatter/linter for {ext}")
    return "\n".join(report)

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return e.output

def batch_clean_workspace(cats):
    for project in cats.keys():
        folder = WS / project
        if folder.exists():
            for file in folder.rglob("*"):
                if file.is_file() and file.suffix.lower() in {".py", ".js", ".ts"}:
                    print(clean_code(file))

def main():
    cfg = load_cfg()
    cats = cfg.get("desktop_sorting", {})
    print("Scanning Noizy Workspace for relevant project files...")
    scan_workspace_folders(cats)
    print("✅ Workspace files organized by project and extension.")

    print("Deleting duplicate files in each project folder...")
    delete_duplicates_in_projects(cats)
    print("✅ Duplicates deleted.")

    print("Deleting files with 'access' in their name...")
    delete_access_code(cats)
    print("✅ Access code deleted.")

    print("Batch cleaning all code files in workspace...")
    batch_clean_workspace(cats)
    print("✅ All code files cleaned and linted.")

    logs_dir = WS / "Bubba's Bitz" / "Logs"
    for path in logs_dir.rglob("*"):
        print(path)

if __name__ == "__main__":
    main()