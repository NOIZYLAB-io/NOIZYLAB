#!/usr/bin/env python3
"""
Execute Master Process - Runs from anywhere
"""

import os
import subprocess
from pathlib import Path

PROJECT_DIR = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/_noizy_projects")
PROCESSOR = PROJECT_DIR / "PROJECT_MASTER_PROCESSOR.py"

def execute():
    """Execute the master process"""
    print("🚀 EXECUTING MASTER PROCESS")
    print("=" * 80)
    print()
    
    if not PROJECT_DIR.exists():
        print(f"❌ Project directory not found: {PROJECT_DIR}")
        return
    
    if not PROCESSOR.exists():
        print(f"❌ Processor not found: {PROCESSOR}")
        return
    
    print(f"✅ Found processor: {PROCESSOR}")
    print()
    
    # Change to directory and execute
    os.chdir(str(PROJECT_DIR))
    
    # Execute processor
    print("📡 Starting master process...")
    print()
    
    import sys
    sys.path.insert(0, str(PROJECT_DIR))
    
    # Import and run
    import importlib.util
    spec = importlib.util.spec_from_file_location("processor", PROCESSOR)
    processor_module = importlib.util.module_from_spec(spec)
    
    # Run it
    spec.loader.exec_module(processor_module)
    
    # Call main with --live
    import sys
    original_argv = sys.argv
    sys.argv = ['PROJECT_MASTER_PROCESSOR.py', '--live']
    
    try:
        processor_module.main()
    finally:
        sys.argv = original_argv

if __name__ == "__main__":
    execute()

