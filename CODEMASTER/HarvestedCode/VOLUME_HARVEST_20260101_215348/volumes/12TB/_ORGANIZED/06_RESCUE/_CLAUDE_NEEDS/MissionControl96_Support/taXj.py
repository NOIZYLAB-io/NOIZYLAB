#!/usr/bin/env python3
"""
🎹 NOIZYGENIE Interactive Library Organizer
Interactive tool for categorizing KONTAKT libraries
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"

CATEGORIES = {
    "1": "01_ELECTRONIC",
    "2": "02_ORCHESTRAL", 
    "3": "03_ACOUSTIC",
    "4": "04_URBAN",
    "5": "05_ROCK_POP",
    "6": "06_WORLD_ETHNIC",
    "7": "07_SYNTHESIZERS",
    "8": "08_DRUMS_PERCUSSION",
    "9": "09_LOOPS_GROOVES",
    "10": "10_SOUNDSCAPES_FX",
    "11": "11_VOCALS",
    "12": "12_CONSTRUCTION_KITS",
    "13": "13_MULTIS_COMBIS",
    "s": "SKIP",
    "q": "QUIT"
}

def get_unorganized_libraries():
    """Get libraries that need organization"""
    unorganized = []
    for item in ROOT.iterdir():
        if (item.is_dir() and 
            not item.name.startswith('.') and 
            not item.name.startswith('_') and
            not item.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_')) and
            item.name not in ['REPORTS', 'BACKUP', 'ORGANIZED_LIBRARIES', 'TEMP_PROCESSING', 'SAMPLE_ARCHIVES']):
            unorganized.append(item.name)
    return sorted(unorganized)

def show_menu():
    """Show categorization menu"""
    print("\n🎯 Choose Category:")
    print("─" * 30)
    print("1️⃣  ELECTRONIC        8️⃣   DRUMS_PERCUSSION")
    print("2️⃣  ORCHESTRAL        9️⃣   LOOPS_GROOVES") 
    print("3️⃣  ACOUSTIC          🔟  SOUNDSCAPES_FX")
    print("4️⃣  URBAN             1️⃣1️⃣  VOCALS")
    print("5️⃣  ROCK_POP          1️⃣2️⃣  CONSTRUCTION_KITS")
    print("6️⃣  WORLD_ETHNIC      1️⃣3️⃣  MULTIS_COMBIS")
    print("7️⃣  SYNTHESIZERS")
    print("─" * 30)
    print("s = Skip  |  q = Quit")

def preview_library_contents(lib_path):
    """Show a preview of what's in the library"""
    lib_path = Path(lib_path)
    files = list(lib_path.rglob("*"))[:10]  # First 10 files
    
    if files:
        print(f"\n📁 Library Preview ({len(files)} files shown):")
        for f in files:
            if f.is_file():
                print(f"   📄 {f.name}")
    else:
        print(f"\n📁 Empty or inaccessible library")

def move_library(lib_name, target_category):
    """Move library to target category"""
    source = ROOT / lib_name
    target = ROOT / target_category / lib_name
    
    try:
        # Ensure target directory exists
        target.parent.mkdir(exist_ok=True)
        
        # Move the library
        shutil.move(str(source), str(target))
        print(f"✅ Moved '{lib_name}' → {target_category}")
        return True
    except Exception as e:
        print(f"❌ Error moving '{lib_name}': {e}")
        return False

def batch_organize():
    """Interactive batch organization"""
    print("🎹 NOIZYGENIE Interactive Library Organizer")
    print("=" * 50)
    
    unorganized = get_unorganized_libraries()
    
    if not unorganized:
        print("✅ All libraries are already organized!")
        return
    
    print(f"📚 Found {len(unorganized)} libraries to organize")
    
    organized_count = 0
    
    for i, lib_name in enumerate(unorganized):
        print(f"\n🔍 Library {i+1}/{len(unorganized)}: {lib_name}")
        print("=" * 60)
        
        # Show library preview
        preview_library_contents(ROOT / lib_name)
        
        # Show menu
        show_menu()
        
        while True:
            choice = input(f"\n➤ Categorize '{lib_name}': ").strip().lower()
            
            if choice == 'q':
                print(f"\n📊 Session Summary: {organized_count} libraries organized")
                return
            elif choice == 's':
                print("⏭️  Skipped")
                break
            elif choice in CATEGORIES:
                if choice.isdigit() and int(choice) <= 13:
                    target = CATEGORIES[choice]
                    if move_library(lib_name, target):
                        organized_count += 1
                    break
                elif choice == "10" or choice == "11" or choice == "12" or choice == "13":
                    target = CATEGORIES[choice]
                    if move_library(lib_name, target):
                        organized_count += 1
                    break
            
            print("❌ Invalid choice. Try again.")
    
    print(f"\n🎉 Organization Complete!")
    print(f"📊 Total organized: {organized_count} libraries")

def quick_batch_by_pattern():
    """Quick organization by naming patterns"""
    print("\n🚀 Quick Pattern-Based Organization")
    print("=" * 40)
    
    unorganized = get_unorganized_libraries()
    
    # Common patterns
    patterns = {
        "runs": "09_LOOPS_GROOVES",
        "discolicks": "09_LOOPS_GROOVES", 
        "wavy": "07_SYNTHESIZERS",
        "sawtooth": "07_SYNTHESIZERS",
        "slow": "10_SOUNDSCAPES_FX",
        "celli": "02_ORCHESTRAL",
        "strings": "02_ORCHESTRAL",
        "brass": "02_ORCHESTRAL",
        "piano": "03_ACOUSTIC",
        "guitar": "03_ACOUSTIC",
        "drums": "08_DRUMS_PERCUSSION",
        "percussion": "08_DRUMS_PERCUSSION",
        "ethnic": "06_WORLD_ETHNIC",
        "world": "06_WORLD_ETHNIC"
    }
    
    auto_organized = 0
    
    for lib in unorganized:
        lib_lower = lib.lower()
        for pattern, category in patterns.items():
            if pattern in lib_lower:
                if move_library(lib, category):
                    auto_organized += 1
                break
    
    print(f"✅ Auto-organized {auto_organized} libraries by pattern")

if __name__ == "__main__":
    print("🎵 Choose organization method:")
    print("1 - Interactive (review each library)")
    print("2 - Quick pattern-based auto-organize")
    print("3 - Both (auto first, then interactive)")
    
    choice = input("\n➤ Your choice (1-3): ").strip()
    
    if choice == "1":
        batch_organize()
    elif choice == "2":
        quick_batch_by_pattern()
    elif choice == "3":
        quick_batch_by_pattern()
        batch_organize()
    else:
        print("Invalid choice")