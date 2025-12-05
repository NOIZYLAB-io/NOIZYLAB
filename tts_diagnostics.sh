#!/bin/zsh
# Quick diagnostics for TTS setup (ElevenLabs + macOS say)
set -euo pipefail
cd "$(dirname "$0")"

echo "=== TTS Diagnostics ==="

# Check macOS say
if /usr/bin/say -v '?' | grep -qi '^Kate\b'; then
  echo "macOS voice: Kate available"
else
  echo "macOS voice: Kate not listed, will fallback to Daniel"
fi

# Check certifi
if python3 -c 'import certifi,sys;print(certifi.where())' >/dev/null 2>&1; then
  echo "Python certifi: OK"
else
  echo "Python certifi: MISSING (pip install certifi)"
fi

# Show Backups
mkdir -p ./Backups
ls -lh ./Backups | sed 's/^/Backups: /'

# Try environment sources for ElevenLabs
if [[ -f ./tts.env ]]; then echo "env: tts.env present"; else echo "env: tts.env absent"; fi
if launchctl getenv ELEVENLABS_API_KEY >/dev/null 2>&1; then echo "env: launchctl ELEVENLABS_API_KEY present"; else echo "env: launchctl ELEVENLABS_API_KEY absent"; fi
if security find-generic-password -a "$USER" -s "ElevenLabsAPIKey" -w >/dev/null 2>&1; then echo "env: Keychain ElevenLabsAPIKey present"; else echo "env: Keychain ElevenLabsAPIKey absent"; fi

# Attempt Sarah test (will fail with clear message if key invalid)
export SSL_CERT_FILE=$(python3 -c 'import certifi;print(certifi.where())' 2>/dev/null || echo "")
echo "Sarah diagnostics test" > /tmp/sarah_diag.txt
set +e
python3 ./elevenlabs_tts.py --text-file /tmp/sarah_diag.txt --out ./Backups/sarah_diag.mp3 --voice Sarah
RET=$?
set -e
if [[ $RET -eq 0 ]]; then
  echo "Sarah test: SUCCESS (./Backups/sarah_diag.mp3)"
else
  echo "Sarah test: FAILED (check ELEVENLABS_API_KEY). If you pasted the wrong key, run:"
  echo "  security delete-generic-password -a $USER -s ElevenLabsAPIKey"
  echo "  launchctl unsetenv ELEVENLABS_API_KEY"
  echo "Then re-run setup:"
  echo "  ./setup_elevenlabs_key.sh"
fi

# Always confirm local fallback works
/usr/bin/say -v "$(/usr/bin/say -v '?' | awk '/^Kate/{print $1; found=1} END{if(!found)print "Daniel"}')" -r 170 -o ./Backups/fallback_ok.aiff "Local TTS fallback is working." && afconvert -f WAVE -d LEI16 ./Backups/fallback_ok.aiff ./Backups/fallback_ok.wav >/dev/null 2>&1 && echo "Fallback test: OK (./Backups/fallback_ok.wav)"

echo "=== Done ==="