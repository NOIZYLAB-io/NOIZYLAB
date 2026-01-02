#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/noizygenie_deep_organizer.py
# NOIZYGENIE: ULTIMATE DEEP ORGANIZATION PROTOCOL

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

print("🧙‍♂️ NOIZYGENIE: DEEP ORGANIZATION PROTOCOL")
print("🔮 ANALYZING MASSIVE KONTAKT_LAB STRUCTURE")
print("⚡" * 80)

# Enhanced project structure with deep categorization
DEEP_PROJECT_STRUCTURE = {
    "01_ORCHESTRAL_PREMIUM": {
        "description": "Premium orchestral libraries and string sections",
        "patterns": ["ORCHESTRAL", "ACOUSTIC", "Celli", "Violin", "String", "Aleatoric"],
        "subfolders": ["strings", "brass", "woodwinds", "full_orchestra", "solo_instruments"]
    },
    "02_ETHNIC_WORLD": {
        "description": "World ethnic instruments and cultural libraries",
        "patterns": ["WORLD_ETHNIC", "ERHU", "CHINA_SETS", "MID_EAST", "BANSURI", "DIGERIDOO", 
                    "CEYLON", "EGYPTIAN", "ALPINE", "GAOHU", "CUMBUS", "TANBUR"],
        "subfolders": ["asian", "middle_eastern", "european", "african", "american"]
    },
    "03_WIND_INSTRUMENTS": {
        "description": "Wind instruments - flutes, whistles, brass",
        "patterns": ["BAWU", "HOTCHIKU", "HULUSI", "KENA", "SHAKUHACHI", "SHAWN", "SHENAI", 
                    "SHENG", "WHISTLE", "CIARAMELLA", "DOUCAINE", "MANCOSEDDA", "SUSATO"],
        "subfolders": ["flutes", "whistles", "reed", "brass_wind", "ethnic_wind"]
    },
    "04_STRING_INSTRUMENTS": {
        "description": "Plucked and bowed string instruments",
        "patterns": ["RENAISSANCE_LUTE", "SAZ", "TIMPLE", "Lutes", "Reeds", "PLECTRUM"],
        "subfolders": ["guitars", "lutes", "exotic_strings", "bowed_strings"]
    },
    "05_ELECTRONIC_SYNTH": {
        "description": "Electronic synthesizers and modern sounds",
        "patterns": ["ELECTRONIC", "SYNTHESIZERS", "Industrial", "Evolve", "FRISKY"],
        "subfolders": ["analog", "digital", "hybrid", "experimental", "industrial"]
    },
    "06_DRUMS_PERCUSSION": {
        "description": "Drums, percussion, and rhythmic elements",
        "patterns": ["DRUMS_PERCUSSION", "CLAPS", "BELLTREE", "CASTANETS", "CUICA", 
                    "TAMBORCITO", "GLASSES"],
        "subfolders": ["acoustic_drums", "electronic_drums", "world_percussion", "fx_percussion"]
    },
    "07_KEYBOARDS_PIANOS": {
        "description": "Keyboard instruments and pianos",
        "patterns": ["Scarbee", "HARMONIUM", "Piano", "Keyboard"],
        "subfolders": ["acoustic_pianos", "electric_pianos", "organs", "vintage_keys"]
    },
    "08_VOCALS_HUMAN": {
        "description": "Vocal libraries and human sounds",
        "patterns": ["VOCALS", "HUMAN_WHISTLING", "Spitfire"],
        "subfolders": ["choirs", "solo_vocals", "vocal_fx", "human_sounds"]
    },
    "09_LOOPS_CONSTRUCTION": {
        "description": "Loops, construction kits, and grooves",
        "patterns": ["LOOPS_GROOVES", "CONSTRUCTION_KITS", "MULTIS", "Discolicks", 
                    "Runs_", "SawTooth", "Wavy", "Slow_"],
        "subfolders": ["tempo_120", "tempo_140", "tempo_100", "arpeggios", "construction"]
    },
    "10_SOUNDSCAPES_FX": {
        "description": "Soundscapes, atmospheres, and sound effects",
        "patterns": ["SOUNDSCAPES_FX", "Quirky", "Cinescapes", "RS_Cinescapes"],
        "subfolders": ["atmospheres", "textures", "transitions", "impacts", "ambient"]
    },
    "11_FACTORY_LIBRARIES": {
        "description": "Official Native Instruments factory content",
        "patterns": ["Kontakt_Factory", "Native_Instruments", "KONTAKT_LAB_2026", "NI2026"],
        "subfolders": ["factory_content", "demos", "presets"]
    },
    "12_SYSTEM_UTILITIES": {
        "description": "System files, utilities, and maintenance",
        "patterns": ["_FIX", "_NKI", "_Staccato", "_TWEAKABLE", "BACKUP", "Data", 
                    "REPORTS", "PY_Scripts", "TEMP", "SAMPLE_ARCHIVES", "ORGANIZED", 
                    "Auxiliary", "Lite_Patches", "Excerpts", "PROJECT_ORGANIZER"],
        "subfolders": ["scripts", "backups", "temp_files", "utilities", "patches"]
    },
    "13_DOCUMENTATION": {
        "description": "Documentation, logs, and reports",
        "patterns": [".txt", ".html", ".json", "LOG", "MASTER", "REPAIR", "MIGRATION"],
        "subfolders": ["logs", "reports", "manuals", "migration_data"]
    }
}

