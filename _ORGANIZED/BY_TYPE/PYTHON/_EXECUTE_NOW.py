#!/usr/bin/env python3
"""DIRECT EXECUTION - No path issues"""
import os
import shutil
from pathlib import Path

# Change to script directory first
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Now execute AUTOALLOW
exec(open('AUTOALLOW.py').read())

