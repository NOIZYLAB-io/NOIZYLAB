#!/usr/bin/env python3
"""
⚡ RUN TURBO NOW - FASTEST EXECUTION ⚡
No menus, no waiting - just GO!
"""

import os
from pathlib import Path

# Change to script directory
os.chdir(Path(__file__).parent)

print("="*80)
print("⚡ TURBO ORGANIZER - EXECUTING NOW! ⚡")
print("="*80)
print("\n⭐⭐⭐ HARD RULE ACTIVE ⭐⭐⭐")
print("NO METADATA = YOUR ORIGINAL COMPOSITION!\n")
print("Starting in 3 seconds...")

import time
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("\n🚀 TURBO MODE ACTIVATED!\n")

# Import and run TURBO
try:
    import TURBO_ORGANIZER
    TURBO_ORGANIZER.main()
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTrying direct execution...")
    exec(open("TURBO_ORGANIZER.py").read())

print("\n" + "="*80)
print("✅ COMPLETE!")
print("="*80)
print("\nYour files are now organized in:")
print("  ORGANIZED_WAVES/ORIGINAL_COMPOSITIONS/ ⭐⭐⭐")
print("  ORGANIZED_WAVES/COMMERCIAL_SAMPLES/")
print("\n⭐ CHECK YOUR ORIGINALS AND BACKUP NOW! ⭐")
print("="*80 + "\n")

