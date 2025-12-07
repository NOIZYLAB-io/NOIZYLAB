#!/usr/bin/env python3
"""🜂 MYTHOS 2 — THE PRIMAL STORY ENGINE"""

class AIEngine:
    def ask(self, prompt): return f"[PrimalStory] {prompt[:100]}..."

class PrimalStory:
    def __init__(self):
        self.ai = AIEngine()
    def origin(self):
        return self.ai.ask("Write PRIMAL ORIGIN MYTH: First Sound, Shattering of Silence, birth of Pantheon")
    def creation_myth(self, realm_name):
        return self.ai.ask(f"Write creation myth for realm: {realm_name}")
