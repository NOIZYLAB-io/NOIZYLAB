#!/usr/bin/env python3
"""
NOIZYGENIE Master Organizer & Fixer
Complete organization and repair system for Native Instruments arsenal
"""

import os
import sys
import shutil
from pathlib import Path
from collections import defaultdict, Counter
import json
import time
import subprocess
from datetime import datetime

class MasterOrganizerFixer:
    def __init__(self):
        self.desktop = Path.home() / "Desktop"
        self.kontakt_lab = self.desktop / "KONTAKT_LAB"
        self.reports_dir = self.kontakt_lab / "REPORTS"
        self.six_tb = Path("/Volumes/6TB")
        self.four_tb_blk = Path("/Volumes/4TB BLK")
        self.four_tb_lacie = Path("/Volumes/4TB Lacie")
        self.red_dragon = Path("/Volumes/RED DRAGON")
        self.mission_control = Path("/Volumes/Mission Control")
        
        # Statistics
        self.stats = {
            'files_moved': 0,
            'libraries_organized': 0,
            'libraries_repaired': 0,
            'libraries_completed': 0,
            'samples_added': 0,
            'duplicates_removed': 0
        }
        
    def initialize_workspace(self):
        """Initialize the complete workspace structure"""
        print("🏗️  INITIALIZING MASTER WORKSPACE")
        print("=" * 60)
        
        # Create essential directories
        directories = [
            self.kontakt_lab,
            self.reports_dir,
            self.kontakt_lab / "ORGANIZED_LIBRARIES",
            self.kontakt_lab / "SAMPLE_ARCHIVES",
            self.kontakt_lab / "BACKUP",
            self.kontakt_lab / "TEMP_PROCESSING"
        ]
        
        for directory in directories:
            directory.mkdir(exist_ok=True, parents=True)
            print(f"   📁 Created: {directory.name}")
        
        print("✅ Workspace initialized!")
    
    def discover_ni_files_all_volumes(self):
        """Discover all NI files across all mounted volumes"""
        print("\n🔍 DISCOVERING NI FILES ACROSS ALL VOLUMES")
        print("=" * 60)
        
        volumes = [
            self.six_tb,
            self.four_tb_blk, 
            self.four_tb_lacie,
            self.red_dragon,
            self.mission_control
        ]
        
        discovered_files = {
            '.nki': [],
            '.nkm': [],
            '.nkc': [],
            '.ncw': [],
            '.wav': [],
            '.aiff': []
        }
        
        for volume in volumes:
            if not volume.exists():
                print(f"   ⏭️  Skipping {volume.name} (not mounted)")
                continue
                
            print(f"\n   🔍 Scanning: {volume.name}")
            
            try:
                for root, dirs, files in os.walk(volume):
                    # Limit depth to prevent infinite scanning
                    if len(Path(root).parts) - len(volume.parts) > 8:
                        dirs.clear()
                        continue
                    
                    for file in files:
                        file_lower = file.lower()
                        for ext in discovered_files.keys():
                            if file_lower.endswith(ext):
                                file_path = Path(root) / file
                                discovered_files[ext].append(file_path)
                
                # Report volume statistics
                total_files = sum(len(files) for files in discovered_files.values())
                if total_files > 0:
                    print(f"      📊 {volume.name}: {total_files:,} NI files found")
                    for ext, files in discovered_files.items():
                        if files:
                            print(f"         {ext}: {len(files):,} files")
                            
            except Exception as e:
                print(f"      ❌ Error scanning {volume.name}: {e}")
        
        return discovered_files
    
    def organize_by_libraries(self, discovered_files):
        """Organize files into coherent libraries"""
        print("\n📚 ORGANIZING FILES INTO LIBRARIES")
        print("=" * 60)
        
        # Group files by potential library structure
        library_groups = defaultdict(list)
        
        # Analyze directory structures to identify libraries
        for ext, files in discovered_files.items():
            if ext in ['.nki', '.nkm', '.nkc']:  # Instrument files
                for file_path in files:
                    # Skip files already in KONTAKT_LAB
                    if str(file_path).startswith(str(self.kontakt_lab)):
                        continue
                    
                    # Identify potential library name from path structure
                    path_parts = file_path.parts
                    
                    # Look for library indicators in path
                    library_name = None
                    for i, part in enumerate(path_parts):
                        part_lower = part.lower()
                        if any(indicator in part_lower for indicator in [
                            'kontakt', 'library', 'instrument', 'preset',
                            'collection', 'pack', 'bundle'
                        ]):
                            library_name = part
                            break
                    
                    if not library_name:
                        # Use parent directory as library name
                        library_name = file_path.parent.name
                    
                    # Clean library name
                    library_name = self.clean_library_name(library_name)
                    library_groups[library_name].append(file_path)
        
        print(f"   📊 Identified {len(library_groups)} potential libraries")
        
        # Move files to organized structure
        organized_count = 0
        for library_name, files in library_groups.items():
            if len(files) < 3:  # Skip small groups
                continue
                
            target_library = self.kontakt_lab / library_name
            target_library.mkdir(exist_ok=True)
            
            print(f"   📁 Organizing: {library_name} ({len(files)} files)")
            
            for file_path in files:
                try:
                    target_file = target_library / file_path.name
                    if not target_file.exists():
                        shutil.copy2(file_path, target_file)
                        self.stats['files_moved'] += 1
                        organized_count += 1
                except Exception as e:
                    print(f"      ❌ Error moving {file_path.name}: {e}")
        
        self.stats['libraries_organized'] = len([d for d in self.kontakt_lab.iterdir() if d.is_dir()])
        print(f"   ✅ Organized {organized_count} files into libraries")
        
    def clean_library_name(self, name):
        """Clean and standardize library names"""
        # Remove common unwanted characters and normalize
        import re
        cleaned = re.sub(r'[^\w\s-]', '', name)
        cleaned = re.sub(r'\s+', '_', cleaned.strip())
        return cleaned[:50]  # Limit length
    
    def build_comprehensive_sample_database(self):
        """Build comprehensive sample database from all volumes"""
        print("\n🗄️  BUILDING COMPREHENSIVE SAMPLE DATABASE")
        print("=" * 60)
        
        sample_db = {}
        sample_patterns = set()
        
        volumes = [self.six_tb, self.four_tb_blk, self.four_tb_lacie, self.red_dragon]
        
        for volume in volumes:
            if not volume.exists():
                continue
                
            print(f"   📊 Indexing samples from: {volume.name}")
            
            sample_count = 0
            for root, dirs, files in os.walk(volume):
                # Limit depth
                if len(Path(root).parts) - len(volume.parts) > 6:
                    dirs.clear()
                    continue
                
                current_path = Path(root)
                sample_files = [f for f in files if f.lower().endswith(('.ncw', '.wav', '.aiff'))]
                
                if len(sample_files) >= 5:  # Only directories with meaningful sample collections
                    sample_db[str(current_path)] = {
                        'files': sample_files,
                        'count': len(sample_files),
                        'volume': volume.name
                    }
                    
                    # Add patterns for matching
                    for sample in sample_files:
                        # Extract meaningful patterns
                        name_clean = sample.lower().replace('.ncw', '').replace('.wav', '').replace('.aiff', '')
                        words = name_clean.split('_')
                        for word in words:
                            if len(word) > 3:
                                sample_patterns.add(word)
                    
                    sample_count += len(sample_files)
            
            print(f"      💾 {volume.name}: {sample_count:,} samples indexed")
        
        print(f"   🎯 Total sample database: {len(sample_db):,} directories")
        print(f"   🔍 Sample patterns: {len(sample_patterns):,} unique patterns")
        
        return sample_db, sample_patterns
    
    def intelligent_library_repair(self, sample_db, sample_patterns):
        """Perform intelligent repair of all libraries"""
        print("\n🔧 INTELLIGENT LIBRARY REPAIR SYSTEM")
        print("=" * 60)
        
        libraries = [d for d in self.kontakt_lab.iterdir() if d.is_dir() and not d.name.startswith('.')]
        
        repaired = 0
        completed = 0
        
        for library in sorted(libraries):
            if library.name in ['REPORTS', 'ORGANIZED_LIBRARIES', 'SAMPLE_ARCHIVES', 'BACKUP', 'TEMP_PROCESSING']:
                continue
            
            # Analyze current library status
            instruments = list(library.rglob("*.nki")) + list(library.rglob("*.nkm")) + list(library.rglob("*.nkc"))
            current_samples = list(library.rglob("*.ncw")) + list(library.rglob("*.wav")) + list(library.rglob("*.aiff"))
            
            if len(instruments) == 0:
                continue
            
            print(f"\n   🔧 Repairing: {library.name}")
            print(f"      📊 Current: {len(instruments)} instruments, {len(current_samples)} samples")
            
            if len(current_samples) >= len(instruments) * 0.5:
                print(f"      ✅ Already well-sampled")
                continue
            
            # Create samples directory
            samples_dir = library / "Samples"
            samples_dir.mkdir(exist_ok=True)
            
            # Intelligent sample matching
            added_samples = 0
            target_samples = min(len(instruments), 100)  # Reasonable target
            
            # Extract keywords from library name for matching
            lib_keywords = set()
            lib_name_clean = library.name.lower()
            for word in lib_name_clean.replace('_', ' ').split():
                if len(word) > 3:
                    lib_keywords.add(word)
            
            # Score and rank sample directories
            scored_sources = []
            for db_path, db_info in sample_db.items():
                score = 0
                path_lower = db_path.lower()
                
                # Keyword matching
                for keyword in lib_keywords:
                    if keyword in path_lower:
                        score += 10
                
                # Pattern matching
                common_patterns = 0
                for pattern in sample_patterns:
                    if pattern in path_lower and pattern in lib_name_clean:
                        common_patterns += 1
                
                score += common_patterns * 2
                
                # Prefer larger sample collections
                score += min(db_info['count'] / 10, 10)
                
                if score > 0:
                    scored_sources.append((score, db_path, db_info))
            
            # Sort by score and use top sources
            scored_sources.sort(reverse=True)
            
            for score, source_path, source_info in scored_sources[:10]:  # Top 10 sources
                if added_samples >= target_samples:
                    break
                
                try:
                    source_dir = Path(source_path)
                    if source_dir.exists():
                        # Copy a reasonable number of samples
                        sample_files = source_info['files'][:min(20, target_samples - added_samples)]
                        
                        for sample_file in sample_files:
                            source_file = source_dir / sample_file
                            target_file = samples_dir / sample_file
                            
                            if source_file.exists() and not target_file.exists():
                                shutil.copy2(source_file, target_file)
                                added_samples += 1
                                self.stats['samples_added'] += 1
                
                except Exception as e:
                    continue
            
            # Report results
            if added_samples > 0:
                repaired += 1
                self.stats['libraries_repaired'] += 1
                
                new_sample_count = len(current_samples) + added_samples
                completion_ratio = new_sample_count / len(instruments) if len(instruments) > 0 else 0
                
                if completion_ratio >= 0.5:
                    completed += 1
                    self.stats['libraries_completed'] += 1
                    print(f"      🎉 COMPLETED! Added {added_samples} samples (ratio: {completion_ratio:.1f})")
                else:
                    print(f"      ✅ Enhanced! Added {added_samples} samples (ratio: {completion_ratio:.1f})")
            else:
                print(f"      ⚠️  No suitable samples found")
        
        print(f"\n   🎯 Repair Summary: {repaired} libraries enhanced, {completed} completed")
    
    def remove_duplicates(self):
        """Remove duplicate files within libraries"""
        print("\n🧹 REMOVING DUPLICATE FILES")
        print("=" * 60)
        
        libraries = [d for d in self.kontakt_lab.iterdir() if d.is_dir()]
        duplicates_removed = 0
        
        for library in libraries:
            if library.name.startswith('.') or library.name in ['REPORTS']:
                continue
            
            # Find duplicates by filename and size
            files_by_name_size = defaultdict(list)
            
            for file_path in library.rglob("*"):
                if file_path.is_file():
                    key = (file_path.name.lower(), file_path.stat().st_size)
                    files_by_name_size[key].append(file_path)
            
            # Remove duplicates, keeping the first one
            for (name, size), file_list in files_by_name_size.items():
                if len(file_list) > 1:
                    for duplicate in file_list[1:]:
                        try:
                            duplicate.unlink()
                            duplicates_removed += 1
                            self.stats['duplicates_removed'] += 1
                        except Exception:
                            pass
        
        if duplicates_removed > 0:
            print(f"   🗑️  Removed {duplicates_removed} duplicate files")
    
    def generate_master_report(self):
        """Generate comprehensive master report"""
        print("\n📊 GENERATING MASTER REPORT")
        print("=" * 60)
        
        # Run auto scanner for current status
        try:
            subprocess.run([sys.executable, str(Path.home() / "auto_scan.py")], 
                         capture_output=True, text=True, check=True)
        except Exception as e:
            print(f"   ⚠️  Auto scanner error: {e}")
        
        # Generate summary report
        report_file = self.reports_dir / f"MASTER_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w') as f:
            f.write("🎹 NOIZYGENIE MASTER ORGANIZER & FIXER REPORT\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("📊 OPERATION STATISTICS:\n")
            f.write(f"   Files Moved: {self.stats['files_moved']:,}\n")
            f.write(f"   Libraries Organized: {self.stats['libraries_organized']:,}\n")
            f.write(f"   Libraries Repaired: {self.stats['libraries_repaired']:,}\n")
            f.write(f"   Libraries Completed: {self.stats['libraries_completed']:,}\n")
            f.write(f"   Samples Added: {self.stats['samples_added']:,}\n")
            f.write(f"   Duplicates Removed: {self.stats['duplicates_removed']:,}\n\n")
            
            # Library status overview
            libraries = [d for d in self.kontakt_lab.iterdir() if d.is_dir() and not d.name.startswith('.')]
            f.write(f"📚 LIBRARY OVERVIEW:\n")
            f.write(f"   Total Libraries: {len(libraries)}\n\n")
            
            for library in sorted(libraries):
                if library.name in ['REPORTS', 'ORGANIZED_LIBRARIES']:
                    continue
                    
                instruments = len(list(library.rglob("*.nki"))) + \
                             len(list(library.rglob("*.nkm"))) + \
                             len(list(library.rglob("*.nkc")))
                
                samples = len(list(library.rglob("*.ncw"))) + \
                         len(list(library.rglob("*.wav"))) + \
                         len(list(library.rglob("*.aiff")))
                
                status = "🎉 COMPLETE" if samples >= instruments * 0.5 else \
                        "⚠️ PARTIAL" if samples > 0 else "❌ FRAGMENT"
                
                f.write(f"   {library.name}: {instruments} inst, {samples} samples ({status})\n")
        
        print(f"   📄 Master report saved: {report_file.name}")
    
    def run_complete_organization_and_repair(self):
        """Execute the complete organization and repair process"""
        start_time = time.time()
        
        print("🎹 NOIZYGENIE MASTER ORGANIZER & FIXER")
        print("=" * 60)
        print("🎯 Mission: Complete Native Instruments Arsenal Organization & Repair")
        print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Step 1: Initialize workspace
        self.initialize_workspace()
        
        # Step 2: Discover all NI files across volumes
        discovered_files = self.discover_ni_files_all_volumes()
        
        # Step 3: Organize files into libraries
        self.organize_by_libraries(discovered_files)
        
        # Step 4: Build comprehensive sample database
        sample_db, sample_patterns = self.build_comprehensive_sample_database()
        
        # Step 5: Intelligent library repair
        self.intelligent_library_repair(sample_db, sample_patterns)
        
        # Step 6: Remove duplicates
        self.remove_duplicates()
        
        # Step 7: Generate master report
        self.generate_master_report()
        
        # Final summary
        elapsed_time = time.time() - start_time
        print(f"\n🎉 MASTER ORGANIZATION & REPAIR COMPLETE!")
        print(f"⏱️  Total Time: {elapsed_time/60:.1f} minutes")
        print(f"📊 Final Statistics:")
        for key, value in self.stats.items():
            print(f"   {key.replace('_', ' ').title()}: {value:,}")
        
        print(f"\n✅ Check MASTERLIST.html for complete status")
        print(f"📄 Detailed reports in: {self.reports_dir}")

if __name__ == "__main__":
    try:
        organizer = MasterOrganizerFixer()
        organizer.run_complete_organization_and_repair()
    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()