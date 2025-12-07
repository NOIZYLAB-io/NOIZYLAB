#!/usr/bin/env python3
"""
Smart Project Migrator
Intelligently migrates projects between NOIZYLAB and _ORGANIZED
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime, timedelta

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
ORGANIZED = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")

class SmartMigrator:
    def __init__(self):
        self.noizylab = NOIZYLAB
        self.organized = ORGANIZED
    
    def find_archive_candidates(self, days_inactive=90):
        """Find projects in NOIZYLAB that should be archived"""
        print("🔍 Finding archive candidates...")
        print("=" * 80)
        
        candidates = []
        
        if not self.noizylab.exists():
            print("❌ NOIZYLAB not found")
            return candidates
        
        cutoff_date = datetime.now() - timedelta(days=days_inactive)
        
        for item in self.noizylab.iterdir():
            if not item.is_dir() or item.name.startswith('.'):
                continue
            
            if item.name in ['scripts', 'docs', 'logs', 'backups', 'node_modules']:
                continue
            
            # Check last modification
            try:
                mtime = datetime.fromtimestamp(item.stat().st_mtime)
                
                # Check for activity indicators
                has_recent_activity = False
                for file in item.rglob('*'):
                    if file.is_file():
                        file_mtime = datetime.fromtimestamp(file.stat().st_mtime)
                        if file_mtime > cutoff_date:
                            has_recent_activity = True
                            break
                
                if not has_recent_activity:
                    # Get project size
                    size = sum(f.stat().st_size for f in item.rglob('*') 
                              if f.is_file())
                    
                    # Detect language/category
                    category = self.detect_category(item)
                    
                    candidates.append({
                        'name': item.name,
                        'path': str(item),
                        'size': size,
                        'last_modified': mtime.isoformat(),
                        'days_inactive': (datetime.now() - mtime).days,
                        'suggested_category': category
                    })
            except Exception as e:
                pass
        
        # Sort by inactivity
        candidates.sort(key=lambda x: x['days_inactive'], reverse=True)
        
        if candidates:
            print(f"\n📦 Found {len(candidates)} archive candidates:\n")
            for i, candidate in enumerate(candidates[:20], 1):
                size_mb = candidate['size'] / (1024 * 1024)
                print(f"  {i:2}. {candidate['name']:30s}")
                print(f"      Inactive: {candidate['days_inactive']} days")
                print(f"      Size: {size_mb:.1f} MB")
                print(f"      → {candidate['suggested_category']}")
                print()
        else:
            print("✅ No archive candidates found")
        
        return candidates
    
    def detect_category(self, project_path):
        """Detect appropriate category for project"""
        file_types = {}
        
        for file in project_path.rglob('*'):
            if file.is_file():
                ext = file.suffix.lower()
                file_types[ext] = file_types.get(ext, 0) + 1
        
        # Determine category
        if file_types.get('.py', 0) > 5:
            return '🐍 Python_Projects'
        elif file_types.get('.js', 0) > 5 or file_types.get('.ts', 0) > 5:
            return '🚀 Production_Projects'
        elif file_types.get('.rb', 0) > 5:
            return '💎 Ruby_Projects'
        elif file_types.get('.rs', 0) > 5:
            return '🦀 Rust_Projects'
        elif file_types.get('.go', 0) > 5:
            return '🐹 Go_Projects'
        elif file_types.get('.swift', 0) > 5 or file_types.get('.kt', 0) > 5:
            return '📱 Mobile_Projects'
        else:
            return '🔧 Tools_And_Utilities'
    
    def archive_project(self, project_name, dry_run=True):
        """Archive a project to _ORGANIZED"""
        if not self.organized.exists():
            print(f"❌ _ORGANIZED not found: {self.organized}")
            return False
        
        project_path = self.noizylab / project_name
        if not project_path.exists():
            print(f"❌ Project not found: {project_name}")
            return False
        
        # Detect category
        category = self.detect_category(project_path)
        category_path = self.organized / category
        category_path.mkdir(exist_ok=True)
        
        dest_path = category_path / project_name
        
        if dest_path.exists():
            print(f"⚠️  Project already exists in {category}")
            return False
        
        print(f"\n📦 Archiving: {project_name}")
        print(f"   From: {project_path}")
        print(f"   To: {dest_path}")
        
        if dry_run:
            print("   [DRY RUN] Would move project")
            return True
        
        try:
            shutil.move(str(project_path), str(dest_path))
            print("   ✅ Project archived successfully")
            return True
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False
    
    def restore_project(self, project_name, category, dry_run=True):
        """Restore a project from _ORGANIZED to NOIZYLAB"""
        if not self.organized.exists():
            print(f"❌ _ORGANIZED not found")
            return False
        
        source_path = self.organized / category / project_name
        if not source_path.exists():
            print(f"❌ Project not found: {category}/{project_name}")
            return False
        
        dest_path = self.noizylab / project_name
        
        if dest_path.exists():
            print(f"⚠️  Project already exists in NOIZYLAB")
            return False
        
        print(f"\n📦 Restoring: {project_name}")
        print(f"   From: {source_path}")
        print(f"   To: {dest_path}")
        
        if dry_run:
            print("   [DRY RUN] Would move project")
            return True
        
        try:
            shutil.move(str(source_path), str(dest_path))
            print("   ✅ Project restored successfully")
            return True
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False

def main():
    import sys
    
    print("=" * 80)
    print(" " * 25 + "SMART PROJECT MIGRATOR")
    print("=" * 80)
    
    migrator = SmartMigrator()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'find':
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 90
            migrator.find_archive_candidates(days)
        
        elif command == 'archive':
            if len(sys.argv) > 2:
                project = sys.argv[2]
                dry_run = '--dry-run' in sys.argv
                migrator.archive_project(project, dry_run)
            else:
                print("Usage: python3 SMART_MIGRATOR.py archive <project_name> [--dry-run]")
        
        elif command == 'restore':
            if len(sys.argv) > 3:
                project = sys.argv[2]
                category = sys.argv[3]
                dry_run = '--dry-run' in sys.argv
                migrator.restore_project(project, category, dry_run)
            else:
                print("Usage: python3 SMART_MIGRATOR.py restore <project_name> <category> [--dry-run]")
        
        else:
            print(f"Unknown command: {command}")
    else:
        print("\n🔍 Find archive candidates:")
        print("  python3 SMART_MIGRATOR.py find [days_inactive]")
        print("\n📦 Archive a project:")
        print("  python3 SMART_MIGRATOR.py archive <project_name> [--dry-run]")
        print("\n📥 Restore a project:")
        print("  python3 SMART_MIGRATOR.py restore <project_name> <category> [--dry-run]")
        
        print("\n💡 Quick example:")
        print("  python3 SMART_MIGRATOR.py find 90")

if __name__ == "__main__":
    main()

