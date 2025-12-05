#!/usr/bin/env python3
"""
Migrate _CLAUDE_NEEDS Directory
Safely moves/copies all contents to appropriate destinations and deletes folder
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

SOURCE = Path("/Volumes/12TB/_CLAUDE_NEEDS")
LOG_FILE = SOURCE / ".migration_log.json"

# Destination mappings
DESTINATIONS = {
    # NOIZYLAB related
    'NOIZYLAB_WORKSPACE': Path("/Users/m2ultra/NOIZYLAB/workspaces"),
    'NOIZYLAB': Path("/Users/m2ultra/NOIZYLAB/archive"),
    'MC96_DOCUMENTATION': Path("/Users/m2ultra/NOIZYLAB/docs/mc96"),
    'MissionControl96_Support': Path("/Users/m2ultra/NOIZYLAB/support"),
    'MISSION_CONTROL_ARCHIVE': Path("/Users/m2ultra/NOIZYLAB/archive/mission-control"),
    
    # NOIZYFISH related
    'NOIZYVOX': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects"),
    'NoizyFish_Fishnet': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects"),
    'CLAUDES_NOIZYFISH_WORLD': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects"),
    
    # Music related
    'Sample_Collection_2026': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🎵 Music_Projects"),
    'MUSIC_MONETIZATION': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/💰 Billion_Dollar_Ideas"),
    'MUSIC DOCS': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📚 Learning_Projects"),
    
    # Archives
    'RED DRAGON': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives"),
    'From 4TB BlueFish': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives"),
    'FLIP 4TB 01': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives"),
    'LIVE SHOW DUPES': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives"),
    'FOLDER TIDY KTK': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives"),
    
    # Installers
    'Installers_2026': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🔧 Tools_And_Utilities"),
    
    # Logs
    'LOGS': Path("/Users/m2ultra/NOIZYLAB/logs/archive"),
}

class ClaudeNeedsMigrator:
    def __init__(self, dry_run=True):
        self.source = SOURCE
        self.dry_run = dry_run
        self.migration_log = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': dry_run,
            'moved': [],
            'copied': [],
            'errors': [],
            'skipped': []
        }
    
    def analyze_contents(self):
        """Analyze what's in _CLAUDE_NEEDS"""
        print("🔍 Analyzing _CLAUDE_NEEDS directory...")
        print("=" * 80)
        
        if not self.source.exists():
            print(f"❌ Source not found: {self.source}")
            return {}
        
        contents = {}
        
        for item in sorted(self.source.iterdir()):
            if item.name.startswith('.') or item.name == 'MIGRATE_CLAUDE_NEEDS.py':
                continue
            
            if item.is_dir():
                size = self.get_dir_size(item)
                contents[item.name] = {
                    'type': 'directory',
                    'size': size,
                    'path': str(item)
                }
            elif item.is_file():
                try:
                    size = item.stat().st_size
                    contents[item.name] = {
                        'type': 'file',
                        'size': size,
                        'path': str(item)
                    }
                except:
                    pass
        
        return contents
    
    def get_dir_size(self, path, max_depth=3):
        """Get approximate directory size"""
        total = 0
        count = 0
        try:
            for root, dirs, files in os.walk(path):
                depth = root.replace(str(path), '').count(os.sep)
                if depth >= max_depth:
                    dirs[:] = []
                    continue
                
                for file in files:
                    try:
                        file_path = Path(root) / file
                        total += file_path.stat().st_size
                        count += 1
                        if count > 1000:  # Limit for speed
                            return total
                    except:
                        pass
        except:
            pass
        return total
    
    def format_size(self, bytes_size):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    def determine_destination(self, item_name):
        """Determine destination for an item"""
        # Check direct mapping
        if item_name in DESTINATIONS:
            return DESTINATIONS[item_name]
        
        # Check if it's a NOIZYLAB item
        if 'noizylab' in item_name.lower() or 'mc96' in item_name.lower():
            return Path("/Users/m2ultra/NOIZYLAB/archive")
        
        # Check if it's NOIZYFISH related
        if 'noizyfish' in item_name.lower() or 'noizyvox' in item_name.lower():
            return Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects")
        
        # Default to archives
        return Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives")
    
    def migrate_item(self, item_name, item_info):
        """Migrate a single item"""
        source_path = Path(item_info['path'])
        dest_base = self.determine_destination(item_name)
        
        # Ensure destination exists
        dest_base.mkdir(parents=True, exist_ok=True)
        dest_path = dest_base / item_name
        
        # Handle name conflicts
        counter = 1
        original_dest = dest_path
        while dest_path.exists():
            if source_path.is_file():
                stem = original_dest.stem
                dest_path = dest_base / f"{stem}_{counter}{original_dest.suffix}"
            else:
                dest_path = dest_base / f"{item_name}_{counter}"
            counter += 1
        
        print(f"\n📦 {item_name}")
        print(f"   From: {source_path}")
        print(f"   To: {dest_path}")
        print(f"   Size: {self.format_size(item_info['size'])}")
        
        if self.dry_run:
            print("   [DRY RUN] Would move")
            return {'status': 'dry_run', 'source': str(source_path), 'dest': str(dest_path)}
        
        try:
            if source_path.is_dir():
                shutil.move(str(source_path), str(dest_path))
                action = 'moved'
            else:
                shutil.move(str(source_path), str(dest_path))
                action = 'moved'
            
            print(f"   ✅ {action.capitalize()} successfully")
            return {'status': 'success', 'action': action, 'source': str(source_path), 'dest': str(dest_path)}
        
        except Exception as e:
            error_msg = str(e)
            print(f"   ❌ Error: {error_msg}")
            return {'status': 'error', 'source': str(source_path), 'error': error_msg}
    
    def migrate_all(self):
        """Migrate all contents"""
        print("=" * 80)
        print(" " * 25 + "CLAUDE NEEDS MIGRATOR")
        print("=" * 80)
        print(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE MIGRATION'}")
        print(f"Source: {self.source}")
        print()
        
        # Analyze contents
        contents = self.analyze_contents()
        
        if not contents:
            print("❌ No contents found to migrate")
            return
        
        print(f"\n📊 Found {len(contents)} items to migrate:\n")
        
        # Show what will be migrated
        total_size = 0
        for name, info in sorted(contents.items()):
            size_str = self.format_size(info['size'])
            dest = self.determine_destination(name)
            print(f"  • {name:30s} ({size_str:>10}) → {dest.name}/")
            total_size += info['size']
        
        print(f"\n📦 Total size: {self.format_size(total_size)}")
        
        # Confirm
        if not self.dry_run:
            print("\n⚠️  This will MOVE all files and DELETE the _CLAUDE_NEEDS folder!")
            confirm = input("Type 'YES' to proceed: ").strip()
            if confirm != 'YES':
                print("❌ Migration cancelled")
                return
        
        print("\n" + "=" * 80)
        print("🚀 STARTING MIGRATION")
        print("=" * 80)
        
        # Migrate each item
        for name, info in sorted(contents.items()):
            result = self.migrate_item(name, info)
            
            if result['status'] == 'success':
                if result['action'] == 'moved':
                    self.migration_log['moved'].append(result)
            elif result['status'] == 'error':
                self.migration_log['errors'].append(result)
            elif result['status'] == 'dry_run':
                self.migration_log['moved'].append(result)
        
        # Save log
        with open(LOG_FILE, 'w') as f:
            json.dump(self.migration_log, f, indent=2)
        
        print("\n" + "=" * 80)
        print("📊 MIGRATION SUMMARY")
        print("=" * 80)
        print(f"✅ Migrated: {len(self.migration_log['moved'])}")
        print(f"❌ Errors: {len(self.migration_log['errors'])}")
        
        if self.migration_log['errors']:
            print("\n⚠️  Errors encountered:")
            for error in self.migration_log['errors']:
                print(f"  • {error.get('source', 'Unknown')}: {error.get('error', 'Unknown error')}")
        
        print(f"\n💾 Log saved: {LOG_FILE}")
        
        # Delete source folder if migration successful
        if not self.dry_run and not self.migration_log['errors']:
            remaining = [item for item in self.source.iterdir() 
                        if not item.name.startswith('.') and item.name != 'MIGRATE_CLAUDE_NEEDS.py']
            
            if not remaining or all(item.name in ['MIGRATE_CLAUDE_NEEDS.py', '.DS_Store', '.migration_log.json'] 
                                   for item in remaining):
                print("\n🧹 Cleaning up _CLAUDE_NEEDS folder...")
                try:
                    # Remove migration log file
                    if LOG_FILE.exists():
                        LOG_FILE.unlink()
                    
                    # Try to remove directory
                    if self.source.exists():
                        shutil.rmtree(self.source)
                        print(f"✅ Deleted: {self.source}")
                except Exception as e:
                    print(f"⚠️  Could not delete source folder: {e}")
                    print("   You may need to delete it manually")
        
        print("\n✅ Migration complete!")

def main():
    import sys
    
    dry_run = '--live' not in sys.argv
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files will be moved")
        print("   Add --live flag to actually migrate files\n")
    else:
        print("🚨 LIVE MODE - Files will be moved!\n")
    
    migrator = ClaudeNeedsMigrator(dry_run=dry_run)
    migrator.migrate_all()

if __name__ == "__main__":
    main()

