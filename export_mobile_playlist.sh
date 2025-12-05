#!/bin/zsh
SOURCE=~/SleepLearning_AppleTechCourse
DEST=~/Desktop/MobileLearning
mkdir -p "$DEST"

# Copy all MP3 modules and metadata
find "$SOURCE" -type f -name "*.mp3" -exec cp -u {} "$DEST" \;

echo "🎧 Mobile playlist ready at $DEST/_playlist.m3u"
# Create a randomized playlist for variety
MP3_COUNT=$(ls "$DEST"/*.mp3 2>/dev/null | wc -l)
if [[ $MP3_COUNT -gt 0 ]]; then
	ls "$DEST"/*.mp3 | gshuf > "$DEST"/_playlist.m3u
	echo "🎧 Mobile playlist ready at $DEST/_playlist.m3u"
else
	echo "⚠️ No MP3 files found in $DEST. Please add audio files to generate a playlist."
fi
