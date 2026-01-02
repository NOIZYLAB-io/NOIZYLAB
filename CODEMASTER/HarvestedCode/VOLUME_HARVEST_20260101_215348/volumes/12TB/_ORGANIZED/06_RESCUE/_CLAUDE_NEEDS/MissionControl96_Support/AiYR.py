#!/usr/bin/env python3
"""
NOIZYGENIE PROJECT ORGANIZER
Reorganizes existing Python projects into a structured workspace
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

# Project organization structure based on your actual scripts
PROJECT_STRUCTURE = {
    "01_KONTAKT_MANAGEMENT": {
        "description": "Core Kontakt library management and status checking",
        "scripts": [
            "check_kontakt_lab_status.py",
            "ni_deep_scan_rebuild.py"
        ],
        "folders": ["data", "logs", "reports", "config", "status_reports"]
    },
    "02_LIBRARY_MIGRATION": {
        "description": "Library migration and purity checking tools",
        "scripts": [
            "ni_purity_migrate.py",
            "ni_name_normalize.py"
        ],
        "folders": ["migrations", "purity_reports", "normalized", "safety"]
    },
    "03_REPAIR_RECOVERY": {
        "description": "Advanced repair and recovery systems",
        "scripts": [
            "hog_targeted_repair.py",
            "hog_parallel_runner.py"
        ],
        "folders": ["repair_logs", "recovery_data", "divine_reports", "backups"]
    },
    "04_FILE_MAPPING": {
        "description": "File location mapping and rehoming systems",
        "scripts": [
            "find_original_homes.py",
            "rehoming_from_map.py"
        ],
        "folders": ["maps", "rehoming_logs", "relocations", "safety"]
    },
    "05_PLUGIN_MANAGEMENT": {
        "description": "Plugin inventory and vendor detection",
        "scripts": [
            "plugin_vendor_scan.py"
        ],
        "folders": ["inventories", "vendor_reports", "plugin_data"]
    },
    "06_UTILITIES": {
        "description": "Shared utilities and helper functions",
        "scripts": [],
        "folders": ["common", "helpers", "templates", "shared_config"]
    }
}

# Base paths
CURRENT_REPORTS = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/REPORTS")
CURRENT_PROJECT_ORGANIZER = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER")
NEW_PROJECT_ROOT = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/ORGANIZED_PROJECTS")
BACKUP_ROOT = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_BACKUP")

def create_backup():
    """Create timestamped backup of current state"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = BACKUP_ROOT / f"backup_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Backup REPORTS folder
    if CURRENT_REPORTS.exists():
        shutil.copytree(CURRENT_REPORTS, backup_dir / "REPORTS")
        print(f"✅ Backed up REPORTS to: {backup_dir / 'REPORTS'}")
    
    # Backup PROJECT_ORGANIZER folder
    if CURRENT_PROJECT_ORGANIZER.exists():
        shutil.copytree(CURRENT_PROJECT_ORGANIZER, backup_dir / "PROJECT_ORGANIZER")
        print(f"✅ Backed up PROJECT_ORGANIZER to: {backup_dir / 'PROJECT_ORGANIZER'}")
    
    return backup_dir

def create_project_structure():
    """Create the organized project structure"""
    print("🏗️ Creating organized project structure...")
    
    for project_name, config in PROJECT_STRUCTURE.items():
        project_path = NEW_PROJECT_ROOT / project_name
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Create subfolders
        for folder in config["folders"]:
            (project_path / folder).mkdir(exist_ok=True)
        
        # Create README for each project
        readme_content = f"""# {project_name}

{config['description']}

## Scripts
{chr(10).join(f"- {script}" for script in config['scripts']) if config['scripts'] else "- No specific scripts assigned yet"}

## Structure
{chr(10).join(f"- `{folder}/` - {get_folder_description(folder)}" for folder in config['folders'])}

## Usage
Run scripts from this directory to maintain proper paths and dependencies.

## Configuration
Use the shared configuration system in `../06_UTILITIES/shared_config/` for common settings.
"""
        
        (project_path / "README.md").write_text(readme_content)
        print(f"📁 Created project: {project_name}")

