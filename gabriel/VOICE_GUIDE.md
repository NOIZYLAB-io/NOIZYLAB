# GABRIEL Voice X2000 - Complete Technical Guide

## Overview
GABRIEL Voice X2000 is a premium AI voice synthesis system featuring triple-layered voice engines, smart emotion detection, and multiple character presets.

**Location:** `/Users/m2ultra/NOIZYLAB/GABRIEL/titanhive/voice.py` (5400+ lines)

---

## Quick Start

### Command Line (gab)
```bash
# Basic usage
./gab say "Hello world"              # Master triple-voice
./gab smart "Warning! Critical!"     # Auto-detect emotion
./gab god "Unlimited power"          # God mode preset

# Shortcuts
./gab s "text"   # say
./gab w "text"   # winston
./gab g "text"   # godmode
./gab t "text"   # threat
./gab a "text"   # smart (auto)
```

### Python API
```python
from titanhive.voice import (
    say, smart, mix, deep, narrate,
    get_master_engine, get_preset_engine, get_smart_voice
)

# Quick functions
say("Hello")                    # Master voice
say("Hello", "commander")       # With preset
smart("Warning! Danger!")       # Auto-detect emotion
mix("Layered voice")            # Mixed voices
deep("Extra deep")              # Deep layered
narrate("Once upon a time...")  # Paced narration
```

---

## Voice Presets

| Preset | Description | Pitch | Speed | Voice |
|--------|-------------|-------|-------|-------|
| `winston` | Ian McShane Continental | -3 | 0.88 | onyx |
| `commander` | Military authority | -2 | 0.95 | onyx |
| `butler` | English refined | -1 | 0.92 | fable |
| `godmode` | Omniscient AI | -4 | 0.82 | onyx |
| `narrator` | Documentary | -1 | 0.90 | fable |
| `threat` | Menacing | -4 | 0.75 | onyx |

### Preset EQ Settings
Each preset has custom equalization:
- **Bass** (180Hz): Chest resonance
- **Presence** (800Hz): Authority/clarity
- **Treble** (4000Hz): Brightness control

---

## Engines

### MasterVoiceEngine
Triple-layered premium voice combining:
1. **Jamie (Premium)** - macOS Siri Neural (primary)
2. **OpenAI Onyx** - Deep, authoritative (TTS-1-HD)
3. **Edge TTS Thomas** - British texture

Features:
- 3 semitone pitch drop
- Warm EQ processing
- Light compression
- NO distortion

```python
from titanhive.voice import get_master_engine

engine = get_master_engine()
engine.speak("Text")           # Full triple-layer
engine.realtime("Text")        # Fast single-voice
engine.stream_speak("Text", callback=fn)  # With progress
```

### VoicePresetEngine
Character voice presets with custom processing.

```python
from titanhive.voice import get_preset_engine

engine = get_preset_engine()
engine.winston("Continental greeting")
engine.commander("Deploy all units")
engine.godmode("Absolute power")
engine.threat("Your last warning")
```

### SmartVoice
Intelligent emotion detection from text.

```python
from titanhive.voice import get_smart_voice

sv = get_smart_voice()
emotion, preset, speed = sv.detect_emotion("Warning! Critical!")
# Returns: ("threatening", "threat", 0.9)

sv.speak("Auto-detected emotion")
sv.speak_paced("With natural pauses.")
sv.converse("Context-aware response")
```

**Emotion Keywords:**
- `urgent`: emergency, critical, immediately, now
- `threatening`: warning, danger, consequence, regret
- `authoritative`: command, execute, deploy, initiate
- `calm`: welcome, thank, please, appreciate
- `powerful`: unlimited, absolute, infinite, god
- `storytelling`: once, story, journey, adventure

### VoiceMixer
Layer multiple voices for rich sound.

```python
from titanhive.voice import get_voice_mixer

mixer = get_voice_mixer()
mixer.speak_mixed("Text", voices=["onyx", "fable"], levels=[1.0, 0.3])
mixer.speak_deep("Extra deep")   # onyx + echo
mixer.speak_stereo("Stereo")     # Left/right separation
```

