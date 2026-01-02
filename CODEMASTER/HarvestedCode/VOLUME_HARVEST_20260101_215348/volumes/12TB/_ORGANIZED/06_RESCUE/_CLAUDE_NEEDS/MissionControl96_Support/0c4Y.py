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

# Search paths (from your HOG scripts)
SEARCH_ROOTS = [
    Path.home() / "Desktop",
    Path.home() / "Documents", 
    Path.home() / "Downloads",
    Path.home() / "Music",
    Path.home() / "Library" / "Audio",
    Path("/Library/Audio"),
    Path("/Users/Shared"),
    Path("/Applications/Native Instruments"),
    Path("/Volumes"),
]

# Exclusion patterns (noisy paths to avoid)
NOISY_PATHS = [
    str(KONTAKT_LAB / "REPORTS"),
    str(Path.home() / "NoizyFish_VAULT"),
    str(SAFETY_ROOT),
]

def get_project_config(project_name: str) -> dict:
    '''Get configuration for a specific project'''
    return {{
        "name": project_name,
        "path": PROJECTS.get(project_name),
        "logs": PROJECTS.get(project_name) / "logs" if project_name in PROJECTS else None,
        "data": PROJECTS.get(project_name) / "data" if project_name in PROJECTS else None,
        "reports": PROJECTS.get(project_name) / "reports" if project_name in PROJECTS else None,
    }}

def save_project_state(project_name: str, state_data: dict):
    '''Save project state to JSON'''
    project_path = PROJECTS.get(project_name)
    if project_path:
        state_file = project_path / "data" / "project_state.json" 
        state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(state_file, 'w') as f:
            json.dump(state_data, f, indent=2)

def load_project_state(project_name: str) -> dict:
    '''Load project state from JSON'''
    project_path = PROJECTS.get(project_name)
    if project_path:
        state_file = project_path / "data" / "project_state.json"
        if state_file.exists():
            with open(state_file, 'r') as f:
                return json.load(f)
    return {{}}

print("🔧 NOIZYGENIE Master Config Loaded")
print(f"📁 Project Root: {{PROJECT_ROOT}}")
print(f"🎯 Active Projects: {{len(PROJECTS)}}")
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

AVAILABLE_TOOLS = {
    "1": ("Kontakt Lab Status", PROJECTS["01_KONTAKT_MANAGEMENT"] / "check_kontakt_lab_status.py"),
    "2": ("Deep Scan & Rebuild", PROJECTS["01_KONTAKT_MANAGEMENT"] / "ni_deep_scan_rebuild.py"),
    "3": ("Purity Migration", PROJECTS["02_LIBRARY_MIGRATION"] / "ni_purity_migrate.py"),
    "4": ("Name Normalization", PROJECTS["02_LIBRARY_MIGRATION"] / "ni_name_normalize.py"),
    "5": ("Targeted Repair", PROJECTS["03_REPAIR_RECOVERY"] / "hog_targeted_repair.py"),
    "6": ("Parallel Repair", PROJECTS["03_REPAIR_RECOVERY"] / "hog_parallel_runner.py"),
    "7": ("Find Original Homes", PROJECTS["04_FILE_MAPPING"] / "find_original_homes.py"),
    "8": ("Rehoming from Map", PROJECTS["04_FILE_MAPPING"] / "rehoming_from_map.py"),
    "9": ("Plugin Vendor Scan", PROJECTS["05_PLUGIN_MANAGEMENT"] / "plugin_vendor_scan.py"),
}

def show_project_status():
    '''Show status of all projects'''
    print("\\n📊 PROJECT STATUS:")
    for name, path in PROJECTS.items():
        if path.exists():
            script_count = len(list(path.glob("*.py")))
            folder_count = len([x for x in path.iterdir() if x.is_dir()])
            print(f"   ✅ {name}: {script_count} scripts, {folder_count} folders")
        else:
            print(f"   ❌ {name}: Not found")

