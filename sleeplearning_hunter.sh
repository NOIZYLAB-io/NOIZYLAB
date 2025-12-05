#!/usr/bin/env bash
set -euo pipefail

OUTDIR="$HOME/noizy_sleeplearning"
MONLOG="$OUTDIR/monitor.log"
FOUNDLOG="$OUTDIR/found.log"
PLIST_STAGE="$OUTDIR/staged_plists"
KEYWORDS="sleeplearning|sleep-learning|sleep learning|sleepLearning|sleep_learning|sleeplearn"
TIMESTAMP(){ date -u +"%Y-%m-%dT%H:%M:%SZ"; }

mkdir -p "$OUTDIR" "$PLIST_STAGE"
echo "$(TIMESTAMP) SleepLearning hunter started" >> "$MONLOG"

# immediate blunt silence
osascript -e "set volume output muted true" 2>/dev/null || true
pkill -f '\bsay\b' 2>/dev/null || true
pkill -f -i 'voiceover' 2>/dev/null || true
pkill -f -i 'speech' 2>/dev/null || true
pkill -f -i 'avspeech' 2>/dev/null || true
pkill -f -i 'siri' 2>/dev/null || true

# helper: record parent chain for a pid
dump_parent_chain(){
  pid=$1
  echo "=== parent chain for PID $pid at $(TIMESTAMP) ===" >> "$FOUNDLOG"
  p=$pid
  while [ "$p" -gt 1 ]; do
    ps -p $p -o pid,ppid,comm= >> "$FOUNDLOG" 2>/dev/null || true
    p=$(ps -p $p -o ppid= 2>/dev/null | tr -d ' ' || echo 1)
    if [ -z "$p" ]; then break; fi
  done
  echo "=== end chain ===" >> "$FOUNDLOG"
}

# scan existing LaunchAgents/Daemons and stage any that match key words
stage_matching_plists(){
  echo "$(TIMESTAMP) scanning plist dirs" >> "$MONLOG"
  for d in "$HOME/Library/LaunchAgents" /Library/LaunchAgents /Library/LaunchDaemons; do
    [ -d "$d" ] || continue
    while IFS= read -r f; do
      if egrep -qi "$KEYWORDS" "$f" 2>/dev/null || basename "$f" | egrep -qi "$KEYWORDS"; then
        echo "$(TIMESTAMP) matched plist: $f" >> "$MONLOG"
        mkdir -p "$PLIST_STAGE"
        cp -a "$f" "$PLIST_STAGE/" 2>/dev/null || mv "$f" "$PLIST_STAGE/" 2>/dev/null || true
        # attempt safe unload
        launchctl bootout gui/$(id -u) "$f" 2>/dev/null || launchctl bootout system "$f" 2>/dev/null || true
        echo "$(TIMESTAMP) staged and booted out: $f" >> "$FOUNDLOG"
      fi
    done < <(find "$d" -type f -name "*.plist" 2>/dev/null || true)
  done
}

# scan Shortcuts DB for entries mentioning keywords (best-effort)
scan_shortcuts_db(){
  DB="$HOME/Library/Application Support/com.apple.shortcuts/Shortcuts.sqlite"
  if [ -f "$DB" ]; then
    sqlite3 "$DB" "select ZSHORTCUT.Z_PK, ZSHORTCUT.ZNAME from ZSHORTCUT where ZSHORTCUT.ZNAME REGEXP '(?i)$KEYWORDS' COLLATE NOCASE;" 2>/dev/null >> "$MONLOG" || true
    # fallback: grep exported sqlite bin chunk
    sqlite3 "$DB" "select ZNAME from ZSHORTCUT" 2>/dev/null | egrep -i "$KEYWORDS" >> "$MONLOG" 2>/dev/null || true
  fi
}

# realtime log watcher function (captures system log lines containing keywords)
watch_logs_once(){
  log show --style syslog --last 30s --predicate "eventMessage CONTAINS[cd] \"SleepLearning\" OR eventMessage CONTAINS[cd] \"sleep-learning\" OR eventMessage CONTAINS[cd] \"sleep learning\" OR eventMessage CONTAINS[cd] \"sleeplearn\" OR eventMessage CONTAINS[cd] \"sleepLearning\"" 2>/dev/null | sed -n '1,200p' >> "$MONLOG" || true
}

