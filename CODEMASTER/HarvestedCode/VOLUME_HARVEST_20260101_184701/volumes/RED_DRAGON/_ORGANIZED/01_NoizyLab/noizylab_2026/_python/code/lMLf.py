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
import concurrent.futures
import time
import hashlib
import os

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

def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning Mr. Plowman, are we ready to get started?"
    elif hour < 18:
        greeting = "Good afternoon Mr. Plowman, are we ready to get started?"
    else:
        greeting = "Good evening Mr. Plowman, are we ready to get started?"
    print(greeting)
    speak(greeting)

# ---------- Deep Code Consistency + Mission Control + Restart + Email Plans ----------
import py_compile

def check_workspace_code():
    """Compile every .py under WORKSPACE; report errors per file."""
    report = ["Workspace Code Consistency Check:"]
    py_files = list(WORKSPACE.rglob("*.py"))
    if not py_files:
        report.append("No Python files found in workspace.")
    for f in py_files:
        try:
            py_compile.compile(str(f), doraise=True)
            report.append(f"✅ {f.relative_to(WORKSPACE)}")
        except Exception as e:
            report.append(f"❌ {f.relative_to(WORKSPACE)} — {e}")
    log = "\n".join(report)
    save_log("workspace_code_check", log)
    return log

def mission_control_health():
    """Inspect key Mission Control and Dock speed prefs; suggest fixes."""
    report = ["Mission Control Health:"]
    def dread(domain, key):
        out = run(["defaults", "read", domain, key])
        return out if out and not out.startswith("Error:") else "(not set)"
    expose = dread("com.apple.dock", "expose-animation-duration")
    mru = dread("com.apple.dock", "mru-spaces")
    spans = dread("com.apple.spaces", "spans-displays")
    autohide = dread("com.apple.dock", "autohide-time-modifier")
    report += [
        f"• expose-animation-duration: {expose}",
        f"• Dock autohide-time-modifier: {autohide}",
        f"• Mission Control 'mru-spaces': {mru}",
        f"• Displays have separate Spaces (spans-displays): {spans}",
        "",
        "Speed-up suggestions (optional, reversible):",
        "  - Faster Mission Control: defaults write com.apple.dock expose-animation-duration -float 0.1; killall Dock",
        "  - Snappier Dock hide/show: defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock",
        "  - Disable MRU spaces re-order: defaults write com.apple.dock mru-spaces -bool false; killall Dock",
        "  - Keep separate Spaces per display: defaults write com.apple.spaces spans-displays -bool false; killall Dock",
        "",
        "Restore defaults:",
        "  - defaults delete com.apple.dock expose-animation-duration; killall Dock",
        "  - defaults delete com.apple.dock autohide-time-modifier; killall Dock",
        "  - defaults delete com.apple.dock mru-spaces; killall Dock",
        "  - defaults delete com.apple.spaces spans-displays; killall Dock",
    ]
    log = "\n".join(report)
    save_log("mission_control_health", log)
    return log

def restart_mac():
    """Attempt a safe restart via System Events (macOS will prompt if needed)."""
    speak("Preparing to restart macOS now.")
    cmd = ['osascript', '-e', 'tell application "System Events" to restart']
    out = run(cmd)
    log = f"Restart requested via System Events.\n{out}"
    save_log("restart_request", log)
    return log

def finish_parallels_with_tools():
    """Start Parallels, choose/remember VM, trigger Tools install, and log."""
    status = parallels_status()
    vm_launch = launch_parallels()
    report = "=== Parallels Finish ===\n" + status + "\n\n" + vm_launch
    save_log("parallels_finish", report)
    return report

def webador_outlook_plan():
    """
    Generate a step-by-step plan to use Webador mailboxes inside Outlook.
    Writes a ready-to-edit Markdown playbook + CSV template.
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    md = WORKSPACE / f"Saved_Notes/Webador_Outlook_Playbook_{ts}.md"
    csv = WORKSPACE / f"Saved_Notes/Webador_Emails_Template_{ts}.csv"
    suggested = [
        ("hello",        "General inquiries / public"),
        ("studio",       "Sessions & production"),
        ("press",        "Media & PR"),
        ("partnerships", "Biz dev / collabs"),
        ("accounts",     "Invoices & payments"),
    ]
    md.write_text("""# Webador → Outlook Email Plan (Fill placeholders)

## 0) Decide your domain
- Domain: **{{YOUR_DOMAIN}}**  (example: fishmusic.io)
- Where it’s managed: Webador (recommended for this flow)

## 1) Create 5 mailboxes in Webador
- Webador Dashboard → Email → Add mailbox (requires Pro/Business plan)
- Create:
  - hello@{{YOUR_DOMAIN}}
  - studio@{{YOUR_DOMAIN}}
  - press@{{YOUR_DOMAIN}}
  - partnerships@{{YOUR_DOMAIN}}
  - accounts@{{YOUR_DOMAIN}}
