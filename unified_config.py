#!/usr/bin/env python3
"""
Unified Configuration System for NOIZYLAB Tools
Centralized configuration management with Claude integration
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
import sys

sys.path.insert(0, str(Path.home() / 'NOIZYLAB'))
try:
    from claude_integration import get_api_key, get_workspace_path
except ImportError:
    pass

class UnifiedConfig:
    def __init__(self):
        self.config_dir = Path.home() / 'NOIZYLAB' / '.config'
        self.config_file = self.config_dir / 'noizylab_config.json'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        self.default_config = {
            'workspace': {
                'path': str(Path.home() / 'NOIZYLAB'),
                'audio_dir': str(Path.home() / 'NOIZYLAB' / 'Audio'),
                'files_dir': str(Path.home() / 'NOIZYLAB' / 'Files'),
                'projects_dir': str(Path.home() / 'NOIZYLAB' / 'Projects'),
                'media_dir': str(Path.home() / 'NOIZYLAB' / 'Media')
            },
            'organizer': {
                'use_ai': True,
                'max_workers': 8,
                'duplicate_detection': True,
                'audio_fingerprinting': True,
                'auto_organize': False
            },
            'claude': {
                'enabled': True,
                'model': 'claude-3-5-sonnet-20241022',
                'max_tokens': 8192,
                'temperature': 0.7
            },
            'database': {
                'path': str(Path.home() / 'NOIZYLAB' / '.data' / 'noizylab.db'),
                'wal_mode': True,
                'cache_size': 10000
            },
            'integrations': {
                'audio_organizer': True,
                'file_scanner': True,
                'git_organizer': True,
                'downloads_scanner': True,
                'claude_workspace': True
            },
            'settings': {
                'auto_backup': True,
                'log_level': 'INFO',
                'notifications': True
            }
        }
        
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                    # Merge with defaults
                    config = self.default_config.copy()
                    self._deep_update(config, user_config)
                    return config
            except Exception as e:
                print(f"Error loading config: {e}")
        
        # Save default config
        self.save_config(self.default_config)
        return self.default_config
    
    def _deep_update(self, base, update):
        """Deep update dictionary."""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_update(base[key], value)
            else:
                base[key] = value
    
    def save_config(self, config: Optional[Dict[str, Any]] = None):
        """Save configuration to file."""
        if config is None:
            config = self.config
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get(self, key_path: str, default=None):
        """Get configuration value by dot-separated path."""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path: str, value: Any):
        """Set configuration value by dot-separated path."""
        keys = key_path.split('.')
        config = self.config
        
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        config[keys[-1]] = value
        self.save_config()
    
    def get_workspace_path(self) -> Path:
        """Get workspace path."""
        return Path(self.get('workspace.path', str(Path.home() / 'NOIZYLAB')))
    
    def get_audio_dir(self) -> Path:
        """Get audio directory."""
        return Path(self.get('workspace.audio_dir', str(Path.home() / 'NOIZYLAB' / 'Audio')))
    
    def is_integration_enabled(self, integration: str) -> bool:
        """Check if integration is enabled."""
        return self.get(f'integrations.{integration}', False)
    
    def is_ai_enabled(self) -> bool:
        """Check if AI is enabled."""
        return self.get('organizer.use_ai', True) and self.get('claude.enabled', True)
    
    def get_claude_config(self) -> Dict[str, Any]:
        """Get Claude configuration."""
        return self.get('claude', {})

# Global instance
_config = None

def get_config() -> UnifiedConfig:
    """Get global config instance."""
    global _config
    if _config is None:
        _config = UnifiedConfig()
    return _config

