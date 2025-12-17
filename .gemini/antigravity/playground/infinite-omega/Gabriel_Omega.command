#!/bin/bash
# GABRIEL OMEGA ONE-CLICK LAUNCHER
# double-click this file to start the system.

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Set Executable Permissions just in case
chmod +x start_gabriel.sh

# Launch the Main Ignition Script
echo "💎 GABRIEL OMEGA LAUNCH SEQUENCING..."
./start_gabriel.sh
