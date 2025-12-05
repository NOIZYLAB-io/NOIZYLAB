#!/bin/zsh
# === Mission Certified: Audio Generation Engine ===
# Converts every module.txt in subfolders into FocusWalk WAV + MP3 narration

ROOT="$PWD"
VOICE="Daniel"          # Warm male voice on macOS
RATE=170                # Speech speed
DATE=$(date "+%Y-%m-%d_%H-%M")

echo "🎧 Generating narrated audio for all modules under $ROOT"
echo "Voice: $VOICE  •  Rate: $RATE wpm"

for MODULE in $(find "$ROOT" -type f -name "module.txt"); do
  DIR=$(dirname "$MODULE")
  NAME=$(basename "$DIR")
  echo "---- Processing $NAME ----"

  # Temporary aiff path
  TMP="$DIR/${NAME}_temp.aiff"

  # Generate narration
  say -v "$VOICE" -r $RATE -o "$TMP" -f "$MODULE"

  # Convert to MP3 and WAV
  afconvert "$TMP" "$DIR/${NAME}_FocusWalk.mp3" -f mp3
  afconvert "$TMP" "$DIR/${NAME}_FocusWalk.wav" -f WAVE

  # Clean up
  rm "$TMP"

  # Copy transcript + playlist
  cp "$MODULE" "$DIR/${NAME}_FocusWalk_Transcript.txt"
  echo "$DIR/${NAME}_FocusWalk.mp3" > "$DIR/_playlist.m3u"

  # Log result
  echo "$(date "+%Y-%m-%d %H:%M")  $NAME  →  Audio created" \
    >> "$ROOT/audio_generation_log.txt"
  echo "✅  $NAME complete"
done

echo "All modules processed."
echo "Audio files are in their respective module folders."
