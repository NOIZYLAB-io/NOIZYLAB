import os
import subprocess
import time
import speech_recognition as sr
import json
from pathlib import Path

# CONFIGURATION
FILE_PATH = "/Users/rsp_ms/Documents/rituals/my_script.py"
RUNTIME = "python3"
GIT_ENABLED = True
GIT_COMMIT_MSG = "🔁 Ritual Executed: Capsule Clean — Soul Synced to Legacy Grid"
STATUS_JSON = str(Path.home() / "RSP/NW_MissionControl/dashboard/status.json")
SESSION_LOG = str(Path.home() / "RSP/Logs/noizylab_voice_session.jsonl")
SOUNDS = {
    "start": "/System/Library/Sounds/Glass.aiff",
    "success": "/System/Library/Sounds/Hero.aiff",
    "error": "/System/Library/Sounds/Basso.aiff"
}

# --- Voice Feedback ---
def speak(message, voice="Samantha"):
    os.system(f'say -v "{voice}" "{message}"')

def play_sound(sound):
    if os.path.exists(sound):
        subprocess.run(["afplay", sound])

# --- Session Logging ---
def log_session(event, details=None):
    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "event": event,
        "details": details or {}
    }
    os.makedirs(os.path.dirname(SESSION_LOG), exist_ok=True)
    with open(SESSION_LOG, "a") as f:
        f.write(json.dumps(log) + "\n")

# --- Dashboard Status ---
def announce_status():
    if os.path.exists(STATUS_JSON):
        try:
            with open(STATUS_JSON) as f:
                status = json.load(f)
            msg = f"Mission Control: {status.get('nw',{}).get('state','Unknown')} — {status.get('nw',{}).get('message','No message')}"
            speak(msg, "Alex")
        except Exception as e:
            speak("Unable to read dashboard status.", "Samantha")
    else:
        speak("Dashboard status file not found.", "Samantha")

# --- Voice Recognition ---
def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Listening for ritual command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🧠 Heard: {command}")
        log_session("voice_command", {"command": command})
        return command
    except sr.UnknownValueError:
        play_sound(SOUNDS["error"])
        speak("I didn't catch that. Try again.", "Samantha")
        log_session("voice_error", {"error": "UnknownValueError"})
        return None

# --- Ritual Actions ---
def is_valid_python(file_path):
    try:
        subprocess.check_output([RUNTIME, "-m", "py_compile", file_path])
        return True
    except subprocess.CalledProcessError:
        return False

def auto_save_and_run():
    play_sound(SOUNDS["start"])
    speak("Validating capsule...", "Samantha")
    if is_valid_python(FILE_PATH):
        speak("Code is clean. Executing ritual.", "Samantha")
        subprocess.run([RUNTIME, FILE_PATH])
        play_sound(SOUNDS["success"])
        speak("Ritual complete.", "Samantha")
        log_session("ritual_run", {"status": "success"})
        if GIT_ENABLED:
            git_sync()
    else:
        play_sound(SOUNDS["error"])
        speak("Syntax error detected. Launching fallback overlay.", "Samantha")
        log_session("ritual_run", {"status": "error"})
        launch_debugger()

def git_sync():
    speak("Syncing soul to GitHub...", "Alex")
    subprocess.run(["git", "add", FILE_PATH])
    subprocess.run(["git", "commit", "-m", GIT_COMMIT_MSG])
    subprocess.run(["git", "push"])
    play_sound(SOUNDS["success"])
    speak("Soul synced to legacy grid.", "Alex")
    log_session("git_sync", {"file": FILE_PATH})

def launch_debugger():
    speak("Opening debugger overlay in VS Code.", "Samantha")
    subprocess.run(["code", FILE_PATH])
    log_session("debugger_opened", {"file": FILE_PATH})

def archive_capsule():
    speak("Archiving capsule...", "Samantha")
    # Placeholder for archive logic
    play_sound(SOUNDS["success"])
    speak("Capsule archived.", "Samantha")
    log_session("capsule_archived")

def scan_vault():
    speak("Scanning vault for anomalies...", "Alex")
    # Placeholder for scan logic
    play_sound(SOUNDS["success"])
    speak("Vault scan complete.", "Alex")
    log_session("vault_scanned")

def launch_focus_mode():
    speak("Launching focus mode. Ambient soundscape engaged.", "Samantha")
    # Placeholder for ambient sound logic
    play_sound(SOUNDS["start"])
    log_session("focus_mode_launched")

def show_dashboard():
    announce_status()
    log_session("dashboard_announced")

# --- Main Loop ---
def run_noizylab():
    speak("NOIZYLAB is online. Awaiting command.", "Alex")
    announce_status()
    while True:
        command = listen_for_command()
        if command:
            if "run ritual" in command or "execute capsule" in command:
                auto_save_and_run()
            elif "sync soul" in command:
                git_sync()
            elif "open debugger" in command:
                launch_debugger()
            elif "archive capsule" in command:
                archive_capsule()
            elif "scan vault" in command:
                scan_vault()
            elif "focus mode" in command:
                launch_focus_mode()
            elif "show dashboard" in command:
                show_dashboard()
            elif "shutdown" in command:
                speak("Shutting down NOIZYLAB. Ritual complete.", "Samantha")
                log_session("shutdown")
                break
            else:
                play_sound(SOUNDS["error"])
                speak("Unknown command. Try again.", "Samantha")
                log_session("unknown_command", {"command": command})

if __name__ == "__main__":
    run_noizylab()
