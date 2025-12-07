#!/usr/bin/env python3
"""
🟣 ASCENSION 1 — Universal Mission Declaration Protocol
Defines a mission, and every agent subscribes to it
Fish Music Inc - CB_01
⭐️🔥 GORUNFREE! 🎸🔥
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional


class MissionProtocol:
    """Universal mission declaration - the anchor for all systems"""

    FILE = Path(__file__).parent / "current_mission.json"

    def __init__(self):
        self.FILE.parent.mkdir(parents=True, exist_ok=True)
        if not self.FILE.exists():
            self.FILE.write_text(json.dumps({
                "mission": None,
                "auto_allow": False,
                "created": None,
                "activated": None
            }, indent=2))

    def set_mission(self, name: str, description: str = None) -> Dict:
        """Declare a new mission"""
        data = {
            "mission": name,
            "description": description,
            "auto_allow": False,
            "created": datetime.now().isoformat(),
            "activated": None
        }
        self.FILE.write_text(json.dumps(data, indent=2))
        print(f"🎯 MISSION SET: {name}")
        return data

    def enable_autoallow(self) -> Dict:
        """Enable AUTOALLOW - greenlight everything"""
        data = json.loads(self.FILE.read_text())
        data["auto_allow"] = True
        data["activated"] = datetime.now().isoformat()
        self.FILE.write_text(json.dumps(data, indent=2))
        print("⭐️🔥 AUTOALLOW ENABLED - ALL SYSTEMS GO!")
        return data

    def disable_autoallow(self) -> Dict:
        """Disable AUTOALLOW"""
        data = json.loads(self.FILE.read_text())
        data["auto_allow"] = False
        self.FILE.write_text(json.dumps(data, indent=2))
        print("🛑 AUTOALLOW DISABLED")
        return data

    def get(self) -> Dict:
        """Get current mission state"""
        return json.loads(self.FILE.read_text())

    def clear(self) -> Dict:
        """Clear mission"""
        data = {
            "mission": None,
            "auto_allow": False,
            "created": None,
            "activated": None
        }
        self.FILE.write_text(json.dumps(data, indent=2))
        return data

    def is_active(self) -> bool:
        """Check if mission is active with autoallow"""
        data = self.get()
        return data["mission"] is not None and data["auto_allow"] == True

    def status(self) -> str:
        """Get mission status string"""
        data = self.get()
        if data["auto_allow"]:
            return f"⭐️🔥 ASCENSION ACTIVE: {data['mission']}"
        elif data["mission"]:
            return f"🎯 MISSION SET (not ascended): {data['mission']}"
        else:
            return "⚪ NO ACTIVE MISSION"


if __name__ == "__main__":
    mp = MissionProtocol()
    print(mp.status())
    print(f"Current: {mp.get()}")
