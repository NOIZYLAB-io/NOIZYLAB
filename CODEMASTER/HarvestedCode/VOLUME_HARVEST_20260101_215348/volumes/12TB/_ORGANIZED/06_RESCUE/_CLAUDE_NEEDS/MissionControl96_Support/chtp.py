import os
import subprocess
import speech_recognition as sr

BASE = os.path.expanduser("~/Desktop/NoizyFish")
modules = [
    "scripts/token_manager.py",
    "scripts/noizyfb_consolidator.py",
    "scripts/admin_snapshot.py",
    "scripts/legacy_sync.py"
]

def run_all():
    for module in modules:
        path = os.path.join(BASE, module)
        print(f"🚀 Running: {path}")
        subprocess.run(["python3", path])

def listen_for_trigger():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Say 'Facebook cleanup' to launch...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        if "facebook cleanup" in command:
            run_all()
    except Exception as e:
        print(f"❌ Voice error: {e}")

if __name__ == "__main__":
    listen_for_trigger()
