#!/usr/bin/env python3
"""
hand_of_god.py — Bubba + Cha-Cha unified control script

Primary features:
 - workspace audit
 - diagnostics (basic)
 - desktop cleanup (move files into categorized project folders)
 - big-house scan (scan mounted volumes under /Volumes and copy/move files)
 - parallels checks + start (uses prlctl if available)
 - interactive Windows 11 checklist
 - optional OpenAI refactor step if OPENAI_API_KEY is present and --refactor used
 - DRY-RUN by default; pass --apply to actually move/copy/start

Usage examples:
  python3 hand_of_god.py --audit
  python3 hand_of_god.py --clean-desktop         # dry run: shows planned moves
  python3 hand_of_god.py --clean-desktop --apply # actually moves files
  python3 hand_of_god.py --big-house --copy-mode --apply
  python3 hand_of_god.py --parallels --apply --iso /path/to/Win11.iso
  python3 hand_of_god.py --checklist              # guides Windows install
"""

import argparse
import subprocess
import sys
import shutil
import os
from pathlib import Path
from datetime import datetime
import json

# -------------------------
# Configuration / Paths
# -------------------------
HOME = Path.home()
WORKSPACE = HOME / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
BUBBA_BITZ = WORKSPACE / "Bubbas_Bitz"
LOGS = BUBBA_BITZ / "Logs"
LOGS.mkdir(parents=True, exist_ok=True)

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOGFILE = LOGS / f"hand_of_god_{TIMESTAMP}.log"

# simple categories used by janitor logic
CATEGORIES = {
    "Audio_Project": [".wav", ".aiff", ".mp3", ".flac"],
    "Code_Project": [".py", ".sh", ".js", ".ts", ".cpp", ".c", ".h"],
    "Docs_Project": [".txt", ".md", ".rtf", ".docx", ".pdf"],
    "Images_Project": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
}

# safety: directories we will never touch
SYSTEM_BLACKLIST = {Path("/"), Path("/System"), Path("/bin"), Path("/usr"), Path("/private")}

# -------------------------
# Utilities
# -------------------------
def log(msg: str, echo=True):
    ts = datetime.now().isoformat()
    line = f"[{ts}] {msg}"
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    if echo:
        print(line)

def run_cmd(cmd):
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        return out.strip()
    except Exception as e:
        return f"Error running {' '.join(cmd)}: {e}"

def ensure_pip_package(pkg_name, import_name=None):
    import_name = import_name or pkg_name
    try:
        __import__(import_name)
        return True
    except ImportError:
        log(f"Package {pkg_name} missing; attempting to install via pip...", True)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
            __import__(import_name)
            log(f"Installed {pkg_name} successfully.", True)
            return True
        except Exception as e:
            log(f"Failed to install {pkg_name}: {e}", True)
            return False

# -------------------------
# Features
# -------------------------
def audit_workspace():
    log("Running workspace audit...")
    essentials = [
        "hand_of_god.py", "the_janitor.py", "cha_cha_clean_v2.py",
        "parallels_setup.py", "super_brain.py"
    ]
    report = []
    for fname in essentials:
        p = WORKSPACE / fname
        found = p.exists()
        report.append((fname, found, str(p)))
        log(f"Audit: {fname} -> {'FOUND' if found else 'MISSING'}: {p}")
    return report

def run_diagnostics():
    log("Collecting system diagnostics...")
    info = {}
    info["python_version"] = run_cmd([sys.executable, "--version"])
    info["disk_root"] = run_cmd(["df", "-h", "/"])
    try:
        info["memory"] = run_cmd(["vm_stat"])
    except Exception:
        info["memory"] = "vm_stat unavailable on this mac"
    log("Diagnostics complete.")
    return info

def preview_move_plan(target_folder: Path):
    """
    Given a folder, return a list of planned moves (src, dest)
    """
    moves = []
    if not target_folder.exists():
        log(f"Target folder not found: {target_folder}")
        return moves
    for item in target_folder.iterdir():
        if item.is_file():
            moved = False
            for project, exts in CATEGORIES.items():
                if item.suffix.lower() in exts:
                    dest_dir = BUBBA_BITZ / project
                    moves.append((item, dest_dir / item.name))
                    moved = True
                    break
            if not moved:
                dest_dir = BUBBA_BITZ / "Misc_Project"
                moves.append((item, dest_dir / item.name))
    return moves

def perform_moves(move_plan, apply=False):
    actions = []
    for src, dst in move_plan:
        if any(parent in SYSTEM_BLACKLIST for parent in src.resolve().parents):
            log(f"Skipping system file: {src}", True)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if apply:
            try:
                shutil.move(str(src), str(dst))
                log(f"Moved {src} -> {dst}", True)
                actions.append(("moved", src, dst))
            except Exception as e:
                log(f"Failed to move {src} -> {dst}: {e}", True)
                actions.append(("error", src, dst, str(e)))
        else:
            log(f"[DRY-RUN] Would move {src} -> {dst}", True)
            actions.append(("plan", src, dst))
    return actions

