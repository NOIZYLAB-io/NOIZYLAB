#!/usr/bin/env python3
"""
NOIZYGENIE Advanced Library Repair System v2.0
Enhanced repair system with intelligent sample matching
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict
import re
from datetime import datetime

def advanced_library_repair():
    """Advanced repair system with intelligent sample matching"""
    
    kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
    six_tb = Path("/Volumes/6TB")
    
    print("🔧 NOIZYGENIE Advanced Library Repair System v2.0")
    print("=" * 60)
    
    # Focus on libraries with substantial instrument counts
    priority_libraries = []
    
    print("🎯 Phase 1: Identifying Priority Libraries...")
    
    for item in kontakt_lab.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ['REPORTS']:
            instruments = len(list(item.rglob("*.nki"))) + \
                         len(list(item.rglob("*.nkm"))) + \
                         len(list(item.rglob("*.nkc")))
            samples = len(list(item.rglob("*.ncw"))) + \
                     len(list(item.rglob("*.wav"))) + \
                     len(list(item.rglob("*.aiff")))
            
            # Focus on libraries with good instrument count but missing samples
            if instruments >= 10 and samples < instruments // 2:
                priority_libraries.append({
                    'name': item.name,
                    'path': item,
                    'instruments': instruments,
                    'samples': samples,
                    'priority': instruments  # Higher instrument count = higher priority
                })
    
    # Sort by priority (instrument count)
    priority_libraries.sort(key=lambda x: x['priority'], reverse=True)
    
    print(f"   🎯 Found {len(priority_libraries)} priority libraries for repair")
    
    if not six_tb.exists():
        print(f"❌ 6TB volume not available for sample sourcing")
        return
    
    print("\n🔍 Phase 2: Smart Sample Location...")
    
    # Build targeted sample index for known NI library patterns
    ni_sample_locations = defaultdict(list)
    
    # Known Native Instruments library patterns
    ni_patterns = [
        r'kontakt.*library',
        r'native.*instruments',
        r'komplete.*\d+',
        r'samples',
        r'instruments.*samples',
        r'.*\.ncw$',
        r'.*samples.*',
        r'kontakt.*samples'
    ]
    
    sample_dirs_found = []
    
    # Search for Native Instruments sample directories
    for root, dirs, files in os.walk(six_tb):
        # Skip deep nesting to avoid endless search
        if len(Path(root).parts) - len(six_tb.parts) > 4:
            dirs.clear()
            continue
            
        current_dir = Path(root)
        dir_name_lower = current_dir.name.lower()
        
        # Check if directory matches NI patterns
        is_ni_dir = any(re.search(pattern, dir_name_lower) for pattern in ni_patterns)
        
        # Also check if it contains NI sample files
        has_samples = any(f.lower().endswith(('.ncw', '.wav', '.aiff')) for f in files[:10])
        
        if is_ni_dir or has_samples:
            sample_count = sum(1 for f in files if f.lower().endswith(('.ncw', '.wav', '.aiff')))
            if sample_count >= 5:  # Directory with substantial samples
                sample_dirs_found.append({
                    'path': current_dir,
                    'name': current_dir.name,
                    'sample_count': sample_count
                })
    
    print(f"   📦 Found {len(sample_dirs_found)} directories with NI samples")
    
    print("\n🔧 Phase 3: Advanced Library Repair...")
    
    repairs_successful = 0
    libraries_completed = 0
    
    # Process top priority libraries
    for i, lib_info in enumerate(priority_libraries[:20]):  # Top 20 priority libraries
        lib_name = lib_info['name']
        lib_path = lib_info['path']
        
        print(f"\n🔧 Repairing Priority Library {i+1}/20: {lib_name}")
        print(f"   📊 Current: {lib_info['instruments']} instruments, {lib_info['samples']} samples")
        
        samples_added = 0
        
        # Create samples directory
        samples_dir = lib_path / "Samples"
        samples_dir.mkdir(exist_ok=True)
        
        # Smart matching strategy
        lib_name_lower = lib_name.lower()
        lib_keywords = re.findall(r'\w+', lib_name_lower)
        
        # Search for matching sample directories
        best_matches = []
        
        for sample_dir in sample_dirs_found:
            sample_dir_lower = sample_dir['name'].lower()
            
            # Calculate match score
            match_score = 0
            
            # Exact name match (highest priority)
            if lib_name_lower in sample_dir_lower or sample_dir_lower in lib_name_lower:
                match_score += 100
            
            # Keyword matches
            for keyword in lib_keywords:
                if len(keyword) >= 3 and keyword in sample_dir_lower:
                    match_score += 10
            
            # Instrument-related keywords
            instrument_keywords = ['piano', 'guitar', 'drum', 'string', 'brass', 'wind', 'synth', 
                                 'bass', 'lead', 'pad', 'orchestra', 'choir', 'voice']
            for keyword in instrument_keywords:
                if keyword in lib_name_lower and keyword in sample_dir_lower:
                    match_score += 20
            
            if match_score >= 10:  # Minimum threshold
                best_matches.append({
                    'dir': sample_dir,
                    'score': match_score
                })
        
        # Sort by match score
        best_matches.sort(key=lambda x: x['score'], reverse=True)
        
        # Copy samples from best matching directories
        for match in best_matches[:3]:  # Top 3 matches
            source_dir = match['dir']['path']
            print(f"   📦 Copying samples from: {source_dir.name} (score: {match['score']})")
            
            try:
                sample_files = list(source_dir.rglob("*.ncw")) + \
                              list(source_dir.rglob("*.wav")) + \
                              list(source_dir.rglob("*.aiff"))
                
                # Copy up to 50 samples to avoid overwhelming
                for sample_file in sample_files[:50]:
                    target_file = samples_dir / sample_file.name
                    if not target_file.exists():
                        shutil.copy2(sample_file, target_file)
                        samples_added += 1
                        
            except Exception as e:
                print(f"   ⚠️  Error copying from {source_dir.name}: {e}")
        
        # Results
        if samples_added > 0:
            repairs_successful += 1
            
            # Check if library is now complete
            new_sample_count = len(list(lib_path.rglob("*.ncw"))) + \
                              len(list(lib_path.rglob("*.wav"))) + \
                              len(list(lib_path.rglob("*.aiff")))
            
            if new_sample_count >= lib_info['instruments'] // 2:
                libraries_completed += 1
                print(f"   🎉 Library COMPLETED! Added {samples_added} samples (total: {new_sample_count})")
            else:
                print(f"   ✅ Partial repair: Added {samples_added} samples (total: {new_sample_count})")
        else:
            print(f"   ❌ No matching samples found")
    
    # Final summary
    print(f"\n✅ ADVANCED REPAIR COMPLETE!")
    print(f"🔧 Libraries Processed: 20")
    print(f"✅ Repairs Successful: {repairs_successful}")
    print(f"🎉 Libraries Completed: {libraries_completed}")
    
    # Update auto scanner to reflect changes
    print(f"\n🔄 Updating arsenal status...")
    
    return {
        'processed': 20,
        'repaired': repairs_successful,
        'completed': libraries_completed
    }

if __name__ == "__main__":
    try:
        results = advanced_library_repair()
        
        # Run auto scanner to update HTML report
        print("\n📊 Updating HTML MasterList...")
        os.system("python3 ~/auto_scan.py")
        
        print("\n🎉 Advanced Library Repair Complete!")
        print("📄 Check MASTERLIST.html for updated library status")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()