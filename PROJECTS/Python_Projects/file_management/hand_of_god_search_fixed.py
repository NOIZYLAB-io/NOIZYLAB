#!/usr/bin/env python3
"""
🙏 NOIZYGENIE "HAND OF GOD" SEARCH PROTOCOL
Divine Intervention Sample Recovery System
Mission: Find ALL missing parts across ALL volumes with omniscient search
"""

import os
import re
import json
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Configuration - Divine Search Paths
ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
SEARCH_VOLUMES = [
    Path.home() / "Desktop",
    Path.home() / "Documents", 
    Path.home() / "Downloads",
    Path.home() / "Music",
    Path("/Volumes"),  # External drives
    Path("/Users/Shared"),
    Path.home() / "Library" / "Audio",
    Path.home() / "NoizyGenie_Master_Workspace"
]

# Add any custom paths you know might contain samples
DIVINE_SEARCH_PATHS = [
    "/Applications/Native Instruments",
    "/Library/Audio",
    "/System/Library/Audio",
    Path.home() / "Desktop" / "SAMPLE_ARCHIVES",
    Path.home() / "Desktop" / "BACKUP",
    Path.home() / "Desktop" / "ORGANIZED_LIBRARIES"
]

# FishNet integration - VAULT setup
VAULT = Path.home() / "NoizyFish_VAULT"
SUMMARY_DIR = VAULT / "FishNet_Logs" / "summaries"
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
COUNT_FILE = VAULT / "FishNet_Logs" / "count.txt"

def update_summary(result, path, dest):
    """Update FishNet summary tracking"""
    today = datetime.now().strftime("%Y-%m-%d")
    summary_path = SUMMARY_DIR / f"fishnet_summary_{today}.txt"
    with open(summary_path, "a") as f:
        f.write(f"[{datetime.now()}] {result} → {path} → {dest}\n")

    # Update running count
    count = 0
    if COUNT_FILE.exists():
        with open(COUNT_FILE) as f:
            count = int(f.read().strip() or 0)
    count += 1
    with open(COUNT_FILE, "w") as f:
        f.write(str(count))

