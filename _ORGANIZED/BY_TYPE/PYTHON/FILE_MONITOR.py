#!/usr/bin/env python3
"""
👁️ REAL-TIME FILE MONITOR 👁️

Monitor for new WAV files and auto-organize them!

Features:
- Watch folders for new files
- Auto-organize on detection
- Real-time notifications
- Continuous monitoring
- Batch processing
"""

import os
import time
from pathlib import Path
from datetime import datetime
import hashlib

# ============================================================================
# CONFIGURATION
# ============================================================================

WATCH_FOLDERS = [
    Path.home() / "Downloads",
    Path.home() / "Desktop",
    Path("/Volumes/4TBSG/NEW_AUDIO"),  # Add your folders
]

OUTPUT_BASE = Path("AUTO_ORGANIZED")
MONITOR_LOG = Path("MONITORING_LOGS")

CONFIG = {
    'scan_interval': 10,  # Check every 10 seconds
    'min_file_age': 5,  # Wait 5 seconds before processing (ensure complete)
    'auto_organize': True,
    'apply_hard_rule': True,
    'notification_mode': 'console'  # 'console' or 'file'
}

# ============================================================================
# FILE TRACKING
# ============================================================================

class FileTracker:
    """Track processed files to avoid reprocessing"""
    
    def __init__(self):
        self.processed_files = set()
        self.cache_file = Path("monitor_cache.txt")
        self.load_cache()
    
    def load_cache(self):
        """Load previously processed files"""
        if self.cache_file.exists():
            with open(self.cache_file, 'r') as f:
                self.processed_files = set(line.strip() for line in f)
    
    def save_cache(self):
        """Save processed files"""
        with open(self.cache_file, 'w') as f:
            for filepath in self.processed_files:
                f.write(f"{filepath}\n")
    
    def is_processed(self, filepath):
        """Check if file was already processed"""
        return str(filepath) in self.processed_files
    
    def mark_processed(self, filepath):
        """Mark file as processed"""
        self.processed_files.add(str(filepath))
        self.save_cache()
    
    def get_file_hash(self, filepath):
        """Get unique hash for file"""
        stat = filepath.stat()
        return f"{filepath.name}_{stat.st_size}_{stat.st_mtime}"

# ============================================================================
# QUICK METADATA CHECK
# ============================================================================

def quick_metadata_check(filepath):
    """Quick check if file has metadata"""
    try:
        with open(filepath, 'rb') as f:
            if f.read(4) != b'RIFF':
                return None
            f.read(4)
            if f.read(4) != b'WAVE':
                return None
            
            # Check first 50KB
            data = f.read(50000)
            has_metadata = b'INFO' in data or b'bext' in data
            
            return {
                'path': filepath,
                'has_metadata': has_metadata,
                'size': filepath.stat().st_size,
                'detected_time': datetime.now()
            }
    except:
        return None

# ============================================================================
# AUTO ORGANIZER
# ============================================================================

def auto_organize_file(filepath, metadata):
    """Automatically organize a newly detected file"""
    
    # Apply HARD RULE
    if CONFIG['apply_hard_rule']:
        if not metadata['has_metadata']:
            dest_folder = OUTPUT_BASE / "ORIGINAL_COMPOSITIONS"
            category = "Original"
        else:
            dest_folder = OUTPUT_BASE / "COMMERCIAL_SAMPLES"
            category = "Commercial"
    else:
        dest_folder = OUTPUT_BASE / "AUTO_ORGANIZED"
        category = "Auto"
    
    dest_folder.mkdir(parents=True, exist_ok=True)
    
    # Copy file
    dest_file = dest_folder / filepath.name
    
    # Handle duplicates
    counter = 1
    original_dest = dest_file
    while dest_file.exists():
        dest_file = dest_folder / f"{original_dest.stem}_{counter}{original_dest.suffix}"
        counter += 1
    
    import shutil
    shutil.copy2(filepath, dest_file)
    
    return dest_file, category

# ============================================================================
# MONITORING ENGINE
# ============================================================================

def scan_folders_once(tracker):
    """Scan watch folders once"""
    new_files = []
    
    for watch_folder in WATCH_FOLDERS:
        if not watch_folder.exists():
            continue
        
        # Find WAV files
        wav_files = list(watch_folder.glob('*.wav')) + list(watch_folder.glob('*.WAV'))
        
        for wav_file in wav_files:
            # Check if already processed
            if tracker.is_processed(wav_file):
                continue
            
            # Check if file is old enough (complete)
            age = time.time() - wav_file.stat().st_mtime
            if age < CONFIG['min_file_age']:
                continue
            
            # New file detected!
            new_files.append(wav_file)
    
    return new_files

