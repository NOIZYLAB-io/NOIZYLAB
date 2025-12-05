#!/bin/bash
# Superior Drummer Location Finder

ROOT="/Volumes/MAG 4TB"
OUTPUT="/Volumes/MAG 4TB/NoizyWorkspace/SUPERIOR_DRUMMER_LOCATIONS.txt"

echo "════════════════════════════════════════════════════════════════" > "$OUTPUT"
echo "     SUPERIOR DRUMMER - ALL LOCATIONS FOUND" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "Scan Date: $(date)" >> "$OUTPUT"
echo "Root: $ROOT" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Scanning for Superior Drummer files and directories..."

# Find all directories with "superior" in name
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "1. DIRECTORIES WITH 'SUPERIOR' IN NAME" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

find "$ROOT" -type d -iname "*superior*" 2>/dev/null | while read dir; do
    size=$(du -sh "$dir" 2>/dev/null | awk '{print $1}')
    count=$(find "$dir" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "📁 $dir" >> "$OUTPUT"
    echo "   Size: $size | Files: $count" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

# Find all files with "superior" in name
echo "" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "2. FILES WITH 'SUPERIOR' IN NAME" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

find "$ROOT" -type f -iname "*superior*" 2>/dev/null | while read file; do
    size=$(ls -lh "$file" 2>/dev/null | awk '{print $5}')
    echo "📄 $(basename "$file")" >> "$OUTPUT"
    echo "   $file" >> "$OUTPUT"
    echo "   Size: $size" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

# Search for Superior Drummer related content in EZ Drummer Database
echo "" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "3. SUPERIOR DRUMMER IN EZ DRUMMER DATABASE" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

if [ -d "$ROOT/_EZ Drummer/Database" ]; then
    find "$ROOT/_EZ Drummer/Database" -name "midiDB" 2>/dev/null | while read db; do
        if strings "$db" 2>/dev/null | grep -qi "SUPERIOR"; then
            dbdir=$(dirname "$db")
            dbname=$(basename "$dbdir")
            echo "📀 $dbname" >> "$OUTPUT"
            echo "   Location: $dbdir" >> "$OUTPUT"
            echo "   Database: $db" >> "$OUTPUT"
            echo "" >> "$OUTPUT"
        fi
    done
fi

# Look for Superior Drummer MIDI content
echo "" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "4. SUPERIOR DRUMMER MIDI LIBRARIES" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

if [ -d "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" ]; then
    echo "📁 SUPERIOR DRUMMER 3 - MIDI Library" >> "$OUTPUT"
    echo "   Location: $ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" >> "$OUTPUT"
    
    size=$(du -sh "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" 2>/dev/null | awk '{print $1}')
    echo "   Size: $size" >> "$OUTPUT"
    
    # Count subdirectories
    subdirs=$(find "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
    echo "   Subdirectories: $((subdirs - 1))" >> "$OUTPUT"
    
    # Count MIDI files
    midis=$(find "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    echo "   MIDI Files: $midis" >> "$OUTPUT"
    
    echo "" >> "$OUTPUT"
    echo "   Grooves by Category:" >> "$OUTPUT"
    ls -1 "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" 2>/dev/null | grep "@" | while read cat; do
        catname=$(echo "$cat" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
        count=$(find "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3/$cat" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
        echo "     • $catname ($count grooves)" >> "$OUTPUT"
    done
    echo "" >> "$OUTPUT"
fi

# Check for other Superior libraries
if [ -d "$ROOT/_EZ Drummer/Midi/00000@_SUPERIOR LIBRARIES" ]; then
    echo "📁 SUPERIOR LIBRARIES - General" >> "$OUTPUT"
    echo "   Location: $ROOT/_EZ Drummer/Midi/00000@_SUPERIOR LIBRARIES" >> "$OUTPUT"
    size=$(du -sh "$ROOT/_EZ Drummer/Midi/00000@_SUPERIOR LIBRARIES" 2>/dev/null | awk '{print $1}')
    echo "   Size: $size" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
fi

# Search for Superior Drummer in BFD/FXpansion
echo "" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "5. SUPERIOR DRUMMER IN OTHER SOFTWARE" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

if [ -d "$ROOT/FXpansion" ]; then
    find "$ROOT/FXpansion" -iname "*superior*" 2>/dev/null | while read item; do
        if [ -f "$item" ]; then
            echo "📄 $(basename "$item")" >> "$OUTPUT"
        else
            echo "📁 $(basename "$item")" >> "$OUTPUT"
        fi
        echo "   $item" >> "$OUTPUT"
        echo "" >> "$OUTPUT"
    done
fi

# Summary
echo "" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "SUMMARY" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# Count totals
total_dirs=$(find "$ROOT" -type d -iname "*superior*" 2>/dev/null | wc -l | tr -d ' ')
total_files=$(find "$ROOT" -type f -iname "*superior*" 2>/dev/null | wc -l | tr -d ' ')

echo "Total Directories Found: $total_dirs" >> "$OUTPUT"
echo "Total Files Found: $total_files" >> "$OUTPUT"

if [ -d "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" ]; then
    sd3_size=$(du -sh "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" 2>/dev/null | awk '{print $1}')
    sd3_midis=$(find "$ROOT/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    echo "" >> "$OUTPUT"
    echo "Superior Drummer 3 MIDI Library:" >> "$OUTPUT"
    echo "  - Total Size: $sd3_size" >> "$OUTPUT"
    echo "  - MIDI Grooves: $sd3_midis" >> "$OUTPUT"
fi

echo "" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "Scan completed: $(date)" >> "$OUTPUT"
echo "Report saved to: $OUTPUT" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════" >> "$OUTPUT"

echo ""
echo "✅ Scan complete! Opening report..."
cat "$OUTPUT"

