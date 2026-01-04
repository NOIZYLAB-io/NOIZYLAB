#!/usr/bin/env bash
# safari_layout_reset.sh
# Usage:
#   ./safari_layout_reset.sh --soft
#   ./safari_layout_reset.sh --hard
#   ./safari_layout_reset.sh --full
#   ./safari_layout_reset.sh --hard --no-resume
#
# --soft:  Reposition/resize open Safari windows (Safari stays running)
# --hard:  Quit Safari + delete saved window/session state folder
# --full:  --hard + remove "NSWindow Frame" keys from Safari prefs (window frame memory)
# --no-resume: make Safari stop writing Resume state by removing write permission on savedState folder (optional)

set -euo pipefail

MODE="full"
NO_RESUME="false"

for arg in "${@:-}"; do
  case "$arg" in
    --soft) MODE="soft" ;;
    --hard) MODE="hard" ;;
    --full) MODE="full" ;;
    --no-resume) NO_RESUME="true" ;;
    *) ;;
  esac
done

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This script is for macOS Safari."
  exit 1
fi

timestamp="$(date +%Y%m%d_%H%M%S)"
backup_dir="$HOME/Desktop/SafariLayoutBackups/$timestamp"
mkdir -p "$backup_dir"

saved_state="$HOME/Library/Saved Application State/com.apple.Safari.savedState"
container_plist="$HOME/Library/Containers/com.apple.Safari/Data/Library/Preferences/com.apple.Safari.plist"
legacy_plist="$HOME/Library/Preferences/com.apple.Safari.plist"

backup_if_exists() {
  local f="$1"
  if [[ -f "$f" ]]; then
    cp -a "$f" "$backup_dir/"
  fi
}

soft_reposition_windows() {
  # Centers ALL Safari windows on the screen containing the mouse cursor
  # Requires: System Settings → Privacy & Security → Accessibility → enable for Terminal/iTerm
  osascript -l JavaScript <<'JXA'
ObjC.import('Cocoa');

function screenForPoint(pt) {
  const screens = $.NSScreen.screens;
  for (let i = 0; i < screens.count; i++) {
    const s = screens.objectAtIndex(i);
    const f = s.visibleFrame; // excludes Dock + menu bar
    const x0 = f.origin.x, y0 = f.origin.y, w = f.size.width, h = f.size.height;
    if (pt.x >= x0 && pt.x <= x0 + w && pt.y >= y0 && pt.y <= y0 + h) return f;
  }
  return $.NSScreen.mainScreen.visibleFrame;
}

const percent = 0.85;

const se = Application('System Events');
const proc = se.processes.byName('Safari');
if (!proc.exists()) throw new Error('Safari is not running. Run with --hard/--full to launch cleanly.');

proc.frontmost = true;

const mouse = $.NSEvent.mouseLocation;
const frame = screenForPoint(mouse);

const W = frame.size.width, H = frame.size.height;
const X0 = frame.origin.x, Y0 = frame.origin.y;

const w = Math.round(W * percent);
const h = Math.round(H * percent);
const x = Math.round(X0 + (W - w) / 2);
const y = Math.round(Y0 + (H - h) / 2);

const wins = proc.windows;
for (let i = 0; i < wins.length; i++) {
  wins[i].position = [x, y];
  wins[i].size = [w, h];
}
JXA
}

quit_safari() {
  osascript -e 'tell application "Safari" to quit' >/dev/null 2>&1 || true
  # give it a beat to die
  sleep 0.8
}

clear_saved_state() {
  if [[ -d "$saved_state" ]]; then
    rm -rf "$saved_state"
  fi
  if [[ "$NO_RESUME" == "true" ]]; then
    mkdir -p "$saved_state"
    chmod -R -w "$saved_state" || true
  fi
}

remove_window_frame_keys() {
  # Removes keys like "NSWindow Frame ..." from Safari prefs (window geometry memory)
  # Prefs live in Safari's container on modern macOS.
  local plist_path=""
  if [[ -f "$container_plist" ]]; then
    plist_path="$container_plist"
  elif [[ -f "$legacy_plist" ]]; then
    plist_path="$legacy_plist"
  else
    echo "No Safari plist found at expected locations."
    return 0
  fi

  backup_if_exists "$plist_path"

  /usr/bin/python3 - <<PY
import plistlib, re, pathlib, sys
p = pathlib.Path(r"""$plist_path""")
data = plistlib.loads(p.read_bytes())
keys = list(data.keys())
rx = re.compile(r"^NSWindow Frame", re.IGNORECASE)
removed = [k for k in keys if rx.search(k)]
for k in removed:
    data.pop(k, None)
p.write_bytes(plistlib.dumps(data))
print(f"Removed {len(removed)} window-frame keys from: {p}")
PY
}

launch_safari() {
  open -a Safari
}

case "$MODE" in
  soft)
    soft_reposition_windows
    ;;
  hard)
    backup_if_exists "$container_plist"
    backup_if_exists "$legacy_plist"
    quit_safari
    clear_saved_state
    launch_safari
    ;;
  full)
    backup_if_exists "$container_plist"
    backup_if_exists "$legacy_plist"
    quit_safari
    clear_saved_state
    remove_window_frame_keys
    launch_safari
    ;;
esac

echo "Done. Backup (if any) saved to: $backup_dir"
if [[ "$NO_RESUME" == "true" ]]; then
  echo "Note: Resume disabled by making savedState folder read-only. To undo:"
  echo "  chmod -R +w \"$HOME/Library/Saved Application State/com.apple.Safari.savedState\""
fi
