#!/usr/bin/env python3
"""
NOIZYVOX SOVEREIGN VOICE ENGINE
===============================
Unified voice synthesis, cloning, and AI narration system.
Consolidated from the NOIZYVOX platform codebase.

The Voice of the Sovereign Sanctuary.
GORUNFREE.
"""

import os
import sys
import json
import asyncio
import hashlib
import requests
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# Optional imports
try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    EDGE_TTS_AVAILABLE = False

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False


class VoiceProvider(Enum):
    """Supported voice providers."""
    ELEVENLABS = "elevenlabs"
    AZURE = "azure"
    EDGE = "edge"
    GTTS = "gtts"
    OPENAI = "openai"
    GEMINI = "gemini"


class EmotionalMode(Enum):
    """Emotional voice modes for sovereign narration."""
    FOCUS = "focus"          # Calm, precise guidance
    ALERT = "alert"          # Warning, attention needed
    CELEBRATE = "celebrate"  # Success, achievement
    EMPATHY = "empathy"      # Understanding, support
    TEACHING = "teaching"    # Instructional, patient
    HYPE = "hype"           # Maximum energy
    WHISPER = "whisper"     # Quiet, confidential
    NEUTRAL = "neutral"     # Standard delivery
    SOVEREIGN = "sovereign" # Authoritative, official


# Emotional settings for ElevenLabs
EMOTIONAL_SETTINGS = {
    EmotionalMode.FOCUS: {"stability": 0.75, "similarity_boost": 0.85, "style": 0.3},
    EmotionalMode.ALERT: {"stability": 0.5, "similarity_boost": 0.9, "style": 0.6},
    EmotionalMode.CELEBRATE: {"stability": 0.4, "similarity_boost": 0.8, "style": 0.8},
    EmotionalMode.EMPATHY: {"stability": 0.7, "similarity_boost": 0.85, "style": 0.5},
    EmotionalMode.TEACHING: {"stability": 0.65, "similarity_boost": 0.8, "style": 0.4},
    EmotionalMode.HYPE: {"stability": 0.3, "similarity_boost": 0.75, "style": 0.9},
    EmotionalMode.WHISPER: {"stability": 0.8, "similarity_boost": 0.9, "style": 0.2},
    EmotionalMode.NEUTRAL: {"stability": 0.5, "similarity_boost": 0.75, "style": 0.5},
    EmotionalMode.SOVEREIGN: {"stability": 0.7, "similarity_boost": 0.9, "style": 0.4},
}


@dataclass
class NoizyVoxVoice:
    """A NOIZYVOX voice profile."""
    name: str
    voice_id: str
    tier: str = "premium"
    persona: str = ""
    tags: List[str] = field(default_factory=list)
    latency_ms: int = 400
    model: str = "eleven_multilingual_v2"
    consent: str = "Professional license on file"
    usage: str = ""


# NOIZYVOX Voice Roster
NOIZYVOX_ROSTER = [
    NoizyVoxVoice(
        name="NoizyVox Prime",
        voice_id="noizyvox-prime-v1",
        persona="Authoritative, reassuring technical lead",
        tags=["support", "uptime", "cpu-repair"],
        latency_ms=380,
        usage="Primary support voice for portal and agent replies"
    ),
    NoizyVoxVoice(
        name="NoizyVox Flow",
        voice_id="noizyvox-flow-v1",
        persona="Warm, musical cadence for creative outreach",
        tags=["creative", "marketing", "vibe"],
        latency_ms=420,
        usage="Invitation videos, waitlist hype, milestone artifacts"
    ),
    NoizyVoxVoice(
        name="NoizyVox Sentinel",
        voice_id="noizyvox-sentinel-v1",
        persona="Calm, precise ops dispatcher",
        tags=["alerts", "ops", "finance"],
        latency_ms=360,
        usage="System alerts, billing confirmations, SLA updates"
    ),
]