def get_folder_description(folder_name):
    """Get description for common folder types"""
    descriptions = {
        "data": "Input data and working files",
        "logs": "Execution logs and debug information", 
        "reports": "Generated reports and analysis results",
        "config": "Configuration files and settings",
        "migrations": "Migration reports and tracking",
        "safety": "Safety backups and collision handling",
        "repair_logs": "Repair operation logs",
        "recovery_data": "Recovered file information",
        "maps": "File location mapping data",
        "inventories": "Plugin and library inventories",
        "common": "Shared utility functions",
        "helpers": "Helper scripts and modules",
        "templates": "Template files and examples"
    }
    return descriptions.get(folder_name, "Project-specific files")

def move_scripts_to_projects():
    """Move existing scripts to appropriate project folders"""
    print("\n📦 Moving scripts to organized projects...")
    
    # Build script location mapping
    script_locations = {}
    for project_name, config in PROJECT_STRUCTURE.items():
        for script in config["scripts"]:
            script_locations[script] = project_name
    
    moved_count = 0
    
    # Search for scripts in both REPORTS and PROJECT_ORGANIZER
    search_paths = []
    if CURRENT_REPORTS.exists():
        search_paths.extend(CURRENT_REPORTS.glob("*.py"))
    if CURRENT_PROJECT_ORGANIZER.exists():
        search_paths.extend(CURRENT_PROJECT_ORGANIZER.glob("*.py"))
    
    for script_file in search_paths:
        script_name = script_file.name
        
        if script_name in script_locations:
            target_project = script_locations[script_name]
            target_path = NEW_PROJECT_ROOT / target_project / script_name
            
            try:
                shutil.copy2(script_file, target_path)
                print(f"✅ Moved {script_name} → {target_project}")
                moved_count += 1
            except Exception as e:
                print(f"❌ Failed to move {script_name}: {e}")
        else:
            # Move unassigned scripts to utilities
            target_path = NEW_PROJECT_ROOT / "06_UTILITIES" / script_name
            try:
                shutil.copy2(script_file, target_path)
                print(f"📦 Moved {script_name} → 06_UTILITIES (unassigned)")
                moved_count += 1
            except Exception as e:
                print(f"❌ Failed to move {script_name}: {e}")
    
    print(f"\n📊 Moved {moved_count} scripts to organized projects")

def create_master_config():
    """Create master configuration file"""
    config_content = f"""#!/usr/bin/env python3
'''
NOIZYGENIE MASTER CONFIGURATION
Centralized configuration for all projects
'''

from pathlib import Path
import json

# Base paths
PROJECT_ROOT = Path(__file__).parent
KONTAKT_LAB = PROJECT_ROOT.parent
REPORTS_DIR = KONTAKT_LAB / "REPORTS"
BACKUP_DIR = KONTAKT_LAB / "PROJECT_BACKUP"
ORGANIZED_PROJECTS = KONTAKT_LAB / "ORGANIZED_PROJECTS"

# Volume paths (based on your actual setup)
VOLUMES_6TB = Path("/Volumes/6TB")
NATIVE_INSTRUMENTS_SOURCE = VOLUMES_6TB / "Native Instruments"
NATIVE_INSTRUMENTS_2026 = VOLUMES_6TB / "Native_Instruments_2026"
NI_2026_ROOT = VOLUMES_6TB / "_NI_2026"
LIBRARIES_DEST = NI_2026_ROOT / "LIBRARIES"
SAFETY_ROOT = NI_2026_ROOT / "SAFETY"
ORPHANS_PATH = NI_2026_ROOT / "_ORPHANS"

# Project structure
PROJECTS = {{
    {chr(10).join(f'    "{name}": ORGANIZED_PROJECTS / "{name}",' for name in PROJECT_STRUCTURE.keys())}
}}

# Common file extensions
INSTRUMENT_EXT = {{".nki", ".nkm"}}
AUDIO_EXT = {{".wav", ".aif", ".aiff", ".ncw"}}
MONOLITH_EXT = {{".nkx", ".nks", ".nkb", ".nksn", ".nkc", ".nkr"}}
ALLOWED_AUDIO_EXT = AUDIO_EXT | MONOLITH_EXT

# Vendor detection patterns (from your plugin scanner)
VENDOR_HINTS = {{
    "native instruments": "Native Instruments",
    "kontakt": "Native Instruments", 
    "eastwest": "EastWest",
    "spitfire": "Spitfire Audio",
    "project sam": "ProjectSAM",
    "sonokinetic": "Sonokinetic",
    "8dio": "8Dio",
    "cinesamples": "Cinesamples",
    "output": "Output",
    "heavyocity": "Heavyocity",
}}

# Enhanced vendor detection patterns
ENHANCED_VENDOR_HINTS = {
    # Native Instruments
    "native instruments": "Native Instruments",
    "kontakt": "Native Instruments", 
    "massive": "Native Instruments",
    "komplete": "Native Instruments",
    "reaktor": "Native Instruments",
    
    # Best Service - EthnoWorld Series
    "best service": "Best Service",
    "ethnoworld": "Best Service EthnoWorld",
    "ethno world": "Best Service EthnoWorld", 
    "eduardtaube": "Best Service EthnoWorld",
    "best_service": "Best Service",
    "ethnoworld5": "Best Service EthnoWorld 5",
    "ethnoworld6": "Best Service EthnoWorld 6",
    "ethno_world": "Best Service EthnoWorld",
    "world_ethnic": "Best Service EthnoWorld",
    
    # Zero-G Libraries (TONS!)
    "zero-g": "Zero-G",
    "zerog": "Zero-G",
    "zero_g": "Zero-G",
    "datafile": "Zero-G",
    "ambient": "Zero-G",
    "ethnic": "Zero-G",
    "shamanic": "Zero-G",
    "vocal": "Zero-G",
    "world": "Zero-G",
    "temple": "Zero-G",
    "sacred": "Zero-G",
    
    # Other Major Vendors
    "eastwest": "EastWest",
    "spitfire": "Spitfire Audio",
    "project sam": "ProjectSAM",
    "projectsam": "ProjectSAM",
    "sonokinetic": "Sonokinetic",
    "8dio": "8Dio",
    "cinesamples": "Cinesamples",
    "output": "Output",
    "heavyocity": "Heavyocity",
    "audiobro": "AudioBro",
    "symphonic": "ProjectSAM",
}

def create_vendor_detection_script():
    """Create advanced vendor detection script."""
    vendor_detector_content = """#!/usr/bin/env python3
