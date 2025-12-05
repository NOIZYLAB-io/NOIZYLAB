#!/bin/bash
# Ultra-fast duplicate and mislabeled file scanner using native shell tools

ROOT="/Volumes/MAG 4TB"
OUTPUT="/Volumes/MAG 4TB/NoizyWorkspace/scan_results.txt"

echo "ULTRA-FAST SCAN FOR DUPLICATES & MISLABELED FILES" > "$OUTPUT"
echo "Root: $ROOT" >> "$OUTPUT"
echo "Started: $(date)" >> "$OUTPUT"
echo "========================================" >> "$OUTPUT"

echo "Scanning files..."

# Find all files (excluding certain directories)
echo -e "\n### Finding all files..." >> "$OUTPUT"
FILES=$(find "$ROOT" -type f \
    -not -path "*/.*" \
    -not -path "*/.git/*" \
    -not -path "*/__pycache__/*" \
    -not -path "*/node_modules/*" \
    2>/dev/null)

TOTAL=$(echo "$FILES" | wc -l | tr -d ' ')
echo "Total files found: $TOTAL" >> "$OUTPUT"

# Find duplicate filenames
echo -e "\n### DUPLICATE FILENAMES ###" >> "$OUTPUT"
echo "$FILES" | xargs -n1 basename 2>/dev/null | sort | uniq -d > /tmp/dupe_names.txt

if [ -s /tmp/dupe_names.txt ]; then
    echo "Found $(wc -l < /tmp/dupe_names.txt | tr -d ' ') duplicate filenames" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    
    head -50 /tmp/dupe_names.txt | while read name; do
        echo "--- '$name' ---" >> "$OUTPUT"
        echo "$FILES" | grep -F "/$name$" | while read filepath; do
            size=$(stat -f%z "$filepath" 2>/dev/null || echo "0")
            size_mb=$(echo "scale=2; $size / 1048576" | bc)
            echo "  $size_mb MB - $filepath" >> "$OUTPUT"
        done
        echo "" >> "$OUTPUT"
    done
else
    echo "No duplicate filenames found" >> "$OUTPUT"
fi

# Find files with quality indicators
echo -e "\n### SUSPICIOUS FILES (Quality Indicators) ###" >> "$OUTPUT"
echo "$FILES" | grep -iE "(low|lq|draft|temp|test|_old|copy|backup|duplicate|dupe)" | head -100 >> "$OUTPUT"

# Find files without extensions
echo -e "\n### FILES WITHOUT EXTENSIONS ###" >> "$OUTPUT"
echo "$FILES" | grep -v '\.' | head -50 >> "$OUTPUT"

# Find potential size duplicates (same size files)
echo -e "\n### ANALYZING SIZE DUPLICATES..." >> "$OUTPUT"
echo "$FILES" | while read f; do
    if [ -f "$f" ]; then
        size=$(stat -f%z "$f" 2>/dev/null || echo "0")
        if [ "$size" -gt 10240 ]; then  # > 10KB
            echo "$size|$f"
        fi
    fi
done | sort -t'|' -k1 -n > /tmp/files_by_size.txt

# Find size duplicates
awk -F'|' '{sizes[$1]=sizes[$1]" "$2; count[$1]++} END {for (s in sizes) if (count[s] > 1) print s"|"count[s]"|"sizes[s]}' /tmp/files_by_size.txt | sort -t'|' -k2 -rn | head -20 > /tmp/size_dupes.txt

if [ -s /tmp/size_dupes.txt ]; then
    echo "Found potential exact duplicates:" >> "$OUTPUT"
    while IFS='|' read size count files; do
        size_mb=$(echo "scale=2; $size / 1048576" | bc)
        echo -e "\nSize: $size_mb MB - $count files:" >> "$OUTPUT"
        echo "$files" | tr ' ' '\n' | head -5 >> "$OUTPUT"
    done < /tmp/size_dupes.txt
else
    echo "No size duplicates found" >> "$OUTPUT"
fi

# Summary
echo -e "\n========================================" >> "$OUTPUT"
echo "SCAN COMPLETE" >> "$OUTPUT"
echo "Finished: $(date)" >> "$OUTPUT"
echo "Results saved to: $OUTPUT" >> "$OUTPUT"

echo "Scan complete! Results in $OUTPUT"
cat "$OUTPUT"

