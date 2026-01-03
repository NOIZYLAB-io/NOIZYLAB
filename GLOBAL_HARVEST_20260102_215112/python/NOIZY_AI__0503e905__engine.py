"""
NOIZYVOICE TTS Engine - Abstract Base
BETTER THAN ELEVENLABS - Full Feature Set
"""
import abc
import re
import numpy as np
from typing import Optional, AsyncIterator, Dict, List, Any
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum
from loguru import logger


class TTSModel(Enum):
    """Available TTS models"""
    XTTS_V2 = "xtts-v2"
    STYLETTS2 = "styletts2"
    FISH_SPEECH = "fish-speech"
    BARK = "bark"
    PIPER = "piper"
    CHATTERBOX = "chatterbox"
    COSYVOICE = "cosyvoice"


class AudioFormat(Enum):
    """Supported audio formats"""
    WAV = "wav"
    MP3 = "mp3"
    OGG = "ogg"
    FLAC = "flac"
    PCM = "pcm"


class EmotionType(Enum):
    """Supported emotions"""
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    FEARFUL = "fearful"
    SURPRISED = "surprised"
    DISGUSTED = "disgusted"
    CALM = "calm"
    EXCITED = "excited"
    WHISPER = "whisper"
    SHOUT = "shout"


@dataclass
class VoiceSettings:
    """Voice configuration settings"""
    stability: float = 0.5  # 0-1, lower = more variable
    similarity_boost: float = 0.75  # 0-1, voice similarity
    style: float = 0.0  # 0-1, style exaggeration
    use_speaker_boost: bool = True


@dataclass
class TTSRequest:
    """TTS generation request - FULL FEATURE SET"""
    text: str
    voice_id: Optional[str] = None
    voice_sample: Optional[Path] = None
    language: str = "en"

    # Speed & Pitch
    speed: float = 1.0  # 0.5-2.0
    pitch: float = 1.0  # 0.5-2.0

    # Emotion & Style
    emotion: Optional[str] = None
    intensity: float = 1.0  # emotion intensity 0-2

    # Voice Settings
    voice_settings: Optional[VoiceSettings] = None

    # Audio Tags
    audio_tags: Optional[Dict] = None

    # Output
    stream: bool = False
    output_format: str = "wav"
    sample_rate: int = 24000

    # Advanced
    seed: Optional[int] = None  # reproducibility
    temperature: float = 0.7  # randomness
    top_p: float = 0.9  # nucleus sampling

    # Multi-speaker
    speakers: Optional[List[Dict]] = None  # for dialogue

    # Effects
    reverb: float = 0.0  # 0-1
    echo: float = 0.0  # 0-1
    noise_gate: bool = True
    normalize: bool = True


@dataclass
class TTSResponse:
    """TTS generation response"""
    audio: np.ndarray
    sample_rate: int
    duration: float
    model: str
    latency_ms: float

    # Metadata
    metadata: Dict = field(default_factory=dict)

    # Alignment data
    word_timestamps: Optional[List[Dict]] = None
    phoneme_timestamps: Optional[List[Dict]] = None

    # Quality metrics
    naturalness_score: Optional[float] = None


@dataclass
class DialogueTurn:
    """Single turn in a dialogue"""
    speaker: str
    text: str
    emotion: Optional[str] = None
    pause_after: float = 0.5  # seconds


@dataclass
class DialogueRequest:
    """Multi-speaker dialogue request"""
    turns: List[DialogueTurn]
    voices: Dict[str, str]  # speaker -> voice_id mapping
    output_format: str = "wav"
    crossfade: float = 0.1  # seconds between speakers


