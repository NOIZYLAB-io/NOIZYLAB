ù&#!/usr/bin/env python3
"""
bubba_desktop_sweep_json.py

Bubba sorts Desktop files into project folders based on bubba_config.json.
Also moves related files from Documents into Noizy_Workspace.
Cha-Cha announces only essential facts.
"""

import shutil, json, subprocess, os
from pathlib import Path

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
DESKTOP = Path.home() / "Desktop"
DOCS = Path.home() / "Documents"
CONFIG_FILE = WORKSPACE / "bubba_config.json"
LOGS = WORKSPACE / "Saved_Notes"
LOGS.mkdir(parents=True, exist_ok=True)

def say_nav(text: str, voice="Siri Voice 1"):
    print(f"**{text}**")
    try:
        subprocess.run(["say", "-v", voice, text], check=False)
    except (subprocess.SubprocessError, OSError) as err:
        print(f"Voice error: {err}")

def load_config():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}

def unique_dest(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suf = dest.stem, dest.suffix
    parent = dest.parent
    i = 1
    while True:
        alt = parent / f"{stem} ({i}){suf}"
        if not alt.exists():
            return alt
        i += 1

def sort_file(file: Path, cats: dict, ws: Path) -> str:
    ext = file.suffix.lower()
    for proj, exts in cats.items():
        if ext in exts:
            dest_dir = ws / proj
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = unique_dest(dest_dir / file.name)
            try:
                shutil.move(str(file), str(dest))
                return f"Moved: {file.name} -> {proj}"
            except (shutil.Error, OSError) as err:
                return f"Error moving {file.name}: {err}"
    return f"Skipped: {file.name}"

def move_documents_to_workspace(ws: Path, voice="Siri Voice 1"):
    """Move files from Documents to Noizy_Workspace if related to NoizyAI or Fish Music Inc."""
    keywords = {
        "noizyai": "NoizyAI_Project",
        "fishmusic": "FishMusic_Project"
    }
    moved, skipped = 0, 0
    log_lines = []

    for item in DOCS.iterdir():
        if item.is_file():
            name = item.name.lower()
            matched = None
            for kw, folder in keywords.items():
                if kw in name:
                    matched = folder
                    break
            if matched:
                dest_dir = ws / matched
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest = unique_dest(dest_dir / item.name)
                try:
                    shutil.move(str(item), str(dest))
                    log_lines.append(f"Moved: {item.name} -> {matched}")
                    moved += 1
                except Exception as err:
                    log_lines.append(f"Error moving {item.name}: {err}")
                    skipped += 1
            else:
                skipped += 1

    summary = f"Documents scan: Moved {moved}, Skipped {skipped}."
    (LOGS / "documents_to_workspace.txt").write_text("\n".join(log_lines) + "\n\n" + summary)
    say_nav(summary, voice)
    return summary

def delete_empty_folders(root: Path):
    """Recursively delete empty folders under root."""
    count = 0
    for folder in root.rglob("*"):
        if folder.is_dir() and not any(folder.iterdir()):
            try:
                folder.rmdir()
                count += 1
            except OSError as err:
                print(f"Could not delete {folder}: {err}")
    return count

def main():
    cfg = load_config()
    voice = cfg.get("voice", "Siri Voice 1")
    cats = cfg.get("desktop_sorting", {})
    auto_restart = cfg.get("auto_restart_after_sweep", False)

    say_nav(f"Config loaded. Voice: {voice}. Auto-restart: {auto_restart}.", voice)
    say_nav("Sweep beginning.", voice)

    # Move relevant files from Documents to workspace
    move_documents_to_workspace(WORKSPACE, voice)

    moved, skipped = 0, 0
    log_lines = []

    if not DESKTOP.exists():
        say_nav("Desktop not found.", voice)
        return

    for item in DESKTOP.iterdir():
        if item.is_file():
            result = sort_file(item, cats, WORKSPACE)
            log_lines.append(result)
            if result.startswith("Moved"):
                moved += 1
            elif result.startswith("Error"):
                skipped += 1
            else:
                skipped += 1

    summary = f"Complete. Moved {moved}. Skipped {skipped}."
    (LOGS / "desktop_sweep_json.txt").write_text("\n".join(log_lines) + "\n\n" + summary)
    say_nav(summary, voice)

    # Delete empty folders in workspace
    empty_count = delete_empty_folders(WORKSPACE)
    if empty_count:
        say_nav(f"Deleted {empty_count} empty folders in workspace.", voice)

    if auto_restart:
        say_nav("Rebooting now.", voice)
        os.system("sudo shutdown -r now")

if __name__ == "__main__":
    main()
É É¡
¡û ûø
ø· ·õ
õ   ≥
≥ù& 2]file:///Users/rsp_ms/Documents/Noizyfish_Aquarium/Noizy_Workspace/bubba_desktop_sweep_json.py