class HandOfGodSearcher:
    def __init__(self):
        self.missing_samples = {}
        self.found_samples = {}
        self.search_results = {}
        self.divine_cache = {}
        self.start_time = datetime.now()
        self.recovery_vault = VAULT / "Divine_Recovery"
        self.recovery_vault.mkdir(parents=True, exist_ok=True)
        
    def divine_log(self, message, level="DIVINE"):
        """Sacred logging with divine timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        icons = {
            "DIVINE": "🙏",
            "SEARCH": "🔍", 
            "FOUND": "✨",
            "MISSING": "💫",
            "MIRACLE": "⚡",
            "ERROR": "💥",
            "CLEAN": "🧼",
            "DUPE": "🔄",
            "ISSUE": "⚠️"
        }
        icon = icons.get(level, "📿")
        print(f"[{timestamp}] {icon} {message}")
    
    def analyze_broken_library(self, lib_path):
        """Divine analysis of broken library structure"""
        lib_path = Path(lib_path)
        self.divine_log(f"Analyzing broken library: {lib_path.name}", "SEARCH")
        
        analysis = {
            "name": lib_path.name,
            "path": str(lib_path),
            "instruments": [],
            "missing_samples": [],
            "existing_samples": [],
            "sample_directories": [],
            "potential_matches": []
        }
        
        try:
            # Find all instrument files
            for ext in [".nki", ".nkm", ".nkc"]:
                instruments = list(lib_path.rglob(f"*{ext}"))
                analysis["instruments"].extend([str(f) for f in instruments])
            
            # Find existing samples
            for ext in [".wav", ".aif", ".aiff", ".ncw"]:
                samples = list(lib_path.rglob(f"*{ext}"))
                analysis["existing_samples"].extend([str(f) for f in samples])
            
            # Find sample directories (even empty ones)
            for item in lib_path.rglob("*"):
                if item.is_dir() and any(keyword in item.name.lower() for keyword in 
                    ["sample", "audio", "wav", "sound", "loop", "one shot", "multisampl"]):
                    analysis["sample_directories"].append(str(item))
            
            # Analyze instrument files for sample references
            for instrument_file in analysis["instruments"]:
                missing = self.extract_sample_references(instrument_file)
                analysis["missing_samples"].extend(missing)
        
        except Exception as e:
            self.divine_log(f"Error analyzing {lib_path.name}: {e}", "ERROR")
        
        return analysis
    
    def extract_sample_references(self, instrument_path):
        """Extract sample file references from instrument files"""
        missing_samples = []
        
        try:
            # Read instrument file and look for sample references
            with open(instrument_path, 'rb') as f:
                content = f.read()
            
            # Convert to string for easier pattern matching
            try:
                text_content = content.decode('utf-8', errors='ignore')
            except:
                text_content = str(content)
            
            # Find potential sample file names
            sample_patterns = [
                r'([A-Za-z0-9_\-\s]+\.wav)',
                r'([A-Za-z0-9_\-\s]+\.aif)',
                r'([A-Za-z0-9_\-\s]+\.ncw)',
                r'Samples/([A-Za-z0-9_\-\s/]+)',
                r'Audio/([A-Za-z0-9_\-\s/]+)'
            ]
            
            for pattern in sample_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    if isinstance(match, str) and len(match) > 3:
                        missing_samples.append(match.strip())
        
        except Exception as e:
            self.divine_log(f"Error reading instrument {instrument_path}: {e}", "ERROR")
        
        return list(set(missing_samples))  # Remove duplicates
    
    def divine_search_volume(self, volume_path, target_samples):
        """Divine search across entire volume for missing samples"""
        volume_path = Path(volume_path)
        if not volume_path.exists():
            return {}
        
        self.divine_log(f"Divine search in volume: {volume_path}", "SEARCH")
        found_samples = {}
        
        try:
            # Get all audio files in volume
            audio_extensions = [".wav", ".aif", ".aiff", ".ncw", ".rex", ".rx2"]
            
            for ext in audio_extensions:
                for audio_file in volume_path.rglob(f"*{ext}"):
                    file_name = audio_file.name.lower()
                    
                    # Check if this matches any missing sample
                    for missing_sample in target_samples:
                        missing_lower = missing_sample.lower()
                        
                        # Various matching strategies
                        if (file_name == missing_lower or
                            missing_lower in file_name or
                            file_name in missing_lower or
                            self.fuzzy_match(file_name, missing_lower)):
                            
                            if missing_sample not in found_samples:
                                found_samples[missing_sample] = []
                            found_samples[missing_sample].append(str(audio_file))
                            self.divine_log(f"MIRACLE FOUND: {missing_sample} → {audio_file}", "FOUND")
        
        except Exception as e:
            self.divine_log(f"Error searching volume {volume_path}: {e}", "ERROR")
        
        return found_samples
    
    def process_found_sample(self, sample_name, sample_path, library_name):
        """Process found sample and categorize it using FishNet logic"""
        sample_path = Path(sample_path)
        
        # Determine quality and categorization
        try:
            file_size = sample_path.stat().st_size
            
            # Basic quality checks
            if file_size > 100000:  # > 100KB
                category = "CLEAN"
                dest_dir = self.recovery_vault / "Clean_Samples" / library_name
            elif file_size > 10000:  # 10KB - 100KB
                category = "ISSUE"
                dest_dir = self.recovery_vault / "Issue_Samples" / library_name
            else:
                category = "ISSUE"
                dest_dir = self.recovery_vault / "Issue_Samples" / library_name
            
            # Create destination directory
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy sample to recovery vault
            dest_path = dest_dir / sample_path.name
            if not dest_path.exists():
                shutil.copy2(sample_path, dest_path)
                self.divine_log(f"Recovered sample: {sample_name} → {dest_path}", category)
                
                # Update FishNet summary
                update_summary(category, str(sample_path), str(dest_path))
                
                return True
            else:
                # File already exists - check if it's a duplicate
                category = "DUPE"
                dupe_dir = self.recovery_vault / "Duplicate_Samples" / library_name
                dupe_dir.mkdir(parents=True, exist_ok=True)
                
                # Create unique name for duplicate
                counter = 1
                while True:
                    name, ext = sample_path.stem, sample_path.suffix
                    dupe_path = dupe_dir / f"{name}_{counter}{ext}"
                    if not dupe_path.exists():
                        shutil.copy2(sample_path, dupe_path)
                        self.divine_log(f"Duplicate sample: {sample_name} → {dupe_path}", category)
                        
                        # Update FishNet summary
                        update_summary(category, str(sample_path), str(dupe_path))
                        return True
                    counter += 1
                    if counter > 100:  # Safety limit
                        break
                        
        except Exception as e:
            self.divine_log(f"Error processing sample {sample_name}: {e}", "ERROR")
            return False
        
        return False
    
    def fuzzy_match(self, file1, file2, threshold=0.7):
        """Fuzzy matching for sample names"""
        # Simple fuzzy matching based on common substrings
        file1_clean = re.sub(r'[^a-z0-9]', '', file1.lower())
        file2_clean = re.sub(r'[^a-z0-9]', '', file2.lower())
        
        if len(file1_clean) == 0 or len(file2_clean) == 0:
            return False
        
        # Check for substantial overlap
        shorter = min(len(file1_clean), len(file2_clean))
        longer = max(len(file1_clean), len(file2_clean))
        
        if shorter / longer < 0.5:
            return False
        
        # Count matching characters
        matches = sum(1 for a, b in zip(file1_clean, file2_clean) if a == b)
        return matches / longer >= threshold
    
    def search_library_backups(self, lib_name):
        """Search for backup versions of library"""
        self.divine_log(f"Searching for backups of: {lib_name}", "SEARCH")
        backup_locations = []
        
        search_paths = SEARCH_VOLUMES + [Path(p) for p in DIVINE_SEARCH_PATHS]
        
        for search_path in search_paths:
            if not search_path.exists():
                continue
                
            try:
                # Look for directories with similar names
                for item in search_path.rglob("*"):
                    if item.is_dir():
                        item_name = item.name.lower()
                        lib_name_lower = lib_name.lower()
                        
                        if (lib_name_lower in item_name or 
                            item_name in lib_name_lower or
                            self.fuzzy_match(item_name, lib_name_lower, 0.8)):
                            backup_locations.append(str(item))
                            self.divine_log(f"Potential backup found: {item}", "FOUND")
            except Exception as e:
                continue
        
        return backup_locations
    
    def hand_of_god_master_search(self):
        """The ultimate Hand of God search protocol"""
        self.divine_log("🙏 INITIATING HAND OF GOD SEARCH PROTOCOL", "DIVINE")
        self.divine_log("=" * 60, "DIVINE")
        
        # Get all libraries from verification report
        verification_file = ROOT / "REBUILD_VERIFICATION_REPORT.json"
        if not verification_file.exists():
            self.divine_log("No verification report found. Running emergency search...", "SEARCH")
            return self.emergency_search()
        
        with open(verification_file, 'r') as f:
            verification_data = json.load(f)
        
        # Focus on broken and partial libraries
        problematic_libs = {
            name: data for name, data in verification_data.items()
            if data.get("rebuild_status") in ["BROKEN", "PARTIAL_SAMPLES_MISSING", "PARTIAL_INSTRUMENTS_MISSING"]
        }
        
        self.divine_log(f"Found {len(problematic_libs)} libraries needing divine intervention", "SEARCH")
        
        all_missing_samples = []
        search_results = {}
        
        # Analyze each problematic library
        for lib_name, lib_data in problematic_libs.items():
            self.divine_log(f"Divine analysis of: {lib_name}", "SEARCH")
            
            lib_path = Path(lib_data["path"])
            analysis = self.analyze_broken_library(lib_path)
            
            # Collect all missing samples
            all_missing_samples.extend(analysis["missing_samples"])
            
            # Search for backups
            backups = self.search_library_backups(lib_name)
            analysis["backup_locations"] = backups
            
            search_results[lib_name] = analysis
        
        # Remove duplicates from missing samples
        unique_missing = list(set(all_missing_samples))
        self.divine_log(f"Total unique missing samples: {len(unique_missing)}", "SEARCH")
        
        # Perform divine search across all volumes
        self.divine_log("Commencing divine search across all volumes...", "DIVINE")
        found_samples = {}
        recovery_count = 0
        
        for volume in SEARCH_VOLUMES + [Path(p) for p in DIVINE_SEARCH_PATHS]:
            if volume.exists():
                volume_results = self.divine_search_volume(volume, unique_missing)
                for sample, locations in volume_results.items():
                    if sample not in found_samples:
                        found_samples[sample] = []
                    found_samples[sample].extend(locations)
                    
                    # Process each found sample
                    for location in locations:
                        # Determine which library this sample belongs to
                        for lib_name, analysis in search_results.items():
                            if sample in analysis.get("missing_samples", []):
                                if self.process_found_sample(sample, location, lib_name):
                                    recovery_count += 1
                                break
        
        self.divine_log(f"Total samples recovered: {recovery_count}", "MIRACLE")
        
        # Generate divine report
        self.generate_divine_report(search_results, found_samples, recovery_count)
        
        return search_results, found_samples
    
    def emergency_search(self):
        """Emergency search when no verification data exists"""
        self.divine_log("EMERGENCY DIVINE SEARCH MODE", "DIVINE")
        
        # Find all libraries and analyze them
        if not ROOT.exists():
            self.divine_log(f"KONTAKT_LAB not found at {ROOT}", "ERROR")
            return {}, {}
            
        all_libs = []
        for item in ROOT.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                all_libs.append(item)
        
        search_results = {}
        all_missing = []
        
        for lib_path in all_libs:
            analysis = self.analyze_broken_library(lib_path)
            all_missing.extend(analysis["missing_samples"])
            search_results[lib_path.name] = analysis
        
        # Divine search
        unique_missing = list(set(all_missing))
        found_samples = {}
        recovery_count = 0
        
        for volume in SEARCH_VOLUMES:
            if volume.exists():
                volume_results = self.divine_search_volume(volume, unique_missing)
                for sample, locations in volume_results.items():
                    if sample not in found_samples:
                        found_samples[sample] = []
                    found_samples[sample].extend(locations)
                    
                    # Process each found sample
                    for location in locations:
                        # Determine which library this sample belongs to
                        for lib_name, analysis in search_results.items():
                            if sample in analysis.get("missing_samples", []):
                                if self.process_found_sample(sample, location, lib_name):
                                    recovery_count += 1
                                break
        
        self.generate_divine_report(search_results, found_samples, recovery_count)
        return search_results, found_samples
    
    def generate_divine_report(self, search_results, found_samples, recovery_count=0):
        """Generate the sacred Hand of God report"""
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        total_missing = len(set().union(*[r.get('missing_samples', []) for r in search_results.values()]))
        
        report = f"""
