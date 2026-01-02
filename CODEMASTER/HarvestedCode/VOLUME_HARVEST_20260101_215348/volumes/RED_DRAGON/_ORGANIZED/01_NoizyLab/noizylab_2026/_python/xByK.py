#!/usr/bin/env python3
"""
bubba_core.py
Bubba = VS Buddy's new name.
Expanded: audits workspace, diagnostics, projects, Parallels control,
Super Brain handoff, App Store build prep.
"""

import sys
import subprocess
import os
from pathlib import Path
import shutil
import json

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
SAVE_DIR = WORKSPACE / "Saved_Notes"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

MUTE_FILE = WORKSPACE / "mute_state.json"
CONFIG_FILE = WORKSPACE / "bubba_config.json"

# -------- Utility --------
def save_log(name, content):
    f = SAVE_DIR / f"bubba_{name}.txt"
    f.write_text(content, encoding="utf-8")
    return f

def run(cmd):
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        return out.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

# -------- Core Skills --------
def audit_workspace():
    files = [
        "hand_of_god.py",
        "cha_cha_hotrod.py",
        "cha_cha_listener.py",
        "cha_cha_to_bubba.py",
        "bubba_core.py",
        "super_brain.py"
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

# -------- New Skills --------
def parallels_status():
    """Check if Parallels Desktop is running + list VMs if possible."""
    apps = run(["pgrep", "-fl", "Parallels"])
    vms = run(["prlctl", "list"]) if shutil.which("prlctl") else "prlctl not installed."
    report = f"Parallels Processes:\n{apps}\n\nVMs:\n{vms}"
    save_log("parallels", report)
    return report

def launch_parallels():
    """Launch Parallels Desktop."""
    out = run(["open", "-a", "Parallels Desktop"])
    save_log("parallels_launch", out)
    return "Launched Parallels Desktop."

def get_super_brain_path():
    if CONFIG_FILE.exists():
        try:
            cfg = json.loads(CONFIG_FILE.read_text())
            return Path(cfg.get("super_brain_path"))
        except Exception:
            pass
    return WORKSPACE / "super_brain.py"

def super_brain(prompt="Hello from Bubba"):
    """Pass a prompt to Super Brain if available."""
    sb = get_super_brain_path()
    if not sb.exists():
        return "❌ Super Brain not found."
    result = run(["python3", str(sb), prompt])
    save_log("super_brain", result)
    return result

def prep_app_store(target="apple"):
    """Stub: prepare builds for Apple or Microsoft store."""
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

# -------- Mute State Management --------
def get_mute_state():
    if MUTE_FILE.exists():
        try:
            return json.loads(MUTE_FILE.read_text()).get("mute", False)
        except Exception:
            return False
    return False

def set_mute_state(state: bool):
    data = {"mute": state}
    MUTE_FILE.write_text(json.dumps(data))
    return state

# -------- Command Router --------
def help_text():
    return (
        "Bubba understands these commands:\n"
        "- audit workspace\n"
        "- run diagnostics\n"
        "- list projects\n"
        "- parallels status\n"
        "- launch parallels\n"
        "- super brain <prompt>\n"
        "- prep appstore apple\n"
        "- prep appstore microsoft\n"
        "- help\n"
    )

def handle_command(cmd: str):
    cmd = cmd.lower()
    if "audit" in cmd:
        return audit_workspace()
    elif "diagnostic" in cmd:
        return run_diagnostics()
    elif "list" in cmd or "project" in cmd:
        return list_projects()
    elif "parallels status" in cmd:
        return parallels_status()
    elif "launch parallels" in cmd:
        return launch_parallels()
    elif "super brain" in cmd:
        prompt = cmd.replace("super brain", "").strip() or "Hello from Bubba"
        return super_brain(prompt)
    elif "prep appstore" in cmd:
        if "microsoft" in cmd:
            return prep_app_store("microsoft")
        else:
            return prep_app_store("apple")
    elif "mute" in cmd:
        set_mute_state(True)
        return "🔇 Cha-Cha is now muted."
    elif "unmute" in cmd:
        set_mute_state(False)
        return "🔊 Cha-Cha is now unmuted."
    elif "silence" in cmd:
        set_mute_state(True)
        return "🔇 Silence enforced by Bubba."
    elif "help" in cmd:
        return help_text()
    else:
        return "❓ Bubba doesn't know that command yet. Try 'help'."

# -------- Entry --------
def main():
    if len(sys.argv) < 2:
        print(help_text())
        return
    command = " ".join(sys.argv[1:])
    result = handle_command(command)
    print(result)

if __name__ == "__main__":
    main()
