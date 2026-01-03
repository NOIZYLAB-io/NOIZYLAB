#!/usr/bin/env python3
"""
MC96 ECOUNIVERSE - Quick Start
Run from repository root: python mc96.py

This is a convenience wrapper that imports the main MC96 module
from GABRIEL_UNIFIED/core/mc96.py
"""

import sys
from pathlib import Path

# Add GABRIEL_UNIFIED/core to path
core_path = Path(__file__).parent / "GABRIEL_UNIFIED" / "core"
sys.path.insert(0, str(core_path))

if __name__ == "__main__":
    from mc96 import main
    import asyncio
    asyncio.run(main())
