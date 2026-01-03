#!/usr/bin/env python3
"""
HOT ROD LAUNCHER - Maximum Performance Mode
"""
import sys
import os
from pathlib import Path

# Enable optimizations
os.environ['PYTHONOPTIMIZE'] = '2'  # Remove assert statements
os.environ['PYTHONUNBUFFERED'] = '1'  # Unbuffered output

# Add hot rod optimizations
sys.path.insert(0, str(Path(__file__).parent))

if __name__ == "__main__":
    from SUPER_ULTIMATE_SYSTEM import SuperUltimateSystem
    system = SuperUltimateSystem()
    system.main_menu()
