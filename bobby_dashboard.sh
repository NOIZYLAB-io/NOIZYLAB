#!/bin/zsh
set -euo pipefail

LOGFILE=~/Desktop/bobby_dashboard.log
AQUARIUM=~/Documents/_The_Aquarium

# Ensure Aquarium exists
mkdir -p "$AQUARIUM"

# Helper to log + speak
log_and_say() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOGFILE"
  say "$1"
}

while true; do
  clear
  log_and_say "Bobby Dashboard is online. What do you want me to do, Rob?"
  echo "🐟 Bobby Dashboard"
  echo "1) Run Aquarium Cleanup"
  echo "2) Generate Folder Report"
  echo "3) Quarantine Empty Folders"
  echo "4) View Last 20 Log Lines"
  echo "5) Exit"
  echo "6) Clean Desktop (move files into Aquarium)"
  echo -n "Select an option: "
  read choice

  case $choice in
    1)
      if [[ -x ~/Desktop/aquarium_cleanup.sh ]]; then
        log_and_say "Running Aquarium cleanup now."
        ~/Desktop/aquarium_cleanup.sh | tee -a "$LOGFILE"
        log_and_say "Cleanup complete."
      else
        log_and_say "Cleanup script not found on Desktop."
      fi
      ;;
    2)
      REPORT=~/Desktop/aquarium_report.txt
      log_and_say "Generating folder report."
      if command -v tree >/dev/null 2>&1; then
        tree "$AQUARIUM" > "$REPORT"
      else
        ls -R "$AQUARIUM" > "$REPORT"
      fi
      log_and_say "Report saved to your Desktop."
      ;;
    3)
      mkdir -p "$AQUARIUM/_empty"
      log_and_say "Moving empty folders into quarantine."
      find "$AQUARIUM" -type d -empty -not -path "*/_empty/*" -exec mv {} "$AQUARIUM/_empty/" \; || true
      log_and_say "Empty folders quarantined."
      ;;
    4)
      log_and_say "Showing the last 20 lines of the log."
      tail -n 20 "$LOGFILE" || log_and_say "No log entries yet."
      read -k1 -s -r -p "Press any key to return to the menu..."
      ;;
    5)
      log_and_say "Goodbye for now."
      exit 0
      ;;
    6)
      log_and_say "Cleaning the Desktop now."
      mkdir -p "$AQUARIUM/_projects/DesktopImports"
      mkdir -p "$AQUARIUM/_assets/DesktopImports"

      # Project/code files
      find ~/Desktop -maxdepth 1 -type f \( -iname "*.py" -o -iname "*.js" -o -iname "*.c" -o -iname "*.cpp" -o -iname "*.swift" -o -iname "*.sh" \) | while read file; do
        mv -n "$file" "$AQUARIUM/_projects/DesktopImports/"
        echo "Moved project file: $file" >> "$LOGFILE"
      done

      # Asset/media/docs files
      find ~/Desktop -maxdepth 1 -type f \( -iname "*.wav" -o -iname "*.aiff" -o -iname "*.mp3" -o -iname "*.png" -o -iname "*.jpg" -o -iname "*.pdf" -o -iname "*.docx" \) | while read file; do
        mv -n "$file" "$AQUARIUM/_assets/DesktopImports/"
        echo "Moved asset file: $file" >> "$LOGFILE"
      done

      log_and_say "Desktop files have been sorted into Aquarium folders."
      ;;
    *)
      log_and_say "Invalid choice. Please try again."
      ;;
  esac
done
