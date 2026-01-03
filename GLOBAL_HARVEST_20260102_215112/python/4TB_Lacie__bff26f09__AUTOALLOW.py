#!/usr/bin/env python3
"""
AUTOALLOW - Automatic execution of ALL operations
No prompts, no confirmations - just executes everything
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class AutoAllow:
    def __init__(self):
        self.noizylab = Path("/Users/m2ultra/NOIZYLAB")
        self.executed = []
        
    def auto_fix(self):
        """Auto-fix all issues"""
        print("🔧 AUTO-FIXING ALL ISSUES...")
        
        fixes = 0
        
        # Clean .DS_Store
        for ds in self.noizylab.rglob('.DS_Store'):
            try:
                ds.unlink()
                fixes += 1
            except:
                pass
        
        # Clean temp files
        for temp in self.noizylab.rglob('*.tmp'):
            try:
                temp.unlink()
                fixes += 1
            except:
                pass
        
        for temp in self.noizylab.rglob('*.bak'):
            try:
                temp.unlink()
                fixes += 1
            except:
                pass
        
        # Clean Python cache
        for cache in self.noizylab.rglob('__pycache__'):
            try:
                shutil.rmtree(cache)
                fixes += 1
            except:
                pass
        
        print(f"   ✅ Fixed {fixes} items")
        self.executed.append(f"Fixed {fixes} items")
    
    def auto_transfer_music_samples(self):
        """Auto-transfer Music Samples"""
        source = Path("/Volumes/4TB Big Fish/Music Samples")
        if not source.exists():
            return
        
        # Find disk16s2
        dest_base = None
        for vol in Path("/Volumes").iterdir():
            if vol.is_dir() and 'disk16' in vol.name.lower():
                dest_base = vol
                break
        
        if not dest_base:
            dest_base = Path("/Volumes/SAMPLE_MASTER")
        
        dest = dest_base / "Music_Samples"
        
        try:
            if dest.exists():
                shutil.rmtree(dest)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(dest))
            print(f"   ✅ Music Samples → {dest}")
            self.executed.append("Music Samples moved")
        except Exception as e:
            print(f"   ⚠️  Music Samples: {e}")
    
    def auto_absorb_python(self):
        """Auto-absorb Python projects"""
        source = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🐍 Python_Projects/NoizyFish")
        if not source.exists():
            return
        
        dest = self.noizylab / "NoizyFish"
        
        try:
            if not dest.exists():
                shutil.copytree(source, dest)
                print(f"   ✅ NoizyFish → {dest}")
                self.executed.append("NoizyFish absorbed")
            else:
                # Merge
                for item in source.iterdir():
                    if item.name.startswith('.'):
                        continue
                    dest_item = dest / item.name
                    if not dest_item.exists():
                        if item.is_dir():
                            shutil.copytree(item, dest_item)
                        else:
                            shutil.copy2(item, dest_item)
                print(f"   ✅ NoizyFish merged")
                self.executed.append("NoizyFish merged")
        except Exception as e:
            print(f"   ⚠️  NoizyFish: {e}")
    
    def auto_transfer_sfx(self):
        """Auto-transfer SFX Master"""
        source = Path("/Volumes/4TB Big Fish/SFX Master")
        if not source.exists():
            return
        
        dest = Path("/Volumes/SAMPLE_MASTER/SFX_Master_Organized")
        
        try:
            if dest.exists():
                shutil.rmtree(dest)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(dest))
            print(f"   ✅ SFX Master → {dest}")
            self.executed.append("SFX Master moved")
        except Exception as e:
            print(f"   ⚠️  SFX Master: {e}")
    
    def execute_all(self):
        """Execute everything automatically"""
        print("=" * 80)
        print(" " * 20 + "AUTOALLOW - EXECUTING ALL")
        print("=" * 80)
        print()
        
        # Auto-fix
        self.auto_fix()
        
        # Auto-transfers
        print("\n🚀 AUTO-TRANSFERRING...")
        self.auto_transfer_music_samples()
        self.auto_absorb_python()
        self.auto_transfer_sfx()
        
        # Summary
        print("\n" + "=" * 80)
        print("✅ AUTOALLOW COMPLETE!")
        print("=" * 80)
        print(f"Operations executed: {len(self.executed)}")
        for op in self.executed:
            print(f"   • {op}")
        print()

def main():
    auto = AutoAllow()
    auto.execute_all()

if __name__ == "__main__":
    main()