'''
NOIZYGENIE VENDOR DETECTIVE
Advanced vendor detection for Best Service EthnoWorld & Zero-G libraries
'''

import os
from pathlib import Path
from collections import defaultdict
import json

# Enhanced vendor patterns
VENDOR_PATTERNS = {
    "Best Service EthnoWorld": [
        "ethnoworld", "ethno world", "eduardtaube", "best service", 
        "ethnic", "world instruments", "traditional", "folk"
    ],
    "Zero-G": [
        "zero-g", "zerog", "zero_g", "datafile", "ambient", 
        "shamanic", "vocal textures", "world vocals", "sacred",
        "temple", "ethnic vocals", "ceremonial"
    ],
    "Native Instruments": [
        "native instruments", "kontakt", "komplete", "massive", 
        "reaktor", "ni_", "absynth"
    ],
    "EastWest": [
        "eastwest", "east west", "quantum leap", "play engine",
        "hollywood", "symphonic"
    ],
    "Spitfire Audio": [
        "spitfire", "british", "london", "abbey road", "bbc"
    ],
    "ProjectSAM": [
        "project sam", "projectsam", "symphobia", "orchestral essentials"
    ]
}

def detect_vendor(item_name: str, item_path: Path) -> str:
    '''Detect vendor from item name and path'''
    item_lower = item_name.lower()
    path_lower = str(item_path).lower()
    
    # Check for vendor patterns
    for vendor, patterns in VENDOR_PATTERNS.items():
        for pattern in patterns:
            if pattern in item_lower or pattern in path_lower:
                return vendor
    
    # Special detection for voice/ethnic samples
    voice_indicators = ["vocal", "voice", "choir", "whistle", "chant", "breath"]
    ethnic_indicators = ["bawu", "erhu", "hulusi", "shamisen", "tabla", "sitar"]
    
    if any(indicator in item_lower for indicator in voice_indicators + ethnic_indicators):
        # Likely Best Service EthnoWorld or Zero-G
        if any(ethnic in item_lower for ethnic in ["ethno", "world", "traditional"]):
            return "Best Service EthnoWorld"
        elif any(zero in item_lower for zero in ["ambient", "sacred", "shamanic"]):
            return "Zero-G"
    
    return "Unknown"

