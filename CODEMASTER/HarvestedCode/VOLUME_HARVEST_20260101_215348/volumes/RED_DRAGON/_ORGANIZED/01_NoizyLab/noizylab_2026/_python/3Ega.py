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


CLEANUP_CMD = "cleanup big house"
SYNONYMS = {
    "tidy big house": CLEANUP_CMD,
    "sort drives": CLEANUP_CMD,
    "organize volumes": CLEANUP_CMD,
    "parallels start": "launch parallels",
    "parallels boot": "launch parallels",
    "prep store": "prep appstore",
    "app store": "prep appstore",
    "checklist": "write checklist",
}

def normalize_command(cmd_str: str) -> str:
    """Normalize synonyms to canonical form."""
    cmd = cmd_str.lower().strip()
    for alt, canonical in SYNONYMS.items():
        if alt in cmd:
            return canonical
    return cmd

def run_bucket(bucket_name: str, cmd_str: str):
    if bucket_name not in BUCKETS:
        print(f"❓ Unknown bucket: {bucket_name}. Falling back to {DEFAULT_BUCKET}.")
        bucket_name = DEFAULT_BUCKET
    target = BUCKETS[bucket_name]
    if not target.exists():
        print(f"⚠️ Bucket {bucket_name} file not found at {target}")
        return
    try:
        subprocess.run(["python3", str(target), cmd_str], check=False)
    except subprocess.SubprocessError as e:
        print(f"⚠️ Error running {bucket_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bucket_switcher.py \"[bucket] command...\"")
        sys.exit(1)

    parts = sys.argv[1].split(maxsplit=1)

    if len(parts) == 1:
        # No bucket provided → Bubba default
        bucket_name = DEFAULT_BUCKET
        cmd_str = normalize_command(parts[0])
    else:
        bucket_name = parts[0].lower()
        cmd_str = normalize_command(parts[1])

    run_bucket(bucket_name, cmd_str)
