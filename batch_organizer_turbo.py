#!/usr/bin/env python3
"""
BATCH ORGANIZER TURBO - Ultra-Fast Batch Processing
Organize thousands of files per second with AI categorization
"""

import os
import shutil
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import defaultdict
from datetime import datetime
import multiprocessing

PRIMARY = Path("/Volumes/6TB")
SECONDARY = Path("/Volumes/4TBSG")

class TurboOrganizer:
    def __init__(self):
        self.max_workers = multiprocessing.cpu_count() * 3
        self.moves_planned = []
        self.stats = defaultdict(int)
        
    def ai_categorize(self, filepath):
        """AI-powered file categorization"""
        path_str = str(filepath).lower()
        filename = os.path.basename(filepath).lower()
        ext = os.path.splitext(filename)[1].lower()
        
        # Kontakt files
        if ext in ['.nki', '.nkm', '.nkc', '.nkr']:
            # Detect type
            if any(kw in path_str or kw in filename for kw in 
                   ['string', 'violin', 'cello', 'orchestra', 'symphonic']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Orchestral" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['cinematic', 'epic', 'trailer', 'score']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Cinematic" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['drum', 'percussion', 'perc', 'hit']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Percussion" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['synth', 'pad', 'lead', 'bass']):
                return PRIMARY / "KONTAKT_LIBRARIES" / "Synths_Pads" / filename
            else:
                return PRIMARY / "KONTAKT_LIBRARIES" / "Other" / filename
        
        # Kontakt samples
        elif ext in ['.ncw', '.nkx']:
            return PRIMARY / "KONTAKT_LIBRARIES" / "_Samples" / filename
        
        # WAV files
        elif ext == '.wav':
            if any(kw in path_str or kw in filename for kw in 
                   ['kick', 'kik']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Kicks" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['snare', 'snr']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Snares" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['hat', 'hh', 'hihat']):
                return PRIMARY / "AUDIO_SAMPLES" / "Drums" / "Hats" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['loop', 'beat']):
                return PRIMARY / "AUDIO_SAMPLES" / "Loops" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['bass', '808', 'sub']):
                return PRIMARY / "AUDIO_SAMPLES" / "Bass" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['vocal', 'vox', 'voice']):
                return PRIMARY / "AUDIO_SAMPLES" / "Vocal_Samples" / filename
            elif any(kw in path_str or kw in filename for kw in 
                    ['fx', 'effect', 'impact', 'sweep']):
                return PRIMARY / "AUDIO_SAMPLES" / "FX_Samples" / filename
            else:
                return PRIMARY / "AUDIO_SAMPLES" / "Other" / filename
        
        # AIF files
        elif ext in ['.aif', '.aiff']:
            return PRIMARY / "AUDIO_SAMPLES" / "AIFF" / filename
        
        # Presets
        elif ext in ['.fxp', '.fxb']:
            return PRIMARY / "PLUGIN_PRESETS" / "VST" / filename
        elif ext in ['.nka', '.nksn']:
            return PRIMARY / "PLUGIN_PRESETS" / "Native" / filename
        
        # Samplers
        elif ext == '.exs':
            return PRIMARY / "SAMPLER_INSTRUMENTS" / "EXS24" / filename
        elif ext == '.sfz':
            return PRIMARY / "SAMPLER_INSTRUMENTS" / "SFZ" / filename
        
        # Documents
        elif ext in ['.pdf', '.txt', '.rtf']:
            return SECONDARY / "DOCUMENTATION" / "Manuals" / filename
        
        # Installers
        elif ext in ['.dmg', '.pkg', '.zip', '.rar']:
            return SECONDARY / "INSTALLERS" / "Archives" / filename
        
        return None
    
    def batch_scan_and_plan(self, source_dirs):
        """Scan and plan moves in parallel"""
        print(f"\n⚡ TURBO MODE: Using {self.max_workers} workers")
        print("🔍 Scanning and planning organization...\n")
        
        all_files = []
        for source_dir in source_dirs:
            if not source_dir.exists():
                continue
            
            print(f"📂 Scanning: {source_dir.name}")
            
            for root, dirs, files in os.walk(source_dir):
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                
                for filename in files:
                    if not filename.startswith('.'):
                        filepath = Path(root) / filename
                        all_files.append(filepath)
        
        print(f"\n📊 Found {len(all_files):,} files")
        print("🎯 Planning organization with AI categorization...\n")
        
        # Categorize in parallel
        def categorize_file(filepath):
            try:
                new_path = self.ai_categorize(filepath)
                if new_path and new_path != filepath:
                    size = os.path.getsize(filepath)
                    return {
                        'from': str(filepath),
                        'to': str(new_path),
                        'size': size
                    }
            except:
                pass
            return None
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(categorize_file, fp) for fp in all_files]
            
            for i, future in enumerate(futures, 1):
                result = future.result()
                if result:
                    self.moves_planned.append(result)
                    category = Path(result['to']).parts[3] if len(Path(result['to']).parts) > 3 else "Other"
                    self.stats[category] += 1
                
                if i % 500 == 0:
                    print(f"  Progress: {i:,}/{len(all_files):,} ({i/len(all_files)*100:.1f}%)", end='\r')
        
        print(f"\n\n✅ Planning complete!")
        print(f"📊 Files to organize: {len(self.moves_planned):,}")
        
        return self.moves_planned
    
    def execute_turbo(self, dry_run=True):
        """Execute moves in turbo mode"""
        print("\n" + "="*70)
        print("🚀 TURBO BATCH ORGANIZATION")
        print("="*70)
        
        if dry_run:
            print("\n⚠️  DRY RUN - Preview only")
        else:
            print("\n🔴 LIVE MODE - Moving files now!")
        
        # Show stats
        print(f"\n📊 Organization by category:")
        for category, count in sorted(self.stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {category:30} {count:>8,} files")
        
        # Show sample
        print(f"\n📋 Sample moves (first 10):")
        for i, move in enumerate(self.moves_planned[:10], 1):
            print(f"\n{i}. {Path(move['from']).name}")
            print(f"   TO: {move['to']}")
        
        if len(self.moves_planned) > 10:
            print(f"\n... and {len(self.moves_planned) - 10:,} more files")
        
        if not dry_run:
            print("\n🚀 Executing moves in turbo mode...")
            
            def move_file(move):
                try:
                    src = Path(move['from'])
                    dst = Path(move['to'])
                    
                    # Create destination
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Handle conflicts
                    if dst.exists():
                        counter = 1
                        while dst.exists():
                            dst = dst.parent / f"{dst.stem}_{counter}{dst.suffix}"
                            counter += 1
                    
                    shutil.move(str(src), str(dst))
                    return True
                except:
                    return False
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = [executor.submit(move_file, move) for move in self.moves_planned]
                
                success = 0
                for i, future in enumerate(futures, 1):
                    if future.result():
                        success += 1
                    
                    if i % 100 == 0:
                        print(f"  Progress: {i:,}/{len(self.moves_planned):,} ({i/len(self.moves_planned)*100:.1f}%)", end='\r')
            
            print(f"\n\n✅ Moved {success:,} files successfully!")
        
        print("="*70)

def main():
    print("\n" + "⚡"*35)
    print("  BATCH ORGANIZER TURBO - AI-Powered")
    print("⚡"*35 + "\n")
    
    organizer = TurboOrganizer()
    
    # Source directories
    sources = [
        Path("/Volumes/4TBSG/KTK 2026 TO SORT"),
        Path("/Volumes/6TB/KONTAKT_LAB"),
        Path("/Volumes/6TB/WAVE_MASTER"),
    ]
    
    print("📂 Source directories:")
    for src in sources:
        status = "✓" if src.exists() else "✗"
        print(f"  {status} {src}")
    
    # Scan and plan
    organizer.batch_scan_and_plan(sources)
    
    # Execute (dry-run by default)
    organizer.execute_turbo(dry_run=True)
    
    print("\n💡 To actually organize:")
    print("   python3 batch_organizer_turbo.py --live")

if __name__ == "__main__":
    import sys
    dry_run = '--live' not in sys.argv
    
    if not dry_run:
        print("\n🔴 LIVE MODE!")
        response = input("Type 'ORGANIZE' to confirm: ")
        if response != 'ORGANIZE':
            sys.exit(0)
    
    main()

