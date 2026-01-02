import os
import shutil
import subprocess
from pathlib import Path

HOME = Path.home()
AQUARIUM = HOME / "NoizyFish_Aquarium"
DATA = AQUARIUM / "data"
LOGS = AQUARIUM / "logs"
COCKPIT = AQUARIUM / "🐍 Python_Projects" / "NoizyCockPit"

# Organize files
DATA.mkdir(parents=True, exist_ok=True)
for src in [HOME / "account_alignment.csv"]:
    if src.exists():
        shutil.move(str(src), str(DATA / src.name))
for src in [HOME / "account_alignment.py", HOME / "collect_by_name.sh", HOME / "force_permissions.sh"]:
    if src.exists():
        shutil.move(str(src), str(AQUARIUM / src.name))

# Remove temp, backup, and clutter files
for pattern in [".zcompdump.*", ".zshrc.bak", ".zshrc.save", ".zprofile.bak", ".profile.pysave", ".CFUserTextEncoding", ".userchain"]:
    for f in HOME.glob(pattern):
        f.unlink(missing_ok=True)
for folder in [".zsh_sessions", ".Trash"]:
    shutil.rmtree(HOME / folder, ignore_errors=True)

# Archive logs
LOGS.mkdir(parents=True, exist_ok=True)
for logdir in [HOME / ".aitk", HOME / ".codemate", HOME / ".console-ninja"]:
    if logdir.exists():
        for log in logdir.rglob("*.log"):
            shutil.move(str(log), str(LOGS / log.name))

# Handle Untitled files
for f in HOME.glob("Untitled*"):
    f.unlink(missing_ok=True)

# Run pipeline scripts
def run_script(script_path):
    if script_path.exists():
        subprocess.run(["python3", str(script_path)])

run_script(COCKPIT / "inbox_scan.py")
run_script(COCKPIT / "subscription_scan.py")
run_script(COCKPIT / "sync.py")

# Open results if available (macOS only)
result_csv = COCKPIT / "data" / "platform_trace.csv"
if result_csv.exists():
    subprocess.run(["open", str(result_csv)])

# Desktop notification (macOS)
subprocess.run(["osascript", "-e", "display notification \"NoizyFish_Aquarium pipeline complete!\" with title \"NoizyCockPit\""])

print("✅ Master automation complete!")
