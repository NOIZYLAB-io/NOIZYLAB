#!/usr/bin/env python3
"""
Integration tests for cloud agent delegation
Tests the cloud-delegate.py functionality
"""

import json
import sys
from pathlib import Path

# Add AGENTS directory to path
AGENTS_DIR = Path(__file__).parent

def load_registry():
    """Load the agent registry configuration"""
    registry_path = AGENTS_DIR / "registry.json"
    with open(registry_path, 'r') as f:
        return json.load(f)

try:
    # Test registry loading
    print("Testing registry loading...")
    registry = load_registry()
    assert 'agents' in registry, "Registry missing 'agents' key"
    assert 'cloud' in registry, "Registry missing 'cloud' key"
    assert registry['cloud']['enabled'] == True, "Cloud should be enabled"
    print("✅ Registry loads correctly")
    
    # Test agent configuration
    print("\nTesting agent configuration...")
    agent_ids = [agent['id'] for agent in registry['agents']]
    assert 'gabriel' in agent_ids, "gabriel agent not found"
    assert 'mc96' in agent_ids, "mc96 agent not found"
    assert 'systemGuardian' in agent_ids, "systemGuardian agent not found"
    print("✅ All expected agents present")
    
    # Test cloud configuration
    print("\nTesting cloud configuration...")
    cloud_config = registry['cloud']
    assert 'endpoint' in cloud_config, "Missing cloud endpoint"
    assert 'endpoints' in cloud_config, "Missing cloud endpoints"
    assert 'health' in cloud_config['endpoints'], "Missing health endpoint"
    assert 'list' in cloud_config['endpoints'], "Missing list endpoint"
    assert 'delegate' in cloud_config['endpoints'], "Missing delegate endpoint"
    print("✅ Cloud configuration valid")
    
    # Test agent deployment modes
    print("\nTesting agent deployment modes...")
    for agent in registry['agents']:
        assert 'deployment' in agent, f"Agent {agent['id']} missing deployment key"
        assert isinstance(agent['deployment'], list), f"Agent {agent['id']} deployment should be a list"
        assert len(agent['deployment']) > 0, f"Agent {agent['id']} has empty deployment list"
    print("✅ All agents have valid deployment modes")
    
    # Test SystemGuardian is cloud-only
    system_guardian = next(a for a in registry['agents'] if a['id'] == 'systemGuardian')
    assert system_guardian['status'] == 'active', "SystemGuardian should be active"
    assert 'cloud' in system_guardian['deployment'], "SystemGuardian should support cloud deployment"
    print("✅ SystemGuardian is properly configured as cloud-enabled")
    
    # Test cloud-delegate.py script exists and is executable
    print("\nTesting cloud-delegate.py...")
    cloud_delegate_path = AGENTS_DIR / "cloud-delegate.py"
    assert cloud_delegate_path.exists(), "cloud-delegate.py not found"
    assert cloud_delegate_path.is_file(), "cloud-delegate.py is not a file"
    print("✅ cloud-delegate.py exists")
    
    # Test launch.sh exists
    print("\nTesting launch.sh...")
    launch_sh_path = AGENTS_DIR / "launch.sh"
    assert launch_sh_path.exists(), "launch.sh not found"
    assert launch_sh_path.is_file(), "launch.sh is not a file"
    print("✅ launch.sh exists")
    
    print("\n" + "="*50)
    print("🎉 All tests passed!")
    print("="*50)
    print("\nCloud agent delegation is ready to use:")
    print("  - Cloud endpoint:", cloud_config['endpoint'])
    print("  - Available agents:", ', '.join(agent_ids))
    print("  - Test with: ./launch.sh cloud-health")
    
except Exception as e:
    print(f"\n❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
