#!/usr/bin/env python3
"""🔥 IGNITE A NEW AEON"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aeon import AeonFire

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "PRIMORDIAL"
    theme = sys.argv[2] if len(sys.argv) > 2 else "cosmic genesis"
    
    print(f"🜂 IGNITING AEON: {name}")
    print(f"   Theme: {theme}")
    print()
    
    fire = AeonFire()
    result = fire.spark(name, theme)
    
    print(f"✅ AEON SPARKED: {result}")
    print()
    print("🔥 GORUNFREE! 🎸🔥")

if __name__ == "__main__":
    main()