🙏 HAND OF GOD SEARCH PROTOCOL - DIVINE REPORT
{'='*60}
Search Initiated: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}
Divine Intervention Complete: {end_time.strftime('%Y-%m-%d %H:%M:%S')}
Total Duration: {duration}

📊 DIVINE SEARCH RESULTS:
{'='*30}
Libraries Analyzed: {len(search_results)}
Unique Missing Samples: {total_missing}
Samples Found by Divine Intervention: {len(found_samples)}
Samples Successfully Recovered: {recovery_count}
Recovery Success Rate: {len(found_samples) / max(1, total_missing) * 100:.1f}%

🗂️ FISHNET INTEGRATION:
{'='*20}
Recovery Vault: {self.recovery_vault}
Clean Samples: {len(list((self.recovery_vault / "Clean_Samples").rglob("*"))) if (self.recovery_vault / "Clean_Samples").exists() else 0}
Duplicate Samples: {len(list((self.recovery_vault / "Duplicate_Samples").rglob("*"))) if (self.recovery_vault / "Duplicate_Samples").exists() else 0}
Issue Samples: {len(list((self.recovery_vault / "Issue_Samples").rglob("*"))) if (self.recovery_vault / "Issue_Samples").exists() else 0}

✨ MIRACULOUS DISCOVERIES:
{'='*25}
"""
        
        for sample, locations in found_samples.items():
            report += f"\n🎵 {sample}:\n"
            for location in locations[:3]:  # Show first 3 locations
                report += f"   📍 {location}\n"
            if len(locations) > 3:
                report += f"   ... and {len(locations) - 3} more locations\n"
        
        report += f"""

