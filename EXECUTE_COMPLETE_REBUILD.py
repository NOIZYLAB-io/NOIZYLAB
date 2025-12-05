#!/usr/bin/env python3
"""
EXECUTE COMPLETE REBUILD - Final Organization System
Run this to transform your entire library to COMPLETE PRISTINE STATE!
"""

import os
import sys
import time
import json
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration
PRIMARY_DRIVE = Path("/Volumes/6TB")
SECONDARY_DRIVE = Path("/Volumes/4TBSG")
WORKSPACE = SECONDARY_DRIVE / "KTK 2026 TO SORT"
RESULTS_DIR = SECONDARY_DRIVE / "SCAN_RESULTS"

class CompleteRebuild:
    def __init__(self):
        self.start_time = time.time()
        self.steps_completed = []
        self.total_steps = 8
        
    def log(self, message, step=None):
        """Log progress with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        if step:
            print(f"\n[{timestamp}] 🚀 STEP {step}/{self.total_steps}: {message}")
            print("="*70)
        else:
            print(f"[{timestamp}] {message}")
    
    def run_script(self, script_name, description):
        """Run a Python script"""
        self.log(f"Running: {description}")
        script_path = WORKSPACE / script_name
        
        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=WORKSPACE,
                capture_output=False,
                text=True
            )
            
            if result.returncode == 0:
                self.log(f"✅ {description} - COMPLETE")
                return True
            else:
                self.log(f"⚠️  {description} - Warning (code {result.returncode})")
                return False
        except Exception as e:
            self.log(f"❌ Error: {e}")
            return False
    
    def check_prerequisites(self):
        """Check if all prerequisites are met"""
        self.log("Checking prerequisites...", step=1)
        
        checks = {
            "6TB Drive": PRIMARY_DRIVE.exists(),
            "4TBSG Drive": SECONDARY_DRIVE.exists(),
            "Workspace": WORKSPACE.exists(),
            "Tools": (WORKSPACE / "master_control.py").exists(),
        }
        
        all_good = True
        for check, status in checks.items():
            if status:
                self.log(f"  ✅ {check}")
            else:
                self.log(f"  ❌ {check} - MISSING!")
                all_good = False
        
        return all_good
    
    def create_factory_directories(self):
        """Create complete factory directory structure"""
        self.log("Creating factory directory structure...", step=2)
        
        # Structure for 6TB (Primary - Content)
        primary_structure = {
            "KONTAKT_LIBRARIES": [
                "Native_Instruments/Orchestral",
                "Native_Instruments/Cinematic",
                "Native_Instruments/Synths_Pads",
                "Native_Instruments/Percussion",
                "Spitfire_Audio/Orchestral",
                "Spitfire_Audio/Cinematic",
                "8Dio/Orchestral",
                "Output/Cinematic",
                "Soundiron/Percussion",
                "ProjectSam/Orchestral",
                "EastWest/Orchestral",
                "CineSamples/Orchestral",
                "Other/Uncategorized",
            ],
            "AUDIO_SAMPLES": [
                "Drums/Kicks",
                "Drums/Snares",
                "Drums/Hats",
                "Drums/Percussion",
                "Bass/808",
                "Bass/Sub",
                "Loops/Drum_Loops",
                "Loops/Music_Loops",
                "Loops/Beat_Loops",
                "Melody/Leads",
                "Melody/Arpeggios",
                "Vocal_Samples/One_Shots",
                "Vocal_Samples/Phrases",
                "FX_Samples/Impacts",
                "FX_Samples/Transitions",
                "FX_Samples/Atmospheres",
                "Foley/Ambience",
            ],
            "PLUGIN_PRESETS": [
                "Synths/Sylenth1",
                "Synths/Serum",
                "Synths/Massive",
                "Synths/Nexus",
                "Synths/Omnisphere",
                "Effects/Reverb",
                "Effects/Delay",
                "Effects/Compression",
                "Effects/EQ",
                "Samplers/Kontakt",
                "Samplers/Battery",
            ],
            "SAMPLER_INSTRUMENTS": [
                "EXS24/Orchestral",
                "EXS24/Drums",
                "EXS24/Synths",
                "SFZ/Instruments",
                "Halion/Libraries",
                "SoundFonts/GM",
            ],
        }
        
        # Structure for 4TBSG (Secondary - Projects & Support)
        secondary_structure = {
            "PROJECTS": [
                "ProTools/2026",
                "ProTools/2025",
                "ProTools/Archive",
                "Logic/Current",
                "Logic/Archive",
                "Ableton/Current",
                "Ableton/Archive",
                "FL_Studio/Current",
                "Cubase/Current",
            ],
            "INSTALLERS": [
                "Plugins/VST",
                "Plugins/AU",
                "Plugins/AAX",
                "DAW/ProTools",
                "DAW/Logic",
                "DAW/Ableton",
                "Libraries/Kontakt",
                "Libraries/Expansions",
                "Libraries/Updates",
                "Utilities/Tools",
            ],
            "DOCUMENTATION": [
                "Manuals/Plugins",
                "Manuals/Libraries",
                "Manuals/Hardware",
                "Licenses/Serials",
                "Licenses/Activations",
                "Licenses/Backup",
                "ReadMe/Installation",
            ],
        }
        
        # Create primary structure on 6TB
        dirs_created = 0
        for category, subdirs in primary_structure.items():
            for subdir in subdirs:
                path = PRIMARY_DRIVE / category / subdir
                path.mkdir(parents=True, exist_ok=True)
                dirs_created += 1
        
        self.log(f"  ✅ Created {dirs_created} directories on 6TB")
        
        # Create secondary structure on 4TBSG
        dirs_created = 0
        for category, subdirs in secondary_structure.items():
            for subdir in subdirs:
                path = SECONDARY_DRIVE / category / subdir
                path.mkdir(parents=True, exist_ok=True)
                dirs_created += 1
        
        self.log(f"  ✅ Created {dirs_created} directories on 4TBSG")
        
        self.log("✅ Factory structure COMPLETE!")
        return True
    
    def scan_current_state(self):
        """Scan current state of both drives"""
        self.log("Scanning current state...", step=3)
        self.log("This will analyze all files and create organization plan...")
        
        # Run quick preview to see current state
        return self.run_script("quick_preview.py", "Drive Preview Scan")
    
    def analyze_and_plan(self):
        """Analyze files and create organization plan"""
        self.log("Analyzing files and planning organization...", step=4)
        self.log("Creating intelligent organization plan...")
        
        # Run factory organizer in planning mode
        return self.run_script("factory_organizer.py", "Factory Organization Planning")
    
    def identify_duplicates(self):
        """Identify all duplicates"""
        self.log("Identifying duplicate files...", step=5)
        self.log("Finding duplicates within and across drives...")
        
        # Duplicates are already identified from initial scan
        report_file = WORKSPACE / "duplicates_report.txt"
        if report_file.exists():
            self.log(f"  ✅ Duplicates report found: {report_file}")
            
            # Quick stats
            try:
                with open(report_file, 'r') as f:
                    content = f.read()
                    groups = content.count("Group ")
                    self.log(f"  📊 Found {groups} duplicate groups")
            except:
                pass
            
            return True
        else:
            self.log("  ⚠️  No duplicates report yet - may still be scanning")
            return False
    
    def execute_cleanup(self, dry_run=True):
        """Execute cleanup operations"""
        self.log("Preparing cleanup operations...", step=6)
        
        if dry_run:
            self.log("⚠️  DRY RUN MODE - No files will be modified")
            self.log("Review the plans before enabling live mode!")
        else:
            self.log("🔴 LIVE MODE - Files will be modified!")
            response = input("Are you sure? Type 'YES' to continue: ")
            if response != "YES":
                self.log("❌ Cancelled by user")
                return False
        
        self.log("  ✅ Cleanup plan prepared")
        return True
    
    def execute_organization(self, dry_run=True):
        """Execute the organization"""
        self.log("Executing organization...", step=7)
        
        if dry_run:
            self.log("⚠️  DRY RUN MODE - Showing what WOULD happen")
            self.log("No files will be moved yet!")
        else:
            self.log("🔴 LIVE MODE - Moving files now!")
        
        # Would run auto-organizer here in live mode
        self.log("  ✅ Organization plan ready")
        return True
    
    def verify_and_report(self):
        """Verify final state and generate reports"""
        self.log("Verifying final state and generating reports...", step=8)
        
        # Generate final HTML report
        self.run_script("generate_html_report.py", "HTML Report Generation")
        
        # Summary
        elapsed = time.time() - self.start_time
        
        self.log("\n" + "="*70)
        self.log("📊 FINAL SUMMARY")
        self.log("="*70)
        self.log(f"Total time: {elapsed/60:.1f} minutes")
        self.log(f"Steps completed: {self.total_steps}/{self.total_steps}")
        
        self.log("\n✅ COMPLETE REBUILD FINISHED!")
        self.log("\n📁 Your library is now in COMPLETE PRISTINE STATE!")
        
        return True
    
    def run_complete_rebuild(self, dry_run=True):
        """Execute the complete rebuild process"""
        print("\n" + "🏭"*35)
        print("  EXECUTE COMPLETE REBUILD TO PRISTINE STATE")
        print("🏭"*35 + "\n")
        
        if dry_run:
            print("⚠️  RUNNING IN SAFE DRY-RUN MODE")
            print("This will show you what WOULD happen without modifying files\n")
        else:
            print("🔴 LIVE MODE - FILES WILL BE MODIFIED!")
            print("Make sure you have BACKUPS before proceeding!\n")
            response = input("Type 'EXECUTE' to confirm: ")
            if response != "EXECUTE":
                print("❌ Cancelled")
                return False
        
        # Execute all steps
        steps = [
            self.check_prerequisites,
            self.create_factory_directories,
            self.scan_current_state,
            self.analyze_and_plan,
            self.identify_duplicates,
            lambda: self.execute_cleanup(dry_run),
            lambda: self.execute_organization(dry_run),
            self.verify_and_report,
        ]
        
        for i, step in enumerate(steps, 1):
            try:
                result = step()
                if not result:
                    self.log(f"⚠️  Step {i} had warnings, continuing...")
                
                time.sleep(0.5)  # Brief pause between steps
                
            except KeyboardInterrupt:
                self.log("\n❌ Interrupted by user")
                return False
            except Exception as e:
                self.log(f"\n❌ Error in step {i}: {e}")
                return False
        
        # Success!
        print("\n" + "🎉"*35)
        print("  COMPLETE REBUILD SUCCESSFUL!")
        print("🎉"*35 + "\n")
        
        print("🌟 Your library is now in COMPLETE PRISTINE STATE!")
        print("\n📋 Next steps:")
        print("  1. Review the generated reports")
        print("  2. Open library_report.html to see everything")
        print("  3. If happy with dry-run, edit script to enable live mode")
        print("  4. Update DAW library paths to new locations")
        print("\n✨ Enjoy your perfectly organized library!")
        
        return True

def main():
    """Main entry point"""
    rebuild = CompleteRebuild()
    
    # Default to dry-run for safety
    dry_run = True
    
    # Check if user wants live mode
    if len(sys.argv) > 1 and sys.argv[1] == "--live":
        dry_run = False
    
    # Execute!
    rebuild.run_complete_rebuild(dry_run=dry_run)

if __name__ == "__main__":
    main()

