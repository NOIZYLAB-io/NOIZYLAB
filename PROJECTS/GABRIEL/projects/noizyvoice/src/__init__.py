"""
NOIZYVOICE - Next-Gen Voice AI Platform
Better Than ElevenLabs - Open Source Foundation

GABRIEL ALMEIDA - NOIZYLAB
MC96ECOUNIVERSE
"""

__version__ = "0.1.0"
__author__ = "GABRIEL ALMEIDA"
__license__ = "Apache-2.0"

from .server import app
from .tts.engine import TTSEngine
from .voice.clone import VoiceCloner
from .voice.manager import VoiceManager

__all__ = [
    "app",
    "TTSEngine",
    "VoiceCloner",
    "VoiceManager",
]