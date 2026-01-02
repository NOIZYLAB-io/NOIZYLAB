import subprocess
import datetime
import os

VM_NAME = "NOIZYWIN"
LOG_DIR = os.path.expanduser("~/noizylog")
os.makedirs(LOG_DIR, exist_ok=True)

def create_snapshot():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    snap_name = f"heal-{timestamp}"
    description = "Healing ritual snapshot"
    cmd = ["prlctl", "snapshot", VM_NAME, "--name", snap_name, "--description", description]
    result = subprocess.run(cmd, capture_output=True, text=True)
    log_path = os.path.join(LOG_DIR, "snapshot.log")
    with open(log_path, "a") as log:
        log.write(f"{timestamp}: Created snapshot {snap_name}\n{result.stdout}\n")
    print(f"✅ Snapshot {snap_name} created.")

if __name__ == "__main__":
    create_snapshot()
