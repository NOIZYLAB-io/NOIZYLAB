#!/usr/bin/env python3
"""
Setup NOIZYLAB API Key for Claude Workspace Integration
Securely stores API key and configures workspace access
"""

import os
import json
import base64
from pathlib import Path
from cryptography.fernet import Fernet
import getpass

class NOIZYLABAPISetup:
    def __init__(self):
        self.home = Path.home()
        self.noizylab_dir = self.home / 'NOIZYLAB'
        self.config_file = self.noizylab_dir / '.noizylabrc'
        self.api_key_file = self.noizylab_dir / '.noizylab_api_key'
        self.workspace_config = self.noizylab_dir / 'claude_workspace.json'
        
        # Ensure NOIZYLAB directory exists
        self.noizylab_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_encryption_key(self):
        """Generate encryption key for API key storage."""
        key_file = self.noizylab_dir / '.encryption_key'
        
        if key_file.exists():
            return key_file.read_bytes()
        else:
            key = Fernet.generate_key()
            key_file.write_bytes(key)
            key_file.chmod(0o600)  # Secure permissions
            return key
    
    def encrypt_api_key(self, api_key):
        """Encrypt API key for secure storage."""
        try:
            key = self.generate_encryption_key()
            f = Fernet(key)
            encrypted = f.encrypt(api_key.encode())
            return encrypted
        except ImportError:
            # Fallback to base64 if cryptography not available
            return base64.b64encode(api_key.encode())
    
    def decrypt_api_key(self, encrypted_key):
        """Decrypt API key."""
        try:
            key = self.generate_encryption_key()
            f = Fernet(key)
            decrypted = f.decrypt(encrypted_key)
            return decrypted.decode()
        except:
            # Fallback to base64
            return base64.b64decode(encrypted_key).decode()
    
    def save_api_key(self, api_key):
        """Save API key securely."""
        encrypted = self.encrypt_api_key(api_key)
        
        # Save encrypted key
        self.api_key_file.write_bytes(encrypted)
        self.api_key_file.chmod(0o600)  # Secure permissions
        
        # Also save to config file (base64 encoded for safety)
        config = {
            'api_key_encrypted': base64.b64encode(encrypted).decode(),
            'api_key_set': True,
            'setup_date': str(Path().cwd()),
        }
        
        self.config_file.write_text(json.dumps(config, indent=2))
        self.config_file.chmod(0o600)
        
        print("✅ API key saved securely")
    
    def load_api_key(self):
        """Load and decrypt API key."""
        if not self.api_key_file.exists():
            return None
        
        try:
            encrypted = self.api_key_file.read_bytes()
            return self.decrypt_api_key(encrypted)
        except Exception as e:
            print(f"Error loading API key: {e}")
            return None
    
    def setup_environment(self):
        """Setup environment variables for Claude workspace."""
        api_key = self.load_api_key()
        if not api_key:
            print("⚠️  No API key found. Please set it up first.")
            return False
        
        # Create environment setup script
        env_script = self.noizylab_dir / 'setup_env.sh'
        env_script_content = f"""#!/bin/bash
# NOIZYLAB API Key Environment Setup
# Source this file: source ~/NOIZYLAB/setup_env.sh

export NOIZYLAB_API_KEY="{api_key}"
export ANTHROPIC_API_KEY="{api_key}"
export CLAUDE_API_KEY="{api_key}"

echo "✅ NOIZYLAB API keys loaded"
"""
        env_script.write_text(env_script_content)
        env_script.chmod(0o755)
        
        # Create Python environment setup
        env_py = self.noizylab_dir / 'setup_env.py'
        env_py_content = f"""#!/usr/bin/env python3
\"\"\"NOIZYLAB API Key Environment Setup for Python\"\"\"
import os
import sys

# Load API key
api_key = "{api_key}"

# Set environment variables
os.environ['NOIZYLAB_API_KEY'] = api_key
os.environ['ANTHROPIC_API_KEY'] = api_key
os.environ['CLAUDE_API_KEY'] = api_key

print("✅ NOIZYLAB API keys loaded into environment")
"""
        env_py.write_text(env_py_content)
        env_py.chmod(0o755)
        
        print("✅ Environment setup scripts created")
        return True
    
    def create_workspace_config(self):
        """Create Claude workspace configuration."""
        api_key = self.load_api_key()
        if not api_key:
            print("⚠️  No API key found. Please set it up first.")
            return False
        
        workspace_config = {
            'workspace_name': 'NOIZYLAB',
            'api_key': api_key,
            'api_endpoint': 'https://api.anthropic.com/v1/messages',
            'model': 'claude-3-5-sonnet-20241022',
            'max_tokens': 8192,
            'temperature': 0.7,
            'tools_enabled': True,
            'workspace_path': str(self.noizylab_dir),
            'integrations': {
                'audio_organizer': True,
                'file_scanner': True,
                'git_organizer': True,
                'downloads_scanner': True
            },
            'settings': {
                'auto_save': True,
                'backup_enabled': True,
                'log_level': 'INFO'
            }
        }
        
        self.workspace_config.write_text(json.dumps(workspace_config, indent=2))
        self.workspace_config.chmod(0o600)
        
        print("✅ Claude workspace configuration created")
        return True
    
    def create_claude_integration(self):
        """Create Claude integration helper."""
        integration_file = self.noizylab_dir / 'claude_integration.py'
        
        integration_code = '''#!/usr/bin/env python3
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
'''
        
        integration_file.write_text(integration_code)
        integration_file.chmod(0o755)
        
        print("✅ Claude integration helper created")
    
    def setup_complete(self, api_key):
        """Complete setup process."""
        print("\n" + "=" * 80)
        print("NOIZYLAB API KEY SETUP")
        print("=" * 80)
        
        # Save API key
        self.save_api_key(api_key)
        
        # Setup environment
        self.setup_environment()
        
        # Create workspace config
        self.create_workspace_config()
        
        # Create integration helper
        self.create_claude_integration()
        
        print("\n" + "=" * 80)
        print("SETUP COMPLETE!")
        print("=" * 80)
        print(f"✅ API key saved: {self.api_key_file}")
        print(f"✅ Config file: {self.config_file}")
        print(f"✅ Workspace config: {self.workspace_config}")
        print(f"✅ Environment scripts: ~/NOIZYLAB/setup_env.sh")
        print(f"✅ Integration helper: ~/NOIZYLAB/claude_integration.py")
        print("\nTo use in your scripts:")
        print("  from claude_integration import get_api_key")
        print("  api_key = get_api_key()")
        print("\nTo load environment:")
        print("  source ~/NOIZYLAB/setup_env.sh")
        print("=" * 80)


def main():
    """Main setup."""
    import sys
    
    setup = NOIZYLABAPISetup()
    
    # Get API key from command line or prompt
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
    else:
        # Try to get from existing config
        existing_key = setup.load_api_key()
        if existing_key:
            print(f"Found existing API key. Update? (y/n): ", end='')
            if input().lower() != 'y':
                print("Keeping existing key.")
                return
        
        api_key = getpass.getpass("Enter NOIZYLAB API key: ")
    
    if not api_key or len(api_key) < 10:
        print("❌ Invalid API key")
        return
    
    setup.setup_complete(api_key)

if __name__ == '__main__':
    main()

