#!/usr/bin/env python3
"""
Smart Git Organizer - Intelligently decides:
- Code files → Git repos (per project)
- Media/binary files → Local storage
- Creates symlinks for project references
"""

import os
import shutil
import subprocess
from pathlib import Path
from collections import defaultdict
import json
from datetime import datetime

class SmartGitOrganizer:
    def __init__(self, source_dir=None, base_dir=None):
        self.source_dir = Path(source_dir) if source_dir else Path.home() / 'Downloads'
        self.base_dir = Path(base_dir) if base_dir else Path.home() / 'NOIZYLAB'
        self.projects_dir = self.base_dir / 'Projects'
        self.media_dir = self.base_dir / 'Media'
        self.files_dir = self.base_dir / 'Files'
        
        # File type categorization
        self.code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h',
            '.go', '.rs', '.rb', '.php', '.swift', '.kt', '.scala', '.clj',
            '.sh', '.bash', '.zsh', '.fish', '.ps1', '.bat', '.cmd'
        }
        
        self.config_extensions = {
            '.json', '.yaml', '.yml', '.toml', '.ini', '.conf', '.config',
            '.xml', '.properties', '.env', '.rc'
        }
        
        self.doc_extensions = {
            '.md', '.txt', '.rst', '.adoc', '.org', '.tex'
        }
        
        self.media_extensions = {
            '.wav', '.mp3', '.aiff', '.flac', '.m4a', '.aac', '.ogg', '.wma',
            '.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv',
            '.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp',
            '.dmg', '.iso', '.img', '.zip', '.tar', '.gz', '.bz2', '.7z', '.rar'
        }
        
        self.stats = {
            'code_files': 0,
            'config_files': 0,
            'doc_files': 0,
            'media_files': 0,
            'other_files': 0,
            'git_repos_created': 0,
            'files_moved': 0
        }
    
    def categorize_file(self, filepath):
        """Categorize file by extension."""
        ext = filepath.suffix.lower()
        size = filepath.stat().st_size if filepath.exists() else 0
        
        if ext in self.code_extensions:
            return 'code', size < 10 * 1024 * 1024  # <10MB for Git
        elif ext in self.config_extensions:
            return 'config', size < 10 * 1024 * 1024
        elif ext in self.doc_extensions:
            return 'doc', size < 10 * 1024 * 1024
        elif ext in self.media_extensions:
            return 'media', False  # Never use Git for media
        else:
            return 'other', size < 10 * 1024 * 1024
    
    def detect_project(self, filepath):
        """Detect project name from file path or content."""
        # Check parent directory names
        parent = filepath.parent.name.lower()
        
        # Common project indicators
        if 'package.json' in str(filepath) or 'requirements.txt' in str(filepath):
            # Try to read project name
            try:
                if 'package.json' in str(filepath):
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        return data.get('name', 'unknown-project')
            except:
                pass
        
        # Use directory name as project
        if parent and parent not in ['downloads', 'desktop', 'documents']:
            return parent.replace(' ', '-').replace('_', '-')
        
        return 'misc-project'
    
    def create_git_repo(self, project_name, project_dir):
        """Create Git repository for project."""
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize Git if not exists
        git_dir = project_dir / '.git'
        if not git_dir.exists():
            try:
                subprocess.run(['git', 'init'], cwd=project_dir, 
                             capture_output=True, check=True)
                self.stats['git_repos_created'] += 1
                return True
            except Exception as e:
                print(f"Warning: Could not create Git repo: {e}")
                return False
        return True
    
    def organize_file(self, filepath):
        """Organize file based on category."""
        category, use_git = self.categorize_file(filepath)
        
        if category in ['code', 'config', 'doc'] and use_git:
            # Move to Git repo
            project_name = self.detect_project(filepath)
            project_dir = self.projects_dir / project_name
            self.create_git_repo(project_name, project_dir)
            
            # Create appropriate subdirectory
            if category == 'code':
                dest_dir = project_dir / 'src'
            elif category == 'config':
                dest_dir = project_dir / 'config'
            else:
                dest_dir = project_dir / 'docs'
            
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / filepath.name
            
            # Handle duplicates
            if dest_path.exists():
                name, ext = os.path.splitext(filepath.name)
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{name}_{counter}{ext}"
                    counter += 1
            
            shutil.move(str(filepath), str(dest_path))
            self.stats['files_moved'] += 1
            
            # Stage in Git
            try:
                subprocess.run(['git', 'add', str(dest_path.relative_to(project_dir))],
                             cwd=project_dir, capture_output=True)
            except:
                pass
            
            return {'status': 'moved_to_git', 'project': project_name, 'path': str(dest_path)}
        
        else:
            # Move to local storage
            if category == 'media':
                dest_dir = self.media_dir / filepath.suffix.lstrip('.').upper()
            else:
                dest_dir = self.files_dir / filepath.suffix.lstrip('.').upper()
            
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / filepath.name
            
            if dest_path.exists():
                name, ext = os.path.splitext(filepath.name)
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{name}_{counter}{ext}"
                    counter += 1
            
            shutil.move(str(filepath), str(dest_path))
            self.stats['files_moved'] += 1
            
            return {'status': 'moved_to_local', 'category': category, 'path': str(dest_path)}
    
    def process_downloads(self):
        """Process all files in Downloads."""
        print("=" * 80)
        print("SMART GIT ORGANIZER - Code → Git, Media → Local")
        print("=" * 80)
        
        files = list(self.source_dir.glob('*'))
        files = [f for f in files if f.is_file() and not f.name.startswith('.')]
        
        print(f"Found {len(files)} files to organize\n")
        
        for filepath in files:
            category, _ = self.categorize_file(filepath)
            
            if category == 'code':
                self.stats['code_files'] += 1
            elif category == 'config':
                self.stats['config_files'] += 1
            elif category == 'doc':
                self.stats['doc_files'] += 1
            elif category == 'media':
                self.stats['media_files'] += 1
            else:
                self.stats['other_files'] += 1
            
            result = self.organize_file(filepath)
            print(f"{filepath.name} → {result['status']}")
        
        # Commit Git repos
        self.commit_git_repos()
        
        # Generate report
        self.generate_report()
    
    def commit_git_repos(self):
        """Commit changes in all Git repos."""
        for project_dir in self.projects_dir.iterdir():
            if (project_dir / '.git').exists():
                try:
                    subprocess.run(['git', 'add', '-A'], cwd=project_dir, 
                                 capture_output=True)
                    subprocess.run(['git', 'commit', '-m', 
                                  f'Auto-organize: {datetime.now().isoformat()}'],
                                 cwd=project_dir, capture_output=True)
                except:
                    pass
    
    def generate_report(self):
        """Generate organization report."""
        print("\n" + "=" * 80)
        print("ORGANIZATION COMPLETE")
        print("=" * 80)
        print(f"Code files: {self.stats['code_files']}")
        print(f"Config files: {self.stats['config_files']}")
        print(f"Doc files: {self.stats['doc_files']}")
        print(f"Media files: {self.stats['media_files']}")
        print(f"Other files: {self.stats['other_files']}")
        print(f"Git repos created: {self.stats['git_repos_created']}")
        print(f"Files moved: {self.stats['files_moved']}")
        print(f"\nProjects: {self.projects_dir}")
        print(f"Media: {self.media_dir}")
        print(f"Files: {self.files_dir}")
        print("=" * 80)


def main():
    """Main execution."""
    organizer = SmartGitOrganizer()
    organizer.process_downloads()

if __name__ == '__main__':
    main()

