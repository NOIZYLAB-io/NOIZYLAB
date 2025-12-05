#!/bin/zsh
# Clean Python project: remove caches and temp files
set -e

# Remove __pycache__ folders
find . -name "__pycache__" -type d -exec rm -r {} +
# Remove .pyc files
find . -name "*.pyc" -delete
# Optionally remove Backups and temp files
rm -rf ./Backups/* /tmp/* 2>/dev/null || true

echo "✅ Project cleaned."
