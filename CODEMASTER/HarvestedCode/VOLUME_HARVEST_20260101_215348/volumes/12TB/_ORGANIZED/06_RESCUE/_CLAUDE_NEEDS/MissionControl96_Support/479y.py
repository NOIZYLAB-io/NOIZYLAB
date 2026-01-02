#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/check_kontakt_lab_status.py
# NOIZYGENIE: KONTAKT_LAB Status Checker

from pathlib import Path
import os
import shutil
from datetime import datetime

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

def delete_empty_folders_all_volumes():
    """Delete empty folders across all volumes except protected directories"""
    print("\n🧹 ELIMINATING EMPTY FOLDERS ACROSS ALL VOLUMES...")
    print("─" * 80)
    
    # Protected directories - DO NOT TOUCH
    protected_dirs = {
        "Mission Control", "System", "Library", "Applications", 
        "usr", "bin", "sbin", "etc", "var", "tmp", "dev", "proc",
        ".Spotlight-V100", ".fseventsd", ".TemporaryItems", ".Trashes", 
        "lost+found", ".git", "node_modules", "__pycache__", ".DS_Store"
    }
    
    # Get all volumes to scan
    volumes_to_scan = []
    
    # Add /Volumes
    volumes_path = Path("/Volumes")
    if volumes_path.exists():
        for vol in volumes_path.iterdir():
            if vol.is_dir() and not any(protected in str(vol) for protected in protected_dirs):
                volumes_to_scan.append(vol)
    
    # Add user directories
    user_dirs = [
        Path.home() / "Desktop",
        Path.home() / "Downloads", 
        Path.home() / "Documents",
        Path.home() / "Music",
        KONTAKT_LAB  # Include our KONTAKT_LAB
    ]
    
    for user_dir in user_dirs:
        if user_dir.exists():
            volumes_to_scan.append(user_dir)
    
    total_deleted = 0
    scanned_volumes = 0
    
    for volume in volumes_to_scan:
        if not volume.exists() or not volume.is_dir():
            continue
        
        volume_name = volume.name if volume.name else "Root"
        print(f"🔍 Scanning: {volume} ({volume_name})")
        
        deleted_count = 0
        try:
            # Walk through directories bottom-up (topdown=False)
            for root, dirs, files in os.walk(volume, topdown=False):
                root_path = Path(root)
                
                # Skip protected system directories
                if any(protected in str(root_path) for protected in protected_dirs):
                    continue
                
                # Skip our own organization directories
                if any(skip_dir in str(root_path) for skip_dir in 
                       ["DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER", "_ORPHANS"]):
                    continue
                
                try:
                    # Check if directory is truly empty
                    if root_path.is_dir():
                        try:
                            # Check if any files or folders exist
                            contents = list(root_path.iterdir())
                            if not contents:  # Completely empty
                                # Safety check - don't delete important paths
                                if (str(root_path) not in ["/", str(Path.home())] and 
                                    not any(protected in str(root_path) for protected in protected_dirs) and
                                    root_path != volume):  # Don't delete the volume root itself
                                    
                                    root_path.rmdir()
                                    deleted_count += 1
                                    total_deleted += 1
                                    print(f"🗑️  Deleted: {root_path}")
                        except OSError:
                            # Directory not actually empty or permission denied
                            continue
                except (PermissionError, OSError, FileNotFoundError):
                    # Skip directories we can't access
                    continue
        
        except (PermissionError, OSError) as e:
            print(f"⚠️  Access denied to {volume}: {e}")
            continue
        
        if deleted_count > 0:
            print(f"✅ {volume_name}: Deleted {deleted_count} empty folders")
        scanned_volumes += 1
    
    print(f"\n🎉 EMPTY FOLDER CLEANUP COMPLETE!")
    print(f"📊 Volumes Scanned: {scanned_volumes}")
    print(f"🗑️  Total Empty Folders Deleted: {total_deleted}")
    return total_deleted

