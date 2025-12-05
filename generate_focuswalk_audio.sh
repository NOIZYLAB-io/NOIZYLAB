#!/bin/zsh
# Converts text modules into warm male voice audio (MP3 + WAV)

SRC="$PWD/01_DeviceSupport/module.txt"
OUT="$PWD/01_DeviceSupport"

echo "🎙️ Generating FocusWalk Edition..."
# macOS built-in TTS voice (Daniel is a good warm male)
say -v "Daniel" -r 170 -o "$OUT/01_DeviceSupport_FocusWalk.aiff" -f "$SRC"

# Convert AIFF to MP3 and WAV
afconvert "$OUT/01_DeviceSupport_FocusWalk.aiff" "$OUT/01_DeviceSupport_FocusWalk.mp3" -f mp3
afconvert "$OUT/01_DeviceSupport_FocusWalk.aiff" "$OUT/01_DeviceSupport_FocusWalk.wav" -f WAVE

# Clean up intermediate
rm "$OUT/01_DeviceSupport_FocusWalk.aiff"

# Create simple playlist and transcript copy
echo "$OUT/01_DeviceSupport_FocusWalk.mp3" > "$OUT/_playlist.m3u"
cp "$SRC" "$OUT/01_DeviceSupport_FocusWalk_Transcript.txt"

echo "✅ FocusWalk audio, transcript, and playlist created in $OUT"
