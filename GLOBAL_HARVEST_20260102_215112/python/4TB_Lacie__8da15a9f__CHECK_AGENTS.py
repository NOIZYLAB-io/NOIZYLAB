#!/usr/bin/env python3
"""
Check for running agents and processes
"""

import subprocess
import json
import os
from pathlib import Path

def check_processes():
    """Check for running agent-related processes"""
    print("🔍 Checking for running agents/processes...\n")
    
    # Check Python processes
    try:
        result = subprocess.run(
            ['ps', 'aux'], 
            capture_output=True, 
            text=True
        )
        
        lines = result.stdout.split('\n')
        
        # Look for agent-related processes
        agents = []
        python_procs = []
        
        for line in lines:
            if 'python' in line.lower():
                python_procs.append(line)
            
            # Check for agent keywords
            keywords = ['gabriel', 'mc96', 'agent', 'organizer', 'cleanup', 'analyzer']
            if any(kw in line.lower() for kw in keywords):
                agents.append(line)
        
        if agents:
            print("🤖 Agent-related processes found:")
            print("-" * 80)
            for proc in agents[:10]:
                print(f"  {proc}")
        else:
            print("✓ No agent processes running")
        
        if python_procs:
            print(f"\n🐍 Python processes: {len(python_procs)}")
            for proc in python_procs[:5]:
                parts = proc.split()
                if len(parts) > 10:
                    cpu = parts[2]
                    mem = parts[3]
                    cmd = ' '.join(parts[10:])
                    print(f"  CPU: {cpu}% | MEM: {mem}% | {cmd[:60]}...")
    
    except Exception as e:
        print(f"Error checking processes: {e}")

def check_noizylab_agents():
    """Check for agent scripts in NOIZYLAB"""
    noizylab = Path("/Users/m2ultra/NOIZYLAB")
    
    print("\n📁 Agent scripts in NOIZYLAB:\n")
    
    agent_files = []
    # pathlib doesn't support brace expansion, so use multiple patterns
    # Use set to avoid duplicates if file matches multiple patterns
    seen_files = set()
    patterns = ['*.py', '*.js', '*.mjs', '*.sh']
    for pattern in patterns:
        for file in noizylab.rglob(pattern):
            if file not in seen_files:
                seen_files.add(file)
                if any(keyword in file.name.lower() for keyword in ['agent', 'gabriel', 'mc96', 'organizer']):
                    agent_files.append(file)
    
    if agent_files:
        for agent in sorted(agent_files)[:20]:
            size = agent.stat().st_size / 1024  # KB
            print(f"  {agent.name:40s} ({size:.1f} KB) → {agent.parent.name}/")
    else:
        print("  No agent scripts found")

def check_system_resources():
    """Check system resources"""
    print("\n💻 System Resources:\n")
    
    try:
        # CPU usage
        result = subprocess.run(
            ['top', '-l', '1', '-n', '10'],
            capture_output=True,
            text=True,
            timeout=5
        )
        print("Top processes by CPU:")
        for line in result.stdout.split('\n')[:15]:
            if line.strip() and '%CPU' not in line and 'PID' not in line:
                print(f"  {line[:80]}")
    except:
        print("  Could not check system resources")

def main():
    print("=" * 80)
    print(" " * 25 + "AGENT STATUS CHECK")
    print("=" * 80)
    
    check_processes()
    check_noizylab_agents()
    check_system_resources()
    
    print("\n" + "=" * 80)
    print("✅ Check complete")
    print("=" * 80)
    
    print("\n💡 To speed things up:")
    print("  1. Close unnecessary processes")
    print("  2. Run: python3 /Users/m2ultra/NOIZYLAB/QUICK_ORGANIZE.py")
    print("  3. Avoid heavy scanning operations")

if __name__ == "__main__":
    main()

