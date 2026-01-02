#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/check_kontakt_lab_status.py
# NOIZYGENIE: KONTAKT_LAB Status Checker

from pathlib import Path
import os

def check_kontakt_lab_status():
    """Check the current state of KONTAKT_LAB"""
    print("🧙‍♂️ NOIZYGENIE: KONTAKT_LAB STATUS CHECK")
    print("=" * 60)
    
    kontakt_lab = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
    
    if not kontakt_lab.exists():
        print("❌ KONTAKT_LAB not found!")
        return
    
    # Organization folders (expected to remain)
    organization_folders = {
        "DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"
    }
    
    # Check what's currently in KONTAKT_LAB
    items = list(kontakt_lab.iterdir())
    
    print(f"📊 Current items in KONTAKT_LAB: {len(items)}")
    print()
    
    organization_items = []
    library_items = []
    other_items = []
    
    for item in items:
        if item.name in organization_folders:
            organization_items.append(item)
        elif item.name.endswith('.py'):
            organization_items.append(item)
        elif item.name.endswith(('.txt', '.html', '.json')):
            other_items.append(item)
        else:
            library_items.append(item)
    
    print("🏗️ ORGANIZATION STRUCTURE:")
    for item in organization_items:
        if item.is_dir():
            try:
                count = len(list(item.iterdir()))
                print(f"   📁 {item.name} ({count} items)")
            except:
                print(f"   📁 {item.name}")
        else:
            print(f"   📄 {item.name}")
    
    print(f"\n📚 REMAINING LIBRARIES: {len(library_items)}")
    for item in library_items[:10]:  # Show first 10
        print(f"   📦 {item.name}")
    if len(library_items) > 10:
        print(f"   ... and {len(library_items) - 10} more")
    
    print(f"\n📄 OTHER FILES: {len(other_items)}")
    for item in other_items:
        print(f"   📄 {item.name}")
    
    # Check if organization has been run
    deep_organized = kontakt_lab / "DEEP_ORGANIZED"
    if deep_organized.exists():
        print(f"\n✅ ORGANIZATION COMPLETE!")
        organized_count = 0
        try:
            for category in deep_organized.iterdir():
                if category.is_dir():
                    for subfolder in category.iterdir():
                        if subfolder.is_dir() and subfolder.name != "README.md":
                            count = len(list(subfolder.iterdir()))
                            organized_count += count
        except:
            pass
        print(f"   📦 {organized_count} items organized")
    else:
        print(f"\n⏳ ORGANIZATION NOT YET RUN")
        print("   📝 Run organize_projects.py to organize everything!")
    
    # Check orphans folder
    orphans_path = Path("/Volumes/6TB/_NI_2026/_ORPHANS")
    if orphans_path.exists():
        orphan_count = len(list(orphans_path.iterdir()))
        print(f"\n🏠 ORPHAN SANCTUARY: {orphan_count} items")
    else:
        print(f"\n🏠 ORPHAN SANCTUARY: Not yet created")
    
    # Summary
    print(f"\n" + "=" * 60)
    if len(library_items) == 0:
        print("🎉 KONTAKT_LAB IS CLEAN! All libraries organized!")
    elif len(library_items) > 0 and deep_organized.exists():
        print("⚠️  Some libraries remain - check if organization is complete")
    else:
        print("📋 Ready for organization - run organize_projects.py!")

if __name__ == "__main__":
    check_kontakt_lab_status()
