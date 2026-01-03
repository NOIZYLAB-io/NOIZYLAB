#!/usr/bin/env python3
"""
PROJECT MASTER PROCESSOR
SCAN → HEAL → OPTIMIZE → HARVEST → ABSORB → MOVE
Complete workflow for _noizy_projects
"""

import os
import shutil
import hashlib
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

SOURCE = Path(__file__).parent
DEST_BASE = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/NOIZY_PROJECTS_MASTER")

class ProjectMasterProcessor:
    def __init__(self):
        self.stats = defaultdict(int)
        self.duplicates = []
        self.naming_issues = []
        self.corrupt_files = []
        self.empty_dirs = []
        self.projects = {}
        self.code_files = defaultdict(list)
        self.assets = defaultdict(list)
        self.dependencies = defaultdict(set)
        self.db_path = SOURCE / ".project_intelligence.db"
        self.init_database()
    
    def init_database(self):
        """Initialize project intelligence database"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                language TEXT,
                framework TEXT,
                location TEXT,
                file_count INTEGER,
                size INTEGER,
                dependencies TEXT,
                status TEXT,
                last_modified TIMESTAMP,
                harvested BOOLEAN DEFAULT 0,
                absorbed BOOLEAN DEFAULT 0
            )
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS code_harvest (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER,
                file_path TEXT,
                file_type TEXT,
                language TEXT,
                lines_of_code INTEGER,
                complexity REAL,
                harvested_at TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def scan_all_projects(self):
        """PHASE 1: SCAN - Analyze all projects"""
        print("=" * 80)
        print(" " * 20 + "PHASE 1: SCANNING ALL PROJECTS")
        print("=" * 80)
        print(f"Source: {SOURCE}")
        print()
        
        for item in SOURCE.iterdir():
            if item.name.startswith('.'):
                continue
            
            if item.is_dir():
                self.scan_project(item)
            elif item.is_file():
                self.scan_file(item)
        
        print(f"\n✅ Scan complete!")
        print(f"   Projects found: {len(self.projects)}")
        print(f"   Total files: {self.stats['total_files']:,}")
        print(f"   Total size: {self.stats['total_size'] / (1024**3):.2f} GB")
    
    def scan_project(self, project_path):
        """Scan individual project"""
        project_name = project_path.name
        print(f"📦 Scanning: {project_name}")
        
        project_info = {
            'name': project_name,
            'path': str(project_path),
            'type': self.detect_project_type(project_path),
            'files': [],
            'file_count': 0,
            'size': 0,
            'languages': set(),
            'frameworks': set(),
            'dependencies': set(),
            'issues': []
        }
        
        # Scan files
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]
            
            for file in files:
                file_path = Path(root) / file
                self.stats['total_files'] += 1
                
                try:
                    size = file_path.stat().st_size
                    project_info['size'] += size
                    self.stats['total_size'] += size
                    
                    ext = file_path.suffix.lower()
                    
                    # Detect language/framework
                    lang = self.detect_language(file_path, ext)
                    if lang:
                        project_info['languages'].add(lang)
                    
                    framework = self.detect_framework(file_path, ext)
                    if framework:
                        project_info['frameworks'].add(framework)
                    
                    # Check for duplicates
                    if size < 10 * 1024 * 1024:  # < 10MB
                        file_hash = self.quick_hash(file_path)
                        if file_hash:
                            self.check_duplicate(file_path, file_hash, size)
                    
                    # Categorize
                    if ext in ['.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rs', '.cpp', '.c']:
                        self.code_files[lang or 'unknown'].append(file_path)
                    elif ext in ['.json', '.yaml', '.yml', '.toml']:
                        self.dependencies[project_name].add(file_path)
                    
                    project_info['files'].append({
                        'path': str(file_path),
                        'size': size,
                        'type': ext
                    })
                    project_info['file_count'] += 1
                    
                except Exception as e:
                    self.corrupt_files.append({
                        'path': str(file_path),
                        'error': str(e)
                    })
                    project_info['issues'].append(f"Corrupt: {file}")
        
        # Detect project type
        project_info['type'] = self.detect_project_type(project_path)
        
        # Check for empty directories
        if project_info['file_count'] == 0:
            self.empty_dirs.append(str(project_path))
        
        self.projects[project_name] = project_info
    
    def scan_file(self, file_path):
        """Scan standalone file"""
        try:
            size = file_path.stat().st_size
            self.stats['total_files'] += 1
            self.stats['total_size'] += size
        except:
            pass
    
    def detect_project_type(self, project_path):
        """Detect project type"""
        files = list(project_path.glob('*'))
        
        if any(f.name in ['package.json', 'node_modules'] for f in files):
            return 'nodejs'
        if any(f.name in ['requirements.txt', 'setup.py', 'Pipfile', 'pyproject.toml'] for f in files):
            return 'python'
        if any(f.name in ['go.mod', 'go.sum'] for f in files):
            return 'go'
        if any(f.name in ['Cargo.toml'] for f in files):
            return 'rust'
        if any(f.name in ['pom.xml', 'build.gradle'] for f in files):
            return 'java'
        if any(f.name in ['Makefile', 'CMakeLists.txt'] for f in files):
            return 'c_cpp'
        if any(f.name in ['docker-compose.yml', 'Dockerfile'] for f in files):
            return 'docker'
        
        return 'unknown'
    
    def detect_language(self, file_path, ext):
        """Detect programming language"""
        lang_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'javascript',
            '.tsx': 'typescript',
            '.java': 'java',
            '.go': 'go',
            '.rs': 'rust',
            '.cpp': 'cpp',
            '.c': 'c',
            '.sh': 'bash',
            '.rb': 'ruby',
            '.php': 'php'
        }
        return lang_map.get(ext)
    
    def detect_framework(self, file_path, ext):
        """Detect framework"""
        name = file_path.name.lower()
        path_str = str(file_path).lower()
        
        if 'react' in name or 'react' in path_str:
            return 'react'
        if 'vue' in name:
            return 'vue'
        if 'angular' in name:
            return 'angular'
        if 'next' in name:
            return 'nextjs'
        if 'express' in name:
            return 'express'
        if 'django' in name:
            return 'django'
        if 'flask' in name:
            return 'flask'
        if 'fastapi' in name:
            return 'fastapi'
        
        return None
    
    def quick_hash(self, file_path):
        """Quick hash for duplicate detection"""
        try:
            md5 = hashlib.md5()
            with open(file_path, 'rb') as f:
                md5.update(f.read(min(1024 * 1024, file_path.stat().st_size)))
                md5.update(str(file_path.stat().st_size).encode())
            return md5.hexdigest()
        except:
            return None
    
    def check_duplicate(self, file_path, file_hash, size):
        """Check for duplicate files"""
        if not hasattr(self, 'file_hashes'):
            self.file_hashes = {}
        
        if file_hash in self.file_hashes:
            self.duplicates.append({
                'original': self.file_hashes[file_hash],
                'duplicate': str(file_path),
                'size': size
            })
        else:
            self.file_hashes[file_hash] = str(file_path)
    
    def heal_issues(self):
        """PHASE 2: HEAL - Fix issues"""
        print("\n" + "=" * 80)
        print(" " * 20 + "PHASE 2: HEALING ISSUES")
        print("=" * 80)
        
        healed = 0
        
        # Fix naming issues
        print(f"\n📝 Fixing naming issues...")
        for file_path in list(self.naming_issues)[:100]:  # Limit
            try:
                path = Path(file_path)
                new_name = path.name.strip().replace('  ', ' ')
                if new_name != path.name:
                    new_path = path.parent / new_name
                    if not new_path.exists():
                        path.rename(new_path)
                        healed += 1
            except:
                pass
        
        print(f"   ✅ Fixed {healed} naming issues")
        
        # Report issues
        if self.duplicates:
            dup_size = sum(d['size'] for d in self.duplicates) / (1024**3)
            print(f"\n🔄 Duplicates: {len(self.duplicates)} ({dup_size:.2f} GB)")
        
        if self.corrupt_files:
            print(f"\n⚠️  Corrupt files: {len(self.corrupt_files)}")
        
        if self.empty_dirs:
            print(f"\n📁 Empty directories: {len(self.empty_dirs)}")
        
        print(f"\n✅ Healing complete!")
    
    def optimize_structure(self):
        """PHASE 3: OPTIMIZE - Organize structure"""
        print("\n" + "=" * 80)
        print(" " * 20 + "PHASE 3: OPTIMIZING STRUCTURE")
        print("=" * 80)
        
        print(f"\n📊 Project Analysis:")
        print(f"   Total projects: {len(self.projects)}")
        
        # Group by type
        by_type = defaultdict(list)
        for name, info in self.projects.items():
            by_type[info['type']].append(name)
        
        print(f"\n📁 Projects by Type:")
        for ptype, projects in sorted(by_type.items()):
            print(f"   • {ptype:15s} - {len(projects):3} projects")
        
        # Language distribution
        all_langs = set()
        for info in self.projects.values():
            all_langs.update(info['languages'])
        
        print(f"\n💻 Languages Used:")
        for lang in sorted(all_langs):
            count = sum(1 for info in self.projects.values() if lang in info['languages'])
            print(f"   • {lang:15s} - {count:3} projects")
        
        print(f"\n✅ Structure analyzed!")
    
    def harvest_code(self):
        """PHASE 4: HARVEST - Extract valuable code"""
        print("\n" + "=" * 80)
        print(" " * 20 + "PHASE 4: HARVESTING CODE")
        print("=" * 80)
        
        harvest_dir = DEST_BASE / "HARVESTED_CODE"
        harvest_dir.mkdir(parents=True, exist_ok=True)
        
        harvested = 0
        
        for lang, files in self.code_files.items():
            if not files:
                continue
            
            lang_dir = harvest_dir / lang
            lang_dir.mkdir(exist_ok=True)
            
            print(f"\n💎 Harvesting {lang} code...")
            print(f"   Files: {len(files)}")
            
            for file_path in files[:100]:  # Limit per language
                try:
                    # Copy to harvested location
                    rel_path = file_path.relative_to(SOURCE)
                    dest_path = lang_dir / rel_path.name
                    
                    if not dest_path.exists():
                        shutil.copy2(file_path, dest_path)
                        harvested += 1
                except:
                    pass
        
        print(f"\n✅ Harvested {harvested} code files")
    
    def absorb_to_system(self):
        """PHASE 5: ABSORB - Integrate into main system"""
        print("\n" + "=" * 80)
        print(" " * 20 + "PHASE 5: ABSORBING INTO SYSTEM")
        print("=" * 80)
        
        # Identify key projects to absorb
        key_projects = [
            'NoizyFish',
            'noizy_agents',
            'noizy_genie_ms',
            'rituals',
            'scripts'
        ]
        
        absorbed = []
        
        for project_name in key_projects:
            if project_name in self.projects:
                project = self.projects[project_name]
                print(f"\n🔗 Absorbing: {project_name}")
                print(f"   Type: {project['type']}")
                print(f"   Languages: {', '.join(project['languages'])}")
                absorbed.append(project_name)
        
        print(f"\n✅ Absorbed {len(absorbed)} key projects")
        
        # Save absorption manifest
        manifest = {
            'absorbed_projects': absorbed,
            'timestamp': datetime.now().isoformat(),
            'location': str(DEST_BASE)
        }
        
        manifest_path = DEST_BASE / "ABSORPTION_MANIFEST.json"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"   Manifest: {manifest_path}")
    
    def move_to_master(self, dry_run=True):
        """PHASE 6: MOVE - Move to organized location"""
        print("\n" + "=" * 80)
        print(" " * 20 + "PHASE 6: MOVING TO MASTER")
        print("=" * 80)
        
        dest = DEST_BASE / "PROJECTS"
        
        print(f"\n📦 Moving all projects...")
        print(f"   Source: {SOURCE}")
        print(f"   Destination: {dest}")
        
        if dry_run:
            print(f"   [DRY RUN] Would move {len(self.projects)} projects")
            return
        
        dest.mkdir(parents=True, exist_ok=True)
        
        moved = 0
        
        for project_name, project_info in self.projects.items():
            source_path = Path(project_info['path'])
            dest_path = dest / project_name
            
            if dest_path.exists():
                continue
            
            try:
                shutil.move(str(source_path), str(dest_path))
                moved += 1
                print(f"   ✅ {project_name}")
            except Exception as e:
                print(f"   ❌ {project_name}: {e}")
        
        print(f"\n✅ Moved {moved} projects")
    
    def process_all(self, dry_run=True):
        """Execute complete workflow"""
        print("=" * 80)
        print(" " * 15 + "PROJECT MASTER PROCESSOR")
        print(" " * 15 + "SCAN → HEAL → OPTIMIZE → HARVEST → ABSORB → MOVE")
        print("=" * 80)
        print()
        
        if dry_run:
            print("⚠️  DRY RUN MODE\n")
        
        # Phase 1: SCAN
        self.scan_all_projects()
        
        # Phase 2: HEAL
        self.heal_issues()
        
        # Phase 3: OPTIMIZE
        self.optimize_structure()
        
        # Phase 4: HARVEST
        if not dry_run:
            self.harvest_code()
        
        # Phase 5: ABSORB
        if not dry_run:
            self.absorb_to_system()
        
        # Phase 6: MOVE
        self.move_to_master(dry_run=dry_run)
        
        # Final Summary
        print("\n" + "=" * 80)
        print(" " * 20 + "COMPLETE SUMMARY")
        print("=" * 80)
        print(f"Projects processed: {len(self.projects)}")
        print(f"Total files: {self.stats['total_files']:,}")
        print(f"Total size: {self.stats['total_size'] / (1024**3):.2f} GB")
        print(f"Duplicates: {len(self.duplicates)}")
        print(f"Code files harvested: {sum(len(files) for files in self.code_files.values())}")
        
        if not dry_run:
            print(f"\n✅ All phases complete!")
            print(f"   Location: {DEST_BASE}")
        
        print()

def main():
    import sys
    
    dry_run = '--live' not in sys.argv
    
    processor = ProjectMasterProcessor()
    processor.process_all(dry_run=dry_run)

if __name__ == "__main__":
    main()

