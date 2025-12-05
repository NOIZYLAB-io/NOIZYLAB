#!/bin/bash
set -euo pipefail

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  start ms-settings:signinoptions
elif [[ "$OSTYPE" == "darwin"* ]]; then
  open "x-apple.systempreferences:com.apple.TouchID-Settings.extension"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  sudo apt-get update
  sudo apt-get install fprintd libpam-fprintd -y
else
  echo "Unsupported OSTYPE: $OSTYPE" >&2
  exit 1
fi
