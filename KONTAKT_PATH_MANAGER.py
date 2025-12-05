#!/usr/bin/env python3
"""
🎹 KONTAKT PATH MANAGER 🎹
For: Rob Plowman - NOIZYLAB & Fish Music Inc
Purpose: Manage Kontakt library paths after migration

Features:
- Update Native Access library locations
- Batch update Kontakt library paths
- Fix broken sample references
- Generate Kontakt nicnt files
"""

import os
import sys
import json
import plistlib
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import subprocess
import shutil

# =============================================================================
# PATHS
# =============================================================================

SAMPLE_MASTER = Path("/Volumes/SAMPLE_MASTER")
KONTAKT_PREFS = Path.home() / "Library/Application Support/Native Instruments"
NATIVE_ACCESS_DB = Path.home() / "Library/Application Support/Native Instruments/Native Access"
SERVICE_CENTER = Path.home() / "Library/Application Support/Native Instruments/Service Center"

# =============================================================================
# KONTAKT PATH MANAGER
# =============================================================================

class KontaktPathManager:
    """Manage Kontakt library paths and references"""
    
    def __init__(self):
        self.libraries = {}
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
    def scan_sample_master(self) -> Dict:
        """Scan SAMPLE_MASTER for all Kontakt libraries"""
        print("=" * 70)
        print("🔍 SCANNING SAMPLE_MASTER FOR KONTAKT LIBRARIES")
        print("=" * 70)
        
        libraries = {}
        
        if not SAMPLE_MASTER.exists():
            print("❌ SAMPLE_MASTER not mounted!")
            return libraries
        
        # Find all .nicnt files (library definition files)
        nicnt_files = list(SAMPLE_MASTER.rglob("*.nicnt"))
        print(f"Found {len(nicnt_files)} .nicnt files")
        
        # Find directories that look like Kontakt libraries
        for category_dir in SAMPLE_MASTER.iterdir():
            if not category_dir.is_dir() or category_dir.name.startswith('.'):
                continue
            
            for lib_dir in category_dir.rglob("*"):
                if not lib_dir.is_dir():
                    continue
                
                # Check if it's a Kontakt library (has Instruments or Samples folder)
                has_instruments = (lib_dir / "Instruments").exists()
                has_samples = (lib_dir / "Samples").exists()
                has_nki = any(lib_dir.glob("*.nki")) or any(lib_dir.rglob("*.nki"))
                
                if has_instruments or has_samples or has_nki:
                    lib_name = lib_dir.name
                    libraries[lib_name] = {
                        'path': str(lib_dir),
                        'category': category_dir.name,
                        'has_instruments': has_instruments,
                        'has_samples': has_samples,
                        'nicnt': None
                    }
                    
                    # Check for nicnt file
                    nicnt = list(lib_dir.glob("*.nicnt"))
                    if nicnt:
                        libraries[lib_name]['nicnt'] = str(nicnt[0])
        
        print(f"Found {len(libraries)} Kontakt libraries")
        self.libraries = libraries
        return libraries
    
    def generate_nicnt(self, lib_name: str, lib_path: Path, vendor: str = "NOIZYLAB") -> str:
        """Generate a .nicnt file for a library"""
        # nicnt files are XML-based
        nicnt_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<productHints version="1.0">
    <Product version="1" type="Content" productSpecificContent="Kontakt7.nks">
        <ShortName>{lib_name}</ShortName>
        <Name>{lib_name}</Name>
        <Vendor>{vendor}</Vendor>
        <UPID></UPID>
        <SNPID></SNPID>
        <Visibility Type="0" value=""/>
        <ContentDir>{lib_path}</ContentDir>
        <HU></HU>
    </Product>
