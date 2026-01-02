#!/usr/bin/env python3
"""
NOIZYGENIE Arsenal Auto Scanner
Automated scanning and monitoring of Native Instruments libraries
"""

import os
import sys
import json
from pathlib import Path
from collections import Counter
from datetime import datetime

def auto_scan_arsenal():
    """Automated arsenal scanning with history tracking"""
    
    kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
    reports_dir = kontakt_lab / "REPORTS"
    
    # Ensure directories exist
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    snapshot_file = reports_dir / "last_snapshot.json"
    history_file = reports_dir / "arsenal_history.log"
    
    print("🎹 NOIZYGENIE Arsenal Auto Scanner")
    print("=" * 50)
    print(f"📍 Scanning: {kontakt_lab}")
    
    if not kontakt_lab.exists():
        print(f"❌ KONTAKT_LAB not found at {kontakt_lab}")
        return
    
    # Initialize counters and classification
    library_stats = {
        'COMPLETE': [],
        'PARTIAL': [],  
        'FRAGMENT': [],
        'UNKNOWN': []
    }
    
    file_counters = Counter()
    total_files = 0
    classifications = {}
    
    # Scan all directories in KONTAKT_LAB
    for item in kontakt_lab.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name != 'REPORTS':
            lib_name = item.name
            
            # Count different file types
            nki_files = list(item.rglob("*.nki"))
            nkm_files = list(item.rglob("*.nkm")) 
            nkc_files = list(item.rglob("*.nkc"))
            ncw_files = list(item.rglob("*.ncw"))
            wav_files = list(item.rglob("*.wav"))
            aiff_files = list(item.rglob("*.aiff"))
            
            # Total instruments and samples
            instruments = len(nki_files) + len(nkm_files) + len(nkc_files)
            samples = len(ncw_files) + len(wav_files) + len(aiff_files)
            lib_total = instruments + samples
            
            # Update global counters
            file_counters['.nki'] += len(nki_files)
            file_counters['.nkm'] += len(nkm_files)
            file_counters['.nkc'] += len(nkc_files)
            file_counters['.ncw'] += len(ncw_files)
            file_counters['.wav'] += len(wav_files)
            file_counters['.aiff'] += len(aiff_files)
            total_files += lib_total
            
            # Classify library completeness
            if instruments > 0 and samples > 0:
                # Has both instruments and samples
                if samples >= instruments * 3:  # Good sample-to-instrument ratio
                    classification = 'COMPLETE'
                else:
                    classification = 'PARTIAL'
            elif instruments > 0 and samples == 0:
                # Only instruments, likely incomplete
                classification = 'FRAGMENT' 
            elif instruments == 0 and samples > 0:
                # Only samples, orphaned
                classification = 'FRAGMENT'
            else:
                # No relevant files
                classification = 'UNKNOWN'
            
            classifications[lib_name] = classification
            library_stats[classification].append({
                'name': lib_name,
                'instruments': instruments,
                'samples': samples,
                'total': lib_total
            })
    
    # Compare with previous scan
    changes = []
    if snapshot_file.exists():
        with open(snapshot_file, "r") as f:
            last_data = json.load(f)
        last_libs = last_data.get("libraries", {})

        # Check for new or changed libraries
        for lib, status in classifications.items():
            old_status = last_libs.get(lib)
            if old_status is None:
                changes.append(f"+ New Library: {lib} ({status})")
            elif old_status != status:
                changes.append(f"~ Status Change: {lib} {old_status} → {status}")

        # Check for removed libraries
        for lib in last_libs:
            if lib not in classifications:
                changes.append(f"- Removed Library: {lib} ({last_libs[lib]})")

    # Save current snapshot
    with open(snapshot_file, "w") as f:
        json.dump({"libraries": classifications, "timestamp": datetime.now().isoformat()}, f, indent=2)

    # Update history log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    complete_count = len(library_stats['COMPLETE'])
    partial_count = len(library_stats['PARTIAL'])
    fragment_count = len(library_stats['FRAGMENT'])
    unknown_count = len(library_stats['UNKNOWN'])
    total_libs = sum(len(libs) for libs in library_stats.values())
    
    with open(history_file, "a") as f:
        f.write(f"[{timestamp}] Total: {total_libs}, ✅ {complete_count}, ⚠️ {partial_count}, ❌ {fragment_count}, ❓ {unknown_count}\n")
        for change in changes:
            f.write(f"   {change}\n")
        f.write("\n")
    
    # Console output
    print(f"📊 Arsenal Status:")
    print(f"   Total Libraries: {total_libs}")
    print(f"   Total Files: {total_files:,}")
    print(f"   ✅ Complete: {complete_count}")
    print(f"   ⚠️ Partial: {partial_count}")  
    print(f"   ❌ Fragment: {fragment_count}")
    print(f"   ❓ Unknown: {unknown_count}")
    
    if changes:
        print(f"\n🔄 Changes Detected ({len(changes)}):")
        for change in changes[:5]:  # Show first 5 changes
            print(f"   {change}")
        if len(changes) > 5:
            print(f"   ... and {len(changes) - 5} more changes")
    else:
        print("\n🔄 No changes detected since last scan")
    
    print(f"\n📁 Reports saved to: {reports_dir}")
    return classifications, changes

if __name__ == "__main__":
    try:
        classifications, changes = auto_scan_arsenal()
        print("\n✅ Auto scan complete!")
    except Exception as e:
        print(f"❌ Error during auto scan: {e}")
        sys.exit(1)