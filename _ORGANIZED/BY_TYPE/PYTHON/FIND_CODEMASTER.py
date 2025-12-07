#!/usr/bin/env python3
"""
FIND CODEMASTER - Locate IT_AGENT and FISHNET
The fastest code & asset fisherman in MC96 ecosystem
"""

import os
from pathlib import Path
import json

class CodemasterFinder:
    def __init__(self):
        self.noizylab = Path("/Users/m2ultra/NOIZYLAB")
        self.it_genius = self.noizylab / "it_genius"
        self.mc96 = self.noizylab / "mc96"
        
    def find_codemaster(self):
        """Find CODEMASTER IT_AGENT"""
        print("=" * 80)
        print(" " * 20 + "FINDING CODEMASTER IT_AGENT")
        print("=" * 80)
        print()
        
        codemaster_locations = []
        
        # Check IT_GENIUS directory
        if self.it_genius.exists():
            print("✅ Found IT_GENIUS directory:")
            print(f"   Location: {self.it_genius}")
            print()
            
            # Find main launchers
            launchers = [
                "MASTER_LAUNCHER.py",
                "START_HERE.py",
                "ULTRA_LAUNCH.py",
                "PERFECT_LAUNCHER.py",
                "SUPER_ULTIMATE_SYSTEM.py",
                "ULTIMATE_1000X_SYSTEM.py"
            ]
            
            print("🚀 IT_AGENT Launchers:")
            for launcher in launchers:
                launcher_path = self.it_genius / launcher
                if launcher_path.exists():
                    print(f"   ✅ {launcher}")
                    codemaster_locations.append(str(launcher_path))
        
        # Check MC96 for FISHNET
        if self.mc96.exists():
            print("\n✅ Found MC96 directory:")
            print(f"   Location: {self.mc96}")
            print()
            
            # Look for FISHNET
            print("🐟 FISHNET Code Finder:")
            fishnet_files = list(self.mc96.rglob("*fishnet*"))
            fishnet_files.extend(list(self.noizylab.rglob("*FISHNET*")))
            
            if fishnet_files:
                for f in fishnet_files:
                    print(f"   ✅ {f}")
            else:
                print("   ⚠️  FISHNET not found - may be integrated into MC96 CLI")
            
            # Check MC96 CLI for code finding capabilities
            mc96_cli = self.noizylab / "mc96-cli.mjs"
            if mc96_cli.exists():
                print(f"   ✅ MC96 CLI: {mc96_cli}")
                print("      This is the code & asset finder for MC96 ecosystem!")
        
        # Check for code finder scripts
        print("\n🔍 Code Finding Capabilities:")
        finders = [
            "universal_problem_solver.py",
            "code_cleaner.py",
            "VOLUME_SCANNER.py"
        ]
        
        for finder in finders:
            finder_path = self.it_genius / finder
            if finder_path.exists():
                print(f"   ✅ {finder}")
        
        return codemaster_locations
    
    def activate_codemaster(self):
        """Activate CODEMASTER with FISHNET"""
        print("\n" + "=" * 80)
        print(" " * 20 + "ACTIVATING CODEMASTER")
        print("=" * 80)
        print()
        
        # Main launcher
        main_launcher = self.it_genius / "MASTER_LAUNCHER.py"
        
        if main_launcher.exists():
            print(f"🚀 Activating IT_AGENT (CODEMASTER)...")
            print(f"   Launcher: {main_launcher}")
            print()
            print("✅ CODEMASTER READY!")
            print()
            print("To activate:")
            print(f"   cd {self.it_genius}")
            print(f"   python3 MASTER_LAUNCHER.py")
            print()
            print("OR:")
            print(f"   cd {self.noizylab}")
            print(f"   python3 mc96-cli.mjs")
            print()
        
        # FISHNET activation
        print("🐟 FISHNET Code Finder:")
        print("   MC96 CLI has integrated code finding")
        print("   Use: node mc96-cli.mjs")
        print()

def main():
    finder = CodemasterFinder()
    locations = finder.find_codemaster()
    finder.activate_codemaster()

if __name__ == "__main__":
    main()

