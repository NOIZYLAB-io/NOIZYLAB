#!/usr/bin/env bash
set -e
ROOT="$HOME/noizy_core"
mkdir -p "$ROOT/logs"
python3 -m venv "$ROOT/.venv"
source "$ROOT/.venv/bin/activate"
pip install -U pip
pip install -r "$ROOT/requirements.txt"
python "$ROOT/launch_all.py"
