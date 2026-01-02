import os
import subprocess
import datetime
import json
import platform

def say(msg):
    try:
        subprocess.run(["say", msg])  # macOS
    except:
        subprocess.run(["powershell", "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{}')".format(msg)])

def verify_windows():
    version = platform.platform()
    activated = subprocess.run(["powershell", "(Get-WmiObject -Class SoftwareLicensingProduct | Where-Object {$_.PartialProductKey}) | Select-Object LicenseStatus"], capture_output=True, text=True).stdout
    health = subprocess.run(["powershell", "Get-PnpDevice | Where-Object {$_.Status -ne 'OK'}"], capture_output=True, text=True).stdout
    return "✅" if "1" in activated and not health.strip() else "⚠️"

def infuse_sequoia():
    agents = ["Strategist", "Healer", "Archivist", "Visionary"]
    capsule = {
        "timestamp": datetime.datetime.now().isoformat(),
        "agents": agents,
        "rituals": ["overlay_launch", "capsule_build", "slab_scan"],
        "sequoia_logic": "Vertical agent orchestration + capsule economy"
    }
    with open("C:\🧞‍♂️NOIZYWIND\Legacy\sequoia_infusion_log.json", "w") as f:
        json.dump(capsule, f, indent=4)

def launch_overlay():
    subprocess.run(["start", "C:\🧞‍♂️NOIZYWIND\Overlays\planar_eyelevel.html"], shell=True)

def play_ambient():
    subprocess.run(["start", "C:\🧞‍♂️NOIZYWIND\Soundscapes\focused_loop.wav"], shell=True)

def build_capsule():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    capsule = f"C:\🧞‍♂️NOIZYWIND\Legacy\Capsule_{ts}.zip"
    subprocess.run(["powershell", "Compress-Archive", "-Path", "C:\🧞‍♂️NOIZYWIND\Legacy\*", "-DestinationPath", capsule])
    return capsule

def log_capsule(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "AutoSaved",
        "agent": "Archivist",
        "mood": "Focused"
    }
    with open("C:\🧞‍♂️NOIZYWIND\Legacy\autosave_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")

def sync_to_github(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "Pushed to GitHub (symbolic)"
    }
    with open("C:\🧞‍♂️NOIZYWIND\Legacy\capsule_sync_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")

# 🔥 Full Ritual Execution
say("Slab awakening. NoizyGenieMode ignition sequence initiated.")
status = verify_windows()
say(f"Slab verification status: {status}")
infuse_sequoia()
launch_overlay()
play_ambient()
capsule = build_capsule()
log_capsule(capsule)
sync_to_github(capsule)
say("Capsule autosaved. Slab is sovereign. Legacy preserved.")
