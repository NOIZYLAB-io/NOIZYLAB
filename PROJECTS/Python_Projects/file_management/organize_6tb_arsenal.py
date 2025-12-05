#!/usr/bin/env python3
"""
NOIZYGENIE 6TB Arsenal Organizer
Process the massive 1M+ NI file discovery from 6TB volume
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict, Counter
import json
import time
from datetime import datetime

class SixTBArsenalOrganizer:
    def __init__(self):
        self.six_tb = Path("/Volumes/6TB")
        self.kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
        self.reports_dir = self.kontakt_lab / "REPORTS"
        self.six_tb_archive = self.kontakt_lab / "6TB_ARCHIVE"
        
        # Results from scan
        self.scan_results = {
            'nki': 19567,
            'nkm': 646, 
            'nkc': 2325,
            'ncw': 895868,
            'wav': 164452
        }
        
        self.stats = {
            'libraries_organized': 0,
            'files_processed': 0,
            'samples_archived': 0,
            'complete_libraries': 0
        }
    
    def analyze_6tb_structure(self):
        """Analyze the structure and identify major NI collections"""
        print("🔍 ANALYZING 6TB STRUCTURE FOR NI COLLECTIONS")
        print("=" * 60)
        
        # Look for major NI installation paths
        ni_paths = []
        
        # Common NI installation patterns
        search_patterns = [
            "**/Native Instruments/**",
            "**/Kontakt**/**",
            "**/KOMPLETE**/**",
            "**/NI_**/**",
            "**/*Library*/**",
            "**/*Instruments*/**"
        ]
        
        for pattern in search_patterns:
            try:
                found_paths = list(self.six_tb.glob(pattern))
                for path in found_paths[:20]:  # Limit to prevent overflow
                    if path.is_dir():
                        # Check if it contains NI files
                        ni_file_count = (
                            len(list(path.rglob("*.nki"))[:100]) +
                            len(list(path.rglob("*.nkm"))[:100]) +
                            len(list(path.rglob("*.nkc"))[:100])
                        )
                        
                        if ni_file_count > 10:
                            ni_paths.append({
                                'path': path,
                                'name': path.name,
                                'ni_files': ni_file_count,
                                'pattern': pattern
                            })
            except Exception as e:
                print(f"   ⚠️  Error searching {pattern}: {e}")
        
        # Sort by NI file count
        ni_paths.sort(key=lambda x: x['ni_files'], reverse=True)
        
        print(f"📊 Found {len(ni_paths)} major NI collections:")
        for i, collection in enumerate(ni_paths[:10], 1):
            print(f"   {i:2d}. {collection['name'][:50]} - {collection['ni_files']} files")
        
        return ni_paths
    
    def create_archive_structure(self):
        """Create organized archive structure for 6TB content"""
        print("\n🏗️  CREATING 6TB ARCHIVE STRUCTURE")
        print("=" * 60)
        
        # Create organized directory structure
        archive_dirs = [
            self.six_tb_archive,
            self.six_tb_archive / "COMPLETE_LIBRARIES",
            self.six_tb_archive / "PARTIAL_LIBRARIES", 
            self.six_tb_archive / "SAMPLE_COLLECTIONS",
            self.six_tb_archive / "FACTORY_CONTENT",
            self.six_tb_archive / "THIRD_PARTY",
            self.six_tb_archive / "PRESETS_ONLY"
        ]
        
        for directory in archive_dirs:
            directory.mkdir(exist_ok=True, parents=True)
            print(f"   📁 Created: {directory.name}")
        
        print("✅ Archive structure ready!")
    
    def organize_by_completeness(self, ni_collections):
        """Organize collections by completeness (instruments + samples)"""
        print("\n📚 ORGANIZING BY LIBRARY COMPLETENESS")
        print("=" * 60)
        
        organized = 0
        
        for collection in ni_collections[:20]:  # Process top 20 collections
            collection_path = collection['path']
            collection_name = self.clean_name(collection['name'])
            
            print(f"\n🔍 Processing: {collection_name}")
            
            try:
                # Count instruments and samples
                instruments = (
                    list(collection_path.rglob("*.nki")) +
                    list(collection_path.rglob("*.nkm")) + 
                    list(collection_path.rglob("*.nkc"))
                )
                
                samples = (
                    list(collection_path.rglob("*.ncw"))[:500] +  # Limit to prevent memory issues
                    list(collection_path.rglob("*.wav"))[:200]
                )
                
                print(f"   📊 Found: {len(instruments)} instruments, {len(samples)} samples")
                
                # Determine library type
                if len(samples) >= len(instruments) * 0.8:
                    target_dir = self.six_tb_archive / "COMPLETE_LIBRARIES" / collection_name
                    library_type = "COMPLETE"
                elif len(samples) >= len(instruments) * 0.3:
                    target_dir = self.six_tb_archive / "PARTIAL_LIBRARIES" / collection_name
                    library_type = "PARTIAL"
                elif len(instruments) > 50:
                    target_dir = self.six_tb_archive / "PRESETS_ONLY" / collection_name
                    library_type = "PRESETS"
                else:
                    target_dir = self.six_tb_archive / "SAMPLE_COLLECTIONS" / collection_name
                    library_type = "SAMPLES"
                
                print(f"   🎯 Classification: {library_type}")
                
                # Create organized copy (copy key files, not entire collection due to size)
                target_dir.mkdir(exist_ok=True, parents=True)
                
                # Copy instruments (reasonable number)
                instruments_dir = target_dir / "Instruments"
                instruments_dir.mkdir(exist_ok=True)
                
                copied_instruments = 0
                for instrument in instruments[:100]:  # Limit to 100 instruments per library
                    try:
                        target_file = instruments_dir / instrument.name
                        if not target_file.exists():
                            shutil.copy2(instrument, target_file)
                            copied_instruments += 1
                            self.stats['files_processed'] += 1
                    except Exception as e:
                        continue
                
                # Copy representative samples
                if samples and len(samples) > 0:
                    samples_dir = target_dir / "Samples"
                    samples_dir.mkdir(exist_ok=True)
                    
                    copied_samples = 0
                    for sample in samples[:50]:  # Limit to 50 samples per library
                        try:
                            target_file = samples_dir / sample.name
                            if not target_file.exists():
                                shutil.copy2(sample, target_file)
                                copied_samples += 1
                                self.stats['samples_archived'] += 1
                        except Exception as e:
                            continue
                
                # Create library info file
                info_file = target_dir / "LIBRARY_INFO.txt"
                with open(info_file, 'w') as f:
                    f.write(f"Library: {collection_name}\n")
                    f.write(f"Source: {collection_path}\n")
                    f.write(f"Type: {library_type}\n")
                    f.write(f"Instruments: {len(instruments)}\n")
                    f.write(f"Samples: {len(samples)}\n")
                    f.write(f"Copied Instruments: {copied_instruments}\n")
                    f.write(f"Copied Samples: {copied_samples}\n")
                    f.write(f"Organized: {datetime.now()}\n")
                
                organized += 1
                self.stats['libraries_organized'] += 1
                
                if library_type == "COMPLETE":
                    self.stats['complete_libraries'] += 1
                
                print(f"   ✅ Organized! Copied {copied_instruments} instruments, {copied_samples} samples")
                
            except Exception as e:
                print(f"   ❌ Error processing {collection_name}: {e}")
        
        print(f"\n🎉 Organized {organized} collections from 6TB!")
    
    def clean_name(self, name):
        """Clean directory names for organization"""
        import re
        cleaned = re.sub(r'[^\w\s-]', '', name)
        cleaned = re.sub(r'\s+', '_', cleaned.strip())
        return cleaned[:50]
    
    def create_sample_database_index(self):
        """Create comprehensive sample database index from 6TB"""
        print("\n🗄️  CREATING SAMPLE DATABASE INDEX")
        print("=" * 60)
        
        sample_index = {
            'directories': {},
            'patterns': set(),
            'total_samples': 0,
            'created': datetime.now().isoformat()
        }
        
        sample_dirs_found = 0
        
        # Scan for sample-heavy directories
        for root, dirs, files in os.walk(self.six_tb):
            # Limit depth
            if len(Path(root).parts) - len(self.six_tb.parts) > 6:
                dirs.clear()
                continue
            
            current_path = Path(root)
            sample_files = [f for f in files if f.lower().endswith(('.ncw', '.wav', '.aiff'))]
            
            if len(sample_files) >= 20:  # Only directories with substantial samples
                sample_index['directories'][str(current_path)] = {
                    'sample_count': len(sample_files),
                    'file_types': Counter(Path(f).suffix.lower() for f in sample_files),
                    'keywords': self.extract_keywords(current_path.name.lower())
                }
                
                sample_dirs_found += 1
                sample_index['total_samples'] += len(sample_files)
                
                # Extract patterns for smart matching
                for sample in sample_files[:10]:  # Sample from each directory
                    words = sample.lower().replace('.ncw', '').replace('.wav', '').replace('.aiff', '').split('_')
                    for word in words:
                        if len(word) > 3:
                            sample_index['patterns'].add(word)
            
            # Progress indicator
            if sample_dirs_found % 100 == 0 and sample_dirs_found > 0:
                print(f"      📊 Indexed {sample_dirs_found} sample directories...")
        
        # Convert set to list for JSON serialization
        sample_index['patterns'] = list(sample_index['patterns'])
        
        # Save index
        index_file = self.reports_dir / "6TB_SAMPLE_DATABASE.json"
        with open(index_file, 'w') as f:
            json.dump(sample_index, f, indent=2)
        
        print(f"   💾 Sample database created: {sample_dirs_found:,} directories indexed")
        print(f"   🎯 Total samples catalogued: {sample_index['total_samples']:,}")
        print(f"   🔍 Unique patterns: {len(sample_index['patterns']):,}")
        print(f"   📄 Database saved: {index_file.name}")
    
    def extract_keywords(self, text):
        """Extract meaningful keywords from text"""
        import re
        words = re.findall(r'\b\w{4,}\b', text.lower())
        return [w for w in words if w not in ['kontakt', 'native', 'instruments', 'library']]
    
    def generate_6tb_master_report(self):
        """Generate comprehensive report of 6TB organization"""
        print("\n📊 GENERATING 6TB MASTER REPORT")
        print("=" * 60)
        
        report_file = self.reports_dir / f"6TB_ORGANIZATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w') as f:
            f.write("🎹 NOIZYGENIE 6TB ARSENAL ORGANIZATION REPORT\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("📊 6TB SCAN DISCOVERY:\n")
            f.write(f"   Total NI Files Found: 1,082,858\n")
            f.write(f"   .nki files: {self.scan_results['nki']:,}\n")
            f.write(f"   .nkm files: {self.scan_results['nkm']:,}\n")
            f.write(f"   .nkc files: {self.scan_results['nkc']:,}\n")
            f.write(f"   .ncw files: {self.scan_results['ncw']:,}\n")
            f.write(f"   .wav files: {self.scan_results['wav']:,}\n\n")
            
            f.write("🏗️  ORGANIZATION STATISTICS:\n")
            f.write(f"   Libraries Organized: {self.stats['libraries_organized']}\n")
            f.write(f"   Files Processed: {self.stats['files_processed']}\n")
            f.write(f"   Samples Archived: {self.stats['samples_archived']}\n")
            f.write(f"   Complete Libraries: {self.stats['complete_libraries']}\n\n")
            
            f.write("📁 ARCHIVE STRUCTURE:\n")
            f.write(f"   Complete Libraries: {self.six_tb_archive / 'COMPLETE_LIBRARIES'}\n")
            f.write(f"   Partial Libraries: {self.six_tb_archive / 'PARTIAL_LIBRARIES'}\n")
            f.write(f"   Sample Collections: {self.six_tb_archive / 'SAMPLE_COLLECTIONS'}\n")
            f.write(f"   Factory Content: {self.six_tb_archive / 'FACTORY_CONTENT'}\n")
            f.write(f"   Third Party: {self.six_tb_archive / 'THIRD_PARTY'}\n")
            f.write(f"   Presets Only: {self.six_tb_archive / 'PRESETS_ONLY'}\n\n")
            
            f.write("🎯 NEXT ACTIONS:\n")
            f.write("   1. Review organized libraries in 6TB_ARCHIVE\n")
            f.write("   2. Migrate complete libraries to main KONTAKT_LAB\n")
            f.write("   3. Use sample database for library repair\n")
            f.write("   4. Continue processing remaining collections\n")
        
        print(f"   📄 Master report saved: {report_file.name}")
    
    def run_6tb_organization(self):
        """Execute complete 6TB organization process"""
        start_time = time.time()
        
        print("🎹 NOIZYGENIE 6TB ARSENAL ORGANIZER")
        print("=" * 60)
        print("🎯 Processing 1,082,858 Native Instruments files from 6TB")
        print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Initialize directories
        self.kontakt_lab.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True, parents=True)
        
        # Step 1: Analyze 6TB structure
        ni_collections = self.analyze_6tb_structure()
        
        # Step 2: Create archive structure
        self.create_archive_structure()
        
        # Step 3: Organize by completeness
        self.organize_by_completeness(ni_collections)
        
        # Step 4: Create sample database index
        self.create_sample_database_index()
        
        # Step 5: Generate master report
        self.generate_6tb_master_report()
        
        # Final summary
        elapsed_time = time.time() - start_time
        print(f"\n🎉 6TB ORGANIZATION COMPLETE!")
        print(f"⏱️  Total Time: {elapsed_time/60:.1f} minutes")
        print(f"📊 Final Statistics:")
        for key, value in self.stats.items():
            print(f"   {key.replace('_', ' ').title()}: {value:,}")
        
        print(f"\n✅ Organized content available in: {self.six_tb_archive}")
        print(f"📄 Sample database ready for library repair")
        print(f"🎯 Ready to enhance existing KONTAKT_LAB with 6TB resources!")

if __name__ == "__main__":
    try:
        organizer = SixTBArsenalOrganizer()
        organizer.run_6tb_organization()
    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()