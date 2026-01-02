#!/usr/bin/env python3
"""
bucket_switcher.py
Cha-Cha routes commands to Bubba, Super Brain, Noizy Brain, etc.
Features:
 - Default fallback bucket (Bubba).
 - Synonym mapping for more natural commands.
"""

import subprocess, sys
from pathlib import Path

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"

BUCKETS = {
    "bubba": WORKSPACE / "bubba_hand_of_god.py",
    "superbrain": WORKSPACE / "super_brain.py",
    "noizybrain": WORKSPACE / "noizy_brain.py",
}

DEFAULT_BUCKET = "bubba"

# ---------- Synonym Map ----------
# Maps alternate phrases to canonical bucket commands
SYNONYMS = {
    "tidy big house": "cleanup big house",
    "sort drives": "cleanup big house",
    "organize volumes": "cleanup big house",
    "parallels start": "launch parallels",
    "parallels boot": "launch parallels",
    "prep store": "prep appstore",
    "app store": "prep appstore",
    "checklist": "write checklist",
}

def normalize_command(command: str) -> str:
    """Normalize synonyms to canonical form."""
    cmd = command.lower().strip()
    for alt, canonical in SYNONYMS.items():
        if alt in cmd:
            return canonical
    return cmd

def run_bucket(bucket: str, command: str):
    if bucket not in BUCKETS:
        print(f"❓ Unknown bucket: {bucket}. Falling back to {DEFAULT_BUCKET}.")
        bucket = DEFAULT_BUCKET
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
        print("Usage: python3 bucket_switcher.py \"[bucket] command...\"")
        sys.exit(1)

    parts = sys.argv[1].split(maxsplit=1)

    if len(parts) == 1:
        # No bucket provided → Bubba default
        bucket = DEFAULT_BUCKET
        command = normalize_command(parts[0])
    else:
        bucket = parts[0].lower()
        command = normalize_command(parts[1])

    run_bucket(bucket, command)
