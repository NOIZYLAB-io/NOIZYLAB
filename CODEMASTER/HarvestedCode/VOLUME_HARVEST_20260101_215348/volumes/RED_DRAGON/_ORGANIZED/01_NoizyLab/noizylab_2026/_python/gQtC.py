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

import sys, subprocess, shutil, json
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
    if "audit" in cmd:
        return audit_workspace()
    elif "diagnostic" in cmd:
        return run_diagnostics()
    elif "parallels status" in cmd:
        return parallels_status()
    elif "launch parallels" in cmd:
        return launch_parallels()
    elif "appstore apple" in cmd:
        return prep_app_store("apple")
    elif "appstore microsoft" in cmd:
        return prep_app_store("microsoft")
    elif "cleanup desktop" in cmd:
        return cleanup_desktop()
    elif "mute" in cmd:
        set_mute_state(True)
        return "🔇 Cha-Cha muted."
    elif "unmute" in cmd:
        set_mute_state(False)
        return "🔊 Cha-Cha unmuted."
    else:
        return f"Unknown command: {cmd}"

# ---------- Main ----------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--listen":
            listen_loop()
        else:
            cmd = " ".join(sys.argv[1:])
            out = handle_command(cmd)
            print(out); speak(out)
    else:
        while True:
            cmd = input("Cha-Cha awaiting command: ").strip()
            if cmd in ("quit", "exit", "q"):
                speak("Goodbye, my dear.")
                break
            out = handle_command(cmd)
            print(out); speak(out)