def main():
    print("🧙‍♂️ NOIZYGENIE PROJECT LAUNCHER")
    print("=" * 60)
    
    for key, (name, script_path) in AVAILABLE_TOOLS.items():
        status = "✅" if script_path.exists() else "❌"
        print(f"{key}. {status} {name}")
    
    print("\\ns. Show Project Status")
    print("q. Quit")
    
    choice = input("\\n🚀 Select a tool to run: ").strip()
    
    if choice.lower() == 'q':
        print("👋 Goodbye!")
        return
    elif choice.lower() == 's':
        show_project_status()
        return
    
    if choice in AVAILABLE_TOOLS:
        name, script_path = AVAILABLE_TOOLS[choice]
        print(f"\\n🚀 Launching: {name}")
        print(f"📄 Script: {script_path}")
        
        if script_path.exists():
            # Change to script directory for proper relative paths
            script_dir = script_path.parent
            os.chdir(script_dir)
            subprocess.run([sys.executable, str(script_path)])
        else:
            print(f"❌ Script not found: {script_path}")
            print("   Run the project organizer to set up the structure")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
"""
    
    launcher_path = NEW_PROJECT_ROOT / "project_launcher.py"
    launcher_path.write_text(launcher_content)
    os.chmod(launcher_path, 0o755)  # Make executable
    print(f"🚀 Created project launcher: {launcher_path}")

def create_shared_utilities():
    """Create shared utility modules"""
    utils_dir = NEW_PROJECT_ROOT / "06_UTILITIES" / "common"
    utils_dir.mkdir(parents=True, exist_ok=True)
    
    # Common file operations
    file_utils_content = '''"""
Common file operation utilities for NOIZYGENIE projects
"""
import os
import shutil
import hashlib
from pathlib import Path
from typing import Optional, Tuple

def safe_move(src: Path, dst: Path, safety_dir: Optional[Path] = None) -> Tuple[str, Path]:
    """Safely move a file/folder, handling conflicts"""
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    if not dst.exists():
        shutil.move(str(src), str(dst))
        return ("moved", dst)
    
    # Handle collision
    if safety_dir:
        safety_dir.mkdir(parents=True, exist_ok=True)
        parked = safety_dir / f"{dst.name}__COLLISION__{int(time.time())}"
        shutil.move(str(src), str(parked))
        return ("collision_parked", parked)
    else:
        # Rename with counter
        counter = 1
        while dst.exists():
            stem = dst.stem
            suffix = dst.suffix
            dst = dst.parent / f"{stem}_COPY_{counter}{suffix}"
            counter += 1
        shutil.move(str(src), str(dst))
        return ("renamed", dst)

def sha1_hash(path: Path, chunk_size: int = 2**20) -> str:
    """Calculate SHA1 hash of file"""
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()

def human_bytes(n: int) -> str:
    """Convert bytes to human readable format"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024.0:
            return f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"
'''
    
    (utils_dir / "file_utils.py").write_text(file_utils_content)
    
    # Common logging utilities
    log_utils_content = '''"""
Common logging utilities for NOIZYGENIE projects
"""
import logging
from pathlib import Path
from datetime import datetime

def setup_logger(name: str, log_file: Path, level=logging.INFO):
    """Set up a logger with file and console output"""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_project_start(project_name: str, log_dir: Path):
    """Standard project start logging"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"{project_name}_{timestamp}.log"
    return setup_logger(project_name, log_file)
'''
    
    (utils_dir / "log_utils.py").write_text(log_utils_content)
    print(f"🛠️ Created shared utilities in: {utils_dir}")

def main():
    """Main organization function"""
    print("🧙‍♂️ NOIZYGENIE PROJECT ORGANIZER")
    print("🔥" * 60)
    print("Organizing your existing Python projects...")
    
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
    
    # Create summary report
    summary = {
        "organization_completed": datetime.now().isoformat(),
        "backup_location": str(backup_dir),
        "project_root": str(NEW_PROJECT_ROOT),
        "projects_created": len(PROJECT_STRUCTURE),
        "launcher": str(NEW_PROJECT_ROOT / "project_launcher.py"),
        "master_config": str(NEW_PROJECT_ROOT / "master_config.py")
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
    print(f"💾 Backup: {backup_dir}")
    print(f"📋 Summary: {summary_file}")
    print("\n🌟 Use project_launcher.py to run any tool!")
    print("🌟 Each project has its own README with usage instructions!")

if __name__ == "__main__":
    main()