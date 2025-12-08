#!/usr/bin/env python3
"""
Auto-Execute with Profile Preferences
Uses hard rules from profile settings
"""

import sys
from pathlib import Path

# Load preferences first
sys.path.insert(0, str(Path(__file__).parent))
try:
    from load_preferences import PREFERENCES, AUTO_EXECUTE, MAX_SPEED
except:
    AUTO_EXECUTE = True
    MAX_SPEED = True

# Import and execute based on preferences
if AUTO_EXECUTE:
    if MAX_SPEED:
        # Maximum speed mode
        exec(open('/Users/m2ultra/NOIZYLAB/GORUNFREEX1000.py').read())
    else:
        # Normal auto mode
        exec(open('/Users/m2ultra/NOIZYLAB/AUTOALLOW.py').read())

