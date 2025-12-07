#!/usr/bin/env python3
"""
MASTER REBUILD - Complete System Reorganization
One-click professional library rebuild
"""

import subprocess
import sys
from pathlib import Path

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")

def run_script(script_name, description):
    """Run a script"""
    print(f"\n{'='*70}")
    print(f"🚀 {description}")
    print(f"{'='*70}\n")
    
    script_path = WORKSPACE / script_name
    result = subprocess.run([sys.executable, str(script_path)], cwd=WORKSPACE)
    
    return result.returncode == 0

def main():
    print("\n" + "🏭"*35)
    print("  MASTER REBUILD - Complete Factory Reset")
    print("🏭"*35 + "\n")
    
    print("This will execute the complete rebuild pipeline:")
    print("\n1. Create factory directory structure")
    print("2. Scan all files on both drives")
    print("3. Plan intelligent organization")
    print("4. Show preview of changes")
    print("\n⚠️  ALL OPERATIONS ARE IN DRY-RUN MODE BY DEFAULT")
    
    input("\nPress Enter to begin or Ctrl+C to cancel...")
    
    # Step 1: Quick preview
    print("\n" + "🎬"*35)
    print("STEP 1: DRIVE PREVIEW")
    print("🎬"*35)
    run_script("quick_preview.py", "Scanning drives")
    
    # Step 2: Factory organization
    print("\n" + "🎬"*35)
    print("STEP 2: FACTORY ORGANIZATION")
    print("🎬"*35)
    run_script("factory_organizer.py", "Planning factory organization")
    
    print("\n" + "="*70)
    print("✅ MASTER REBUILD PLANNING COMPLETE!")
    print("="*70)
    print("\n📊 Review the reports generated in SCAN_RESULTS/")
    print("💡 All operations were in DRY-RUN mode (safe)")
    print("\n🎯 Next steps:")
    print("  1. Review planned changes")
    print("  2. BACKUP your drives")
    print("  3. Edit scripts to enable live mode")
    print("  4. Execute the rebuild")

if __name__ == "__main__":
    main()

