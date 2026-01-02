#!/usr/bin/env python3
"""
Bubba Desktop Sweep:
Sorts Desktop files into project folders inside the Noizyfish Workspace.
"""

import shutil, json, subprocess
from pathlib import Path

HOME = Path.home()
DESK = HOME / "Desktop"
WS   = HOME / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
CFG  = WS / "bubba_config.json"
LOGS = WS / "Saved_Notes"
LOGS.mkdir(parents=True, exist_ok=True)

def say(msg, voice="Siri Voice 1"):
    print(f"** {msg} **")
    try:
        subprocess.run(["say", "-v", voice, msg], check=False)
    except Exception:
        pass

def load_cfg():
    if CFG.exists():
        try:
            return json.loads(CFG.read_text())
        except Exception:
            pass
    return {"voice": "Siri Voice 1", "desktop_sorting": {}}

def uniq(p: Path) -> Path:
    if not p.exists(): return p
    stem, suf = p.stem, p.suffix
    parent = p.parent
    i = 1
    while True:
        alt = parent / f"{stem} ({i}){suf}"
        if not alt.exists():
            return alt
        i += 1

def should_skip(path: Path):
    # Don't move files already in Noizy_Workspace
    try:
        return WS in path.resolve().parents
    except Exception:
        return False

def sweep():
    cfg = load_cfg()
    voice = cfg.get("voice", "Siri Voice 1")
    cats  = cfg.get("desktop_sorting", {})

    moved, skipped, errors = 0, 0, 0
    for item in DESK.iterdir():
        if item.is_file():
            dest_dir = None
            for folder, exts in cats.items():
                if item.suffix.lower() in exts:
                    dest_dir = WS / folder
                    break
            if dest_dir:
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_file = uniq(dest_dir / item.name)
                try:
                    shutil.move(str(item), str(dest_file))
                    moved += 1
                except Exception as e:
                    print(f"Error moving {item}: {e}")
                    errors += 1
            else:
                skipped += 1

    log = LOGS / "desktop_sweep.log"
    with open(log, "a") as f:
        f.write(f"Sweep finished: moved={moved}, skipped={skipped}, errors={errors}\n")
    say(f"Sweep complete. {moved} moved, {skipped} skipped, {errors} errors.", voice)

def deep_sweep():
    cfg = load_cfg()
    voice = cfg.get("voice", "Siri Voice 1")
    cats  = cfg.get("desktop_sorting", {})

    moved, skipped, errors = 0, 0, 0
    log_lines = []

    for file in HOME.rglob("*"):
        if file.is_file() and not should_skip(file):
            dest_dir = None
            for folder, exts in cats.items():
                if file.suffix.lower() in exts:
                    dest_dir = WS / folder
                    break
            if dest_dir:
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_file = uniq(dest_dir / file.name)
                try:
                    shutil.move(str(file), str(dest_file))
                    moved += 1
                    log_lines.append(f"Moved: {file} -> {dest_file}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")
                    log_lines.append(f"Error: {file} -> {e}")
                    errors += 1
            else:
                skipped += 1

    log = LOGS / "deep_sweep.log"
    with open(log, "a") as f:
        f.write(f"Deep sweep finished: moved={moved}, skipped={skipped}, errors={errors}\n")
        f.write("\n".join(log_lines) + "\n")
    say(f"Deep sweep complete. {moved} moved, {skipped} skipped, {errors} errors.", voice)

if __name__ == "__main__":
    sweep()
