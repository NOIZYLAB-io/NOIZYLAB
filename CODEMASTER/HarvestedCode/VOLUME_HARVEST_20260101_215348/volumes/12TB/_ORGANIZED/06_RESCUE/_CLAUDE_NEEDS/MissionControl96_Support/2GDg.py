#!/usr/bin/env python3
"""
🚀 NOIZYGENIE AGENT MODE - PRE-FLIGHT CHECK
Quick overview before launching full agent mode
"""

from pathlib import Path

ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
TARGET_2026 = Path.home() / "Desktop" / "KONTAKT_LAB_2026"

def pre_flight_check():
    print("🚀 NOIZYGENIE AGENT MODE - PRE-FLIGHT CHECK")
    print("=" * 50)
    
    # Check source directory
    if not ROOT.exists():
        print("❌ KONTAKT_LAB directory not found!")
        return False
    
    # Count libraries
    organized_libs = 0
    unorganized_libs = 0
    
    # Count organized
    for category_dir in ROOT.iterdir():
        if category_dir.is_dir() and category_dir.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_')):
            organized_libs += len([d for d in category_dir.iterdir() if d.is_dir()])
    
    # Count unorganized
    for item in ROOT.iterdir():
        if (item.is_dir() and 
            not item.name.startswith('.') and 
            not item.name.startswith('_') and
            not item.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_')) and
            item.name not in ['REPORTS', 'BACKUP', 'ORGANIZED_LIBRARIES', 'TEMP_PROCESSING', 'SAMPLE_ARCHIVES']):
            unorganized_libs += 1
    
    total_libs = organized_libs + unorganized_libs
    
    print(f"📊 LIBRARY INVENTORY:")
    print(f"   📁 Organized Libraries: {organized_libs}")
    print(f"   📦 Unorganized Libraries: {unorganized_libs}")
    print(f"   📚 Total Libraries: {total_libs}")
    
    print(f"\n🎯 MISSION OBJECTIVES:")
    print(f"   1. Verify integrity of ALL {total_libs} libraries")
    print(f"   2. Identify perfectly rebuilt libraries")
    print(f"   3. Create KONTAKT_LAB_2026 structure")
    print(f"   4. Migrate only PERFECT libraries to 2026")
    print(f"   5. Generate comprehensive rebuild report")
    
    print(f"\n📋 WHAT WILL HAPPEN:")
    print(f"   🔍 Deep scan each library for:")
    print(f"      • .nki/.nkm instrument files")
    print(f"      • .wav/.aif/.ncw sample files") 
    print(f"      • File integrity and completeness")
    print(f"   📦 Create 2026 folder structure")
    print(f"   🚀 Copy ONLY perfectly rebuilt libraries")
    print(f"   📋 Generate detailed reports")
    
    # Check if 2026 already exists
    if TARGET_2026.exists():
        print(f"\n⚠️  WARNING: KONTAKT_LAB_2026 already exists!")
        print(f"   Agent will merge/update existing structure")
    
    print(f"\n🚀 READY FOR AGENT MODE LAUNCH!")
    print(f"   Run: python3 noizygenie_agent_mode.py")
    
    return True

if __name__ == "__main__":
    pre_flight_check()