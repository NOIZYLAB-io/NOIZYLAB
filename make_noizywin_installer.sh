#!/bin/bash
# Build NoizyWin installer USB
set -e
ISO_PATH="$1"
USB_DEV="$2"
RES_DIR="$(dirname "$0")/../resources"

if [[ -z "$ISO_PATH" || -z "$USB_DEV" ]]; then
  echo "Usage: $0 <Windows ISO path> <USB device>"
  exit 1
fi

echo "Erasing USB..."
diskutil eraseDisk ExFAT NoizyWin "$USB_DEV"
echo "Mounting ISO..."
hdiutil attach "$ISO_PATH" -mountpoint /Volumes/WinISO

echo "Copying Windows files..."
cp -R /Volumes/WinISO/* /Volumes/NoizyWin/

echo "Copying resources..."
cp "$RES_DIR/autounattend.xml" /Volumes/NoizyWin/
cp "$RES_DIR/post_install.ps1" /Volumes/NoizyWin/

echo "Ejecting ISO and USB..."
hdiutil detach /Volumes/WinISO
diskutil eject "$USB_DEV"
echo "✅ NoizyWin installer USB is ready."
