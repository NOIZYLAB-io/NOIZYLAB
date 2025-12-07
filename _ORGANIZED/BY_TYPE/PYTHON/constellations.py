#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

class ConstellationMemory:
    FILE = Path(__file__).parent / "memory.json"
    def __init__(self):
        self.FILE.parent.mkdir(parents=True, exist_ok=True)
        if not self.FILE.exists():
            self.FILE.write_text(json.dumps({"constellations": []}, indent=2))
    def add(self, insight):
        data = json.loads(self.FILE.read_text())
        data["constellations"].append({"insight": insight, "ts": datetime.now().isoformat()})
        self.FILE.write_text(json.dumps(data, indent=2))
    def retrieve(self):
        return json.loads(self.FILE.read_text())["constellations"]
