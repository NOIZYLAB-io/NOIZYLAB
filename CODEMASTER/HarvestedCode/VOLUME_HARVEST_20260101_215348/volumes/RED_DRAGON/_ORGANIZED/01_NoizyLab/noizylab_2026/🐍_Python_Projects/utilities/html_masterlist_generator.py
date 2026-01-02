#!/usr/bin/env python3
"""
NOIZYGENIE Arsenal HTML MasterList Generator
Creates a beautiful HTML report of all libraries with visual status indicators
"""

import os
from pathlib import Path
from collections import Counter
from datetime import datetime

def generate_html_masterlist():
    """Generate HTML MasterList from KONTAKT_LAB libraries"""
    
    kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
    html_master = kontakt_lab / "MASTERLIST.html"
    
    if not kontakt_lab.exists():
        print(f"❌ KONTAKT_LAB not found at {kontakt_lab}")
        return
    
    print("🌐 Generating HTML MasterList...")
    
    # Scan libraries and classify them
    libraries = {}
    classifications = {}
    
    for item in kontakt_lab.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ['REPORTS']:
            lib_name = item.name
            
            # Count file types
            file_types = {
                ".nki": list(item.rglob("*.nki")),
                ".nkm": list(item.rglob("*.nkm")),
                ".nkc": list(item.rglob("*.nkc")),
                ".ncw": list(item.rglob("*.ncw")),
                ".wav": list(item.rglob("*.wav")),
                ".aiff": list(item.rglob("*.aiff"))
            }
            
            libraries[lib_name] = file_types
            
            # Classify completeness
            instruments = len(file_types[".nki"]) + len(file_types[".nkm"]) + len(file_types[".nkc"])
            samples = len(file_types[".ncw"]) + len(file_types[".wav"]) + len(file_types[".aiff"])
            
            if instruments > 0 and samples > 0:
                if samples >= instruments * 5:
                    classifications[lib_name] = "COMPLETE"
                else:
                    classifications[lib_name] = "PARTIAL"
            elif instruments > 0:
                classifications[lib_name] = "FRAGMENT"
            else:
                classifications[lib_name] = "UNKNOWN"
    
    # Count by status
    complete = sum(1 for status in classifications.values() if "COMPLETE" in status)
    partial = sum(1 for status in classifications.values() if "PARTIAL" in status)
    fragment = sum(1 for status in classifications.values() if "FRAGMENT" in status)
    unknown = sum(1 for status in classifications.values() if "UNKNOWN" in status)
    
    # Generate HTML
    save_html_masterlist(libraries, [], classifications, complete, partial, fragment, unknown)

def save_html_masterlist(libraries, broken_birds, classifications, complete, partial, fragment, unknown):
    """Save HTML masterlist with beautiful styling"""
    
    kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
    html_master = kontakt_lab / "MASTERLIST.html"
    total_libs = len(classifications)

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
    html.append(".status-badge { padding:4px 8px; border-radius:4px; font-size:12px; }")
    html.append(".complete-badge { background:#d5f4e6; }")
    html.append(".partial-badge { background:#fef9e7; }")
    html.append(".fragment-badge { background:#fadbd8; }")
    html.append(".unknown-badge { background:#eaeded; }")
    html.append("</style></head><body>")

    html.append("<h1>🎹 NOIZYGENIE Arsenal MasterList 🎹</h1>")
    html.append(f"<div class='subtitle'>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>")
    
    html.append("<div class='stats'>")
    html.append(f"<strong>Total Libraries: {total_libs}</strong><br><br>")
    html.append(f"✅ <span class='complete'>Complete: {complete}</span> &nbsp;&nbsp; ")
    html.append(f"⚠️ <span class='partial'>Partial: {partial}</span> &nbsp;&nbsp; ")
    html.append(f"❌ <span class='fragment'>Fragments: {fragment}</span> &nbsp;&nbsp; ")
    html.append(f"❓ <span class='unknown'>Unknown: {unknown}</span>")
    html.append("</div>")

    html.append("<table>")
    html.append("<tr><th>Library Name</th><th>Status</th><th>Total Files</th><th>Instruments</th><th>Samples</th><th>Details</th></tr>")

    # Sort libraries by status (complete first, then by file count)
    sorted_libs = sorted(libraries.items(), key=lambda x: (
        0 if "COMPLETE" in classifications[x[0]] else
        1 if "PARTIAL" in classifications[x[0]] else
        2 if "FRAGMENT" in classifications[x[0]] else 3,
        -sum(len(v) for v in x[1].values())  # Negative for descending order
    ))

    for lib, exts in sorted_libs:
        total_files = sum(len(v) for v in exts.values())
        status = classifications[lib]
        instrument_count = len(exts.get(".nki", [])) + len(exts.get(".nkm", [])) + len(exts.get(".nkc", []))
        sample_count = len(exts.get(".ncw", [])) + len(exts.get(".wav", [])) + len(exts.get(".aiff", []))

        # Choose CSS class and badge
        if "COMPLETE" in status:
            cls = "complete"
            badge_cls = "complete-badge"
            status_icon = "✅"
        elif "PARTIAL" in status:
            cls = "partial"
            badge_cls = "partial-badge"
            status_icon = "⚠️"
        elif "FRAGMENT" in status:
            cls = "fragment"
            badge_cls = "fragment-badge"
            status_icon = "❌"
        else:
            cls = "unknown"
            badge_cls = "unknown-badge"
            status_icon = "❓"

        # File type breakdown
        file_details = f".nki({len(exts.get('.nki', []))}) .nkm({len(exts.get('.nkm', []))}) .ncw({len(exts.get('.ncw', []))}) .wav({len(exts.get('.wav', []))})"

        html.append(f"<tr>")
        html.append(f"<td><strong>{lib}</strong></td>")
        html.append(f"<td><span class='status-badge {badge_cls}'>{status_icon} <span class='{cls}'>{status}</span></span></td>")
        html.append(f"<td><strong>{total_files:,}</strong></td>")
        html.append(f"<td>{instrument_count:,}</td>")
        html.append(f"<td>{sample_count:,}</td>")
        html.append(f"<td><small>{file_details}</small></td>")
        html.append(f"</tr>")

    html.append("</table>")
    
    html.append("<div style='text-align:center; margin-top:30px; color:#7f8c8d;'>")
    html.append("🎵 NOIZYGENIE Arsenal Management System 🎵")
    html.append("</div>")
    
    html.append("</body></html>")

    with open(html_master, "w") as f:
        f.write("\n".join(html))

    print(f"🌐 HTML MasterList saved: {html_master}")
    return str(html_master)

if __name__ == "__main__":
    generate_html_masterlist()