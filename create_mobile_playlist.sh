#!/bin/zsh
SOURCE=~/SleepLearning_AppleTechCourse
DEST=~/Desktop/MobileLearning
mkdir -p "$DEST"

# Copy all MP3 modules and metadata
find "$SOURCE" -type f -name "*.mp3" -exec cp -u {} "$DEST" \;

# Create a randomized playlist for variety
ls "$DEST"/*.mp3 | shuf > "$DEST"/_playlist.m3u

echo "🎧 Mobile playlist ready at $DEST/_playlist.m3u"
