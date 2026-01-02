#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎤 VOX - Voice Control Application for iPad 🎤                    ║
║                                                                           ║
║  Control LUCY, TREVOR, and ALEX from your iPad!                         ║
║  Part of MC96 HyperSort Suite                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
import subprocess
from pathlib import Path
import random
import json
import os

app = Flask(__name__)

# Base path for MC96
BASE_PATH = Path("/Users/rsp_ms/MC96_MobileApp")

# Voice file mappings
VOICES = {
    "lucy": {
        "greeting": BASE_PATH / "LUCY" / "lucy_greeting.wav",
        "code": BASE_PATH / "LUCY" / "lucy_code.wav",
        "apple": BASE_PATH / "LUCY" / "lucy_apple.wav",
        "french": BASE_PATH / "LUCY" / "lucy_french.wav",
        "cheerio": BASE_PATH / "LUCY" / "lucy_cheerio.wav",
    },
    "trevor": {
        "greeting": BASE_PATH / "TREVOR" / "trevor_greeting.wav",
        "music": BASE_PATH / "TREVOR" / "trevor_music.wav",
        "data": BASE_PATH / "TREVOR" / "trevor_data.wav",
        "engineering": BASE_PATH / "TREVOR" / "trevor_engineering.wav",
        "innovation": BASE_PATH / "TREVOR" / "trevor_innovation.wav",
    },
    "alex": {
        "greeting": BASE_PATH / "ALEX" / "alex_greeting.wav",
        "strategy": BASE_PATH / "ALEX" / "alex_strategy.wav",
        "architecture": BASE_PATH / "ALEX" / "alex_architecture.wav",
        "leadership": BASE_PATH / "ALEX" / "alex_leadership.wav",
        "delivery": BASE_PATH / "ALEX" / "alex_delivery.wav",
    },
}

# Companion info
COMPANIONS = {
    "lucy": {
        "name": "LUCY",
        "icon": "🎸",
        "description": "British/French Creative Genius - BITW with 1000X Quality",
        "color": "#FF6B9D",
        "accent": "#FF1744",
    },
    "trevor": {
        "name": "TREVOR",
        "icon": "🎵",
        "description": "American Kid Engineering Master",
        "color": "#4FC3F7",
        "accent": "#00B0FF",
    },
    "alex": {
        "name": "ALEX",
        "icon": "⚡",
        "description": "Strategic Professional Advisor",
        "color": "#FFD54F",
        "accent": "#FFC400",
    },
}


@app.route('/')
def index():
    """Main iPad interface."""
    return render_template('index.html', companions=COMPANIONS)


@app.route('/api/companions')
def get_companions():
    """Get all companions info."""
    return jsonify(COMPANIONS)


@app.route('/api/voices/<companion>')
def get_voices(companion):
    """Get available voices for a companion."""
    if companion not in VOICES:
        return jsonify({"error": "Companion not found"}), 404

    voices = {}
    for voice_type, path in VOICES[companion].items():
        voices[voice_type] = {
            "name": voice_type.title(),
            "available": path.exists(),
            "path": str(path)
        }

    return jsonify(voices)


@app.route('/api/play', methods=['POST'])
def play_voice():
    """Play a voice."""
    data = request.json
    companion = data.get('companion')
    voice_type = data.get('voice_type')

    if companion not in VOICES:
        return jsonify({"error": "Companion not found"}), 404

    if voice_type not in VOICES[companion]:
        return jsonify({"error": "Voice type not found"}), 404

    voice_path = VOICES[companion][voice_type]

    if not voice_path.exists():
        return jsonify({
            "error": "Voice file not found",
            "path": str(voice_path)
        }), 404

    # Play the voice using afplay (macOS)
    try:
        subprocess.Popen(["afplay", str(voice_path)])
        return jsonify({
            "success": True,
            "companion": companion,
            "voice_type": voice_type,
            "message": f"{COMPANIONS[companion]['name']} is speaking!"
        })
    except Exception as e:
        return jsonify({
            "error": f"Failed to play voice: {str(e)}"
        }), 500


@app.route('/api/play/random', methods=['POST'])
def play_random():
    """Play a random voice from any companion."""
    data = request.json
    companion = data.get('companion', None)

    if companion and companion not in VOICES:
        return jsonify({"error": "Companion not found"}), 404

    # Select random companion if not specified
    if not companion:
        companion = random.choice(list(VOICES.keys()))

    # Select random voice type
    voice_type = random.choice(list(VOICES[companion].keys()))

    # Play it
    return play_voice_internal(companion, voice_type)


