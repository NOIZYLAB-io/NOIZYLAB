#!/usr/bin/env python3
"""
Load NOIZYLAB Profile Preferences
Auto-loads hard rules and system settings
"""

import json
from pathlib import Path

PREFERENCES_FILE = Path(__file__).parent / ".noizylab_preferences.json"

class NoizyLabPreferences:
    def __init__(self):
        self.preferences = self.load_preferences()
        self.hard_rules = self.preferences.get('profile_settings', {}).get('preferences', {}).get('hard_rules', {})
        self.behavior = self.preferences.get('profile_settings', {}).get('behavior_settings', {})
    
    def load_preferences(self):
        """Load preferences from file"""
        if PREFERENCES_FILE.exists():
            try:
                with open(PREFERENCES_FILE) as f:
                    return json.load(f)
            except:
                pass
        
        return {}
    
    def get_setting(self, key, default=False):
        """Get a preference setting"""
        # Check hard rules first
        if key in self.hard_rules:
            return self.hard_rules[key]
        
        # Check behavior settings
        if key in self.behavior:
            return self.behavior[key]
        
        return default
    
    def should_auto_execute(self):
        """Check if auto-execute is enabled"""
        return self.get_setting('always_auto_execute', True)
    
    def should_max_speed(self):
        """Check if maximum speed is enabled"""
        return self.get_setting('always_maximum_speed', True)
    
    def should_oversee(self):
        """Check if automatic oversight is enabled"""
        return self.get_setting('always_oversee_transfers', True)

# Global preferences instance
PREFERENCES = NoizyLabPreferences()

# Export settings
AUTO_EXECUTE = PREFERENCES.should_auto_execute()
MAX_SPEED = PREFERENCES.should_max_speed()
AUTO_OVERSEE = PREFERENCES.should_oversee()

