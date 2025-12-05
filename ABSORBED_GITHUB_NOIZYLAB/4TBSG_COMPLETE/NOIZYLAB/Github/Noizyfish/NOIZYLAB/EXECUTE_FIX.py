#!/usr/bin/env python3
"""Execute fix with proper path handling"""
import sys
import os
from pathlib import Path

# Change to script directory
os.chdir(Path(__file__).parent)

# Import and execute
exec(open('FIX_NOW_IMMEDIATE.py').read())

