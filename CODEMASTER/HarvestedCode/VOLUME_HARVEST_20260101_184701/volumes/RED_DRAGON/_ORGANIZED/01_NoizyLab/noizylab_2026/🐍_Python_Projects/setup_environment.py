#!/usr/bin/env python3
"""
Noizy_Aquarium Environment Setup
===============================

This script adds Noizy_Aquarium to your shell environment so you can
import scripts from anywhere in your system.
"""

import os
import subprocess
from pathlib import Path

AQUARIUM_PATH = str(Path(__file__).parent.absolute())
SHELL_RC_FILES = [
    Path.home() / ".zshrc",
    Path.home() / ".bashrc", 
    Path.home() / ".bash_profile"
]

def add_to_shell_rc():
    """Add PYTHONPATH export to shell RC files."""
    export_line = f'export PYTHONPATH="${{PYTHONPATH}}:{AQUARIUM_PATH}"'
    comment_line = "# Noizy_Aquarium Python Scripts"
    
    for rc_file in SHELL_RC_FILES:
        if rc_file.exists():
            # Check if already added
            content = rc_file.read_text()
            if AQUARIUM_PATH in content:
                print(f"✅ {rc_file.name} already configured")
                continue
            
            # Add to RC file
            with open(rc_file, 'a') as f:
                f.write(f"\n{comment_line}\n{export_line}\n")
            print(f"✅ Added to {rc_file.name}")
    
    print(f"\n🔄 Restart your terminal or run:")
    print(f"   source ~/.zshrc")
    print(f"\n🐍 Then you can import scripts from anywhere:")
    print(f"   python -c \"from noizy_aquarium.automation import agent_preflight\"")

def create_symlink():
    """Create a symlink in a common location for easy access."""
    symlink_path = Path.home() / "bin" / "noizy_aquarium"
    bin_dir = Path.home() / "bin"
    
    # Create bin directory if it doesn't exist
    bin_dir.mkdir(exist_ok=True)
    
    # Create symlink
    if not symlink_path.exists():
        try:
            symlink_path.symlink_to(AQUARIUM_PATH)
            print(f"✅ Created symlink: {symlink_path} -> {AQUARIUM_PATH}")
        except OSError as e:
            print(f"⚠️  Could not create symlink: {e}")
    else:
        print(f"✅ Symlink already exists: {symlink_path}")

if __name__ == "__main__":
    print("🐠 Setting up Noizy_Aquarium environment...")
    print(f"📁 Aquarium location: {AQUARIUM_PATH}")
    print()
    
    add_to_shell_rc()
    create_symlink()
    
    print(f"\n🎉 Setup complete! Your {len(os.listdir(AQUARIUM_PATH))} Python scripts are now organized and accessible.")