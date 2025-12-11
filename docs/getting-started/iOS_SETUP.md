# iPhone & iPad Setup for SleepLearning

This connects your Mac’s generated audio to your iPhone/iPad automatically via iCloud Drive, with simple ways to play the newest lesson.

## What’s already set up
- AutoRun watches your course folder. When you add or update a .txt file, it generates audio (prefers ElevenLabs Sarah, falls back to Siri Kate/Daniel) and saves it to:
  - iCloud Drive > SleepLearning > Backups (full archive, synced)
  - iCloud Drive > SleepLearning > Latest (stable names like latest.m4a)
- A playlist is also generated at iCloud Drive > SleepLearning > Backups > playlist.m3u

## On iPhone/iPad (Files app)
- Open Files app → iCloud Drive → SleepLearning:
  - Backups: full set of audio files (mp3/wav/aiff)
  - Latest: latest.mp3 (or latest.m4a/wav/aiff) for quick play
  - Backups/playlist.m3u: a playlist with most-recent-first

## Quick Play options
1) Apple Shortcuts (recommended)
- Create a Shortcut named “Play Latest SleepLearning”:
  - Action: Get File → iCloud Drive → SleepLearning/Latest/latest.m4a (or latest.mp3)
  - Action: Play Sound (or Open In…) → choose your player (Music, VLC, Files Preview)
  - Optional: Add to Home Screen and set Automation: Time of Day (e.g., bedtime)

2) Use VLC or Podcasts
- VLC can open playlist.m3u directly from Files → iCloud Drive → SleepLearning → Backups
- Or, open individual files and add them to a playlist in your preferred app

## Troubleshooting
- If you don’t see SleepLearning in iCloud Drive:
  - Settings → [your name] → iCloud → iCloud Drive → ON
  - Ensure Desktop & Documents syncing is ON (if you want broader coverage)
  - Give a minute for sync after new audio is generated
- Audio format not playing?: use latest.m4a which we generate specifically for iOS compatibility
- Want lower file sizes?: ElevenLabs MP3 is compact; macOS fallback makes WAV + M4A for iOS

## Power tips
- Set a Bedtime Focus Automation in Shortcuts to auto-play Latest
- Share playlist.m3u to Apple Music/VLC for curated sessions
- Use AirPlay or Bluetooth to stream while charging
