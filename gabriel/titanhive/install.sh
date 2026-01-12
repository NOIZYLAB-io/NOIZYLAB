#!/bin/bash
# ============================================================
#  🎤 TITANHIVE VOICE INSTALLER - M2 Ultra
# ============================================================

set -e
echo "🎤 INSTALLING TITANHIVE VOICE DEPENDENCIES..."
echo "================================================"

# Core TTS
pip3 install --quiet edge-tts gtts pydub requests

# AI Integration
pip3 install --quiet google-generativeai openai

# Whisper (optional - large download)
read -p "📢 Install Whisper for transcription? (~1GB) [y/N]: " install_whisper
if [[ "$install_whisper" =~ ^[Yy]$ ]]; then
    pip3 install openai-whisper
fi

# Verify
echo ""
echo "✅ VERIFICATION:"
echo "─────────────────"
python3 -c "import edge_tts; print('  ✓ Edge TTS')" 2>/dev/null || echo "  ✗ Edge TTS"
python3 -c "import gtts; print('  ✓ gTTS')" 2>/dev/null || echo "  ✗ gTTS"
python3 -c "import pydub; print('  ✓ Pydub')" 2>/dev/null || echo "  ✗ Pydub"
python3 -c "import google.generativeai; print('  ✓ Gemini')" 2>/dev/null || echo "  ✗ Gemini"
python3 -c "import openai; print('  ✓ OpenAI')" 2>/dev/null || echo "  ✗ OpenAI"
python3 -c "import whisper; print('  ✓ Whisper')" 2>/dev/null || echo "  ○ Whisper (not installed)"

# Check ffmpeg
which ffmpeg >/dev/null 2>&1 && echo "  ✓ FFmpeg" || echo "  ✗ FFmpeg (brew install ffmpeg)"

echo ""
echo "🎉 INSTALLATION COMPLETE!"
echo ""
echo "🔊 TEST VOICE:"
echo "  python3 titanhive/voice.py speak \"Hello from M2 Ultra!\""
echo ""
echo "💬 START CHAT:"
echo "  python3 titanhive/voice.py chat"
