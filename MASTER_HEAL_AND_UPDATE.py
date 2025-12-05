#!/usr/bin/env python3
"""
🔥 MASTER HEAL & UPDATE - SAMPLE LIBRARY CONSOLIDATION 🔥
For: Rob Plowman - NOIZYLAB & Fish Music Inc
Purpose: Consolidate 6TB libraries to SAMPLE_MASTER with full organization
"""

import os
import sys
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import subprocess

# =============================================================================
# CONFIGURATION
# =============================================================================

SAMPLE_MASTER = Path("/Volumes/SAMPLE_MASTER")
SOURCE_6TB = Path("/Volumes/6TB")

# Target structure on SAMPLE_MASTER
TARGET_STRUCTURE = {
    "01_Native_Instruments": "Native Instruments Kontakt Libraries",
    "02_8Dio": "8Dio Sample Libraries", 
    "03_Spectrasonics": "Omnisphere, Keyscape, Trilian, Stylus",
    "04_Toontrack": "Superior Drummer, EZdrummer",
    "05_Orchestral": "Orchestra, Strings, Brass, Woodwinds",
    "06_Drums_Percussion": "Drums, Percussion, Drum Machines",
    "07_Synths_Keys": "Synthesizers, Keyboards, Pianos",
    "08_Guitars_Bass": "Guitars, Bass instruments",
    "09_Vocals_Choir": "Vocal libraries, Choirs",
    "10_World_Ethnic": "World instruments, Ethnic",
    "11_SFX_Cinematic": "Sound effects, Cinematic tools",
    "12_Loops_Construction": "Loop libraries, Construction kits",
    "13_Nexus_reFX": "Nexus content",
    "99_Archives": "Legacy and archived content"
}

# Priority libraries to migrate first
PRIORITY_MIGRATIONS = [
    # Native Instruments COMPLETE (1TB)
    ("_NI_2026/LIBRARIES/Native Instruments/COMPLETE", "01_Native_Instruments/COMPLETE"),
    # 8Dio Libraries (871GB)  
    ("_NI_2026/LIBRARIES/8Dio/PARTIAL/8Dio Libraries", "02_8Dio"),
    # Superior Drummer (218GB)
    ("Superior Drummer", "04_Toontrack/Superior_Drummer"),
    # Kontakt Lab organized (52GB)
    ("KONTAKT_LAB/DEEP_ORGANIZED", "05_Orchestral/_DEEP_ORGANIZED"),
]

