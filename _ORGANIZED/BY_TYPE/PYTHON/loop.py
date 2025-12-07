#!/usr/bin/env python3
import time
class CelestialLoop:
    def __init__(self):
        from celestial.orbit import OrbitEngine
        from celestial.awareness import OmnipresentAwareness
        self.orbit = OrbitEngine()
        self.aware = OmnipresentAwareness()
    def run(self):
        while True:
            print("✨ CELESTIAL:", self.orbit.align())
            print("🌐 NODES:", self.aware.probe())
            time.sleep(120)
    def pulse(self):
        return {"orbit": self.orbit.align(), "nodes": self.aware.probe()}