🏥 LIBRARIES NEEDING DIVINE HEALING:
{'='*35}
"""
        
        for lib_name, analysis in search_results.items():
            if analysis.get("missing_samples"):
                missing_count = len(analysis["missing_samples"])
                found_count = sum(1 for sample in analysis["missing_samples"] if sample in found_samples)
                recovery_rate = found_count / missing_count * 100 if missing_count > 0 else 0
                
                report += f"\n📚 {lib_name}:\n"
                report += f"   Missing: {missing_count} samples\n"
                report += f"   Found: {found_count} samples\n" 
                report += f"   Recovery Rate: {recovery_rate:.1f}%\n"
                
                if analysis.get("backup_locations"):
                    report += f"   🔍 Backup Locations Found:\n"
                    for backup in analysis["backup_locations"][:2]:
                        report += f"      📁 {backup}\n"
        
        report += f"\n🙏 MAY THE DIVINE FORCE BE WITH YOUR SAMPLES! 🙏"
        
        # Save report
        report_file = ROOT / f"HAND_OF_GOD_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(report)
        self.divine_log(f"Divine report saved: {report_file}", "DIVINE")

def main():
    """Main divine execution"""
    print("🙏 HAND OF GOD SEARCH PROTOCOL ACTIVATED")
    print("Divine Intervention for Sample Recovery")
    print("=" * 50)
    
    searcher = HandOfGodSearcher()
    search_results, found_samples = searcher.hand_of_god_master_search()
    
    print("\n🙏 DIVINE INTERVENTION COMPLETE!")
    print("May your samples be forever found! ✨")

if __name__ == "__main__":
    main()