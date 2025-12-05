#!/usr/bin/env python3
"""Execute all fixes immediately"""
import sys
sys.path.insert(0, '/Users/m2ultra/NOIZYLAB')
from FIX_ALL_PLAYS import PlayFixer

fixer = PlayFixer()
fixer.fix_all()

