#!/bin/bash
# NOIZYLAB Media Sync - Audio/Video to Google Drive
# Code → GitHub | Media → Google Drive

# Use env vars - NOIZYLAB_GDRIVE must be set for Google Drive sync
# Example: export NOIZYLAB_GDRIVE="$HOME/Library/CloudStorage/GoogleDrive-YOUR_EMAIL/My Drive/NOIZYLAB_MEDIA"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NOIZYLAB="${NOIZYLAB_HOME:-$(dirname "$SCRIPT_DIR")}"
GDRIVE="${NOIZYLAB_GDRIVE:-}"

# Verify GDRIVE is set for push/pull operations
check_gdrive() {
    if [ -z "$GDRIVE" ]; then
        echo "❌ Error: NOIZYLAB_GDRIVE environment variable is not set"
        echo ""
        echo "Set it in your shell profile:"
        echo "  export NOIZYLAB_GDRIVE=\"\$HOME/Library/CloudStorage/GoogleDrive-YOUR_EMAIL/My Drive/NOIZYLAB_MEDIA\""
        exit 1
    fi
}

echo "🎵 NOIZYLAB Media Sync"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Source: $NOIZYLAB"
echo "Target: $GDRIVE"
echo ""

case "$1" in
  push)
    check_gdrive
    echo "📤 Pushing media to Google Drive..."
    # Sync audio files
    rsync -avh --progress --include='*.wav' --include='*.mp3' --include='*.flac' \
          --include='*.aif' --include='*.aiff' --include='*.m4a' --include='*.ogg' \
          --include='*/' --exclude='*' "$NOIZYLAB/" "$GDRIVE/Audio/"
    # Sync video files
    rsync -avh --progress --include='*.mov' --include='*.mp4' --include='*.avi' \
          --include='*.mkv' --include='*.webm' --include='*/' --exclude='*' \
          "$NOIZYLAB/" "$GDRIVE/Video/"
    echo "✅ Media pushed to Google Drive"
    ;;
  pull)
    check_gdrive
    echo "📥 Pulling media from Google Drive..."
    rsync -avh --progress "$GDRIVE/" "$NOIZYLAB/media/"
    echo "✅ Media pulled from Google Drive"
    ;;
  status)
    check_gdrive
    echo "📊 Google Drive NOIZYLAB_MEDIA:"
    du -sh "$GDRIVE"/* 2>/dev/null || echo "  (empty or not synced)"
    ;;
  *)
    echo "Usage: $0 {push|pull|status}"
    echo ""
    echo "  push   - Send local audio/video to Google Drive"
    echo "  pull   - Get audio/video from Google Drive"
    echo "  status - Show Google Drive media stats"
    exit 1
    ;;
esac
