#!/usr/bin/env python3
"""🌍 FORGE A NEW REALM"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from realmforge import RealmManager

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "NOIZYREALM"
    theme = sys.argv[2] if len(sys.argv) > 2 else "epic dark electronic"
    
    print(f"🌍 FORGING REALM: {name}")
    print(f"   Theme: {theme}")
    print()
    
    rm = RealmManager()
    realm = rm.create_realm(name, theme)
    
    print(f"✅ REALM FORGED: {realm}")
    print()
    print("🔥 GORUNFREE! 🎸🔥")

if __name__ == "__main__":
    main()
