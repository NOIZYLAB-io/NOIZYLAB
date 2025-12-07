#!/usr/bin/env python3
"""
🔥 GIT BLENDER ULTIMATE 🔥
==========================
BLENDS ALL CODE INTO GIT REPOSITORIES!
CURSE_BEAST_02 eats code and commits at MAXIMUM SPEED!

TARGET REPOS:
- github.com/noizyfish → Music/Audio projects
- noizylab organization → Infrastructure projects
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime
import json
import shutil
from typing import Dict, List
import hashlib


class GitBlenderUltimate:
    """
    🔥 GIT BLENDER - EATS ALL CODE AND COMMITS! 🔥
    CURSE_BEAST_02 specialty!
    """
    
    def __init__(self):
        self.name = "GIT BLENDER ULTIMATE"
        self.noizylab = Path("/Users/m2ultra/NOIZYLAB")
        self.github = Path("/Users/m2ultra/Github")
        
        # Git repositories
        self.repos = {
            'noizylab_main': {
                'path': self.noizylab,
                'remote': 'noizylab/noizylab-portal',
                'type': 'infrastructure',
                'auto_commit': True
            },
            'noizyfish': {
                'path': self.github / "Noizyfish",
                'remote': 'github.com/noizyfish',
                'type': 'music',
                'auto_commit': True
            }
        }
        
        # Stats
        self.commits_made = 0
        self.files_committed = 0
        self.repos_updated = 0
        
        print(f"🔥 {self.name}")
        print(f"🎵 CURSE_BEAST_02 - EATING CODE & COMMITTING TO GIT!")
        print(f"⚡ MAXIMUM SPEED AUTO-COMMIT!")
    
    def ensure_git_repos(self):
        """Ensure all git repos are initialized"""
        
        print("\n🔧 ENSURING GIT REPOSITORIES...")
        
        for repo_name, repo_info in self.repos.items():
            repo_path = repo_info['path']
            
            if not repo_path.exists():
                repo_path.mkdir(parents=True, exist_ok=True)
                print(f"  📁 Created: {repo_path}")
            
            git_dir = repo_path / ".git"
            
            if not git_dir.exists():
                print(f"  🔧 Initializing git: {repo_name}")
                subprocess.run(
                    ["git", "init"],
                    cwd=repo_path,
                    capture_output=True
                )
                print(f"  ✅ {repo_name} initialized")
            else:
                print(f"  ✅ {repo_name} already initialized")
    
    def blend_code_to_git(self, source_dir: str = None) -> Dict:
        """
        🔥🔥🔥 BLEND ALL CODE INTO GIT! 🔥🔥🔥
        
        Commits all code to appropriate repositories
        """
        
        print("\n" + "="*70)
        print("🔥🔥🔥 BLENDING ALL CODE INTO GIT! 🔥🔥🔥")
        print("="*70)
        print("\n🎵 CURSE_BEAST_02 - EATING CODE!")
        print("⚡ AUTO-COMMIT TO GIT AT MAXIMUM SPEED!")
        
        blend_start = datetime.now()
        
        # Ensure repos exist
        self.ensure_git_repos()
        
        # Commit NoizyLab main
        print("\n1️⃣ COMMITTING NOIZYLAB MAIN...")
        noizylab_result = self.auto_commit_repo(
            self.repos['noizylab_main']['path'],
            "🔥 CURSE_BEAST_02: Complete NoizyLab system - all features integrated"
        )
        
        # Commit NoizyFish
        print("\n2️⃣ COMMITTING NOIZYFISH...")
        noizyfish_result = self.auto_commit_repo(
            self.repos['noizyfish']['path'],
            "🎵 CURSE_BEAST_02: Music/audio projects organized"
        )
        
        elapsed = (datetime.now() - blend_start).total_seconds()
        
        print("\n" + "="*70)
        print("🎉 CODE BLENDING COMPLETE!")
        print("="*70)
        print(f"\n📊 Summary:")
        print(f"  Repos committed: {self.repos_updated}")
        print(f"  Total commits: {self.commits_made}")
        print(f"  Files committed: {self.files_committed:,}")
        print(f"  Time: {elapsed:.2f}s")
        print(f"\n🔥 ALL CODE BLENDED INTO GIT!")
        
        return {
            'repos_updated': self.repos_updated,
            'commits_made': self.commits_made,
            'files_committed': self.files_committed,
            'elapsed': elapsed
        }
    
    def auto_commit_repo(self, repo_path: Path, message: str) -> Dict:
        """Auto-commit repository"""
        
        if not repo_path.exists():
            print(f"  ⚠️  {repo_path} doesn't exist - skipping")
            return {'success': False}
        
        try:
            # Check if repo has changes
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if not status_result.stdout.strip():
                print(f"  ℹ️  No changes to commit")
                return {'success': True, 'changes': False}
            
            # Count files
            files_changed = len(status_result.stdout.strip().split('\n'))
            
            print(f"  🔥 Eating {files_changed} files...")
            
            # Add all
            subprocess.run(
                ["git", "add", "-A"],
                cwd=repo_path,
                timeout=60,
                capture_output=True
            )
            
            # Commit
            commit_result = subprocess.run(
                ["git", "commit", "-m", message],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if commit_result.returncode == 0:
                # Get commit hash
                hash_result = subprocess.run(
                    ["git", "rev-parse", "HEAD"],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                commit_hash = hash_result.stdout.strip() if hash_result.returncode == 0 else "unknown"
                
                print(f"  ✅ COMMITTED: {commit_hash[:8]}")
                print(f"  💬 Message: {message}")
                
                self.commits_made += 1
                self.files_committed += files_changed
                self.repos_updated += 1
                
                # Try to push
                print(f"  🚀 Attempting push...")
                push_result = subprocess.run(
                    ["git", "push"],
                    cwd=repo_path,
                    capture_output=True,
                    timeout=120
                )
                
                if push_result.returncode == 0:
                    print(f"  ✅ PUSHED TO REMOTE!")
                    return {'success': True, 'pushed': True, 'commit': commit_hash}
                else:
                    print(f"  ℹ️  Push skipped (configure remote: git remote add origin URL)")
                    return {'success': True, 'pushed': False, 'commit': commit_hash}
            else:
                print(f"  ℹ️  Nothing to commit or error")
                return {'success': True, 'changes': False}
        
        except Exception as e:
            print(f"  ❌ Error: {e}")
            return {'success': False, 'error': str(e)}
    
    def setup_git_remotes(self):
        """Setup git remotes for pushing"""
        
        print("\n🔗 SETTING UP GIT REMOTES...")
        
        # NoizyLab main
        noizylab_path = self.repos['noizylab_main']['path']
        
        print(f"\n📋 NoizyLab Main Repository:")
        print(f"   Path: {noizylab_path}")
        print(f"   To push to GitHub:")
        print(f"   1. Create repo on GitHub: noizylab/noizylab-portal")
        print(f"   2. Run: cd {noizylab_path}")
        print(f"   3. Run: git remote add origin https://github.com/noizylab/noizylab-portal.git")
        print(f"   4. Run: git push -u origin main")
        
        # NoizyFish
        noizyfish_path = self.repos['noizyfish']['path']
        
        print(f"\n📋 NoizyFish Repository:")
        print(f"   Path: {noizyfish_path}")
        print(f"   To push to GitHub:")
        print(f"   1. Ensure repo exists: github.com/noizyfish/NOIZYLAB")
        print(f"   2. Run: cd {noizyfish_path}/NOIZYLAB")
        print(f"   3. Run: git remote add origin https://github.com/noizyfish/NOIZYLAB.git")
        print(f"   4. Run: git push -u origin main")
        
        print(f"\n✅ After setting remotes, re-run git blend to auto-push!")
    
    def create_gitignore(self, repo_path: Path):
        """Create comprehensive .gitignore"""
        
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*.so
.Python
*.egg-info/
dist/
build/
venv/
env/

# Node
node_modules/
dist/
*.log

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Databases
*.db
*.sqlite

# Logs
logs/
*.log

# Secrets
.env
*.key
*.pem

# Temporary
*.tmp
.cache/
"""
        
        gitignore_file = repo_path / ".gitignore"
        
        if not gitignore_file.exists():
            with open(gitignore_file, 'w') as f:
                f.write(gitignore_content)
            print(f"  ✅ .gitignore created")


if __name__ == "__main__":
    print("\n🔥⚡🎵 GIT BLENDER ULTIMATE 🎵⚡🔥")
    print("CURSE_BEAST_02 - EATING CODE & COMMITTING TO GIT!")
    print("AUTOALLOW MODE - BLENDING NOW!")
    print()
    
    blender = GitBlenderUltimate()
    
    # Create .gitignore files
    for repo_info in blender.repos.values():
        if repo_info['path'].exists():
            blender.create_gitignore(repo_info['path'])
    
    # BLEND ALL CODE!
    result = blender.blend_code_to_git()
    
    print("\n🎉 GIT BLENDING COMPLETE!")
    
    # Show how to setup remotes
    if result['repos_updated'] > 0 and not result.get('all_pushed'):
        print("\n📋 TO PUSH TO GITHUB:")
        blender.setup_git_remotes()