# main monitor loop
stage_matching_plists

echo "$(TIMESTAMP) entering monitor loop" >> "$MONLOG"
while true; do
  # mute and kill again to prevent stacking while hunting
  osascript -e "set volume output muted true" 2>/dev/null || true
  pkill -f '\bsay\b' 2>/dev/null || true

  # 1) check live processes for keywords
  ps aux | egrep -i "$KEYWORDS" | egrep -v 'egrep|noizy_sleeplearning' >> "$MONLOG" 2>/dev/null || true
  # if found, log and dump parent chain
  for pid in $(ps aux | egrep -i "$KEYWORDS" | awk '{print $2}' | egrep -v '^(PID|)$' || true); do
    if [ -n "$pid" ]; then
      echo "$(TIMESTAMP) detected process PID $pid matching keywords" >> "$FOUNDLOG"
      ps -p $pid -o pid,ppid,comm,etime,user= >> "$FOUNDLOG" 2>/dev/null || true
      dump_parent_chain "$pid"
      # attempt to kill that exact PID (safe, non-forced)
      kill "$pid" 2>/dev/null || true
      echo "$(TIMESTAMP) attempted kill of PID $pid" >> "$FOUNDLOG"
    fi
  done

  # 2) check for any staged/remaining plists matching keywords (repeat scan)
  stage_matching_plists

  # 3) check launchctl list for names containing keywords
  launchctl list | egrep -i "$KEYWORDS" >> "$MONLOG" 2>/dev/null || true
  if launchctl list | egrep -i "$KEYWORDS" >/dev/null 2>&1; then
    launchctl list | egrep -i "$KEYWORDS" >> "$FOUNDLOG" 2>/dev/null || true
    echo "$(TIMESTAMP) launchctl reported matching agents; staging and booting out" >> "$FOUNDLOG"
    # find plist paths and move them to staged dir (best-effort)
    for p in $(ls ~/Library/LaunchAgents 2>/dev/null | egrep -i "$KEYWORDS" || true); do
      [ -f "$HOME/Library/LaunchAgents/$p" ] && cp -a "$HOME/Library/LaunchAgents/$p" "$PLIST_STAGE/" 2>/dev/null || true
      launchctl bootout gui/$(id -u) "$HOME/Library/LaunchAgents/$p" 2>/dev/null || true
      echo "$(TIMESTAMP) moved $p to staged" >> "$FOUNDLOG"
    done
  fi

  # 4) watch system logs for any recent SleepLearning mentions and snapshot surrounding lines
  watch_logs_once

  # 5) inspect Shortcuts DB for new entries that might be created on the fly
  scan_shortcuts_db

  # 6) check for new files/scripts on desktop or common locations referencing SleepLearning
  grep -R --no-messages -i -n "$KEYWORDS" "$HOME/Desktop" "$HOME" 2>/dev/null | sed -n '1,200p' >> "$MONLOG" || true

  # 7) if any matches were logged to FOUNDLOG in this iteration, break loop (we found something)
  if tail -n 200 "$FOUNDLOG" 2>/dev/null | egrep -qi "$KEYWORDS"; then
    echo "$(TIMESTAMP) match discovered; finalizing logs" >> "$MONLOG"
    # capture a wider log window and copy to OUTDIR/final_capture.log
    log show --style syslog --last 2m --predicate "eventMessage CONTAINS[cd] \"SleepLearning\" OR eventMessage CONTAINS[cd] \"sleep-learning\" OR eventMessage CONTAINS[cd] \"sleep learning\" OR eventMessage CONTAINS[cd] \"sleeplearn\" OR eventMessage CONTAINS[cd] \"sleepLearning\"" 2>/dev/null >> "$OUTDIR/final_capture.log" || true
    echo "$(TIMESTAMP) final capture saved to $OUTDIR/final_capture.log" >> "$MONLOG"
    break
  fi

  sleep 4
done

echo "$(TIMESTAMP) SleepLearning hunter stopped after finding a match (see $FOUNDLOG and $MONLOG)" >> "$MONLOG"
echo "Artifacts: $OUTDIR. To undo any plist moves, check $PLIST_STAGE for staged files." >> "$MONLOG"
