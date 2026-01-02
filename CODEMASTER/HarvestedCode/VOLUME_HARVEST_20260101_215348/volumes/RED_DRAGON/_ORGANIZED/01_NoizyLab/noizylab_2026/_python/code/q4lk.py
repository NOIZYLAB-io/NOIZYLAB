
#!/usr/bin/env python3
"""
bubba_hand_of_god_big_house.py
Bubba Mega-Script:
- Workspace audits, diagnostics, Parallels (with Tools), App Store prep
- Super Brain stub
- Cha-Cha voice with mute/unmute persistence
- Code health checker
- Desktop & Big House cleanup
"""

import sys, subprocess, json, shutil
from pathlib import Path
from datetime import datetime

# ---------- Paths ----------
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
SAVE_DIR = WORKSPACE / "Saved_Notes"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

MUTE_FILE = WORKSPACE / "mute_state.json"
CONFIG_FILE = WORKSPACE / "bubba_config.json"

# ---------- Voice ----------
VOICE = "Siri Voice 1"

def get_mute_state():
    if MUTE_FILE.exists():
        try:
            return json.loads(MUTE_FILE.read_text()).get("mute", False)
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
    f.write_text(content if isinstance(content, str) else json.dumps(content, indent=2), encoding="utf-8")
    return f

def run(cmd):
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        return out.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

# ---------- Config Helpers ----------
def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except Exception:
            return {}
    return {}

def save_config(cfg):
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))

def get_default_vm():
    cfg = load_config()
    return cfg.get("default_vm")

def set_default_vm(vm_name):
    cfg = load_config()
    cfg["default_vm"] = vm_name
    save_config(cfg)

# ---------- Code Health ----------
def check_code_health():
    report = ["Bubba Code Health Check:"]
    try:
        run(["python3", "-m", "py_compile", str(Path(__file__))])
        report.append("✅ Python syntax OK")
    except Exception as e:
        report.append(f"❌ Syntax issue: {e}")
    if not shutil.which("prlctl"):
        report.append("⚠️ prlctl not found (Parallels CLI missing).")
    else:
        report.append("✅ prlctl found.")
    try:
        cfg = load_config()
        vm = cfg.get("default_vm")
        if vm:
            report.append(f"✅ Default VM remembered: {vm}")
        else:
            report.append("⚠️ No default VM set.")
    except Exception as e:
        report.append(f"❌ Config file error: {e}")
    log = "\n".join(report)
    save_log("code_health", log)
    return log

def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Duplicate definition removed; use unified save_log above

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


# ---------- Logging ----------
    # Duplicate definition removed; use unified save_log above

    # Duplicate definition removed; use unified run above

# ---------- Bubba’s Skills ----------
    # Duplicate definition removed; use unified audit_workspace above

    # Duplicate definition removed; use unified run_diagnostics above

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

    # Duplicate definition removed; use unified launch_parallels above

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
def _move_or_copy(item, dest_dir, copy_mode, project, report):
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / item.name
    if copy_mode:
        shutil.copy2(item, dest)
        report.append(f"Copied {item} → {project}")
    else:
        shutil.move(str(item), str(dest))
        report.append(f"Moved {item} → {project}")

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
    for drive in [d for d in volumes.iterdir() if d.is_dir() and d.name not in ("Macintosh HD", "Macintosh HD - Data")]:
        report.append(f"\n--- Scanning {drive.name} ---")
        for item in drive.rglob("*"):
            if not item.is_file():
                continue
            for project, exts in categories.items():
                if item.suffix.lower() in exts:
                    _move_or_copy(item, WORKSPACE / project, copy_mode, project, report)
                    break
            else:
                _move_or_copy(item, WORKSPACE / "Misc_Project", copy_mode, "Misc_Project", report)
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
            def menu():
                menu_items = {
                    "1": ("Audit Workspace", audit_workspace),
                    "2": ("Run Diagnostics", run_diagnostics),
                    "3": ("List Projects", list_projects),
                    "4": ("Parallels Status", parallels_status),
                    "5": ("Launch Parallels", launch_parallels),
                    "6": ("Super Brain Prompt", lambda: super_brain(input("Enter Super Brain prompt: ").strip() or "Hello from Hand of God")),
                    "7": ("Prep App Store (Apple)", lambda: prep_app_store("apple")),
                    "8": ("Prep App Store (Microsoft)", lambda: prep_app_store("microsoft")),
                    "9": ("Cleanup Desktop and Organize", cleanup_system),
                    "b": ("Clean the Big House (all drives)", lambda: clean_big_house(copy_mode=True)),
                    "m": ("Mute Cha-Cha", lambda: (set_mute_state(True), "🔇 Cha-Cha muted.")[1]),
                    "u": ("Unmute Cha-Cha", lambda: (set_mute_state(False), "� Cha-Cha unmuted.")[1]),
                    "v": ("Refresh Cha-Cha's Voice", lambda: f"Cha-Cha refreshed to {VOICE}"),
                    "h": ("Help", lambda: "Bubba Skills: audit, diagnostics, projects, Parallels, Super Brain, App Store, mute/unmute, desktop cleanup, big house cleanup."),
                    "q": ("Quit", lambda: "quit")
                }
                while True:
                    print("\n=== BUBBA + HAND OF GOD (Big House) ===")
                    for key, (desc, _) in menu_items.items():
                        if key == "q":
                            print(f"{key}) Quit")
                        else:
                            print(f"{key}) {desc}")
                    choice = input("Select: ").strip().lower()
                    if choice in menu_items:
                        desc, func = menu_items[choice]
                        out = func()
                        if choice == "q":
                            speak("Goodbye, my dear.")
                            break
                    else:
                        out = "Invalid choice."
                    print(out)
                    speak(out)
            # ---------- Voice ----------
