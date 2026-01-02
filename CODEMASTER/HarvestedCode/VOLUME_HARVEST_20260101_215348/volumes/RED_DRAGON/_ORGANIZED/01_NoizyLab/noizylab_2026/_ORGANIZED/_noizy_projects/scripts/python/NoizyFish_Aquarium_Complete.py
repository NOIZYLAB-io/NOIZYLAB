#!/usr/bin/env python3
"""
NoizyFish_Aquarium Complete Automation Script
Organizes, cleans, backs up, runs pipeline, manages environments, logs, and notifies.
"""
import os
import shutil
import subprocess
from pathlib import Path
import logging
from datetime import datetime

HOME = Path.home()
AQUARIUM = HOME / "NoizyFish_Aquarium"
DATA = AQUARIUM / "data"
LOGS = AQUARIUM / "logs"
COCKPIT = AQUARIUM / "🐍 Python_Projects" / "NoizyCockPit"
BACKUP = HOME / "NoizyFish_Aquarium_backup"
ENV_DIR = COCKPIT / "venv"
REQUIREMENTS = COCKPIT / "requirements.txt"
README = AQUARIUM / "README.md"

# Setup logging
LOGS.mkdir(parents=True, exist_ok=True)
logfile = LOGS / f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=str(logfile), level=logging.INFO)
logging.info('Pipeline started')

# 1. Organize files
DATA.mkdir(parents=True, exist_ok=True)
for src in [HOME / "account_alignment.csv"]:
    if src.exists():
        shutil.move(str(src), str(DATA / src.name))
for src in [HOME / "account_alignment.py", HOME / "collect_by_name.sh", HOME / "force_permissions.sh"]:
    if src.exists():
        shutil.move(str(src), str(AQUARIUM / src.name))
logging.info('Files organized')

# 2. Remove temp, backup, and clutter files
for pattern in [".zcompdump.*", ".zshrc.bak", ".zshrc.save", ".zprofile.bak", ".profile.pysave", ".CFUserTextEncoding", ".userchain"]:
    for f in HOME.glob(pattern):
        f.unlink(missing_ok=True)
for folder in [".zsh_sessions", ".Trash"]:
    shutil.rmtree(HOME / folder, ignore_errors=True)
logging.info('Clutter removed')

# 3. Archive logs
for logdir in [HOME / ".aitk", HOME / ".codemate", HOME / ".console-ninja"]:
    if logdir.exists():
        for log in logdir.rglob("*.log"):
            shutil.move(str(log), str(LOGS / log.name))
logging.info('Logs archived')

# 4. Handle Untitled files
for f in HOME.glob("Untitled*"):
    f.unlink(missing_ok=True)
logging.info('Untitled files handled')

# 5. Backup
BACKUP.mkdir(parents=True, exist_ok=True)
subprocess.run(["rsync", "-av", "--delete", str(AQUARIUM), str(BACKUP)])
logging.info('Backup complete')

# 6. Python environment management
if REQUIREMENTS.exists():
    if not ENV_DIR.exists():
        subprocess.run(["python3", "-m", "venv", str(ENV_DIR)])
    subprocess.run([str(ENV_DIR / "bin" / "pip"), "install", "-r", str(REQUIREMENTS)])
logging.info('Python environment ready')

# 7. Run pipeline scripts
def run_script(script_path):
    if script_path.exists():
        result = subprocess.run([str(ENV_DIR / "bin" / "python"), str(script_path)])
        logging.info(f'Ran {script_path.name} with exit code {result.returncode}')

run_script(COCKPIT / "inbox_scan.py")
run_script(COCKPIT / "subscription_scan.py")
run_script(COCKPIT / "sync.py")

# 8. Open results if available (macOS only)
result_csv = COCKPIT / "data" / "platform_trace.csv"
if result_csv.exists():
    subprocess.run(["open", str(result_csv)])
logging.info('Results opened')

# 9. Desktop notification (macOS)
subprocess.run(["osascript", "-e", "display notification \"NoizyFish_Aquarium pipeline complete!\" with title \"NoizyCockPit\""])
logging.info('Notification sent')

# 10. Documentation
if not README.exists():
    with open(README, "w") as f:
        f.write("""# NoizyFish_Aquarium\n\n## Setup\n- Clone repo\n- Create and activate virtualenv\n- Install requirements\n\n## Usage\n- Run Master_AutoRun.py or Master_AutoRun.sh\n\n## Automation\n- Scripts auto-organize, clean, backup, and run pipeline\n""")
logging.info('README generated')

print("✅ NoizyFish_Aquarium: Complete automation finished!")
