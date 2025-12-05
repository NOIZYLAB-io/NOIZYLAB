#!/usr/bin/env python3
"""🔥 AEON 2 — ERA FORGE (Nested Time-Layers)"""
import json
from pathlib import Path
from datetime import datetime

class EraForge:
    FILE = Path(__file__).parent / "aeons.json"
    def forge_era(self, aeon_name, description):
        data = json.loads(self.FILE.read_text())
        for aeon in data["aeons"]:
            if aeon["name"] == aeon_name:
                aeon["eras"].append({
                    "description": description,
                    "artifacts": [],
                    "events": [],
                    "pantheon_shift": None,
                    "forged": datetime.now().isoformat()
                })
        self.FILE.write_text(json.dumps(data, indent=2))
        return data
    def list_eras(self, aeon_name):
        data = json.loads(self.FILE.read_text())
        for aeon in data["aeons"]:
            if aeon["name"] == aeon_name:
                return aeon.get("eras", [])
        return []
