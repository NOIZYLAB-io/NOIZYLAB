from __future__ import annotations
import os, subprocess, time
from .registry import register
from .base import BaseAgent

@register("agent04_audio_ops")
class AgentAudioOps(BaseAgent):
    """Audio system operations and monitoring agent."""
    
    def step(self):
        audio_status = {
            "timestamp": time.time(),
            "coreaudio_running": self._check_coreaudio(),
            "elevenlabs_ready": bool(os.getenv("ELEVENLABS_API_KEY")),
            "status": "ready"
        }
        
        self.bus.publish("audio_ops", audio_status)
    
    def _check_coreaudio(self) -> bool:
        """Check if CoreAudio daemon is running (macOS)"""
        try:
            result = subprocess.run(['pgrep', 'coreaudiod'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False