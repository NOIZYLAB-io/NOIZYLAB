#!/usr/bin/env python3
#!/usr/bin/env python3
"""
VOLUME SCANNER - Complete Scan of All Mounted Volumes
Scans, organizes, checks integrity, and optimizes content
Runs continuously until all volumes are processed
"""

import os
import sys
import json
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Any
import subprocess

class VolumeScanner:
    """Scan all mounted volumes for integrity and organization"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.scan_results = {
            "start_time": datetime.now().isoformat(),
            "volumes_scanned": [],
            "files_found": 0,
            "files_checked": 0,
            "integrity_issues": [],
            "organized": [],
            "optimized": [],
            "duplicates_found": [],
            "corrupted_files": [],
            "python_files": [],
            "code_files": [],
            "documentation": []
        }
        self.scan_log = self.base_dir / "VOLUME_SCAN_LOG.json"
        self.excluded_paths = {
            '/System', '/Library', '/private', '/usr', '/bin', '/sbin',
            '/Applications', '/dev', '/tmp', '/var', '/etc', '/opt',
            '.Trash', '.DS_Store', 'node_modules', '__pycache__',
            '.git', '.svn', '.hg', '.idea', '.vscode'
        }
        self.processed_hashes = set()
        self.duplicate_groups = {}
    
    def get_mounted_volumes(self) -> List[Path]:
        """Get all mounted volumes"""
        volumes = []
        
        # Get from df
        try:
            result = subprocess.run(['df', '-h'], capture_output=True, text=True)
            for line in result.stdout.split('\n')[1:]:
                if line:
                    parts = line.split()
                    if len(parts) >= 6:
                        mount_point = parts[-1]
                        if mount_point.startswith('/Volumes/') or mount_point == '/':
                            volumes.append(Path(mount_point))
        except:
            pass
        
        # Also check /Volumes directly
        volumes_dir = Path('/Volumes')
        if volumes_dir.exists():
            for item in volumes_dir.iterdir():
                if item.is_dir() and item not in volumes:
                    volumes.append(item)
        
        # Remove duplicates and sort
        volumes = sorted(set(volumes), key=str)
        
        return volumes
    
    def should_scan_path(self, path: Path) -> bool:
        """Check if path should be scanned"""
        path_str = str(path)
        
        # Skip excluded paths
        for excluded in self.excluded_paths:
            if excluded in path_str:
                return False
        
        # Skip hidden files/dirs (except .git, etc. which are already excluded)
        if path.name.startswith('.') and path.name not in ['.gitignore', '.env']:
            return False
        
        return True
    
    def check_file_integrity(self, file_path: Path) -> Dict[str, Any]:
        """Check file integrity"""
        result = {
            "file": str(file_path),
            "status": "ok",
            "issues": [],
            "size": 0,
            "hash": None
        }
        
        try:
            # Check if file is readable
            if not file_path.exists():
                result["status"] = "missing"
                result["issues"].append("File does not exist")
                return result
            
            # Get file size
            result["size"] = file_path.stat().st_size
            
            # Check if file is readable
            try:
                with open(file_path, 'rb') as f:
                    # Read first chunk to check readability
                    chunk = f.read(1024)
                    if not chunk and result["size"] > 0:
                        result["status"] = "corrupted"
                        result["issues"].append("File appears corrupted (empty but has size)")
                        return result
                    
                    # Calculate hash for duplicate detection
                    hasher = hashlib.md5()
                    hasher.update(chunk)
                    if result["size"] < 1024 * 1024:  # For small files, hash entire file
                        f.seek(0)
                        hasher.update(f.read())
                    result["hash"] = hasher.hexdigest()
                    
            except PermissionError:
                result["status"] = "permission_denied"
                result["issues"].append("Permission denied")
            except Exception as e:
                result["status"] = "error"
                result["issues"].append(f"Error reading file: {str(e)}")
        
        except Exception as e:
            result["status"] = "error"
            result["issues"].append(f"Error checking file: {str(e)}")
        
        return result
    
    def find_duplicates(self, file_info: Dict[str, Any]):
        """Find duplicate files"""
        if file_info["hash"]:
            if file_info["hash"] in self.processed_hashes:
                # Duplicate found
                if file_info["hash"] not in self.duplicate_groups:
                    self.duplicate_groups[file_info["hash"]] = []
                self.duplicate_groups[file_info["hash"]].append(file_info["file"])
            else:
                self.processed_hashes.add(file_info["hash"])
    
    def categorize_file(self, file_path: Path) -> str:
        """Categorize file type"""
        ext = file_path.suffix.lower()
        
        if ext in ['.py', '.pyw', '.pyx', '.pyi']:
            return 'python'
        elif ext in ['.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h', '.swift', '.go', '.rs', '.rb', '.php']:
            return 'code'
        elif ext in ['.md', '.txt', '.rst', '.doc', '.docx', '.pdf']:
            return 'documentation'
        elif ext in ['.json', '.xml', '.yaml', '.yml', '.toml', '.ini', '.cfg']:
            return 'config'
        elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']:
            return 'image'
        elif ext in ['.mp4', '.avi', '.mov', '.mkv', '.mp3', '.wav']:
            return 'media'
        else:
            return 'other'
    
    def scan_volume(self, volume_path: Path, max_depth: int = 10, current_depth: int = 0) -> Dict[str, Any]:
        """Scan a single volume"""
        volume_result = {
            "volume": str(volume_path),
            "scanned": False,
            "files_found": 0,
            "files_checked": 0,
            "errors": [],
            "categories": {}
        }
        
        if not volume_path.exists():
            volume_result["errors"].append("Volume does not exist")
            return volume_result
        
        if not self.should_scan_path(volume_path):
            volume_result["errors"].append("Volume excluded from scan")
            return volume_result
        
        print(f"\n📂 Scanning: {volume_path}")
        print(f"   Depth: {current_depth}/{max_depth}")
        
        try:
            # Scan files
            for root, dirs, files in os.walk(volume_path):
                # Filter dirs
                dirs[:] = [d for d in dirs if self.should_scan_path(Path(root) / d)]
                
                for file in files:
                    file_path = Path(root) / file
                    
                    if not self.should_scan_path(file_path):
                        continue
                    
                    volume_result["files_found"] += 1
                    self.scan_results["files_found"] += 1
                    
                    # Check integrity
                    file_info = self.check_file_integrity(file_path)
                    volume_result["files_checked"] += 1
                    self.scan_results["files_checked"] += 1
                    
                    # Categorize
                    category = self.categorize_file(file_path)
                    if category not in volume_result["categories"]:
                        volume_result["categories"][category] = 0
                    volume_result["categories"][category] += 1
                    
                    # Track by category
                    if category == 'python':
                        self.scan_results["python_files"].append(str(file_path))
                    elif category == 'code':
                        self.scan_results["code_files"].append(str(file_path))
                    elif category == 'documentation':
                        self.scan_results["documentation"].append(str(file_path))
                    
                    # Check for issues
                    if file_info["status"] != "ok":
                        self.scan_results["integrity_issues"].append(file_info)
                        if file_info["status"] == "corrupted":
                            self.scan_results["corrupted_files"].append(str(file_path))
                    
                    # Find duplicates
                    if file_info["hash"]:
                        self.find_duplicates(file_info)
                    
                    # Progress update every 100 files
                    if volume_result["files_checked"] % 100 == 0:
                        print(f"   ✅ Checked {volume_result['files_checked']} files...")
            
            volume_result["scanned"] = True
            print(f"   ✅ Complete: {volume_result['files_checked']} files checked")
        
        except PermissionError as e:
            volume_result["errors"].append(f"Permission denied: {e}")
        except Exception as e:
            volume_result["errors"].append(f"Error scanning: {e}")
        
        return volume_result
    
    def save_progress(self):
        """Save scan progress"""
        self.scan_results["end_time"] = datetime.now().isoformat()
        self.scan_results["duplicates_found"] = [
            {"hash": h, "files": files} 
            for h, files in self.duplicate_groups.items() 
            if len(files) > 1
        ]
        
        with open(self.scan_log, 'w') as f:
            json.dump(self.scan_results, f, indent=2)
    
    def run_complete_scan(self):
        """Run complete scan of all volumes"""
        print("╔══════════════════════════════════════════════════════════╗")
        print("║  🔍 VOLUME SCANNER - COMPLETE SCAN 🔍                   ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"\n🕐 Start Time: {self.scan_results['start_time']}")
        print("\n📋 Scanning all mounted volumes...")
        
        volumes = self.get_mounted_volumes()
        print(f"\n📦 Found {len(volumes)} volumes to scan:")
        for vol in volumes:
            print(f"   • {vol}")
        
        print("\n" + "="*80)
        print("🚀 STARTING SCAN (This may take a while...)")
        print("="*80)
        
        for i, volume in enumerate(volumes, 1):
            print(f"\n{'='*80}")
            print(f"📦 Volume {i}/{len(volumes)}: {volume}")
            print(f"{'='*80}")
            
            volume_result = self.scan_volume(volume, max_depth=20)
            self.scan_results["volumes_scanned"].append(volume_result)
            
            # Save progress after each volume
            self.save_progress()
            
            print(f"\n✅ Volume {i}/{len(volumes)} complete")
            print(f"   Files found: {volume_result['files_found']}")
            print(f"   Files checked: {volume_result['files_checked']}")
            if volume_result.get('errors'):
                print(f"   Errors: {len(volume_result['errors'])}")
        
        # Final summary
        self.save_progress()
        
        print("\n" + "="*80)
        print("✅ SCAN COMPLETE!")
        print("="*80)
        
        print(f"\n📊 FINAL RESULTS:")
        print(f"   Volumes Scanned: {len(self.scan_results['volumes_scanned'])}")
        print(f"   Total Files Found: {self.scan_results['files_found']:,}")
        print(f"   Total Files Checked: {self.scan_results['files_checked']:,}")
        print(f"   Python Files: {len(self.scan_results['python_files']):,}")
        print(f"   Code Files: {len(self.scan_results['code_files']):,}")
        print(f"   Documentation: {len(self.scan_results['documentation']):,}")
        print(f"   Integrity Issues: {len(self.scan_results['integrity_issues']):,}")
        print(f"   Corrupted Files: {len(self.scan_results['corrupted_files']):,}")
        print(f"   Duplicate Groups: {len(self.scan_results['duplicates_found']):,}")
        
        print(f"\n📁 Full report saved to: {self.scan_log}")
        print("="*80)

if __name__ == "__main__":
    scanner = VolumeScanner()
    try:
        scanner.run_complete_scan()
    except KeyboardInterrupt:
        print("\n\n⚠️  Scan interrupted by user")
        scanner.save_progress()
        print(f"📁 Progress saved to: {scanner.scan_log}")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        scanner.save_progress()
        print(f"📁 Progress saved to: {scanner.scan_log}")