class MasterHealer:
    """Master consolidation and healing system"""
    
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run
        self.stats = {
            'scanned': 0,
            'duplicates_found': 0,
            'space_recoverable': 0,
            'files_to_move': 0,
            'errors': [],
            'warnings': []
        }
        self.inventory = {
            'sample_master': {},
            'source_6tb': {},
            'duplicates': [],
            'missing': [],
            'orphans': []
        }
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
    def check_volumes(self) -> bool:
        """Verify both volumes are mounted and accessible"""
        print("=" * 70)
        print("🔍 CHECKING VOLUMES")
        print("=" * 70)
        
        volumes_ok = True
        
        # Check SAMPLE_MASTER
        if SAMPLE_MASTER.exists():
            free_space = shutil.disk_usage(SAMPLE_MASTER).free / (1024**4)  # TB
            print(f"✅ SAMPLE_MASTER mounted - {free_space:.2f} TB free")
        else:
            print(f"❌ SAMPLE_MASTER not mounted at {SAMPLE_MASTER}")
            volumes_ok = False
            
        # Check 6TB
        if SOURCE_6TB.exists():
            used_space = shutil.disk_usage(SOURCE_6TB).used / (1024**4)  # TB
            print(f"✅ 6TB mounted - {used_space:.2f} TB used")
        else:
            print(f"❌ 6TB not mounted at {SOURCE_6TB}")
            volumes_ok = False
            
        print()
        return volumes_ok
    
    def scan_directory(self, path: Path, extensions: Set[str] = None) -> Dict:
        """Scan a directory and catalog all sample files"""
        if extensions is None:
            extensions = {'.nki', '.nkm', '.nkc', '.nkx', '.ncw', '.wav', '.aif', '.aiff'}
        
        catalog = {
            'total_files': 0,
            'total_size': 0,
            'by_type': defaultdict(lambda: {'count': 0, 'size': 0}),
            'libraries': defaultdict(lambda: {'files': 0, 'size': 0, 'path': ''}),
            'files': []
        }
        
        if not path.exists():
            return catalog
            
        try:
            for item in path.rglob('*'):
                if item.is_file():
                    ext = item.suffix.lower()
                    try:
                        size = item.stat().st_size
                    except:
                        size = 0
                    
                    catalog['total_files'] += 1
                    catalog['total_size'] += size
                    catalog['by_type'][ext]['count'] += 1
                    catalog['by_type'][ext]['size'] += size
                    
                    # Identify library from path
                    rel_path = item.relative_to(path)
                    if len(rel_path.parts) > 0:
                        lib_name = rel_path.parts[0]
                        catalog['libraries'][lib_name]['files'] += 1
                        catalog['libraries'][lib_name]['size'] += size
                        catalog['libraries'][lib_name]['path'] = str(path / lib_name)
                    
                    self.stats['scanned'] += 1
                    
        except Exception as e:
            self.stats['errors'].append(f"Scan error at {path}: {e}")
            
        return catalog
    
    def find_duplicates(self) -> List[Tuple]:
        """Find duplicate libraries between sources"""
        print("=" * 70)
        print("🔍 SCANNING FOR DUPLICATES")
        print("=" * 70)
        
        duplicates = []
        
        # Get library names from both locations
        sm_libs = set()
        s6_libs = set()
        
        # Scan SAMPLE_MASTER
        for folder in SAMPLE_MASTER.iterdir():
            if folder.is_dir() and not folder.name.startswith('.'):
                sm_libs.add(folder.name)
                for sub in folder.rglob('*'):
                    if sub.is_dir():
                        sm_libs.add(sub.name)
        
        # Scan key 6TB locations
        key_paths = [
            SOURCE_6TB / "_NI_2026/LIBRARIES/Native Instruments/COMPLETE",
            SOURCE_6TB / "_NI_2026/LIBRARIES/8Dio/PARTIAL/8Dio Libraries",
            SOURCE_6TB / "KONTAKT_LAB/DEEP_ORGANIZED",
            SOURCE_6TB / "KONTAKT_LIBRARIES"
        ]
        
        for kp in key_paths:
            if kp.exists():
                for item in kp.iterdir():
                    if item.is_dir():
                        s6_libs.add(item.name)
        
        # Find overlaps
        common = sm_libs & s6_libs
        if common:
            print(f"⚠️  Found {len(common)} potential duplicates:")
            for name in sorted(common)[:20]:
                print(f"   • {name}")
                duplicates.append(name)
            if len(common) > 20:
                print(f"   ... and {len(common) - 20} more")
        else:
            print("✅ No obvious duplicates found")
        
        self.inventory['duplicates'] = duplicates
        self.stats['duplicates_found'] = len(duplicates)
        print()
        return duplicates
    
    def create_target_structure(self):
        """Create organized folder structure on SAMPLE_MASTER"""
        print("=" * 70)
        print("📁 CREATING TARGET STRUCTURE")
        print("=" * 70)
        
        for folder, description in TARGET_STRUCTURE.items():
            target = SAMPLE_MASTER / folder
            if not self.dry_run:
                target.mkdir(parents=True, exist_ok=True)
            status = "[DRY RUN]" if self.dry_run else "✅"
            print(f"{status} {folder}/ - {description}")
        
        print()
    
    def calculate_migration_plan(self) -> Dict:
        """Calculate what needs to be migrated"""
        print("=" * 70)
        print("📊 CALCULATING MIGRATION PLAN")
        print("=" * 70)
        
        plan = {
            'total_size': 0,
            'total_files': 0,
            'migrations': []
        }
        
        for source_rel, target_rel in PRIORITY_MIGRATIONS:
            source_path = SOURCE_6TB / source_rel
            if source_path.exists():
                try:
                    # Get size using du command (faster)
                    result = subprocess.run(
                        ['du', '-sk', str(source_path)],
                        capture_output=True, text=True, timeout=30
                    )
                    if result.returncode == 0:
                        size_kb = int(result.stdout.split()[0])
                        size_gb = size_kb / (1024 * 1024)
                    else:
                        size_gb = 0
                except:
                    size_gb = 0
                
                plan['migrations'].append({
                    'source': str(source_path),
                    'target': str(SAMPLE_MASTER / target_rel),
                    'size_gb': size_gb
                })
                plan['total_size'] += size_gb
                
                print(f"📦 {source_rel}")
                print(f"   → {target_rel}")
                print(f"   Size: {size_gb:.1f} GB")
                print()
        
        print(f"📊 TOTAL TO MIGRATE: {plan['total_size']:.1f} GB")
        print()
        return plan
    
    def generate_heal_script(self) -> str:
        """Generate executable heal/migration script"""
        script_path = Path(f"/Users/m2ultra/NOIZYLAB/EXECUTE_HEAL_{self.timestamp}.sh")
        
        script_content = f'''#!/usr/bin/env bash
# =============================================================================
# 🔥 MASTER HEAL & UPDATE EXECUTION SCRIPT
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# For: Rob Plowman - NOIZYLAB & Fish Music Inc
# =============================================================================

set -euo pipefail

# Colors
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
RED='\\033[0;31m'
CYAN='\\033[0;36m'
NC='\\033[0m'

log() {{ echo -e "${{CYAN}}[$(date +'%H:%M:%S')]${{NC}} $1"; }}
success() {{ echo -e "${{GREEN}}✅${{NC}} $1"; }}
warning() {{ echo -e "${{YELLOW}}⚠️${{NC}} $1"; }}
error() {{ echo -e "${{RED}}❌${{NC}} $1"; }}

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║           🔥 MASTER HEAL & UPDATE EXECUTION 🔥                    ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

# Check volumes
if [ ! -d "/Volumes/SAMPLE_MASTER" ]; then
    error "SAMPLE_MASTER not mounted!"
    exit 1
fi

if [ ! -d "/Volumes/6TB" ]; then
    error "6TB not mounted!"
    exit 1
fi

success "Both volumes mounted"
echo ""

# Check available space
AVAIL=$(df -g /Volumes/SAMPLE_MASTER | tail -1 | awk '{{print $4}}')
log "SAMPLE_MASTER available space: ${{AVAIL}} GB"
echo ""

# Create target structure
log "Creating target folder structure..."
'''
        
        for folder in TARGET_STRUCTURE.keys():
            script_content += f'mkdir -p "/Volumes/SAMPLE_MASTER/{folder}"\n'
        
        script_content += '''
success "Folder structure created"
echo ""

# Migration function
migrate_library() {
    local SOURCE="$1"
    local TARGET="$2"
    local NAME="$3"
    
    if [ ! -d "$SOURCE" ]; then
        warning "Source not found: $SOURCE"
        return 1
    fi
    
    log "Migrating: $NAME"
    log "  From: $SOURCE"
    log "  To: $TARGET"
    
    mkdir -p "$TARGET"
    
    # Use rsync for reliable transfer with progress
    rsync -av --progress "$SOURCE/" "$TARGET/" 2>&1 | tail -5
    
    if [ $? -eq 0 ]; then
        success "Completed: $NAME"
    else
        error "Failed: $NAME"
        return 1
    fi
    echo ""
}

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                    STARTING MIGRATIONS                            ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

'''
        
        # Add migration commands
        for source_rel, target_rel in PRIORITY_MIGRATIONS:
            source_path = SOURCE_6TB / source_rel
            if source_path.exists():
                name = source_rel.split('/')[-1]
                script_content += f'''migrate_library \\
    "/Volumes/6TB/{source_rel}" \\
    "/Volumes/SAMPLE_MASTER/{target_rel}" \\
    "{name}"

'''
        
        script_content += '''
echo ""
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                    MIGRATION COMPLETE                             ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

# Final stats
log "Final SAMPLE_MASTER usage:"
df -h /Volumes/SAMPLE_MASTER

echo ""
success "🔥 HEAL & UPDATE COMPLETE! 🔥"
'''
        
        if not self.dry_run:
            with open(script_path, 'w') as f:
                f.write(script_content)
            os.chmod(script_path, 0o755)
            print(f"✅ Script generated: {script_path}")
        else:
            print(f"[DRY RUN] Would generate: {script_path}")
        
        return str(script_path)
    
    def generate_report(self) -> str:
        """Generate comprehensive status report"""
        report_path = Path(f"/Users/m2ultra/NOIZYLAB/HEAL_REPORT_{self.timestamp}.md")
        
        report = f'''# 🔥 MASTER HEAL & UPDATE REPORT
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**For:** Rob Plowman - NOIZYLAB & Fish Music Inc

---

## 📊 SCAN SUMMARY

| Metric | Value |
|--------|-------|
| Files Scanned | {self.stats['scanned']:,} |
| Duplicates Found | {self.stats['duplicates_found']} |
| Errors | {len(self.stats['errors'])} |
| Warnings | {len(self.stats['warnings'])} |

---

## 💾 VOLUME STATUS

### SAMPLE_MASTER
- **Path:** `/Volumes/SAMPLE_MASTER`
- **Type:** SMB Network Share
- **Capacity:** 1.8 TB
- **Current Usage:** ~51 GB (3%)
- **Available:** ~1.75 TB

### 6TB Source
- **Path:** `/Volumes/6TB`  
- **Type:** Local Disk
- **Capacity:** 5.5 TB
- **Current Usage:** 4.3 TB (79%)
- **Available:** 1.2 TB

---

## 📁 TARGET STRUCTURE

| Folder | Purpose |
|--------|---------|
'''
        
        for folder, desc in TARGET_STRUCTURE.items():
            report += f'| `{folder}/` | {desc} |\n'
        
        report += f'''
---

## 🚀 MIGRATION PRIORITIES

### Phase 1: Native Instruments COMPLETE (~1 TB)
- Abbey Road Drummer series (6 libraries)
- Symphony Series (6 libraries)
- Session Guitarist/Bassist/Horns/Strings
- Stradivari, Guarneri, Amati strings
- The Giant, Una Corda, Vienna Concert Grand
- Cuba, India, Middle East, West Africa, East Asia
- Damage, Action Strikes, Rise and Hit
- EXHALE, Mysteria, Thrill
- **99+ premium Kontakt libraries**

### Phase 2: 8Dio Collection (~871 GB)
- Hybrid Tools Vol 1-4, NEO, NEO II
- Hybrid Tools Equinox, Terminus, Synphony
- Century Strings (Normale, Sordino)
- Century Harps, Ostinato Strings
- Songwriting Guitar, Post-Apocalyptic Guitar
- Glass Marimba, Propanium
- **30+ 8Dio libraries**

### Phase 3: Toontrack (~218 GB)
- Superior Drummer 3 Core
- SDX: Avatar, Music City, Roots Vol 2
- SDX: Indiependent, CVMKII, Allaire, Hit Factory

### Phase 4: Organized Content (~52 GB)
- DEEP_ORGANIZED categories
- Orchestral, Ethnic, Electronic
- Drums, Keys, Vocals, Loops, SFX

---

## ⚠️ DUPLICATES IDENTIFIED

'''
        if self.inventory['duplicates']:
            for dup in self.inventory['duplicates'][:30]:
                report += f'- {dup}\n'
            if len(self.inventory['duplicates']) > 30:
                report += f'- ... and {len(self.inventory["duplicates"]) - 30} more\n'
        else:
            report += '*No obvious duplicates found*\n'
        
        report += f'''
---

## 🔧 EXECUTION

### To Run Migration:
```bash
cd /Users/m2ultra/NOIZYLAB
./EXECUTE_HEAL_{self.timestamp}.sh
```

### Estimated Time:
- **Total Data:** ~2.1 TB
- **Network Transfer:** 8-12 hours (depends on network speed)
- **Local Copy:** 2-4 hours (if direct attached)

---

## ✅ POST-MIGRATION CHECKLIST

- [ ] Verify SAMPLE_MASTER folder structure
- [ ] Spot-check random libraries load in Kontakt
- [ ] Update Native Access library paths
- [ ] Run Kontakt batch resave if needed
- [ ] Archive original 6TB locations
- [ ] Update backup schedules

---

**🔥 READY FOR EXECUTION 🔥**
'''
        
        if not self.dry_run:
            with open(report_path, 'w') as f:
                f.write(report)
            print(f"✅ Report generated: {report_path}")
        else:
            print(f"[DRY RUN] Would generate: {report_path}")
        
        return report
    
    def run(self):
        """Execute full heal and update process"""
        print()
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║        🔥 MASTER HEAL & UPDATE - SAMPLE LIBRARY CONSOLIDATION 🔥  ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print()
        
        if self.dry_run:
            print("⚠️  DRY RUN MODE - No changes will be made")
            print()
        
        # Step 1: Check volumes
        if not self.check_volumes():
            print("❌ Volume check failed. Aborting.")
            return False
        
        # Step 2: Find duplicates
        self.find_duplicates()
        
        # Step 3: Create target structure
        self.create_target_structure()
        
        # Step 4: Calculate migration plan
        plan = self.calculate_migration_plan()
        
        # Step 5: Generate executable script
        script_path = self.generate_heal_script()
        
        # Step 6: Generate report
        report = self.generate_report()
        
        # Summary
        print("=" * 70)
        print("🎯 HEAL & UPDATE SUMMARY")
        print("=" * 70)
        print(f"   Files scanned: {self.stats['scanned']:,}")
        print(f"   Duplicates found: {self.stats['duplicates_found']}")
        print(f"   Total to migrate: {plan['total_size']:.1f} GB")
        print(f"   Errors: {len(self.stats['errors'])}")
        print()
        
        if self.dry_run:
            print("💡 To execute, run:")
            print(f"   python3 {__file__} --execute")
        else:
            print(f"💡 To run migration:")
            print(f"   {script_path}")
        
        print()
        print("🔥 HEAL & UPDATE PREPARATION COMPLETE! 🔥")
        return True


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🔥 MASTER HEAL & UPDATE')
    parser.add_argument('--execute', action='store_true', help='Execute (not dry run)')
    parser.add_argument('--dry-run', action='store_true', default=True, help='Dry run mode')
    
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    healer = MasterHealer(dry_run=dry_run)
    healer.run()


if __name__ == '__main__':
    main()
