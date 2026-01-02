import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# 🔧 Define your workspace
workspace = Path.home() / "VS_MONSTER_GRID"
folders = ["scripts", "capsules", "overlays"]
agents_md = workspace / "AGENTS.md"
log_file = workspace / "capsules" / "capsule_log.txt"

# 🧿 Step 1: Create Ritual Folders
def setup_workspace():
    print("🔧 Setting up your mythic workspace...")
    workspace.mkdir(exist_ok=True)
    for folder in folders:
        (workspace / folder).mkdir(exist_ok=True)
    if not agents_md.exists():
        agents_md.write_text("# Noizy.ai Ritual Agent\n- Purpose: Execute capsule rituals\n- Auto-approve: overlays/, scripts/\n- Confirm edits: AGENTS.md, licensing.json")
    print("✅ Workspace ready.")

# 🧠 Step 2: Check Python Install (MacStudio)
def check_python():
    print("🧠 Checking Python installation...")
    try:
        subprocess.run(["python3", "--version"], check=True)
        print("✅ Python3 is installed.")
    except subprocess.CalledProcessError:
        print("⚠️ Python3 not found. Installing via Homebrew...")
        subprocess.run(['/bin/bash', '-c', "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])
        subprocess.run(["brew", "install", "python"])
        print("✅ Python3 installed.")

# 🔊 Step 3: Run Capsule Ritual
def run_capsule():
    capsule_script = workspace / "scripts" / "inject_capsule.py"
    if capsule_script.exists():
        print("🔊 Running capsule injector...")
        subprocess.run(["python3", str(capsule_script)])
        log_capsule("inject_capsule.py executed")
    else:
        print("⚠️ No capsule injector found. Create 'inject_capsule.py' in scripts/")
        log_capsule("inject_capsule.py missing")

# 🛡️ Step 4: Protect Slab Sovereignty
def protect_files():
    protected = ["AGENTS.md", "capsules/licensing.json"]
    print("🛡️ Protecting sacred files...")
    for file in protected:
        path = workspace / file
        if path.exists():
            os.chmod(path, 0o444)  # Read-only
            print(f"🔒 {file} locked.")

# 📜 Step 5: Log Capsule Rituals
def log_capsule(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as log:
        log.write(f"[{timestamp}] {message}\n")

# 🚀 Run Ritual
if __name__ == "__main__":
    setup_workspace()
    check_python()
    run_capsule()
    protect_files()
    print("🌟 Ritual complete. Your cockpit is ready.")
