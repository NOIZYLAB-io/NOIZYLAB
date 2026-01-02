#!/usr/bin/env python3
"""
NoizyFish_Aquarium Script Registry
=================================

This file provides easy access to all scripts in the NoizyFish_Aquarium collection.
Run this file to see all available scripts and their descriptions.
"""

import os
import sys
from pathlib import Path

AQUARIUM_ROOT = Path(__file__).parent.parent  # NoizyFish_Aquarium root
PYTHON_PROJECTS = Path(__file__).parent       # 🐍 Python_Projects
AI_TOOLKIT = AQUARIUM_ROOT / "🤖 AI_Toolkit"

def list_all_scripts():
    """List all Python scripts in the NoizyFish_Aquarium with descriptions."""
    categories = {
        'audio_processing': 'Audio and Kontakt processing tools',
        'automation': 'Agent, genie, and automation scripts',
        'file_management': 'File organization and library management',
        'utilities': 'General purpose utilities and helpers',
        'workspace_tools': 'VS Code and workspace configuration'
    }
    
    print("🐠 NoizyFish_Aquarium Script Collection 🐠")
    print("=" * 50)
    
    total_scripts = 0
    
    # Python Projects organized scripts
    print(f"\n📁 PYTHON PROJECTS ({PYTHON_PROJECTS.name})")
    for category, description in categories.items():
        category_path = PYTHON_PROJECTS / category
        if category_path.exists():
            scripts = list(category_path.glob("*.py"))
            if scripts:
                print(f"\n  � {category.upper()}")
                print(f"     {description}")
                print("     " + "-" * len(description))
                
                for script in sorted(scripts):
                    print(f"     • {script.name}")
                    total_scripts += 1
    
    # AI Toolkit scripts
    if AI_TOOLKIT.exists():
        ai_scripts = list(AI_TOOLKIT.glob("*.py"))
        if ai_scripts:
            print(f"\n📁 AI TOOLKIT ({AI_TOOLKIT.name})")
            print("     Advanced AI tools and agents")
            print("     " + "-" * 28)
            for script in sorted(ai_scripts):
                print(f"     • {script.name}")
                total_scripts += 1
    
    # NoizyFish core project
    noizyfish_path = PYTHON_PROJECTS / "NoizyFish"
    if noizyfish_path.exists():
        fish_scripts = list(noizyfish_path.glob("*.py"))
        if fish_scripts:
            print(f"\n📁 NOIZYFISH CORE")
            print("     Core NoizyFish project files")
            print("     " + "-" * 28)
            for script in sorted(fish_scripts):
                print(f"     • {script.name}")
                total_scripts += 1
    
    print(f"\n🎯 Total scripts available: {total_scripts}")
    print(f"\n💡 To use Python Project scripts:")
    print(f"   cd {PYTHON_PROJECTS}")
    print(f"   python category/script_name.py")
    
    print(f"\n🤖 To use AI Toolkit scripts:")
    print(f"   cd {AI_TOOLKIT}")
    print(f"   python script_name.py")
    
    print(f"\n🔗 To make scripts importable system-wide:")
    print(f"   export PYTHONPATH=\"$PYTHONPATH:{PYTHON_PROJECTS}\"")

def add_to_python_path():
    """Add NoizyFish_Aquarium Python projects to Python path for this session."""
    if str(PYTHON_PROJECTS) not in sys.path:
        sys.path.insert(0, str(PYTHON_PROJECTS))
        print(f"✅ Added {PYTHON_PROJECTS} to Python path")
    else:
        print(f"ℹ️  {PYTHON_PROJECTS} already in Python path")

if __name__ == "__main__":
    list_all_scripts()
    add_to_python_path()