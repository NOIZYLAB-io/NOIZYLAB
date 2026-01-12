#!/usr/bin/env python3
"""
TitanHive Voice Module - GABRIEL's Advanced Voice Processing System
===================================================================

Multi-provider voice synthesis and transcription with AI integration.

Features:
- OpenAI Whisper transcription
- Multiple TTS providers (Azure, Google, Edge, gTTS)
- AI-powered responses (Gemini, OpenAI)
- Emotion detection
- Professional audio mastering

Usage:
    python3 voice.py master "Hello world"    # Master voice
    python3 voice.py realtime "Hello world"  # Low latency
    python3 voice.py transcribe audio.wav    # Transcribe audio
"""

from __future__ import annotations

import os
import sys
import json
import logging
import subprocess
import tempfile
import asyncio
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Union,
    Tuple,
)
from dataclasses import dataclass, field
from enum import Enum, auto
from abc import ABC, abstractmethod
import threading
from queue import Queue, Empty
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("TitanHive.Voice")

# =============================================================================
# Optional Dependencies with Graceful Fallbacks
# =============================================================================

# Whisper (OpenAI's speech-to-text)
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    whisper = None  # type: ignore
    WHISPER_AVAILABLE = False
    logger.debug("Whisper not available - install with: pip install openai-whisper")

# Pydub (audio processing)
try:
    from pydub import AudioSegment
    from pydub.effects import normalize, compress_dynamic_range
    PYDUB_AVAILABLE = True
except ImportError:
    AudioSegment = None  # type: ignore
    normalize = None  # type: ignore
    compress_dynamic_range = None  # type: ignore
    PYDUB_AVAILABLE = False
    logger.debug("Pydub not available - install with: pip install pydub")

# Google Cloud TTS
try:
    from google.cloud import texttospeech
    GOOGLE_TTS_AVAILABLE = True
except ImportError:
    texttospeech = None  # type: ignore
    GOOGLE_TTS_AVAILABLE = False
    logger.debug("Google Cloud TTS not available")

# Azure Cognitive Services
try:
    import azure.cognitiveservices.speech as speechsdk
    AZURE_TTS_AVAILABLE = True
except ImportError:
    speechsdk = None  # type: ignore
    AZURE_TTS_AVAILABLE = False
    logger.debug("Azure TTS not available")

# gTTS (Google Text-to-Speech - free)
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    gTTS = None  # type: ignore
    GTTS_AVAILABLE = False
    logger.debug("gTTS not available - install with: pip install gtts")

# OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OpenAI = None  # type: ignore
    OPENAI_AVAILABLE = False
    logger.debug("OpenAI not available - install with: pip install openai")

# Google Generative AI (Gemini)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    genai = None  # type: ignore
    GEMINI_AVAILABLE = False
    logger.debug("Google Generative AI not available - install with: pip install google-generativeai")

# Edge TTS
try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    edge_tts = None  # type: ignore
    EDGE_TTS_AVAILABLE = False
    logger.debug("Edge TTS not available - install with: pip install edge-tts")

# Requests
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None  # type: ignore
    REQUESTS_AVAILABLE = False


# =============================================================================
# Enums and Constants
# =============================================================================

class TTSProvider(Enum):
    """Supported TTS providers"""
    AZURE = auto()
    GOOGLE = auto()
    EDGE = auto()
    GTTS = auto()
    OPENAI = auto()
    LOCAL = auto()


class VoiceStyle(Enum):
    """Voice styles for synthesis"""
    NEUTRAL = "neutral"
    CHEERFUL = "cheerful"
    SAD = "sad"
    ANGRY = "angry"
    FEARFUL = "fearful"
    WHISPERING = "whispering"
    SHOUTING = "shouting"


class Emotion(Enum):
    """Detected emotions"""
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    FEARFUL = "fearful"
    SURPRISED = "surprised"
    DISGUSTED = "disgusted"


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class VoiceConfig:
    """Voice configuration settings"""
    name: str = "en-US-JennyNeural"
    rate: float = 1.0
    pitch: float = 0.0
    volume: float = 1.0
    style: VoiceStyle = VoiceStyle.NEUTRAL


@dataclass
class TranscriptionResult:
    """Result of speech-to-text transcription"""
    text: str
    language: str = "en"
    confidence: float = 1.0
    segments: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class ConversationTurn:
    """Single turn in a conversation"""
    text: str
    is_user: bool
    emotion: Optional[str] = None
    timestamp: float = field(default_factory=time.time)


