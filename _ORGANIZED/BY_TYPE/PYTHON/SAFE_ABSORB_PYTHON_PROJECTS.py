#!/usr/bin/env python3
"""
SAFE ABSORPTION SYSTEM
Safely absorbs Python projects into NOIZYLAB with safety checks
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import subprocess

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
SOURCE = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🐍 Python_Projects")

class SafeAbsorptionSystem:
    def __init__(self):
        self.noizylab = NOIZYLAB
        self.source = SOURCE
        self.backup_dir = NOIZYLAB / ".absorption_backups"
        self.conflicts = []
        self.absorbed = []
        
    def check_safety(self):
        """Check if absorption is safe"""
        print("=" * 80)
        print(" " * 20 + "SAFETY CHECKS")
        print("=" * 80)
        print()
        
        safety_checks = {
            'noizylab_exists': self.noizylab.exists(),
            'source_exists': self.source.exists(),
            'has_backup_space': self.check_backup_space(),
            'can_write': self.check_write_permissions(),
        }
        
        print("🔍 Safety Checks:")
        all_safe = True
        
        for check, result in safety_checks.items():
            status = "✅" if result else "❌"
            print(f"   {status} {check.replace('_', ' ').title()}")
            if not result:
                all_safe = False
        
        if not all_safe:
            print("\n⚠️  Safety checks failed! Absorption may be unsafe.")
            return False
        
        print("\n✅ All safety checks passed!")
        return True
    
    def check_backup_space(self):
        """Check if we have space for backups"""
        try:
            stat = os.statvfs(self.noizylab)
            free_gb = (stat.f_avail * stat.f_frsize) / (1024**3)
            return free_gb > 10  # Need at least 10GB
        except:
            return False
    
    def check_write_permissions(self):
        """Check write permissions"""
        try:
            test_file = self.noizylab / ".write_test"
            test_file.touch()
            test_file.unlink()
            return True
        except:
            return False
    
    def detect_conflicts(self):
        """Detect conflicts before absorption"""
        print("\n" + "=" * 80)
        print(" " * 20 + "CONFLICT DETECTION")
        print("=" * 80)
        
        conflicts = []
        
        # Check each project in source
        for item in self.source.iterdir():
            if not item.is_dir() or item.name.startswith('.'):
                continue
            
            project_name = item.name
            noizylab_path = self.noizylab / project_name
            
            if noizylab_path.exists():
                conflicts.append({
                    'project': project_name,
                    'source': str(item),
                    'destination': str(noizylab_path),
                    'type': 'directory_exists'
                })
        
        self.conflicts = conflicts
        
        if conflicts:
            print(f"\n⚠️  Found {len(conflicts)} potential conflicts:")
            for conflict in conflicts:
                print(f"   • {conflict['project']} - Already exists in NOIZYLAB")
        else:
            print("\n✅ No conflicts detected!")
        
        return conflicts
    
    def create_backup(self, project_path):
        """Create backup before absorption"""
        backup_path = self.backup_dir / datetime.now().strftime("%Y%m%d_%H%M%S") / project_path.name
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            if project_path.exists():
                shutil.copytree(project_path, backup_path, dirs_exist_ok=True)
                return backup_path
        except Exception as e:
            print(f"   ⚠️  Backup failed: {e}")
        
        return None
    
    def safe_absorb_project(self, project_path, strategy='merge'):
        """Safely absorb a project with conflict resolution"""
        project_name = project_path.name
        dest_path = self.noizylab / project_name
        
        print(f"\n🔗 Absorbing: {project_name}")
        
        # Create backup first
        print("   📦 Creating backup...")
        backup = self.create_backup(dest_path if dest_path.exists() else project_path)
        if backup:
            print(f"   ✅ Backup: {backup}")
        
        # Strategy: merge, overwrite, or skip
        if dest_path.exists():
            if strategy == 'merge':
                print("   🔀 Merging (copying new files only)...")
                self.merge_project(project_path, dest_path)
            elif strategy == 'overwrite':
                print("   ⚠️  Overwriting existing...")
                shutil.rmtree(dest_path)
                shutil.copytree(project_path, dest_path)
            else:
                print("   ⏭️  Skipping (already exists)")
                return False
        else:
            print("   📥 Copying project...")
            shutil.copytree(project_path, dest_path)
        
        self.absorbed.append({
            'project': project_name,
            'source': str(project_path),
            'destination': str(dest_path),
            'backup': str(backup) if backup else None,
            'timestamp': datetime.now().isoformat()
        })
        
        print("   ✅ Absorbed successfully!")
        return True
    
    def merge_project(self, source, dest):
        """Merge project files safely"""
        for root, dirs, files in os.walk(source):
            # Skip hidden/system dirs
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
            
            rel_path = Path(root).relative_to(source)
            dest_dir = dest / rel_path
            
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                src_file = Path(root) / file
                dst_file = dest_dir / file
                
                # Only copy if doesn't exist or source is newer
                if not dst_file.exists():
                    shutil.copy2(src_file, dst_file)
                elif src_file.stat().st_mtime > dst_file.stat().st_mtime:
                    # Source is newer - backup destination first
                    backup_file = dst_file.with_suffix(dst_file.suffix + '.bak')
                    shutil.copy2(dst_file, backup_file)
                    shutil.copy2(src_file, dst_file)
    
    def validate_integration(self):
        """Validate that absorption won't break things"""
        print("\n" + "=" * 80)
        print(" " * 20 + "INTEGRATION VALIDATION")
        print("=" * 80)
        
        # Check for critical files that shouldn't conflict
        critical_paths = [
            'GO.sh',
            'ULTIMATE_SYSTEM.sh',
            'scripts',
            'training',
            'mc96'
        ]
        
        issues = []
        for critical in critical_paths:
            critical_path = self.noizylab / critical
            if not critical_path.exists():
                issues.append(f"Missing critical: {critical}")
        
        if issues:
            print("⚠️  Validation issues:")
            for issue in issues:
                print(f"   • {issue}")
            return False
        
        print("✅ Integration validation passed!")
        return True
    
    def safe_absorb_all(self, dry_run=True):
        """Safely absorb all projects"""
        print("=" * 80)
        print(" " * 20 + "SAFE ABSORPTION SYSTEM")
        print("=" * 80)
        print()
        
        # Safety checks
        if not self.check_safety():
            print("\n❌ Safety checks failed. Aborting.")
            return
        
        # Conflict detection
        conflicts = self.detect_conflicts()
        
        # Integration validation
        if not self.validate_integration():
            print("\n⚠️  Integration validation failed. Review before proceeding.")
        
        if dry_run:
            print("\n⚠️  DRY RUN MODE - No files will be absorbed")
            print("   Add --live to actually absorb\n")
            return
        
        # Create backup directory
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Absorb projects
        print("\n" + "=" * 80)
        print(" " * 20 + "ABSORBING PROJECTS")
        print("=" * 80)
        
        for item in self.source.iterdir():
            if not item.is_dir() or item.name.startswith('.'):
                continue
            
            # Use merge strategy for conflicts
            strategy = 'merge' if any(c['project'] == item.name for c in conflicts) else 'copy'
            self.safe_absorb_project(item, strategy=strategy)
        
        # Create absorption manifest
        manifest = {
            'timestamp': datetime.now().isoformat(),
            'absorbed_projects': self.absorbed,
            'conflicts_resolved': len(conflicts),
            'backup_location': str(self.backup_dir)
        }
        
        manifest_path = self.noizylab / ".ABSORPTION_MANIFEST.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print("\n" + "=" * 80)
        print("✅ SAFE ABSORPTION COMPLETE!")
        print("=" * 80)
        print(f"Projects absorbed: {len(self.absorbed)}")
        print(f"Backup location: {self.backup_dir}")
        print(f"Manifest: {manifest_path}")
        print()

def main():
    import sys
    
    dry_run = '--live' not in sys.argv
    
    absorber = SafeAbsorptionSystem()
    absorber.safe_absorb_all(dry_run=dry_run)

if __name__ == "__main__":
    main()