# Base paths
KONTAKT_LAB = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
ORGANIZED_ROOT = KONTAKT_LAB / "DEEP_ORGANIZED"
BACKUP_ROOT = KONTAKT_LAB / "DEEP_BACKUP"
ANALYSIS_ROOT = KONTAKT_LAB / "DEEP_ANALYSIS"

def analyze_kontakt_lab_structure():
    """Deep analysis of the KONTAKT_LAB structure"""
    print("🔍 DEEP ANALYZING KONTAKT_LAB STRUCTURE...")
    
    analysis = {
        "total_items": 0,
        "directories": 0,
        "files": 0,
        "categories": defaultdict(list),
        "uncategorized": [],
        "file_types": Counter(),
        "size_distribution": {},
        "timestamp": datetime.now().isoformat()
    }
    
    for item in KONTAKT_LAB.iterdir():
        if item.name in ["DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"]:
            continue
            
        analysis["total_items"] += 1
        
        if item.is_dir():
            analysis["directories"] += 1
        else:
            analysis["files"] += 1
            analysis["file_types"][item.suffix.lower()] += 1
        
        # Categorize items
        categorized = False
        for category, config in DEEP_PROJECT_STRUCTURE.items():
            patterns = config["patterns"]
            for pattern in patterns:
                if (pattern in item.name or 
                    item.name.startswith(pattern) or 
                    any(p in item.name for p in pattern.split("_"))):
                    analysis["categories"][category].append(item.name)
                    categorized = True
                    break
            if categorized:
                break
        
        if not categorized:
            analysis["uncategorized"].append(item.name)
    
    # Save analysis report
    ANALYSIS_ROOT.mkdir(parents=True, exist_ok=True)
    analysis_file = ANALYSIS_ROOT / f"deep_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(analysis_file, 'w') as f:
        json.dump(analysis, f, indent=2, default=str)
    
    print(f"📊 ANALYSIS COMPLETE:")
    print(f"   📁 Total Items: {analysis['total_items']}")
    print(f"   📂 Directories: {analysis['directories']}")
    print(f"   📄 Files: {analysis['files']}")
    print(f"   ✅ Categorized: {sum(len(items) for items in analysis['categories'].values())}")
    print(f"   ❓ Uncategorized: {len(analysis['uncategorized'])}")
    print(f"   📋 Analysis saved: {analysis_file}")
    
    return analysis

def create_deep_organization_structure():
    """Create the deep organization structure"""
    print("\n🏗️ CREATING DEEP ORGANIZATION STRUCTURE...")
    
    # Create backup first
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = BACKUP_ROOT / f"backup_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Create main organized structure
    ORGANIZED_ROOT.mkdir(parents=True, exist_ok=True)
    
    for category, config in DEEP_PROJECT_STRUCTURE.items():
        category_path = ORGANIZED_ROOT / category
        category_path.mkdir(exist_ok=True)
        
        # Create subfolders
        for subfolder in config["subfolders"]:
            (category_path / subfolder).mkdir(exist_ok=True)
        
        # Create README for each category
        readme_content = f"""# {category}

{config['description']}

## Patterns Matched
{chr(10).join(f"- {pattern}" for pattern in config['patterns'])}

## Structure
{chr(10).join(f"- {subfolder}/" for subfolder in config['subfolders'])}

## Auto-organized by NOIZYGENIE Deep Organizer
Timestamp: {datetime.now().isoformat()}
"""
        
        (category_path / "README.md").write_text(readme_content)
        print(f"📁 Created category: {category}")
    
    # Create miscellaneous folder
    misc_path = ORGANIZED_ROOT / "99_MISCELLANEOUS"
    misc_path.mkdir(exist_ok=True)
    print("📦 Created miscellaneous category")

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