# =============================================================================
# Audio Processing
# =============================================================================

class AudioProcessor:
    """Audio processing utilities using pydub"""
    
    @staticmethod
    def normalize_audio(audio_path: str, output_path: Optional[str] = None) -> str:
        """Normalize audio levels"""
        if not PYDUB_AVAILABLE or AudioSegment is None or normalize is None:
            logger.warning("Pydub not available, returning original audio")
            return audio_path
        
        try:
            audio = AudioSegment.from_file(audio_path)
            normalized = normalize(audio)
            out_path = output_path or audio_path.replace('.', '_normalized.')
            normalized.export(out_path, format=Path(out_path).suffix[1:])
            return out_path
        except Exception as e:
            logger.error(f"Normalization failed: {e}")
            return audio_path
    
    @staticmethod
    def enhance_voice(audio_path: str, output_path: Optional[str] = None) -> str:
        """Enhance voice audio with compression and normalization"""
        if not PYDUB_AVAILABLE or AudioSegment is None:
            logger.warning("Pydub not available, returning original audio")
            return audio_path
        
        try:
            audio = AudioSegment.from_file(audio_path)
            if normalize is not None:
                audio = normalize(audio)
            if compress_dynamic_range is not None:
                audio = compress_dynamic_range(audio, threshold=-20.0, ratio=4.0)
            out_path = output_path or audio_path.replace('.', '_enhanced.')
            audio.export(out_path, format=Path(out_path).suffix[1:])
            return out_path
        except Exception as e:
            logger.error(f"Enhancement failed: {e}")
            return audio_path
    
    @staticmethod
    def apply_professional_master(audio_path: str, output_path: Optional[str] = None) -> str:
        """Apply professional-grade mastering to audio"""
        # Use ffmpeg for more advanced processing
        out_path = output_path or audio_path.replace('.', '_mastered.')
        
        try:
            cmd = [
                'ffmpeg', '-y', '-i', audio_path,
                '-af', 'loudnorm=I=-16:LRA=11:TP=-1.5',
                out_path
            ]
            subprocess.run(cmd, capture_output=True, check=True)
            return out_path
        except Exception as e:
            logger.error(f"Mastering failed: {e}")
            return audio_path


# =============================================================================
# Transcription (Speech-to-Text)
# =============================================================================

class WhisperTranscriber:
    """OpenAI Whisper speech-to-text"""
    
    def __init__(self, model_size: str = "base"):
        self.model_size = model_size
        self._model: Any = None
    
    @property
    def model(self) -> Any:
        """Lazy load the whisper model"""
        if self._model is None:
            if not WHISPER_AVAILABLE or whisper is None:
                raise RuntimeError("Whisper not available - install with: pip install openai-whisper")
            self._model = whisper.load_model(self.model_size)
        return self._model
    
    def transcribe(self, audio_path: str, language: Optional[str] = None) -> TranscriptionResult:
        """Transcribe audio file to text"""
        try:
            model = self.model
            if model is None:
                return TranscriptionResult(text="[Whisper model not loaded]", language="en")
            
            result = model.transcribe(audio_path, language=language)
            return TranscriptionResult(
                text=result.get("text", "").strip(),
                language=result.get("language", "en"),
                segments=result.get("segments", [])
            )
        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            return TranscriptionResult(text=f"[Error: {e}]", language="en")
    
    def transcribe_realtime(
        self, 
        audio_path: str, 
        callback: Optional[Callable[[str], None]] = None
    ) -> str:
        """Transcribe with real-time segment callbacks"""
        try:
            model = self.model
            if model is None:
                return "[Whisper model not loaded]"
            
            result = model.transcribe(audio_path, verbose=False)
            full_text = ""
            
            for segment in result.get("segments", []):
                text = segment.get("text", "").strip()
                full_text += text + " "
                if callback:
                    callback(text)
            
            return full_text.strip()
        except Exception as e:
            logger.error(f"Realtime transcription failed: {e}")
            return f"[Error: {e}]"


# =============================================================================
# AI Integration
# =============================================================================

