#!/bin/bash
# Rename any dragged-in files from *_rmx or __rmx to .rmx

for f in "$@"; do
  if [[ -f "$f" ]]; then
    newname="$(echo "$f" | sed -E 's/[_]+rmx$/.rmx/i')"
    if [[ "$f" != "$newname" ]]; then
      mv "$f" "$newname"
      echo "Renamed: $f → $newname"
    fi
  fi
done
