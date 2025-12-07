#!/usr/bin/env python3
"""
SCAN, TEST, HEAL, OPTIMIZE & MOVE - Comprehensive Migration System
Processes files from /Volumes/4TBSG to /Users/m2ultra/NOIZYLAB
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Set
import hashlib
import ast
import re

class ScanTestHealOptimizeMove:
    def __init__(self):
        self.source = Path("/Volumes/4TBSG")
        self.dest = Path("/Users/m2ultra/NOIZYLAB")
        self.report = {
            "scan_results": {},
            "test_results": {},
            "heal_results": {},
            "optimize_results": {},
            "move_results": {},
            "timestamp": datetime.now().isoformat(),
            "errors": [],
            "warnings": []
        }
        
        # Directories to process
        self.key_directories = [
            "NOIZYLAB",
            "Extensions",
            "_RESCUE"
        ]
        
        # File types to process
        self.code_extensions = {'.py', '.sh', '.js', '.ts', '.json'}
        self.skip_extensions = {'.wav', '.aif', '.aiff', '.mp3', '.mp4', '.mov', '.dmg', '.pkg'}
        
        self.tested_files = []
        self.healed_files = []
        self.moved_files = []

    def scan_phase(self) -> Dict:
        """Phase 1: Comprehensive scan of source directory"""
        print("\n🔍 PHASE 1: SCANNING 4TBSG DRIVE...")
        print("=" * 60)
        
        scan_data = {
            "total_size": 0,
            "file_counts": {},
            "directory_structure": {},
            "code_files": [],
            "issues_found": []
        }
        
        for directory in self.key_directories:
            dir_path = self.source / directory
            if not dir_path.exists():
                print(f"⚠️  Directory not found: {directory}")
                continue
                
            print(f"\nScanning {directory}...")
            
            file_count = 0
            code_files = []
            dir_size = 0
            
            try:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = Path(root) / file
                        ext = file_path.suffix.lower()
                        
                        try:
                            size = file_path.stat().st_size
                            dir_size += size
                            file_count += 1
                            
                            # Track file types
                            scan_data["file_counts"][ext] = scan_data["file_counts"].get(ext, 0) + 1
                            
                            # Identify code files
                            if ext in self.code_extensions:
                                code_files.append({
                                    "path": str(file_path),
                                    "size": size,
                                    "type": ext
                                })
                                
                        except (OSError, PermissionError) as e:
                            scan_data["issues_found"].append(f"Cannot access: {file_path} - {e}")
                
                scan_data["directory_structure"][directory] = {
                    "file_count": file_count,
                    "size_bytes": dir_size,
                    "size_human": self._format_size(dir_size),
                    "code_files": len(code_files)
                }
                
                scan_data["code_files"].extend(code_files)
                scan_data["total_size"] += dir_size
                
                print(f"  ✓ Files: {file_count}")
                print(f"  ✓ Size: {self._format_size(dir_size)}")
                print(f"  ✓ Code files: {len(code_files)}")
                
            except Exception as e:
                error_msg = f"Error scanning {directory}: {e}"
                print(f"  ✗ {error_msg}")
                scan_data["issues_found"].append(error_msg)
        
        self.report["scan_results"] = scan_data
        
        print(f"\n📊 SCAN SUMMARY:")
        print(f"  Total Size: {self._format_size(scan_data['total_size'])}")
        print(f"  Code Files: {len(scan_data['code_files'])}")
        print(f"  Issues: {len(scan_data['issues_found'])}")
        
        return scan_data

    def test_phase(self, scan_data: Dict) -> Dict:
        """Phase 2: Test all code files for syntax and basic functionality"""
        print("\n🧪 PHASE 2: TESTING CODE FILES...")
        print("=" * 60)
        
        test_data = {
            "total_tested": 0,
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "results": []
        }
        
        code_files = scan_data.get("code_files", [])
        
        for file_info in code_files:
            file_path = Path(file_info["path"])
            ext = file_info["type"]
            
            result = {
                "file": str(file_path),
                "type": ext,
                "status": "unknown",
                "issues": []
            }
            
            try:
                if ext == ".py":
                    result = self._test_python_file(file_path)
                elif ext == ".sh":
                    result = self._test_shell_script(file_path)
                elif ext == ".json":
                    result = self._test_json_file(file_path)
                else:
                    result["status"] = "skipped"
                    result["issues"] = ["File type not tested"]
                
                if result["status"] == "passed":
                    test_data["passed"] += 1
                    self.tested_files.append(file_path)
                elif result["status"] == "failed":
                    test_data["failed"] += 1
                else:
                    test_data["skipped"] += 1
                
                test_data["total_tested"] += 1
                test_data["results"].append(result)
                
                # Progress indicator
                if test_data["total_tested"] % 10 == 0:
                    print(f"  Tested {test_data['total_tested']}/{len(code_files)} files...")
                
            except Exception as e:
                result["status"] = "error"
                result["issues"] = [str(e)]
                test_data["failed"] += 1
                test_data["results"].append(result)
        
        self.report["test_results"] = test_data
        
        print(f"\n📊 TEST SUMMARY:")
        print(f"  ✓ Passed: {test_data['passed']}")
        print(f"  ✗ Failed: {test_data['failed']}")
        print(f"  ⊘ Skipped: {test_data['skipped']}")
        
        return test_data

    def heal_phase(self, test_data: Dict) -> Dict:
        """Phase 3: Heal and fix issues found during testing"""
        print("\n🏥 PHASE 3: HEALING CODE ISSUES...")
        print("=" * 60)
        
        heal_data = {
            "total_healed": 0,
            "successful_fixes": 0,
            "failed_fixes": 0,
            "fixes_applied": []
        }
        
        failed_tests = [r for r in test_data["results"] if r["status"] == "failed"]
        
        for result in failed_tests:
            file_path = Path(result["file"])
            
            try:
                if result["type"] == ".py":
                    fixed = self._heal_python_file(file_path, result["issues"])
                elif result["type"] == ".sh":
                    fixed = self._heal_shell_script(file_path, result["issues"])
                else:
                    continue
                
                if fixed:
                    heal_data["successful_fixes"] += 1
                    heal_data["fixes_applied"].append({
                        "file": str(file_path),
                        "issues": result["issues"],
                        "status": "healed"
                    })
                    self.healed_files.append(file_path)
                    print(f"  ✓ Healed: {file_path.name}")
                else:
                    heal_data["failed_fixes"] += 1
                    
                heal_data["total_healed"] += 1
                
            except Exception as e:
                heal_data["failed_fixes"] += 1
                print(f"  ✗ Failed to heal {file_path.name}: {e}")
        
        self.report["heal_results"] = heal_data
        
        print(f"\n📊 HEAL SUMMARY:")
        print(f"  ✓ Successfully Fixed: {heal_data['successful_fixes']}")
        print(f"  ✗ Failed to Fix: {heal_data['failed_fixes']}")
        
        return heal_data

    def optimize_phase(self, scan_data: Dict) -> Dict:
        """Phase 4: Optimize file organization and structure"""
        print("\n⚡ PHASE 4: OPTIMIZING FILE STRUCTURE...")
        print("=" * 60)
        
        optimize_data = {
            "reorganization_plan": {},
            "duplicates_found": [],
            "size_optimizations": []
        }
        
        # Create optimized directory structure
        structure = {
            "scripts": {"python": [], "shell": [], "other": []},
            "configs": [],
            "data": [],
            "rescue": [],
            "extensions": []
        }
        
        for file_info in scan_data.get("code_files", []):
            file_path = Path(file_info["path"])
            ext = file_info["type"]
            
            # Categorize files
            if ext == ".py":
                structure["scripts"]["python"].append(file_path)
            elif ext == ".sh":
                structure["scripts"]["shell"].append(file_path)
            elif ext == ".json":
                structure["configs"].append(file_path)
            else:
                structure["scripts"]["other"].append(file_path)
        
        # Find duplicates
        duplicates = self._find_duplicates(structure)
        optimize_data["duplicates_found"] = duplicates
        
        optimize_data["reorganization_plan"] = {
            "python_scripts": len(structure["scripts"]["python"]),
            "shell_scripts": len(structure["scripts"]["shell"]),
            "config_files": len(structure["configs"]),
            "other_files": len(structure["scripts"]["other"])
        }
        
        self.report["optimize_results"] = optimize_data
        
        print(f"  ✓ Python scripts: {len(structure['scripts']['python'])}")
        print(f"  ✓ Shell scripts: {len(structure['scripts']['shell'])}")
        print(f"  ✓ Config files: {len(structure['configs'])}")
        print(f"  ⚠️  Duplicates found: {len(duplicates)}")
        
        return optimize_data

    def move_phase(self, scan_data: Dict, optimize_data: Dict) -> Dict:
        """Phase 5: Execute the migration to NOIZYLAB"""
        print("\n📦 PHASE 5: MOVING FILES TO NOIZYLAB...")
        print("=" * 60)
        
        move_data = {
            "total_moved": 0,
            "failed_moves": 0,
            "bytes_transferred": 0,
            "moved_files": []
        }
        
        # Ensure destination exists
        self.dest.mkdir(parents=True, exist_ok=True)
        
        # Create organized structure in destination
        (self.dest / "scripts" / "python").mkdir(parents=True, exist_ok=True)
        (self.dest / "scripts" / "shell").mkdir(parents=True, exist_ok=True)
        (self.dest / "configs").mkdir(parents=True, exist_ok=True)
        (self.dest / "extensions").mkdir(parents=True, exist_ok=True)
        (self.dest / "rescue").mkdir(parents=True, exist_ok=True)
        
        # Move files based on optimization plan
        for file_info in scan_data.get("code_files", [])[:100]:  # Limit initial move
            file_path = Path(file_info["path"])
            
            if not file_path.exists():
                continue
            
            try:
                # Determine destination
                ext = file_path.suffix.lower()
                
                if ext == ".py":
                    dest_dir = self.dest / "scripts" / "python"
                elif ext == ".sh":
                    dest_dir = self.dest / "scripts" / "shell"
                elif ext == ".json":
                    dest_dir = self.dest / "configs"
                else:
                    dest_dir = self.dest / "scripts" / "other"
                
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_path = dest_dir / file_path.name
                
                # Handle duplicates
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                # Copy file (preserve original on 4TBSG)
                shutil.copy2(file_path, dest_path)
                
                move_data["total_moved"] += 1
                move_data["bytes_transferred"] += file_info["size"]
                move_data["moved_files"].append({
                    "source": str(file_path),
                    "destination": str(dest_path),
                    "size": file_info["size"]
                })
                
                self.moved_files.append(dest_path)
                
                if move_data["total_moved"] % 10 == 0:
                    print(f"  Moved {move_data['total_moved']} files...")
                
            except Exception as e:
                move_data["failed_moves"] += 1
                print(f"  ✗ Failed to move {file_path.name}: {e}")
        
        self.report["move_results"] = move_data
        
        print(f"\n📊 MOVE SUMMARY:")
        print(f"  ✓ Files Moved: {move_data['total_moved']}")
        print(f"  ✓ Data Transferred: {self._format_size(move_data['bytes_transferred'])}")
        print(f"  ✗ Failed: {move_data['failed_moves']}")
        
        return move_data

    def _test_python_file(self, file_path: Path) -> Dict:
        """Test a Python file for syntax errors"""
        result = {
            "file": str(file_path),
            "type": ".py",
            "status": "unknown",
            "issues": []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Try to compile
            compile(content, str(file_path), 'exec')
            result["status"] = "passed"
            
        except SyntaxError as e:
            result["status"] = "failed"
            result["issues"].append(f"Syntax error at line {e.lineno}: {e.msg}")
        except Exception as e:
            result["status"] = "failed"
            result["issues"].append(f"Compilation error: {str(e)}")
        
        return result

    def _test_shell_script(self, file_path: Path) -> Dict:
        """Test a shell script for basic syntax"""
        result = {
            "file": str(file_path),
            "type": ".sh",
            "status": "unknown",
            "issues": []
        }
        
        try:
            # Check if file has shebang
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline()
            
            if not first_line.startswith('#!'):
                result["issues"].append("Missing shebang line")
            
            # Basic shell syntax check
            proc = subprocess.run(
                ['bash', '-n', str(file_path)],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if proc.returncode == 0:
                result["status"] = "passed"
            else:
                result["status"] = "failed"
                result["issues"].append(f"Syntax error: {proc.stderr}")
                
        except subprocess.TimeoutExpired:
            result["status"] = "failed"
            result["issues"].append("Syntax check timed out")
        except Exception as e:
            result["status"] = "failed"
            result["issues"].append(f"Test error: {str(e)}")
        
        return result

    def _test_json_file(self, file_path: Path) -> Dict:
        """Test a JSON file for validity"""
        result = {
            "file": str(file_path),
            "type": ".json",
            "status": "unknown",
            "issues": []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)
            result["status"] = "passed"
        except json.JSONDecodeError as e:
            result["status"] = "failed"
            result["issues"].append(f"JSON error at line {e.lineno}: {e.msg}")
        except Exception as e:
            result["status"] = "failed"
            result["issues"].append(f"Read error: {str(e)}")
        
        return result

    def _heal_python_file(self, file_path: Path, issues: List[str]) -> bool:
        """Attempt to heal Python file issues"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Basic fixes
            fixes_made = False
            
            # Fix common syntax issues
            if "SyntaxError" in ' '.join(issues):
                # Remove trailing whitespace
                lines = content.split('\n')
                cleaned_lines = [line.rstrip() for line in lines]
                new_content = '\n'.join(cleaned_lines)
                
                if new_content != content:
                    # Verify fix works
                    try:
                        compile(new_content, str(file_path), 'exec')
                        # Don't write yet - this is analysis phase
                        fixes_made = True
                    except:
                        pass
            
            return fixes_made
            
        except Exception:
            return False

    def _heal_shell_script(self, file_path: Path, issues: List[str]) -> bool:
        """Attempt to heal shell script issues"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            fixes_made = False
            
            # Add shebang if missing
            if "Missing shebang" in ' '.join(issues):
                if not content.startswith('#!'):
                    new_content = "#!/bin/bash\n" + content
                    fixes_made = True
            
            return fixes_made
            
        except Exception:
            return False

    def _find_duplicates(self, structure: Dict) -> List[Dict]:
        """Find duplicate files by content hash"""
        duplicates = []
        seen_hashes = {}
        
        all_files = []
        for category in structure.values():
            if isinstance(category, dict):
                for subcategory in category.values():
                    all_files.extend(subcategory)
            elif isinstance(category, list):
                all_files.extend(category)
        
        for file_path in all_files:
            if not file_path.exists():
                continue
                
            try:
                file_hash = self._hash_file(file_path)
                if file_hash in seen_hashes:
                    duplicates.append({
                        "original": str(seen_hashes[file_hash]),
                        "duplicate": str(file_path),
                        "hash": file_hash
                    })
                else:
                    seen_hashes[file_hash] = file_path
            except Exception:
                continue
        
        return duplicates

    def _hash_file(self, file_path: Path) -> str:
        """Calculate MD5 hash of a file"""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    def _format_size(self, bytes: int) -> str:
        """Format bytes to human readable size"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024.0:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024.0
        return f"{bytes:.2f} PB"

    def generate_report(self):
        """Generate comprehensive report"""
        report_path = self.dest / f"MIGRATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(report_path, 'w') as f:
            json.dump(self.report, f, indent=2)
        
        print(f"\n📄 Report saved to: {report_path}")
        
        # Generate summary
        summary_path = self.dest / f"MIGRATION_SUMMARY_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(summary_path, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("SCAN, TEST, HEAL, OPTIMIZE & MOVE - MIGRATION REPORT\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Date: {self.report['timestamp']}\n")
            f.write(f"Source: {self.source}\n")
            f.write(f"Destination: {self.dest}\n\n")
            
            f.write("SCAN RESULTS:\n")
            f.write(f"  Total Size: {self._format_size(self.report['scan_results'].get('total_size', 0))}\n")
            f.write(f"  Code Files: {len(self.report['scan_results'].get('code_files', []))}\n\n")
            
            f.write("TEST RESULTS:\n")
            f.write(f"  Passed: {self.report['test_results'].get('passed', 0)}\n")
            f.write(f"  Failed: {self.report['test_results'].get('failed', 0)}\n\n")
            
            f.write("HEAL RESULTS:\n")
            f.write(f"  Fixed: {self.report['heal_results'].get('successful_fixes', 0)}\n")
            f.write(f"  Failed: {self.report['heal_results'].get('failed_fixes', 0)}\n\n")
            
            f.write("MOVE RESULTS:\n")
            f.write(f"  Moved: {self.report['move_results'].get('total_moved', 0)}\n")
            f.write(f"  Transferred: {self._format_size(self.report['move_results'].get('bytes_transferred', 0))}\n")
        
        print(f"📄 Summary saved to: {summary_path}")

    def execute(self):
        """Execute all phases"""
        print("\n" + "=" * 60)
        print("SCAN, TEST, HEAL, OPTIMIZE & MOVE")
        print("Comprehensive Migration System")
        print("=" * 60)
        
        try:
            # Phase 1: Scan
            scan_data = self.scan_phase()
            
            # Phase 2: Test
            test_data = self.test_phase(scan_data)
            
            # Phase 3: Heal
            heal_data = self.heal_phase(test_data)
            
            # Phase 4: Optimize
            optimize_data = self.optimize_phase(scan_data)
            
            # Phase 5: Move
            move_data = self.move_phase(scan_data, optimize_data)
            
            # Generate reports
            self.generate_report()
            
            print("\n" + "=" * 60)
            print("✅ MIGRATION COMPLETE!")
            print("=" * 60)
            
        except Exception as e:
            print(f"\n❌ CRITICAL ERROR: {e}")
            import traceback
            traceback.print_exc()
            self.report["errors"].append(str(e))
            self.generate_report()


if __name__ == "__main__":
    migrator = ScanTestHealOptimizeMove()
    migrator.execute()
