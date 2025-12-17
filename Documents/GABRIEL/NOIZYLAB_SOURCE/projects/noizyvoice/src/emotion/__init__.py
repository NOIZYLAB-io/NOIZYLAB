"""Emotion Detection & Control Module"""
from .detector import EmotionDetector
from .tags import AudioTagParser
from .prosody import ProsodyController

__all__ = ["EmotionDetector", "AudioTagParser", "ProsodyController"]