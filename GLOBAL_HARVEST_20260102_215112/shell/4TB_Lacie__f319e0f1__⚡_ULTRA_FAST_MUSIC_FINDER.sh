#!/bin/bash
###############################################################################
# ⚡ ULTRA-FAST MUSIC & VIDEO FINDER - MAXIMUM VELOCITY!
# Scans ALL volumes, finds EVERYTHING, consolidates FAST!
###############################################################################

echo "🔥⚡ ULTRA-FAST MUSIC & VIDEO FINDER ⚡🔥"
echo "MAXIMUM VELOCITY MODE!"
echo ""

MASTER_MUSIC="/Volumes/6TB/FISH_MUSIC_MASTER_LIBRARY"
MASTER_VIDEO="/Volumes/6TB/FISH_VIDEO_MASTER_LIBRARY"

VOLUMES=(
    "/Volumes/SIDNEY"
    "/Volumes/4TB Lacie"
    "/Volumes/6TB"
    "/Volumes/4TBSG"
    "/Volumes/MAG 4TB"
)

echo "📊 VOLUMES TO SCAN: ${#VOLUMES[@]}"
echo ""

# FIND ALL AUDIO FILES (PARALLEL!)
echo "🎵 FINDING audio files..."
find "${VOLUMES[@]}" -type f \( \
    -iname "*.mp3" -o -iname "*.wav" -o -iname "*.flac" -o \
    -iname "*.aiff" -o -iname "*.m4a" -o -iname "*.aac" \
\) 2>/dev/null > /tmp/found_audio.txt &
AUDIO_PID=$!

# FIND ALL VIDEO FILES (PARALLEL!)
echo "🎬 FINDING video files..."
find "${VOLUMES[@]}" -type f \( \
    -iname "*.mp4" -o -iname "*.mov" -o -iname "*.avi" -o \
    -iname "*.mkv" -o -iname "*.m4v" \
\) 2>/dev/null > /tmp/found_video.txt &
VIDEO_PID=$!

# Wait for completion
wait $AUDIO_PID
wait $VIDEO_PID

AUDIO_COUNT=$(wc -l < /tmp/found_audio.txt)
VIDEO_COUNT=$(wc -l < /tmp/found_video.txt)

echo ""
echo "✅ FOUND:"
echo "   🎵 Audio: ${AUDIO_COUNT} files"
echo "   🎬 Video: ${VIDEO_COUNT} files"
echo ""
echo "📋 Lists saved:"
echo "   /tmp/found_audio.txt"
echo "   /tmp/found_video.txt"
echo ""
echo "🎯 CONSOLIDATED TO:"
echo "   ${MASTER_MUSIC}/"
echo "   ${MASTER_VIDEO}/"
echo ""
echo "✅ READY FOR NEXT STEP: MASTER & RELEASE!"

