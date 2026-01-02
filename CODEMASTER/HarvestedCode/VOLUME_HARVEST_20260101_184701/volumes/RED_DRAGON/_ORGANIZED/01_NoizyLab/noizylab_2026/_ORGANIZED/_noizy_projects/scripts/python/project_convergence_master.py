#!/usr/bin/env python3
"""
🧞‍♂️🗂️ PROJECT CONVERGENCE MASTER 📁✨
=====================================
The ultimate script to gather all scattered projects!
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

class ProjectConvergenceMaster:
    def __init__(self):
        self.home_dir = Path.home()
        self.master_workspace = self.home_dir / "NoizyGenie_Master_Workspace"
        self.common_project_locations = [
            self.home_dir / "Desktop",
            self.home_dir / "Documents",
            self.home_dir / "Downloads", 
            self.home_dir / "Developer",
            self.home_dir / "Projects",
            self.home_dir / "Code",
            self.home_dir / "Workspace",
            self.home_dir / "Scripts",
            self.home_dir / "RSP",
            Path("/Users/rsp_ms/RSP/Scripts")
        ]
        
        self.project_indicators = [
            ".git", ".vscode", "package.json", "requirements.txt", 
            "Cargo.toml", "pom.xml", "build.gradle", "composer.json",
            "Gemfile", "go.mod", "main.py", "main.js", "index.html",
            "README.md", "Makefile", ".gitignore"
        ]
        
    def create_master_workspace(self):
        """Create the ultimate master workspace structure"""
        print("🏗️ CREATING MASTER WORKSPACE STRUCTURE...")
        
        workspace_structure = {
            "🐍 Python_Projects": "All Python applications and scripts",
            "🌟 JavaScript_Projects": "Node.js, React, Vue, and JS projects", 
            "🦀 Rust_Projects": "Rust applications and libraries",
            "☕ Java_Projects": "Java applications and Spring projects",
            "💎 Ruby_Projects": "Ruby on Rails and Ruby scripts",
            "🐹 Go_Projects": "Go applications and microservices",
            "🌐 Web_Projects": "HTML, CSS, Frontend projects",
            "🤖 AI_ML_Projects": "Machine Learning and AI projects",
            "🎮 Game_Projects": "Game development projects",
            "📱 Mobile_Projects": "iOS, Android, React Native",
            "🐳 DevOps_Projects": "Docker, Kubernetes, CI/CD",
            "📊 Data_Projects": "Data analysis and visualization",
            "🧞‍♂️ NoizyGenie_Creations": "All our magical creations",
            "💰 Billion_Dollar_Ideas": "Trillion dollar concepts",
            "🔧 Tools_And_Utilities": "Helper scripts and tools",
            "📚 Learning_Projects": "Tutorials and experiments",
            "🚀 Production_Projects": "Live applications",
            "🧪 Experimental": "Proof of concepts and tests"
        }
        
        self.master_workspace.mkdir(exist_ok=True)
        
        for folder, description in workspace_structure.items():
            folder_path = self.master_workspace / folder
            folder_path.mkdir(exist_ok=True)
            
            # Create description file
            desc_file = folder_path / "README.md"
            desc_file.write_text(f"# {folder}\n\n{description}\n\n*Organized by NoizyGenie Project Convergence Master* 🧞‍♂️")
            
            print(f"   ✅ {folder}")
            
    def scan_for_projects(self):
        """Scan all common locations for projects"""
        print("\n🔍 SCANNING FOR SCATTERED PROJECTS...")
        found_projects = []
        
        for location in self.common_project_locations:
            if location.exists():
                print(f"   🔍 Scanning: {location}")
                projects = self._find_projects_in_directory(location)
                found_projects.extend(projects)
                
        return found_projects
    
    def _find_projects_in_directory(self, directory):
        """Find projects in a specific directory"""
        projects = []
        
        try:
            for item in directory.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    # Check if it's a project directory
                    if self._is_project_directory(item):
                        project_type = self._detect_project_type(item)
                        projects.append({
                            'path': item,
                            'name': item.name,
                            'type': project_type,
                            'size': self._get_directory_size(item)
                        })
                        
        except PermissionError:
            pass  # Skip directories we can't access
            
        return projects
    
    def _is_project_directory(self, path):
        """Check if directory contains project indicators"""
        for indicator in self.project_indicators:
            if (path / indicator).exists():
                return True
        return False
    
    def _detect_project_type(self, path):
        """Detect the type of project"""
        if (path / "package.json").exists():
            return "🌟 JavaScript_Projects"
        elif (path / "requirements.txt").exists() or any(f.suffix == '.py' for f in path.glob('*.py')):
            return "🐍 Python_Projects"
        elif (path / "Cargo.toml").exists():
            return "🦀 Rust_Projects"
        elif (path / "pom.xml").exists() or (path / "build.gradle").exists():
            return "☕ Java_Projects"
        elif (path / "Gemfile").exists():
            return "💎 Ruby_Projects"
        elif (path / "go.mod").exists():
            return "🐹 Go_Projects"
        elif any(f.suffix in ['.html', '.css'] for f in path.glob('*')):
            return "🌐 Web_Projects"
        elif any(name in path.name.lower() for name in ['ai', 'ml', 'machine', 'neural', 'tensorflow', 'pytorch']):
            return "🤖 AI_ML_Projects"
        elif any(name in path.name.lower() for name in ['game', 'unity', 'unreal']):
            return "🎮 Game_Projects"
        elif any(name in path.name.lower() for name in ['mobile', 'android', 'ios', 'flutter']):
            return "📱 Mobile_Projects"
        elif any(name in path.name.lower() for name in ['docker', 'kubernetes', 'devops', 'ci', 'cd']):
            return "🐳 DevOps_Projects"
        elif any(name in path.name.lower() for name in ['data', 'analysis', 'visualization']):
            return "📊 Data_Projects"
        elif any(name in path.name.lower() for name in ['noizygenie', 'genie', 'trillion', 'bionic']):
            return "🧞‍♂️ NoizyGenie_Creations"
        else:
            return "🔧 Tools_And_Utilities"
    
    def _get_directory_size(self, path):
        """Get directory size in MB"""
        try:
            total_size = sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
            return round(total_size / (1024 * 1024), 2)  # Convert to MB
        except:
            return 0
    
    def organize_projects(self, projects):
        """Move projects to organized structure"""
        print(f"\n🗂️ ORGANIZING {len(projects)} PROJECTS...")
        
        organization_report = {
            'moved': 0,
            'errors': 0,
            'categories': {}
        }
        
        for project in projects:
            try:
                target_category = project['type']
                target_dir = self.master_workspace / target_category / project['name']
                
                if target_dir.exists():
                    print(f"   ⚠️ Already exists: {project['name']}")
                    continue
                    
                print(f"   📁 Moving: {project['name']} → {target_category}")
                shutil.move(str(project['path']), str(target_dir))
                
                organization_report['moved'] += 1
                organization_report['categories'][target_category] = organization_report['categories'].get(target_category, 0) + 1
                
            except Exception as e:
                print(f"   ❌ Error moving {project['name']}: {str(e)}")
                organization_report['errors'] += 1
                
        return organization_report
    
    def create_master_index(self, projects, report):
        """Create master index of all projects"""
        print("\n📋 CREATING MASTER PROJECT INDEX...")
        
        index_content = f"""# 🧞‍♂️ NoizyGenie Master Workspace Index

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## 📊 Organization Summary
- **Total Projects Found**: {len(projects)}
- **Successfully Organized**: {report['moved']}
- **Errors**: {report['errors']}

