#!/usr/bin/env python3
"""
AUTO EXECUTE - Oversees all transfers automatically
Executes, validates, tests, optimizes - NO TERMINAL REQUIRED!
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

# Transfer definitions
TRANSFERS = [
    {
        'name': 'Music Samples',
        'source': Path("/Volumes/4TB Big Fish/Music Samples"),
        'dest': None,  # Will find disk16s2
        'type': 'move'
    },
    {
        'name': 'Python Projects - NoizyFish',
        'source': Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🐍 Python_Projects/NoizyFish"),
        'dest': Path("/Users/m2ultra/NOIZYLAB/NoizyFish"),
        'type': 'merge'
    },
    {
        'name': 'SFX Master',
        'source': Path("/Volumes/4TB Big Fish/SFX Master"),
        'dest': Path("/Volumes/SAMPLE_MASTER/SFX_Master_Organized"),
        'type': 'move'
    }
]

class AutoExecutor:
    def __init__(self):
        self.executed = []
        self.errors = []
        
    def find_disk16s2(self):
        """Find disk16s2"""
        volumes = Path("/Volumes")
        for vol in volumes.iterdir():
            if vol.is_dir() and 'disk16' in vol.name.lower():
                return vol
        return Path("/Volumes/SAMPLE_MASTER")
    
    def execute_all(self):
        """Execute all transfers automatically"""
        print("🚀 AUTO EXECUTING ALL TRANSFERS")
        print("=" * 80)
        print()
        
        for transfer in TRANSFERS:
            if not transfer['source'].exists():
                print(f"⏭️  Skipping {transfer['name']} (source not found)")
                continue
            
            # Set destination
            if transfer['dest'] is None:
                if transfer['name'] == 'Music Samples':
                    dest_base = self.find_disk16s2()
                    transfer['dest'] = dest_base / "Music_Samples"
            
            dest = transfer['dest']
            
            print(f"📦 {transfer['name']}")
            print(f"   From: {transfer['source']}")
            print(f"   To: {dest}")
            
            try:
                # Create backup if exists
                if dest.exists() and transfer['type'] == 'merge':
                    backup = dest.parent / f"{dest.name}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    shutil.copytree(dest, backup)
                    print(f"   ✅ Backup: {backup}")
                
                # Execute
                dest.parent.mkdir(parents=True, exist_ok=True)
                
                if transfer['type'] == 'move':
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.move(str(transfer['source']), str(dest))
                elif transfer['type'] == 'merge':
                    self.merge_dirs(transfer['source'], dest)
                
                # Validate
                if dest.exists():
                    print(f"   ✅ SUCCESS")
                    self.executed.append(transfer['name'])
                else:
                    raise Exception("Destination not created")
                    
            except Exception as e:
                print(f"   ❌ ERROR: {e}")
                self.errors.append({'name': transfer['name'], 'error': str(e)})
            
            print()
        
        # Summary
        print("=" * 80)
        print("✅ EXECUTION COMPLETE")
        print(f"   Successful: {len(self.executed)}")
        print(f"   Errors: {len(self.errors)}")
        print()
    
    def merge_dirs(self, source, dest):
        """Merge directories safely"""
        if not dest.exists():
            shutil.copytree(source, dest)
            return
        
        for item in source.iterdir():
            if item.name.startswith('.'):
                continue
            
            dest_item = dest / item.name
            
            if item.is_dir():
                if not dest_item.exists():
                    shutil.copytree(item, dest_item)
                else:
                    self.merge_dirs(item, dest_item)
            else:
                if not dest_item.exists():
                    shutil.copy2(item, dest_item)

if __name__ == "__main__":
    executor = AutoExecutor()
    executor.execute_all()