class TTSEngine(abc.ABC):
    """Abstract TTS Engine base class - FULL IMPLEMENTATION"""

    # Supported languages mapping
    LANGUAGE_MAP = {
        "en": "English", "es": "Spanish", "fr": "French", "de": "German",
        "it": "Italian", "pt": "Portuguese", "pl": "Polish", "tr": "Turkish",
        "ru": "Russian", "nl": "Dutch", "cs": "Czech", "ar": "Arabic",
        "zh": "Chinese", "ja": "Japanese", "ko": "Korean", "hu": "Hungarian",
        "hi": "Hindi", "vi": "Vietnamese", "th": "Thai", "id": "Indonesian",
        "sv": "Swedish", "da": "Danish", "fi": "Finnish", "no": "Norwegian",
        "el": "Greek", "he": "Hebrew", "uk": "Ukrainian", "ro": "Romanian",
        "bg": "Bulgarian", "hr": "Croatian", "sk": "Slovak", "sl": "Slovenian",
    }

    # Audio tag definitions
    AUDIO_TAGS = {
        "whisper": {"intensity": 0.3, "pitch_shift": -0.05, "speed": 0.9},
        "whispers": {"intensity": 0.3, "pitch_shift": -0.05, "speed": 0.9},
        "shout": {"intensity": 1.8, "pitch_shift": 0.15, "speed": 1.1},
        "shouts": {"intensity": 1.8, "pitch_shift": 0.15, "speed": 1.1},
        "laugh": {"effect": "laugh", "duration": 1.0},
        "laughs": {"effect": "laugh", "duration": 1.0},
        "sigh": {"effect": "sigh", "duration": 0.8},
        "sighs": {"effect": "sigh", "duration": 0.8},
        "cry": {"effect": "cry", "intensity": 0.7},
        "cries": {"effect": "cry", "intensity": 0.7},
        "excited": {"speed": 1.15, "pitch_shift": 0.1, "intensity": 1.3},
        "sad": {"speed": 0.85, "pitch_shift": -0.1, "intensity": 0.7},
        "angry": {"speed": 1.1, "intensity": 1.4, "pitch_shift": 0.05},
        "scared": {"speed": 1.15, "pitch_shift": 0.15, "tremolo": 0.3},
        "calm": {"speed": 0.9, "intensity": 0.8},
        "happy": {"speed": 1.05, "pitch_shift": 0.08, "intensity": 1.2},
        "surprised": {"speed": 1.2, "pitch_shift": 0.2},
        "pause": {"effect": "pause", "duration": 0.5},
        "long_pause": {"effect": "pause", "duration": 1.5},
        "breath": {"effect": "breath", "duration": 0.3},
        "door_creaks": {"effect": "sfx", "sound": "door_creak"},
        "footsteps": {"effect": "sfx", "sound": "footsteps"},
        "thunder": {"effect": "sfx", "sound": "thunder"},
    }

    def __init__(self, model_path: Optional[Path] = None, device: str = "cuda"):
        self.model_path = model_path
        self.device = device
        self.model = None
        self.is_loaded = False
        self.sample_rate = 24000
        self.voice_embeddings: Dict[str, Any] = {}
        self.sfx_library: Dict[str, np.ndarray] = {}

    @abc.abstractmethod
    async def load_model(self) -> None:
        """Load the TTS model"""
        pass

    @abc.abstractmethod
    async def synthesize(self, request: TTSRequest) -> TTSResponse:
        """Synthesize speech from text"""
        pass

    @abc.abstractmethod
    async def stream(self, request: TTSRequest) -> AsyncIterator[bytes]:
        """Stream synthesized speech"""
        pass

    @abc.abstractmethod
    async def clone_voice(
        self,
        audio_path: Path,
        voice_id: str,
        description: Optional[str] = None,
    ) -> str:
        """Clone a voice from audio sample"""
        pass

    async def synthesize_dialogue(self, request: DialogueRequest) -> TTSResponse:
        """Synthesize multi-speaker dialogue"""
        import time
        start = time.time()

        audio_segments = []
        total_duration = 0.0

        for turn in request.turns:
            # Get voice for speaker
            voice_id = request.voices.get(turn.speaker)
            if not voice_id:
                raise ValueError(f"No voice mapped for speaker: {turn.speaker}")

            # Create TTS request
            tts_request = TTSRequest(
                text=turn.text,
                voice_id=voice_id,
                emotion=turn.emotion,
            )

            # Synthesize
            response = await self.synthesize(tts_request)
            audio_segments.append(response.audio)
            total_duration += response.duration

            # Add pause
            if turn.pause_after > 0:
                pause_samples = int(turn.pause_after * self.sample_rate)
                audio_segments.append(np.zeros(pause_samples))
                total_duration += turn.pause_after

        # Concatenate with crossfade
        final_audio = self._crossfade_segments(audio_segments, request.crossfade)

        return TTSResponse(
            audio=final_audio,
            sample_rate=self.sample_rate,
            duration=total_duration,
            model=self.__class__.__name__,
            latency_ms=(time.time() - start) * 1000,
            metadata={
                "speakers": list(request.voices.keys()),
                "turns": len(request.turns),
            },
        )

    def _crossfade_segments(
        self,
        segments: List[np.ndarray],
        crossfade_duration: float
    ) -> np.ndarray:
        """Crossfade audio segments together"""
        if not segments:
            return np.array([])

        if len(segments) == 1:
            return segments[0]

        crossfade_samples = int(crossfade_duration * self.sample_rate)
        result = segments[0].copy()

        for segment in segments[1:]:
            if len(segment) == 0:
                continue

            if crossfade_samples > 0 and len(result) > crossfade_samples:
                # Create crossfade
                fade_out = np.linspace(1, 0, crossfade_samples)
                fade_in = np.linspace(0, 1, crossfade_samples)

                # Apply crossfade
                result[-crossfade_samples:] *= fade_out
                segment_copy = segment.copy()
                segment_copy[:crossfade_samples] *= fade_in

                # Overlap
                result[-crossfade_samples:] += segment_copy[:crossfade_samples]
                result = np.concatenate([result, segment_copy[crossfade_samples:]])
            else:
                result = np.concatenate([result, segment])

        return result

    def preprocess_text(self, text: str) -> str:
        """Preprocess text before synthesis"""
        # Remove extra whitespace
        text = " ".join(text.split())

        # Expand common abbreviations
        abbreviations = {
            "Dr.": "Doctor", "Mr.": "Mister", "Mrs.": "Missus",
            "Ms.": "Miss", "Jr.": "Junior", "Sr.": "Senior",
            "vs.": "versus", "etc.": "et cetera", "e.g.": "for example",
            "i.e.": "that is", "Prof.": "Professor", "St.": "Saint",
            "Mt.": "Mount", "Ave.": "Avenue", "Blvd.": "Boulevard",
        }
        for abbr, expansion in abbreviations.items():
            text = text.replace(abbr, expansion)

        # Expand numbers (basic)
        text = self._expand_numbers(text)

        return text

    def _expand_numbers(self, text: str) -> str:
        """Expand numbers to words (basic implementation)"""
        # This is simplified - production would use num2words
        number_words = {
            "0": "zero", "1": "one", "2": "two", "3": "three",
            "4": "four", "5": "five", "6": "six", "7": "seven",
            "8": "eight", "9": "nine", "10": "ten",
        }

        for num, word in number_words.items():
            # Only replace standalone numbers
            text = re.sub(rf'\b{num}\b', word, text)

        return text

    def parse_audio_tags(self, text: str) -> tuple[str, List[Dict]]:
        """Parse audio tags from text

        Supports:
        - [whisper]text[/whisper]
        - [laugh]
        - [pause:1.5]
        - [emotion:happy]text[/emotion]
        """
        tags = []
        clean_text = text

        # Pattern for paired tags: [tag]content[/tag]
        paired_pattern = r'\[(\w+)\](.*?)\[/\1\]'
        for match in re.finditer(paired_pattern, text):
            tag_name = match.group(1).lower()
            tag_content = match.group(2)

            if tag_name in self.AUDIO_TAGS:
                tags.append({
                    "type": "paired",
                    "tag": tag_name,
                    "content": tag_content,
                    "settings": self.AUDIO_TAGS[tag_name],
                    "start": match.start(),
                    "end": match.end(),
                })

        # Pattern for single tags: [tag] or [tag:value]
        single_pattern = r'\[(\w+)(?::([^\]]+))?\]'
        for match in re.finditer(single_pattern, text):
            tag_name = match.group(1).lower()
            tag_value = match.group(2)

            # Skip closing tags
            if text[match.start()-1:match.start()] == '/':
                continue

            if tag_name in self.AUDIO_TAGS or tag_name in ["pause", "emotion"]:
                tag_data = {
                    "type": "single",
                    "tag": tag_name,
                    "start": match.start(),
                    "end": match.end(),
                }

                if tag_value:
                    tag_data["value"] = tag_value

                if tag_name in self.AUDIO_TAGS:
                    tag_data["settings"] = self.AUDIO_TAGS[tag_name]

                tags.append(tag_data)

        # Remove all tags from text
        clean_text = re.sub(r'\[/?[^\]]+\]', '', text)
        clean_text = " ".join(clean_text.split())  # Normalize whitespace

        return clean_text, tags

    def apply_audio_effects(
        self,
        audio: np.ndarray,
        effects: Dict[str, Any],
    ) -> np.ndarray:
        """Apply audio effects based on tags"""
        import librosa

        # Speed adjustment
        if "speed" in effects and effects["speed"] != 1.0:
            audio = librosa.effects.time_stretch(audio, rate=effects["speed"])

        # Pitch shift
        if "pitch_shift" in effects and effects["pitch_shift"] != 0:
            n_steps = 12 * effects["pitch_shift"]  # Convert to semitones
            audio = librosa.effects.pitch_shift(
                audio, sr=self.sample_rate, n_steps=n_steps
            )

        # Intensity (volume)
        if "intensity" in effects:
            audio = audio * effects["intensity"]

        # Tremolo (for scared voice)
        if effects.get("tremolo"):
            tremolo_rate = effects.get("tremolo", 0.3)
            t = np.arange(len(audio)) / self.sample_rate
            tremolo = 1 + tremolo_rate * np.sin(2 * np.pi * 5 * t)  # 5Hz tremolo
            audio = audio * tremolo

        # Normalize to prevent clipping
        max_val = np.abs(audio).max()
        if max_val > 0.95:
            audio = audio * (0.95 / max_val)

        return audio

    async def unload_model(self) -> None:
        """Unload model from memory"""
        if self.model is not None:
            del self.model
            self.model = None
            self.is_loaded = False

            import torch
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            logger.info("Model unloaded")

    def get_info(self) -> Dict:
        """Get engine information"""
        return {
            "model": self.__class__.__name__,
            "device": self.device,
            "is_loaded": self.is_loaded,
            "sample_rate": self.sample_rate,
            "supported_languages": list(self.LANGUAGE_MAP.keys()),
            "audio_tags": list(self.AUDIO_TAGS.keys()),
            "voice_count": len(self.voice_embeddings),
        }

    def list_voices(self) -> List[Dict]:
        """List available voices"""
        return [
            {"id": vid, "name": vid}
            for vid in self.voice_embeddings.keys()
        ]