class GeminiAssistant:
    """Google Gemini AI assistant for voice responses"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self._client: Any = None
        self._model: Any = None
    
    @property
    def client(self) -> Any:
        """Lazy load Gemini client"""
        if self._client is None:
            if not GEMINI_AVAILABLE or genai is None:
                raise RuntimeError("Google Generative AI not available")
            
            if self.api_key:
                genai.configure(api_key=self.api_key)
            
            # Use the correct API for google-generativeai
            self._model = genai.GenerativeModel('gemini-1.5-flash')
            self._client = self._model
        
        return self._client
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate AI response to a prompt"""
        try:
            client = self.client
            if client is None:
                return "[Gemini not configured]"
            
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            response = client.generate_content(full_prompt)
            
            # Handle response text
            if hasattr(response, 'text') and response.text:
                return response.text.strip()
            return "[No response generated]"
            
        except Exception as e:
            logger.error(f"Gemini generation failed: {e}")
            return f"[Error: {e}]"
    
    def generate_greeting(self, time_of_day: Optional[str] = None) -> str:
        """Generate a personalized greeting"""
        if time_of_day is None:
            import datetime
            hour = datetime.datetime.now().hour
            if hour < 12:
                time_of_day = "morning"
            elif hour < 17:
                time_of_day = "afternoon"
            else:
                time_of_day = "evening"
        
        prompt = f"Generate a brief, friendly {time_of_day} greeting in one sentence."
        return self.generate_response(prompt)


class OpenAIAssistant:
    """OpenAI GPT assistant for voice responses"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o-mini"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self._client: Any = None
    
    @property
    def client(self) -> Any:
        """Lazy load OpenAI client"""
        if self._client is None:
            if not OPENAI_AVAILABLE or OpenAI is None:
                raise RuntimeError("OpenAI not available - install with: pip install openai")
            self._client = OpenAI(api_key=self.api_key)
        return self._client
    
    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate AI response using OpenAI"""
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            logger.error(f"OpenAI generation failed: {e}")
            return f"[Error: {e}]"


# =============================================================================
# Emotion Detection
# =============================================================================

class EmotionDetector:
    """Simple rule-based emotion detection from text"""
    
    EMOTION_KEYWORDS: Dict[Emotion, List[str]] = {
        Emotion.HAPPY: ["happy", "joy", "excited", "wonderful", "great", "amazing", "love", "fantastic"],
        Emotion.SAD: ["sad", "unhappy", "depressed", "sorry", "miss", "lonely", "crying", "tears"],
        Emotion.ANGRY: ["angry", "mad", "furious", "hate", "annoyed", "frustrated", "rage"],
        Emotion.FEARFUL: ["scared", "afraid", "fear", "terrified", "worried", "anxious", "nervous"],
        Emotion.SURPRISED: ["surprised", "wow", "shocked", "unexpected", "amazing", "unbelievable"],
        Emotion.DISGUSTED: ["disgusted", "gross", "awful", "terrible", "horrible", "sick"],
    }
    
    @classmethod
    def detect(cls, text: str) -> Dict[str, Any]:
        """Detect emotion from text"""
        text_lower = text.lower()
        scores: Dict[str, float] = {}
        
        for emotion, keywords in cls.EMOTION_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            if score > 0:
                scores[emotion.value] = float(score)
        
        if scores:
            # Find emotion with highest score
            emotion_name = max(scores.keys(), key=lambda k: scores[k])
            return {
                "emotion": emotion_name,
                "confidence": min(1.0, scores[emotion_name] / 3),
                "scores": scores
            }
        
        return {
            "emotion": Emotion.NEUTRAL.value,
            "confidence": 0.5,
            "scores": {"neutral": 1.0}
        }


# =============================================================================
# Conversation Manager
# =============================================================================

class ConversationManager:
    """Manage conversation history with emotion tracking"""
    
    def __init__(self, max_history: int = 100):
        self.history: List[ConversationTurn] = []
        self.max_history = max_history
    
    def add(self, text: str, is_user: bool, emotion: Optional[str] = None) -> None:
        """Add a turn to the conversation"""
        if emotion is None:
            emotion = EmotionDetector.detect(text).get("emotion", "neutral")
        
        turn = ConversationTurn(
            text=text,
            is_user=is_user,
            emotion=emotion
        )
        self.history.append(turn)
        
        # Trim history if needed
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
    
    def get_context(self, num_turns: int = 5) -> str:
        """Get recent conversation context as string"""
        recent = self.history[-num_turns:]
        lines = []
        for turn in recent:
            role = "User" if turn.is_user else "Assistant"
            lines.append(f"{role}: {turn.text}")
        return "\n".join(lines)
    
    def clear(self) -> None:
        """Clear conversation history"""
        self.history.clear()


# =============================================================================
# Text-to-Speech Providers
# =============================================================================

