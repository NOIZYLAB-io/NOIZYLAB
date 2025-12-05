#!/usr/bin/env python3
"""
NOIZYGENIE Batch Library Repair System
Enhanced repair system to process remaining fragment libraries
"""

import os
import shutil
import json
from pathlib import Path
from collections import defaultdict, Counter
import time
from datetime import datetime
import sys
sys.path.append('/Users/rsp_ms')
from palatino_terminal import PalatinoTerminal

class BatchLibraryRepair:
    def __init__(self):
        self.pt = PalatinoTerminal()
        self.kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
        self.reports_dir = self.kontakt_lab / "REPORTS"
        self.six_tb = Path("/Volumes/6TB")
        
        # Load sample database if it exists
        self.sample_db = self.load_sample_database()
        
        # Statistics
        self.stats = {
            'libraries_processed': 0,
            'libraries_repaired': 0,
            'libraries_completed': 0,
            'samples_added': 0,
            'processing_time': 0
        }
    
    def load_sample_database(self):
        """Load the 6TB sample database if available"""
        db_file = self.reports_dir / "6TB_SAMPLE_DATABASE.json"
        
        if db_file.exists():
            try:
                with open(db_file, 'r') as f:
                    db = json.load(f)
                self.pt.success(f"Loaded sample database: {len(db.get('directories', {})):,} directories")
                return db
            except Exception as e:
                self.pt.warning(f"Could not load sample database: {e}")
        
        self.pt.info("Sample database", "Not found - will build during repair")
        return None
    
    def identify_priority_fragments(self, max_libraries=50):
        """Identify high-priority fragment libraries for repair"""
        self.pt.subheader("Identifying Priority Fragment Libraries")
        
        fragment_libraries = []
        
        # Scan all libraries
        for item in self.kontakt_lab.iterdir():
            if not item.is_dir() or item.name.startswith('.') or item.name in ['REPORTS', '6TB_ARCHIVE']:
                continue
            
            # Check if it's a fragment
            instruments = (
                list(item.rglob("*.nki")) +
                list(item.rglob("*.nkm")) +
                list(item.rglob("*.nkc"))
            )
            
            samples = (
                list(item.rglob("*.ncw")) +
                list(item.rglob("*.wav")) +
                list(item.rglob("*.aiff"))
            )
            
            if len(instruments) > 0 and len(samples) < len(instruments) * 0.3:
                # Calculate priority score
                priority_score = 0
                
                # More instruments = higher priority
                priority_score += len(instruments) * 2
                
                # Certain keywords boost priority
                name_lower = item.name.lower()
                for keyword in ['bass', 'drum', 'piano', 'guitar', 'string', 'brass', 'vocal', 'lead', 'pad']:
                    if keyword in name_lower:
                        priority_score += 20
                
                # Boost score for libraries with some samples (easier to complete)
                priority_score += len(samples) * 5
                
                fragment_libraries.append({
                    'name': item.name,
                    'path': item,
                    'instruments': len(instruments),
                    'samples': len(samples),
                    'priority_score': priority_score
                })
        
        # Sort by priority score
        fragment_libraries.sort(key=lambda x: x['priority_score'], reverse=True)
        
        selected = fragment_libraries[:max_libraries]
        
        self.pt.info("Fragment libraries found", f"{len(fragment_libraries):,}")
        self.pt.info("Selected for processing", f"{len(selected)}")
        
        if selected:
            print(f"\n🎯 Top Priority Libraries:")
            for i, lib in enumerate(selected[:10], 1):
                print(f"   {i:2d}. {lib['name']:<30} - {lib['instruments']:>3} inst, {lib['samples']:>3} samples (score: {lib['priority_score']})")
        
        return selected
    
    def build_smart_sample_index(self):
        """Build intelligent sample index from 6TB for repair operations"""
        self.pt.subheader("Building Smart Sample Index from 6TB")
        
        if not self.six_tb.exists():
            self.pt.error("6TB volume not available")
            return {}
        
        sample_index = {}
        indexed_dirs = 0
        
        # Focus on high-value sample directories
        for root, dirs, files in os.walk(self.six_tb):
            # Limit depth
            if len(Path(root).parts) - len(self.six_tb.parts) > 7:
                dirs.clear()
                continue
            
            current_path = Path(root)
            sample_files = [f for f in files if f.lower().endswith(('.ncw', '.wav', '.aiff'))]
            
            if len(sample_files) >= 15:  # Only substantial sample collections
                # Extract keywords from path
                path_text = str(current_path).lower()
                keywords = self.extract_sample_keywords(path_text)
                
                sample_index[str(current_path)] = {
                    'sample_count': len(sample_files),
                    'keywords': keywords,
                    'file_types': self.count_file_types(sample_files),
                    'quality_score': self.calculate_quality_score(current_path, sample_files)
                }
                
                indexed_dirs += 1
                
                # Progress indicator
                if indexed_dirs % 500 == 0:
                    print(f"      📊 Indexed {indexed_dirs:,} sample directories...")
        
        self.pt.info("Sample directories indexed", f"{indexed_dirs:,}")
        return sample_index
    
    def extract_sample_keywords(self, path_text):
        """Extract meaningful keywords from sample path"""
        import re
        
        # Common instrument and genre keywords
        instrument_keywords = [
            'bass', 'drum', 'piano', 'guitar', 'synth', 'vocal', 'string', 'brass', 
            'lead', 'pad', 'arp', 'chord', 'melody', 'percussion', 'kick', 'snare',
            'hi?hat', 'cymbal', 'tom', 'organ', 'flute', 'sax', 'trumpet', 'violin',
            'cello', 'viola', 'harp', 'bells', 'choir', 'voice'
        ]
        
        genre_keywords = [
            'house', 'techno', 'trance', 'ambient', 'jazz', 'rock', 'pop', 'hip.hop',
            'trap', 'dubstep', 'dnb', 'breaks', 'electro', 'disco', 'funk', 'soul'
        ]
        
        found_keywords = []
        
        for keyword in instrument_keywords + genre_keywords:
            if re.search(keyword.replace('?', r'[- ]?'), path_text):
                found_keywords.append(keyword.replace('?', ''))
        
        return found_keywords
    
    def count_file_types(self, sample_files):
        """Count different sample file types"""
        types = Counter()
        for file in sample_files:
            ext = Path(file).suffix.lower()
            types[ext] += 1
        return dict(types)
    
    def calculate_quality_score(self, path, sample_files):
        """Calculate quality score for sample directory"""
        score = 0
        
        # More samples = higher score
        score += min(len(sample_files) / 10, 20)
        
        # Prefer .ncw (KONTAKT compressed) samples
        ncw_count = len([f for f in sample_files if f.lower().endswith('.ncw')])
        score += ncw_count * 2
        
        # Boost score for Native Instruments paths
        path_lower = str(path).lower()
        if 'native instruments' in path_lower or 'kontakt' in path_lower:
            score += 15
        
        # Organized directory structures get bonus
        if any(word in path_lower for word in ['samples', 'audio', 'library']):
            score += 10
        
        return score
    
    def smart_sample_matching(self, library_name, sample_index):
        """Intelligently match samples to library based on keywords"""
        library_keywords = self.extract_sample_keywords(library_name.lower())
        
        # Score all sample directories for this library
        scored_matches = []
        
        for sample_path, sample_info in sample_index.items():
            match_score = 0
            
            # Keyword matching
            common_keywords = set(library_keywords) & set(sample_info['keywords'])
            match_score += len(common_keywords) * 15
            
            # Quality score from sample directory
            match_score += sample_info['quality_score']
            
            # Prefer directories with more samples
            match_score += min(sample_info['sample_count'] / 20, 10)
            
            if match_score > 5:  # Only consider decent matches
                scored_matches.append({
                    'path': sample_path,
                    'score': match_score,
                    'info': sample_info
                })
        
        # Return top matches
        scored_matches.sort(key=lambda x: x['score'], reverse=True)
        return scored_matches[:8]  # Top 8 sample sources
    
    def repair_library_with_samples(self, library_info, sample_index):
        """Repair a single library using intelligent sample matching"""
        library_path = library_info['path']
        library_name = library_info['name']
        
        print(f"\n🔧 Repairing: {library_name}")
        print(f"   📊 Current: {library_info['instruments']} instruments, {library_info['samples']} samples")
        
        # Find matching samples
        sample_matches = self.smart_sample_matching(library_name, sample_index)
        
        if not sample_matches:
            print(f"   ❌ No suitable samples found")
            return False
        
        # Create samples directory
        samples_dir = library_path / "Samples"
        samples_dir.mkdir(exist_ok=True)
        
        added_samples = 0
        target_samples = min(library_info['instruments'], 80)  # Reasonable target
        
        for match in sample_matches:
            if added_samples >= target_samples:
                break
            
            source_path = Path(match['path'])
            if not source_path.exists():
                continue
            
            try:
                # Get sample files from this source
                source_samples = list(source_path.glob("*.ncw"))[:15] + \
                               list(source_path.glob("*.wav"))[:10]
                
                for sample_file in source_samples:
                    if added_samples >= target_samples:
                        break
                    
                    target_file = samples_dir / sample_file.name
                    if not target_file.exists():
                        shutil.copy2(sample_file, target_file)
                        added_samples += 1
                        self.stats['samples_added'] += 1
            
            except Exception as e:
                continue
        
        # Report results
        if added_samples > 0:
            self.stats['libraries_repaired'] += 1
            
            new_total_samples = library_info['samples'] + added_samples
            completion_ratio = new_total_samples / library_info['instruments']
            
            if completion_ratio >= 0.5:
                self.stats['libraries_completed'] += 1
                print(f"   🎉 COMPLETED! Added {added_samples} samples (ratio: {completion_ratio:.1f})")
            else:
                print(f"   ✅ Enhanced! Added {added_samples} samples (ratio: {completion_ratio:.1f})")
            
            return True
        else:
            print(f"   ⚠️  No samples could be added")
            return False
    
    def run_batch_repair(self, max_libraries=50):
        """Run the complete batch repair process"""
        start_time = time.time()
        
        self.pt.header("NOIZYGENIE Batch Library Repair System")
        self.pt.info("Target", f"Repair up to {max_libraries} fragment libraries")
        self.pt.info("Started", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Step 1: Identify priority fragments
        priority_libraries = self.identify_priority_fragments(max_libraries)
        
        if not priority_libraries:
            self.pt.warning("No fragment libraries found to repair")
            return
        
        # Step 2: Build/load sample index
        if self.sample_db and 'directories' in self.sample_db:
            sample_index = self.sample_db['directories']
            self.pt.success(f"Using cached sample database")
        else:
            sample_index = self.build_smart_sample_index()
        
        if not sample_index:
            self.pt.error("No sample index available - cannot proceed")
            return
        
        # Step 3: Process libraries
        self.pt.section_break()
        self.pt.subheader("Processing Fragment Libraries")
        
        for i, library_info in enumerate(priority_libraries, 1):
            print(f"\n📦 Processing {i}/{len(priority_libraries)}: {library_info['name']}")
            
            success = self.repair_library_with_samples(library_info, sample_index)
            self.stats['libraries_processed'] += 1
            
            # Prevent overwhelming the system
            if i % 10 == 0:
                print(f"      ⏸️  Brief pause after {i} libraries...")
                time.sleep(2)
        
        # Final results
        elapsed_time = time.time() - start_time
        self.stats['processing_time'] = elapsed_time
        
        self.pt.section_break()
        self.pt.complete("BATCH REPAIR COMPLETE!")
        
        self.pt.info("Libraries Processed", f"{self.stats['libraries_processed']}")
        self.pt.info("Libraries Repaired", f"{self.stats['libraries_repaired']}")
        self.pt.info("Libraries Completed", f"{self.stats['libraries_completed']}")
        self.pt.info("Samples Added", f"{self.stats['samples_added']:,}")
        self.pt.info("Processing Time", f"{elapsed_time/60:.1f} minutes")
        
        # Update HTML masterlist
        print(f"\n📊 Updating HTML masterlist...")
        os.system("python3 ~/auto_scan.py")
        
        self.pt.timestamp()

if __name__ == "__main__":
    try:
        repair_system = BatchLibraryRepair()
        repair_system.run_batch_repair(max_libraries=30)  # Process 30 libraries
    except KeyboardInterrupt:
        print("\n⏹️  Batch repair cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()