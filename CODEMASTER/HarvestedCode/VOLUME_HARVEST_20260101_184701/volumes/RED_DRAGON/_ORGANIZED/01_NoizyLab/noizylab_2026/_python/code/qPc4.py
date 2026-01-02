#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bubba: system janitor & orchestrator.
Contract-compliant with Cha-Cha router:
- Accepts arbitrary text payload from CLI.
- Routes known commands to helpers.
- Unknown commands handled gracefully.
- Replies with structured JSON.
- Logs everything to Saved_Notes.
"""

import json
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
LOG_DIR = WORKSPACE / "Saved_Notes"
LOG_DIR.mkdir(parents=True, exist_ok=True)

VOICE = "Siri Voice 1"

def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_log(name: str, data: dict):
    p = LOG_DIR / f"bubba_{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return str(p)

# ------------------------
# Core Bubba helpers
# ------------------------
def audit_workspace():
    files = [str(p) for p in WORKSPACE.glob("**/*") if p.is_file()]
    return {"count": len(files), "files": files[:20]}  # show only first 20 for brevity

def run_diagnostics():
    try:
        df = shutil.disk_usage("/")
        free_gb = round(df.free / (1024**3), 1)
    except (OSError, ValueError) as e:
        free_gb = f"error: {e}"
    result = subprocess.run(
        ["pgrep", "-fl", "Parallels"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False
    )
    parallels_running = bool(result.stdout.strip())
    return {"disk_free_gb": free_gb, "parallels_running": parallels_running}

def launch_parallels():
    try:
        subprocess.Popen(["open", "-a", "Parallels Desktop"])
        return {"launched": True}
    except (OSError, ValueError) as e:
        return {"launched": False, "error": str(e)}

def cleanup_desktop():
    desktop = Path.home() / "Desktop"
    report = []
    if desktop.exists():
        for f in desktop.iterdir():
            if f.is_file():
                dest = WORKSPACE / "Desktop_Files"
                dest.mkdir(exist_ok=True, parents=True)
                new = dest / f.name
                shutil.move(str(f), str(new))
                report.append(f"{f} → {new}")
    return {"moved": report, "count": len(report)}

# ------------------------
# Command router
# ------------------------
COMMANDS = {
    "audit workspace": audit_workspace,
    "diagnostics": run_diagnostics,
    "parallels status": run_diagnostics,
    "launch parallels": launch_parallels,
    "cleanup desktop": cleanup_desktop,
    "cleanup big house": run_diagnostics,  # placeholder, could expand
}

def handle_command(cmd: str):
    cmd_l = cmd.lower().strip()
    for key, func in COMMANDS.items():
        if key in cmd_l:
            return {"status": "ok", "command": key, "result": func()}
    return {"status": "not_found", "command": cmd, "result": "No matching command."}

# ------------------------
# Main CLI entrypoint
# ------------------------
if __name__ == "__main__":
    payload = " ".join(sys.argv[1:]).strip()
    if not payload:
        reply = {"status": "error", "msg": "No payload given", "ts": now_ts()}
    else:
        reply = handle_command(payload)
        reply["ts"] = now_ts()
    log_path = save_log("run", reply)
    reply["log_file"] = log_path
    print(json.dumps(reply, indent=2))
    sys.exit(0 if reply["status"] in ("ok","not_found") else 1)
        except Exception:
            return False
    return False

def set_mute_state(state: bool):
    MUTE_FILE.write_text(json.dumps({"mute": state}))
    return state

def speak(msg: str):
    if get_mute_state():
        return
    subprocess.run(["say", "-v", VOICE, msg], check=False)

# ---------- Logging ----------
def save_log(name, content):
    f = SAVE_DIR / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    f.write_text(content, encoding="utf-8")
    return f

def run(cmd):
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        return out.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

# ---------- Bubba’s Skills ----------
def audit_workspace():
    files = [
        "hand_of_god.py", "cha_cha_hotrod.py", "cha_cha_listener.py",
        "cha_cha_to_bubba.py", "bubba_core.py", "super_brain.py"
    ]
    report = ["Bubba Workspace Audit:"]
    for f in files:
        path = WORKSPACE / f
        report.append(f"{f}: {'✅ FOUND' if path.exists() else '❌ MISSING'}")
    log = "\n".join(report)
    save_log("audit", log)
    return log

def run_diagnostics():
    cmds = {
        "Python": ["python3", "--version"],
        "Disk": ["df", "-h", "/"],
        "Memory": ["vm_stat"]
    }
    report = ["Bubba Diagnostics:"]
    for name, cmd in cmds.items():
        report.append(f"\n## {name}\n{run(cmd)}")
    log = "\n".join(report)
    save_log("diagnostics", log)
    return log

def list_projects():
    base = Path.home() / "Documents" / "Noizyfish_Aquarium"
    if not base.exists():
        return "No Noizyfish_Aquarium folder found."
    projects = [p.name for p in base.iterdir() if p.is_dir()]
    log = "Bubba Projects:\n" + "\n".join(projects)
    save_log("projects", log)
    return log

def parallels_status():
    apps = run(["pgrep", "-fl", "Parallels"])
    vms = run(["prlctl", "list"]) if shutil.which("prlctl") else "prlctl not installed."
    report = f"Parallels Processes:\n{apps}\n\nVMs:\n{vms}"
    save_log("parallels", report)
    return report

def launch_parallels():
    run(["open", "-a", "Parallels Desktop"])
    return "Launched Parallels Desktop."

# ---------- Super Brain Stub ----------
def super_brain(prompt="Hello from Bubba"):
    sb = WORKSPACE / "super_brain.py"
    if not sb.exists():
        return f"Super Brain stub missing at {sb}"
    try:
        result = subprocess.check_output(["python3", str(sb), prompt], text=True)
        save_log("super_brain", result)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Super Brain error: {e.output}"

# ---------- App Store Prep ----------
def prep_app_store(target="apple"):
    if target == "apple":
        steps = [
            "Check Apple Developer account",
            "Ensure Xcode + CLT installed",
            "Generate app bundle (stub)",
            "Sign & notarize (manual step)"
        ]
    else:
        steps = [
            "Check Microsoft Partner Center account",
            "Ensure Windows VM has Visual Studio",
            "Generate MSIX package (stub)",
            "Upload via Partner dashboard"
        ]
    report = f"App Store Prep for {target.capitalize()}:\n- " + "\n- ".join(steps)
    save_log(f"appstore_{target}", report)
    return report

# ---------- Cleanup Desktop ----------
def cleanup_system():
    report = ["Bubba Desktop Cleanup Report:\n"]

    categories = {
        "Audio_Project": [".wav", ".aiff", ".mp3", ".flac"],
        "Code_Project": [".py", ".sh", ".js", ".ts", ".cpp", ".c", ".h"],
        "Docs_Project": [".txt", ".md", ".rtf", ".docx", ".pdf"],
        "Images_Project": [".png", ".jpg", ".jpeg", ".gif", ".svg"]
    }

    desktop = Path.home() / "Desktop"
    if not desktop.exists():
        return "No Desktop folder found."

    for item in desktop.iterdir():
        if item.is_file():
            moved = False
            for project, exts in categories.items():
                if item.suffix.lower() in exts:
                    dest_dir = WORKSPACE / project
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(item), str(dest_dir / item.name))
                    report.append(f"Moved {item.name} → {project}")
                    moved = True
                    break
            if not moved:
                dest_dir = WORKSPACE / "Misc_Project"
                dest_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(dest_dir / item.name))
                report.append(f"Moved {item.name} → Misc_Project")

    log = "\n".join(report)
    save_log("cleanup_desktop", log)
    return log

# ---------- Big House Cleanup ----------
def clean_big_house(copy_mode=True):
    report = ["Bubba Big House Cleanup Report:\n"]

    categories = {
        "Audio_Project": [".wav", ".aiff", ".mp3", ".flac"],
        "Code_Project": [".py", ".sh", ".js", ".ts", ".cpp", ".c", ".h"],
        "Docs_Project": [".txt", ".md", ".rtf", ".docx", ".pdf"],
        "Images_Project": [".png", ".jpg", ".jpeg", ".gif", ".svg"]
    }

    volumes = Path("/Volumes")
    if not volumes.exists():
        return "No /Volumes directory found."

    for drive in volumes.iterdir():
        if not drive.is_dir():
            continue
        if drive.name in ("Macintosh HD", "Macintosh HD - Data"):
            continue  # skip system drives

        report.append(f"\n--- Scanning {drive.name} ---")
        for item in drive.rglob("*"):
            if item.is_file():
                moved = False
                for project, exts in categories.items():
                    if item.suffix.lower() in exts:
                        dest_dir = WORKSPACE / project
                        dest_dir.mkdir(parents=True, exist_ok=True)
                        dest = dest_dir / item.name
                        if copy_mode:
                            shutil.copy2(item, dest)
                            report.append(f"Copied {item} → {project}")
                        else:
                            shutil.move(str(item), str(dest))
                            report.append(f"Moved {item} → {project}")
                        moved = True
                        break
                if not moved:
                    dest_dir = WORKSPACE / "Misc_Project"
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest = dest_dir / item.name
                    if copy_mode:
                        shutil.copy2(item, dest)
                        report.append(f"Copied {item} → Misc_Project")
                    else:
                        shutil.move(str(item), str(dest))
                        report.append(f"Moved {item} → Misc_Project")

    log = "\n".join(report)
    save_log("cleanup_big_house", log)
    return log

# ---------- Menu ----------
def menu():
    while True:
        print("\n=== BUBBA + HAND OF GOD (Big House) ===")
        print("1) Audit Workspace")
        print("2) Run Diagnostics")
        print("3) List Projects")
        print("4) Parallels Status")
        print("5) Launch Parallels")
        print("6) Super Brain Prompt")
        print("7) Prep App Store (Apple)")
        print("8) Prep App Store (Microsoft)")
        print("9) Cleanup Desktop and Organize")
        print("b) Clean the Big House (all drives)")
        print("m) Mute Cha-Cha")
        print("u) Unmute Cha-Cha")
        print("v) Refresh Cha-Cha's Voice")
        print("h) Help")
        print("q) Quit")
        choice = input("Select: ").strip().lower()

        if choice == "1":
            out = audit_workspace()
        elif choice == "2":
            out = run_diagnostics()
        elif choice == "3":
            out = list_projects()
        elif choice == "4":
            out = parallels_status()
        elif choice == "5":
            out = launch_parallels()
        elif choice == "6":
            prompt = input("Enter Super Brain prompt: ").strip() or "Hello from Hand of God"
            out = super_brain(prompt)
        elif choice == "7":
            out = prep_app_store("apple")
        elif choice == "8":
            out = prep_app_store("microsoft")
        elif choice == "9":
            out = cleanup_system()
        elif choice == "b":
            out = clean_big_house(copy_mode=True)
        elif choice == "m":
            set_mute_state(True)
            out = "🔇 Cha-Cha muted."
        elif choice == "u":
            set_mute_state(False)
            out = "🔊 Cha-Cha unmuted."
        elif choice == "v":
            global VOICE
            # ---------- Voice ----------
            # Lock Cha-Cha to Siri Voice 1 (British Premium)
            VOICE = "Siri Voice 1"
            out = f"Cha-Cha refreshed to {VOICE}."
        elif choice == "h":
            out = "Bubba Skills: audit, diagnostics, projects, Parallels, Super Brain, App Store, mute/unmute, desktop cleanup, big house cleanup."
        elif choice == "q":
            speak("Goodbye, my dear.")
            break
        else:
            out = "Invalid choice."

        print(out)
        speak(out)

# ---------- Entry ----------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:]).lower()
        if "super brain" in command:
            result = super_brain(command)
        elif "cleanup desktop" in command:
            result = cleanup_system()
        elif "cleanup big house" in command:
            result = clean_big_house(copy_mode=True)
        else:
            result = f"Direct command mode not supported for: {command}"
        print(result)
        speak(result)
    else:
        menu()