</productHints>
'''
        return nicnt_content
    
    def create_library_nicnts(self, output_dir: Path = None):
        """Create .nicnt files for all libraries that don't have them"""
        if output_dir is None:
            output_dir = Path("/Users/m2ultra/NOIZYLAB/nicnt_files")
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print("\n" + "=" * 70)
        print("📝 GENERATING .NICNT FILES")
        print("=" * 70)
        
        created = 0
        for lib_name, lib_info in self.libraries.items():
            if lib_info['nicnt'] is None:
                nicnt_path = output_dir / f"{lib_name}.nicnt"
                content = self.generate_nicnt(lib_name, Path(lib_info['path']))
                
                with open(nicnt_path, 'w') as f:
                    f.write(content)
                
                print(f"   ✓ {lib_name}.nicnt")
                created += 1
        
        print(f"\nCreated {created} .nicnt files in {output_dir}")
        return created
    
    def get_native_access_paths(self) -> List[Dict]:
        """Read current Native Access library paths"""
        print("\n" + "=" * 70)
        print("📖 READING NATIVE ACCESS CONFIGURATION")
        print("=" * 70)
        
        paths = []
        
        # Check for Native Access 2 config
        na2_config = NATIVE_ACCESS_DB / "settings.json"
        if na2_config.exists():
            try:
                with open(na2_config, 'r') as f:
                    config = json.load(f)
                    if 'contentPaths' in config:
                        print(f"Found {len(config['contentPaths'])} content paths:")
                        for path in config['contentPaths']:
                            print(f"   • {path}")
                            paths.append({'type': 'content', 'path': path})
            except Exception as e:
                print(f"Error reading NA2 config: {e}")
        
        # Check Service Center paths
        sc_prefs = SERVICE_CENTER / "Preferences"
        if sc_prefs.exists():
            try:
                # Service Center uses plist files
                for plist in sc_prefs.glob("*.plist"):
                    print(f"Found Service Center plist: {plist.name}")
            except Exception as e:
                print(f"Error reading SC prefs: {e}")
        
        return paths
    
    def add_sample_master_to_native_access(self):
        """Add SAMPLE_MASTER to Native Access content paths"""
        print("\n" + "=" * 70)
        print("➕ ADDING SAMPLE_MASTER TO NATIVE ACCESS")
        print("=" * 70)
        
        na2_config = NATIVE_ACCESS_DB / "settings.json"
        
        if not na2_config.exists():
            print("❌ Native Access config not found")
            print("   Please open Native Access first to create the config")
            return False
        
        try:
            with open(na2_config, 'r') as f:
                config = json.load(f)
            
            # Backup original
            backup = na2_config.with_suffix('.json.backup')
            shutil.copy(na2_config, backup)
            print(f"   Backed up config to {backup}")
            
            # Add SAMPLE_MASTER paths
            if 'contentPaths' not in config:
                config['contentPaths'] = []
            
            # Add main categories
            paths_to_add = [
                str(SAMPLE_MASTER / "01_Native_Instruments"),
                str(SAMPLE_MASTER / "02_8Dio"),
                str(SAMPLE_MASTER / "03_Spectrasonics"),
                str(SAMPLE_MASTER / "04_Toontrack"),
                str(SAMPLE_MASTER / "05_Orchestral"),
            ]
            
            added = 0
            for path in paths_to_add:
                if path not in config['contentPaths']:
                    config['contentPaths'].append(path)
                    print(f"   ✓ Added: {path}")
                    added += 1
                else:
                    print(f"   • Already exists: {path}")
            
            # Write updated config
            with open(na2_config, 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"\n✅ Added {added} new paths to Native Access")
            print("   Restart Native Access to apply changes")
            return True
            
        except Exception as e:
            print(f"❌ Error updating Native Access: {e}")
            return False
    
    def generate_path_report(self) -> str:
        """Generate a report of all library paths"""
        report_path = Path(f"/Users/m2ultra/NOIZYLAB/KONTAKT_PATHS_{self.timestamp}.md")
        
        report = f'''# 🎹 KONTAKT LIBRARY PATH REPORT
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 SUMMARY

| Metric | Value |
|--------|-------|
| Total Libraries | {len(self.libraries)} |
| With .nicnt | {sum(1 for l in self.libraries.values() if l['nicnt'])} |
| Missing .nicnt | {sum(1 for l in self.libraries.values() if not l['nicnt'])} |

---

## 📁 LIBRARIES BY CATEGORY

'''
        
        # Group by category
        by_category = {}
        for name, info in self.libraries.items():
            cat = info['category']
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append((name, info))
        
        for category in sorted(by_category.keys()):
            report += f"### {category}\n\n"
            report += "| Library | Has .nicnt | Path |\n"
            report += "|---------|------------|------|\n"
            
            for name, info in sorted(by_category[category]):
                nicnt = "✓" if info['nicnt'] else "✗"
                path = info['path'].replace(str(SAMPLE_MASTER), "...")
                report += f"| {name} | {nicnt} | `{path}` |\n"
            
            report += "\n"
        
        report += '''---

## 🔧 NEXT STEPS

1. **Native Access:** Run `add_sample_master_to_native_access()` to register paths
2. **Kontakt:** Open Kontakt and rescan for libraries
3. **Missing .nicnt:** Use `create_library_nicnts()` to generate missing files

---

**🎹 KONTAKT PATH MANAGER**
'''
        
        with open(report_path, 'w') as f:
            f.write(report)
        
        print(f"\n📄 Report saved: {report_path}")
        return str(report_path)
    
    def full_scan_and_setup(self):
        """Complete scan and setup workflow"""
        print("\n" + "=" * 70)
        print("🎹 KONTAKT PATH MANAGER - FULL SETUP")
        print("=" * 70)
        
        # Scan libraries
        self.scan_sample_master()
        
        # Get current NA paths
        self.get_native_access_paths()
        
        # Generate report
        self.generate_path_report()
        
        print("\n" + "=" * 70)
        print("✅ SCAN COMPLETE")
        print("=" * 70)
        print(f"   Libraries found: {len(self.libraries)}")
        print(f"   Missing .nicnt: {sum(1 for l in self.libraries.values() if not l['nicnt'])}")
        print()
        print("   To add to Native Access, run:")
        print("   python3 KONTAKT_PATH_MANAGER.py --add-na")
        print()


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🎹 KONTAKT PATH MANAGER')
    parser.add_argument('--scan', action='store_true', help='Scan SAMPLE_MASTER for libraries')
    parser.add_argument('--add-na', action='store_true', help='Add paths to Native Access')
    parser.add_argument('--generate-nicnt', action='store_true', help='Generate missing .nicnt files')
    parser.add_argument('--report', action='store_true', help='Generate path report')
    parser.add_argument('--full', action='store_true', help='Full scan and setup')
    
    args = parser.parse_args()
    
    manager = KontaktPathManager()
    
    if args.full or (not any([args.scan, args.add_na, args.generate_nicnt, args.report])):
        manager.full_scan_and_setup()
    else:
        if args.scan:
            manager.scan_sample_master()
        
        if args.add_na:
            manager.scan_sample_master()
            manager.add_sample_master_to_native_access()
        
        if args.generate_nicnt:
            manager.scan_sample_master()
            manager.create_library_nicnts()
        
        if args.report:
            manager.scan_sample_master()
            manager.generate_path_report()


if __name__ == '__main__':
    main()
