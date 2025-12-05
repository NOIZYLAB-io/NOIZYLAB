# Save as: ~/Desktop/NoizyFish/scripts/noizyfish_ongoing_setup.sh

#!/bin/zsh

set -e

echo "🧹 Flushing CoreAudio and UAD..."
sudo launchctl kickstart -k system/com.apple.audio.coreaudiod
killall "UA Mixer Engine" "UAD Meter & Control Panel" "Console" 2>/dev/null || true
sleep 2
open -a "Console"
echo "✅ Audio environment reset."

echo "🔧 Setting up Webador migration Python environment..."
cd ~/Desktop/NoizyFish/utilities/webador_migrate
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip selenium webdriver-manager requests msal
echo "✅ Python environment ready!"

echo "📦 Running Webador extraction..."
export WEBADOR_EMAIL="your-email@example.com"
export WEBADOR_PASS="your-password"
export OUTPUT_DIR=~/Desktop/NoizyFish/utilities/webador_migrate/output
mkdir -p "$OUTPUT_DIR"
python webador_extract.py
echo "✅ Webador extraction complete!"

echo "🗣️ Running Sarah voice (ElevenLabs) test..."
cd ~/Desktop/NoizyFish/scripts
export ELEVENLABS_API_KEY="your-elevenlabs-api-key"
export SARAH_VOICE_ID="EXAVITQu4vr4xnSDxMaL"
python elevenlabs_sarah_voice.py "Hello from Sarah!"
echo "✅ Sarah voice test complete!"

echo "🚀 NoizyFish streamlined setup finished!"

chmod +x ~/Desktop/NoizyFish/scripts/noizyfish_ongoing_setup.sh
