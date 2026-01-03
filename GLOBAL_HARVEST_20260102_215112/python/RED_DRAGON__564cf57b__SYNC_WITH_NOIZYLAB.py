#!/usr/bin/env python3
"""
Sync System between _ORGANIZED and NOIZYLAB
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

ORGANIZED = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")
NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
SYNC_CONFIG = ORGANIZED / ".sync_config.json"

class OrganizedSync:
    def __init__(self):
        self.organized = ORGANIZED
        self.noizylab = NOIZYLAB
        self.sync_config = SYNC_CONFIG
        
        # Load sync config
        if self.sync_config.exists():
            with open(self.sync_config) as f:
                self.config = json.load(f)
        else:
            self.config = {
                'sync_history': [],
                'mappings': {}
            }
    
    def find_noizylab_projects(self):
        """Find projects in NOIZYLAB that should be synced"""
        print("🔍 Finding projects in NOIZYLAB...")
        print("=" * 80)
        
        projects = []
        
        if not self.noizylab.exists():
            print(f"❌ NOIZYLAB not found: {self.noizylab}")
            return projects
        
        # Find top-level directories that look like projects
        for item in self.noizylab.iterdir():
            if item.is_dir():
                # Skip system directories
                if item.name.startswith('.') or item.name in ['node_modules', 'scripts', 'docs', 'logs', 'backups']:
                    continue
                
                # Check if it looks like a project (has files, not just config)
                has_code = False
                for file in item.rglob('*'):
                    if file.is_file():
                        ext = file.suffix.lower()
                        if ext in ['.py', '.js', '.ts', '.rb', '.rs', '.go', '.java', '.cpp', '.c']:
                            has_code = True
                            break
                
                if has_code:
                    projects.append({
                        'name': item.name,
                        'path': str(item),
                        'size': self.get_dir_size(item)
                    })
        
        print(f"Found {len(projects)} projects in NOIZYLAB:\n")
        for i, project in enumerate(projects[:20], 1):
            size_mb = project['size'] / (1024 * 1024)
            print(f"  {i:2}. {project['name']:30s} ({size_mb:.1f} MB)")
        
        return projects
    
    def find_organized_projects(self):
        """Find all projects in _ORGANIZED"""
        print("\n🔍 Finding projects in _ORGANIZED...")
        print("=" * 80)
        
        projects = []
        
        if not self.organized.exists():
            print(f"❌ _ORGANIZED not found: {self.organized}")
            return projects
        
        # Load catalog if available
        catalog_file = self.organized / ".catalog.json"
        if catalog_file.exists():
            with open(catalog_file) as f:
                catalog = json.load(f)
                projects = list(catalog.get('projects', {}).keys())
                print(f"Found {len(projects)} projects from catalog")
        else:
            # Scan manually
            for category in self.organized.iterdir():
                if category.is_dir() and not category.name.startswith('.'):
                    for project in category.iterdir():
                        if project.is_dir():
                            projects.append({
                                'name': project.name,
                                'category': category.name,
                                'path': str(project)
                            })
            print(f"Found {len(projects)} projects")
        
        return projects
    
    def suggest_sync_candidates(self):
        """Suggest projects that could be synced"""
        print("\n" + "=" * 80)
        print("🔄 SYNC CANDIDATES")
        print("=" * 80)
        
        noizylab_projects = self.find_noizylab_projects()
        organized_projects = self.find_organized_projects()
        
        # Extract names from organized projects
        organized_names = set()
        if organized_projects:
            if isinstance(organized_projects[0], dict):
                organized_names = {p['name'] for p in organized_projects}
            else:
                organized_names = set(organized_projects)
        
        # Find projects in NOIZYLAB not in _ORGANIZED
        candidates = []
        for project in noizylab_projects:
            if project['name'] not in organized_names:
                candidates.append(project)
        
        if candidates:
            print(f"\n💡 Found {len(candidates)} projects in NOIZYLAB not in _ORGANIZED:\n")
            for i, project in enumerate(candidates, 1):
                size_mb = project['size'] / (1024 * 1024)
                print(f"  {i:2}. {project['name']:30s} ({size_mb:.1f} MB)")
            
            print("\n📝 These projects could be archived to _ORGANIZED")
        else:
            print("\n✅ All NOIZYLAB projects are already in _ORGANIZED")
        
        return candidates
    
    def get_dir_size(self, path):
        """Get directory size"""
        total = 0
        try:
            for item in path.rglob('*'):
                if item.is_file():
                    total += item.stat().st_size
        except:
            pass
        return total
    
    def detect_category(self, project_path):
        """Detect appropriate category for a project"""
        project_path = Path(project_path)
        
        # Count file types
        file_types = {}
        for file in project_path.rglob('*'):
            if file.is_file():
                ext = file.suffix.lower()
                file_types[ext] = file_types.get(ext, 0) + 1
        
        # Determine category based on file types
        if file_types.get('.py', 0) > file_types.get('.js', 0):
            return '🐍 Python_Projects'
        elif file_types.get('.js', 0) > 0 or file_types.get('.ts', 0) > 0:
            return '🚀 Production_Projects'
        elif file_types.get('.rb', 0) > 0:
            return '💎 Ruby_Projects'
        elif file_types.get('.rs', 0) > 0:
            return '🦀 Rust_Projects'
        elif file_types.get('.go', 0) > 0:
            return '🐹 Go_Projects'
        else:
            return '🔧 Tools_And_Utilities'
    
    def save_config(self):
        """Save sync configuration"""
        with open(self.sync_config, 'w') as f:
            json.dump(self.config, f, indent=2)

def main():
    print("=" * 80)
    print(" " * 25 + "_ORGANIZED ↔ NOIZYLAB SYNC")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    sync = OrganizedSync()
    sync.suggest_sync_candidates()
    
    print("\n" + "=" * 80)
    print("✅ Analysis complete!")
    print("=" * 80)
    print("\n💡 To archive a project:")
    print("   1. Identify project to archive")
    print("   2. Choose appropriate category in _ORGANIZED")
    print("   3. Move or copy project to that category")

if __name__ == "__main__":
    main()

