#!/usr/bin/env python3
"""
NOIZYGENIE FishNet Enhanced Audio Monitor
Intelligent audio file processing with Native Instruments integration
"""

import time, os, shutil, hashlib
import json
from pathlib import Path
from datetime import datetime
import sys
sys.path.append('/Users/rsp_ms')
from palatino_terminal import PalatinoTerminal

# Enhanced imports for audio processing
try:
    import mutagen
    import soundfile as sf
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    AUDIO_LIBS_AVAILABLE = True
except ImportError:
    AUDIO_LIBS_AVAILABLE = False
    print("⚠️  Audio libraries not available. Install with:")
    print("   pip install mutagen soundfile watchdog")

class NoizyFishNet:
    def __init__(self):
        self.pt = PalatinoTerminal()
        
        # Enhanced watch directories with Native Instruments focus
        self.WATCH_DIRS = [
            "/Users/rsp_ms/Mission_Control",
            "/Volumes/4TB Utility", 
            "/Volumes/NoizyWind",
            "/Volumes/6TB/Native Instruments",  # Added NI monitoring
            "/Users/rsp_ms/Desktop/KONTAKT_LAB",  # Monitor organized libraries
            "/Volumes/6TB/BFA Libraries"  # Monitor BFA Libraries
        ]
        
        # Enhanced vault structure
        self.VAULT = "/Users/rsp_ms/NoizyFish_VAULT"
        self.CLEAN = os.path.join(self.VAULT, "Originals_Clean")
        self.DUPES = os.path.join(self.VAULT, "Originals_Dupes") 
        self.ISSUES = os.path.join(self.VAULT, "Originals_Issues")
        self.NI_SAMPLES = os.path.join(self.VAULT, "NI_Samples")  # New NI category
        self.BFA_SAMPLES = os.path.join(self.VAULT, "BFA_Samples")  # New BFA category
        self.LOG_FILE = os.path.join(self.VAULT, "FishNet_Logs", "fishnet_log.txt")
        self.STATS_FILE = os.path.join(self.VAULT, "FishNet_Logs", "fishnet_stats.json")
        
        # Create all directories
        for d in (self.CLEAN, self.DUPES, self.ISSUES, self.NI_SAMPLES, 
                 self.BFA_SAMPLES, os.path.dirname(self.LOG_FILE)):
            os.makedirs(d, exist_ok=True)
        
        # Hash database for duplicate detection
        self.hashes = {}
        self.stats = {
            'processed': 0,
            'clean': 0,
            'duplicates': 0,
            'issues': 0,
            'ni_samples': 0,
            'bfa_samples': 0,
            'start_time': datetime.now().isoformat()
        }
        
        # Load existing stats if available
        self.load_stats()
        
    def load_stats(self):
        """Load existing statistics"""
        if os.path.exists(self.STATS_FILE):
            try:
                with open(self.STATS_FILE, 'r') as f:
                    saved_stats = json.load(f)
                    self.stats.update(saved_stats)
            except Exception as e:
                self.log_action(f"Error loading stats: {e}")
    
    def save_stats(self):
        """Save current statistics"""
        try:
            with open(self.STATS_FILE, 'w') as f:
                json.dump(self.stats, f, indent=2)
        except Exception as e:
            self.log_action(f"Error saving stats: {e}")
    
    def file_hash(self, path):
        """Generate SHA256 hash of file"""
        h = hashlib.sha256()
        try:
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    h.update(chunk)
            return h.hexdigest()
        except Exception as e:
            self.log_action(f"Hash error {path}: {e}")
            return None
    
    def has_metadata(self, path):
        """Check if audio file has metadata tags"""
        if not AUDIO_LIBS_AVAILABLE:
            return False
        try:
            audio = mutagen.File(path)
            return bool(audio and audio.tags)
        except:
            return False
    
    def check_quality(self, path):
        """Check audio quality (duration and sample rate)"""
        if not AUDIO_LIBS_AVAILABLE:
            return True  # Assume good quality if can't check
        try:
            info = sf.info(path)
            # Enhanced quality criteria
            duration_ok = info.duration >= 2  # At least 2 seconds
            samplerate_ok = info.samplerate >= 22050  # At least 22kHz
            channels_ok = info.channels <= 2  # Mono or stereo
            
            return duration_ok and samplerate_ok and channels_ok
        except:
            return False
    
    def detect_source_type(self, path):
        """Detect if file is from Native Instruments, BFA, or other source"""
        path_lower = str(path).lower()
        
        # Native Instruments detection
        ni_indicators = [
            'native instruments', 'kontakt', 'komplete', 'massive',
            'reaktor', 'absynth', 'battery', 'maschine', '.nki', '.nkm', '.ncw'
        ]
        
        # Big Fish Audio detection  
        bfa_indicators = [
            'big fish', 'bfa', 'bigfish', 'big fish audio'
        ]
        
        if any(indicator in path_lower for indicator in ni_indicators):
            return 'NI'
        elif any(indicator in path_lower for indicator in bfa_indicators):
            return 'BFA'
        else:
            return 'OTHER'
    
    def log_action(self, msg):
        """Log action with timestamp"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"[{timestamp}] {msg}"
        
        try:
            with open(self.LOG_FILE, "a") as log:
                log.write(log_msg + "\n")
            print(f"📝 {msg}")  # Also print to console
        except Exception as e:
            print(f"❌ Log error: {e}")
    
    def process_file(self, path):
        """Enhanced file processing with Native Instruments support"""
        # Check if it's an audio file
        audio_extensions = (".wav", ".aiff", ".mp3", ".flac", ".m4a", ".ncw", ".nks")
        if not path.lower().endswith(audio_extensions):
            return
        
        # Skip files that already have metadata (likely processed)
        if self.has_metadata(path):
            return
        
        self.stats['processed'] += 1
        
        try:
            # Generate file hash
            file_hash = self.file_hash(path)
            if not file_hash:
                return
            
            filename = os.path.basename(path)
            source_type = self.detect_source_type(path)
            
            # Check for duplicates
            if file_hash in self.hashes:
                dest = os.path.join(self.DUPES, filename)
                # Avoid overwriting existing files
                counter = 1
                while os.path.exists(dest):
                    name, ext = os.path.splitext(filename)
                    dest = os.path.join(self.DUPES, f"{name}_{counter:03d}{ext}")
                    counter += 1
                
                shutil.copy2(path, dest)
                self.stats['duplicates'] += 1
                self.log_action(f"DUPE → {source_type} → {filename}")
                
            else:
                # New file - add to hash database
                self.hashes[file_hash] = path
                
                # Determine destination based on source and quality
                if source_type == 'NI':
                    if self.check_quality(path):
                        dest_dir = self.NI_SAMPLES
                        category = "NI_CLEAN"
                        self.stats['ni_samples'] += 1
                    else:
                        dest_dir = self.ISSUES
                        category = "NI_ISSUE"
                        self.stats['issues'] += 1
                        
                elif source_type == 'BFA':
                    if self.check_quality(path):
                        dest_dir = self.BFA_SAMPLES
                        category = "BFA_CLEAN"
                        self.stats['bfa_samples'] += 1
                    else:
                        dest_dir = self.ISSUES
                        category = "BFA_ISSUE"
                        self.stats['issues'] += 1
                        
                else:
                    # Other sources
                    if self.check_quality(path):
                        dest_dir = self.CLEAN
                        category = "CLEAN"
                        self.stats['clean'] += 1
                    else:
                        dest_dir = self.ISSUES
                        category = "ISSUE"
                        self.stats['issues'] += 1
                
                # Copy file to destination
                dest = os.path.join(dest_dir, filename)
                counter = 1
                while os.path.exists(dest):
                    name, ext = os.path.splitext(filename)
                    dest = os.path.join(dest_dir, f"{name}_{counter:03d}{ext}")
                    counter += 1
                
                shutil.copy2(path, dest)
                self.log_action(f"{category} → {filename}")
        
        except Exception as e:
            self.log_action(f"ERROR processing {path}: {e}")
            self.stats['issues'] += 1
        
        # Save stats periodically
        if self.stats['processed'] % 10 == 0:
            self.save_stats()
    
    def print_stats(self):
        """Print current statistics"""
        self.pt.subheader("FishNet Processing Statistics")
        self.pt.info("Total Processed", f"{self.stats['processed']:,}")
        self.pt.info("Clean Files", f"{self.stats['clean']:,}")
        self.pt.info("NI Samples", f"{self.stats['ni_samples']:,}")
        self.pt.info("BFA Samples", f"{self.stats['bfa_samples']:,}")
        self.pt.info("Duplicates", f"{self.stats['duplicates']:,}")
        self.pt.info("Issues", f"{self.stats['issues']:,}")
        
        uptime = datetime.now() - datetime.fromisoformat(self.stats['start_time'])
        self.pt.info("Uptime", f"{uptime}")
    
    def scan_existing_files(self):
        """Scan existing files in watch directories"""
        self.pt.header("FishNet Initial Scan")
        
        total_files = 0
        for watch_dir in self.WATCH_DIRS:
            if os.path.exists(watch_dir):
                self.pt.info("Scanning", watch_dir)
                for root, dirs, files in os.walk(watch_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        self.process_file(file_path)
                        total_files += 1
                        
                        # Progress indicator
                        if total_files % 100 == 0:
                            print(f"      📊 Scanned {total_files:,} files...")
        
        self.save_stats()
        self.print_stats()

class FishNetHandler(FileSystemEventHandler):
    def __init__(self, fishnet):
        self.fishnet = fishnet
    
    def on_created(self, event):
        if not event.is_directory:
            self.fishnet.process_file(event.src_path)
    
    def on_moved(self, event):
        if not event.is_directory:
            self.fishnet.process_file(event.dest_path)

def main():
    """Main FishNet execution"""
    if not AUDIO_LIBS_AVAILABLE:
        print("❌ Required audio libraries not available")
        return
    
    fishnet = NoizyFishNet()
    
    fishnet.pt.header("NOIZYGENIE FishNet Enhanced Audio Monitor")
    fishnet.pt.info("Watch Directories", f"{len(fishnet.WATCH_DIRS)}")
    fishnet.pt.info("Vault Location", fishnet.VAULT)
    
    # Option to scan existing files first
    scan_choice = input("\n🔍 Scan existing files first? (y/n): ").lower().strip()
    if scan_choice == 'y':
        fishnet.scan_existing_files()
    
    # Start monitoring
    fishnet.pt.subheader("Starting Real-time Monitoring")
    for watch_dir in fishnet.WATCH_DIRS:
        if os.path.exists(watch_dir):
            fishnet.pt.info("Monitoring", watch_dir)
        else:
            fishnet.pt.warning(f"Directory not found: {watch_dir}")
    
    # Setup file system observer
    observer = Observer()
    handler = FishNetHandler(fishnet)
    
    for watch_dir in fishnet.WATCH_DIRS:
        if os.path.exists(watch_dir):
            observer.schedule(handler, watch_dir, recursive=True)
    
    observer.start()
    fishnet.log_action("FishNet monitoring started")
    
    try:
        print(f"\n🎣 FishNet is monitoring... Press Ctrl+C to stop")
        stats_counter = 0
        while True:
            time.sleep(30)  # Print stats every 30 seconds
            stats_counter += 1
            if stats_counter % 2 == 0:  # Every minute
                fishnet.print_stats()
    
    except KeyboardInterrupt:
        fishnet.pt.success("FishNet monitoring stopped")
        observer.stop()
        fishnet.save_stats()
        fishnet.log_action("FishNet monitoring stopped")
    
    observer.join()
    fishnet.pt.timestamp()

if __name__ == "__main__":
    main()