#!/usr/bin/env python3
"""
Execute Move All - Direct execution
"""

import subprocess
import sys
import os

os.chdir("/Users/m2ultra/NOIZYLAB")

print("🚀 MOVE ALL & SORT ALL")
print("=" * 60)
print("\n⚠️  WARNING: This will MOVE all files from _CLAUDE_NEEDS")
print("   and DELETE the folder after migration!")
print()

confirm = input("Type 'YES MOVE ALL' to proceed: ").strip()

if confirm != "YES MOVE ALL":
    print("❌ Cancelled")
    sys.exit(1)

print("\n🚀 Starting migration...")
print()

# Execute migration (this will also trigger auto-sort)
subprocess.run([sys.executable, "MIGRATE_CLAUDE_NEEDS.py", "--live"])

print("\n✅ Complete!")

