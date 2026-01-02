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
    
    # Generate HTML MasterList
    try:
        html_master = kontakt_lab / "MASTERLIST.html"
        
        # Generate HTML report
        html = []
        html.append("<!DOCTYPE html>")
        html.append("<html><head><meta charset='UTF-8'>")
        html.append("<title>NOIZYGENIE Arsenal MasterList</title>")
        html.append("<style>")
        html.append("body { font-family: Palatino, serif; font-size: 14px; background:#f8f8f8; padding:20px; }")
        html.append("h1 { text-align:center; color:#2c3e50; margin-bottom:10px; }")
        html.append(".subtitle { text-align:center; color:#7f8c8d; margin-bottom:30px; }")
        html.append(".stats { text-align:center; font-size:16px; margin:20px 0; padding:15px; background:white; border-radius:8px; }")
        html.append("table { border-collapse: collapse; width: 100%; margin-top:20px; background:white; border-radius:8px; overflow:hidden; }")
        html.append("th, td { border:1px solid #ddd; padding:8px 12px; text-align:left; }")
        html.append("th { background:#34495e; color:white; font-weight:bold; }")
        html.append("tr:nth-child(even) { background:#f9f9f9; }")
        html.append("tr:hover { background:#e8f4fd; }")
        html.append(".complete { color: #27ae60; font-weight:bold; }")
        html.append(".partial { color: #f39c12; font-weight:bold; }")
        html.append(".fragment { color: #e74c3c; font-weight:bold; }")
        html.append(".unknown { color: #95a5a6; font-weight:bold; }")
        html.append("</style></head><body>")

        html.append("<h1>🎹 NOIZYGENIE Arsenal MasterList 🎹</h1>")
        html.append(f"<div class='subtitle'>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>")
        
        html.append("<div class='stats'>")
        html.append(f"<strong>Total Libraries: {total_libs}</strong><br><br>")
        html.append(f"✅ <span class='complete'>Complete: {complete_count}</span> &nbsp;&nbsp; ")
        html.append(f"⚠️ <span class='partial'>Partial: {partial_count}</span> &nbsp;&nbsp; ")
        html.append(f"❌ <span class='fragment'>Fragments: {fragment_count}</span> &nbsp;&nbsp; ")
        html.append(f"❓ <span class='unknown'>Unknown: {unknown_count}</span>")
        html.append("</div>")

        html.append("<table><tr><th>Library Name</th><th>Status</th><th>Files</th></tr>")
        
        for lib_name, status in classifications.items():
            cls = "complete" if status == "COMPLETE" else "partial" if status == "PARTIAL" else "fragment" if status == "FRAGMENT" else "unknown"
            icon = "✅" if status == "COMPLETE" else "⚠️" if status == "PARTIAL" else "❌" if status == "FRAGMENT" else "❓"
            
            # Count files for this library
            lib_path = kontakt_lab / lib_name
            if lib_path.exists():
                total_files = sum(1 for f in lib_path.rglob("*") if f.is_file() and f.suffix.lower() in ['.nki', '.nkm', '.nkc', '.ncw', '.wav', '.aiff'])
            else:
                total_files = 0
                
            html.append(f"<tr><td><strong>{lib_name}</strong></td><td class='{cls}'>{icon} {status}</td><td>{total_files:,}</td></tr>")

        html.append("</table>")
        html.append("<div style='text-align:center; margin-top:30px; color:#7f8c8d;'>🎵 NOIZYGENIE Arsenal Management System 🎵</div>")
        html.append("</body></html>")

        with open(html_master, "w") as f:
            f.write("\\n".join(html))
        
        print(f"🌐 HTML MasterList updated: {html_master}")
        
    except Exception as e:
        print(f"⚠️ HTML generation error: {e}")
    
    return classifications, changes

if __name__ == "__main__":
    try:
        classifications, changes = auto_scan_arsenal()
        print("\n✅ Auto scan complete!")
    except Exception as e:
        print(f"❌ Error during auto scan: {e}")
        sys.exit(1)