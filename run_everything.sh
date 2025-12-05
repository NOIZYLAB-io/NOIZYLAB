#!/usr/bin/env bash
set -e

# --- NoizyCore Full Automation Script ---
ROOT="$HOME/noizy_core"
PY_SCRIPT="$HOME/scripts/add_noizy_ai_bookmark.py"
PORTAL_URL="https://noizy.ai/portal"

# 1. Ensure Firefox is closed for bookmark automation
if pgrep Firefox >/dev/null; then
  echo "🦊 Closing Firefox to update bookmarks..."
  pkill Firefox
  # Wait until Firefox is fully closed
  for i in {1..10}; do
    if ! pgrep Firefox >/dev/null; then break; fi
    sleep 1
  done
fi

# 2. Add Noizy.ai Demo Portal bookmark to Firefox
if [ -f "$PY_SCRIPT" ]; then
  python3 "$PY_SCRIPT"
else
  echo "⚠️ Bookmark script not found: $PY_SCRIPT"
fi

# 3. Open the Noizy.ai Demo Portal in Firefox
open -a Firefox "$PORTAL_URL"

# 4. Start NoizyCore services (launch_all.py)
if [ -f "$ROOT/launch_all.py" ]; then
  cd "$ROOT"
  if [ ! -d ".venv" ]; then
    echo "🧩 Creating Python virtual environment..."
    python3 -m venv .venv
  fi
  source .venv/bin/activate
  python launch_all.py &
else
  echo "⚠️ NoizyCore launch_all.py not found in $ROOT"
fi

# 5. Start autosync (background)
if [ -f "$ROOT/tools/autosync.sh" ]; then
  bash "$ROOT/tools/autosync.sh" &
else
  echo "⚠️ Autosync script not found in $ROOT/tools/autosync.sh"
fi

# 6. All done!
echo "🚀 NoizyCore automation complete."
