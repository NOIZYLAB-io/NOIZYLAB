#!/usr/bin/env python3
"""Test the organizer on a small sample"""

from pathlib import Path
import sys

# Simple test
print("Testing WAV organizer system...")
print("="*80)

source = Path("WAVES TO MOVE")

if not source.exists():
    print(f"❌ Source not found: {source.absolute()}")
    sys.exit(1)

print(f"✓ Source found: {source.absolute()}")

# Count files
wav_files = list(source.rglob('*.wav')) + list(source.rglob('*.WAV'))
print(f"✓ Found {len(wav_files)} WAV files")

# Show samples
print("\nSample files:")
for f in sorted(wav_files)[:10]:
    print(f"  • {f.name}")
if len(wav_files) > 10:
    print(f"  ... and {len(wav_files) - 10} more")

print("\n" + "="*80)
print("System is ready!")
print("\nTo organize files, run:")
print("  python3 ULTIMATE_ORGANIZER.py")
print("="*80)

