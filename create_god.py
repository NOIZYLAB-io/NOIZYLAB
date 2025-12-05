#!/usr/bin/env python3
"""🜁 CREATE A DEITY"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mythos import Pantheon

def main():
    domain = sys.argv[1] if len(sys.argv) > 1 else "music"
    
    print(f"🜁 CREATING DEITY OF: {domain}")
    print()
    
    pantheon = Pantheon()
    god = pantheon.create_god(domain)
    
    print(f"✅ DEITY CREATED: {god}")
    print()
    print("🔥 GORUNFREE! 🎸🔥")

if __name__ == "__main__":
    main()
