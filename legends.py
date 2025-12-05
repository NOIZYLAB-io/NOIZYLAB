#!/usr/bin/env python3
"""🜃 MYTHOS 4 — LEGEND FORGE"""

class AIEngine:
    def ask(self, prompt): return f"[Legend] {prompt[:100]}..."

class LegendForge:
    def __init__(self):
        self.ai = AIEngine()
    def forge(self, figure_name):
        return self.ai.ask(f"Forge MYTHIC LEGEND for hero: {figure_name}")
    def epic(self, realm_name):
        return self.ai.ask(f"Create epic saga for realm: {realm_name}")
