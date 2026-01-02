#!/usr/bin/env python3
"""
bubba_desktop_sweep_json.py

Bubba sorts Desktop files into project folders based on bubba_config.json.
Cha-Cha announces only essential facts.
"""

import shutil, json, subprocess, os
from pathlib import Path

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
DESKTOP = Path.home() / "Desktop"
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

def main():
    cfg = load_config()
    voice = cfg.get("voice", "Siri Voice 1")
    cats = cfg.get("desktop_sorting", {})
    auto_restart = cfg.get("auto_restart_after_sweep", False)

    say_nav(f"Config loaded. Voice: {voice}. Auto-restart: {auto_restart}.", voice)
    say_nav("Sweep beginning.", voice)

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

    if auto_restart:
        say_nav("Rebooting now.", voice)
        os.system("sudo shutdown -r now")

if __name__ == "__main__":
    main()