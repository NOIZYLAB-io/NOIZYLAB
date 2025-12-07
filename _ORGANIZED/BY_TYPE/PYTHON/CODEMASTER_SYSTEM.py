#!/usr/bin/env python3
"""
CODEMASTER SYSTEM - Unified IT_AGENT & GABRIEL
The FASTEST code & asset fisherman using FISHNET in MC96 ecosystem
"""

import os
import subprocess
from pathlib import Path
import json

class CodemasterSystem:
    def __init__(self):
        self.noizylab = Path("/Users/m2ultra/NOIZYLAB")
        self.it_genius = self.noizylab / "it_genius"
        self.gabriel = self.noizylab / "gabriel"
        self.mc96 = self.noizylab / "mc96"
        
        # Load preferences
        self.load_preferences()
    
    def load_preferences(self):
        """Load hard rules from preferences"""
        prefs_file = self.noizylab / ".noizylab_preferences.json"
        if prefs_file.exists():
            with open(prefs_file) as f:
                prefs = json.load(f)
                self.auto_execute = prefs.get('profile_settings', {}).get('preferences', {}).get('hard_rules', {}).get('always_auto_execute', True)
        else:
            self.auto_execute = True
    
    def find_all_codemasters(self):
        """Find all CODEMASTER agents"""
        print("=" * 80)
        print(" " * 20 + "CODEMASTER SYSTEM - IT_AGENT & GABRIEL")
        print("=" * 80)
        print()
        
        codemasters = {}
        
        # IT_GENIUS (IT_AGENT)
        if self.it_genius.exists():
            print("🤖 IT_AGENT (IT_GENIUS):")
            print(f"   Location: {self.it_genius}")
            
            launchers = [
                "MASTER_LAUNCHER.py",
                "START_HERE.py",
                "ULTRA_LAUNCH.py",
                "PERFECT_LAUNCHER.py"
            ]
            
            for launcher in launchers:
                launcher_path = self.it_genius / launcher
                if launcher_path.exists():
                    print(f"   ✅ {launcher}")
                    codemasters['it_agent'] = {
                        'name': 'IT_AGENT',
                        'location': str(self.it_genius),
                        'launcher': str(launcher_path),
                        'type': 'Python'
                    }
        
        # GABRIEL
        if self.gabriel.exists():
            print("\n🟣 GABRIEL:")
            print(f"   Location: {self.gabriel}")
            
            gabriel_cli = self.noizylab / "gabriel-cli.mjs"
            if gabriel_cli.exists():
                print(f"   ✅ CLI: gabriel-cli.mjs")
                print(f"   ✅ Scanner: gabriel/scanner/")
                print(f"   ✅ Code Processor: gabriel/code-processor/")
                
                codemasters['gabriel'] = {
                    'name': 'GABRIEL',
                    'location': str(self.gabriel),
                    'cli': str(gabriel_cli),
                    'scanner': str(self.gabriel / "scanner"),
                    'code_processor': str(self.gabriel / "code-processor"),
                    'type': 'Node.js'
                }
        
        # MC96 FISHNET
        if self.mc96.exists():
            print("\n🐟 MC96 FISHNET:")
            print(f"   Location: {self.mc96}")
            
            mc96_cli = self.noizylab / "mc96-cli.mjs"
            if mc96_cli.exists():
                print(f"   ✅ CLI: mc96-cli.mjs")
                codemasters['mc96'] = {
                    'name': 'MC96',
                    'location': str(self.mc96),
                    'cli': str(mc96_cli),
                    'type': 'Node.js'
                }
        
        return codemasters
    
    def activate_codemaster_unified(self):
        """Activate unified CODEMASTER system"""
        print("\n" + "=" * 80)
        print(" " * 20 + "ACTIVATING CODEMASTER SYSTEM")
        print("=" * 80)
        print()
        
        codemasters = self.find_all_codemasters()
        
        print("\n🚀 CODEMASTER ACTIVATION OPTIONS:")
        print()
        print("1. 🤖 IT_AGENT (Python) - Master system launcher")
        print("2. 🟣 GABRIEL (Node.js) - Scanner & code processor")
        print("3. 🐟 MC96 FISHNET (Node.js) - Code & asset finder")
        print("4. 🔥 UNIFIED MODE - All codemasters active")
        print()
        
        if self.auto_execute:
            print("⚠️  AUTO-EXECUTE MODE - Will activate all automatically")
            self.activate_all(codemasters)
        else:
            choice = input("Select codemaster (1-4): ").strip()
            if choice == "1":
                self.activate_it_agent()
            elif choice == "2":
                self.activate_gabriel()
            elif choice == "3":
                self.activate_mc96()
            elif choice == "4":
                self.activate_all(codemasters)
    
    def activate_it_agent(self):
        """Activate IT_AGENT"""
        launcher = self.it_genius / "MASTER_LAUNCHER.py"
        if launcher.exists():
            print(f"\n🚀 Activating IT_AGENT...")
            print(f"   {launcher}")
            subprocess.run(["python3", str(launcher)])
    
    def activate_gabriel(self):
        """Activate GABRIEL"""
        cli = self.noizylab / "gabriel-cli.mjs"
        if cli.exists():
            print(f"\n🟣 Activating GABRIEL...")
            print(f"   {cli}")
            subprocess.run(["node", str(cli), "scan"])
    
    def activate_mc96(self):
        """Activate MC96 FISHNET"""
        cli = self.noizylab / "mc96-cli.mjs"
        if cli.exists():
            print(f"\n🐟 Activating MC96 FISHNET...")
            print(f"   {cli}")
            subprocess.run(["node", str(cli)])
    
    def activate_all(self, codemasters):
        """Activate all codemasters"""
        print("\n🔥 ACTIVATING ALL CODEMASTERS...")
        
        # GABRIEL scanner first
        if 'gabriel' in codemasters:
            print("\n🟣 Starting GABRIEL scanner...")
            cli = codemasters['gabriel']['cli']
            subprocess.Popen(["node", cli, "scan"], cwd=str(self.noizylab))
        
        # MC96 FISHNET
        if 'mc96' in codemasters:
            print("🐟 Starting MC96 FISHNET...")
            cli = codemasters['mc96']['cli']
            subprocess.Popen(["node", cli], cwd=str(self.noizylab))
        
        # IT_AGENT
        if 'it_agent' in codemasters:
            print("🤖 Starting IT_AGENT...")
            launcher = codemasters['it_agent']['launcher']
            subprocess.Popen(["python3", launcher])
        
        print("\n✅ All CODEMASTERS activated!")

def main():
    codemaster = CodemasterSystem()
    codemaster.activate_codemaster_unified()

if __name__ == "__main__":
    main()

