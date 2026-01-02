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

def organize_kontakt_lab_items():
    """Organize all KONTAKT_LAB items into deep structure"""
    print("\n🔄 ORGANIZING KONTAKT_LAB ITEMS...")
    
    organized_count = 0
    collision_count = 0
    skip_dirs = {"DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"}
    
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
        
        # Move uncategorized items to miscellaneous
        if not organized and item.exists():
            misc_path = ORGANIZED_ROOT / "99_MISCELLANEOUS" / item_name
            
            counter = 1
            while misc_path.exists():
                stem = misc_path.stem if misc_path.suffix else misc_path.name
                suffix = misc_path.suffix
                misc_path = misc_path.parent / f"{stem}_COPY_{counter}{suffix}"
                counter += 1
            
            try:
                shutil.move(str(item), str(misc_path))
                organized_count += 1
                print(f"📦 {item_name} → MISCELLANEOUS")
            except Exception as e:
                print(f"❌ Failed to move {item_name}: {e}")
    
    return organized_count, collision_count

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

def main():
    """Execute the ultimate deep organization"""
    print("🧙‍♂️ NOIZYGENIE DEEP ORGANIZATION PROTOCOL")
    print("🔮 ULTIMATE KONTAKT_LAB REORGANIZATION")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    # Execute deep organization steps
    analysis = analyze_kontakt_lab_structure()
    create_deep_organization_structure()
    organized_count, collision_count = organize_kontakt_lab_items()
    create_deep_navigation_tools()
    
    # Final report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ NOIZYGENIE DEEP ORGANIZATION COMPLETE!")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"📊 Items Analyzed: {analysis['total_items']}")
    print(f"✅ Items Organized: {organized_count}")
    print(f"⚠️  Name Collisions: {collision_count}")
    print(f"📁 Categories Created: {len(DEEP_PROJECT_STRUCTURE)}")
    print(f"🗂️  Organized Structure: {ORGANIZED_ROOT}")
    print(f"💾 Analysis Reports: {ANALYSIS_ROOT}")
    print("\n🌟 YOUR KONTAKT_LAB IS NOW DEEPLY ORGANIZED!")
    print("🔍 Use deep_browser.py to explore your organized libraries")
    print("📊 Use deep_statistics.py for detailed statistics")
    print("🏆 NOIZYGENIE DEEP ORGANIZATION ACHIEVED!")

if __name__ == "__main__":
    main()