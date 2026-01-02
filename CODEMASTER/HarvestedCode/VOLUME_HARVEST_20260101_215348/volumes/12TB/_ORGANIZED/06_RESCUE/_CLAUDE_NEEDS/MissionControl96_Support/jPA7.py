#!/usr/bin/env python3
"""
🐟 NOIZYGENIE FISHNET MONITOR
Real-time audio file processing and organization system
Watches multiple directories and automatically sorts audio files
"""

import time, os, shutil, hashlib
import mutagen, soundfile as sf
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Configuration - Watch Directories
WATCH_DIRS = ["/Users/rsp_ms/Mission_Control",
              "/Volumes/4TB Utility",
              "/Volumes/NoizyWind"]

# VAULT Structure
VAULT = "/Users/rsp_ms/NoizyFish_VAULT"
CLEAN, DUPES, ISSUES = [os.path.join(VAULT, sub) 
                        for sub in ("Originals_Clean", "Originals_Dupes", "Originals_Issues")]
LOG_FILE = os.path.join(VAULT, "FishNet_Logs", "fishnet_log.txt")

# Create directory structure
for d in (CLEAN, DUPES, ISSUES, os.path.dirname(LOG_FILE)):
    os.makedirs(d, exist_ok=True)

# Global hash registry for duplicate detection
hashes = {}

def file_hash(path):
    """Generate SHA256 hash for file content"""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def has_metadata(path):
    """Check if audio file has metadata tags"""
    try:
        audio = mutagen.File(path)
        return bool(audio and audio.tags)
    except:
        return False

def check_quality(path):
    """Check audio file quality (duration >= 2s, sample rate >= 22050Hz)"""
    try:
        info = sf.info(path)
        return info.duration >= 2 and info.samplerate >= 22050
    except:
        return False

def log_action(msg):
    """Log actions to FishNet log file"""
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {msg}\n")
    print(f"🐟 FishNet: {msg}")

def process_file(path):
    """Process and categorize audio file"""
    # Only process audio files
    if not path.lower().endswith((".wav",".aiff",".mp3",".flac",".m4a")):
        return
    
    # Skip files that already have metadata (likely organized)
    if has_metadata(path):
        return
    
    try:
        # Generate hash for duplicate detection
        h = file_hash(path)
        filename = os.path.basename(path)
        
        if h in hashes:
            # Duplicate found
            dest = os.path.join(DUPES, filename)
            # Handle filename conflicts
            counter = 1
            while os.path.exists(dest):
                name, ext = os.path.splitext(filename)
                dest = os.path.join(DUPES, f"{name}_{counter}{ext}")
                counter += 1
            
            shutil.copy2(path, dest)
            log_action(f"DUPE → {path} → {dest}")
        else:
            # New file - register hash
            hashes[h] = path
            
            if check_quality(path):
                # High quality file
                dest = os.path.join(CLEAN, filename)
                # Handle filename conflicts
                counter = 1
                while os.path.exists(dest):
                    name, ext = os.path.splitext(filename)
                    dest = os.path.join(CLEAN, f"{name}_{counter}{ext}")
                    counter += 1
                
                shutil.copy2(path, dest)
                log_action(f"CLEAN → {path} → {dest}")
            else:
                # Quality issues
                dest = os.path.join(ISSUES, filename)
                # Handle filename conflicts
                counter = 1
                while os.path.exists(dest):
                    name, ext = os.path.splitext(filename)
                    dest = os.path.join(ISSUES, f"{name}_{counter}{ext}")
                    counter += 1
                
                shutil.copy2(path, dest)
                log_action(f"ISSUE → {path} → {dest}")
                
    except Exception as e:
        log_action(f"ERROR {path}: {e}")

class FishNetHandler(FileSystemEventHandler):
    """File system event handler for FishNet monitoring"""
    
    def on_created(self, event):
        """Handle new file creation"""
        if not event.is_directory:
            log_action(f"NEW FILE DETECTED: {event.src_path}")
            process_file(event.src_path)
    
    def on_moved(self, event):
        """Handle file moves (might be new files)"""
        if not event.is_directory:
            log_action(f"FILE MOVED: {event.dest_path}")
            process_file(event.dest_path)

def initialize_fishnet():
    """Initialize FishNet system"""
    print("🐟 INITIALIZING NOIZYGENIE FISHNET MONITOR")
    print("=" * 50)
    
    # Check watch directories
    active_dirs = []
    for watch_dir in WATCH_DIRS:
        if os.path.exists(watch_dir):
            active_dirs.append(watch_dir)
            print(f"✅ Monitoring: {watch_dir}")
        else:
            print(f"⚠️  Directory not found: {watch_dir}")
    
    if not active_dirs:
        print("❌ No valid watch directories found!")
        return None
    
    print(f"\n🗂️  VAULT Structure:")
    print(f"   📁 Clean Files: {CLEAN}")
    print(f"   📁 Duplicates: {DUPES}")
    print(f"   📁 Issues: {ISSUES}")
    print(f"   📄 Log File: {LOG_FILE}")
    
    # Pre-scan existing files in watch directories
    print(f"\n🔍 Pre-scanning existing files...")
    total_processed = 0
    
    for watch_dir in active_dirs:
        print(f"Scanning: {watch_dir}")
        for root, dirs, files in os.walk(watch_dir):
            for file in files:
                if file.lower().endswith((".wav",".aiff",".mp3",".flac",".m4a")):
                    file_path = os.path.join(root, file)
                    process_file(file_path)
                    total_processed += 1
                    if total_processed % 10 == 0:
                        print(f"  Processed {total_processed} files...")
    
    print(f"✅ Pre-scan complete: {total_processed} files processed")
    log_action(f"FISHNET INITIALIZED - Pre-scanned {total_processed} files")
    
    return active_dirs

if __name__ == "__main__":
    try:
        # Initialize system
        active_dirs = initialize_fishnet()
        if not active_dirs:
            exit(1)
        
        # Start monitoring
        print(f"\n🐟 FISHNET MONITOR ACTIVE")
        print("Watching for new audio files...")
        print("Press Ctrl+C to stop\n")
        
        observer = Observer()
        handler = FishNetHandler()
        
        for watch_dir in active_dirs:
            observer.schedule(handler, watch_dir, recursive=True)
            log_action(f"MONITORING STARTED: {watch_dir}")
        
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Stopping FishNet Monitor...")
            log_action("FISHNET MONITOR STOPPED BY USER")
            observer.stop()
        
        observer.join()
        print("✅ FishNet Monitor stopped successfully")
        
    except Exception as e:
        print(f"❌ FishNet Error: {e}")
        log_action(f"CRITICAL ERROR: {e}")