def process_new_files(new_files, tracker, log_file):
    """Process newly detected files"""
    if not new_files:
        return
    
    print(f"\n🔔 {len(new_files)} new WAV file(s) detected!")
    
    for filepath in new_files:
        print(f"  📄 {filepath.name}")
        
        # Check metadata
        metadata = quick_metadata_check(filepath)
        
        if not metadata:
            print(f"    ⚠️  Not a valid WAV file")
            continue
        
        # Log detection
        log_entry = f"[{datetime.now().isoformat()}] DETECTED: {filepath}\n"
        log_entry += f"  Size: {metadata['size']/(1024**2):.2f} MB\n"
        log_entry += f"  Has metadata: {metadata['has_metadata']}\n"
        
        # Auto organize if enabled
        if CONFIG['auto_organize']:
            try:
                dest_file, category = auto_organize_file(filepath, metadata)
                
                icon = "⭐" if category == "Original" else "📦"
                print(f"    {icon} Auto-organized as: {category}")
                print(f"    → {dest_file}")
                
                log_entry += f"  Organized: {dest_file}\n"
                log_entry += f"  Category: {category}\n"
            
            except Exception as e:
                print(f"    ❌ Error organizing: {e}")
                log_entry += f"  Error: {e}\n"
        
        log_entry += "\n"
        
        # Save log
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        # Mark as processed
        tracker.mark_processed(filepath)

def monitor_continuous():
    """Continuous monitoring mode"""
    print("="*80)
    print("👁️ REAL-TIME FILE MONITOR 👁️")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE AUTO-ENFORCEMENT ⭐⭐⭐")
    print("NO METADATA = AUTO-ORGANIZED AS ORIGINAL!")
    print("\nMonitoring folders:")
    
    active_folders = []
    for folder in WATCH_FOLDERS:
        if folder.exists():
            print(f"  ✓ {folder}")
            active_folders.append(folder)
        else:
            print(f"  ✗ {folder} (not found)")
    
    if not active_folders:
        print("\n❌ No active watch folders!")
        return
    
    print(f"\nConfiguration:")
    print(f"  • Scan interval: {CONFIG['scan_interval']} seconds")
    print(f"  • Auto-organize: {CONFIG['auto_organize']}")
    print(f"  • Output: {OUTPUT_BASE}/")
    
    print("\n" + "="*80)
    print("🟢 Monitoring active... Press Ctrl+C to stop")
    print("="*80 + "\n")
    
    # Initialize
    MONITOR_LOG.mkdir(exist_ok=True)
    log_file = MONITOR_LOG / f"monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    tracker = FileTracker()
    
    scan_count = 0
    total_processed = 0
    
    try:
        while True:
            scan_count += 1
            
            # Scan for new files
            new_files = scan_folders_once(tracker)
            
            if new_files:
                process_new_files(new_files, tracker, log_file)
                total_processed += len(new_files)
            else:
                # Periodic status
                if scan_count % 60 == 0:  # Every 10 minutes
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                          f"Monitoring... ({total_processed} files processed)")
            
            # Wait for next scan
            time.sleep(CONFIG['scan_interval'])
    
    except KeyboardInterrupt:
        print("\n\n" + "="*80)
        print("🛑 Monitoring stopped")
        print("="*80)
        print(f"\nTotal files processed: {total_processed}")
        print(f"Log file: {log_file}")
        print("="*80 + "\n")

def monitor_once():
    """Single scan mode"""
    print("="*80)
    print("👁️ FILE MONITOR - SINGLE SCAN")
    print("="*80 + "\n")
    
    MONITOR_LOG.mkdir(exist_ok=True)
    log_file = MONITOR_LOG / f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    tracker = FileTracker()
    
    print("Scanning watch folders...\n")
    new_files = scan_folders_once(tracker)
    
    if new_files:
        process_new_files(new_files, tracker, log_file)
        print(f"\n✓ Processed {len(new_files)} file(s)")
    else:
        print("✓ No new files found")
    
    print(f"\nLog: {log_file}")
    print("="*80 + "\n")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'once':
        monitor_once()
    else:
        print("\nStarting continuous monitoring...")
        print("This will run until you press Ctrl+C")
        print("\nPress Enter to start...")
        input()
        
        monitor_continuous()

