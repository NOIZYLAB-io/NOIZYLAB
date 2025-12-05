#!/usr/bin/env bash

set -euo pipefail

SRC="${2:-/Users/m2ultra}"
DEST_VOL="${3:-/Volumes/12TB}"
DEST_ROOT="${DEST_VOL}/MediaArchive"
LOG_DIR="${DEST_VOL}/MediaArchiveLogs"
TS="$(date +%Y%m%d-%H%M%S)"
LOG="${LOG_DIR}/offload-${TS}.log"
DRYRUN=0
AUDIT=0
MOVE=0

usage() {
  cat <<EOF
Usage:
  media_offload.sh --audit <SRC> <DEST_VOL>
  media_offload.sh --dry-run <SRC> <DEST_VOL>
  media_offload.sh --move <SRC> <DEST_VOL>

Examples:
  media_offload.sh --audit "/Users/m2ultra" "/Volumes/12TB"
  media_offload.sh --dry-run "/Users/m2ultra" "/Volumes/12TB"
  media_offload.sh --move "/Users/m2ultra" "/Volumes/12TB"
EOF
  exit 1
}

[ $# -lt 2 ] && usage

case "${1}" in
  --audit) AUDIT=1 ;;
  --dry-run) DRYRUN=1 ;;
  --move) MOVE=1 ;;
  *) usage ;;
esac

# Validate paths
if [ ! -d "$SRC" ]; then echo "Source not found: $SRC"; exit 1; fi
if [ ! -d "$DEST_VOL" ]; then echo "Destination volume not found: $DEST_VOL"; exit 1; fi

mkdir -p "$DEST_ROOT" "$LOG_DIR"

# Media extensions (case-insensitive)
IMG_EXT="jpg|jpeg|png|gif|tiff|tif|bmp|webp|heic|raw|cr2|nef|arw|dng|psd"
VID_EXT="mp4|mov|m4v|mkv|avi|wmv|flv|webm|mts|m2ts|3gp|mpeg|mpg|ogg"
AUD_EXT="wav|mp3|aac|m4a|aiff|flac|ogg|oga|alac|mid|midi"
PROJ_EXT="prproj|aep|aup|logicx|band|davinci|rpp" # project containers (optional)
ARCHIVE_EXT="zip|rar|7z|tar|gz|bz2|xz"

# Exclusions to avoid system/app caches and cloud placeholders
EXCLUDES=(
  "Library/Caches"
  "Library/CloudStorage"
  "Library/Application Support/Adobe"
  "Library/Mobile Documents"
  "Library/Containers"
  "Library/Group Containers"
  "node_modules"
  ".git"
  "VirtualBox VMs"
)

exclude_expr() {
  local expr=""
  for e in "${EXCLUDES[@]}"; do
    expr="$expr -not -path \"$SRC/$e/*\""
  done
  echo "$expr"
}

# Find media function
find_media() {
  # shellcheck disable=SC2046
  eval find "\"$SRC\"" -type f \
    $(exclude_expr) \
    \( -iregex ".*\\.\\(${IMG_EXT}\\)" -o -iregex ".*\\.\\(${VID_EXT}\\)" -o -iregex ".*\\.\\(${AUD_EXT}\\)" \) \
    -print
}

# Audit summary
audit() {
  echo "Auditing media in: $SRC"
  MEDIA_LIST=$(mktemp)
  find_media > "$MEDIA_LIST"

  TOTAL_FILES=$(wc -l < "$MEDIA_LIST" | tr -d ' ')
  TOTAL_SIZE=$(awk 'BEGIN{sum=0} { cmd="stat -f%z \""$0"\""; cmd|getline s; sum+=s } END{ print sum }' "$MEDIA_LIST")
  # Human-readable size
  HR_SIZE=$(echo "$TOTAL_SIZE" | awk '{
    split("B KB MB GB TB",u);
    size=$1; i=1;
    while (size>=1024 && i<5) { size/=1024; i++ }
    printf("%.2f %s\n", size, u[i])
  }')

  echo "Files: $TOTAL_FILES"
  echo "Size: $HR_SIZE"
  echo "Saving detailed list to: $LOG"
  {
    echo "Audit ${TS}"
    echo "Source: $SRC"
    echo "Destination: $DEST_ROOT"
    echo "Files: $TOTAL_FILES"
    echo "Size: $HR_SIZE"
    echo
    echo "---- FILES ----"
    cat "$MEDIA_LIST"
  } > "$LOG"
  rm -f "$MEDIA_LIST"
  echo "Audit complete."
}

