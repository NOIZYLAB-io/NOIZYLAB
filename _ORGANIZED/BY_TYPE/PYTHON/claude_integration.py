#!/usr/bin/env python3
"""
Claude Workspace Integration for NOIZYLAB
Provides easy access to Claude API from NOIZYLAB tools
"""

import os
import json
from pathlib import Path

class ClaudeWorkspace:
    def __init__(self):
        self.config_path = Path.home() / 'NOIZYLAB' / 'claude_workspace.json'
        self.config = self.load_config()
        self.api_key = self.config.get('api_key') if self.config else None
        
        # Set environment variables
        if self.api_key:
            os.environ['ANTHROPIC_API_KEY'] = self.api_key
            os.environ['NOIZYLAB_API_KEY'] = self.api_key
    
    def load_config(self):
        """Load workspace configuration."""
        if self.config_path.exists():
            try:
                return json.loads(self.config_path.read_text())
            except:
                return None
        return None
    
    def get_api_key(self):
        """Get API key from config or environment."""
        if self.api_key:
            return self.api_key
        return os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('NOIZYLAB_API_KEY')
    
    def get_workspace_path(self):
        """Get workspace path."""
        if self.config:
            return Path(self.config.get('workspace_path', Path.home() / 'NOIZYLAB'))
        return Path.home() / 'NOIZYLAB'
    
    def is_integration_enabled(self, integration_name):
        """Check if integration is enabled."""
        if self.config:
            return self.config.get('integrations', {}).get(integration_name, False)
        return False

# Global instance
workspace = ClaudeWorkspace()

# Convenience functions
def get_api_key():
    """Get Claude API key."""
    return workspace.get_api_key()

def get_workspace_path():
    """Get workspace path."""
    return workspace.get_workspace_path()

def is_enabled(integration):
    """Check if integration is enabled."""
    return workspace.is_integration_enabled(integration)
