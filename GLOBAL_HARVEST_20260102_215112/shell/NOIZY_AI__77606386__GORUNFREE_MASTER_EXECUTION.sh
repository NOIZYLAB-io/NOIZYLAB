#!/usr/bin/env bash

# ==========================
#  MC96 GORUNFREE MASTER
#  v0.1 – Starter Edition
# ==========================

set -e

ROOT_DRIVE="/Volumes/GABRIEL"
NOEXT_REPORT="$HOME/Desktop/no_extension_files.txt"

menu() {
  clear
  echo "============================"
  echo "   MC96 GORUNFREE MASTER"
  echo "============================"
  echo
  echo "1) Open GoDaddy DNS page for noizylab.ca"
  echo "2) Scan $ROOT_DRIVE for files with NO extension"
  echo "3) Show where the last report was saved"
  echo "4) Quit"
  echo
  read -p "Choose [1-4] (Enter = 1): " choice
  choice=${choice:-1}
}

open_dns() {
  echo "Opening GoDaddy DNS in your browser..."
  # macOS 'open' command – adjust URL if needed
  open "https://dcc.godaddy.com/domains"
}

scan_noext() {
  echo "Scanning $ROOT_DRIVE for files with NO extension..."
  echo "This may take a while on large drives."
  echo
  find "$ROOT_DRIVE" -type f ! -name "*.*" > "$NOEXT_REPORT"
  echo "Done. Report saved to:"
  echo "  $NOEXT_REPORT"
}

show_report() {
  echo "Last no-extension report (if it exists):"
  echo "  $NOEXT_REPORT"
  [ -f "$NOEXT_REPORT" ] || echo "(File not created yet.)"
}

while true; do
  menu
  case "$choice" in
    1) open_dns; read -p "Press Enter to return to menu..." ;;
    2) scan_noext; read -p "Press Enter to return to menu..." ;;
    3) show_report; read -p "Press Enter to return to menu..." ;;
    4) echo "Goodbye."; exit 0 ;;
    *) echo "Invalid choice."; sleep 1 ;;
  esac
done

