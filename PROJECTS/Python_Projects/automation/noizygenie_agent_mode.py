#!/usr/bin/env python3
"""
🚀 NOIZYGENIE AGENT MODE - ULTIMATE LIBRARY REBUILD VERIFIER
Mission: 100% Library Verification & 2026 Migration System
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import hashlib

# Configuration
ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
TARGET_2026 = Path.home() / "Desktop" / "KONTAKT_LAB_2026"
VERIFICATION_REPORT = ROOT / "REBUILD_VERIFICATION_REPORT.json"
MIGRATION_LOG = ROOT / "2026_MIGRATION_LOG.txt"

class NoizyGenieAgent:
    def __init__(self):
        self.verified_count = 0
        self.broken_count = 0
        self.migrated_count = 0
        self.verification_results = {}
        self.start_time = datetime.now()
    
    def log(self, message, level="INFO"):
        """Enhanced logging with timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = "🔍" if level == "VERIFY" else "✅" if level == "SUCCESS" else "❌" if level == "ERROR" else "ℹ️"
        print(f"[{timestamp}] {prefix} {message}")
        
        # Also log to file
        with open(MIGRATION_LOG, "a") as f:
            f.write(f"[{timestamp}] {level}: {message}\n")
    
    def verify_library_integrity(self, lib_path):
        """Deep verification of library integrity"""
        lib_path = Path(lib_path)
        verification = {
            "name": lib_path.name,
            "path": str(lib_path),
            "verified": False,
            "issues": [],
            "file_count": 0,
            "size_mb": 0,
            "has_nki": False,
            "has_samples": False,
            "rebuild_status": "UNKNOWN"
        }
        
        try:
            if not lib_path.exists():
                verification["issues"].append("Library path does not exist")
                return verification
            
            # Count files and check types
            all_files = list(lib_path.rglob("*"))
            verification["file_count"] = len([f for f in all_files if f.is_file()])
            
            # Calculate total size
            total_size = sum(f.stat().st_size for f in all_files if f.is_file())
            verification["size_mb"] = round(total_size / (1024 * 1024), 2)
            
            # Check for essential KONTAKT files
            nki_files = list(lib_path.rglob("*.nki"))
            nkm_files = list(lib_path.rglob("*.nkm"))
            sample_files = list(lib_path.rglob("*.wav")) + list(lib_path.rglob("*.aif")) + list(lib_path.rglob("*.ncw"))
            
            verification["has_nki"] = len(nki_files) > 0 or len(nkm_files) > 0
            verification["has_samples"] = len(sample_files) > 0
            
            # Determine rebuild status
            if verification["has_nki"] and verification["has_samples"]:
                verification["rebuild_status"] = "PERFECT"
                verification["verified"] = True
            elif verification["has_nki"]:
                verification["rebuild_status"] = "PARTIAL_SAMPLES_MISSING"
                verification["issues"].append("Missing sample files")
            elif verification["has_samples"]:
                verification["rebuild_status"] = "PARTIAL_INSTRUMENTS_MISSING"
                verification["issues"].append("Missing instrument files")
            else:
                verification["rebuild_status"] = "BROKEN"
                verification["issues"].append("No KONTAKT files found")
            
            # Check for common issues
            if verification["file_count"] == 0:
                verification["issues"].append("Empty library")
            elif verification["file_count"] < 5:
                verification["issues"].append("Suspiciously few files")
            
        except Exception as e:
            verification["issues"].append(f"Verification error: {str(e)}")
        
        return verification
    
    def scan_all_libraries(self):
        """Comprehensive scan of all libraries"""
        self.log("🔍 STARTING COMPREHENSIVE LIBRARY SCAN", "VERIFY")
        self.log("=" * 60)
        
        all_libraries = []
        
        # Scan organized categories
        for category_dir in ROOT.iterdir():
            if category_dir.is_dir() and category_dir.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_')):
                for lib_dir in category_dir.iterdir():
                    if lib_dir.is_dir():
                        all_libraries.append(lib_dir)
        
        # Scan unorganized libraries
        for item in ROOT.iterdir():
            if (item.is_dir() and 
                not item.name.startswith('.') and 
                not item.name.startswith('_') and
                not item.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_')) and
                item.name not in ['REPORTS', 'BACKUP', 'ORGANIZED_LIBRARIES', 'TEMP_PROCESSING', 'SAMPLE_ARCHIVES']):
                all_libraries.append(item)
        
        self.log(f"📚 Found {len(all_libraries)} total libraries to verify")
        
        # Verify each library
        results = {}
        perfect_count = 0
        partial_count = 0
        broken_count = 0
        
        for i, lib_path in enumerate(all_libraries):
            self.log(f"🔍 Verifying {i+1}/{len(all_libraries)}: {lib_path.name}", "VERIFY")
            
            verification = self.verify_library_integrity(lib_path)
            results[lib_path.name] = verification
            
            if verification["rebuild_status"] == "PERFECT":
                perfect_count += 1
                self.log(f"✅ PERFECT: {lib_path.name}", "SUCCESS")
            elif verification["rebuild_status"].startswith("PARTIAL"):
                partial_count += 1
                self.log(f"⚠️ PARTIAL: {lib_path.name} - {verification['rebuild_status']}")
            else:
                broken_count += 1
                self.log(f"❌ BROKEN: {lib_path.name} - {', '.join(verification['issues'])}", "ERROR")
        
        # Save verification results
        with open(VERIFICATION_REPORT, "w") as f:
            json.dump(results, f, indent=2, default=str)
        
        # Display summary
        total = len(all_libraries)
        self.log("=" * 60)
        self.log("📊 VERIFICATION SUMMARY:")
        self.log(f"   🎯 PERFECT REBUILDS: {perfect_count}/{total} ({perfect_count/total*100:.1f}%)")
        self.log(f"   ⚠️  PARTIAL REBUILDS: {partial_count}/{total} ({partial_count/total*100:.1f}%)")
        self.log(f"   ❌ BROKEN LIBRARIES: {broken_count}/{total} ({broken_count/total*100:.1f}%)")
        
        self.verification_results = results
        return results
    
    def prepare_2026_migration(self):
        """Prepare the 2026 migration structure"""
        self.log("🚀 PREPARING 2026 MIGRATION STRUCTURE")
        
        # Create 2026 directory structure
        TARGET_2026.mkdir(exist_ok=True)
        
        # Create organized category structure in 2026
        categories = [
            "01_ELECTRONIC", "02_ORCHESTRAL", "03_ACOUSTIC", "04_URBAN",
            "05_ROCK_POP", "06_WORLD_ETHNIC", "07_SYNTHESIZERS", 
            "08_DRUMS_PERCUSSION", "09_LOOPS_GROOVES", "10_SOUNDSCAPES_FX",
            "11_VOCALS", "12_CONSTRUCTION_KITS", "13_MULTIS_COMBIS"
        ]
        
        for category in categories:
            (TARGET_2026 / category).mkdir(exist_ok=True)
        
        # Create special folders
        (TARGET_2026 / "PERFECT_REBUILDS").mkdir(exist_ok=True)
        (TARGET_2026 / "PARTIAL_REBUILDS").mkdir(exist_ok=True)
        (TARGET_2026 / "NEEDS_REPAIR").mkdir(exist_ok=True)
        (TARGET_2026 / "MIGRATION_REPORTS").mkdir(exist_ok=True)
        
        self.log("✅ 2026 directory structure created")
    
    def migrate_perfect_libraries(self):
        """Migrate only perfectly rebuilt libraries to 2026"""
        self.log("🚀 STARTING MIGRATION OF PERFECT LIBRARIES")
        
        if not self.verification_results:
            self.log("❌ No verification results found. Run scan first.", "ERROR")
            return
        
        perfect_libs = {name: data for name, data in self.verification_results.items() 
                       if data["rebuild_status"] == "PERFECT"}
        
        self.log(f"📦 Migrating {len(perfect_libs)} perfect libraries")
        
        migrated = 0
        for lib_name, lib_data in perfect_libs.items():
            try:
                source_path = Path(lib_data["path"])
                
                # Determine target category (if organized) or use PERFECT_REBUILDS
                if any(cat in str(source_path.parent) for cat in ["01_", "02_", "03_", "04_", "05_", "06_", "07_", "08_", "09_", "10_", "11_", "12_", "13_"]):
                    category = source_path.parent.name
                    target_path = TARGET_2026 / category / lib_name
                else:
                    target_path = TARGET_2026 / "PERFECT_REBUILDS" / lib_name
                
                # Copy library
                if source_path.exists():
                    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                    migrated += 1
                    self.log(f"✅ Migrated: {lib_name} → {target_path.parent.name}")
                
            except Exception as e:
                self.log(f"❌ Failed to migrate {lib_name}: {e}", "ERROR")
        
        self.log(f"🎉 MIGRATION COMPLETE: {migrated} libraries moved to 2026")
        self.migrated_count = migrated
    
    def generate_final_report(self):
        """Generate comprehensive final report"""
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        report = f"""
🚀 NOIZYGENIE AGENT MODE - FINAL MISSION REPORT
{'='*60}
Mission Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}
Mission Completed: {end_time.strftime('%Y-%m-%d %H:%M:%S')}
Total Duration: {duration}

📊 VERIFICATION RESULTS:
"""
        
        if self.verification_results:
            perfect = sum(1 for r in self.verification_results.values() if r["rebuild_status"] == "PERFECT")
            partial = sum(1 for r in self.verification_results.values() if r["rebuild_status"].startswith("PARTIAL"))
            broken = sum(1 for r in self.verification_results.values() if r["rebuild_status"] == "BROKEN")
            total = len(self.verification_results)
            
            report += f"""
   🎯 Perfect Rebuilds: {perfect}/{total} ({perfect/total*100:.1f}%)
   ⚠️  Partial Rebuilds: {partial}/{total} ({partial/total*100:.1f}%)
   ❌ Broken Libraries: {broken}/{total} ({broken/total*100:.1f}%)

🚀 MIGRATION STATUS:
   📦 Libraries Migrated to 2026: {self.migrated_count}
   📁 2026 Structure: CREATED
   
🎉 MISSION STATUS: {'SUCCESS - 100% REBUILD ACHIEVED!' if perfect == total else f'PARTIAL SUCCESS - {perfect/total*100:.1f}% PERFECT'}
"""
        
        report_file = TARGET_2026 / "MIGRATION_REPORTS" / f"FINAL_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, "w") as f:
            f.write(report)
        
        print(report)
        self.log(f"📋 Final report saved: {report_file}")

def main():
    """Main execution function"""
    print("🚀 NOIZYGENIE AGENT MODE ACTIVATED!")
    print("Mission: 100% Library Rebuild Verification & 2026 Migration")
    print("=" * 60)
    
    agent = NoizyGenieAgent()
    
    # Initialize migration log
    with open(MIGRATION_LOG, "w") as f:
        f.write(f"NOIZYGENIE AGENT MODE - MISSION LOG\n")
        f.write(f"Started: {datetime.now()}\n")
        f.write("=" * 50 + "\n")
    
    try:
        # Step 1: Comprehensive verification
        agent.scan_all_libraries()
        
        # Step 2: Prepare 2026 structure
        agent.prepare_2026_migration()
        
        # Step 3: Migrate perfect libraries
        agent.migrate_perfect_libraries()
        
        # Step 4: Generate final report
        agent.generate_final_report()
        
        print("\n🎉 NOIZYGENIE AGENT MODE MISSION COMPLETE!")
        
    except Exception as e:
        agent.log(f"💥 MISSION FAILED: {e}", "ERROR")
        print(f"💥 MISSION FAILED: {e}")

if __name__ == "__main__":
    main()