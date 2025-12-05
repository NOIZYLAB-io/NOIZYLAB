#!/bin/zsh
# SleepLearning Diagnostics & Self-Healing Script
set -e

# 1. Check Python
if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ Python3 not found. Please install Python3."
  exit 1
fi
PYVER=$(python3 -c 'import sys; print(sys.version.split()[0])')
echo "✅ Python3 found: $PYVER"

# 2. Check pip & dependencies
if ! command -v pip3 >/dev/null 2>&1; then
  echo "❌ pip3 not found. Please install pip3."
  exit 2
fi
REQUIRED_PKGS=(certifi requests)
for PKG in "${REQUIRED_PKGS[@]}"; do
  python3 -c "import $PKG" 2>/dev/null || {
    echo "Installing missing Python package: $PKG"
    pip3 install --user $PKG
  }
done
echo "✅ Python dependencies ready."

# 3. Check ElevenLabs API Key
KEY=$(security find-generic-password -a "$USER" -s "ElevenLabsAPIKey" -w 2>/dev/null || echo "")
if [[ -z "$KEY" ]]; then
  echo "❌ ElevenLabs API Key not found in Keychain. Run setup_elevenlabs_key.sh to add."
else
  echo "✅ ElevenLabs API Key found in Keychain."
fi

# 4. Check Siri voices
say -v | grep -i "Kate" >/dev/null && echo "✅ Siri 'Kate' voice available." || echo "❌ Siri 'Kate' voice missing."
say -v | grep -i "Daniel" >/dev/null && echo "✅ Siri 'Daniel' voice available." || echo "❌ Siri 'Daniel' voice missing."

# 5. Check iCloud sync
ICLOUD_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning"
if [[ -d "$ICLOUD_DIR" ]]; then
  echo "✅ iCloud SleepLearning folder found."
else
  echo "❌ iCloud SleepLearning folder missing. Please enable iCloud Drive."
fi

# 6. Check playlist
ls "$ICLOUD_DIR"/*.m3u 2>/dev/null && echo "✅ Playlist(s) found in iCloud." || echo "❌ No playlist found in iCloud."

# 7. Log results
LOG=./diagnostics_$(date +%Y%m%d_%H%M%S).log
exec > >(tee "$LOG") 2>&1

echo "\n🎯 Diagnostics complete. See $LOG for details."
