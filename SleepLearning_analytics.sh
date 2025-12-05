#!/bin/zsh
LOGFILE="$PWD/Backups/playback.log"
echo "SleepLearning Analytics Report"
echo "Most played modules:"
cut -d ' ' -f 4 "$LOGFILE" | sort | uniq -c | sort -nr | head -10
echo "Modules needing more review:"
# (Add logic to identify least played modules)