def create_deep_navigation_tools():
    """Create navigation and utility tools for the organized structure"""
    print("\n🛠️ CREATING DEEP NAVIGATION TOOLS...")
    
    # Create directory browser
    browser_content = """#!/usr/bin/env python3
'''
NOIZYGENIE DEEP BROWSER
Browse the organized KONTAKT_LAB structure
'''

import os
from pathlib import Path

def browse_category(category_path):
    '''Browse a specific category'''
    print(f"\\n📁 Browsing: {category_path.name}")
    print("=" * 50)
    
    items = list(category_path.iterdir())
    for i, item in enumerate(items, 1):
        if item.is_dir():
            item_count = len(list(item.iterdir()))
            print(f"{i:2d}. 📂 {item.name} ({item_count} items)")
        else:
            print(f"{i:2d}. 📄 {item.name}")
    
    return items

def main():
    organized_root = Path(__file__).parent / "DEEP_ORGANIZED"
    
    if not organized_root.exists():
        print("❌ Organized structure not found!")
        return
    
    categories = [d for d in organized_root.iterdir() if d.is_dir()]
    
    while True:
        print("\\n🧙‍♂️ NOIZYGENIE DEEP BROWSER")
        print("=" * 40)
        
        for i, cat in enumerate(categories, 1):
            item_count = sum(len(list(sub.iterdir())) for sub in cat.iterdir() if sub.is_dir())
            print(f"{i:2d}. {cat.name} ({item_count} items)")
        
        print("\\nq. Quit")
        
        choice = input("\\nSelect category to browse: ").strip()
        
        if choice.lower() == 'q':
            break
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                items = browse_category(categories[idx])
                
                sub_choice = input("\\nEnter number to explore subfolder (or Enter to continue): ").strip()
                if sub_choice.isdigit():
                    sub_idx = int(sub_choice) - 1
                    if 0 <= sub_idx < len(items) and items[sub_idx].is_dir():
                        browse_category(items[sub_idx])
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a number")

if __name__ == "__main__":
    main()
"""
    
    browser_path = ORGANIZED_ROOT.parent / "deep_browser.py"
    browser_path.write_text(browser_content)
    os.chmod(browser_path, 0o755)
    
    # Create statistics generator
    stats_content = """#!/usr/bin/env python3
'''
NOIZYGENIE DEEP STATISTICS
Generate comprehensive statistics for organized libraries
'''

import json
from pathlib import Path
from collections import Counter

def generate_stats():
    organized_root = Path(__file__).parent / "DEEP_ORGANIZED"
    
    if not organized_root.exists():
        print("❌ Organized structure not found!")
        return
    
    stats = {
        "categories": {},
        "total_items": 0,
        "file_types": Counter(),
        "size_distribution": {}
    }
    
    for category in organized_root.iterdir():
        if not category.is_dir():
            continue
        
        cat_stats = {
            "subfolders": {},
            "total_items": 0
        }
        
        for subfolder in category.iterdir():
            if subfolder.name == "README.md":
                continue
            
            if subfolder.is_dir():
                items = list(subfolder.iterdir())
                cat_stats["subfolders"][subfolder.name] = len(items)
                cat_stats["total_items"] += len(items)
                stats["total_items"] += len(items)
        
        stats["categories"][category.name] = cat_stats
    
    # Print statistics
    print("🧙‍♂️ NOIZYGENIE DEEP STATISTICS")
    print("=" * 50)
    print(f"📊 Total Items Organized: {stats['total_items']}")
    print(f"📁 Categories: {len(stats['categories'])}")
    print()
    
    for cat_name, cat_data in stats["categories"].items():
        print(f"📂 {cat_name}: {cat_data['total_items']} items")
        for subfolder, count in cat_data["subfolders"].items():
            print(f"   └── {subfolder}: {count}")
    
    return stats

if __name__ == "__main__":
    generate_stats()
"""
    
    stats_path = ORGANIZED_ROOT.parent / "deep_statistics.py"
    stats_path.write_text(stats_content)
    os.chmod(stats_path, 0o755)
    
    print(f"🛠️ Created navigation tools:")
    print(f"   🔍 Browser: {browser_path}")
    print(f"   📊 Statistics: {stats_path}")

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