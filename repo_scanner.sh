#!/bin/bash
# Repository Scanner & Analyzer
# Scans all repos and generates detailed analysis

OUTPUT="repo_analysis.json"
echo "[" > "$OUTPUT"
first=true

while IFS= read -r git_dir; do
    if [ -z "$git_dir" ]; then continue; fi
    
    repo_dir=$(dirname "$git_dir")
    
    # Skip if directory doesn't exist
    if [ ! -d "$repo_dir" ]; then continue; fi
    
    cd "$repo_dir" || continue
    
    # Add comma for JSON array
    if [ "$first" = false ]; then
        echo "," >> "$OUTPUT"
    fi
    first=false
    
    # Gather repo info
    repo_name=$(basename "$repo_dir")
    size=$(du -sh . 2>/dev/null | awk '{print $1}')
    branch=$(git branch --show-current 2>/dev/null || echo "unknown")
    remote=$(git remote get-url origin 2>/dev/null || echo "none")
    last_commit=$(git log -1 --format="%ai" 2>/dev/null || echo "unknown")
    status=$(git status --porcelain 2>/dev/null | wc -l | xargs)
    branches=$(git branch -a 2>/dev/null | wc -l | xargs)
    
    # Write JSON object
    cat >> "$OUTPUT" << EOF
  {
    "path": "$repo_dir",
    "name": "$repo_name",
    "size": "$size",
    "branch": "$branch",
    "remote": "$remote",
    "last_commit": "$last_commit",
    "dirty_files": $status,
    "branch_count": $branches
  }
EOF
done < repos.txt

echo "" >> "$OUTPUT"
echo "]" >> "$OUTPUT"

echo "Analysis complete! Results in $OUTPUT"
