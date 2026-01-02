from __future__ import annotations
from .registry import register
from .base import BaseAgent

@register("agent_client_portal")
class AgentClientPortal(BaseAgent):
    """Listens for new client uploads and decides action."""
    def step(self):
        events = self.bus.fetch("client_intake")
        if not events: return
        for e in events[-5:]:
            data = e["payload"]
            diag = data.get("diagnostic_code", "")
            print(f"[Client Upload] {data.get('client')} -> {diag}")