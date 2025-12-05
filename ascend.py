#!/usr/bin/env python3
"""
⚡️ ASCENSION 6 — SYSTEM-WIDE OVERRIDE SWITCH
Single script to activate ASCENSION MODE
Fish Music Inc - CB_01
⭐️🔥 GORUNFREE! 🎸🔥

Usage:
    python3 scripts/ascend.py                    # Default ascension
    python3 scripts/ascend.py "MISSION_NAME"    # Named mission
    python3 scripts/ascend.py --status          # Check status
    python3 scripts/ascend.py --descend         # Exit ascension
"""

import sys
import os

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ascension.mission import MissionProtocol


def main():
    mp = MissionProtocol()
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg == "--status":
            print(mp.status())
            print(f"\nFull state: {mp.get()}")
            return
        
        elif arg == "--descend":
            mp.disable_autoallow()
            print("🛑 DESCENDED - Ascension mode deactivated")
            return
        
        elif arg == "--help":
            print(__doc__)
            return
        
        else:
            # Custom mission name
            mission_name = arg
    else:
        mission_name = "GLOBAL_SUPERSTAR_ASCEND"

    # ASCEND
    print()
    print("=" * 60)
    print("⭐️🔥 INITIATING ASCENSION PROTOCOL ⭐️🔥")
    print("=" * 60)
    print()
    
    mp.set_mission(mission_name)
    mp.enable_autoallow()
    
    print()
    print("╔════════════════════════════════════════════════════════╗")
    print("║                                                        ║")
    print("║        🌌 ASCENSION MODE ACTIVATED 🌌                  ║")
    print("║                                                        ║")
    print("║   All systems are now in AUTOALLOW mode.              ║")
    print("║   Every agent, module, and AI has permission          ║")
    print("║   to execute without friction or blockers.            ║")
    print("║                                                        ║")
    print(f"║   Mission: {mission_name:<43} ║")
    print("║                                                        ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    print("🔥 GORUNFREE! 🎸🔥")
    print()


if __name__ == "__main__":
    main()
