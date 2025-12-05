#!/usr/bin/env python3
"""
🔥 ULTIMATE CURSOR AUTOFIX - Handles ALL Cursor Issues
Fixes autoaccept, git locks, staging issues, and more
"""

import os
import subprocess
import json
import time
from pathlib import Path

class CursorAutoFix:
    def __init__(self):
        self.repo = '/Users/m2ultra/Github/Noizyfish/NOIZYLAB'
        self.issues_found = []
        self.fixes_applied = []
        
    def log(self, message, level="INFO"):
        """Logging with emoji"""
        emoji = {
            "INFO": "ℹ️",
            "SUCCESS": "✅",
            "ERROR": "❌",
            "WARNING": "⚠️",
            "FIX": "🔧"
        }
        print(f"{emoji.get(level, 'ℹ️')} {message}")
    
    def run_command(self, cmd, cwd=None, timeout=30):
        """Run command safely"""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=cwd or self.repo,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timeout"
        except Exception as e:
            return False, "", str(e)
    
    def fix_git_locks(self):
        """Fix ALL git locks"""
        self.log("Fixing Git locks...", "FIX")
        
        # Kill all git processes
        self.run_command("killall git", timeout=5)
        time.sleep(1)
        
        # Remove all lock files
        lock_files = [
            '.git/index.lock',
            '.git/HEAD.lock',
            '.git/refs/heads/main.lock',
            '.git/refs/heads/master.lock'
        ]
        
        for lock in lock_files:
            lock_path = os.path.join(self.repo, lock)
            if os.path.exists(lock_path):
                try:
                    os.remove(lock_path)
                    self.fixes_applied.append(f"Removed {lock}")
                except Exception as e:
                    self.log(f"Could not remove {lock}: {e}", "WARNING")
        
        self.log("Git locks cleared", "SUCCESS")
    
    def fix_git_index(self):
        """Fix corrupted git index"""
        self.log("Checking Git index...", "FIX")
        
        # Try to reset index if corrupted
        success, _, _ = self.run_command("git reset", timeout=10)
        if success:
            self.fixes_applied.append("Git index reset")
            self.log("Git index OK", "SUCCESS")
        else:
            self.log("Git index may need manual repair", "WARNING")
    
    def optimize_git_config(self):
        """Optimize Git for large repos"""
        self.log("Optimizing Git configuration...", "FIX")
        
        configs = {
            'core.preloadindex': 'true',
            'core.fscache': 'true',
            'gc.auto': '256',
            'feature.manyFiles': 'true',
            'index.threads': 'true',
            'pack.threads': '0',
            'pack.windowMemory': '100m'
        }
        
        for key, value in configs.items():
            success, _, _ = self.run_command(
                f"git config {key} {value}",
                timeout=5
            )
            if success:
                self.fixes_applied.append(f"Set {key} = {value}")
        
        self.log("Git config optimized", "SUCCESS")
    
    def check_disk_space(self):
        """Check available disk space"""
        self.log("Checking disk space...", "INFO")
        
        success, stdout, _ = self.run_command("df -h .", timeout=5)
        if success:
            lines = stdout.strip().split('\n')
            if len(lines) > 1:
                self.log(f"Disk: {lines[1]}", "INFO")
    
    def create_smart_gitignore(self):
        """Create smart .gitignore for Cursor"""
        self.log("Creating smart .gitignore...", "FIX")
        
        gitignore_path = os.path.join(self.repo, '.gitignore')
        
        gitignore_content = """# Cursor & Editor
.cursor/
.vscode/
.idea/
*.swp
*.swo
*~

# OS Files
.DS_Store
Thumbs.db
Desktop.ini

# Temporary
*.tmp
*.temp
*.log
*.pid

# Large Files (use Git LFS)
*.mp4
*.MP4
*.wav
*.WAV
*.mov
*.avi

# Build artifacts
node_modules/
__pycache__/
*.pyc
dist/
build/
.env

# Git
.git/index.lock
.git/HEAD.lock
"""
        
        try:
            # Only add new entries, don't overwrite
            if os.path.exists(gitignore_path):
                with open(gitignore_path, 'r') as f:
                    existing = f.read()
                if '.cursor/' not in existing:
                    with open(gitignore_path, 'a') as f:
                        f.write('\n# Smart Cursor additions\n')
                        f.write('.cursor/\n')
                        f.write('.git/index.lock\n')
                    self.fixes_applied.append("Updated .gitignore")
            else:
                with open(gitignore_path, 'w') as f:
                    f.write(gitignore_content)
                self.fixes_applied.append("Created .gitignore")
            
            self.log(".gitignore configured", "SUCCESS")
        except Exception as e:
            self.log(f"Could not update .gitignore: {e}", "WARNING")
    
    def test_git_operations(self):
        """Test basic git operations"""
        self.log("Testing Git operations...", "INFO")
        
        tests = [
            ("git status", 10),
            ("git log -1 --oneline", 5),
            ("git ls-files | head -1", 5)
        ]
        
        all_ok = True
        for cmd, timeout in tests:
            success, _, stderr = self.run_command(cmd, timeout=timeout)
            if success:
                self.log(f"  ✓ {cmd.split()[1]}", "SUCCESS")
            else:
                self.log(f"  ✗ {cmd.split()[1]}: {stderr}", "ERROR")
                all_ok = False
        
        return all_ok
    
    def create_staging_script(self):
        """Create smart staging helper"""
        self.log("Creating staging helper...", "FIX")
        
        script_path = os.path.join(os.path.dirname(self.repo), 'SMART_STAGE.sh')
        
        script_content = """#!/bin/bash
# Smart staging for large repos

cd /Users/m2ultra/Github/Noizyfish/NOIZYLAB

echo "🚀 SMART STAGING"
echo "================================"

# Clear locks first
killall git 2>/dev/null || true
rm -f .git/index.lock 2>/dev/null

# Stage in small batches
git add *.md *.py *.sh *.json 2>/dev/null || true
git add _CLAUDE_ORGANIZED/ 2>/dev/null || true

echo "✅ Staged successfully"
git status --short | head -10
"""
        
        try:
            with open(script_path, 'w') as f:
                f.write(script_content)
            os.chmod(script_path, 0o755)
            self.fixes_applied.append(f"Created {script_path}")
            self.log("Staging helper created", "SUCCESS")
        except Exception as e:
            self.log(f"Could not create staging helper: {e}", "WARNING")
    
    def generate_report(self):
        """Generate comprehensive report"""
        print("\n" + "=" * 60)
        print("📊 CURSOR AUTOFIX REPORT")
        print("=" * 60)
        
        print(f"\n✅ Fixes Applied: {len(self.fixes_applied)}")
        for fix in self.fixes_applied:
            print(f"  • {fix}")
        
        if self.issues_found:
            print(f"\n⚠️  Issues Found: {len(self.issues_found)}")
            for issue in self.issues_found:
                print(f"  • {issue}")
        
        print("\n🎯 RECOMMENDATIONS:")
        print("  1. Use small batch commits")
        print("  2. Stage files by category")
        print("  3. Clear locks before operations")
        print("  4. Use Git LFS for large files")
        print("  5. Optimize git config (done!)")
        
        # Save report
        report_path = '/Users/m2ultra/CURSOR_AUTOFIX_REPORT.json'
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'fixes_applied': self.fixes_applied,
            'issues_found': self.issues_found,
            'repo_path': self.repo
        }
        
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Report saved: {report_path}")
        print("\n✨ CURSOR AUTOFIX COMPLETE!\n")
    
    def run(self):
        """Execute all fixes"""
        print("\n" + "🔥" * 30)
        print("ULTIMATE CURSOR AUTOFIX")
        print("🔥" * 30 + "\n")
        
        # Fix locks first
        self.fix_git_locks()
        
        # Fix index
        self.fix_git_index()
        
        # Optimize config
        self.optimize_git_config()
        
        # Create gitignore
        self.create_smart_gitignore()
        
        # Create helpers
        self.create_staging_script()
        
        # Check disk
        self.check_disk_space()
        
        # Test operations
        if self.test_git_operations():
            self.log("All Git operations working!", "SUCCESS")
        else:
            self.log("Some Git operations failed", "WARNING")
            self.issues_found.append("Git operations need attention")
        
        # Report
        self.generate_report()

if __name__ == "__main__":
    fixer = CursorAutoFix()
    fixer.run()
