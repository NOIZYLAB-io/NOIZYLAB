#!/usr/bin/env python3
"""
Cloud Agent Delegation Script
Delegates tasks to cloud-based agents via Cloudflare Worker
"""

import json
import sys
import argparse
from typing import Optional, Dict, Any
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)

# Load registry configuration
REGISTRY_PATH = Path(__file__).parent / "registry.json"

def load_registry() -> Dict[str, Any]:
    """Load the agent registry configuration"""
    with open(REGISTRY_PATH, 'r') as f:
        return json.load(f)

def delegate_to_cloud(agent: str, action: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Delegate a task to a cloud agent
    
    Args:
        agent: Agent name (gabriel, mc96, systemGuardian)
        action: Action to perform
        params: Optional parameters for the action
        
    Returns:
        Response from the cloud agent
    """
    registry = load_registry()
    
    if not registry.get('cloud', {}).get('enabled'):
        return {
            'success': False,
            'error': 'Cloud delegation is not enabled in registry'
        }
    
    endpoint = registry['cloud']['endpoint']
    delegate_path = registry['cloud']['endpoints']['delegate']
    url = f"{endpoint}{delegate_path}"
    
    payload = {
        'agent': agent,
        'action': action,
        'params': params or {}
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'Request failed: {str(e)}'
        }

def list_cloud_agents() -> Dict[str, Any]:
    """List available cloud agents"""
    registry = load_registry()
    
    if not registry.get('cloud', {}).get('enabled'):
        return {
            'success': False,
            'error': 'Cloud delegation is not enabled'
        }
    
    endpoint = registry['cloud']['endpoint']
    list_path = registry['cloud']['endpoints']['list']
    url = f"{endpoint}{list_path}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'Request failed: {str(e)}'
        }

def check_cloud_health() -> Dict[str, Any]:
    """Check cloud worker health"""
    registry = load_registry()
    
    if not registry.get('cloud', {}).get('enabled'):
        return {
            'success': False,
            'error': 'Cloud delegation is not enabled'
        }
    
    endpoint = registry['cloud']['endpoint']
    health_path = registry['cloud']['endpoints']['health']
    url = f"{endpoint}{health_path}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'Request failed: {str(e)}'
        }

def main():
    parser = argparse.ArgumentParser(
        description='Delegate tasks to cloud-based NOIZYLAB agents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check cloud health
  %(prog)s --health
  
  # List available cloud agents
  %(prog)s --list
  
  # Delegate to SystemGuardian
  %(prog)s --agent systemGuardian --action status
  
  # Delegate to MC96 with parameters
  %(prog)s --agent mc96 --action organize --params '{"path": "/data"}'
  
  # Delegate to GABRIEL
  %(prog)s --agent gabriel --action health
        """
    )
    
    parser.add_argument('--health', action='store_true', 
                       help='Check cloud worker health')
    parser.add_argument('--list', action='store_true',
                       help='List available cloud agents')
    parser.add_argument('--agent', type=str,
                       help='Agent to delegate to (gabriel, mc96, systemGuardian)')
    parser.add_argument('--action', type=str,
                       help='Action to perform')
    parser.add_argument('--params', type=str,
                       help='JSON parameters for the action')
    
    args = parser.parse_args()
    
    # Check health
    if args.health:
        result = check_cloud_health()
        print(json.dumps(result, indent=2))
        sys.exit(0 if result.get('status') == 'ok' else 1)
    
    # List agents
    if args.list:
        result = list_cloud_agents()
        print(json.dumps(result, indent=2))
        sys.exit(0 if 'agents' in result else 1)
    
    # Delegate to agent
    if args.agent and args.action:
        params = None
        if args.params:
            try:
                params = json.loads(args.params)
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON parameters: {e}")
                sys.exit(1)
        
        result = delegate_to_cloud(args.agent, args.action, params)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result.get('success') else 1)
    
    # No valid command
    parser.print_help()
    sys.exit(1)

if __name__ == '__main__':
    main()
