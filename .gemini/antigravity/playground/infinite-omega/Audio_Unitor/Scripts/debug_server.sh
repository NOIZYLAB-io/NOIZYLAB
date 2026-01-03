#!/bin/bash
echo "Starting Debug Server..."
if [ -f "turbo_server.py" ]; then
    python3 turbo_server.py > debug_server.log 2>&1
    echo "Exit Code: $?" >> debug_server.log
else
    echo "Error: turbo_server.py not found in $(pwd)" | tee -a debug_server.log >&2
    exit 1
fi
