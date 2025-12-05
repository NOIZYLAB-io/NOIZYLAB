#!/bin/zsh

echo "🧠 Testing SleepLearning AutoSave System..."
cd /Users/rsp_ms/SleepLearning_AppleTechCourse

# Ensure backup folder exists
mkdir -p "./Backups"

# Load local TTS env if present (for LaunchAgent compatibility)
if [[ -f "./tts.env" ]]; then
    set -a
    source ./tts.env
    set +a
fi

# Try to pull API key from macOS Keychain if not set
if [[ -z "${ELEVENLABS_API_KEY}" ]]; then
    # Try launchctl environment (persisted user env vars)
    KEY_FROM_LAUNCHCTL=$(launchctl getenv ELEVENLABS_API_KEY 2>/dev/null || true)
    if [[ -n "${KEY_FROM_LAUNCHCTL}" ]]; then
        export ELEVENLABS_API_KEY="${KEY_FROM_LAUNCHCTL}"
    fi
fi

if [[ -z "${ELEVENLABS_API_KEY}" ]]; then
    KEY_FROM_KC=$(security find-generic-password -a "$USER" -s "ElevenLabsAPIKey" -w 2>/dev/null || true)
    if [[ -n "${KEY_FROM_KC}" ]]; then
        export ELEVENLABS_API_KEY="${KEY_FROM_KC}"
    fi
fi

if [[ -z "${ELEVENLABS_API_KEY}" ]]; then
    KEY_FROM_KC2=$(security find-generic-password -a "$USER" -s "ELEVENLABS_API_KEY" -w 2>/dev/null || true)
    if [[ -n "${KEY_FROM_KC2}" ]]; then
        export ELEVENLABS_API_KEY="${KEY_FROM_KC2}"
    fi
fi

# -------- TTS Helpers (ElevenLabs Sarah preferred) --------
# Usage priority:
# 1) ElevenLabs (voice Sarah by default) if ELEVENLABS_API_KEY is set
# 2) macOS Siri voice "Kate" if available
# 3) macOS voice "Daniel" as safe fallback

gen_with_elevenlabs() {
    local infile="$1"
    local outbase="$2"
    local voice_name="${ELEVEN_VOICE:-Sarah}"
    if [[ -z "${ELEVENLABS_API_KEY}" ]]; then
        return 1
    fi
    if [[ ! -x "./elevenlabs_tts.py" ]]; then
        return 1
    fi
    echo "🔊 ElevenLabs: generating ${outbase}.mp3 (voice: ${voice_name})"
    python3 ./elevenlabs_tts.py --text-file "$infile" --out "./Backups/${outbase}.mp3" --voice "${voice_name}" || return 1
    return 0
}

detect_mac_voice() {
    # Prefer Kate if present, else Daniel
    if /usr/bin/say -v '?' | grep -qi '^Kate\b'; then
        echo "Kate"
    else
        echo "Daniel"
    fi
}

gen_with_say() {
    local infile="$1"
    local outbase="$2"
    local rate="${TTS_RATE:-170}"
    local voice="${MAC_VOICE:-$(detect_mac_voice)}"
    echo "🗣️ macOS say: generating ${outbase}.aiff (voice: ${voice}, rate: ${rate})"
    /usr/bin/say -v "${voice}" -r "${rate}" -o "./Backups/${outbase}.aiff" -f "$infile" || return 1
    # Convert to WAV for max compatibility
    afconvert -f WAVE -d LEI16 "./Backups/${outbase}.aiff" "./Backups/${outbase}.wav" >/dev/null 2>&1 || true
    return 0
}

generate_audio_for_text() {
    local infile="$1"
    local base="$2"
    # Try ElevenLabs first; fallback to macOS say
    if ! gen_with_elevenlabs "$infile" "$base"; then
        gen_with_say "$infile" "$base"
    fi
}
# ----------------------------------------------------------

# Find recently modified files (last 5 minutes for testing)
echo "Looking for recently modified files..."
find . -type f \( -name "*.txt" -o -name "*.mp3" \) -mmin -5 | while read FILE; do
    echo "Found: $FILE"
    
    # Create backup with timestamp
    BASENAME=$(basename "$FILE")
    BACKUP_PATH="./Backups/$BASENAME"
    
    if [[ -e "$BACKUP_PATH" ]]; then
        TS=$(date +%Y%m%d_%H%M%S)
        cp "$FILE" "./Backups/${BASENAME}_$TS" 2>/dev/null
        echo "✅ Versioned backup: ${BASENAME}_$TS"
    else
        cp "$FILE" "$BACKUP_PATH" 2>/dev/null
        echo "✅ Initial backup: $BASENAME"
    fi
    
    # If it's a text file, generate audio
    if [[ "$FILE" == *.txt ]]; then
        echo "🎵 Generating audio for: $BASENAME"
        generate_audio_for_text "$FILE" "${BASENAME%.*}_audio"
        echo "🎧 Audio generated (mp3/aiff/wav where available)"
    fi
done

echo ""
echo "📊 Backup Summary:"
ls -la ./Backups/
echo ""
echo "✨ AutoSave test complete!"