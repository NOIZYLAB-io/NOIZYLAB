#!/usr/bin/env python3
"""
Migrate _CLAUDE_NEEDS Directory
Safely moves all contents to appropriate destinations and deletes folder
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

SOURCE = Path("/Volumes/12TB/_CLAUDE_NEEDS")
LOG_DIR = Path("/Users/m2ultra/NOIZYLAB/logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"claude_needs_migration_{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"

# Destination mappings
DESTINATIONS = {
    # NOIZYLAB related - move to NOIZYLAB
    'NOIZYLAB_WORKSPACE': Path("/Users/m2ultra/NOIZYLAB/workspaces"),
    'NOIZYLAB': Path("/Users/m2ultra/NOIZYLAB/archive/claude_needs"),
    'MC96_DOCUMENTATION': Path("/Users/m2ultra/NOIZYLAB/docs/mc96"),
    'MissionControl96_Support': Path("/Users/m2ultra/NOIZYLAB/support"),
    'MISSION_CONTROL_ARCHIVE': Path("/Users/m2ultra/NOIZYLAB/archive/mission-control"),
    'LOGS': Path("/Users/m2ultra/NOIZYLAB/logs/archive"),
    
    # NOIZYFISH related - move to _ORGANIZED Production
    'NOIZYVOX': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects/NOIZYVOX"),
    'NoizyFish_Fishnet': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects/NoizyFish_Fishnet"),
    'CLAUDES_NOIZYFISH_WORLD': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🚀 Production_Projects/CLAUDES_NOIZYFISH_WORLD"),
    
    # Music related - move to appropriate categories
    'Sample_Collection_2026': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🎵 Music_Projects/Sample_Collection_2026"),
    'MUSIC_MONETIZATION': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/💰 Billion_Dollar_Ideas/MUSIC_MONETIZATION"),
    'MUSIC DOCS': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📚 Learning_Projects/MUSIC_DOCS"),
    
    # Archives - move to Archives
    'RED DRAGON': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives/RED_DRAGON_ARCHIVE"),
    'From 4TB BlueFish': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives/From_4TB_BlueFish"),
    'FLIP 4TB 01': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives/FLIP_4TB_01"),
    'LIVE SHOW DUPES': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives/LIVE_SHOW_DUPES"),
    'FOLDER TIDY KTK': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives/FOLDER_TIDY_KTK"),
    
    # Installers
    'Installers_2026': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🔧 Tools_And_Utilities/Installers_2026"),
}

class ClaudeNeedsMigrator:
    def __init__(self, dry_run=False, copy_mode=False):
        self.source = SOURCE
        self.dry_run = dry_run
        self.copy_mode = copy_mode
        self.migration_log = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': dry_run,
            'copy_mode': copy_mode,
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
            # Skip hidden files, migration script, and log files
            if item.name.startswith('.') or item.name == 'MIGRATE_CLAUDE_NEEDS.py':
                continue
            
            if item.is_dir():
                size = self.estimate_dir_size(item)
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
    
    def estimate_dir_size(self, path):
        """Estimate directory size quickly"""
        total = 0
        count = 0
        try:
            for root, dirs, files in os.walk(path):
                # Skip large directories to speed up
                dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'venv']]
                
                for file in files:
                    try:
                        file_path = Path(root) / file
                        total += file_path.stat().st_size
                        count += 1
                        if count > 500:  # Limit for speed
                            break
                    except:
                        pass
                if count > 500:
                    break
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
        
        # Handle NOIZYLAB items - ensure they go to /Users/m2ultra/NOIZYLAB/
        if 'noizylab' in item_name.lower():
            # Map to appropriate NOIZYLAB subdirectory
            if 'workspace' in item_name.lower():
                return Path("/Users/m2ultra/NOIZYLAB/workspaces")
            elif 'mc96' in item_name.lower() or 'mission' in item_name.lower():
                return Path("/Users/m2ultra/NOIZYLAB/archive")
            else:
                return Path("/Users/m2ultra/NOIZYLAB/archive")
        
        # Handle alias files
        if 'alias' in item_name.lower():
            # Find the actual directory
            base_name = item_name.replace(' alias', '').replace(' alias', '').strip()
            if base_name in DESTINATIONS:
                return DESTINATIONS[base_name].parent
        
        # Check if it's a Python script - goes to NOIZYLAB scripts
        if item_name.endswith('.py'):
            return Path("/Users/m2ultra/NOIZYLAB/scripts")
        
        # Default to archives
        return Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/📦 Archives")
    
    def migrate_item(self, item_name, item_info):
        """Migrate a single item"""
        source_path = Path(item_info['path'])
        dest_base = self.determine_destination(item_name)
        
        # Handle alias files - skip them if directory exists
        if 'alias' in item_name.lower() or source_path.is_symlink():
            base_name = item_name.replace(' alias', '').strip()
            actual_dir = self.source / base_name
            if actual_dir.exists() and actual_dir.is_dir():
                print(f"\n⏭️  Skipping alias: {item_name}")
                self.migration_log['skipped'].append({
                    'item': item_name,
                    'reason': 'alias - actual directory exists'
                })
                return {'status': 'skipped'}
        
        # Ensure destination exists
        dest_base.mkdir(parents=True, exist_ok=True)
        
        # For files, use the filename
        if source_path.is_file():
            dest_path = dest_base / item_name
        else:
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
            action_str = 'copy' if self.copy_mode else 'move'
            print(f"   [DRY RUN] Would {action_str}")
            return {'status': 'dry_run', 'source': str(source_path), 'dest': str(dest_path)}
        
        try:
            if self.copy_mode:
                # Copy mode - keep original
                if source_path.is_dir():
                    shutil.copytree(str(source_path), str(dest_path), dirs_exist_ok=True)
                    action = 'copied_dir'
                else:
                    shutil.copy2(str(source_path), str(dest_path))
                    action = 'copied_file'
                print(f"   ✅ Copied successfully")
            else:
                # Move mode - remove original
                if source_path.is_dir():
                    shutil.move(str(source_path), str(dest_path))
                    action = 'moved_dir'
                else:
                    shutil.move(str(source_path), str(dest_path))
                    action = 'moved_file'
                print(f"   ✅ Moved successfully")
            
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
        mode_str = 'DRY RUN' if self.dry_run else ('COPY MODE' if self.copy_mode else 'MOVE MODE')
        print(f"Mode: {mode_str}")
        print(f"Source: {self.source}")
        print()
        
        if not self.source.exists():
            print(f"❌ Source directory not found: {self.source}")
            return
        
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
            if self.copy_mode:
                print("\n⚠️  WARNING: This will COPY all files (originals will remain)!")
                confirm = input("Type 'YES COPY ALL' to proceed: ").strip()
                if confirm != 'YES COPY ALL':
                    print("❌ Migration cancelled")
                    return
            else:
                print("\n⚠️  WARNING: This will MOVE all files and DELETE the _CLAUDE_NEEDS folder!")
                confirm = input("Type 'YES MOVE ALL' to proceed: ").strip()
                if confirm != 'YES MOVE ALL':
                    print("❌ Migration cancelled")
                    return
        
        print("\n" + "=" * 80)
        print("🚀 STARTING MIGRATION")
        print("=" * 80)
        
        # Migrate each item
        for name, info in sorted(contents.items()):
            result = self.migrate_item(name, info)
            
            if result.get('status') == 'success':
                if 'copied' in result.get('action', ''):
                    self.migration_log['copied'].append(result)
                else:
                    self.migration_log['moved'].append(result)
            elif result.get('status') == 'error':
                self.migration_log['errors'].append(result)
            elif result.get('status') == 'dry_run':
                self.migration_log['moved'].append(result)
        
        # Save log
        with open(LOG_FILE, 'w') as f:
            json.dump(self.migration_log, f, indent=2)
        
        print("\n" + "=" * 80)
        print("📊 MIGRATION SUMMARY")
        print("=" * 80)
        print(f"✅ Migrated: {len(self.migration_log['moved'])}")
        print(f"⏭️  Skipped: {len(self.migration_log['skipped'])}")
        print(f"❌ Errors: {len(self.migration_log['errors'])}")
        
        if self.migration_log['errors']:
            print("\n⚠️  Errors encountered:")
            for error in self.migration_log['errors']:
                print(f"  • {error.get('source', 'Unknown')}: {error.get('error', 'Unknown error')}")
        
        print(f"\n💾 Log saved: {LOG_FILE}")
        
        # Delete source folder if migration successful and not copy mode
        if not self.dry_run and not self.copy_mode:
            # Check what's left
            remaining = []
            for item in self.source.iterdir():
                if not item.name.startswith('.') and item.name != 'MIGRATE_CLAUDE_NEEDS.py':
                    remaining.append(item.name)
            
            if len(remaining) == 0 or all(item in ['MIGRATE_CLAUDE_NEEDS.py', '.DS_Store'] for item in remaining):
                print("\n🧹 Cleaning up _CLAUDE_NEEDS folder...")
                try:
                    # Remove .DS_Store if exists
                    ds_store = self.source / '.DS_Store'
                    if ds_store.exists():
                        ds_store.unlink()
                    
                    # Try to remove directory
                    if self.source.exists() and len(list(self.source.iterdir())) <= 1:
                        # Only migration script left
                        shutil.rmtree(self.source)
                        print(f"✅ Deleted: {self.source}")
                    else:
                        print(f"⚠️  Folder not empty. Remaining: {remaining}")
                        print("   Please review and delete manually if needed")
                except Exception as e:
                    print(f"⚠️  Could not delete source folder: {e}")
                    print("   You may need to delete it manually")
        elif self.copy_mode:
            print("\nℹ️  Copy mode: Original files remain in _CLAUDE_NEEDS")
            print("   You can delete the folder manually if desired")
        
        print("\n✅ Migration complete!")

def sort_after_migration():
    """Sort and organize everything after migration"""
    print("\n" + "=" * 80)
    print("📦 SORTING & ORGANIZING AFTER MIGRATION")
    print("=" * 80)
    
    noizylab = Path("/Users/m2ultra/NOIZYLAB")
    
    # Run organization scripts
    scripts_to_run = [
        ("FAST_CLEANUP.sh", "bash"),
        ("QUICK_ORGANIZE.py", "python3"),
    ]
    
    for script_name, command in scripts_to_run:
        script_path = noizylab / script_name
        if script_path.exists():
            print(f"\n🔄 Running {script_name}...")
            try:
                import subprocess
                subprocess.run([command, str(script_path)], cwd=str(noizylab), timeout=300)
                print(f"✅ {script_name} completed")
            except Exception as e:
                print(f"⚠️  {script_name} had issues: {e}")
    
    # Organize _ORGANIZED if it exists
    organized = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")
    if organized.exists():
        analyze_script = organized / "ANALYZE_ORGANIZED.py"
        if analyze_script.exists():
            print(f"\n🔄 Analyzing _ORGANIZED...")
            try:
                import subprocess
                subprocess.run(["python3", str(analyze_script)], cwd=str(organized), timeout=300)
                print(f"✅ _ORGANIZED analyzed")
            except Exception as e:
                print(f"⚠️  Analysis had issues: {e}")
    
    print("\n✅ Sorting complete!")

def main():
    import sys
    
    dry_run = '--live' not in sys.argv and '--copy' not in sys.argv
    copy_mode = '--copy' in sys.argv
    skip_sort = '--no-sort' in sys.argv
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files will be moved/copied")
        print("   Add --live to move files, or --copy to copy files\n")
    elif copy_mode:
        print("📋 COPY MODE - Files will be copied (originals remain)\n")
    else:
        print("🚨 MOVE MODE - Files will be moved!\n")
        print("📦 After migration, everything will be sorted and organized!\n")
    
    migrator = ClaudeNeedsMigrator(dry_run=dry_run, copy_mode=copy_mode)
    migrator.migrate_all()
    
    # Sort after migration (unless skipped or dry run)
    if not dry_run and not skip_sort and not copy_mode:
        sort_after_migration()

if __name__ == "__main__":
    main()

