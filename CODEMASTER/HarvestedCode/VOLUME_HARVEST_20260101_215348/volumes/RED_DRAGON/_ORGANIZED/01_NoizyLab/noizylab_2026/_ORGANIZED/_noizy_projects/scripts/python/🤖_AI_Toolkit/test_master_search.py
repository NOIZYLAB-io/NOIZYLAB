#!/usr/bin/env python3
"""
Quick Master Search Test
"""

import sys
import os
from pathlib import Path

# Add the toolkit directory to path
toolkit_dir = Path(__file__).parent.parent
sys.path.append(str(toolkit_dir / "00_Master_Search"))

from master_search import MasterSearchSystem

def test_master_search():
    """Test the master search system"""
    try:
        # Initialize the system
        print("🤖 Initializing Master Search System...")
        master_search = MasterSearchSystem()
        
        # Test tool discovery
        print(f"📦 Discovered {len(master_search.tools)} tools")
        print(f"🤖 Discovered {len(master_search.agents)} agents")
        
        # Test simple search
        print("\n🔍 Testing search for 'music'...")
        tool_results = master_search.search_tools("music")
        agent_results = master_search.search_agents("music")
        
        print(f"Found {len(tool_results)} relevant tools")
        print(f"Found {len(agent_results)} relevant agents")
        
        if tool_results:
            print(f"Top tool: {tool_results[0]['name']}")
        
        if agent_results:
            print(f"Top agent: {agent_results[0]['name']}")
        
        # Test status
        print("\n📊 Getting system status...")
        status = master_search.get_tool_status()
        available_tools = sum(1 for tool in status["tools"].values() if tool["available"])
        print(f"Available tools: {available_tools}/{len(status['tools'])}")
        
        print("\n✅ Master Search System working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_master_search()