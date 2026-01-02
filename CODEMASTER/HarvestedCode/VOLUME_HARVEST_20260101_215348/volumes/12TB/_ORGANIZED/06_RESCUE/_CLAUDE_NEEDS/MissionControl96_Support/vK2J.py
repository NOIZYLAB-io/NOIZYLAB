#!/usr/bin/env python3
"""
Volume Chooser and Scanner for Native Instruments Files
Select a volume and scan for NI file types
"""

import os
from pathlib import Path

def scan_volume_for_ni_files():
    # Available mounted volumes (updated with real volume names)
    volumes = [
        "12TB",
        "4TB BLK", 
        "4TB Lacie",
        "4TB_Utility",
        "4TBSG",
        "6TB",
        "JOE",
        "MAG 4TB",
        "RED DRAGON",
        "SIDNEY"
    ]
    
    print("🎹 NOIZYGENIE Volume Scanner for Native Instruments Files")
    print("=" * 60)
    print("📁 Available Volumes:")
    
    for i, volume in enumerate(volumes, 1):
        volume_path = Path(f"/Volumes/{volume}")
        status = "✅ Mounted" if volume_path.exists() else "❌ Not Available"
        print(f"   {i:2d}. {volume:<15} {status}")
    
    print(f"\n🔍 Current selection: Volume #{choice} - {volumes[choice-1]}")
    
    # Scan the selected volume
    selected_volume = volumes[choice - 1]
    target_path = Path(f"/Volumes/{selected_volume}")
    
    if not target_path.exists():
        print(f"❌ Volume '{selected_volume}' not found!")
        return
    
    print(f"\n🔍 Scanning: {selected_volume}")
    print("   Looking for: .nki, .nkm, .nkc, .ncw, .wav, .aiff files")
    
    # Track NI files
    ni_files = {
        '.nki': [],
        '.nkm': [], 
        '.nkc': [],
        '.ncw': [],
        '.wav': [],
        '.aiff': []
    }
    
    scanned_dirs = 0
    total_files = 0
    
    try:
        for root, dirs, files in os.walk(target_path):
            scanned_dirs += 1
            
            # Limit depth to prevent infinite scanning
            if len(Path(root).parts) - len(target_path.parts) > 8:
                dirs.clear()
                continue
                
            # Progress indicator
            if scanned_dirs % 1000 == 0:
                print(f"      📊 Scanned {scanned_dirs:,} directories...")
            
            for file in files:
                total_files += 1
                file_lower = file.lower()
                
                for ext in ni_files.keys():
                    if file_lower.endswith(ext):
                        file_path = Path(root) / file
                        ni_files[ext].append(str(file_path))
        
        # Results
        print(f"\n📊 SCAN RESULTS for {selected_volume}:")
        print(f"   📁 Directories scanned: {scanned_dirs:,}")
        print(f"   📄 Total files found: {total_files:,}")
        
        total_ni_files = sum(len(files) for files in ni_files.values())
        print(f"   🎹 Native Instruments files: {total_ni_files:,}")
        
        if total_ni_files > 0:
            print(f"\n🎯 NI File Breakdown:")
            for ext, files in ni_files.items():
                if files:
                    print(f"      {ext}: {len(files):,} files")
        
        # Save detailed results
        output_file = Path.home() / "Desktop" / f"volume_scan_{selected_volume.replace(' ', '_')}.txt"
        
        with open(output_file, "w") as f:
            f.write(f"🎹 NOIZYGENIE Volume Scan Results\n")
            f.write(f"Volume: {selected_volume}\n")
            f.write(f"Scan Date: {os.popen('date').read().strip()}\n")
            f.write(f"Total NI Files: {total_ni_files:,}\n\n")
            
            for ext, files in ni_files.items():
                if files:
                    f.write(f"\n{ext.upper()} FILES ({len(files):,}):\n")
                    f.write("-" * 50 + "\n")
                    for file_path in files:
                        f.write(f"{file_path}\n")
        
        print(f"\n📄 Detailed results saved to: {output_file.name}")
        
        # Suggest next actions
        if total_ni_files > 0:
            print(f"\n🎯 NEXT ACTIONS:")
            print(f"   📁 Organize files into KONTAKT_LAB")
            print(f"   🔧 Run library repair system") 
            print(f"   📊 Update master inventory")
        
    except Exception as e:
        print(f"❌ Error scanning {selected_volume}: {e}")

# Configuration - change this number to select different volume
choice = 6  # Default to 6TB (volume index 6)

if __name__ == "__main__":
    scan_volume_for_ni_files()
