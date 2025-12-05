#!/bin/zsh
# Converts module text into warm-male narration (MP3 + WAV)

# location of the module text
SRC="$PWD/$(ls */module.txt | head -n 1)"
OUT_DIR="$(dirname "$SRC")"

echo "🎙️ Generating FocusWalk Edition from: $SRC"

# choose your warm male voice — list available ones with: say -v "?"
VOICE="Daniel"          # you can change to Oliver, Alex, etc.
RATE=170                # words per minute

# create temporary AIFF, then convert
say -v "$VOICE" -r $RATE -o "$OUT_DIR/module_temp.aiff" -f "$SRC"

# Convert to MP3 and WAV
afconvert "$OUT_DIR/module_temp.aiff" "$OUT_DIR/$(basename $OUT_DIR)_FocusWalk.mp3" -f mp3
afconvert "$OUT_DIR/module_temp.aiff" "$OUT_DIR/$(basename $OUT_DIR)_FocusWalk.wav" -f WAVE

# clean up
rm "$OUT_DIR/module_temp.aiff"

# copy transcript and make playlist
cp "$SRC" "$OUT_DIR/$(basename $OUT_DIR)_FocusWalk_Transcript.txt"
echo "$OUT_DIR/$(basename $OUT_DIR)_FocusWalk.mp3" > "$OUT_DIR/_playlist.m3u"

echo "✅ Audio files and transcript created in $OUT_DIR"