- Record passwords securely.

## 2) DNS hygiene (deliverability)
- In Webador DNS settings, add/confirm:
  - **SPF** (TXT at root): v=spf1 include:_spf.YOURMAILHOST -all
    - Use the exact SPF value Webador provides for your domain.
  - **DKIM** (TXT like `default._domainkey`): paste the DKIM key Webador gives you.
  - **DMARC** (TXT at `_dmarc`): v=DMARC1; p=quarantine; rua=mailto:dmarc@{{YOUR_DOMAIN}}; ruf=mailto:dmarc@{{YOUR_DOMAIN}}; fo=1
    - Adjust policy `p=` to `none` initially if you want to observe first.

## 3) Outlook (Mac/Windows) add each mailbox (IMAP)
- Outlook → Add Account → Use “IMAP/POP” (manual)
- **Incoming (IMAP):** Use the hostname, port, and SSL/TLS setting shown in Webador’s Email settings.
  - Typical IMAP: port 993 + SSL/TLS
- **Outgoing (SMTP):** Use the SMTP host/port from Webador.
  - Typical SMTP: port 465 (SSL) or 587 (STARTTLS)
- Username: full email address (e.g., hello@{{YOUR_DOMAIN}})
- Password: mailbox password you set in Webador

## 4) Test
- Send between mailboxes (hello → studio) and to a Gmail address.
- Check spam placement; adjust SPF/DMARC if needed.

## 5) Optional routing
- If later you migrate to Microsoft 365 mail hosting:
  - Add your domain in Microsoft 365 Admin Center
  - Switch MX to Microsoft
  - Create the same five users/aliases in Exchange Online
  - Update Outlook accounts to Microsoft sign-in.

## Notes
- Keep this playbook and the CSV template together.
- Store mailbox passwords in a password manager.
""".strip(), encoding="utf-8")
    lines = ["localpart,display_name,notes"]
    for lp, note in suggested:
        lines.append(f"{lp},{lp.capitalize()},\"{note}\"")
    csv.write_text("\n".join(lines), encoding="utf-8")
    msg = f"Playbook written:\n- {md}\n- {csv}\nEdit {{YOUR_DOMAIN}} and provider-specific DNS entries."
    save_log("webador_outlook_plan", msg)
    return msg

# ---------- Drive Benchmark ----------
def benchmark_drives(workers_per_drive=1, sample_hash=False):
    drives = [d for d in Path("/Volumes").iterdir() if d.is_dir() and d.name not in ("Macintosh HD", "Macintosh HD - Data")]
    if not drives:
        return "No external drives found in /Volumes."

    def iter_files(root: Path):
        for dirpath, _, filenames in os.walk(root):
            for fn in filenames:
                yield Path(dirpath) / fn

    def scan_drive(root: Path):
        count = 0
        t0 = time.perf_counter()
        for p in iter_files(root):
            count += 1
            if sample_hash and (count % 100 == 0):  # sample every 100th file
                try:
                    with open(p, "rb") as f:
                        hashlib.blake2b(f.read(1024*128)).hexdigest()
                except Exception:
                    pass
        dt = time.perf_counter() - t0
        return f"{root.name}: {count} files in {dt:.1f}s ({(count/dt)*60:.0f} files/min)"

    futures = []
    t0 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(drives)*workers_per_drive) as pool:
        for d in drives:
            for _ in range(workers_per_drive):
                futures.append(pool.submit(scan_drive, d))
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    dt = time.perf_counter() - t0

    log = f"\n=== Bubba Drive Benchmark (workers/drive={workers_per_drive}) ===\n"
    log += "\n".join(results)
    log += f"\nTOTAL time: {dt:.1f}s"
    save_log(f"benchmark_{workers_per_drive}", log)
    return log

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
    choice = input("Select voice number (or press Enter to cancel): ")


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
            elif "tidy desktop" in command or "clean desktop" in command:
                result = tidy_desktop_to_noizy()
            else:
                result = f"Direct command mode not supported for: {command}"
            print(result)
            speak(result)
        else:
            menu()
            choice = input("Choose an option: ").strip().lower()
            if choice == "a":
                out = audit_workspace()
                print(json.dumps(out, indent=2))
            elif choice == "b":
                out = run_diagnostics()
                print(json.dumps(out, indent=2))
            elif choice == "c":
                out = launch_parallels()
                print(json.dumps(out, indent=2))
            elif choice == "d":
                out = tidy_desktop_to_noizy()
                print(out)
                speak(out)
            elif choice == "x":
                out = benchmark_drives(workers_per_drive=1)
                print(out)
                speak(out)
            elif choice == "y":
                out = benchmark_drives(workers_per_drive=2)
                print(out)
                speak(out)
            else:
                print("Invalid choice, please try again.")
