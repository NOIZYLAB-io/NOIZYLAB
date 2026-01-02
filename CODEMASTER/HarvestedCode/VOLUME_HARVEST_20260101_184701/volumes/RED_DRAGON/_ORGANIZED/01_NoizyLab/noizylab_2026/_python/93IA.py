#!/usr/bin/env python3
"""
bucket_switcher.py
Cha-Cha uses this to tell Bubba which "bucket" (project) to talk to.
Now includes Super Brain.
"""

import subprocess, sys
from pathlib import Path

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"

BUCKETS = {
    "bubba": WORKSPACE / "bubba_hand_of_god.py",
    "superbrain": WORKSPACE / "super_brain.py",
    "noizybrain": WORKSPACE / "noizy_brain.py",
    # add more buckets here as your empire grows
}

def run_bucket(bucket: str, command: str):
    if bucket not in BUCKETS:
        print(f"❓ Unknown bucket: {bucket}")
        return
    target = BUCKETS[bucket]
    if not target.exists():
        print(f"⚠️ Bucket {bucket} file not found at {target}")
        return
    try:
        subprocess.run(["python3", str(target), command], check=False)
    except Exception as e:
        print(f"⚠️ Error running {bucket}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bucket_switcher.py \"bucket command...\" or \"command...\" (defaults to Bubba)")
        sys.exit(1)

    parts = sys.argv[1].split(maxsplit=1)
    if parts[0].lower() in BUCKETS:
        bucket = parts[0].lower()
        command = parts[1] if len(parts) > 1 else ""
    else:
        bucket = "bubba"
        command = sys.argv[1]

    run_bucket(bucket, command)
