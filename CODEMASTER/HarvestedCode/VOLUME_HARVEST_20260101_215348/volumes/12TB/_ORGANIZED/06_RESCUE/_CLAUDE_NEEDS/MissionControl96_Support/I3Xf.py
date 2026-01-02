#!/usr/bin/env python3
"""
NOIZYGENIE Arsenal Manager - Enhanced Edition
Organizes Native Instruments files while preserving complete library integrity
"""

import os
import shutil
import re
import time
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import difflib
import json
import os

class NOIZYGENIEArsenalManager:
    def __init__(self):
        self.base_path = Path.home() / "Desktop" / "KONTAKT_LAB"
        self.ni_extensions = ['.nki', '.nkm', '.nkc', '.ncw', '.wav', '.aiff']
        self.library_threshold = 5  # minimum files to be considered a library
        self.volume_paths = [
            Path("/Volumes/6TB"),
            Path("/Volumes/4TB BLK"),
            Path("/Volumes/4TB Lacie"),
            Path("/Volumes/RED DRAGON"),
            Path("/Volumes/Mission Control")
        ]
        
        # Setup reports directory and files
        self.reports_dir = self.base_path / "REPORTS"
        self.reports_dir.mkdir(exist_ok=True)
        self.snapshot_file = self.reports_dir / "last_snapshot.json"
        self.history_file = self.reports_dir / "arsenal_history.log"
        
    def create_kontakt_lab_folder(self):
        """Create the KONTAKT_LAB folder on Desktop if it doesn't exist"""
        self.kontakt_lab_path.mkdir(exist_ok=True)
        print(f"✓ KONTAKT_LAB folder ready at: {self.kontakt_lab_path}")
        
    def find_mission_control_volumes(self):
        """Find potential Mission Control or similar volumes"""
        volumes_path = Path("/Volumes")
        mission_control_volumes = []
        
        if volumes_path.exists():
            for volume in volumes_path.iterdir():
                if volume.is_dir():
                    volume_name = volume.name.lower()
                    # Look for volumes that might contain Mission Control or similar
                    if any(keyword in volume_name for keyword in ['mission', 'control', 'audio', 'music', 'samples', 'library']):
                        mission_control_volumes.append(volume)
                    # Also check all volumes just in case
                    else:
                        mission_control_volumes.append(volume)
        
        return mission_control_volumes
    
    def scan_for_ni_files(self, search_paths):
        """Recursively scan for Native Instruments files"""
        print("🔍 Scanning for Native Instruments files...")
        
        for search_path in search_paths:
            if not search_path.exists():
                continue
                
            print(f"  Scanning: {search_path}")
            
            try:
                for root, dirs, files in os.walk(search_path):
                    # Skip hidden directories and common system folders
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['System', 'Library', 'usr', 'var', 'tmp']]
                    
                    for file in files:
                        if any(file.lower().endswith(ext) for ext in self.ni_extensions):
                            file_path = Path(root) / file
                            self.found_files.append(file_path)
                            print(f"    Found: {file}")
                            
            except PermissionError:
                print(f"    ⚠️  Permission denied: {search_path}")
                continue
            except Exception as e:
                print(f"    ⚠️  Error scanning {search_path}: {e}")
                continue
    
    def extract_library_name(self, file_path):
        """Extract potential library name from file path or name"""
        path_parts = file_path.parts
        file_name = file_path.stem
        
        # Common patterns for library identification
        library_patterns = [
            # Look for common library folder patterns
            r'(Kontakt|Libraries?|Instruments?|Samples?)',
            # Look for manufacturer names
            r'(Native Instruments?|NI|Heavyocity|Output|Spitfire|East West)',
            # Look for product names in path
            r'([A-Z][a-zA-Z\s]+(?:Library|Collection|Pack|Instruments?))',
        ]
        
        # Try to find library name in path
        for part in reversed(path_parts):
            part_clean = re.sub(r'[_\-\.]', ' ', part)
            for pattern in library_patterns:
                match = re.search(pattern, part_clean, re.IGNORECASE)
                if match:
                    return self.clean_library_name(match.group(1))
        
        # Try to extract from filename
        file_clean = re.sub(r'[_\-\.]', ' ', file_name)
        
        # Look for common prefixes/patterns in filename
        common_prefixes = re.findall(r'^([A-Z][a-zA-Z]+)', file_clean)
        if common_prefixes:
            return self.clean_library_name(common_prefixes[0])
        
        # Fallback: use parent directory name
        if len(path_parts) > 1:
            return self.clean_library_name(path_parts[-2])
        
        return "Unknown_Library"
    
    def clean_library_name(self, name):
        """Clean and standardize library names"""
        # Remove common suffixes and clean up
        cleaned = re.sub(r'(Library|Collection|Pack|Instruments?|Samples?)', '', name, flags=re.IGNORECASE)
        cleaned = re.sub(r'[^\w\s]', '', cleaned)
        cleaned = re.sub(r'\s+', '_', cleaned.strip())
        return cleaned or "Unknown_Library"
    
    def group_similar_libraries(self, library_groups):
        """Group libraries with similar names"""
        library_names = list(library_groups.keys())
        merged_groups = {}
        processed = set()
        
        for lib_name in library_names:
            if lib_name in processed:
                continue
                
            # Find similar library names
            similar_libs = [lib_name]
            for other_lib in library_names:
                if other_lib != lib_name and other_lib not in processed:
                    # Check similarity using difflib
                    similarity = difflib.SequenceMatcher(None, lib_name.lower(), other_lib.lower()).ratio()
                    if similarity > 0.7:  # 70% similarity threshold
                        similar_libs.append(other_lib)
            
            # Use the most common/longest name as the group name
            group_name = max(similar_libs, key=len)
            
            # Merge all files from similar libraries
            merged_files = []
            for similar_lib in similar_libs:
                merged_files.extend(library_groups[similar_lib])
                processed.add(similar_lib)
            
            merged_groups[group_name] = merged_files
        
        return merged_groups
    
    def organize_files(self):
        """Organize files by library groups"""
        if not self.found_files:
            print("❌ No Native Instruments files found!")
            return
        
        print(f"\n📦 Organizing {len(self.found_files)} files by library...")
        
        # Group files by potential library
        library_groups = defaultdict(list)
        
        for file_path in self.found_files:
            library_name = self.extract_library_name(file_path)
            library_groups[library_name].append(file_path)
        
        # Merge similar library groups
        merged_groups = self.group_similar_libraries(library_groups)
        
        print(f"📚 Found {len(merged_groups)} library groups:")
        for lib_name, files in merged_groups.items():
            print(f"  - {lib_name}: {len(files)} files")
        
        # Create folders and move files
        moved_count = 0
        for library_name, files in merged_groups.items():
            library_folder = self.kontakt_lab_path / library_name
            library_folder.mkdir(exist_ok=True)
            
            print(f"\n📁 Processing library: {library_name}")
            
            for file_path in files:
                try:
                    dest_path = library_folder / file_path.name
                    
                    # Handle duplicate names
                    counter = 1
                    original_dest = dest_path
                    while dest_path.exists():
                        stem = original_dest.stem
                        suffix = original_dest.suffix
                        dest_path = library_folder / f"{stem}_{counter}{suffix}"
                        counter += 1
                    
                    shutil.copy2(file_path, dest_path)
                    print(f"  ✓ Moved: {file_path.name}")
                    moved_count += 1
                    
                except Exception as e:
                    print(f"  ❌ Error moving {file_path.name}: {e}")
        
        print(f"\n🎉 Successfully organized {moved_count} files into {len(merged_groups)} library folders!")
        print(f"📍 Location: {self.kontakt_lab_path}")
    
    def run(self):
        """Main execution method"""
        print("🎵 Native Instruments File Organizer")
        print("=" * 50)
        
        # Create KONTAKT_LAB folder
        self.create_kontakt_lab_folder()
        
        # Find volumes to search
        volumes = self.find_mission_control_volumes()
        
        # Also search common locations
        search_paths = volumes + [
            Path.home(),  # User home directory
            Path("/Applications"),  # Applications folder
            Path.home() / "Documents",  # Documents
            Path.home() / "Music",  # Music folder
        ]
        
        print(f"\n🔍 Will search {len(search_paths)} locations:")
        for path in search_paths:
            print(f"  - {path}")
        
        # Scan for files
        self.scan_for_ni_files(search_paths)
        
        # Organize files
        self.organize_files()

if __name__ == "__main__":
    arsenal_mgr = NOIZYGENIEArsenalManager()
    arsenal_mgr.run()