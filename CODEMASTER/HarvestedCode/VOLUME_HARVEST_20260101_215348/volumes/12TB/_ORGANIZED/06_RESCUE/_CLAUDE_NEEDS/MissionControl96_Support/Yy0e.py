import os
import subprocess

BASE = os.path.expanduser("~/Desktop/NoizyFish")
modules = [
    "scripts/token_manager.py",
    "scripts/noizyfb_consolidator.py",
    "scripts/admin_snapshot.py",
    "scripts/legacy_sync.py"
]

def run_all():
    for module in modules:
        path = os.path.join(BASE, module)
        print(f"🚀 Running: {path}")
        subprocess.run(["python3", path])

if __name__ == "__main__":
    run_all()
