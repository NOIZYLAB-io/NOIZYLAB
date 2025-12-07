#!/usr/bin/env python3
"""
EXECUTE MOVE ALL - Move All Files to Correct Folders NOW!
This script will actually MOVE files to their proper locations
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

# Drives
PRIMARY = Path("/Volumes/6TB")
SECONDARY = Path("/Volumes/4TBSG")
SOURCE = SECONDARY / "KTK 2026 TO SORT"

# Logging
MOVE_LOG = SECONDARY / "SCAN_RESULTS" / "moves_executed.json"
ERROR_LOG = SECONDARY / "SCAN_RESULTS" / "move_errors.json"

class FileMove:
    def __init__(self):
        self.moves = []
        self.stats = defaultdict(int)
        self.errors = []
        self.moved_count = 0
        
    def smart_categorize(self, filepath):
        """Smart categorization - determines where file should go"""
        path_str = str(filepath).lower()
        filename = os.path.basename(filepath).lower()
        ext = os.path.splitext(filename)[1].lower()
        
        # Skip system files
        if filename.startswith('.') or filename in ['desktop.ini', 'thumbs.db']:
            return None
        
        # KONTAKT FILES
        if ext in ['.nki', '.nkm', '.nkc', '.nkr']:
            # Detect instrument type
            if any(kw in path_str for kw in ['string', 'violin', 'cello', 'orchestra', 'symphonic']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Orchestral" / filename
            elif any(kw in path_str for kw in ['cinematic', 'epic', 'trailer', 'score', 'film']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Cinematic" / filename
            elif any(kw in path_str for kw in ['drum', 'percussion', 'perc', 'hit', 'cymbal']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Percussion" / filename
            elif any(kw in path_str for kw in ['synth', 'pad', 'lead', 'bass', 'ambient']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Synths_Pads" / filename
            elif any(kw in path_str for kw in ['piano', 'keys', 'keyboard']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Keys_Mallets" / filename
            elif any(kw in path_str for kw in ['guitar', 'bass']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Guitars_Bass" / filename
            elif any(kw in path_str for kw in ['vocal', 'voice', 'choir', 'vox']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Vocals_Choir" / filename
            elif any(kw in path_str for kw in ['ethnic', 'world', 'exotic']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Ethnic_World" / filename
            elif any(kw in path_str for kw in ['fx', 'effect', 'sfx']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Effects_SFX" / filename
            else:
                return PRIMARY / "KONTAKT_LIBRARIES" / "Other" / filename
        
        # KONTAKT SAMPLES
        elif ext in ['.ncw', '.nkx']:
            # Try to match with parent instrument
            parent_dir = os.path.basename(os.path.dirname(filepath))
            return PRIMARY / "KONTAKT_LIBRARIES" / "_Samples" / parent_dir / filename
        
        # WAV FILES
        elif ext == '.wav':
            if any(kw in filename for kw in ['kick', 'bd', 'bassdrum']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Kicks" / filename
            elif any(kw in filename for kw in ['snare', 'snr', 'sd']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Snares" / filename
            elif any(kw in filename for kw in ['hat', 'hh', 'hihat', 'hi-hat']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Hats" / filename
            elif any(kw in filename for kw in ['perc', 'tom', 'conga', 'bongo']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Percussion" / filename
            elif any(kw in path_str for kw in ['loop', 'beat', 'drum loop']):
                return PRIMARY / "AUDIO_SAMPLES" / "Loops" / "Drum_Loops" / filename
            elif any(kw in path_str for kw in ['music loop', 'musical']):
                return PRIMARY / "AUDIO_SAMPLES" / "Loops" / "Music_Loops" / filename
            elif any(kw in filename for kw in ['bass', '808', 'sub']):
                return PRIMARY / "AUDIO_SAMPLES" / "Bass" / filename
            elif any(kw in path_str for kw in ['vocal', 'vox', 'voice', 'acapella']):
                return PRIMARY / "AUDIO_SAMPLES" / "Vocal_Samples" / filename
            elif any(kw in path_str for kw in ['fx', 'effect', 'impact', 'sweep', 'whoosh', 'riser']):
                return PRIMARY / "AUDIO_SAMPLES" / "FX_Samples" / filename
            elif any(kw in path_str for kw in ['foley', 'ambience', 'atmosphere', 'environment']):
                return PRIMARY / "AUDIO_SAMPLES" / "Foley" / filename
            elif any(kw in filename for kw in ['melody', 'lead', 'riff']):
                return PRIMARY / "AUDIO_SAMPLES" / "Melody" / filename
            else:
                return PRIMARY / "AUDIO_SAMPLES" / "Other" / filename
        
        # AIFF FILES
        elif ext in ['.aif', '.aiff']:
            return PRIMARY / "AUDIO_SAMPLES" / "AIFF" / filename
        
        # PRESETS
        elif ext in ['.fxp', '.fxb']:
            return PRIMARY / "PLUGIN_PRESETS" / "VST" / filename
        elif ext in ['.nka', '.nksn', '.nkp']:
            return PRIMARY / "PLUGIN_PRESETS" / "Native" / filename
        
        # SAMPLER INSTRUMENTS
        elif ext == '.exs':
            if any(kw in path_str for kw in ['drum', 'percussion']):
                return PRIMARY / "SAMPLER_INSTRUMENTS" / "EXS24" / "Drums" / filename
            elif any(kw in path_str for kw in ['orchestra', 'string', 'brass']):
                return PRIMARY / "SAMPLER_INSTRUMENTS" / "EXS24" / "Orchestral" / filename
            else:
                return PRIMARY / "SAMPLER_INSTRUMENTS" / "EXS24" / "Other" / filename
        elif ext == '.sfz':
            return PRIMARY / "SAMPLER_INSTRUMENTS" / "SFZ" / filename
        elif ext == '.sxt':
            return PRIMARY / "SAMPLER_INSTRUMENTS" / "Halion" / filename
        
        # DOCUMENTS
        elif ext in ['.pdf', '.txt', '.rtf', '.doc', '.docx']:
            if any(kw in filename for kw in ['manual', 'guide', 'readme', 'read me']):
                return SECONDARY / "DOCUMENTATION" / "Manuals" / filename
            elif any(kw in filename for kw in ['license', 'serial', 'key']):
                return SECONDARY / "DOCUMENTATION" / "Licenses" / filename
            else:
                return SECONDARY / "DOCUMENTATION" / "Other" / filename
        
        # INSTALLERS
        elif ext in ['.dmg', '.pkg', '.zip', '.rar', '.7z', '.iso']:
            return SECONDARY / "INSTALLERS" / "Archives" / filename
        
        # Skip unknown
        return None
    
    def scan_and_plan(self, source_dir, max_files=None):
        """Scan source and plan all moves"""
        print(f"\n🔍 Scanning: {source_dir}")
        
        all_files = []
        for root, dirs, files in os.walk(source_dir):
            # Skip already organized
            if 'KONTAKT_LIBRARIES' in root or 'AUDIO_SAMPLES' in root:
                continue
            
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                filepath = Path(root) / filename
                all_files.append(filepath)
                
                if max_files and len(all_files) >= max_files:
                    break
            
            if max_files and len(all_files) >= max_files:
                break
        
        print(f"📊 Found {len(all_files):,} files")
        print("🎯 Planning moves...\n")
        
        planned = 0
        for filepath in all_files:
            try:
                dest = self.smart_categorize(filepath)
                if dest:
                    self.moves.append({
                        'source': str(filepath),
                        'dest': str(dest),
                        'size': os.path.getsize(filepath)
                    })
                    
                    # Track stats
                    category = dest.parts[3] if len(dest.parts) > 3 else "Unknown"
                    self.stats[category] += 1
                    planned += 1
            except Exception as e:
                self.errors.append({'file': str(filepath), 'error': str(e), 'stage': 'planning'})
        
        print(f"✅ Planned {planned:,} moves")
        return self.moves
    
    def execute_moves(self, dry_run=False, max_workers=24):
        """Execute the actual file moves"""
        print("\n" + "="*70)
        print("🚀 EXECUTING FILE MOVES")
        print("="*70)
        
        if dry_run:
            print("\n⚠️  DRY RUN - Showing what WOULD happen\n")
        else:
            print("\n🔴 LIVE MODE - Actually moving files!\n")
        
        # Show stats
        print("📊 Moves by category:")
        for cat, count in sorted(self.stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat:30} {count:>8,} files")
        
        print(f"\n📋 Sample moves (first 10):")
        for i, move in enumerate(self.moves[:10], 1):
            print(f"\n{i}. {Path(move['source']).name}")
            print(f"   → {move['dest']}")
        
        if len(self.moves) > 10:
            print(f"\n... and {len(self.moves) - 10:,} more\n")
        
        if dry_run:
            print("\n💡 To actually move files, run with: --execute")
            return
        
        # Execute moves
        print("\n🚀 Moving files in parallel...\n")
        
        def move_file(move):
            try:
                src = Path(move['source'])
                dst = Path(move['dest'])
                
                # Skip if source doesn't exist
                if not src.exists():
                    return False
                
                # Create destination directory
                dst.parent.mkdir(parents=True, exist_ok=True)
                
                # Handle conflicts
                if dst.exists():
                    counter = 1
                    original_stem = dst.stem
                    while dst.exists():
                        dst = dst.parent / f"{original_stem}_{counter}{dst.suffix}"
                        counter += 1
                
                # Move file
                shutil.move(str(src), str(dst))
                return True
                
            except Exception as e:
                self.errors.append({
                    'file': move['source'],
                    'dest': move['dest'],
                    'error': str(e),
                    'stage': 'execution'
                })
                return False
        
        # Execute in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(move_file, move): move for move in self.moves}
            
            for i, future in enumerate(as_completed(futures), 1):
                if future.result():
                    self.moved_count += 1
                
                if i % 50 == 0:
                    pct = (i / len(self.moves)) * 100
                    print(f"  Progress: {i:,}/{len(self.moves):,} ({pct:.1f}%)", end='\r')
        
        print(f"\n\n✅ COMPLETE!")
        print(f"  Moved: {self.moved_count:,} files")
        print(f"  Failed: {len(self.errors)}")
        
        # Save logs
        self.save_logs()
        
        return self.moved_count
    
    def save_logs(self):
        """Save execution logs"""
        MOVE_LOG.parent.mkdir(parents=True, exist_ok=True)
        
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'total_planned': len(self.moves),
            'total_moved': self.moved_count,
            'total_errors': len(self.errors),
            'by_category': dict(self.stats),
            'sample_moves': self.moves[:100]
        }
        
        with open(MOVE_LOG, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        if self.errors:
            with open(ERROR_LOG, 'w') as f:
                json.dump(self.errors, f, indent=2)
        
        print(f"\n📄 Logs saved:")
        print(f"  {MOVE_LOG}")
        if self.errors:
            print(f"  {ERROR_LOG}")

def main():
    print("\n" + "🚀"*35)
    print("  EXECUTE MOVE ALL - Move Files to Correct Folders")
    print("🚀"*35 + "\n")
    
    import sys
    
    # Check mode
    execute_mode = '--execute' in sys.argv
    test_mode = '--test' in sys.argv
    
    if not execute_mode and not test_mode:
        print("⚠️  DRY RUN MODE")
        print("\nThis will show you what would happen without actually moving files.")
        print("\nOptions:")
        print("  --execute   Actually move the files")
        print("  --test      Test with first 100 files only")
        print("\nRunning dry run...\n")
    
    mover = FileMove()
    
    # Scan and plan
    max_files = 100 if test_mode else None
    mover.scan_and_plan(SOURCE, max_files=max_files)
    
    if not mover.moves:
        print("\n✅ No files to move! Everything is already organized.")
        return
    
    # Execute
    if execute_mode:
        print("\n🔴 EXECUTE MODE - Files will actually be moved!")
        print("⚠️  Make sure you have backups!")
        
        response = input("\nType 'MOVE' to confirm: ")
        if response != 'MOVE':
            print("❌ Cancelled")
            return
    
    mover.execute_moves(dry_run=not execute_mode)
    
    print("\n" + "="*70)
    print("✅ DONE!")
    print("="*70)
    
    if not execute_mode:
        print("\n💡 To actually move files:")
        print("   python3 EXECUTE_MOVE_ALL.py --execute")

if __name__ == "__main__":
    main()

