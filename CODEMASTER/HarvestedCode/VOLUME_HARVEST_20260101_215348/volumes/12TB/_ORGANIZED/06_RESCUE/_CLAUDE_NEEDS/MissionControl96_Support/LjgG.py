cd
#!/usr/bin/env python3
"""
Native Instruments File Organizer - Auto Version
Specifically handles Kirk Hunter Orchestra and other NI libraries
"""

import os
import shutil
import re
from pathlib import Path
from collections import defaultdict
import difflib

class NIFileOrganizer:
    def __init__(self):
        self.desktop_path = Path.home() / "Desktop"
        self.kontakt_lab_path = self.desktop_path / "KONTAKT_LAB"
        self.ni_extensions = ['.nki', '.nkm', '.nkc']
        self.found_files = []
        
        # Known library patterns for better organization
        self.library_patterns = {
            'kirk': 'Kirk_Hunter_Orchestra',
            'hunter': 'Kirk_Hunter_Orchestra',
            'orchestra': 'Kirk_Hunter_Orchestra',
            'heavyocity': 'Heavyocity',
            'output': 'Output',
            'spitfire': 'Spitfire_Audio',
            'eastwest': 'EastWest',
            'native': 'Native_Instruments',
            'arturia': 'Arturia',
            'spectrasonics': 'Spectrasonics',
            'cinematique': 'Cinematique_Instruments'
        }
        
    def create_kontakt_lab_folder(self):
        self.kontakt_lab_path.mkdir(exist_ok=True)
        print(f"✓ KONTAKT_LAB folder ready at: {self.kontakt_lab_path}")
        
    def scan_for_ni_files(self, search_paths):
        print("🔍 Scanning for Native Instruments files (.nki, .nkm, .nkc)...")
        
        for search_path in search_paths:
            if not search_path.exists():
                continue
                
            print(f"  📂 Scanning: {search_path}")
            
            try:
                for root, dirs, files in os.walk(search_path):
                    # Skip system directories but keep music/audio related ones
                    dirs[:] = [d for d in dirs if not d.startswith('.') and 
                              d.lower() not in ['system', 'library', 'usr', 'var', 'tmp', 'bin', 'sbin']]
                    
                    for file in files:
                        if any(file.lower().endswith(ext) for ext in self.ni_extensions):
                            file_path = Path(root) / file
                            self.found_files.append(file_path)
                            
                            # Special notification for Kirk Hunter Orchestra
                            if 'kirk' in str(file_path).lower() or 'hunter' in str(file_path).lower():
                                print(f"    🎼 KIRK HUNTER ORCHESTRA: {file}")
                            else:
                                print(f"    🎵 Found: {file}")
                            
            except (PermissionError, OSError):
                print(f"    ⚠️  Skipping {search_path}: Access denied")
                continue
            except Exception as e:
                print(f"    ⚠️  Error scanning {search_path}: {e}")
                continue
    
    def extract_library_name(self, file_path):
        path_str = str(file_path).lower()
        
        # Check for known library patterns first
        for pattern, library_name in self.library_patterns.items():
            if pattern in path_str:
                return library_name
        
        # Extract from path components
        path_parts = file_path.parts
        
        for part in reversed(path_parts):
            part_lower = part.lower()
            
            # Skip common folder names
            if part_lower in ['kontakt', 'instruments', 'samples', 'libraries', 'library']:
                continue
            
            # Skip version numbers
            if re.search(r'v?\d+[\.\d]*$', part_lower):
                continue
                
            # Use meaningful directory names
            if len(part) > 3 and not part.startswith('.'):
                cleaned = self.clean_library_name(part)
                if cleaned != "Unknown_Library":
                    return cleaned
        
        return "Unknown_Library"
    
    def clean_library_name(self, name):
        # Remove version numbers and common suffixes
        cleaned = re.sub(r'v?\d+[\.\d]*', '', name, flags=re.IGNORECASE)
        cleaned = re.sub(r'(library|collection|pack|instrument|sample|kontakt)$', '', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'[^\w\s\-]', '', cleaned)
        cleaned = re.sub(r'\s+', '_', cleaned.strip())
        cleaned = re.sub(r'_+', '_', cleaned)
        cleaned = cleaned.strip('_')
        
        return cleaned if len(cleaned) > 2 else "Unknown_Library"
    
    def organize_files(self):
        if not self.found_files:
            print("❌ No Native Instruments files found!")
            return False
        
        print(f"\n📦 Organizing {len(self.found_files)} files by library...")
        
        # Group files by library
        library_groups = defaultdict(list)
        
        for file_path in self.found_files:
            library_name = self.extract_library_name(file_path)
            library_groups[library_name].append(file_path)
        
        print(f"📚 Detected {len(library_groups)} library groups:")
        for lib_name, files in library_groups.items():
            if 'kirk' in lib_name.lower():
                print(f"  🎼 {lib_name}: {len(files)} files (KIRK HUNTER ORCHESTRA)")
            else:
                print(f"  - {lib_name}: {len(files)} files")
        
        # Organize files
        moved_count = 0
        
        for library_name, files in library_groups.items():
            library_folder = self.kontakt_lab_path / library_name
            library_folder.mkdir(exist_ok=True)
            
            print(f"\n📁 Processing: {library_name}")
            
            for file_path in files:
                try:
                    dest_path = library_folder / file_path.name
                    
                    # Handle duplicates
                    counter = 1
                    original_dest = dest_path
                    while dest_path.exists():
                        stem = original_dest.stem
                        suffix = original_dest.suffix
                        dest_path = library_folder / f"{stem}_{counter}{suffix}"
                        counter += 1
                    
                    # Copy the file
                    shutil.copy2(file_path, dest_path)
                    print(f"  ✓ Copied: {file_path.name}")
                    moved_count += 1
                    
                except Exception as e:
                    print(f"  ❌ Error copying {file_path.name}: {e}")
        
        print(f"\n🎉 Organization Complete!")
        print(f"   ✓ Successfully copied: {moved_count} files")
        print(f"   📍 Location: {self.kontakt_lab_path}")
        
        return moved_count > 0
    
    def run(self):
        print("🎵 NATIVE INSTRUMENTS KONTAKT FILE ORGANIZER")
        print("🎼 Special Focus: Kirk Hunter Orchestra")
        print("=" * 60)
        
        self.create_kontakt_lab_folder()
        
        # Comprehensive search locations
        search_paths = [
            Path("/Volumes"),  # All mounted volumes
            Path.home(),
            Path("/Applications"),
            Path.home() / "Documents",
            Path.home() / "Music",
            Path.home() / "Desktop",
            Path.home() / "Downloads",
            Path.home() / "Library" / "Audio",
            Path("/Library/Audio"),
        ]
        
        # Add any existing volumes
        volumes_path = Path("/Volumes")
        if volumes_path.exists():
            for volume in volumes_path.iterdir():
                if volume.is_dir() and not volume.name.startswith('.'):
                    search_paths.append(volume)
                    print(f"📀 Will scan volume: {volume.name}")
        
        # Remove duplicates and non-existent paths
        search_paths = [path for path in set(search_paths) if path.exists()]
        
        print(f"\n🔍 Scanning {len(search_paths)} locations...")
        
        self.scan_for_ni_files(search_paths)
        success = self.organize_files()
        
        if success:
            print(f"\n🚀 Opening KONTAKT_LAB folder...")
            os.system(f'open "{self.kontakt_lab_path}"')
        
        print("\n✨ Organization complete!")

# Auto-run the organizer
if __name__ == "__main__":
    organizer = NIFileOrganizer()
    organizer.run()
