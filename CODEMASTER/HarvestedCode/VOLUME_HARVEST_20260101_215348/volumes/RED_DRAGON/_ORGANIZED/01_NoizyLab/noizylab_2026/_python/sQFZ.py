# ---------- Health Check ----------
def system_health():
    py = run(["python3", "--version"])
    disk = run(["df", "-h", "/"]).splitlines()[1] if run(["df", "-h", "/"]) else "Disk check failed"
    mem = run(["vm_stat"]).splitlines()[:5]
    parallels = run(["pgrep", "-fl", "Parallels"])
    report = [
        f"Python: {py}",
        f"Disk: {disk}",
        "Memory: " + " | ".join(mem),
        f"Parallels: {'running' if parallels else 'not running'}"
    ]
    return "\n".join(report)

def announce_health():
    report = system_health()
    print("🩺 Startup Health Check\n" + report)
    # Condense to a short spoken version
    summary = []
    if "running" in report: summary.append("Parallels is running")
    else: summary.append("Parallels not running")
    summary.append("Disk and memory checked")
    speak("Startup health check complete. " + ". ".join(summary))
    log("HealthCheck → " + report)
# ---------- Voice Listener ----------
def have_sr():
    try:
        import speech_recognition  # noqa: F401
        return True
    except Exception:
        return False

def listen_once(timeout=5, phrase_time_limit=8):
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening…")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        return r.recognize_google(audio)
    except Exception:
        return ""

def listen_loop():
    if not have_sr():
        msg = ("SpeechRecognition not installed.\n"
               "Install with: pip install SpeechRecognition pyaudio\n"
               "On Mac: brew install portaudio && pip install pyaudio")
        print(msg); speak("Microphone is not ready.")
        return
        announce_health()   # 👈 new line
    wake_phrases = ["hey cha-cha", "cha-cha my dear", "hey cha cha", "cha cha"]
    speak("Cha-Cha is listening, my dear.")
    while True:
        said = listen_once()
        if not said:
            continue
        text = said.lower()
        if any(p in text for p in wake_phrases):
            for p in wake_phrases:
                text = text.replace(p, "").strip()
            if text:
                out = handle_command(text)
                print(out); speak(out)
#!/usr/bin/env python3
"""
cha_cha_bubba.py
Cha-Cha as front-end, Bubba as executor.
- Voice & text input
- Bubba skills (audit, diagnostics, parallels, app store, cleanup)
- Auto-check Parallels Tools
"""


import sys, subprocess, shutil, json, difflib
from pathlib import Path
from datetime import datetime

# ---------- Paths ----------
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
SAVE_DIR = WORKSPACE / "Saved_Notes"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

MUTE_FILE = WORKSPACE / "mute_state.json"

# ---------- Cha-Cha Voice ----------
VOICE = "Siri Voice 1"

def get_mute_state():
    if MUTE_FILE.exists():
        try:
            return json.loads(MUTE_FILE.read_text()).get("mute", False)
        except Exception:
            return False

def run_diagnostics():
    return "\n".join([
        "Python: " + run(["python3", "--version"]),
        "Disk: " + run(["df", "-h", "/"]),
        "Memory: " + run(["vm_stat"])
    ])
    return False

def set_mute_state(state: bool):
    MUTE_FILE.write_text(json.dumps({"mute": state}))
    return state

def speak(msg: str):
    if get_mute_state():
        return
    subprocess.run(["say", "-v", VOICE, msg], check=False)


# ---------- Logging ----------
LOG_FILE = SAVE_DIR / f"cha_cha_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
def log(msg: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} {msg}\n")

# ---------- Command Router ----------
COMMANDS = {
    "audit workspace": audit_workspace,
    "diagnostics": run_diagnostics,
    "parallels status": parallels_status,
    "launch parallels": launch_parallels,
    "appstore apple": lambda: prep_app_store("apple"),
    "appstore microsoft": lambda: prep_app_store("microsoft"),
    "cleanup desktop": cleanup_desktop,
    "mute": lambda: (set_mute_state(True), "🔇 Cha-Cha muted.")[1],
    "unmute": lambda: (set_mute_state(False), "🔊 Cha-Cha unmuted.")[1],
}

def match_command(text: str):
    keys = list(COMMANDS.keys())
    best = difflib.get_close_matches(text, keys, n=1, cutoff=0.5)
    return best[0] if best else None

def handle_chain(text: str):
    # Support chaining: "... and ... then ..."
    parts = []
    for token in text.replace("then", "and").split("and"):
        parts.extend([p.strip() for p in token.split(",") if p.strip()])
    results = []
    for part in parts:
        out = handle_command(part)
        results.append(f"[{part}] {out}")
    return "\n".join(results)

def run(cmd):
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        return out.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

# ---------- Bubba Skills ----------
def audit_workspace():
    files = ["hand_of_god.py", "super_brain.py", "bucket_switcher.py"]
    report = ["Audit:"]
    for f in files:
        path = WORKSPACE / f
        report.append(f"{f}: {'✅ FOUND' if path.exists() else '❌ MISSING'}")
    return "\n".join(report)

def run_diagnostics():
    return "\n".join([
        "Python: " + run(["python3", "--version"]),
        "Disk: " + run(["df", "-h", "/"]),
        "Memory: " + run(["vm_stat"])
    ])

def parallels_status():
    apps = run(["pgrep", "-fl", "Parallels"])
    vms = run(["prlctl", "list"]) if shutil.which("prlctl") else "prlctl not installed."
    return f"Parallels Processes:\n{apps}\n\nVMs:\n{vms}"

def launch_parallels():
    run(["open", "-a", "Parallels Desktop"])
    tools = run(["ls", "/Applications/Parallels Desktop.app/Contents/Applications/Parallels Tools.app"])
    return f"Launched Parallels. Tools check: {tools or 'Tools not found!'}"

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
    return f"App Store Prep ({target}):\n- " + "\n- ".join(steps)

def cleanup_desktop():
    desktop = Path.home() / "Desktop"
    if not desktop.exists():
        return "No Desktop folder."
    dest = WORKSPACE / "Desktop_Archive"
    dest.mkdir(parents=True, exist_ok=True)
    moved = []
    for f in desktop.iterdir():
        if f.is_file():
            shutil.move(str(f), str(dest / f.name))
            moved.append(f.name)
    return "Moved:\n" + "\n".join(moved)

# ---------- Command Router ----------
def handle_command(cmd: str):
    cmd = cmd.lower()
    key = match_command(cmd)
    if key:
        result = COMMANDS[key]()
        log(f"{cmd} → {result}")
        return result
    else:
        msg = f"Unknown command: {cmd}"
        log(msg)
        return msg

# ---------- Main ----------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--listen":
            listen_loop()
        else:
            cmd = " ".join(sys.argv[1:])
            result = handle_chain(cmd)
            print(result)
            speak(result)
    else:
        announce_health()   # 👈 new line
        while True:
            cmd = input("Cha-Cha> ").strip()
            if cmd in ("quit", "exit", "q"):
                speak("Goodbye, my dear.")
                break
            result = handle_chain(cmd)
            print(result)
            speak(result)