def organize_kontakt_lab_items():
    """Organize all KONTAKT_LAB items into deep structure with ORPHAN sanctuary"""
    print("\n🔄 ORGANIZING KONTAKT_LAB ITEMS...")
    
    organized_count = 0
    collision_count = 0
    orphan_count = 0
    skip_dirs = {"DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"}
    
    # Create NI_2026 ORPHANS folder
    ni_2026_orphans = Path("/Volumes/6TB/_NI_2026/_ORPHANS")
    ni_2026_orphans.mkdir(parents=True, exist_ok=True)
    print(f"🏠 Created orphan sanctuary: {ni_2026_orphans}")
    
    for item in KONTAKT_LAB.iterdir():
        if item.name in skip_dirs:
            continue
        
        organized = False
        item_name = item.name
        
        # Find matching category
        for category, config in DEEP_PROJECT_STRUCTURE.items():
            patterns = config["patterns"]
            for pattern in patterns:
                if (pattern in item_name or 
                    item_name.startswith(pattern) or 
                    item_name.endswith(pattern) or
                    any(p in item_name for p in pattern.split("_"))):
                    
                    # Determine best subfolder
                    target_subfolder = "general"  # default
                    if category == "02_ETHNIC_WORLD":
                        if any(x in item_name.upper() for x in ["CHINA", "ERHU", "GAOHU"]):
                            target_subfolder = "asian"
                        elif any(x in item_name.upper() for x in ["MID_EAST", "EGYPTIAN"]):
                            target_subfolder = "middle_eastern"
                        elif "ALPINE" in item_name.upper():
                            target_subfolder = "european"
                    elif category == "03_WIND_INSTRUMENTS":
                        if "WHISTLE" in item_name.upper():
                            target_subfolder = "whistles"
                        elif any(x in item_name.upper() for x in ["FLUTE", "BAWU", "HULUSI"]):
                            target_subfolder = "flutes"
                    elif category == "09_LOOPS_CONSTRUCTION":
                        if "120" in item_name:
                            target_subfolder = "tempo_120"
                        elif "140" in item_name:
                            target_subfolder = "tempo_140"
                        elif "100" in item_name:
                            target_subfolder = "tempo_100"
                        elif "CONSTRUCTION" in item_name.upper():
                            target_subfolder = "construction"
                    
                    # Use first subfolder if no specific match
                    if target_subfolder == "general":
                        target_subfolder = config["subfolders"][0]
                    
                    target_path = ORGANIZED_ROOT / category / target_subfolder / item_name
                    
                    # Handle name collisions
                    counter = 1
                    while target_path.exists():
                        stem = target_path.stem if target_path.suffix else target_path.name
                        suffix = target_path.suffix
                        target_path = target_path.parent / f"{stem}_COPY_{counter}{suffix}"
                        counter += 1
                        collision_count += 1
                    
                    try:
                        shutil.move(str(item), str(target_path))
                        organized_count += 1
                        print(f"✅ {item_name} → {category}/{target_subfolder}")
                        organized = True
                        break
                    except Exception as e:
                        print(f"❌ Failed to move {item_name}: {e}")
                
                if organized:
                    break
            
            if organized:
                break
        
        # Move uncategorized items to ORPHANS in NI_2026
        if not organized and item.exists():
            orphan_path = ni_2026_orphans / item_name
            
            counter = 1
            while orphan_path.exists():
                stem = orphan_path.stem if orphan_path.suffix else orphan_path.name
                suffix = orphan_path.suffix
                orphan_path = orphan_path.parent / f"{stem}_COPY_{counter}{suffix}"
                counter += 1
            
            try:
                shutil.move(str(item), str(orphan_path))
                organized_count += 1
                orphan_count += 1
                print(f"🏠 ORPHAN: {item_name} → _ORPHANS")
            except Exception as e:
                print(f"❌ Failed to move orphan {item_name}: {e}")
                # Last resort - try local miscellaneous
                misc_path = ORGANIZED_ROOT / "99_MISCELLANEOUS" / item_name
                try:
                    shutil.move(str(item), str(misc_path))
                    organized_count += 1
                    print(f"📦 BACKUP: {item_name} → MISCELLANEOUS")
                except Exception as e2:
                    print(f"❌ FINAL FAILURE: {item_name} - {e2}")
    
    return organized_count, collision_count, orphan_count