def scan_for_vendors(root_path: Path):
    '''Scan directory for vendor detection'''
    print(f"🔍 Scanning for vendors in: {root_path}")
    
    vendor_counts = defaultdict(list)
    total_items = 0
    
    for item in root_path.iterdir():
        if item.name.startswith('.'):
            continue
            
        total_items += 1
        vendor = detect_vendor(item.name, item)
        vendor_counts[vendor].append(item.name)
        
        if vendor != "Unknown":
            print(f"   📦 {vendor}: {item.name}")
    
    return vendor_counts, total_items

def generate_vendor_report(vendor_counts: dict, total_items: int):
    '''Generate detailed vendor report'''
    print("\\n🎯 VENDOR DETECTION REPORT")
    print("=" * 60)
    
    for vendor, items in vendor_counts.items():
        percentage = (len(items) / total_items) * 100 if total_items > 0 else 0
        print(f"📊 {vendor}: {len(items)} items ({percentage:.1f}%)")
        
        # Show first few items as examples
        for item in items[:3]:
            print(f"    └── {item}")
        if len(items) > 3:
            print(f"    └── ... and {len(items) - 3} more")
        print()
    
    return vendor_counts

def suggest_organization(vendor_counts: dict):
    '''Suggest organization structure based on detected vendors'''
    print("🎯 SUGGESTED ORGANIZATION:")
    print("=" * 40)
    
    if "Best Service EthnoWorld" in vendor_counts:
        count = len(vendor_counts["Best Service EthnoWorld"])
        print(f"📁 Create: /Volumes/6TB/_NI_2026/LIBRARIES/Best_Service/EthnoWorld/ ({count} items)")
    
    if "Zero-G" in vendor_counts:
        count = len(vendor_counts["Zero-G"])
        print(f"📁 Create: /Volumes/6TB/_NI_2026/LIBRARIES/Zero-G/Collections/ ({count} items)")
    
    if "Native Instruments" in vendor_counts:
        count = len(vendor_counts["Native Instruments"])
        print(f"📁 Organize: /Volumes/6TB/_NI_2026/LIBRARIES/Native_Instruments/ ({count} items)")

def main():
    kontakt_lab = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
    
    if not kontakt_lab.exists():
        print("❌ KONTAKT_LAB not found!")
        return
    
    print("🧙‍♂️ NOIZYGENIE VENDOR DETECTIVE")
    print("🔎 Detecting Best Service EthnoWorld & Zero-G Libraries")
    print("=" * 60)
    
    vendor_counts, total_items = scan_for_vendors(kontakt_lab)
    
    if total_items == 0:
        print("📭 No items found to analyze")
        return
    
    report = generate_vendor_report(vendor_counts, total_items)
    suggest_organization(vendor_counts)
    
    # Save report
    report_file = kontakt_lab / "vendor_detection_report.json"
    with open(report_file, 'w') as f:
        json.dump({
            "timestamp": str(datetime.now()),
            "total_items": total_items,
            "vendor_counts": {k: len(v) for k, v in vendor_counts.items()},
            "detailed_items": {k: v for k, v in vendor_counts.items()}
        }, f, indent=2)
    
    print(f"\\n💾 Report saved: {report_file}")

if __name__ == "__main__":
    from datetime import datetime
    main()
"""
    
    vendor_script_path = NEW_PROJECT_ROOT / "05_PLUGIN_MANAGEMENT" / "vendor_detective.py"
    vendor_script_path.parent.mkdir(parents=True, exist_ok=True)
    vendor_script_path.write_text(vendor_detector_content)
    os.chmod(vendor_script_path, 0o755)
    print(f"🔍 Created vendor detective: {vendor_script_path}")

def create_ethnoworld_organizer():
    """Create specialized EthnoWorld & Zero-G organizer."""
    ethno_organizer_content = """#!/usr/bin/env python3
'''
NOIZYGENIE ETHNOWORLD & ZERO-G ORGANIZER
Specialized organizer for Best Service EthnoWorld 5/6 and Zero-G libraries
'''

import shutil
from pathlib import Path
from datetime import datetime