## 📁 Project Categories

"""
        
        for category, count in report['categories'].items():
            index_content += f"### {category} ({count} projects)\n\n"
            
            category_path = self.master_workspace / category
            if category_path.exists():
                for project_dir in category_path.iterdir():
                    if project_dir.is_dir() and project_dir.name != 'README.md':
                        index_content += f"- **{project_dir.name}**\n"
                        
            index_content += "\n"
            
        index_content += f"""
## 🎯 Quick Access

```bash
# Navigate to master workspace
cd "{self.master_workspace}"

# Open in VS Code
code "{self.master_workspace}"
```

## 🧞‍♂️ NoizyGenie Magic Applied!
- ✅ All projects organized by type
- ✅ Consistent folder structure
- ✅ Easy navigation and discovery
- ✅ Centralized project management

*Your scattered projects are now united under one magical roof!* ✨
"""
        
        index_file = self.master_workspace / "PROJECT_INDEX.md"
        index_file.write_text(index_content)
        
        return index_file

def main():
    print("🧞‍♂️ NOIZYGENIE'S PROJECT CONVERGENCE MASTER!")
    print("=" * 60)
    print("🎯 Mission: Unite all scattered projects!")
    print()
    
    master = ProjectConvergenceMaster()
    
    # Create master workspace structure
    master.create_master_workspace()
    
    # Scan for projects
    projects = master.scan_for_projects()
    
    if not projects:
        print("🤔 No projects found in common locations.")
        return
        
    print(f"\n📊 FOUND {len(projects)} PROJECTS:")
    for project in projects:
        print(f"   📁 {project['name']} ({project['type']}) - {project['size']}MB")
    
    # Auto-approve mode activated! 🧞‍♂️⚡
    print(f"\n🚀 AUTO-APPROVE MODE: Organizing {len(projects)} projects automatically!")
    print("🧞‍♂️ NoizyGenie magic - no confirmation needed!")
    response = 'y'  # Auto-approve everything!
    
    # Organize projects
    report = master.organize_projects(projects)
    
    # Create master index
    index_file = master.create_master_index(projects, report)
    
    print(f"\n🎉 PROJECT CONVERGENCE COMPLETE!")
    print(f"📁 Master Workspace: {master.master_workspace}")
    print(f"📋 Project Index: {index_file}")
    print(f"✅ Organized: {report['moved']} projects")
    print(f"❌ Errors: {report['errors']}")
    
    print(f"\n🧞‍♂️ Your scattered projects are now united! ✨")

if __name__ == "__main__":
    main()