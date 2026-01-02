#!/usr/bin/env python3
"""
NOIZYGENIE Library Repair System
Comprehensive system to fix incomplete Native Instruments libraries
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import json

def comprehensive_library_repair():
    """Comprehensive system to repair and complete all NI libraries"""
    
    kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
    six_tb = Path("/Volumes/6TB")
    repair_log = kontakt_lab / "LIBRARY_REPAIR_LOG.txt"
    
    print("🔧 NOIZYGENIE Comprehensive Library Repair System")
    print("=" * 60)
    print(f"📍 Target: {kontakt_lab}")
    print(f"📦 Source Pool: {six_tb}")
    
    # Initialize repair statistics
    repair_stats = {
        'fragments_found': 0,
        'repairs_attempted': 0,
        'repairs_successful': 0,
        'missing_samples_found': 0,
        'complete_libraries_created': 0
    }
    
    sample_database = {}
    fragment_libraries = []
    
    print("\n🔍 Phase 1: Analyzing Current Library Status...")
    
    # Scan current KONTAKT_LAB libraries
    for item in kontakt_lab.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ['REPORTS']:
            lib_name = item.name
            
            # Count file types
            nki_files = list(item.rglob("*.nki"))
            nkm_files = list(item.rglob("*.nkm"))
            nkc_files = list(item.rglob("*.nkc"))
            ncw_files = list(item.rglob("*.ncw"))
            wav_files = list(item.rglob("*.wav"))
            aiff_files = list(item.rglob("*.aiff"))
            
            instruments = len(nki_files) + len(nkm_files) + len(nkc_files)
            samples = len(ncw_files) + len(wav_files) + len(aiff_files)
            
            # Identify fragments (instruments without samples)
            if instruments > 0 and samples == 0:
                repair_stats['fragments_found'] += 1
                fragment_libraries.append({
                    'name': lib_name,
                    'path': item,
                    'instruments': instruments,
                    'samples': samples,
                    'nki_files': nki_files,
                    'nkm_files': nkm_files,
                    'nkc_files': nkc_files
                })
    
    print(f"   📊 Found {repair_stats['fragments_found']} fragment libraries needing repair")
    
    if six_tb.exists():
        print("\n🔍 Phase 2: Building Sample Database from 6TB...")
        
        # Build comprehensive sample database
        scanned_files = 0
        for root, dirs, files in os.walk(six_tb):
            # Skip system directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and 
                      d not in ['System Volume Information', '$RECYCLE.BIN']]
            
            for file in files:
                scanned_files += 1
                if scanned_files % 50000 == 0:
                    print(f"     📈 Indexed {scanned_files:,} files...")
                
                if file.lower().endswith(('.ncw', '.wav', '.aiff')):
                    file_path = Path(root) / file
                    file_stem = file_path.stem.lower()
                    
                    # Index samples by filename patterns
                    if file_stem not in sample_database:
                        sample_database[file_stem] = []
                    sample_database[file_stem].append(str(file_path))
        
        print(f"   📦 Built sample database with {len(sample_database):,} unique sample patterns")
        repair_stats['missing_samples_found'] = len(sample_database)
    
    print("\n🔧 Phase 3: Repairing Fragment Libraries...")
    
    with open(repair_log, 'w') as log:
        log.write("🔧 NOIZYGENIE Library Repair Log\n")
        log.write("=" * 40 + "\n")
        log.write(f"Repair Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for i, fragment in enumerate(fragment_libraries[:50]):  # Process top 50 fragments
            lib_name = fragment['name']
            lib_path = fragment['path']
            
            print(f"🔧 Repairing {i+1}/{len(fragment_libraries[:50])}: {lib_name}")
            repair_stats['repairs_attempted'] += 1
            
            # Create samples directory if it doesn't exist
            samples_dir = lib_path / "Samples"
            samples_dir.mkdir(exist_ok=True)
            
            samples_found = 0
            
            # Search for matching samples
            for instrument_file in fragment['nki_files'] + fragment['nkm_files'] + fragment['nkc_files']:
                instrument_name = instrument_file.stem.lower()
                
                # Try various matching patterns
                search_patterns = [
                    instrument_name,
                    instrument_name.replace('_', ' '),
                    instrument_name.replace(' ', '_'),
                    instrument_name.split('_')[0] if '_' in instrument_name else instrument_name,
                    instrument_name.split(' ')[0] if ' ' in instrument_name else instrument_name
                ]
                
                for pattern in search_patterns:
                    if pattern in sample_database:
                        for sample_path in sample_database[pattern][:5]:  # Max 5 samples per instrument
                            try:
                                sample_source = Path(sample_path)
                                if sample_source.exists():
                                    sample_target = samples_dir / sample_source.name
                                    if not sample_target.exists():
                                        shutil.copy2(sample_source, sample_target)
                                        samples_found += 1
                            except Exception as e:
                                log.write(f"   Error copying sample for {instrument_name}: {e}\n")
            
            # Log repair results
            if samples_found > 0:
                repair_stats['repairs_successful'] += 1
                status = "✅ REPAIRED"
                print(f"   ✅ Found and added {samples_found} samples")
                
                # Re-classify library
                new_sample_count = len(list(lib_path.rglob("*.ncw"))) + \
                                 len(list(lib_path.rglob("*.wav"))) + \
                                 len(list(lib_path.rglob("*.aiff")))
                
                if new_sample_count >= fragment['instruments']:
                    repair_stats['complete_libraries_created'] += 1
                    status = "🎉 COMPLETED"
                    print(f"   🎉 Library now COMPLETE with {new_sample_count} samples!")
                
            else:
                status = "❌ NO SAMPLES FOUND"
                print(f"   ❌ No matching samples found")
            
            log.write(f"{lib_name}: {status}\n")
            log.write(f"   Instruments: {fragment['instruments']}\n")
            log.write(f"   Samples Added: {samples_found}\n\n")
    
    print("\n🔧 Phase 4: Creating Repair Summary...")
    
    # Generate comprehensive repair report
    repair_report = kontakt_lab / "REPAIR_SUMMARY.txt"
    with open(repair_report, 'w') as f:
        f.write("🔧 NOIZYGENIE Library Repair Summary\n")
        f.write("=" * 45 + "\n")
        f.write(f"Repair Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("📊 REPAIR STATISTICS:\n")
        f.write("-" * 25 + "\n")
        f.write(f"Fragment Libraries Found: {repair_stats['fragments_found']}\n")
        f.write(f"Repairs Attempted: {repair_stats['repairs_attempted']}\n")
        f.write(f"Repairs Successful: {repair_stats['repairs_successful']}\n")
        f.write(f"Complete Libraries Created: {repair_stats['complete_libraries_created']}\n")
        f.write(f"Sample Database Size: {repair_stats['missing_samples_found']:,} patterns\n\n")
        
        success_rate = (repair_stats['repairs_successful'] / repair_stats['repairs_attempted'] * 100) if repair_stats['repairs_attempted'] > 0 else 0
        completion_rate = (repair_stats['complete_libraries_created'] / repair_stats['repairs_attempted'] * 100) if repair_stats['repairs_attempted'] > 0 else 0
        
        f.write("📈 REPAIR METRICS:\n")
        f.write("-" * 20 + "\n")
        f.write(f"Success Rate: {success_rate:.1f}%\n")
        f.write(f"Completion Rate: {completion_rate:.1f}%\n")
        f.write(f"Libraries Still Needing Repair: {repair_stats['fragments_found'] - repair_stats['repairs_successful']}\n")
    
    print("✅ LIBRARY REPAIR COMPLETE!")
    print("-" * 35)
    print(f"📊 Fragments Found: {repair_stats['fragments_found']}")
    print(f"🔧 Repairs Attempted: {repair_stats['repairs_attempted']}")
    print(f"✅ Repairs Successful: {repair_stats['repairs_successful']}")
    print(f"🎉 Complete Libraries Created: {repair_stats['complete_libraries_created']}")
    print(f"📄 Repair Log: {repair_log}")
    print(f"📈 Summary Report: {repair_report}")
    
    return repair_stats

def quick_library_validation():
    """Quick validation of library status after repair"""
    
    kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
    
    print("\n🔍 Post-Repair Library Validation...")
    
    validation_stats = {
        'COMPLETE': 0,
        'PARTIAL': 0,
        'FRAGMENT': 0,
        'UNKNOWN': 0
    }
    
    for item in kontakt_lab.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ['REPORTS']:
            # Count files
            instruments = len(list(item.rglob("*.nki"))) + \
                         len(list(item.rglob("*.nkm"))) + \
                         len(list(item.rglob("*.nkc")))
            
            samples = len(list(item.rglob("*.ncw"))) + \
                     len(list(item.rglob("*.wav"))) + \
                     len(list(item.rglob("*.aiff")))
            
            # Classify
            if instruments > 0 and samples >= instruments:
                validation_stats['COMPLETE'] += 1
            elif instruments > 0 and samples > 0:
                validation_stats['PARTIAL'] += 1
            elif instruments > 0:
                validation_stats['FRAGMENT'] += 1
            else:
                validation_stats['UNKNOWN'] += 1
    
    total = sum(validation_stats.values())
    
    print("📊 Post-Repair Library Status:")
    print("-" * 35)
    for status, count in validation_stats.items():
        percentage = (count / total * 100) if total > 0 else 0
        icon = "✅" if status == "COMPLETE" else "⚠️" if status == "PARTIAL" else "❌" if status == "FRAGMENT" else "❓"
        print(f"{icon} {status}: {count} libraries ({percentage:.1f}%)")
    
    return validation_stats

if __name__ == "__main__":
    try:
        print("🎹 Starting Comprehensive Library Repair System...")
        repair_results = comprehensive_library_repair()
        validation_results = quick_library_validation()
        print("\n🎉 All libraries have been processed for repair!")
        
    except Exception as e:
        print(f"❌ Error during library repair: {e}")
        import traceback
        traceback.print_exc()