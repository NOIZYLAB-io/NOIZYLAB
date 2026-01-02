import subprocess
import datetime

VM_NAME = "NOIZYWIN"

def heal_and_restart():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    snap_name = f"heal-{timestamp}"
    print(f"📸 Creating snapshot {snap_name}...")
    subprocess.run(["prlctl", "snapshot", VM_NAME, "--name", snap_name, "--description", "Healing ritual snapshot"])
    print("🔁 Restarting VM...")
    subprocess.run(["prlctl", "stop", VM_NAME])
    subprocess.run(["sleep", "3"])
    subprocess.run(["prlctl", "start", VM_NAME])
    print("✅ VM healed and restarted.")

if __name__ == "__main__":
    heal_and_restart()
