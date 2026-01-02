#!/usr/bin/env python3
import shutil, json, hashlib, subprocess, sys, os
from pathlib import Path

def list_volumes():
    volumes = [Path("/")]
    volumes += [Path("/Volumes") / v for v in os.listdir("/Volumes") if (Path("/Volumes") / v).is_dir()]
    return volumes

def menu(volumes):
    print("\nSelect a location to organize:")
    for i, v in enumerate(volumes, 1):
        print(f"{i}. {v}")
    print(f"{len(volumes)+1}. Drag a folder here and press Enter")
    choice = input("Choose [number]: ").strip()
    if choice == str(len(volumes)+1):
        folder = input("Paste the full path of the folder to organize: ").strip()
        return Path(folder).expanduser()
    try:
        idx = int(choice) - 1
        return volumes[idx]
    except Exception:
        print("Invalid choice, defaulting to main drive (/)")
        return Path("/")

def get_project_for_file(file, cats):
    ext = file.suffix.lower()
    for folder, exts in cats.items():
        if ext in exts:
            return folder
    return None

def move_to_project(file, root, cats):
    project = get_project_for_file(file, cats)
    if not project:
        return
    dest_dir = root / project
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / file.name
    i = 1
    while dest_file.exists():
        dest_file = dest_dir / f"{file.stem} ({i}){file.suffix}"
        i += 1
    shutil.move(str(file), str(dest_file))
    print(f"Moved: {file} -> {dest_file}")

def delete_duplicates(root, cats):
    for project in cats.keys():
        folder = root / project
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
    print("\n".join(report))

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return e.output

def organize_folder(root, cats):
    print(f"\nOrganizing: {root}")
    for file in root.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".py", ".sh", ".json"}:
            move_to_project(file, root, cats)
    delete_duplicates(root, cats)
    for project in cats.keys():
        folder = root / project
        if folder.exists():
            for file in folder.rglob("*"):
                if file.is_file() and file.suffix.lower() in {".py", ".js", ".ts"}:
                    clean_code(file)
    print(f"\n✅ Organization and cleaning complete for {root}")

def load_cfg(cfg_path):
    if cfg_path.exists():
        try:
            return json.loads(cfg_path.read_text())
        except Exception:
            pass
    return {"desktop_sorting": {}}

if __name__ == "__main__":
    # Use your workspace config if available, else default
    ws_cfg = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace" / "bubba_config.json"
    cats = load_cfg(ws_cfg).get("desktop_sorting", {})
    volumes = list_volumes()
    target = menu(volumes)
    organize_folder(target, cats)