@app.route('/api/play/sequence', methods=['POST'])
def play_sequence():
    """Play a sequence of voices."""
    data = request.json
    sequence = data.get('sequence', [])
    gap = data.get('gap', 0.5)

    if not sequence:
        return jsonify({"error": "No sequence provided"}), 400

    results = []
    for item in sequence:
        companion = item.get('companion')
        voice_type = item.get('voice_type')

        if companion in VOICES and voice_type in VOICES[companion]:
            voice_path = VOICES[companion][voice_type]
            if voice_path.exists():
                subprocess.run(["afplay", str(voice_path)])
                results.append({
                    "companion": companion,
                    "voice_type": voice_type,
                    "success": True
                })
            else:
                results.append({
                    "companion": companion,
                    "voice_type": voice_type,
                    "success": False,
                    "error": "File not found"
                })

    return jsonify({
        "success": True,
        "results": results
    })


@app.route('/api/generate', methods=['POST'])
def generate_voices():
    """Generate voices using TTS."""
    data = request.json
    companion = data.get('companion')

    if companion not in ['lucy', 'trevor', 'alex']:
        return jsonify({"error": "Invalid companion"}), 400

    # Path to TTS script
    tts_env = BASE_PATH / "LUCY" / "tts_env" / "bin" / "python"

    if companion == "lucy":
        tts_script = BASE_PATH / "LUCY" / "lucy_tts_advanced.py"
    elif companion == "trevor":
        tts_script = BASE_PATH / "TREVOR" / "trevor_tts_advanced.py"
    else:
        tts_script = BASE_PATH / "ALEX" / "alex_tts_advanced.py"

    if not tts_env.exists() or not tts_script.exists():
        return jsonify({
            "error": "TTS environment not found",
            "tts_env": str(tts_env),
            "tts_script": str(tts_script)
        }), 500

    try:
        result = subprocess.run(
            [str(tts_env), str(tts_script)],
            capture_output=True,
            text=True,
            timeout=300
        )

        return jsonify({
            "success": result.returncode == 0,
            "companion": companion,
            "output": result.stdout,
            "errors": result.stderr
        })
    except Exception as e:
        return jsonify({
            "error": f"Failed to generate voices: {str(e)}"
        }), 500


@app.route('/api/status')
def get_status():
    """Get system status."""
    status = {
        "companions": {},
        "system": {
            "base_path": str(BASE_PATH),
            "tts_available": (BASE_PATH / "LUCY" / "tts_env").exists()
        }
    }

    for companion, voices in VOICES.items():
        available_voices = sum(1 for path in voices.values() if path.exists())
        total_voices = len(voices)

        status["companions"][companion] = {
            "name": COMPANIONS[companion]["name"],
            "icon": COMPANIONS[companion]["icon"],
            "available_voices": available_voices,
            "total_voices": total_voices,
            "ready": available_voices > 0
        }

    return jsonify(status)


def play_voice_internal(companion, voice_type):
    """Internal helper to play a voice."""
    voice_path = VOICES[companion][voice_type]

    if not voice_path.exists():
        return jsonify({
            "error": "Voice file not found",
            "path": str(voice_path)
        }), 404

    try:
        subprocess.Popen(["afplay", str(voice_path)])
        return jsonify({
            "success": True,
            "companion": companion,
            "voice_type": voice_type,
            "message": f"{COMPANIONS[companion]['name']} is speaking!"
        })
    except Exception as e:
        return jsonify({
            "error": f"Failed to play voice: {str(e)}"
        }), 500


if __name__ == '__main__':
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎤 VOX - Voice Control Application 🎤                             ║
║                                                                           ║
║  iPad-optimized web interface for AI voice companions                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

🎸 LUCY   - British/French Creative Genius (BITW 1000X)
🎵 TREVOR - American Engineering Master
⚡ ALEX   - Strategic Professional Advisor

🌐 Starting VOX server...
📱 Access on iPad: http://YOUR_MAC_IP:5555
🖥️  Local access: http://localhost:5555

Press Ctrl+C to stop
    """)

    # Get local IP
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"📱 iPad URL: http://{local_ip}:5555\n")
    except:
        pass

    app.run(host='0.0.0.0', port=5555, debug=True)
