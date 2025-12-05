#!/bin/zsh
export PATH="/opt/homebrew/bin:$PATH"

# Set the working directory to the SleepLearning project
cd "$(dirname "$0")"
WATCH_DIR="$PWD"

echo "🧠 SleepLearning AutoSave + AutoRun engaged..."
echo "Monitoring folder: $WATCH_DIR"
echo "Press Ctrl+C to stop."

# Use standard macOS find command
echo "Using system find command..."

# Load local TTS env if present (for LaunchAgent compatibility)
if [[ -f "./tts.env" ]]; then
  set -a
  source ./tts.env
  set +a
fi

# Try to pull API key from macOS Keychain if not set
if [[ -z "${ELEVENLABS_API_KEY}" ]]; then
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
# ELEVENLABS_API_KEY env var enables ElevenLabs usage
# ELEVEN_VOICE can override default "Sarah"
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
  afconvert -f WAVE -d LEI16 "./Backups/${outbase}.aiff" "./Backups/${outbase}.wav" >/dev/null 2>&1 || true
  return 0
}

generate_audio_for_text() {
  local infile="$1"
  local base="$2"
  if ! gen_with_elevenlabs "$infile" "$base"; then
    gen_with_say "$infile" "$base"
  fi
}
# ----------------------------------------------------------

# Avoid reloading launch agents here to prevent noisy errors when run by launchd
# If you need to reload, do it manually outside this script.

while true; do
  find "$WATCH_DIR" -type f \( -name "*.txt" -o -name "*.mp3" \) -mmin -1 | while read FILE; do
    # Ensure backup folder exists
    mkdir -p "$WATCH_DIR/Backups"

    # Version backup: copy with timestamp if file already exists
    BASENAME=$(basename "$FILE")
    BACKUP_PATH="$WATCH_DIR/Backups/$BASENAME"
    if [[ -e "$BACKUP_PATH" ]]; then
      TS=$(date +%Y%m%d_%H%M%S)
      cp "$FILE" "$WATCH_DIR/Backups/${BASENAME}_$TS" 2>/dev/null
    else
      cp "$FILE" "$BACKUP_PATH" 2>/dev/null
    fi
    # Optional: sync with cloud (uncomment and configure)
    # rsync -a "$WATCH_DIR/Backups/" /path/to/your/cloud/folder/

    # If it's a text file, generate/update audio using ElevenLabs Sarah with macOS fallback
    if [[ "$FILE" == *.txt ]]; then
      TEXTBASE="${BASENAME%.*}_audio"
      echo "🎵 Generating audio for: $BASENAME -> $TEXTBASE"
      generate_audio_for_text "$FILE" "$TEXTBASE"
      # Auto-play preference: MP3 > WAV > AIFF
      if [[ -f "$WATCH_DIR/Backups/${TEXTBASE}.mp3" ]]; then
        afplay "$WATCH_DIR/Backups/${TEXTBASE}.mp3" >/dev/null 2>&1 &
      elif [[ -f "$WATCH_DIR/Backups/${TEXTBASE}.wav" ]]; then
        afplay "$WATCH_DIR/Backups/${TEXTBASE}.wav" >/dev/null 2>&1 &
      elif [[ -f "$WATCH_DIR/Backups/${TEXTBASE}.aiff" ]]; then
        afplay "$WATCH_DIR/Backups/${TEXTBASE}.aiff" >/dev/null 2>&1 &
      fi
    fi

    # Auto-run new audio files with playback logging
    if [[ "$FILE" == *.mp3 ]]; then
      LOGFILE="$WATCH_DIR/Backups/playback.log"
      TS=$(date '+%Y-%m-%d %H:%M:%S')
      echo "[$TS] Played: $BASENAME" >> "$LOGFILE"
      echo "🎧 Playing: $BASENAME"
      afplay "$FILE" &
    fi
  done

  # After processing recent files, sync Backups to iCloud Drive for iOS devices
  ICLOUD_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning/Backups"
  mkdir -p "$ICLOUD_DIR"
  rsync -a --delete "$WATCH_DIR/Backups/" "$ICLOUD_DIR/" >/dev/null 2>&1 || true

  # Also publish a stable "Latest" file for easy iOS Shortcuts access
  LATEST_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning/Latest"
  mkdir -p "$LATEST_DIR"
  # Find newest audio in Backups
  LATEST_SRC=$(ls -1t "$WATCH_DIR/Backups" 2>/dev/null | grep -E '\\.(mp3|wav|aiff)$' | head -1 || true)
  if [[ -n "$LATEST_SRC" ]]; then
    # Copy with stable names; prefer mp3, else wav, else aiff
    EXT="${LATEST_SRC##*.}"
    SRC_PATH="$WATCH_DIR/Backups/$LATEST_SRC"
    case "$EXT" in
      mp3)
        cp -f "$SRC_PATH" "$LATEST_DIR/latest.mp3" 2>/dev/null || true
        # Optional: also produce m4a for iOS
        afconvert -f m4af -d aac "$SRC_PATH" "$LATEST_DIR/latest.m4a" >/dev/null 2>&1 || true
        ;;
      wav)
        cp -f "$SRC_PATH" "$LATEST_DIR/latest.wav" 2>/dev/null || true
        afconvert -f m4af -d aac "$SRC_PATH" "$LATEST_DIR/latest.m4a" >/dev/null 2>&1 || true
        ;;
      aiff|aif|aifc)
        cp -f "$SRC_PATH" "$LATEST_DIR/latest.aiff" 2>/dev/null || true
        afconvert -f m4af -d aac "$SRC_PATH" "$LATEST_DIR/latest.m4a" >/dev/null 2>&1 || true
        ;;
    esac
  fi

  # Generate a simple M3U playlist (most recent first) for apps like VLC
  PLAYLIST="$HOME/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning/Backups/playlist.m3u"
  (
    echo "#EXTM3U"
    ls -1t "$WATCH_DIR/Backups" | grep -E '\\.(mp3|wav|aiff)$' | while read f; do
      echo "../Backups/$f"
    done
  ) > "$PLAYLIST" 2>/dev/null || true

  sleep 60
done

# Note: Auxiliary/demo code removed. Core watcher remains focused.