def cleanup_desktop(apply=False):
    desktop = HOME / "Desktop"
    log(f"Preparing desktop cleanup for: {desktop}")
    moves = preview_move_plan(desktop)
    return perform_moves(moves, apply=apply)

def scan_volumes(copy_mode=True, apply=False):
    volumes = Path("/Volumes")
    if not volumes.exists():
        log("/Volumes directory not found. Nothing to scan.", True)
        return []
    actions = []
    for drive in volumes.iterdir():
        if not drive.is_dir():
            continue
        if drive.name in ("Macintosh HD", "Macintosh HD - Data"):
            continue
        log(f"Scanning drive: {drive.name}")
        for item in drive.rglob("*"):
            if item.is_file():
                # same classification as desktop
                dest_dir = None
                for project, exts in CATEGORIES.items():
                    if item.suffix.lower() in exts:
                        dest_dir = BUBBA_BITZ / project
                        break
                if dest_dir is None:
                    dest_dir = BUBBA_BITZ / "Misc_Project"
                dest_dir.mkdir(parents=True, exist_ok=True)
                dst = dest_dir / item.name
                if apply:
                    try:
                        if copy_mode:
                            shutil.copy2(item, dst)
                            log(f"Copied {item} -> {dst}")
                            actions.append(("copied", item, dst))
                        else:
                            shutil.move(str(item), str(dst))
                            log(f"Moved {item} -> {dst}")
                            actions.append(("moved", item, dst))
                    except Exception as e:
                        log(f"Error copying/moving {item}: {e}")
                        actions.append(("error", item, dst, str(e)))
                else:
                    op = "Would copy" if copy_mode else "Would move"
                    log(f"[DRY-RUN] {op} {item} -> {dst}")
                    actions.append(("plan", item, dst))
    return actions

def check_parallels_and_start(vm_name="Windows 11", iso_path=None, apply=False):
    """
    If prlctl exists, can create a VM (if missing) and start it.
    This function is conservative: it will only create a VM if --apply is passed.
    """
    if shutil.which("prlctl") is None:
        log("prlctl not found in PATH. Parallels CLI unavailable.", True)
        return {"prlctl": False}
    info = {}
    info["prlctl"] = True
    vms = run_cmd(["prlctl", "list", "-a"])
    info["vms_raw"] = vms
    if vm_name in vms:
        log(f"VM '{vm_name}' already exists.")
    else:
        log(f"VM '{vm_name}' not found.")
        if apply:
            if iso_path is None:
                log("No ISO specified; cannot create VM without ISO.")
            else:
                log(f"Creating VM '{vm_name}' with ISO {iso_path}...")
                run_cmd(["prlctl", "create", vm_name, "--ostype", "win-11"])
                run_cmd(["prlctl", "set", vm_name, "--device-set", "cdrom0", "--connect", "--image", iso_path])
                log("VM created and ISO attached.")
    if apply:
        log(f"Starting VM '{vm_name}'...")
        run_cmd(["prlctl", "start", vm_name])
    else:
        log(f"[DRY-RUN] Would start VM '{vm_name}' (use --apply to actually start).")
    return info

def interactive_win11_checklist():
    steps = [
        "Boot VM → Windows logo should appear.",
        "Language, Time, Keyboard → select and click Next → Install Now.",
        "Product Key → Enter or click 'I don’t have a product key'. Choose Windows 11 Pro.",
        "License Agreement → accept and click Next.",
        "Installation Type → choose Custom: Install Windows only (advanced).",
        "Drive Selection → highlight virtual drive and click Next.",
        "Wait for installation (reboots may happen).",
        "Region & Keyboard → pick region/layout.",
        "Device Name → give VM a name (e.g. Noizy-Win11).",
        "Account Setup → sign in with Microsoft or choose Offline account.",
        "Privacy Settings → adjust and continue.",
        "Windows 11 desktop loads.",
        "Parallels Tools → macOS menu bar: Actions → Install Parallels Tools.",
        "Run Parallels Tools installer inside Windows, reboot when finished."
    ]
    log("Starting interactive Windows 11 checklist. Press ENTER after each step.")
    for i, step in enumerate(steps, 1):
        input(f"[{i}/{len(steps)}] {step}\nPress Enter when done → ")
        log(f"Checklist step {i} completed: {step}")
    log("Checklist complete. Windows 11 installation steps done (or acknowledged).")
    print("✅ Checklist finished. Check logs for details.")

