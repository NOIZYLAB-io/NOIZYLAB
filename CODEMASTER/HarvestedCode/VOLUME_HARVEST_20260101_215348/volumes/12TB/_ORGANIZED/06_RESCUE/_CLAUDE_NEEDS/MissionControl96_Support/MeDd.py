import subprocess
import time
import os
from pathlib import Path

# Paths to launch
DAEMON_PATH = str(Path.home() / "WORK_OF_TODAY/utilities/noizylab_autokeep_daemon.py")
DASHBOARD_PATH = str(Path.home() / "Documents/overlays/noizy_sistine_chapel.html")

# Launch NOIZYLAB AutoKeep Daemon
subprocess.Popen(["python3", DAEMON_PATH])
print("NOIZYLAB AutoKeep Daemon launched.")

# Open dashboard overlay
subprocess.run(["open", DASHBOARD_PATH])
print("NOIZY Sistine Chapel dashboard launched.")

# Announce launch
os.system('say "NOIZYLAB Candle is lit. Capsule automation and dashboard are live!"')
