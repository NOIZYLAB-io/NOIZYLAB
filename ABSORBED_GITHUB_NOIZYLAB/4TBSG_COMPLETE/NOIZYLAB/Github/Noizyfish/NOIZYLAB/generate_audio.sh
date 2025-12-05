
#!/bin/zsh
# Robust Apple DeviceSupport audio generator

SRC="./module.txt"
OUT="."
AIFF="$OUT/01_DeviceSupport_FocusWalk.aiff"
MP3="$OUT/01_DeviceSupport_FocusWalk.mp3"
WAV="$OUT/01_DeviceSupport_FocusWalk.wav"
TRANSCRIPT="$OUT/01_DeviceSupport_FocusWalk_Transcript.txt"
PLAYLIST="$OUT/_playlist.m3u"

if [[ ! -f "$SRC" ]]; then
	echo "❌ ERROR: $SRC not found. Please create your module.txt first."
	exit 1
fi

# Generate AIFF audio from text using the real macOS say command
/usr/bin/say -v "Daniel" -r 170 -o "$AIFF" -f "$SRC"
if [[ ! -f "$AIFF" ]]; then
	echo "❌ ERROR: AIFF file was not created."
	exit 2
fi



# Ensure ffmpeg is available in PATH
export PATH="/opt/homebrew/bin:$PATH"

# Convert AIFF to MP3 using ffmpeg (retry until success)
for i in {1..3}; do
	ffmpeg -y -i "$AIFF" "$MP3" && break
	sleep 1
done
if [[ ! -f "$MP3" ]]; then
	echo "❌ ERROR: MP3 file was not created."
else
	echo "✅ MP3 file created: $MP3"
fi

# Convert AIFF to WAV using afconvert (retry until success)
for i in {1..3}; do
	afconvert -f WAVE -d LEI16 "$AIFF" "$WAV" && break
	sleep 1
done
if [[ ! -f "$WAV" ]]; then
	echo "❌ ERROR: WAV file was not created."
else
	echo "✅ WAV file created: $WAV"
fi

# Clean up intermediate files
rm -f "$AIFF" test_output.aiff

# Remove intermediate AIFF file
rm "$AIFF"

# Create playlist and transcript copy
echo "$MP3" > "$PLAYLIST"
cp "$SRC" "$TRANSCRIPT"

echo "✅ Audio, transcript, and playlist created in $OUT"
