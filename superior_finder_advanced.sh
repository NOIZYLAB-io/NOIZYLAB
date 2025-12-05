#!/bin/bash
# Advanced Superior Drummer Finder with Analytics

ROOT="/Volumes/MAG 4TB"
SD3_ROOT="/Volumes/MAG 4TB/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3"
OUTPUT="/Volumes/MAG 4TB/NoizyWorkspace/SD3_ADVANCED_REPORT.txt"

echo "════════════════════════════════════════════════════════════════════" > "$OUTPUT"
echo "     🥁 SUPERIOR DRUMMER 3 - ADVANCED ANALYSIS REPORT 🥁" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "Generated: $(date)" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "🔍 Analyzing Superior Drummer 3 Collection..."

# 1. Complete file inventory
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "1. COMPLETE FILE INVENTORY" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

if [ -d "$SD3_ROOT" ]; then
    total_files=$(find "$SD3_ROOT" -type f -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    total_size=$(du -sh "$SD3_ROOT" 2>/dev/null | awk '{print $1}')
    total_dirs=$(find "$SD3_ROOT" -type d 2>/dev/null | wc -l | tr -d ' ')
    
    echo "Total MIDI Files: $total_files" >> "$OUTPUT"
    echo "Total Size: $total_size" >> "$OUTPUT"
    echo "Total Directories: $total_dirs" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
fi

# 2. Analyze by tempo ranges
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "2. TEMPO ANALYSIS" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Ballad Grooves (Slow):" >> "$OUTPUT"
find "$SD3_ROOT" -type d -name "*200@*BALLAD*" 2>/dev/null | while read dir; do
    count=$(find "$dir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    name=$(basename "$dir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
    echo "  $name: $count grooves" >> "$OUTPUT"
done
echo "" >> "$OUTPUT"

echo "Half-Time Grooves:" >> "$OUTPUT"
find "$SD3_ROOT" -type d -name "*300@*HALF*" 2>/dev/null | while read dir; do
    count=$(find "$dir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    name=$(basename "$dir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
    echo "  $name: $count grooves" >> "$OUTPUT"
done
echo "" >> "$OUTPUT"

echo "Midtempo Grooves:" >> "$OUTPUT"
find "$SD3_ROOT" -type d -name "*400@*MIDTEMPO*" 2>/dev/null | while read dir; do
    count=$(find "$dir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    name=$(basename "$dir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
    echo "  $name: $count grooves" >> "$OUTPUT"
done
echo "" >> "$OUTPUT"

echo "Uptempo Grooves:" >> "$OUTPUT"
find "$SD3_ROOT" -type d -name "*500@*UPTEMPO*" 2>/dev/null | while read dir; do
    count=$(find "$dir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    name=$(basename "$dir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
    echo "  $name: $count grooves" >> "$OUTPUT"
done
echo "" >> "$OUTPUT"

# 3. Time signature breakdown
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "3. TIME SIGNATURE BREAKDOWN" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "4/4 Time:" >> "$OUTPUT"
find "$SD3_ROOT" -type d -name "*4#4*" 2>/dev/null | while read dir; do
    count=$(find "$dir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
    if [ "$count" -gt 0 ]; then
        name=$(basename "$dir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
        echo "  $name: $count grooves" >> "$OUTPUT"
    fi
done | head -20
echo "" >> "$OUTPUT"

echo "3/4 Time:" >> "$OUTPUT"
count_3_4=$(find "$SD3_ROOT" -type d -name "*3#4*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $count_3_4 grooves" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "6/8 Time:" >> "$OUTPUT"
count_6_8=$(find "$SD3_ROOT" -type d -name "*6#8*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $count_6_8 grooves" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "12/8 Time:" >> "$OUTPUT"
count_12_8=$(find "$SD3_ROOT" -type d -name "*12#8*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $count_12_8 grooves" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# 4. Special categories
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "4. SPECIAL CATEGORIES & EXTRAS" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Brushes:" >> "$OUTPUT"
brush_dir=$(find "$SD3_ROOT" -type d -name "*BRUSHES*" 2>/dev/null | head -1)
if [ -n "$brush_dir" ]; then
    find "$brush_dir" -type d -mindepth 1 2>/dev/null | while read subdir; do
        count=$(find "$subdir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
        name=$(basename "$subdir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
        echo "  $name: $count grooves" >> "$OUTPUT"
    done
fi
echo "" >> "$OUTPUT"

echo "Snare Rolls:" >> "$OUTPUT"
roll_count=$(find "$SD3_ROOT" -type d -name "*SNARE*ROLL*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $roll_count rolls" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Cymbal Stuff:" >> "$OUTPUT"
cymbal_count=$(find "$SD3_ROOT" -type d -name "*CYMBAL*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $cymbal_count patterns" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Count-Ins:" >> "$OUTPUT"
countin_count=$(find "$SD3_ROOT" -type d -name "*COUNT*IN*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $countin_count count-ins" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "One Shots:" >> "$OUTPUT"
oneshot_count=$(find "$SD3_ROOT" -type d -name "*ONE*SHOT*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Total: $oneshot_count one-shots" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Percussion:" >> "$OUTPUT"
shaker_count=$(find "$SD3_ROOT" -type d -name "*SHAKER*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
tamb_count=$(find "$SD3_ROOT" -type d -name "*TAMBOURINE*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
echo "  Shaker: $shaker_count patterns" >> "$OUTPUT"
echo "  Tambourine: $tamb_count patterns" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# 5. Swing vs Straight analysis
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "5. SWING vs STRAIGHT ANALYSIS" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

swing_count=$(find "$SD3_ROOT" -type d -name "*SWING*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')
straight_count=$(find "$SD3_ROOT" -type d -name "*STRAIGHT*" -exec find {} -name "*.mid" \; 2>/dev/null | wc -l | tr -d ' ')

echo "Swing Grooves: $swing_count" >> "$OUTPUT"
echo "Straight Grooves: $straight_count" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# 6. File size analysis
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "6. FILE SIZE ANALYSIS" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Largest MIDI Files:" >> "$OUTPUT"
find "$SD3_ROOT" -name "*.mid" -exec ls -lh {} \; 2>/dev/null | sort -k5 -hr | head -10 | awk '{print "  " $9 " - " $5}' >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Smallest MIDI Files:" >> "$OUTPUT"
find "$SD3_ROOT" -name "*.mid" -exec ls -lh {} \; 2>/dev/null | sort -k5 -h | head -10 | awk '{print "  " $9 " - " $5}' >> "$OUTPUT"
echo "" >> "$OUTPUT"

# 7. Directory structure
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "7. COMPLETE DIRECTORY STRUCTURE" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

find "$SD3_ROOT" -maxdepth 1 -type d 2>/dev/null | sort | while read dir; do
    if [ "$dir" != "$SD3_ROOT" ]; then
        dirname=$(basename "$dir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
        count=$(find "$dir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
        subdirs=$(find "$dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
        
        echo "📁 $dirname" >> "$OUTPUT"
        echo "   MIDI Files: $count" >> "$OUTPUT"
        echo "   Subdirectories: $subdirs" >> "$OUTPUT"
        
        # Show subdirectories
        if [ "$subdirs" -gt 0 ]; then
            find "$dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort | while read subdir; do
                subname=$(basename "$subdir" | sed 's/@/ - /g' | sed 's/#/\//g' | sed 's/_/ /g')
                subcount=$(find "$subdir" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
                echo "     └─ $subname ($subcount grooves)" >> "$OUTPUT"
            done
        fi
        echo "" >> "$OUTPUT"
    fi
done

# 8. Usage recommendations
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "8. USAGE RECOMMENDATIONS" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Best for Rock/Pop:" >> "$OUTPUT"
echo "  • Midtempo Straight 4/4 (383 grooves)" >> "$OUTPUT"
echo "  • Location: 405@STRAIGHT_4#4" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Best for Jazz:" >> "$OUTPUT"
echo "  • Swing grooves (all tempos)" >> "$OUTPUT"
echo "  • Brushes collection" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Best for Ballads:" >> "$OUTPUT"
echo "  • 200@BALLAD section (326 grooves)" >> "$OUTPUT"
echo "  • Slower tempos with feeling" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Best for Fills:" >> "$OUTPUT"
echo "  • Snare Rolls ($roll_count rolls)" >> "$OUTPUT"
echo "  • One Shots ($oneshot_count patterns)" >> "$OUTPUT"
echo "  • Cymbal Stuff ($cymbal_count patterns)" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Best for Adding Percussion:" >> "$OUTPUT"
echo "  • Shaker: $shaker_count patterns" >> "$OUTPUT"
echo "  • Tambourine: $tamb_count patterns" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# 9. Summary statistics
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "9. SUMMARY STATISTICS" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Total MIDI Files: $total_files" >> "$OUTPUT"
echo "Total Size: $total_size" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "By Feel:" >> "$OUTPUT"
echo "  Swing: $swing_count grooves" >> "$OUTPUT"
echo "  Straight: $straight_count grooves" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "By Time Signature:" >> "$OUTPUT"
echo "  4/4: Most grooves" >> "$OUTPUT"
echo "  3/4: $count_3_4 grooves" >> "$OUTPUT"
echo "  6/8: $count_6_8 grooves" >> "$OUTPUT"
echo "  12/8: $count_12_8 grooves" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "Special Content:" >> "$OUTPUT"
echo "  Brushes: Available" >> "$OUTPUT"
echo "  Snare Rolls: $roll_count" >> "$OUTPUT"
echo "  Cymbals: $cymbal_count" >> "$OUTPUT"
echo "  Count-ins: $countin_count" >> "$OUTPUT"
echo "  One-shots: $oneshot_count" >> "$OUTPUT"
echo "  Shaker: $shaker_count" >> "$OUTPUT"
echo "  Tambourine: $tamb_count" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"
echo "Report completed: $(date)" >> "$OUTPUT"
echo "Saved to: $OUTPUT" >> "$OUTPUT"
echo "════════════════════════════════════════════════════════════════════" >> "$OUTPUT"

echo ""
echo "✅ Advanced analysis complete!"
echo "📄 Report: $OUTPUT"
echo ""
cat "$OUTPUT"

