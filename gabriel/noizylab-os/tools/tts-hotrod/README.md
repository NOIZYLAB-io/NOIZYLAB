# 🔥 TTS Hot Rod - Gemini Steerable Text-to-Speech

A Python tool that connects to Google's Gemini API with "Hot Rod" steering instructions for human-like speech generation.

## Setup

```bash
cd noizylab-os/tools/tts-hotrod
pip install -r requirements.txt
export GEMINI_API_KEY='your-api-key-here'
```

## Usage

### Quick Generate
```bash
# Hype mode - maximum energy!
python tts_hotrod.py "Let's GO! This is amazing!" --steer HYPE

# Whisper mode - secretive
python tts_hotrod.py "The package has been delivered..." --steer WHISPER

# Save to specific file
python tts_hotrod.py "Hello world" --steer EXCITED -o hello.mp3
```

### Interactive Mode
```bash
python tts_hotrod.py --interactive
```

Commands in interactive mode:
- `/steer HYPE` - Change steering mode
- `/voice Kore` - Change voice
- `/presets` - Show all steering options
- `/quit` - Exit

### Auto-Watch Folder
```bash
python tts_hotrod.py --watch ./scripts
```

Drop `.txt` files in the folder:
```
HYPE
This is my script that will be spoken with maximum energy!
```

### Multi-Speaker Demo
```bash
python tts_hotrod.py --demo
```

## Steering Modes

| Mode | Description |
|------|-------------|
| `HYPE` | Maximum energy, fast pace, rising inflection |
| `WHISPER` | Drop volume, increase airiness |
| `AGGRESSIVE` | Increase volume, hard consonants |
| `STUTTER` | Repeat first phoneme of words |
| `SLOW` | Extend vowel sounds, longer pauses |
| `FAST` | Clip consonants, shorten pauses |
| `SARCASTIC` | Dry delivery with emphasis shifts |
| `EXCITED` | High energy, varied pitch |
| `NEUTRAL` | Standard delivery |

## Available Voices

- Puck
- Charon
- Kore (default)
- Fenrir
- Aoede

## Output

All generated files are saved to `./output/` with format:
```
tts_<steer>_<timestamp>.mp3
```

## Pro Tips

### Phonetic Precision
For technical words, use brackets:
```bash
python tts_hotrod.py "The [fo-NET-ik] API is [in-KRED-uh-bul]" --steer HYPE
```

### Natural Disfluencies
Add breath markers for realism:
```bash
python tts_hotrod.py "[breath] Well, umm, I think [breath] this is pretty cool" --steer SLOW
```

### Script Files
Create a script file `my_script.txt`:
```
WHISPER
[breath] The secret code is... [breath] Hot Rod.
```

Then watch the folder:
```bash
python tts_hotrod.py --watch .
```

## Integration with NoizyLab OS

This tool can be integrated with the NoizyLab OS support ticket system to:
- Read ticket summaries aloud for accessibility
- Generate voice notifications
- Create audio responses for clients
- Power "Calm Mode" voice guidance

---

🏎️ **GO RUN FREE** 🏎️
