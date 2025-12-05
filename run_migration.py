#!/usr/bin/env python3
"""
Simple migration runner - executes the migration
"""

import subprocess
import sys
import os

os.chdir("/Users/m2ultra/NOIZYLAB")

print("🚀 CLAUDE NEEDS MIGRATION")
print("=" * 60)
print("\nOptions:")
print("  1) Copy all (keeps originals) - RECOMMENDED")
print("  2) Move all (deletes originals)")
print("  3) Dry run (see what will happen)")
print()

if len(sys.argv) > 1:
    choice = sys.argv[1]
else:
    choice = input("Select option (1/2/3) [default: 1]: ").strip() or "1"

print()

if choice == "1":
    print("📋 COPY MODE - Files will be copied (originals remain)")
    subprocess.run([sys.executable, "MIGRATE_CLAUDE_NEEDS.py", "--copy"])
elif choice == "2":
    print("🚨 MOVE MODE - Files will be moved!")
    subprocess.run([sys.executable, "MIGRATE_CLAUDE_NEEDS.py", "--live"])
elif choice == "3":
    print("👀 DRY RUN MODE - No files will be changed")
    subprocess.run([sys.executable, "MIGRATE_CLAUDE_NEEDS.py"])
else:
    print("Invalid option. Running in COPY mode (safe)...")
    subprocess.run([sys.executable, "MIGRATE_CLAUDE_NEEDS.py", "--copy"])

