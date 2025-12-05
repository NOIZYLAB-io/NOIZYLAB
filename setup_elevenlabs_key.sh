#!/bin/zsh
# Setup ElevenLabs API key securely and test Sarah voice
set -e

echo "🗝️ ElevenLabs API Key Setup"

# Ensure we run from project dir
cd /Users/rsp_ms/Desktop/MissionControl96

# Ensure curl exists
if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required. Please install it (brew install curl)"
  exit 1
fi

retry_count=0
max_retries=3
while : ; do
  # Prompt for key (silent) if not in env
  if [[ -z "${ELEVENLABS_API_KEY}" && -z "${KEY:-}" ]]; then
    read -s "KEY?Paste your ELEVENLABS_API_KEY (Profile → API Keys) and press Enter: "
    echo ""
  else
    KEY="${KEY:-${ELEVENLABS_API_KEY}}"
  fi

  # Trim leading/trailing whitespace
  KEY=$(python3 - <<'PY'
import sys
print(sys.stdin.read().strip())
PY
<<<"$KEY")

  if [[ -z "$KEY" ]]; then
    echo "No key provided. Aborting."
    exit 2
  fi

  echo "🔎 Validating key with ElevenLabs..."
  HTTP_CODE=$(curl -sS -o /tmp/voices.json -w "%{http_code}" -H "xi-api-key: $KEY" -H "accept: application/json" https://api.elevenlabs.io/v1/voices || true)
  if [[ "$HTTP_CODE" == "200" ]]; then
    break
  fi

  echo ""
  echo "❌ Validation failed (HTTP $HTTP_CODE)."
  if [[ "$HTTP_CODE" == "401" ]]; then
    echo "→ The key is unauthorized. Make sure it's an ElevenLabs API Key from Profile → API Keys (not a project token)."
  fi
  cat /tmp/voices.json 2>/dev/null || true
  ((retry_count++))
  if (( retry_count >= max_retries )); then
    echo "Exceeded retries. Aborting."
    exit 3
  fi
  unset ELEVENLABS_API_KEY
  unset KEY
  echo ""
  echo "Please try pasting the API key again:"
done

# Try to extract Sarah voice_id
SARAH_ID=$(python3 - <<'PY'
import json,sys
try:
    data=json.load(open('/tmp/voices.json'))
    for v in data.get('voices',[]):
        if v.get('name','').lower()=='sarah':
            print(v.get('voice_id',''))
            sys.exit(0)
    sys.exit(1)
except Exception as e:
    sys.exit(1)
PY
)

# Store in Keychain
echo "🔐 Storing key in macOS Keychain (service: ElevenLabsAPIKey)"
security add-generic-password -a "$USER" -s "ElevenLabsAPIKey" -w "$KEY" -U >/dev/null

# Export to launchctl env for LaunchAgents
launchctl setenv ELEVENLABS_API_KEY "$KEY" || true

# Optionally store Sarah voice_id for faster runs
if [[ -n "$SARAH_ID" ]]; then
  echo "✅ Found Sarah voice_id: $SARAH_ID"
  launchctl setenv ELEVEN_VOICE_ID "$SARAH_ID" || true
else
  echo "ℹ️ Could not auto-resolve Sarah voice_id; name lookup will be used."
fi

# Test generation with Sarah
echo "🎤 Generating test with Sarah..."
TEST_TXT=/tmp/sarah_setup_test.txt
echo "This is Sarah from ElevenLabs speaking. Your SleepLearning setup is ready." > "$TEST_TXT"
mkdir -p ./Backups
# Ensure required Python packages are installed
python3 -m pip install --quiet certifi || true
export SSL_CERT_FILE=$(python3 -c 'import certifi;print(certifi.where())' 2>/dev/null || echo "")
python3 ./elevenlabs_tts.py --text-file "$TEST_TXT" --out ./Backups/sarah_setup_test.mp3 --voice Sarah

# Play result
if [[ -f ./Backups/sarah_setup_test.mp3 ]]; then
  echo "🎧 Playing test audio..."
  afplay ./Backups/sarah_setup_test.mp3 || echo "(Skipped playback)"
  echo "✅ ElevenLabs Sarah voice is ready."
else
  echo "❌ Test MP3 not created. Check logs above."
fi

python mission_control.py

# In mcp_server.py

class MCPClient:
    def __init__(self):
        # Initialize connection or state
        pass

    def send_event(self, event_type, data):
        # Example event sending logic
        print(f"Event sent: {event_type} with data: {data}")

from mcp_server import MCPClient as EventBus

bus = EventBus()
bus.send_event("speak", {"text": "Hello from Sarah"})

@app.get("/fetch/diagnostics")
def fetch_diagnostics():
    return mcp_client.diagnostics()

app = FastAPI()
mcp_client = MCPClient()
