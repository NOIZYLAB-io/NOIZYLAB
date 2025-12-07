#!/usr/bin/env python3
"""🜁 MYTHOS 1 — THE PANTHEON REGISTRY"""
import json
from pathlib import Path

class AIEngine:
    def ask(self, prompt): return f"[Pantheon] {prompt[:100]}..."

class Pantheon:
    FILE = Path(__file__).parent / "pantheon.json"
    def __init__(self):
        self.ai = AIEngine()
        self.FILE.parent.mkdir(parents=True, exist_ok=True)
        if not self.FILE.exists():
            self.FILE.write_text(json.dumps({"gods": []}, indent=2))
    def create_god(self, domain):
        god = self.ai.ask(f"Create MYTHIC DEITY for domain: {domain}")
        data = json.loads(self.FILE.read_text())
        data["gods"].append({"domain": domain, "god": god})
        self.FILE.write_text(json.dumps(data, indent=2))
        return god
    def list_gods(self):
        return json.loads(self.FILE.read_text())["gods"]
