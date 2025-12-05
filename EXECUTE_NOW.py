#!/usr/bin/env python3
"""
🚀 EXECUTE NOW - IMMEDIATE FILE ORGANIZATION 🚀

This will ACTUALLY move/copy files to organized folders RIGHT NOW!
"""

import os
import sys
from pathlib import Path

# Change to script directory
os.chdir(Path(__file__).parent)

print("="*80)
print("🚀 IMMEDIATE FILE ORGANIZATION")
print("="*80)
print("\n⭐⭐⭐ HARD RULE WILL BE ENFORCED ⭐⭐⭐")
print("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!\n")

print("Choose organization method:\n")
print("1. ⚡ TURBO (5-10 seconds) - FASTEST!")
print("2. 📊 MEGA (30-60 seconds) - Full analysis")
print("3. ⚖️ ULTIMATE (15-30 seconds) - Balanced")
print("4. 🗄️ 6TB FULL SCAN (20-40 minutes) - Scan entire drive")
print("5. Cancel")

choice = input("\nEnter choice (1-5): ").strip()

if choice == '1':
    print("\n🚀 Launching TURBO ORGANIZER...")
    print("This will organize 'WAVES TO MOVE' folder in seconds!\n")
    import TURBO_ORGANIZER
    TURBO_ORGANIZER.main()
    
elif choice == '2':
    print("\n📊 Launching MEGA ORGANIZER...")
    print("Full featured organization with all analysis!\n")
    import MEGA_ULTIMATE_ORGANIZER
    MEGA_ULTIMATE_ORGANIZER.main()
    
elif choice == '3':
    print("\n⚖️ Launching ULTIMATE ORGANIZER...")
    print("Balanced organization!\n")
    import ULTIMATE_ORGANIZER
    ULTIMATE_ORGANIZER.main()
    
elif choice == '4':
    print("\n🗄️ Launching 6TB FULL SCAN...")
    print("This will scan your ENTIRE drive!\n")
    print("⚠️ This takes 20-40 minutes. Continue? (y/n): ", end='')
    confirm = input().strip().lower()
    if confirm == 'y':
        # Import the 6TB scanner module name without extension
        import importlib.util
        spec = importlib.util.spec_from_file_location("scanner6tb", "6TB_SCANNER.py")
        scanner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner)
        scanner.main()
    else:
        print("Cancelled.")
        
elif choice == '5':
    print("\nCancelled.")
    sys.exit(0)
    
else:
    print("\nInvalid choice!")
    sys.exit(1)

print("\n" + "="*80)
print("✅ ORGANIZATION COMPLETE!")
print("="*80)
print("\nCheck your organized files in:")
print("  • ORGANIZED_WAVES/ORIGINAL_COMPOSITIONS/ ⭐⭐⭐")
print("  • ORGANIZED_WAVES/COMMERCIAL_SAMPLES/")
print("\nor:")
print("  • 6TB_ORGANIZED/ORIGINAL_COMPOSITIONS/ ⭐⭐⭐")
print("  • 6TB_ORGANIZED/Commercial/")
print("\n⭐ BACKUP YOUR ORIGINALS IMMEDIATELY! ⭐")
print("="*80 + "\n")

