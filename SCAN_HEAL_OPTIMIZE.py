#!/usr/bin/env python3
"""
NOIZYLAB Directory Scanner, Healer, and Optimizer
Scans, repairs, and optimizes the NOIZYLAB directory before moving
"""

import os
import sys
import shutil
import hashlib
from pathlib import Path
from collections import defaultdict
import subprocess
import json
from datetime import datetime

class NoizylabHealer:
    def __init__(self, source_path="/Users/m2ultra/NOIZYLAB", target_path="/Volumes/4TBSG/NOIZYLAB"):
        self.source = Path(source_path)
        self.target = Path(target_path)
        self.report = {
            "scan_time": datetime.now().isoformat(),
            "issues_found": [],
            "fixes_applied": [],
            "optimizations": [],
            "errors": []
        }
        self.stats = {
            "total_files": 0,
            "total_dirs": 0,
            "total_size": 0,
            "cleaned_files": 0,
            "space_freed": 0,
            "broken_links": 0,
            "duplicates": 0
        }
        
    def scan_directory(self):
        """Perform comprehensive directory scan"""
        print("🔍 Scanning NOIZYLAB directory...")
        
        try:
            # Count files and directories
            result = subprocess.run(
                ['find', str(self.source), '-type', 'f'],
                capture_output=True, text=True, check=True
            )
            self.stats["total_files"] = len(result.stdout.strip().split('\n'))
            
            result = subprocess.run(
                ['find', str(self.source), '-type', 'd'],
                capture_output=True, text=True, check=True
            )
            self.stats["total_dirs"] = len(result.stdout.strip().split('\n'))
            
            # Get total size
            result = subprocess.run(
                ['du', '-sk', str(self.source)],
                capture_output=True, text=True, check=True
            )
            self.stats["total_size"] = int(result.stdout.split()[0]) * 1024
            
            print(f"✅ Found {self.stats['total_files']:,} files in {self.stats['total_dirs']:,} directories")
            print(f"📦 Total size: {self.stats['total_size'] / (1024**3):.2f} GB")
            
        except Exception as e:
            print(f"❌ Error scanning directory: {e}")
            self.report["errors"].append(f"Scan error: {e}")
    
    def find_broken_symlinks(self):
        """Find and catalog broken symbolic links"""
        print("\n🔗 Checking for broken symlinks...")
        broken_links = []
        
        try:
            result = subprocess.run(
                ['find', str(self.source), '-type', 'l', '!', '-exec', 'test', '-e', '{}', ';', '-print'],
                capture_output=True, text=True, check=True
            )
            broken_links = [line for line in result.stdout.strip().split('\n') if line]
            self.stats["broken_links"] = len(broken_links)
            
            print(f"Found {len(broken_links)} broken symlinks")
            self.report["issues_found"].append(f"{len(broken_links)} broken symlinks")
            
            return broken_links
            
        except Exception as e:
            print(f"❌ Error finding broken symlinks: {e}")
            self.report["errors"].append(f"Symlink scan error: {e}")
            return []
    
    def find_cleanup_files(self):
        """Find files that can be safely removed"""
        print("\n🧹 Finding cleanup candidates...")
        
        cleanup_patterns = {
            ".DS_Store": [],
            "._*": [],
            "*~": [],
            "*.pyc": [],
            "__pycache__": [],
            "*.log": [],
            "*.tmp": [],
            ".cache": []
        }
        
        for pattern in cleanup_patterns.keys():
            try:
                if pattern == "__pycache__":
                    result = subprocess.run(
                        ['find', str(self.source), '-type', 'd', '-name', pattern],
                        capture_output=True, text=True, check=True
                    )
                else:
                    result = subprocess.run(
                        ['find', str(self.source), '-name', pattern],
                        capture_output=True, text=True, check=True
                    )
                files = [line for line in result.stdout.strip().split('\n') if line]
                cleanup_patterns[pattern] = files
                print(f"  • {pattern}: {len(files)} items")
                
            except Exception as e:
                print(f"  ⚠️  Error scanning {pattern}: {e}")
        
        return cleanup_patterns
    
    def clean_files(self, cleanup_files, dry_run=False):
        """Remove unnecessary files"""
        print(f"\n{'🔄 DRY RUN: Would clean' if dry_run else '🧹 Cleaning'} unnecessary files...")
        
        total_cleaned = 0
        space_freed = 0
        
        for pattern, files in cleanup_files.items():
            print(f"\nProcessing {pattern}...")
            for file_path in files:
                try:
                    path = Path(file_path)
                    if path.exists():
                        size = 0
                        if path.is_file():
                            size = path.stat().st_size
                        elif path.is_dir():
                            result = subprocess.run(
                                ['du', '-sk', str(path)],
                                capture_output=True, text=True, check=True
                            )
                            size = int(result.stdout.split()[0]) * 1024
                        
                        if not dry_run:
                            if path.is_dir():
                                shutil.rmtree(path)
                            else:
                                path.unlink()
                        
                        total_cleaned += 1
                        space_freed += size
                        
                except Exception as e:
                    print(f"  ⚠️  Could not remove {file_path}: {e}")
            
            print(f"  Cleaned {len(files)} items ({pattern})")
        
        self.stats["cleaned_files"] = total_cleaned
        self.stats["space_freed"] = space_freed
        
        print(f"\n✅ {'Would clean' if dry_run else 'Cleaned'} {total_cleaned:,} items")
        print(f"💾 {'Would free' if dry_run else 'Freed'} {space_freed / (1024**2):.2f} MB")
        
        self.report["fixes_applied"].append(
            f"{'Simulated cleaning' if dry_run else 'Cleaned'} {total_cleaned} files, "
            f"{'would free' if dry_run else 'freed'} {space_freed / (1024**2):.2f} MB"
        )
    
    def remove_broken_symlinks(self, broken_links, dry_run=False):
        """Remove broken symbolic links"""
        if not broken_links:
            print("\n✅ No broken symlinks to remove")
            return
        
        print(f"\n{'🔄 DRY RUN: Would remove' if dry_run else '🔗 Removing'} broken symlinks...")
        
        removed = 0
        for link in broken_links:
            try:
                if not dry_run:
                    Path(link).unlink()
                removed += 1
            except Exception as e:
                print(f"  ⚠️  Could not remove {link}: {e}")
        
        print(f"✅ {'Would remove' if dry_run else 'Removed'} {removed} broken symlinks")
        self.report["fixes_applied"].append(
            f"{'Would remove' if dry_run else 'Removed'} {removed} broken symlinks"
        )
    
    def fix_permissions(self, dry_run=False):
        """Fix file and directory permissions"""
        print(f"\n{'🔄 DRY RUN: Would fix' if dry_run else '🔐 Fixing'} permissions...")
        
        try:
            if not dry_run:
                # Fix directory permissions to 755
                subprocess.run(
                    ['find', str(self.source), '-type', 'd', '-exec', 'chmod', '755', '{}', '+'],
                    check=True
                )
                
                # Fix file permissions to 644
                subprocess.run(
                    ['find', str(self.source), '-type', 'f', '-exec', 'chmod', '644', '{}', '+'],
                    check=True
                )
                
                # Fix executable scripts
                subprocess.run(
                    ['find', str(self.source), '-type', 'f', '-name', '*.py', '-exec', 'chmod', '+x', '{}', '+'],
                    check=True
                )
                subprocess.run(
                    ['find', str(self.source), '-type', 'f', '-name', '*.sh', '-exec', 'chmod', '+x', '{}', '+'],
                    check=True
                )
            
            print(f"✅ {'Would fix' if dry_run else 'Fixed'} permissions")
            self.report["fixes_applied"].append(
                f"{'Would normalize' if dry_run else 'Normalized'} file and directory permissions"
            )
            
        except Exception as e:
            print(f"❌ Error fixing permissions: {e}")
            self.report["errors"].append(f"Permission fix error: {e}")
    
    def optimize_git_repos(self, dry_run=False):
        """Optimize git repositories"""
        print(f"\n{'🔄 DRY RUN: Would optimize' if dry_run else '📦 Optimizing'} git repositories...")
        
        try:
            result = subprocess.run(
                ['find', str(self.source), '-type', 'd', '-name', '.git'],
                capture_output=True, text=True, check=True
            )
            
            git_repos = [line for line in result.stdout.strip().split('\n') if line]
            print(f"Found {len(git_repos)} git repositories")
            
            optimized = 0
            for git_dir in git_repos:
                repo_path = Path(git_dir).parent
                try:
                    if not dry_run:
                        subprocess.run(
                            ['git', '-C', str(repo_path), 'gc', '--aggressive', '--prune=now'],
                            capture_output=True, timeout=60
                        )
                    optimized += 1
                except Exception as e:
                    print(f"  ⚠️  Could not optimize {repo_path}: {e}")
            
            print(f"✅ {'Would optimize' if dry_run else 'Optimized'} {optimized} repositories")
            self.report["optimizations"].append(
                f"{'Would optimize' if dry_run else 'Optimized'} {optimized} git repositories"
            )
            
        except Exception as e:
            print(f"❌ Error optimizing git repos: {e}")
            self.report["errors"].append(f"Git optimization error: {e}")
    
    def create_backup_manifest(self):
        """Create a manifest of the directory structure"""
        print("\n📋 Creating directory manifest...")
        
        manifest_path = self.source / "NOIZYLAB_MANIFEST.json"
        
        try:
            manifest = {
                "created": datetime.now().isoformat(),
                "source": str(self.source),
                "stats": self.stats,
                "structure": {}
            }
            
            # Get top-level structure
            for item in self.source.iterdir():
                if item.name.startswith('.'):
                    continue
                    
                try:
                    if item.is_dir():
                        result = subprocess.run(
                            ['du', '-sh', str(item)],
                            capture_output=True, text=True, timeout=30
                        )
                        size = result.stdout.split()[0]
                        manifest["structure"][item.name] = {
                            "type": "directory",
                            "size": size
                        }
                    elif item.is_file():
                        manifest["structure"][item.name] = {
                            "type": "file",
                            "size": item.stat().st_size
                        }
                except Exception as e:
                    manifest["structure"][item.name] = {"error": str(e)}
            
            with open(manifest_path, 'w') as f:
                json.dump(manifest, f, indent=2)
            
            print(f"✅ Manifest created: {manifest_path}")
            self.report["optimizations"].append("Created directory manifest")
            
        except Exception as e:
            print(f"❌ Error creating manifest: {e}")
            self.report["errors"].append(f"Manifest creation error: {e}")
    
    def move_to_target(self, dry_run=False):
        """Move the directory to target location"""
        print(f"\n{'🔄 DRY RUN: Would move' if dry_run else '🚚 Moving'} NOIZYLAB to target...")
        
        if self.target.exists():
            print(f"⚠️  Target already exists: {self.target}")
            response = input("Overwrite? (yes/no): ")
            if response.lower() != 'yes':
                print("❌ Move cancelled")
                return False
            
            if not dry_run:
                print("Removing existing target...")
                shutil.rmtree(self.target)
        
        try:
            if not dry_run:
                print(f"Moving {self.source} → {self.target}")
                shutil.move(str(self.source), str(self.target))
                print(f"✅ Successfully moved to {self.target}")
            else:
                print(f"✅ Would move {self.source} → {self.target}")
            
            self.report["optimizations"].append(
                f"{'Would move' if dry_run else 'Moved'} directory to {self.target}"
            )
            return True
            
        except Exception as e:
            print(f"❌ Error moving directory: {e}")
            self.report["errors"].append(f"Move error: {e}")
            return False
    
    def save_report(self):
        """Save the healing report"""
        report_path = self.source / "HEALING_REPORT.json"
        
        try:
            with open(report_path, 'w') as f:
                json.dump(self.report, f, indent=2)
            
            print(f"\n📄 Report saved: {report_path}")
            
        except Exception as e:
            print(f"❌ Error saving report: {e}")
    
    def run(self, dry_run=True, skip_move=False):
        """Run the complete healing process"""
        print("=" * 70)
        print("🏥 NOIZYLAB HEALING SYSTEM")
        print("=" * 70)
        
        if dry_run:
            print("🔄 DRY RUN MODE - No changes will be made")
        
        print()
        
        # Scan
        self.scan_directory()
        
        # Find issues
        broken_links = self.find_broken_symlinks()
        cleanup_files = self.find_cleanup_files()
        
        # Heal
        self.clean_files(cleanup_files, dry_run=dry_run)
        self.remove_broken_symlinks(broken_links, dry_run=dry_run)
        self.fix_permissions(dry_run=dry_run)
        
        # Optimize
        self.optimize_git_repos(dry_run=dry_run)
        
        if not dry_run:
            self.create_backup_manifest()
        
        # Move
        if not skip_move:
            self.move_to_target(dry_run=dry_run)
        
        # Report
        if not dry_run:
            self.save_report()
        
        print("\n" + "=" * 70)
        print("📊 SUMMARY")
        print("=" * 70)
        print(f"Total files: {self.stats['total_files']:,}")
        print(f"Total directories: {self.stats['total_dirs']:,}")
        print(f"Total size: {self.stats['total_size'] / (1024**3):.2f} GB")
        print(f"Cleaned files: {self.stats['cleaned_files']:,}")
        print(f"Space freed: {self.stats['space_freed'] / (1024**2):.2f} MB")
        print(f"Broken symlinks: {self.stats['broken_links']}")
        print("=" * 70)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Heal and optimize NOIZYLAB directory')
    parser.add_argument('--execute', action='store_true', help='Execute changes (default is dry run)')
    parser.add_argument('--skip-move', action='store_true', help='Skip moving to target')
    parser.add_argument('--source', default='/Users/m2ultra/NOIZYLAB', help='Source directory')
    parser.add_argument('--target', default='/Volumes/4TBSG/NOIZYLAB', help='Target directory')
    
    args = parser.parse_args()
    
    healer = NoizylabHealer(source_path=args.source, target_path=args.target)
    healer.run(dry_run=not args.execute, skip_move=args.skip_move)


if __name__ == "__main__":
    main()
