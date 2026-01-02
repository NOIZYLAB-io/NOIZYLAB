#!/usr/bin/env python3
"""
NOIZYGENIE PROJECT ORGANIZER
Reorganizes existing Python projects into a structured workspace
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# Project organization structure
PROJECT_STRUCTURE = {
    "KONTAKT_LAB_MANAGER": {
        "description": "Main Kontakt library management system",
        "scripts": [
            "ni_deep_scan_rebuild.py",
            "ni_purity_migrate.py", 
            "ni_name_normalize.py"
        ],
        "folders": ["data", "logs", "reports", "config"]
    },
    "LIBRARY_REPAIR_TOOLS": {
        "description": "Tools for repairing and recovering broken libraries",
        "scripts": [
            "hog_targeted_repair.py",
            "hog_parallel_runner.py"
        ],
        "folders": ["backup", "recovery", "analysis"]
    },
    "FILE_MAPPING_SYSTEM": {
        "description": "Systems for mapping and relocating files",
        "scripts": [
            "find_original_homes.py",
            "rehoming_from_map.py"
        ],
        "folders": ["maps", "relocations", "tracking"]
    },
    "PLUGIN_MANAGEMENT": {
        "description": "Plugin inventory and management tools",
        "scripts": [
            "plugin_vendor_scan.py"
        ],
        "folders": ["inventories", "vendors", "configs"]
    },
    "UTILITIES": {
        "description": "Common utilities and shared functions",
        "scripts": [],
        "folders": ["common", "helpers", "templates"]
    }
}

# Base paths
CURRENT_REPORTS = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/REPORTS")
NEW_PROJECT_ROOT = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/ORGANIZED_PROJECTS")
BACKUP_ROOT = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_BACKUP")

def create_project_structure():
    """Create the organized project structure"""
    print("🏗️ Creating organized project structure...")
    
    # Create backup of current state
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = BACKUP_ROOT / f"backup_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    if CURRENT_REPORTS.exists():
        shutil.copytree(CURRENT_REPORTS, backup_dir / "REPORTS")
        print(f"✅ Backup created at: {backup_dir}")
    
    # Create new project structure
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
{chr(10).join(f"- {script}" for script in config['scripts'])}

## Structure
{chr(10).join(f"- {folder}/" for folder in config['folders'])}

## Usage
Run scripts from this directory to maintain proper paths and dependencies.
"""
        
        (project_path / "README.md").write_text(readme_content)
        print(f"📁 Created project: {project_name}")

def move_scripts_to_projects():
    """Move existing scripts to appropriate project folders"""
    print("\n📦 Moving scripts to organized projects...")
    
    # Script to project mapping
    script_locations = {}
    for project_name, config in PROJECT_STRUCTURE.items():
        for script in config["scripts"]:
            script_locations[script] = project_name
    
    # Move scripts
    moved_count = 0
    for script_file in CURRENT_REPORTS.glob("*.py"):
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
    
    print(f"\n📊 Moved {moved_count} scripts to organized projects")

def create_master_config():
    """Create master configuration file"""
    config_content = f"""#!/usr/bin/env python3
'''
NOIZYGENIE MASTER CONFIGURATION
Centralized configuration for all projects
'''

from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).parent
KONTAKT_LAB = PROJECT_ROOT.parent
REPORTS_DIR = KONTAKT_LAB / "REPORTS"
BACKUP_DIR = KONTAKT_LAB / "PROJECT_BACKUP"

# Volume paths
VOLUMES_6TB = Path("/Volumes/6TB")
NI_SOURCE = VOLUMES_6TB / "Native Instruments"
NI_2026_ROOT = VOLUMES_6TB / "_NI_2026"
LIBRARIES_DEST = NI_2026_ROOT / "LIBRARIES"
SAFETY_ROOT = NI_2026_ROOT / "SAFETY"

# Project paths
PROJECTS = {{
    {chr(10).join(f'    "{name}": PROJECT_ROOT / "{name}",' for name in PROJECT_STRUCTURE.keys())}
}}

# Common file extensions
INSTRUMENT_EXT = {{".nki", ".nkm"}}
AUDIO_EXT = {{".wav", ".aif", ".aiff", ".ncw"}}
MONOLITH_EXT = {{".nkx", ".nks", ".nkb", ".nksn", ".nkc", ".nkr"}}

# Vendor hints
VENDOR_HINTS = {{
    "Cinesamples": "Cinesamples",
    "Audiobro": "Audiobro", 
    "8Dio": "8Dio",
    "Project Sam": "ProjectSAM",
    "Spitfire Audio": "Spitfire Audio",
    "Output": "Output",
    "EastWest": "EastWest",
}}

print("🔧 NOIZYGENIE Master Config Loaded")
"""
    
    config_path = NEW_PROJECT_ROOT / "master_config.py"
    config_path.write_text(config_content)
    print(f"⚙️ Created master configuration: {config_path}")

