import os
import subprocess
import yaml
from logger import log_step

MANIFEST_PATH = "install_manifest.yaml"
VOICE_PATH = "voice_triggers.yaml"

# Helper to run shell commands and log output/errors

def run_cmd(cmd, step, device):
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log_step(step, device, "completed")
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        log_step(step, device, "error", error=e.stderr.decode())
        return None

# Ritual automation for OMEN & Inspiron

def automate_install(device):
    steps = [
        "Prep Install Media",
        "BIOS/UEFI Rituals",
        "Windows 10 Install",
        "Post-Install Drivers"
    ]
    for step in steps:
        print(f"Running {step} for {device}...")
        log_step(step, device, "in-progress")
        # Device-specific logic
        if device == "D-LINK":
            # Take over D-LINK: install network adapter, configure network
            print("Taking over D-LINK network adapter...")
            # Simulate network setup
            log_step(step, device, "completed")
        else:
            # Simulate install for OMEN/Inspiron
            log_step(step, device, "completed")

# Voice trigger handler

def handle_voice_trigger(trigger):
    with open(VOICE_PATH) as f:
        voice = yaml.safe_load(f)
    flow = voice["flows"].get(trigger)
    if not flow:
        print(f"Unknown trigger: {trigger}")
        return
    device = trigger.split("_")[1]
    automate_install(device)

if __name__ == "__main__":
    # Install Windows 10 on OMEN, Inspiron, and take over D-LINK
    for dev in ["OMEN", "Inspiron", "D-LINK"]:
        print(f"\n=== Starting install for {dev} ===")
        automate_install(dev)
# Example usage:
# handle_voice_trigger("install_OMEN")
# handle_voice_trigger("repair_Inspiron")
