#!/usr/bin/env python3
class OrbitEngine:
    def __init__(self):
        from celestial.starmind import StarMind
        from celestial.chrono import ChronoEngine
        from celestial.constellations import ConstellationMemory
        self.starmind = StarMind()
        self.chrono = ChronoEngine()
        self.memory = ConstellationMemory()
    def align(self):
        snapshot = self.starmind.summarize()
        futures = self.chrono.predict({"snapshot": snapshot})
        self.memory.add(str(futures))
        return {"snapshot": snapshot, "futures": futures}