def create_project_launcher():
    """Create a unified project launcher"""
    launcher_content = """#!/usr/bin/env python3
'''
NOIZYGENIE PROJECT LAUNCHER
Unified interface for all project tools
'''

import sys
import subprocess
from pathlib import Path

# Import master config
sys.path.append(str(Path(__file__).parent))
from master_config import PROJECTS

AVAILABLE_SCRIPTS = {
    "1": ("Deep Scan & Rebuild", PROJECTS["KONTAKT_LAB_MANAGER"] / "ni_deep_scan_rebuild.py"),
    "2": ("Purity Migration", PROJECTS["KONTAKT_LAB_MANAGER"] / "ni_purity_migrate.py"),
    "3": ("Name Normalization", PROJECTS["KONTAKT_LAB_MANAGER"] / "ni_name_normalize.py"),
    "4": ("Targeted Repair", PROJECTS["LIBRARY_REPAIR_TOOLS"] / "hog_targeted_repair.py"),
    "5": ("Parallel Repair", PROJECTS["LIBRARY_REPAIR_TOOLS"] / "hog_parallel_runner.py"),
    "6": ("Find Original Homes", PROJECTS["FILE_MAPPING_SYSTEM"] / "find_original_homes.py"),
    "7": ("Rehoming from Map", PROJECTS["FILE_MAPPING_SYSTEM"] / "rehoming_from_map.py"),
    "8": ("Plugin Scan", PROJECTS["PLUGIN_MANAGEMENT"] / "plugin_vendor_scan.py"),
}

def main():
    print("🧙‍♂️ NOIZYGENIE PROJECT LAUNCHER")
    print("=" * 50)
    
    for key, (name, _) in AVAILABLE_SCRIPTS.items():
        print(f"{key}. {name}")
    
    print("\\nq. Quit")
    
    choice = input("\\nSelect a tool to run: ").strip()
    
    if choice.lower() == 'q':
        print("👋 Goodbye!")
        return
    
    if choice in AVAILABLE_SCRIPTS:
        name, script_path = AVAILABLE_SCRIPTS[choice]
        print(f"\\n🚀 Launching: {name}")
        print(f"📄 Script: {script_path}")
        
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)])
        else:
            print(f"❌ Script not found: {script_path}")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
"""
    
    launcher_path = NEW_PROJECT_ROOT / "project_launcher.py"
    launcher_path.write_text(launcher_content)
    os.chmod(launcher_path, 0o755)  # Make executable
    print(f"🚀 Created project launcher: {launcher_path}")

def main():
    """Organize all projects"""
    print("🧙‍♂️ NOIZYGENIE PROJECT ORGANIZER")
    print("🔥" * 50)
    
    # Create directory structure
    NEW_PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Execute organization steps
    create_project_structure()
    move_scripts_to_projects()
    create_master_config()
    create_project_launcher()
    
    print("\n" + "🎉" * 50)
    print("✅ PROJECT ORGANIZATION COMPLETE!")
    print("🎉" * 50)
    print(f"📁 Projects organized in: {NEW_PROJECT_ROOT}")
    print(f"🔧 Master config: {NEW_PROJECT_ROOT / 'master_config.py'}")
    print(f"🚀 Launcher: {NEW_PROJECT_ROOT / 'project_launcher.py'}")
    print(f"💾 Backup: {BACKUP_ROOT}")
    print("\n🌟 Use project_launcher.py to run any tool!")

if __name__ == "__main__":
    main()