class NoizyVoxEngine:
    """
    The NOIZYVOX Sovereign Voice Engine.

    Provides unified access to multiple TTS providers with emotional modes,
    voice cloning, and sovereign narration capabilities.
    """

    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or Path.home() / "NOIZYLAB" / "GABRIEL" / "sovereign" / "audio"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # API keys from environment
        self.elevenlabs_key = os.getenv("ELEVENLABS_API_KEY", "")
        self.azure_key = os.getenv("AZURE_SPEECH_KEY", "")
        self.azure_region = os.getenv("AZURE_SPEECH_REGION", "eastus")
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")

        # Roster
        self.voices = {v.name: v for v in NOIZYVOX_ROSTER}

        self._check_availability()

    def _check_availability(self):
        """Check which providers are available."""
        self.available_providers = []

        if self.elevenlabs_key:
            self.available_providers.append(VoiceProvider.ELEVENLABS)
        if self.azure_key:
            self.available_providers.append(VoiceProvider.AZURE)
        if EDGE_TTS_AVAILABLE:
            self.available_providers.append(VoiceProvider.EDGE)
        if GTTS_AVAILABLE:
            self.available_providers.append(VoiceProvider.GTTS)
        if self.openai_key:
            self.available_providers.append(VoiceProvider.OPENAI)
        if self.gemini_key:
            self.available_providers.append(VoiceProvider.GEMINI)

    def list_providers(self) -> List[str]:
        """List available voice providers."""
        return [p.value for p in self.available_providers]

    def list_voices(self) -> List[Dict]:
        """List available NOIZYVOX voices."""
        return [
            {
                "name": v.name,
                "voice_id": v.voice_id,
                "persona": v.persona,
                "tags": v.tags,
                "usage": v.usage
            }
            for v in self.voices.values()
        ]

    # =========================================================================
    # TEXT-TO-SPEECH
    # =========================================================================

    async def speak(
        self,
        text: str,
        voice: str = "NoizyVox Prime",
        mode: EmotionalMode = EmotionalMode.NEUTRAL,
        provider: VoiceProvider = None,
        output_file: str = None
    ) -> Optional[Path]:
        """
        Generate speech from text.

        Args:
            text: The text to speak
            voice: NOIZYVOX voice name or provider-specific voice ID
            mode: Emotional mode for delivery
            provider: Voice provider (auto-selects if None)
            output_file: Output filename (auto-generated if None)

        Returns:
            Path to generated audio file, or None on failure
        """

        # Auto-select provider
        if provider is None:
            if self.elevenlabs_key:
                provider = VoiceProvider.ELEVENLABS
            elif EDGE_TTS_AVAILABLE:
                provider = VoiceProvider.EDGE
            elif GTTS_AVAILABLE:
                provider = VoiceProvider.GTTS
            else:
                print("ERROR: No voice providers available")
                return None

        # Generate output filename
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"sovereign_{mode.value}_{timestamp}.mp3"

        output_path = self.output_dir / output_file

        # Route to provider
        if provider == VoiceProvider.ELEVENLABS:
            return await self._speak_elevenlabs(text, voice, mode, output_path)
        elif provider == VoiceProvider.EDGE:
            return await self._speak_edge(text, voice, output_path)
        elif provider == VoiceProvider.GTTS:
            return self._speak_gtts(text, output_path)
        elif provider == VoiceProvider.OPENAI:
            return await self._speak_openai(text, voice, output_path)
        else:
            print(f"ERROR: Provider {provider} not implemented")
            return None

    async def _speak_elevenlabs(
        self,
        text: str,
        voice: str,
        mode: EmotionalMode,
        output_path: Path
    ) -> Optional[Path]:
        """Generate speech using ElevenLabs."""

        if not self.elevenlabs_key:
            print("ERROR: ELEVENLABS_API_KEY not set")
            return None

        # Get voice ID
        voice_id = voice
        if voice in self.voices:
            voice_id = self.voices[voice].voice_id

        # Get emotional settings
        settings = EMOTIONAL_SETTINGS.get(mode, EMOTIONAL_SETTINGS[EmotionalMode.NEUTRAL])

        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

            headers = {
                "xi-api-key": self.elevenlabs_key,
                "Content-Type": "application/json"
            }

            payload = {
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": settings["stability"],
                    "similarity_boost": settings["similarity_boost"],
                    "style": settings.get("style", 0.5),
                    "use_speaker_boost": True
                }
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(response.content)
                print(f"ElevenLabs: Generated {output_path}")
                return output_path
            else:
                print(f"ElevenLabs error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"ElevenLabs error: {e}")
            return None

    async def _speak_edge(self, text: str, voice: str, output_path: Path) -> Optional[Path]:
        """Generate speech using Microsoft Edge TTS (free)."""

        if not EDGE_TTS_AVAILABLE:
            print("ERROR: edge-tts not installed")
            return None

        # Map NOIZYVOX voices to Edge voices
        edge_voice_map = {
            "NoizyVox Prime": "en-US-GuyNeural",
            "NoizyVox Flow": "en-US-AriaNeural",
            "NoizyVox Sentinel": "en-US-JennyNeural",
        }

        edge_voice = edge_voice_map.get(voice, "en-US-AriaNeural")

        try:
            communicate = edge_tts.Communicate(text, edge_voice)
            await communicate.save(str(output_path))
            print(f"Edge TTS: Generated {output_path}")
            return output_path
        except Exception as e:
            print(f"Edge TTS error: {e}")
            return None

    def _speak_gtts(self, text: str, output_path: Path) -> Optional[Path]:
        """Generate speech using Google TTS (free)."""

        if not GTTS_AVAILABLE:
            print("ERROR: gTTS not installed")
            return None

        try:
            tts = gTTS(text=text, lang="en")
            tts.save(str(output_path))
            print(f"gTTS: Generated {output_path}")
            return output_path
        except Exception as e:
            print(f"gTTS error: {e}")
            return None

    async def _speak_openai(self, text: str, voice: str, output_path: Path) -> Optional[Path]:
        """Generate speech using OpenAI TTS."""

        if not self.openai_key:
            print("ERROR: OPENAI_API_KEY not set")
            return None

        # Map to OpenAI voices
        openai_voice_map = {
            "NoizyVox Prime": "onyx",
            "NoizyVox Flow": "nova",
            "NoizyVox Sentinel": "echo",
        }

        openai_voice = openai_voice_map.get(voice, "alloy")

        try:
            url = "https://api.openai.com/v1/audio/speech"

            headers = {
                "Authorization": f"Bearer {self.openai_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "tts-1-hd",
                "input": text,
                "voice": openai_voice
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(response.content)
                print(f"OpenAI TTS: Generated {output_path}")
                return output_path
            else:
                print(f"OpenAI error: {response.status_code}")
                return None

        except Exception as e:
            print(f"OpenAI error: {e}")
            return None

    # =========================================================================
    # VOICE CLONING
    # =========================================================================

    def clone_voice(
        self,
        audio_file: str,
        name: str,
        description: str = ""
    ) -> Optional[str]:
        """
        Clone a voice from audio samples using ElevenLabs.

        Args:
            audio_file: Path to audio sample
            name: Name for the cloned voice
            description: Description of the voice

        Returns:
            Voice ID of the cloned voice, or None on failure
        """

        if not self.elevenlabs_key:
            print("ERROR: ELEVENLABS_API_KEY required for voice cloning")
            return None

        try:
            url = "https://api.elevenlabs.io/v1/voices/add"

            headers = {"xi-api-key": self.elevenlabs_key}

            with open(audio_file, "rb") as f:
                files = {"files": (os.path.basename(audio_file), f, "audio/mpeg")}
                data = {"name": name, "description": description}

                response = requests.post(url, headers=headers, files=files, data=data)

            if response.status_code == 200:
                voice_data = response.json()
                voice_id = voice_data.get("voice_id")
                print(f"Voice cloned! ID: {voice_id}")

                # Add to local roster
                self.voices[name] = NoizyVoxVoice(
                    name=name,
                    voice_id=voice_id,
                    tier="cloned",
                    persona=description
                )

                return voice_id
            else:
                print(f"Clone error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"Clone error: {e}")
            return None

    # =========================================================================
    # SOVEREIGN NARRATION
    # =========================================================================

    async def narrate_manifest(
        self,
        case_id: str,
        customer_name: str,
        device: str,
        diagnosis: str,
        status: str = "RECOVERY COMPLETE"
    ) -> Optional[Path]:
        """
        Generate sovereign narration for a repair manifest.

        Creates an audio version of the architect's note.
        """

        script = f"""
        NOIZYLAB Sovereign Forensics. Case {case_id}.

        {customer_name}, your {device} repair is complete.

        The silicon responded well to the entrainment.
        Diagnosis: {diagnosis}.
        Status: {status}.

        Your hardware has been restored to Sovereign Purity.

        Go. Run. Free.
        """

        output_file = f"manifest_narration_{case_id}.mp3"

        return await self.speak(
            text=script.strip(),
            voice="NoizyVox Prime",
            mode=EmotionalMode.SOVEREIGN,
            output_file=output_file
        )

    async def narrate_repair_step(
        self,
        step_number: int,
        instruction: str,
        warning: bool = False
    ) -> Optional[Path]:
        """Generate voice guidance for a repair step."""

        mode = EmotionalMode.ALERT if warning else EmotionalMode.TEACHING
        voice = "NoizyVox Sentinel" if warning else "NoizyVox Prime"

        script = f"Step {step_number}. {instruction}"

        if warning:
            script = f"Warning. {script}"

        output_file = f"repair_step_{step_number}_{datetime.now().strftime('%H%M%S')}.mp3"

        return await self.speak(
            text=script,
            voice=voice,
            mode=mode,
            output_file=output_file
        )

    async def celebrate_success(self, achievement: str) -> Optional[Path]:
        """Generate celebration audio."""

        script = f"""
        Excellent work! {achievement}
        The sovereign standard has been achieved.
        Go run free!
        """

        return await self.speak(
            text=script.strip(),
            voice="NoizyVox Flow",
            mode=EmotionalMode.CELEBRATE,
            output_file=f"celebrate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        )


# =============================================================================
# CLI INTERFACE
# =============================================================================

async def main():
    """CLI entry point."""

    print("""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                               ║
    ║              NOIZYVOX SOVEREIGN VOICE ENGINE                                  ║
    ║                                                                               ║
    ║              The Voice of the Sanctuary.                                      ║
    ║                                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
    """)

    engine = NoizyVoxEngine()

    print("Available Providers:", engine.list_providers())
    print("\nNOIZYVOX Voices:")
    for voice in engine.list_voices():
        print(f"  - {voice['name']}: {voice['persona']}")

    # Demo generation
    print("\nGenerating demo audio...")

    # Try to generate with any available provider
    audio_path = await engine.speak(
        text="Welcome to the Sovereign Sanctuary. Your hardware will be restored to sovereign purity. Go run free.",
        voice="NoizyVox Prime",
        mode=EmotionalMode.SOVEREIGN
    )

    if audio_path:
        print(f"\nAudio generated: {audio_path}")
    else:
        print("\nNo audio generated - check provider configuration")

    print("\nGORUNFREE!")


if __name__ == "__main__":
    asyncio.run(main())