### AudioQueue
Sequential phrase playback.

```python
from titanhive.voice import get_audio_queue

queue = get_audio_queue()
queue.add("First phrase", "winston")
queue.add("Second phrase", "commander")
queue.play()  # Plays sequentially

# Or shortcut
from titanhive.voice import queue_say
queue_say(["One", "Two", "Three"], preset="winston")
```

---

## Audio Processing

### FFmpeg Filter Chain
```
asetrate=44100*{pitch_factor},
aresample=44100,
atempo={tempo_correction},
equalizer=f=180:t=q:w=1:g={bass},      # Chest resonance
equalizer=f=800:t=q:w=1.5:g={presence}, # Authority
equalizer=f=4000:t=q:w=2:g={treble},   # Brightness
acompressor=threshold=-18dB:ratio=3:attack=10:release=150
```

### Pitch Shifting
```python
pitch_semitones = -3
pitch_factor = 2 ** (pitch_semitones / 12)  # 0.84
tempo_correction = 1 / pitch_factor          # 1.19
```

---

## Backend Priority

1. **Jamie (Premium)** - macOS neural voice (if available)
2. **OpenAI TTS-1-HD** - onyx voice (requires API key)
3. **Edge TTS** - en-GB-ThomasNeural (free, requires edge_tts)
4. **macOS say** - Oliver voice (local fallback)

### Checking Availability
```python
engine = get_master_engine()
status = engine.status()
# {
#   "jamie_available": True,
#   "openai_available": True,
#   "edge_available": True,
#   "pitch_semitones": -3,
#   "available": True
# }
```

---

## CLI Commands

```bash
python3 voice.py master [text]      # Master triple-voice
python3 voice.py realtime [text]    # Low latency
python3 voice.py preset <name> [text]  # Use preset
python3 voice.py presets            # Demo all presets
python3 voice.py demo               # Full demo
python3 voice.py test               # Quick test
python3 voice.py backends           # List backends
python3 voice.py effects            # List effects
```

---

## Environment Variables

```bash
OPENAI_API_KEY=sk-xxx    # Required for OpenAI TTS
GOOGLE_API_KEY=xxx       # Optional for Gemini phrase generation
```

---

## Cache Locations

- Master: `/tmp/gabriel_master/`
- Presets: `/tmp/gabriel_presets/`
- Mixer: `/tmp/gabriel_mixer/`
- Voice cache: `titanhive/.voice_cache/`

---

## Winston Phrase Categories

```python
from titanhive.voice import get_winston_phrase

categories = [
    "greet", "acknowledge", "thinking", "success",
    "warning", "threat", "farewell", "wisdom",
    "godmode", "casual", "impressed", "disappointed",
    "humor", "action", "continental"
]

phrase = get_winston_phrase("threat")
# "I'll say this only once."
```

---

## Integration Example

```python
#!/usr/bin/env python3
from titanhive.voice import (
    get_smart_voice,
    get_master_engine,
    say,
    smart
)

# Simple usage
say("Gabriel online")

# Smart emotion detection
smart("Warning! System critical!")

# Full control
sv = get_smart_voice()
sv.speak("Welcome to the Continental", force_preset="butler")
sv.speak_paced("The story. Begins. Now.")

# Master engine direct
engine = get_master_engine()
if engine.available:
    engine.winston("Rules exist for a reason.")
```

---

## File Structure

```
titanhive/
├── voice.py          # Main voice module (5400+ lines)
├── .env              # API keys
├── .venv/            # Python virtual environment
└── .voice_cache/     # Cached audio files

GABRIEL/
├── gab               # Quick launcher script
├── VOICE_GUIDE.md    # This documentation
└── ...
```

---

## Version Info

- **Name:** GABRIEL Voice X2000 - The Winston Edition
- **Primary Voice:** Oliver (British) Enhanced
- **Character:** Ian McShane as Winston (John Wick)
- **Backends:** macOS, OpenAI, Edge TTS, Azure, Google
- **Lines of Code:** 5400+

---

*Last Updated: 2024-12-28*
