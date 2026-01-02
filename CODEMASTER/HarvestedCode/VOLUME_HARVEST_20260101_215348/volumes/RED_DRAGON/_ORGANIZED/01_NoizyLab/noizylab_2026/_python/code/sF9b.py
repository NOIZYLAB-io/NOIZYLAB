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

import sys, subprocess, json, shutil, re
from pathlib import Path
from datetime import datetime

# ---------- Paths ----------
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
SAVE_DIR = WORKSPACE / "Saved_Notes"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

MUTE_FILE = WORKSPACE / "mute_state.json"
CONFIG_FILE = WORKSPACE / "bubba_config.json"

# ---------- Cha-Cha Voice Handling (Self-Healing) ----------
VOICE_FILE = WORKSPACE / "cha_cha_voice.json"

def detect_available_voices():
    """Detect voices installed on macOS using 'say -v ?'."""
    try:
        voices = subprocess.check_output(["say", "-v", "?"], text=True)
        parsed = []
        for line in voices.splitlines():
            match = re.match(r"^(\S+)", line.strip())
            if match:
                parsed.append(match.group(1))
        return parsed
    except Exception:
        return ["Samantha"]  # safe fallback

def get_current_voice():
    """Load stored Cha-Cha voice or pick best available."""
    if VOICE_FILE.exists():
        try:
            return json.loads(VOICE_FILE.read_text()).get("voice", "Samantha")
        except Exception:
            pass
    return "Samantha"

def set_current_voice(voice: str):
    """Persist chosen Cha-Cha voice."""
    VOICE_FILE.write_text(json.dumps({"voice": voice}))
    return voice

def pick_voice(preferred="Siri Voice 1"):
    """Ensure Cha-Cha always has a valid voice."""
    available = detect_available_voices()
    if preferred in available:
        return set_current_voice(preferred)
    elif "Serena" in available:
        return set_current_voice("Serena")
    elif "Daniel" in available:
        return set_current_voice("Daniel")
    elif available:
        return set_current_voice(available[0])
    return set_current_voice("Samantha")

# Initialize Cha-Cha's voice
VOICE = pick_voice()

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
    """Speak with Cha-Cha's current voice if not muted."""
    if get_mute_state():
        return
    try:
        subprocess.run(["say", "-v", get_current_voice(), msg], check=False)
    except Exception as e:
        print(f"Cha-Cha error: {e}")

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

# ---------- Default Voice Setup ----------
def ensure_default_voice():
    if not MUTE_FILE.exists():
        # First run, lock in Siri Voice 1 (British Premium)
        set_current_voice("Siri Voice 1")
    # Always greet on startup
    greeting = "Good evening Mr. Plowman, are we ready to get started?"
    print(greeting)
    speak(greeting)

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

def choose_voice():
    """Interactive Cha-Cha voice picker."""
    available = detect_available_voices()
    if not available:
        return "No voices detected on this system."
    print("\n=== Available Voices ===")
    for i, v in enumerate(available, start=1):
        print(f"{i}) {v}")
    choice = input("Select voice number (or press Enter to cancel): ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available):
        return "No change made."
    selected = available[int(choice) - 1]
    set_current_voice(selected)
    return f"Cha-Cha switched to {selected}."

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
    ensure_default_voice()
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:]).lower()
        if "super brain" in command:
            result = super_brain(command)
        elif "cleanup desktop" in command:
            result = cleanup_system()
        elif "cleanup big house" in command:
            result = clean_big_house(copy_mode=True)
        elif "choose voice" in command:
            result = choose_voice()
        else:
            result = f"Direct command mode not supported for: {command}"
        print(result)
        speak(result)
    else:
        menu()