class BaseTTSProvider(ABC):
    """Abstract base class for TTS providers"""
    
    @abstractmethod
    def synthesize(self, text: str, output_path: str, voice_config: Optional[VoiceConfig] = None) -> str:
        """Synthesize text to speech"""
        pass


class EdgeTTSProvider(BaseTTSProvider):
    """Microsoft Edge TTS provider (free)"""
    
    DEFAULT_VOICE = "en-US-JennyNeural"
    
    def synthesize(
        self, 
        text: str, 
        output_path: str, 
        voice_config: Optional[VoiceConfig] = None
    ) -> str:
        """Synthesize using Edge TTS"""
        if not EDGE_TTS_AVAILABLE or edge_tts is None:
            raise RuntimeError("Edge TTS not available - install with: pip install edge-tts")
        
        voice = voice_config.name if voice_config else self.DEFAULT_VOICE
        
        async def _synthesize():
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(output_path)
        
        asyncio.run(_synthesize())
        return output_path


class GTTSProvider(BaseTTSProvider):
    """Google Text-to-Speech provider (free)"""
    
    def synthesize(
        self, 
        text: str, 
        output_path: str, 
        voice_config: Optional[VoiceConfig] = None
    ) -> str:
        """Synthesize using gTTS"""
        if not GTTS_AVAILABLE or gTTS is None:
            raise RuntimeError("gTTS not available - install with: pip install gtts")
        
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)
        return output_path


class AzureTTSProvider(BaseTTSProvider):
    """Azure Cognitive Services TTS provider"""
    
    def __init__(self, subscription_key: Optional[str] = None, region: str = "eastus"):
        self.subscription_key = subscription_key or os.getenv("AZURE_SPEECH_KEY")
        self.region = region
    
    def synthesize(
        self, 
        text: str, 
        output_path: str, 
        voice_config: Optional[VoiceConfig] = None
    ) -> str:
        """Synthesize using Azure TTS"""
        if not AZURE_TTS_AVAILABLE or speechsdk is None:
            raise RuntimeError("Azure TTS not available")
        
        if not self.subscription_key:
            raise RuntimeError("Azure Speech subscription key not configured")
        
        speech_config = speechsdk.SpeechConfig(
            subscription=self.subscription_key,
            region=self.region
        )
        
        voice_name = voice_config.name if voice_config else "en-US-JennyNeural"
        speech_config.speech_synthesis_voice_name = voice_name
        
        audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config,
            audio_config=audio_config
        )
        
        result = synthesizer.speak_text_async(text).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return output_path
        else:
            raise RuntimeError(f"Azure TTS failed: {result.reason}")


# =============================================================================
# Audio Queue for Playback
# =============================================================================

class AudioQueue:
    """Thread-safe audio playback queue"""
    
    def __init__(self):
        self._queue: "Queue[str]" = Queue()
        self._playing = False
        self._thread: Optional[threading.Thread] = None
    
    def add(self, audio_path: str) -> None:
        """Add audio file to queue"""
        self._queue.put(audio_path)
        if not self._playing:
            self._start_playback()
    
    def _start_playback(self) -> None:
        """Start playback thread"""
        self._playing = True
        self._thread = threading.Thread(target=self._playback_loop, daemon=True)
        self._thread.start()
    
    def _playback_loop(self) -> None:
        """Main playback loop"""
        while True:
            try:
                audio_path = self._queue.get(timeout=1.0)
                self._play_audio(audio_path)
            except Empty:
                if self._queue.empty():
                    self._playing = False
                    break
    
    def _play_audio(self, audio_path: str) -> None:
        """Play audio file using system player"""
        try:
            if sys.platform == "darwin":
                subprocess.run(["afplay", audio_path], check=True)
            elif sys.platform == "linux":
                subprocess.run(["aplay", audio_path], check=True)
            elif sys.platform == "win32":
                import winsound
                winsound.PlaySound(audio_path, winsound.SND_FILENAME)
        except Exception as e:
            logger.error(f"Audio playback failed: {e}")


# =============================================================================
# Gruff British Engine (Custom Voice)
# =============================================================================

