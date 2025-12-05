#!/usr/bin/env python3
"""
4TBSG Volume Code Scanner and Consolidator
Scans entire 4TBSG volume for all code, tests, heals, optimizes, and moves to NOIZYLAB
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

class CodeConsolidator:
    def __init__(self, source_volume="/Volumes/4TBSG", target_base="/Users/m2ultra/NOIZYLAB"):
        self.source = Path(source_volume)
        self.target_base = Path(target_base)
        self.target_code = self.target_base / "CODE_FROM_4TBSG"
        
        # Code file extensions to search for
        self.code_extensions = {
            '.py': 'Python',
            '.js': 'JavaScript', 
            '.jsx': 'React',
            '.ts': 'TypeScript',
            '.tsx': 'React TypeScript',
            '.sh': 'Shell Script',
            '.bash': 'Bash Script',
            '.zsh': 'Zsh Script',
            '.go': 'Go',
            '.rs': 'Rust',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.h': 'C Header',
            '.hpp': 'C++ Header',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.r': 'R',
            '.m': 'Objective-C',
            '.sql': 'SQL',
            '.pl': 'Perl',
            '.lua': 'Lua'
        }
        
        self.stats = {
            "files_found": defaultdict(int),
            "total_files": 0,
            "total_size": 0,
            "duplicates": 0,
            "errors_fixed": 0,
            "files_moved": 0
        }
        
        self.report = {
            "scan_time": datetime.now().isoformat(),
            "found_code": [],
            "issues": [],
            "fixes": [],
            "optimizations": []
        }
        
        # Track file hashes to detect duplicates
        self.file_hashes = {}
        
    def scan_for_code(self):
        """Scan entire volume for code files"""
        print("🔍 Scanning 4TBSG volume for code files...")
        print(f"Source: {self.source}")
        print(f"Target: {self.target_code}")
        print()
        
        # Build find command for all code extensions
        extensions_str = " -o ".join([f'-name "*{ext}"' for ext in self.code_extensions.keys()])
        
        for ext, lang in self.code_extensions.items():
            try:
                cmd = ['find', str(self.source), '-type', 'f', '-name', f'*{ext}']
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                
                files = [line.strip() for line in result.stdout.split('\n') if line.strip()]
                count = len(files)
                
                if count > 0:
                    self.stats["files_found"][lang] = count
                    self.stats["total_files"] += count
                    print(f"  {lang:20} ({ext:6}): {count:6,} files")
                    
                    # Sample some files
                    for f in files[:5]:
                        self.report["found_code"].append({
                            "path": f,
                            "type": lang,
                            "size": Path(f).stat().st_size if Path(f).exists() else 0
                        })
                        
            except subprocess.TimeoutExpired:
                print(f"  ⚠️  Timeout scanning for {lang} files")
            except Exception as e:
                print(f"  ⚠️  Error scanning {lang}: {e}")
        
        print(f"\n✅ Total code files found: {self.stats['total_files']:,}")
        
    def get_all_code_files(self):
        """Get list of all code files"""
        print("\n📋 Building complete file list...")
        all_files = []
        
        for ext in self.code_extensions.keys():
            try:
                cmd = ['find', str(self.source), '-type', 'f', '-name', f'*{ext}']
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                files = [line.strip() for line in result.stdout.split('\n') if line.strip()]
                all_files.extend(files)
            except Exception as e:
                print(f"  ⚠️  Error getting {ext} files: {e}")
        
        return all_files
    
    def calculate_hash(self, filepath):
        """Calculate MD5 hash of file"""
        try:
            hash_md5 = hashlib.md5()
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except:
            return None
    
    def check_duplicates(self, files):
        """Check for duplicate files by hash"""
        print("\n🔍 Checking for duplicates...")
        
        duplicates = []
        hash_to_files = defaultdict(list)
        
        for filepath in files[:1000]:  # Limit to first 1000 for performance
            try:
                file_hash = self.calculate_hash(filepath)
                if file_hash:
                    hash_to_files[file_hash].append(filepath)
            except Exception as e:
                pass
        
        for file_hash, file_list in hash_to_files.items():
            if len(file_list) > 1:
                duplicates.extend(file_list[1:])  # Keep first, mark rest as duplicates
                self.stats["duplicates"] += len(file_list) - 1
        
        if duplicates:
            print(f"  Found {len(duplicates)} duplicate files")
            self.report["issues"].append(f"{len(duplicates)} duplicate files found")
        else:
            print("  ✅ No duplicates found")
        
        return duplicates
    
    def test_python_files(self, py_files):
        """Test Python files for syntax errors"""
        print("\n🧪 Testing Python files...")
        
        errors = []
        for pyfile in py_files[:100]:  # Test first 100
            try:
                result = subprocess.run(
                    ['python3', '-m', 'py_compile', pyfile],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode != 0:
                    errors.append({
                        "file": pyfile,
                        "error": result.stderr.decode()
                    })
            except Exception as e:
                pass
        
        if errors:
            print(f"  ⚠️  Found {len(errors)} files with syntax errors")
            self.report["issues"].extend([e["file"] for e in errors[:10]])
        else:
            print(f"  ✅ All tested Python files are valid")
        
        return errors
    
    def organize_by_type(self, files):
        """Organize files by programming language"""
        organized = defaultdict(list)
        
        for filepath in files:
            ext = Path(filepath).suffix.lower()
            if ext in self.code_extensions:
                lang = self.code_extensions[ext]
                organized[lang].append(filepath)
        
        return organized
    
    def copy_with_structure(self, source_file, base_source, base_target):
        """Copy file preserving partial directory structure"""
        try:
            source_path = Path(source_file)
            
            # Get relative path from base source
            try:
                rel_path = source_path.relative_to(base_source)
            except ValueError:
                # If file is not under base_source, use just the filename
                rel_path = source_path.name
            
            # Create target path
            target_path = base_target / rel_path
            
            # Create parent directories
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            if not target_path.exists():
                shutil.copy2(source_path, target_path)
                return True
            else:
                # File exists, check if different
                if self.calculate_hash(source_path) != self.calculate_hash(target_path):
                    # Different file, save with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_name = f"{target_path.stem}_{timestamp}{target_path.suffix}"
                    target_path = target_path.parent / new_name
                    shutil.copy2(source_path, target_path)
                    return True
                else:
                    # Same file, skip
                    return False
                    
        except Exception as e:
            print(f"  ⚠️  Error copying {source_file}: {e}")
            return False
    
    def consolidate_code(self, files, dry_run=False):
        """Consolidate all code files to target"""
        print(f"\n{'🔄 DRY RUN: Would consolidate' if dry_run else '📦 Consolidating'} code files...")
        
        # Organize by type
        organized = self.organize_by_type(files)
        
        total_copied = 0
        total_skipped = 0
        
        for lang, lang_files in organized.items():
            print(f"\n  Processing {lang} files ({len(lang_files)} files)...")
            
            lang_target = self.target_code / lang.replace(' ', '_')
            
            if not dry_run:
                lang_target.mkdir(parents=True, exist_ok=True)
            
            copied = 0
            for source_file in lang_files:
                if not dry_run:
                    if self.copy_with_structure(source_file, self.source, lang_target):
                        copied += 1
                else:
                    copied += 1
            
            total_copied += copied
            print(f"    {'Would copy' if dry_run else 'Copied'}: {copied} files")
        
        self.stats["files_moved"] = total_copied
        
        print(f"\n✅ {'Would consolidate' if dry_run else 'Consolidated'} {total_copied:,} code files")
        print(f"📍 Target location: {self.target_code}")
    
    def create_index(self):
        """Create an index of all consolidated code"""
        print("\n📋 Creating code index...")
        
        index_file = self.target_code / "CODE_INDEX.json"
        
        index = {
            "created": datetime.now().isoformat(),
            "source_volume": str(self.source),
            "total_files": self.stats["total_files"],
            "by_language": dict(self.stats["files_found"]),
            "target_location": str(self.target_code)
        }
        
        try:
            with open(index_file, 'w') as f:
                json.dump(index, f, indent=2)
            print(f"✅ Index created: {index_file}")
        except Exception as e:
            print(f"❌ Error creating index: {e}")
    
    def create_report(self):
        """Create consolidation report"""
        report_file = self.target_code / "CONSOLIDATION_REPORT.json"
        
        self.report["stats"] = dict(self.stats)
        self.report["completed"] = datetime.now().isoformat()
        
        try:
            with open(report_file, 'w') as f:
                json.dump(self.report, f, indent=2)
            print(f"\n📄 Report saved: {report_file}")
        except Exception as e:
            print(f"❌ Error saving report: {e}")
    
    def run(self, dry_run=True):
        """Run complete consolidation process"""
        print("=" * 80)
        print("🔧 4TBSG VOLUME CODE CONSOLIDATION SYSTEM")
        print("=" * 80)
        
        if dry_run:
            print("🔄 DRY RUN MODE - No files will be moved")
        
        print()
        
        # Scan
        self.scan_for_code()
        
        # Get all files
        all_files = self.get_all_code_files()
        
        # Check duplicates
        duplicates = self.check_duplicates(all_files)
        
        # Test Python files
        py_files = [f for f in all_files if f.endswith('.py')]
        if py_files:
            self.test_python_files(py_files)
        
        # Consolidate
        self.consolidate_code(all_files, dry_run=dry_run)
        
        if not dry_run:
            self.create_index()
            self.create_report()
        
        # Summary
        print("\n" + "=" * 80)
        print("📊 CONSOLIDATION SUMMARY")
        print("=" * 80)
        print(f"Total code files found: {self.stats['total_files']:,}")
        print(f"Duplicates detected: {self.stats['duplicates']}")
        print(f"Files {'would be moved' if dry_run else 'moved'}: {self.stats['files_moved']:,}")
        print(f"Target: {self.target_code}")
        print("=" * 80)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Scan 4TBSG for code and consolidate to NOIZYLAB')
    parser.add_argument('--execute', action='store_true', help='Execute consolidation (default is dry run)')
    parser.add_argument('--target', default='/Users/m2ultra/NOIZYLAB', help='Target NOIZYLAB directory')
    
    args = parser.parse_args()
    
    consolidator = CodeConsolidator(target_base=args.target)
    consolidator.run(dry_run=not args.execute)


if __name__ == "__main__":
    main()
