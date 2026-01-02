#!/usr/bin/env python3
import shutil, json, hashlib, subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def batch_clean_workspace():
    for file in WS.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".py", ".js", ".ts"}:
            print(clean_code(file))

def usage():
    print("""
Usage:
  python3 bubba_desktop_sweep_json.py --batch
      Organize, deduplicate, clean, and optimize the entire workspace.

  python3 bubba_desktop_sweep_json.py --single <file>
      Clean and lint a single file.

  python3 bubba_desktop_sweep_json.py --project <project_name>
      Organize and clean a specific project folder.

  python3 bubba_desktop_sweep_json.py --help
      Show this help message.
""")

def log_error(msg):
    error_log = WS / "Bubbas_Bitz" / "Logs" / "error_log.txt"
    with open(error_log, "a") as f:
        f.write(msg + "\n")

def optimize_file(file):
    # Example: Suggest optimization if file is large or slow to process
    if file.stat().st_size > 5_000_000:  # >5MB
        print(f"⚡ Optimization: {file} is large. Consider splitting or compressing.")
        log_error(f"Optimization suggested for large file: {file}")

def main():
    cfg = load_cfg()
    cats = cfg.get("desktop_sorting", {})
    print("Scanning Noizy Workspace for relevant project files...")

    # Gather all files to process
    files_to_process = []
    for file in WS.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".py", ".sh", ".json"}:
            project = get_project_for_file(file, cats)
            if project:
                expected_dir = WS / project
                if expected_dir not in file.parents:
                    files_to_process.append((file, project))

    # Use 96 agents for parallel processing
    AGENTS_TOTAL = 96
    with ThreadPoolExecutor(max_workers=AGENTS_TOTAL) as pool:
        futures = [pool.submit(move_to_project, file, project) for file, project in files_to_process]
        for f in as_completed(futures):
            f.result()  # Print output from move_to_project

    print("✅ Workspace files organized by project and extension.")

    print("Deleting duplicate files in each project folder...")
    delete_duplicates_in_projects(cats)
    print("✅ Duplicates deleted.")

    print("Deleting files with 'access' in their name...")
    delete_access_code(cats)
    print("✅ Access code deleted.")

    print("Batch cleaning all code files in workspace...")
    batch_clean_workspace()
    print("✅ All code files cleaned and linted.")

    logs_dir = WS / "Bubbas_Bitz" / "Logs"
    for path in logs_dir.rglob("*"):
        print(path)

if __name__ == "__main__":
    args = sys.argv[1:]
    summary = {"moved": 0, "cleaned": 0, "duplicates": 0, "access_deleted": 0, "errors": 0}
    if not args or "--help" in args:
        usage()
        sys.exit(0)

    if args[0] == "--batch":
        try:
            main()
            print("🧹 Batch clean complete.")
        except Exception as e:
            log_error(f"Batch error: {e}")
            print(f"❌ Batch error: {e}")
            summary["errors"] += 1
    elif args[0] == "--single":
        if len(args) != 2:
            print("❌ Please provide a file path for --single.")
            usage()
            sys.exit(1)
        file = Path(args[1]).expanduser()
        if not file.exists() or not file.is_file():
            print(f"❌ Target file not found: {file}")
            log_error(f"File not found: {file}")
            sys.exit(1)
        try:
            print(clean_code(file))
            summary["cleaned"] += 1
            optimize_file(file)
        except Exception as e:
            log_error(f"Single file error: {file} :: {e}")
            print(f"❌ Error cleaning {file}: {e}")
            summary["errors"] += 1
    elif args[0] == "--project":
        if len(args) != 2:
            print("❌ Please provide a project name for --project.")
            usage()
            sys.exit(1)
        project = args[1]
        folder = WS / project
        if not folder.exists() or not folder.is_dir():
            print(f"❌ Target project folder not found: {folder}")
            log_error(f"Project folder not found: {folder}")
            sys.exit(1)
        cats = load_cfg().get("desktop_sorting", {})
        print(f"Scanning project folder: {folder}")
        try:
            scan_workspace_folders({project: cats.get(project, [])})
            delete_duplicates_in_projects({project: cats.get(project, [])})
            delete_access_code({project: cats.get(project, [])})
            for file in folder.rglob("*"):
                if file.is_file() and file.suffix.lower() in {".py", ".js", ".ts"}:
                    print(clean_code(file))
                    summary["cleaned"] += 1
                    optimize_file(file)
            print(f"✅ Project '{project}' organized and cleaned.")
        except Exception as e:
            log_error(f"Project error: {folder} :: {e}")
            print(f"❌ Error in project {folder}: {e}")
            summary["errors"] += 1
    else:
        print(f"❌ Unknown argument: {args[0]}")
        usage()
        sys.exit(1)

    # Summary report
    print("\n=== Bubba Janitor Summary ===")
    for k, v in summary.items():
        print(f"{k.capitalize()}: {v}")
    print("See Bubbas_Bitz/Logs/error_log.txt for details on any errors or optimization suggestions.")