# Move with verification: rsync copy, verify, then delete originals
offload() {
  echo "Preparing offload of media from $SRC to $DEST_ROOT"
  echo "Log: $LOG"

  RSYNC_FLAGS="-a --xattrs --protect-args --human-readable --info=progress2 --exclude '.DS_Store'"
  for e in "${EXCLUDES[@]}"; do RSYNC_FLAGS="$RSYNC_FLAGS --exclude \"$e\""; done

  # Build include patterns for media
  INCLUDE_PATTERNS=(
    "--include=*/"
    "--include=*.{${IMG_EXT}}"
    "--include=*.{${VID_EXT}}"
    "--include=*.{${AUD_EXT}}"
    "--exclude=*"
  )

  echo "Copying media (rsync)..."
  if [ "$DRYRUN" -eq 1 ]; then
    # shellcheck disable=SC2086
    eval rsync -n $RSYNC_FLAGS "${INCLUDE_PATTERNS[@]}" "\"$SRC/\"" "\"$DEST_ROOT/\"" | tee -a "$LOG"
    echo "Dry-run complete. No changes made."
    exit 0
  fi

  # shellcheck disable=SC2086
  eval rsync $RSYNC_FLAGS "${INCLUDE_PATTERNS[@]}" "\"$SRC/\"" "\"$DEST_ROOT/\"" | tee -a "$LOG"

  echo "Verifying copy (size+count)..."
  SRC_COUNT=$(eval find "\"$SRC\"" -type f $(exclude_expr) \( -iregex ".*\\.\\(${IMG_EXT}\\)" -o -iregex ".*\\.\\(${VID_EXT}\\)" -o -iregex ".*\\.\\(${AUD_EXT}\\)" \) | wc -l | tr -d ' ')
  DEST_COUNT=$(find "$DEST_ROOT" -type f \( -iregex ".*\\.\\(${IMG_EXT}\\)" -o -iregex ".*\\.\\(${VID_EXT}\\)" -o -iregex ".*\\.\\(${AUD_EXT}\\)" \) | wc -l | tr -d ' ')

  SRC_SIZE=$(eval find "\"$SRC\"" -type f $(exclude_expr) \( -iregex ".*\\.\\(${IMG_EXT}\\)" -o -iregex ".*\\.\\(${VID_EXT}\\)" -o -iregex ".*\\.\\(${AUD_EXT}\\)" \) -exec stat -f%z {} \; | awk '{s+=$1} END{print s}')
  DEST_SIZE=$(find "$DEST_ROOT" -type f \( -iregex ".*\\.\\(${IMG_EXT}\\)" -o -iregex ".*\\.\\(${VID_EXT}\\)" -o -iregex ".*\\.\\(${AUD_EXT}\\)" \) -exec stat -f%z {} \; | awk '{s+=$1} END{print s}')

  echo "Source files: $SRC_COUNT | Destination files: $DEST_COUNT" | tee -a "$LOG"
  echo "Source size:  $SRC_SIZE | Destination size:  $DEST_SIZE" | tee -a "$LOG"

  if [ "$SRC_COUNT" -eq "$DEST_COUNT" ] && [ "$SRC_SIZE" -eq "$DEST_SIZE" ]; then
    echo "Verification OK."
  else
    echo "Verification mismatch. Aborting deletion." | tee -a "$LOG"
    echo "Review $LOG and rerun."
    exit 1
  fi

  read -r -p "Delete originals from $SRC now? Type YES to proceed: " CONFIRM
  if [ "$CONFIRM" != "YES" ]; then
    echo "Deletion skipped."
    exit 0
  fi

  echo "Deleting originals..."
  eval find "\"$SRC\"" -type f $(exclude_expr) \( -iregex ".*\\.\\(${IMG_EXT}\\)" -o -iregex ".*\\.\\(${VID_EXT}\\)" -o -iregex ".*\\.\\(${AUD_EXT}\\)" \) -print0 | xargs -0 rm -f
  echo "Offload complete."
}

# Main
if [ "$AUDIT" -eq 1 ]; then
  audit
elif [ "$DRYRUN" -eq 1 ]; then
  offload
elif [ "$MOVE" -eq 1 ] ; then
  offload
else
  usage
fi

