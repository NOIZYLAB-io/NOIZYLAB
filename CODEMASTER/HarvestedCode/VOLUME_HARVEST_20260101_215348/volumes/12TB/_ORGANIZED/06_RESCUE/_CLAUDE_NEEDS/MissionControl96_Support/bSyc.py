import subprocess
import datetime
import os

NODES = ["noizyrouter.local", "noizyvm1.local", "noizywin.local"]
SCRIPT_PATH = "/Users/rob/noizy-rituals/silence-heal.sh"
LOG_PATH = os.path.expanduser("~/noizylog/remote-sync.log")

def sync_rituals():
    with open(LOG_PATH, "a") as log:
        log.write(f"{datetime.datetime.now()}: 🌐 Starting remote ritual sync\n")
        for node in NODES:
            log.write(f"{datetime.datetime.now()}: 🔁 Syncing to {node}\n")
            cmd = f"ssh rob@{node} 'bash -s' < {SCRIPT_PATH}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            log.write(result.stdout + "\n")
            log.write(f"{datetime.datetime.now()}: ✅ Ritual deployed to {node}\n")
        log.write(f"{datetime.datetime.now()}: 🧬 Sync complete\n")

if __name__ == "__main__":
    sync_rituals()
