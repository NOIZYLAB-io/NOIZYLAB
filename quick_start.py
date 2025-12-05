#!/usr/bin/env python3
"""Quick starter - imports and runs the ultimate organizer"""
import sys
from pathlib import Path

# Ensure we're in the right directory
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

print("🎵 Starting Ultimate WAV Organizer...")
print("="*80)

try:
    import ULTIMATE_ORGANIZER
    print("\n✓ Successfully imported organizer")
    print("Running main function...\n")
    ULTIMATE_ORGANIZER.main()
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("\nTrying direct execution...")
    exec(open(script_dir / "ULTIMATE_ORGANIZER.py").read())
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

