#!/usr/bin/env python3
"""
NOIZYGENIE Arsenal Auto Scanner
Comprehensive library scanning and HTML masterlist generation
"""

from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Configuration
ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
REPORTS_DIR = ROOT / "REPORTS"
HTML_MASTER = ROOT / "MASTERLIST.html"

def scan_libraries():
    """Scan all libraries in KONTAKT_LAB"""
    print("🎹 NOIZYGENIE Arsenal Auto Scanner")
    print("=" * 50)
    print(f"📍 Scanning: {ROOT}")
    
    if not ROOT.exists():
        print(f"❌ KONTAKT_LAB not found at {ROOT}")
        return {}, {}, {}, 0, 0, 0, 0
    
    libraries = {}
    broken_birds = []
    
    # Scan all subdirectories
    for item in ROOT.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name != "REPORTS":
            lib_name = item.name
            extensions = defaultdict(list)
            
            # Scan for NI files
            for ext in [".nki", ".nkm", ".nkc", ".ncw", ".wav", ".aiff"]:
                files = list(item.rglob(f"*{ext}"))
                extensions[ext] = [str(f) for f in files]
            
            libraries[lib_name] = dict(extensions)
    
    # Classify libraries
    classifications = {}
    complete = partial = fragment = unknown = 0
    
    for lib_name, exts in libraries.items():
        instruments = len(exts.get(".nki", [])) + len(exts.get(".nkm", [])) + len(exts.get(".nkc", []))
        samples = len(exts.get(".ncw", [])) + len(exts.get(".wav", [])) + len(exts.get(".aiff", []))
        
        if instruments == 0 and samples == 0:
            status = "UNKNOWN"
            unknown += 1
        elif samples >= instruments * 0.8 and instruments > 0:
            status = "COMPLETE"
            complete += 1
        elif samples > 0:
            status = "PARTIAL"
            partial += 1
        else:
            status = "FRAGMENT"
            fragment += 1
            broken_birds.append(lib_name)
        
        classifications[lib_name] = status
    
    # Print summary
    total_files = sum(sum(len(files) for files in lib.values()) for lib in libraries.values())
    print(f"📊 Arsenal Status:")
    print(f"   Total Libraries: {len(libraries)}")
    print(f"   Total Files: {total_files:,}")
    print(f"   ✅ Complete: {complete}")
    print(f"   ⚠️ Partial: {partial}")
    print(f"   ❌ Fragment: {fragment}")
    print(f"   ❓ Unknown: {unknown}")
    
    return libraries, broken_birds, classifications, complete, partial, fragment, unknown

