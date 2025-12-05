#!/usr/bin/env bash
set -e
DIR="$HOME/Noizy/LifeSaverTablet"
source "$DIR/.venv/bin/activate"
# Bind to all interfaces so LAN devices can access
python "$DIR/app.py" --host 0.0.0.0 --port 8080
