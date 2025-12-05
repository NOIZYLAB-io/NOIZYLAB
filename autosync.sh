#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.." || exit 1
. .venv/bin/activate 2>/dev/null || true

# read-only pull for workers; control can push
ROLE=$(grep '^ROLE=' .env 2>/dev/null | cut -d= -f2)
if [ -z "$ROLE" ]; then ROLE="worker"; fi

git fetch --all -q || true
git reset --hard origin/main 2>/dev/null || git pull -q || true

# Relaunch core if changed (simple: always ensure running)
pgrep -f "services/heartbeat.py" >/dev/null || python services/heartbeat.py &
if [ "$ROLE" = "control" ]; then
  pgrep -f "services/core.py" >/dev/null || python services/core.py &
fi
