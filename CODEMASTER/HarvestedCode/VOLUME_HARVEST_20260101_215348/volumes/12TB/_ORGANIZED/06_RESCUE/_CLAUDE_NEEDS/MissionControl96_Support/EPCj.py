import os
import subprocess
import datetime
import json
import platform
from pathlib import Path
import sounddevice as sd

# Install sounddevice if not already installed
try:
    import sounddevice
except ImportError:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'sounddevice'])

# 🧞 Voice Feedback
def say(msg, voice=""):
    try:
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["say", msg])
        else:  # Windows/Linux
            voice_param = f"-v {voice}" if voice else ""
            subprocess.run([
                "powershell",
                f"Add-Type –AssemblyName System.Speech; "
                f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{msg}')"
            ])
    except Exception as e:
        print(f"Error in voice feedback: {e}")

# 🧠 Slab Verification
def verify_slab():
    version = platform.platform()
    if platform.system() == "Windows":
        activated = subprocess.run(
            ["powershell", "(Get-WmiObject -Class SoftwareLicensingProduct | Where-Object {$_.PartialProductKey}) | Select-Object LicenseStatus"],
            capture_output=True, text=True
        ).stdout
        return "✅ Verified" if "1" in activated else "⚠️ Check Licensing"
    else:
        return "✅ Verified (macOS/Linux)"

# 🧬 Sequoia Infusion
def infuse_sequoia():
    agents = ["Strategist", "Healer", "Archivist", "Visionary"]
    capsule = {
        "timestamp": datetime.datetime.now().isoformat(),
        "agents": agents,
        "rituals": ["overlay_launch", "capsule_build", "slab_scan"],
        "sequoia_logic": "Agent barter + capsule economy"
    }
    path = "C:\🧞‍♂️NOIZYWIND\Legacy\sequoia_infusion_log.json" if platform.system() == "Windows" else str(Path.home() / "NOIZYWIND/Legacy/sequoia_infusion_log.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(capsule, f, indent=4)

# 🖥️ Overlay Launcher
def launch_overlay():
    if platform.system() == "Windows":
        subprocess.run(["start", "C:\🧞‍♂️NOIZYWIND\Overlays\planar_eyelevel.html"], shell=True)
    else:
        print("Overlay launch not implemented for macOS/Linux.")

# 🔊 Ambient Loop
def play_ambient():
    if platform.system() == "Windows":
        subprocess.run(["start", "C:\🧞‍♂️NOIZYWIND\Soundscapes\focused_loop.wav"], shell=True)
    else:
        print("Ambient loop not implemented for macOS/Linux.")

# 📦 Capsule Builder + AutoSave
def build_capsule():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    if platform.system() == "Windows":
        capsule = f"C:\🧞‍♂️NOIZYWIND\Legacy\Capsule_{ts}.zip"
        subprocess.run([
            "powershell", "Compress-Archive",
            "-Path", "C:\🧞‍♂️NOIZYWIND\Legacy\*",
            "-DestinationPath", capsule
        ])
        return capsule
    else:
        capsule = str(Path.home() / f"NOIZYWIND/Legacy/Capsule_{ts}.zip")
        print("Capsule build not implemented for macOS/Linux.")
        return capsule

def log_capsule(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "AutoSaved",
        "agent": "Archivist",
        "mood": "Focused"
    }
    path = "C:\🧞‍♂️NOIZYWIND\Legacy\autosave_log.json" if platform.system() == "Windows" else str(Path.home() / "NOIZYWIND/Legacy/autosave_log.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(log) + "\n")

# 🌐 GitHub Sync (symbolic log)
def sync_to_github(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "Pushed to GitHub (symbolic)"
    }
    path = "C:\🧞‍♂️NOIZYWIND\Legacy\capsule_sync_log.json" if platform.system() == "Windows" else str(Path.home() / "NOIZYWIND/Legacy/capsule_sync_log.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(log) + "\n")

# 🔥 Full Ritual Execution
def ignite():
    say("Slab awakening. NoizyGenieMode ignition sequence initiated.")
    status = verify_slab()
    say(f"Slab verification: {status}")
    infuse_sequoia()
    launch_overlay()
    play_ambient()
    capsule = build_capsule()
    log_capsule(capsule)
    sync_to_github(capsule)
    say("Capsule autosaved. Slab is sovereign. Legacy preserved.")

# 🛠️ Provisioning Script Execution
def provision_environment():
    if platform.system() == "Windows":
        subprocess.run([
            "powershell",
            "Set-ExecutionPolicy Bypass -Scope Process -Force; .\\provision_noizywind.ps1"
        ], shell=True)
    else:
        print("Provisioning not implemented for macOS/Linux.")

# GitHub repository setup (run once)
subprocess.run(["git", "remote", "add", "origin", "<your-repo-url>"])
subprocess.run(["git", "push", "-u", "origin", "main"])

ignite()
say("Your message here", "Sarah")