# EthnoWorld instrument categories
ETHNOWORLD_CATEGORIES = {
    "wind_instruments": [
        "bawu", "hulusi", "hotchiku", "shakuhachi", "kena", "whistle",
        "flute", "pan", "ocarina", "recorder", "didgeridoo"
    ],
    "string_instruments": [
        "erhu", "gaohu", "saz", "lute", "oud", "banjo", "mandolin",
        "guitar", "harp", "zither", "dulcimer"
    ],
    "percussion": [
        "tabla", "djembe", "conga", "bongo", "frame_drum", "gong",
        "bell", "chimes", "shaker", "rattle"
    ],
    "vocals": [
        "vocal", "voice", "choir", "chant", "whistle", "throat",
        "overtone", "mongolian", "tibetan", "indian"
    ],
    "keyboards": [
        "harmonium", "accordion", "concertina", "melodica", "kalimba"
    ]
}

# Zero-G categories
ZEROG_CATEGORIES = {
    "ambient_textures": [
        "ambient", "texture", "pad", "atmosphere", "drone", "evolving"
    ],
    "ethnic_vocals": [
        "vocal", "voice", "ethnic", "ceremonial", "sacred", "shamanic"
    ],
    "world_percussion": [
        "percussion", "rhythm", "ethnic", "tribal", "ceremonial"
    ],
    "soundscapes": [
        "soundscape", "environment", "nature", "space", "field_recording"
    ]
}

def organize_ethnoworld_items(source_dir: Path, dest_base: Path):
    '''Organize EthnoWorld items by instrument type'''
    ethno_dest = dest_base / "Best_Service" / "EthnoWorld_5_6"
    ethno_dest.mkdir(parents=True, exist_ok=True)
    
    organized_count = 0
    
    for item in source_dir.iterdir():
        if not (item.is_dir() or item.name.endswith('.nki')):
            continue
        
        item_lower = item.name.lower()
        organized = False
        
        # Try to categorize EthnoWorld items
        for category, patterns in ETHNOWORLD_CATEGORIES.items():
            for pattern in patterns:
                if pattern in item_lower:
                    category_dir = ethno_dest / category
                    category_dir.mkdir(exist_ok=True)
                    
                    dest_path = category_dir / item.name
                    try:
                        if item.is_dir():
                            shutil.move(str(item), str(dest_path))
                        else:
                            shutil.copy2(item, dest_path)
                        
                        print(f"🎭 EthnoWorld: {item.name} → {category}")
                        organized_count += 1
                        organized = True
                        break
                    except Exception as e:
                        print(f"❌ Failed to organize {item.name}: {e}")
                
                if organized:
                    break
            
            if organized:
                break
        
        # If not categorized, put in general folder
        if not organized:
            general_dir = ethno_dest / "general_instruments"
            general_dir.mkdir(exist_ok=True)
            dest_path = general_dir / item.name
            
            try:
                if item.is_dir():
                    shutil.move(str(item), str(dest_path))
                else:
                    shutil.copy2(item, dest_path)
                print(f"📦 EthnoWorld General: {item.name}")
                organized_count += 1
            except Exception as e:
                print(f"❌ Failed to move {item.name}: {e}")
    
    return organized_count

def organize_zerog_items(source_dir: Path, dest_base: Path):
    '''Organize Zero-G items by type'''
    zerog_dest = dest_base / "Zero-G" / "Collections"
    zerog_dest.mkdir(parents=True, exist_ok=True)
    
    organized_count = 0
    
    for item in source_dir.iterdir():
        if not (item.is_dir() or item.name.endswith(('.nki', '.wav', '.aif'))):
            continue
        
        item_lower = item.name.lower()
        organized = False
        
        # Try to categorize Zero-G items
        for category, patterns in ZEROG_CATEGORIES.items():
            for pattern in patterns:
                if pattern in item_lower:
                    category_dir = zerog_dest / category
                    category_dir.mkdir(exist_ok=True)
                    
                    dest_path = category_dir / item.name
                    try:
                        if item.is_dir():
                            shutil.move(str(item), str(dest_path))
                        else:
                            shutil.copy2(item, dest_path)
                        
                        print(f"🌀 Zero-G: {item.name} → {category}")
                        organized_count += 1
                        organized = True
                        break
                    except Exception as e:
                        print(f"❌ Failed to organize {item.name}: {e}")
                
                if organized:
                    break
            
            if organized:
                break
        
        # If not categorized, put in general folder
        if not organized:
            general_dir = zerog_dest / "general_samples"
            general_dir.mkdir(exist_ok=True)
            dest_path = general_dir / item.name
            
            try:
                if item.is_dir():
                    shutil.move(str(item), str(dest_path))
                else:
                    shutil.copy2(item, dest_path)
                print(f"📦 Zero-G General: {item.name}")
                organized_count += 1
            except Exception as e:
                print(f"❌ Failed to move {item.name}: {e}")
    
    return organized_count

