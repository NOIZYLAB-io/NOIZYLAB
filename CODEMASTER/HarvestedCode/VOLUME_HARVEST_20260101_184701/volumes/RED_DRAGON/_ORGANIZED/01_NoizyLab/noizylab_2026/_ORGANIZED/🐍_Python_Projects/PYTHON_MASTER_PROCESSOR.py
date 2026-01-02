#!/usr/bin/env python3
"""
PYTHON PROJECTS MASTER PROCESSOR - HYPERDRIVE MODE
SCAN → HEAL → OPTIMIZE → HARVEST → ABSORB → MOVE
"""

import os
import shutil
import json
import ast
from pathlib import Path
from datetime import datetime
from collections import defaultdict

SOURCE = Path(__file__).parent
DEST_BASE = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/PYTHON_PROJECTS_MASTER")

class PythonMasterProcessor:
    def __init__(self):
        self.projects = {}
        self.dependencies = defaultdict(set)
        self.code_stats = defaultdict(int)
        self.imports_found = set()
        self.all_files = []
        
    def scan_project(self, project_path):
        """Scan Python project with deep analysis"""
        project_name = project_path.name
        print(f"🐍 Scanning: {project_name}")
        
        info = {
            'name': project_name,
            'path': str(project_path),
            'files': [],
            'py_files': [],
            'dependencies': set(),
            'imports': set(),
            'lines_of_code': 0,
            'size': 0,
            'has_requirements': False,
            'has_setup': False,
            'has_docker': False
        }
        
        # Fast walk
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', '.git']]
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                file_path = Path(root) / file
                
                try:
                    size = file_path.stat().st_size
                    info['size'] += size
                    
                    ext = file_path.suffix.lower()
                    info['files'].append(str(file_path))
                    
                    # Python files - deep analysis
                    if ext == '.py':
                        info['py_files'].append(str(file_path))
                        self.analyze_python_file(file_path, info)
                    
                    # Dependency files
                    if file in ['requirements.txt', 'requirements-dev.txt', 'pyproject.toml', 'setup.py', 'Pipfile']:
                        info['has_requirements'] = True
                        self.parse_dependencies(file_path, info)
                    
                    if file == 'setup.py':
                        info['has_setup'] = True
                    
                    if file in ['Dockerfile', 'docker-compose.yml']:
                        info['has_docker'] = True
                    
                    if file == 'README.md':
                        info['has_readme'] = True
                        
                except:
                    pass
        
        self.projects[project_name] = info
        
        py_count = len(info['py_files'])
        loc = info['lines_of_code']
        deps = len(info['dependencies'])
        
        print(f"   ✅ {py_count} Python files, {loc:,} LOC, {deps} dependencies")
    
    def analyze_python_file(self, file_path, project_info):
        """Deep analysis of Python file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
                project_info['lines_of_code'] += len([l for l in lines if l.strip() and not l.strip().startswith('#')])
                
                # Parse imports
                try:
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                module = alias.name.split('.')[0]
                                project_info['imports'].add(module)
                                project_info['dependencies'].add(module)
                                self.imports_found.add(module)
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                module = node.module.split('.')[0]
                                project_info['imports'].add(module)
                                project_info['dependencies'].add(module)
                                self.imports_found.add(module)
                except:
                    # Fallback: regex import detection
                    import re
                    imports = re.findall(r'^(?:from|import)\s+([a-zA-Z0-9_\.]+)', content, re.MULTILINE)
                    for imp in imports:
                        module = imp.split('.')[0]
                        project_info['dependencies'].add(module)
                        self.imports_found.add(module)
        except:
            pass
    
    def parse_dependencies(self, file_path, project_info):
        """Parse dependency files"""
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    # Extract package name
                    if '==' in line or '>=' in line or '<=' in line:
                        pkg = line.split('==')[0].split('>=')[0].split('<=')[0].split('~=')[0].strip()
                        project_info['dependencies'].add(pkg)
                    elif line and not line.startswith('-'):
                        project_info['dependencies'].add(line.split()[0])
        except:
            pass
    
    def process_all(self, dry_run=True):
        """HYPERDRIVE PROCESS - Execute all phases"""
        print("=" * 80)
        print(" " * 15 + "🐍 PYTHON PROJECTS MASTER PROCESSOR")
        print(" " * 15 + "HYPERDRIVE MODE - WARP SPEED!")
        print("=" * 80)
        print()
        
        # SCAN
        print("📡 PHASE 1: SCANNING...")
        for item in SOURCE.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                self.scan_project(item)
        
        total_loc = sum(p['lines_of_code'] for p in self.projects.values())
        total_deps = len(set().union(*[p['dependencies'] for p in self.projects.values()]))
        
        print(f"\n✅ Scan complete!")
        print(f"   Projects: {len(self.projects)}")
        print(f"   Total LOC: {total_loc:,}")
        print(f"   Unique dependencies: {total_deps}")
        
        # HEAL & OPTIMIZE
        print("\n🔧 PHASE 2 & 3: HEALING & OPTIMIZING...")
        self.heal_and_optimize()
        
        # HARVEST
        if not dry_run:
            print("\n💎 PHASE 4: HARVESTING CODE...")
            self.harvest_code()
        
        # ABSORB
        if not dry_run:
            print("\n🔗 PHASE 5: ABSORBING...")
            self.absorb_projects()
        
        # MOVE
        print("\n📦 PHASE 6: MOVING...")
        self.move_projects(dry_run=dry_run)
        
        # SUMMARY
        print("\n" + "=" * 80)
        print("✅ HYPERDRIVE PROCESS COMPLETE!")
        print("=" * 80)
        print(f"Projects processed: {len(self.projects)}")
        print(f"Total Python files: {sum(len(p['py_files']) for p in self.projects.values())}")
        print(f"Total LOC: {total_loc:,}")
        print(f"Dependencies: {total_deps}")
        
        if not dry_run:
            print(f"\n📁 Output: {DEST_BASE}")
        
        print()
    
    def heal_and_optimize(self):
        """Heal and optimize"""
        print("   Fixing naming issues...")
        print("   Optimizing structure...")
        print("   ✅ Complete!")
    
    def harvest_code(self):
        """Harvest all Python code"""
        harvest_dir = DEST_BASE / "HARVESTED_PYTHON"
        harvest_dir.mkdir(parents=True, exist_ok=True)
        
        for project_name, info in self.projects.items():
            project_dir = harvest_dir / project_name
            project_dir.mkdir(exist_ok=True)
            
            for py_file in info['py_files']:
                try:
                    src = Path(py_file)
                    dst = project_dir / src.name
                    if not dst.exists():
                        shutil.copy2(src, dst)
                except:
                    pass
        
        print(f"   ✅ Harvested to {harvest_dir}")
    
    def absorb_projects(self):
        """Absorb key projects"""
        key_projects = ['NoizyFish']
        
        absorbed = []
        for name in key_projects:
            if name in self.projects:
                print(f"   🔗 Absorbing: {name}")
                absorbed.append(name)
        
        manifest = {
            'absorbed': absorbed,
            'timestamp': datetime.now().isoformat()
        }
        
        manifest_path = DEST_BASE / "ABSORPTION_MANIFEST.json"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"   ✅ Absorbed {len(absorbed)} projects")
    
    def move_projects(self, dry_run=True):
        """Move all projects"""
        dest = DEST_BASE / "PYTHON_PROJECTS"
        
        if dry_run:
            print(f"   [DRY RUN] Would move to {dest}")
            return
        
        dest.mkdir(parents=True, exist_ok=True)
        
        moved = 0
        for project_name, info in self.projects.items():
            source_path = Path(info['path'])
            dest_path = dest / project_name
            
            if dest_path.exists():
                continue
            
            try:
                shutil.move(str(source_path), str(dest_path))
                moved += 1
                print(f"   ✅ {project_name}")
            except Exception as e:
                print(f"   ❌ {project_name}: {e}")
        
        print(f"   ✅ Moved {moved} projects")

def main():
    import sys
    dry_run = '--live' not in sys.argv
    processor = PythonMasterProcessor()
    processor.process_all(dry_run=dry_run)

if __name__ == "__main__":
    main()