def create_orphan_browser():
    """Create a browser for the ORPHANS folder"""
    print("\n🏠 CREATING ORPHAN BROWSER...")
    
    orphan_browser_content = """#!/usr/bin/env python3
'''
NOIZYGENIE ORPHAN BROWSER
Browse and manage orphaned libraries in NI_2026/_ORPHANS
'''

import os
import shutil
from pathlib import Path

def browse_orphans():
    orphans_path = Path("/Volumes/6TB/_NI_2026/_ORPHANS")
    
    if not orphans_path.exists():
        print("❌ ORPHANS folder not found!")
        return
    
    orphans = list(orphans_path.iterdir())
    
    if not orphans:
        print("🎉 No orphans found! All libraries have homes!")
        return
    
    print(f"\\n🏠 ORPHAN SANCTUARY: {len(orphans)} homeless items")
    print("=" * 60)
    
    for i, orphan in enumerate(orphans, 1):
        if orphan.is_dir():
            try:
                size = sum(f.stat().st_size for f in orphan.rglob('*') if f.is_file())
                size_mb = size / (1024 * 1024)
                print(f"{i:2d}. 📂 {orphan.name} ({size_mb:.1f} MB)")
            except:
                print(f"{i:2d}. 📂 {orphan.name}")
        else:
            try:
                size_mb = orphan.stat().st_size / (1024 * 1024)
                print(f"{i:2d}. 📄 {orphan.name} ({size_mb:.1f} MB)")
            except:
                print(f"{i:2d}. 📄 {orphan.name}")
    
    return orphans

def relocate_orphan(orphan_path, destination_base):
    '''Relocate an orphan to a proper home'''
    try:
        dest_path = destination_base / orphan_path.name
        counter = 1
        while dest_path.exists():
            stem = dest_path.stem if dest_path.suffix else dest_path.name
            suffix = dest_path.suffix
            dest_path = dest_path.parent / f"{stem}_RELOCATED_{counter}{suffix}"
            counter += 1
        
        shutil.move(str(orphan_path), str(dest_path))
        print(f"✅ Relocated: {orphan_path.name} → {dest_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to relocate {orphan_path.name}: {e}")
        return False

def main():
    while True:
        orphans = browse_orphans()
        
        if not orphans:
            break
        
        print("\\nOptions:")
        print("1. Relocate an orphan")
        print("2. Show orphan details")
        print("3. Refresh list")
        print("q. Quit")
        
        choice = input("\\nChoose an option: ").strip()
        
        if choice.lower() == 'q':
            break
        elif choice == '1':
            try:
                idx = int(input("Enter orphan number to relocate: ")) - 1
                if 0 <= idx < len(orphans):
                    orphan = orphans[idx]
                    
                    # Show relocation options
                    destinations = {
                        "1": Path("/Volumes/6TB/_NI_2026/LIBRARIES/Native Instruments/COMPLETE/01_ORCHESTRAL_PREMIUM/strings"),
                        "2": Path("/Volumes/6TB/_NI_2026/LIBRARIES/Native Instruments/COMPLETE/02_ETHNIC_WORLD/asian"),
                        "3": Path("/Volumes/6TB/_NI_2026/LIBRARIES/Native Instruments/COMPLETE/05_ELECTRONIC_SYNTH/experimental"),
                        "4": Path("/Volumes/6TB/_NI_2026/LIBRARIES/Native Instruments/COMPLETE/06_DRUMS_PERCUSSION/world_percussion"),
                        "5": Path("/Volumes/6TB/_NI_2026/LIBRARIES/Native Instruments/COMPLETE/99_MISCELLANEOUS")
                    }
                    
                    print("\\nRelocation destinations:")
                    for key, path in destinations.items():
                        print(f"{key}. {path.parent.name}/{path.name}")
                    
                    dest_choice = input("Choose destination: ").strip()
                    if dest_choice in destinations:
                        dest_path = destinations[dest_choice]
                        dest_path.mkdir(parents=True, exist_ok=True)
                        relocate_orphan(orphan, dest_path)
                else:
                    print("❌ Invalid orphan number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == '2':
            try:
                idx = int(input("Enter orphan number for details: ")) - 1
                if 0 <= idx < len(orphans):
                    orphan = orphans[idx]
                    print(f"\\n📋 Details for: {orphan.name}")
                    print(f"   📁 Path: {orphan}")
                    print(f"   📂 Type: {'Directory' if orphan.is_dir() else 'File'}")
                    if orphan.is_dir():
                        try:
                            files = list(orphan.rglob('*'))
                            print(f"   📄 Contains: {len(files)} items")
                        except:
                            print("   📄 Contents: Unable to scan")
                else:
                    print("❌ Invalid orphan number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == '3':
            continue
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
"""
    
    orphan_browser_path = KONTAKT_LAB / "orphan_browser.py"
    orphan_browser_path.write_text(orphan_browser_content)
    os.chmod(orphan_browser_path, 0o755)
    print(f"🏠 Created orphan browser: {orphan_browser_path}")

def main():
    """Execute the ultimate deep organization with orphan sanctuary"""
    print("🧙‍♂️ NOIZYGENIE DEEP ORGANIZATION + CLEANUP + ORPHAN SANCTUARY")
    print("🔮 ULTIMATE KONTAKT_LAB REORGANIZATION + EMPTY FOLDER ELIMINATION")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    # Execute deep organization steps
    analysis = analyze_kontakt_lab_structure()
    create_deep_organization_structure()
    
    # Enhanced organization with orphan handling
    organized_count, collision_count, orphan_count = organize_kontakt_lab_items()
    
    # Delete empty folders across all volumes
    global_cleanup = delete_empty_folders_all_volumes()
    
    create_deep_navigation_tools()
    create_orphan_browser()
    
    # Final report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ NOIZYGENIE ULTIMATE ORGANIZATION COMPLETE!")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"📊 Items Analyzed: {analysis['total_items']}")
    print(f"✅ Items Organized: {organized_count}")
    print(f"⚠️  Name Collisions: {collision_count}")
    print(f"🏠 Orphans Relocated: {orphan_count}")
    print(f"🗑️  Empty Folders Deleted: {global_cleanup}")
    print(f"📁 Categories Created: {len(DEEP_PROJECT_STRUCTURE)}")
    print(f"🗂️  Organized Structure: {ORGANIZED_ROOT}")
    print(f"🏠 Orphan Sanctuary: /Volumes/6TB/_NI_2026/_ORPHANS")
    print(f"💾 Analysis Reports: {ANALYSIS_ROOT}")
    print("\n🌟 YOUR KONTAKT_LAB IS NOW PERFECTLY ORGANIZED!")
    print("🔍 Use deep_browser.py to explore organized libraries")
    print("🏠 Use orphan_browser.py to manage homeless items")
    print("📊 Use deep_statistics.py for detailed statistics")
    print("🏆 NOIZYGENIE ULTIMATE PROTOCOL WITH ORPHAN SANCTUARY ACHIEVED!")

if __name__ == "__main__":
    main()