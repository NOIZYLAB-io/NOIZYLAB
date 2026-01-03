#!/usr/bin/env python3
"""
🔍 ROB'S ORIGINALS - METADATA SCANNER
Finds WAV files WITHOUT metadata = ROB's original work!
Separates HIS creations from library content!
GENIUS filter for 40 years of work!

HARD RULE #19 support!!!
Built by CB_01 for ROB!
GORUNFREE X1000!!!
"""

import os
from pathlib import Path
import struct

class MetadataScanner:
    """Scan WAV files for metadata - none = ROB's originals!"""
    
    def __init__(self):
        self.robs_originals = []
        self.library_content = []
        
    def check_wav_metadata(self, wav_path):
        """
        Check if WAV has metadata
        
        Returns:
        - 'ORIGINAL' if no metadata (ROB's work!)
        - 'LIBRARY' if has metadata (commercial)
        """
        try:
            with open(wav_path, 'rb') as f:
                # Read WAV header
                riff = f.read(4)
                if riff != b'RIFF':
                    return 'UNKNOWN'
                
                # Skip size
                f.read(4)
                
                # Check WAVE
                wave = f.read(4)
                if wave != b'WAVE':
                    return 'UNKNOWN'
                
                # Scan for metadata chunks
                has_metadata = False
                
                while True:
                    chunk_header = f.read(8)
                    if len(chunk_header) < 8:
                        break
                    
                    chunk_id = chunk_header[:4]
                    chunk_size = struct.unpack('<I', chunk_header[4:8])[0]
                    
                    # Check for metadata chunks
                    if chunk_id in [b'LIST', b'INFO', b'ID3 ', b'id3 ', 
                                   b'bext', b'iXML', b'cart', b'axml']:
                        has_metadata = True
                        break
                    
                    # Skip chunk data
                    f.seek(chunk_size, 1)
                    if chunk_size % 2:
                        f.seek(1, 1)
                
                if has_metadata:
                    return 'LIBRARY'  # Has metadata = commercial/library
                else:
                    return 'ORIGINAL'  # No metadata = ROB's work!
                    
        except Exception as e:
            return 'ERROR'
    
    def scan_file(self, filepath):
        """Scan single file"""
        if not filepath.lower().endswith('.wav'):
            return
        
        result = self.check_wav_metadata(filepath)
        
        if result == 'ORIGINAL':
            self.robs_originals.append(filepath)
        elif result == 'LIBRARY':
            self.library_content.append(filepath)
    
    def scan_directory(self, directory, max_files=None):
        """Scan entire directory"""
        print(f"🔍 Scanning: {directory}")
        
        count = 0
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.wav'):
                    filepath = os.path.join(root, file)
                    self.scan_file(filepath)
                    count += 1
                    
                    if count % 100 == 0:
                        print(f"  ⚡ Scanned: {count} WAVs...")
                    
                    if max_files and count >= max_files:
                        return
        
        print(f"  ✅ Complete: {count} WAVs scanned")
    
    def generate_report(self):
        """Generate complete report"""
        
        print("\n" + "="*60)
        print("📊 ROB'S ORIGINALS vs LIBRARY CONTENT")
        print("="*60)
        print()
        print(f"🎵 ROB'S ORIGINALS (no metadata): {len(self.robs_originals)}")
        print(f"📚 LIBRARY CONTENT (has metadata): {len(self.library_content)}")
        print()
        
        # Save lists
        with open('/tmp/robs_originals.txt', 'w') as f:
            f.write('\n'.join(self.robs_originals))
        
        with open('/tmp/library_content.txt', 'w') as f:
            f.write('\n'.join(self.library_content))
        
        print("💾 Lists saved:")
        print("   /tmp/robs_originals.txt (ROB's 40-year originals!)")
        print("   /tmp/library_content.txt (commercial/library)")
        print()
        
        # Show sample originals
        if self.robs_originals:
            print("🎵 Sample of ROB's ORIGINALS:")
            for orig in self.robs_originals[:10]:
                print(f"   {Path(orig).name}")
        
        print()
        print("✅ METADATA SCAN COMPLETE!")
        print("🎯 ROB'S ORIGINALS IDENTIFIED!")
        print()
        print("GORUNFREE X1000!!! 🚀")

def main():
    """Scan for ROB's originals!"""
    print("""
🔥⚡🚀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚀⚡🔥

    ROB'S ORIGINALS - METADATA SCANNER
    
    Files WITHOUT metadata = ROB's work!
    Files WITH metadata = Library content!
    
    GENIUS 40-YEAR FILTER!!! 💡
    
🔥⚡🚀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🚀⚡🔥
    """)
    
    scanner = MetadataScanner()
    
    # Scan key locations
    important_dirs = [
        "/Users/m2ultra/NOIZYLAB/_CONSOLIDATED_CODE/",
        "/Users/m2ultra/Github/Noizyfish/",
    ]
    
    for directory in important_dirs:
        if os.path.exists(directory):
            scanner.scan_directory(directory, max_files=1000)  # Limit for speed
    
    scanner.generate_report()

if __name__ == "__main__":
    main()

