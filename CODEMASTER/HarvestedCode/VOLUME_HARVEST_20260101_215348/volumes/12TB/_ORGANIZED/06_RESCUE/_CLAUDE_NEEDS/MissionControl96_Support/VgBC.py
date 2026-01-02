import os
import subprocess
import speech_recognition as sr
from datetime import datetime
import yaml

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

def autosave(data, filename):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base = os.path.expanduser("~/Desktop/NoizyFish/logs")
    os.makedirs(base, exist_ok=True)
    path = os.path.join(base, f"{filename}_{timestamp}.yaml")
    with open(path, "w") as f:
        yaml.dump(data, f)
    print(f"🧾 Autosaved: {path}")

def autosave_status(status):
    import yaml
    import os
    BASE = os.path.expanduser("~/Desktop/NoizyFish")
    path = os.path.join(BASE, "logs", "autorun_status.yaml")
    with open(path, "w") as f:
        yaml.dump(status, f)
    print(f"🧾 Autorun status saved at {path}")

if __name__ == "__main__":
    listen_for_trigger()
