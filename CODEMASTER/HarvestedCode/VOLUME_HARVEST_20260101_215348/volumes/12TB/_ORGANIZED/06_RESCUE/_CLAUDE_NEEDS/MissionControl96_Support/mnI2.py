#!/usr/bin/env python3
"""
Noizy_Aquarium Script Registry
=============================

This file provides easy access to all scripts in the Noizy_Aquarium collection.
Run this file to see all available scripts and their descriptions.
"""

import os
import sys
from pathlib import Path

AQUARIUM_ROOT = Path(__file__).parent

def list_all_scripts():
    """List all Python scripts in the Noizy_Aquarium with descriptions."""
    categories = {
        'audio_processing': 'Audio and Kontakt processing tools',
        'automation': 'Agent, genie, and automation scripts',
        'file_management': 'File organization and library management',
        'utilities': 'General purpose utilities and helpers',
        'workspace_tools': 'VS Code and workspace configuration'
    }
    
    print("🐠 Noizy_Aquarium Script Collection 🐠")
    print("=" * 50)
    
    total_scripts = 0
    
    for category, description in categories.items():
        category_path = AQUARIUM_ROOT / category
        if category_path.exists():
            scripts = list(category_path.glob("*.py"))
            if scripts:
                print(f"\n📁 {category.upper()}")
                print(f"   {description}")
                print("   " + "-" * len(description))
                
                for script in sorted(scripts):
                    print(f"   • {script.name}")
                    total_scripts += 1
    
    print(f"\n🎯 Total scripts organized: {total_scripts}")
    print(f"\n💡 To use any script:")
    print(f"   cd {AQUARIUM_ROOT}")
    print(f"   python category/script_name.py")
    
    print(f"\n🔗 To make scripts importable system-wide:")
    print(f"   export PYTHONPATH=\"$PYTHONPATH:{AQUARIUM_ROOT}\"")

def add_to_python_path():
    """Add Noizy_Aquarium to Python path for this session."""
    if str(AQUARIUM_ROOT) not in sys.path:
        sys.path.insert(0, str(AQUARIUM_ROOT))
        print(f"✅ Added {AQUARIUM_ROOT} to Python path")
    else:
        print(f"ℹ️  {AQUARIUM_ROOT} already in Python path")

if __name__ == "__main__":
    list_all_scripts()
    add_to_python_path()