def main():
    print("🧙‍♂️ NOIZYGENIE ETHNOWORLD & ZERO-G ORGANIZER")
    print("🎭 Organizing Best Service EthnoWorld 5/6 & Zero-G Libraries")
    print("=" * 70)
    
    source_dir = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
    dest_base = Path("/Volumes/6TB/_NI_2026/LIBRARIES")
    
    if not source_dir.exists():
        print("❌ Source directory not found!")
        return
    
    dest_base.mkdir(parents=True, exist_ok=True)
    
    # Organize EthnoWorld items
    print("🎭 Organizing EthnoWorld items...")
    ethno_count = organize_ethnoworld_items(source_dir, dest_base)
    
    # Organize Zero-G items  
    print("\\n🌀 Organizing Zero-G items...")
    zerog_count = organize_zerog_items(source_dir, dest_base)
    
    print(f"\\n🎉 ORGANIZATION COMPLETE!")
    print(f"   🎭 EthnoWorld items organized: {ethno_count}")
    print(f"   🌀 Zero-G items organized: {zerog_count}")
    print(f"   📁 Destination: {dest_base}")

if __name__ == "__main__":
    main()
"""
    
    ethno_script_path = NEW_PROJECT_ROOT / "02_LIBRARY_MIGRATION" / "ethno_zerog_organizer.py"
    ethno_script_path.write_text(ethno_organizer_content)
    os.chmod(ethno_script_path, 0o755)
    print(f"🎭 Created EthnoWorld & Zero-G organizer: {ethno_script_path}")

# Add to main function
def main():
    """Main organization function with vendor detection."""
    print("🧙‍♂️ NOIZYGENIE PROJECT ORGANIZER")
    print("🔥" * 60)
    print("Organizing projects with Best Service EthnoWorld & Zero-G detection...")
    
    # Create directories
    NEW_PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Execute organization steps
    backup_dir = create_backup()
    create_project_structure()
    move_scripts_to_projects() 
    create_master_config()
    create_project_launcher()
    create_shared_utilities()
    
    # NEW: Create vendor-specific tools
    create_vendor_detection_script()
    create_ethnoworld_organizer()
    
    # Create summary report
    summary = {
        "organization_completed": datetime.now().isoformat(),
        "backup_location": str(backup_dir),
        "project_root": str(NEW_PROJECT_ROOT),
        "projects_created": len(PROJECT_STRUCTURE),
        "launcher": str(NEW_PROJECT_ROOT / "project_launcher.py"),
        "master_config": str(NEW_PROJECT_ROOT / "master_config.py"),
        "vendor_detective": str(NEW_PROJECT_ROOT / "05_PLUGIN_MANAGEMENT" / "vendor_detective.py"),
        "ethno_organizer": str(NEW_PROJECT_ROOT / "02_LIBRARY_MIGRATION" / "ethno_zerog_organizer.py")
    }
    
    summary_file = NEW_PROJECT_ROOT / "organization_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("\n" + "🎉" * 60)
    print("✅ PROJECT ORGANIZATION COMPLETE!")
    print("🎉" * 60)
    print(f"📁 Projects organized in: {NEW_PROJECT_ROOT}")
    print(f"🔧 Master config: {NEW_PROJECT_ROOT / 'master_config.py'}")
    print(f"🚀 Launcher: {NEW_PROJECT_ROOT / 'project_launcher.py'}")
    print(f"🔍 Vendor Detective: {NEW_PROJECT_ROOT / '05_PLUGIN_MANAGEMENT' / 'vendor_detective.py'}")
    print(f"🎭 EthnoWorld Organizer: {NEW_PROJECT_ROOT / '02_LIBRARY_MIGRATION' / 'ethno_zerog_organizer.py'}")
    print(f"💾 Backup: {backup_dir}")
    print(f"📋 Summary: {summary_file}")
    print("\n🌟 Use project_launcher.py to run any tool!")
    print("🎭 Use vendor_detective.py to detect EthnoWorld & Zero-G libraries!")
    print("🌀 Use ethno_zerog_organizer.py to organize them properly!")

if __name__ == "__main__":
    main()