def save_html_masterlist(libraries, broken_birds, classifications, complete, partial, fragment, unknown):
    """Generate beautiful HTML masterlist"""
    total_libs = len(classifications)
    html.append("<!DOCTYPE html>")
    html.append("<html><head><meta charset='UTF-8'>")
    html.append("<title>NOIZYGENIE Arsenal MasterList</title>")
    html.append("<style>")
    html.append("* { font-family: Palatino, 'Palatino Linotype', 'Book Antiqua', serif; font-size: 14px; }")
    html.append("body { background:#f8f8f8; padding:20px; line-height: 1.6; }")
    html.append("h1 { text-align:center; color:#2c3e50; font-size: 24px; font-weight: bold; }")
    html.append(".stats { text-align:center; font-size:14px; margin:20px 0; padding:15px; background:#fff; border-radius:8px; }")
    html.append("table { border-collapse: collapse; width: 100%; margin-top:20px; background:#fff; }")
    html.append("th, td { border:1px solid #ccc; padding:8px 12px; text-align:left; font-size: 14px; }")
    html.append("th { background:#34495e; color:#fff; font-weight:bold; font-size: 14px; }")
    html.append("tr:nth-child(even) { background:#f9f9f9; }")
    html.append("tr:hover { background:#e8f4fd; }")
    html.append(".complete { color: #27ae60; font-weight:bold; font-size: 14px; }")
    html.append(".partial { color: #f39c12; font-weight:bold; font-size: 14px; }")
    html.append(".fragment { color: #e74c3c; font-weight:bold; font-size: 14px; }")
    html.append(".unknown { color: #95a5a6; font-weight:bold; font-size: 14px; }")
    html.append(".timestamp { text-align:center; color:#7f8c8d; font-size:14px; margin-top:20px; }")
    html.append("</style></head><body>")

    html.append("<h1>🎹 NOIZYGENIE Arsenal MasterList 🎹</h1>")
    
    html.append(f"<div class='stats'>")
    html.append(f"<strong>Total Libraries: {total_libs}</strong><br>")
    html.append(f"✅ Complete: {complete} &nbsp;&nbsp; ⚠️ Partial: {partial} &nbsp;&nbsp; ❌ Fragments: {fragment} &nbsp;&nbsp; ❓ Unknown: {unknown}")
    html.append(f"</div>")

    html.append("<table>")
    html.append("<tr><th>Library Name</th><th>Status</th><th>Total Files</th><th>Instruments</th><th>Samples</th><th>Ratio</th></tr>")

    # Sort libraries by status priority (Complete first, then Partial, etc.)
    status_priority = {"COMPLETE": 1, "PARTIAL": 2, "FRAGMENT": 3, "UNKNOWN": 4}
    sorted_libraries = sorted(libraries.items(), key=lambda x: (status_priority.get(classifications[x[0]], 5), x[0]))

    for lib_name, exts in sorted_libraries:
        total_files = sum(len(v) for v in exts.values())
        status = classifications[lib_name]
        instrument_count = len(exts.get(".nki", [])) + len(exts.get(".nkm", [])) + len(exts.get(".nkc", []))
        sample_count = len(exts.get(".ncw", [])) + len(exts.get(".wav", [])) + len(exts.get(".aiff", []))
        
        # Calculate ratio
        if instrument_count > 0:
            ratio = f"{sample_count / instrument_count:.1f}"
        else:
            ratio = "N/A"

        # Choose CSS class
        if "COMPLETE" in status:
            cls = "complete"
            status_icon = "✅"
        elif "PARTIAL" in status:
            cls = "partial"
            status_icon = "⚠️"
        elif "FRAGMENT" in status:
            cls = "fragment"
            status_icon = "❌"
        else:
            cls = "unknown"
            status_icon = "❓"

        html.append(f"<tr>")
        html.append(f"<td><strong>{lib_name}</strong></td>")
        html.append(f"<td class='{cls}'>{status_icon} {status}</td>")
        html.append(f"<td>{total_files}</td>")
        html.append(f"<td>{instrument_count}</td>")
        html.append(f"<td>{sample_count}</td>")
        html.append(f"<td>{ratio}</td>")
        html.append(f"</tr>")

    html.append("</table>")
    html.append(f"<div class='timestamp'>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>")
    html.append("</body></html>")

    # Ensure KONTAKT_LAB exists
    ROOT.mkdir(exist_ok=True)
    
    with open(HTML_MASTER, "w") as f:
        f.write("\n".join(html))

    print(f"🌐 HTML MasterList saved: {HTML_MASTER}")

def save_reports(libraries, broken_birds, classifications):
    """Save detailed reports"""
    REPORTS_DIR.mkdir(exist_ok=True, parents=True)
    
    # Save detailed library report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"arsenal_report_{timestamp}.txt"
    
    with open(report_file, 'w') as f:
        f.write("🎹 NOIZYGENIE Arsenal Detailed Report\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("LIBRARY DETAILS:\n")
        f.write("-" * 30 + "\n")
        
        for lib_name, exts in sorted(libraries.items()):
            f.write(f"\n{lib_name}:\n")
            f.write(f"  Status: {classifications[lib_name]}\n")
            for ext, files in exts.items():
                if files:
                    f.write(f"  {ext}: {len(files)} files\n")
        
        if broken_birds:
            f.write(f"\nFRAGMENT LIBRARIES ({len(broken_birds)}):\n")
            f.write("-" * 30 + "\n")
            for bird in broken_birds:
                f.write(f"  - {bird}\n")
    
    print(f"📁 Reports saved to: {REPORTS_DIR}")

def run_complete_scan():
    """Run complete scan and generate all outputs"""
    # Scan libraries
    libraries, broken_birds, classifications, complete, partial, fragment, unknown = scan_libraries()
    
    # Generate HTML masterlist
    save_html_masterlist(libraries, classifications, complete, partial, fragment, unknown)
    save_reports(libraries, broken_birds, classifications)
    
    print(f"\n✅ Auto scan complete!")

if __name__ == "__main__":
    run_complete_scan()