class GruffBritishEngine:
    """Custom gruff British voice using Edge TTS"""
    
    # British male voices available in Edge TTS
    VOICES = [
        "en-GB-RyanNeural",      # British male
        "en-GB-ThomasNeural",    # British male
        "en-AU-WilliamNeural",   # Australian male (deeper)
    ]
    
    def __init__(self, voice_index: int = 0):
        self.voice = self.VOICES[min(voice_index, len(self.VOICES) - 1)]
        self._provider = EdgeTTSProvider() if EDGE_TTS_AVAILABLE else None
    
    def synthesize(self, text: str, output_path: Optional[str] = None) -> str:
        """Synthesize with gruff British voice"""
        if self._provider is None:
            raise RuntimeError("Edge TTS not available for GruffBritishEngine")
        
        out_path = output_path or tempfile.mktemp(suffix=".mp3")
        voice_config = VoiceConfig(name=self.voice, rate=0.9, pitch=-2.0)
        
        return self._provider.synthesize(text, out_path, voice_config)


# =============================================================================
# Main Voice System
# =============================================================================

class VoiceSystem:
    """Main voice system coordinating all components"""
    
    def __init__(self):
        self.transcriber = WhisperTranscriber() if WHISPER_AVAILABLE else None
        self.gemini = GeminiAssistant() if GEMINI_AVAILABLE else None
        self.openai_assistant = OpenAIAssistant() if OPENAI_AVAILABLE else None
        self.conversation = ConversationManager()
        self.audio_queue = AudioQueue()
        
        # Select best available TTS
        self.tts: Optional[BaseTTSProvider] = None
        if EDGE_TTS_AVAILABLE:
            self.tts = EdgeTTSProvider()
        elif GTTS_AVAILABLE:
            self.tts = GTTSProvider()
        elif AZURE_TTS_AVAILABLE:
            self.tts = AzureTTSProvider()
    
    def speak(self, text: str, voice_config: Optional[VoiceConfig] = None) -> Optional[str]:
        """Convert text to speech and play"""
        if self.tts is None:
            logger.error("No TTS provider available")
            return None
        
        output_path = tempfile.mktemp(suffix=".mp3")
        try:
            result_path = self.tts.synthesize(text, output_path, voice_config)
            self.audio_queue.add(result_path)
            return result_path
        except Exception as e:
            logger.error(f"Speech synthesis failed: {e}")
            return None
    
    def transcribe(self, audio_path: str) -> TranscriptionResult:
        """Transcribe audio to text"""
        if self.transcriber is None:
            return TranscriptionResult(text="[Transcriber not available]")
        return self.transcriber.transcribe(audio_path)
    
    def chat(self, user_input: str) -> str:
        """Process user input and generate response"""
        self.conversation.add(user_input, is_user=True)
        
        # Get context
        context = self.conversation.get_context()
        
        # Generate response using available AI
        response = ""
        if self.gemini:
            response = self.gemini.generate_response(user_input, context)
        elif self.openai_assistant:
            response = self.openai_assistant.generate_response(user_input, context)
        else:
            response = f"I heard: {user_input}"
        
        self.conversation.add(response, is_user=False)
        return response
    
    def master_voice(self, text: str) -> Optional[str]:
        """Speak with professional mastered audio"""
        path = self.speak(text)
        if path:
            return AudioProcessor.apply_professional_master(path)
        return None


# =============================================================================
# CLI Interface
# =============================================================================

def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="TitanHive Voice System")
    parser.add_argument("command", choices=["speak", "master", "realtime", "transcribe", "chat"],
                        help="Command to execute")
    parser.add_argument("input", nargs="?", help="Text to speak or audio file to transcribe")
    parser.add_argument("--voice", default="en-US-JennyNeural", help="Voice name")
    parser.add_argument("--model", default="base", help="Whisper model size")
    
    args = parser.parse_args()
    
    voice = VoiceSystem()
    
    if args.command == "speak":
        if args.input:
            voice.speak(args.input)
            print(f"Speaking: {args.input}")
        else:
            print("Error: No text provided")
    
    elif args.command == "master":
        if args.input:
            voice.master_voice(args.input)
            print(f"Master voice: {args.input}")
        else:
            print("Error: No text provided")
    
    elif args.command == "realtime":
        if args.input:
            voice.speak(args.input)
            print(f"Realtime: {args.input}")
        else:
            print("Error: No text provided")
    
    elif args.command == "transcribe":
        if args.input and os.path.exists(args.input):
            result = voice.transcribe(args.input)
            print(f"Transcription: {result.text}")
        else:
            print("Error: No valid audio file provided")
    
    elif args.command == "chat":
        print("TitanHive Voice Chat (type 'quit' to exit)")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("Goodbye!")
                break
            response = voice.chat(user_input)
            print(f"AI: {response}")
            voice.speak(response)


if __name__ == "__main__":
    main()