def optionally_refactor_file_with_openai(filepath: Path):
    """
    If OPENAI_API_KEY present and openai package available, ask model to refactor.
    This is optional and conservative: writes a _refactor copy.
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        log("OPENAI_API_KEY not set; skipping OpenAI refactor.", True)
        return None
    try:
        import openai
    except Exception:
        ok = ensure_pip_package("openai")
        if not ok:
            log("OpenAI package unavailable; skipping refactor.", True)
            return None
        import openai
    openai.api_key = key
    code_text = filepath.read_text(encoding="utf-8")
    log(f"Sending {filepath.name} to OpenAI for light refactor (no logic changes).")
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Cha-Cha, a careful code refactorer. Improve readability and docs; do NOT change the program's logic."},
                {"role": "user", "content": f"Refactor this code (preserve logic):\n\n{code_text}"}
            ],
            max_tokens=1500,
            temperature=0.2
        )
        content = resp["choices"][0]["message"]["content"].strip()
        outpath = filepath.parent / f"{filepath.stem}_refactored{filepath.suffix}"
        outpath.write_text(content, encoding="utf-8")
        log(f"Wrote refactored file to {outpath}", True)
        return outpath
    except Exception as e:
        log(f"OpenAI refactor failed: {e}", True)
        return None

# -------------------------
# Arg parsing & main
# -------------------------
def main():
    p = argparse.ArgumentParser(description="Hand of God - Bubba/Cha-Cha unified toolkit")
    p.add_argument("--audit", action="store_true", help="Run workspace audit")
    p.add_argument("--diagnostics", action="store_true", help="Run diagnostics")
    p.add_argument("--clean-desktop", action="store_true", help="Organize files on Desktop into workspace (DRY-RUN unless --apply)")
    p.add_argument("--big-house", action="store_true", help="Scan /Volumes and consolidate files (DRY-RUN unless --apply)")
    p.add_argument("--copy-mode", action="store_true", help="When used with --big-house, copy files instead of moving")
    p.add_argument("--parallels", action="store_true", help="Check Parallels CLI and optionally create/start VM")
    p.add_argument("--vm-name", default="Windows 11", help="VM name for parallels operations")
    p.add_argument("--iso", help="Windows ISO path (used if creating VM with --apply)")
    p.add_argument("--checklist", action="store_true", help="Interactive Windows 11 checklist helper")
    p.add_argument("--refactor", action="store_true", help="Attempt OpenAI refactor for a file (use --file)")
    p.add_argument("--file", help="Path to code file to refactor or to run single-file cleanup")
    p.add_argument("--apply", action="store_true", help="Actually perform moves/copies/start (default is dry-run)")
    args = p.parse_args()

    log("=== Hand of God session start ===")
    if args.audit:
        audit_workspace()
    if args.diagnostics:
        diag = run_diagnostics()
        log(json.dumps(diag, indent=2))
    if args.clean_desktop:
        cleanup_desktop(apply=args.apply)
    if args.big_house:
        scan_volumes(copy_mode=args.copy_mode, apply=args.apply)
    if args.parallels:
        check_parallels_and_start(vm_name=args.vm_name, iso_path=args.iso, apply=args.apply)
    if args.checklist:
        interactive_win11_checklist()
    if args.refactor and args.file:
        fpath = Path(args.file).expanduser()
        if not fpath.exists():
            log(f"Refactor target not found: {fpath}")
        else:
            optionally_refactor_file_with_openai(fpath)
    if args.file and not args.refactor:
        # single-file cleanup preview -> move into Code_Project if a code file
        fp = Path(args.file).expanduser()
        if fp.exists():
            log(f"Single-file preview for: {fp}")
            moves = preview_move_plan(fp.parent)
            # filter only the one file
            moves = [(s, d) for (s, d) in moves if s.samefile(fp)]
            perform_moves(moves, apply=args.apply)
        else:
            log(f"File not found: {fp}")

    log("=== Hand of God session end ===")
    print(f"Log saved to: {LOGFILE}")

if __name__ == "__main__":
    main()

"""
Parallels Helper - create, launch, and check Windows 11 VM
"""

import subprocess, shutil

VM_NAME = "Windows 11"
ISO_PATH = "/Users/rsp_ms/Downloads/Win11.iso"  # update this path

def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

def ensure_vm():
    vms = run(["prlctl", "list", "-a"])
    if VM_NAME not in vms:
        print("Creating VM...")
        run(["prlctl", "create", VM_NAME, "--ostype", "win-11"])
        run(["prlctl", "set", VM_NAME, "--device-set", "cdrom0", "--connect", "--image", ISO_PATH])
        print("✅ VM created.")
    else:
        print("✅ VM already exists.")

def start_vm():
    print("▶️ Starting VM...")
    run(["prlctl", "start", VM_NAME])
    print("👉 Once Windows boots, install Parallels Tools via macOS menu: Actions → Install Parallels Tools")

if __name__ == "__main__":
    if not shutil.which("prlctl"):
        print("❌ prlctl not found. Make sure Parallels Desktop is installed.")
    else:
        ensure_vm()
        start_vm()