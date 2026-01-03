#!/bin/bash
#═══════════════════════════════════════════════════════════════════════════════
#
#  ███████╗██╗███████╗██╗  ██╗    ███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗
#  ██╔════╝██║██╔════╝██║  ██║    ██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝
#  █████╗  ██║███████╗███████║    █████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║   
#  ██╔══╝  ██║╚════██║██╔══██║    ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║   
#  ██║     ██║███████║██║  ██║    ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   
#  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   
#
#  AUDIO FORMAT CONVERTER — GORUNFREE EDITION
#  44.1kHz/16-bit → 48kHz/24-bit (Broadcast Standard)
#
#═══════════════════════════════════════════════════════════════════════════════

set -e

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

FISH_ROOT="${FISH_ROOT:-/Volumes/FishMusic}"
FISH_DB="${FISH_ROOT}/_CATALOG/fish_music_master.db"
OUTPUT_DIR="${FISH_ROOT}/_CONVERTED"
NOIZYVOX_DIR="${FISH_ROOT}/NOIZYVOX"

# Target format (broadcast/film standard)
TARGET_SAMPLE_RATE=48000
TARGET_BIT_DEPTH=24
TARGET_FORMAT="wav"

# High-quality resampling
RESAMPLE_FILTER="soxr"  # Best quality (requires ffmpeg with soxr)
# Alternative: "sinc" or default

# Parallel jobs
PARALLEL_JOBS=4

# ══════════════════════════════════════════════════════════════════════════════
# COLORS
# ══════════════════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# ══════════════════════════════════════════════════════════════════════════════
# FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

print_banner() {
    echo -e "${CYAN}"
    echo "╔═══════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                       ║"
    echo "║   🎵 FISH MUSIC INC — FORMAT CONVERTER                               ║"
    echo "║                                                                       ║"
    echo "║   44.1kHz/16-bit (CD)  →  48kHz/24-bit (Broadcast)                   ║"
    echo "║                                                                       ║"
    echo "║   High-quality SoX resampling • Preserves dynamics                   ║"
    echo "║   GORUNFREE: One command converts everything                         ║"
    echo "║                                                                       ║"
    echo "╚═══════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# ══════════════════════════════════════════════════════════════════════════════
# ANALYSIS: Find files that need conversion
# ══════════════════════════════════════════════════════════════════════════════

analyze_library() {
    echo ""
    echo "═══════════════════════════════════════════════════════════════════════"
    echo "                    LIBRARY FORMAT ANALYSIS"
    echo "═══════════════════════════════════════════════════════════════════════"
    echo ""
    
    if [ ! -f "$FISH_DB" ]; then
        log_error "Database not found. Run fishcat first."
        return 1
    fi
    
    echo "SAMPLE RATE DISTRIBUTION:"
    echo "─────────────────────────"
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT 
    sample_rate as "Sample Rate",
    COUNT(*) as "Tracks",
    printf("%.1f hrs", SUM(duration_seconds)/3600) as "Duration",
    CASE 
        WHEN sample_rate = 48000 THEN '✓ Broadcast Ready'
        WHEN sample_rate = 44100 THEN '⚠ Needs Conversion'
        WHEN sample_rate = 96000 THEN '✓ Hi-Res (downsample OK)'
        ELSE '? Check'
    END as "Status"
FROM tracks 
WHERE sample_rate > 0
GROUP BY sample_rate
ORDER BY COUNT(*) DESC;
SQL

    echo ""
    echo "BIT DEPTH DISTRIBUTION:"
    echo "───────────────────────"
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT 
    bit_depth as "Bit Depth",
    COUNT(*) as "Tracks",
    CASE 
        WHEN bit_depth >= 24 THEN '✓ Broadcast Ready'
        WHEN bit_depth = 16 THEN '⚠ Can Upsample'
        ELSE '? Check'
    END as "Status"
FROM tracks 
WHERE bit_depth > 0
GROUP BY bit_depth
ORDER BY COUNT(*) DESC;
SQL

    echo ""
    echo "FORMAT DISTRIBUTION:"
    echo "────────────────────"
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT 
    UPPER(format) as "Format",
    COUNT(*) as "Tracks",
    printf("%.1f GB", SUM(file_size_bytes)/1073741824.0) as "Size"
FROM tracks 
GROUP BY format
ORDER BY COUNT(*) DESC;
SQL

    echo ""
    echo "FILES NEEDING CONVERSION:"
    echo "─────────────────────────"
    
    local NEED_CONVERT=$(sqlite3 "$FISH_DB" "SELECT COUNT(*) FROM tracks WHERE sample_rate = 44100 OR bit_depth = 16;")
    local ALREADY_OK=$(sqlite3 "$FISH_DB" "SELECT COUNT(*) FROM tracks WHERE sample_rate = 48000 AND bit_depth >= 24;")
    
    echo -e "  ${YELLOW}Need conversion:${NC}  $NEED_CONVERT tracks"
    echo -e "  ${GREEN}Already 48/24:${NC}    $ALREADY_OK tracks"
    echo ""
}

# ══════════════════════════════════════════════════════════════════════════════
# SINGLE FILE CONVERSION
# ══════════════════════════════════════════════════════════════════════════════

convert_file() {
    local INPUT="$1"
    local OUTPUT_BASE="$2"
    
    if [ ! -f "$INPUT" ]; then
        echo "SKIP: File not found: $INPUT"
        return 1
    fi
    
    local FILENAME=$(basename "$INPUT")
    local NAME="${FILENAME%.*}"
    local OUTPUT="${OUTPUT_BASE}/${NAME}_48k24.wav"
    
    # Skip if already converted
    if [ -f "$OUTPUT" ]; then
        echo "SKIP: Already exists: $OUTPUT"
        return 0
    fi
    
    # Get current format
    local INFO=$(ffprobe -v quiet -select_streams a:0 \
        -show_entries stream=sample_rate,bits_per_sample,channels \
        -of csv=p=0 "$INPUT" 2>/dev/null)
    
    IFS=',' read -r SR BD CH <<< "$INFO"
    
    # Check if conversion needed
    if [ "$SR" = "48000" ] && [ "$BD" -ge 24 ]; then
        # Just copy if already correct format
        echo "COPY: $FILENAME (already 48k/${BD}bit)"
        cp "$INPUT" "$OUTPUT"
        return 0
    fi
    
    echo "CONVERT: $FILENAME (${SR}Hz/${BD}bit → 48000Hz/24bit)"
    
    # High-quality conversion with ffmpeg
    ffmpeg -y -i "$INPUT" \
        -af "aresample=resampler=soxr:precision=28:dither_method=triangular" \
        -ar 48000 \
        -sample_fmt s32 \
        -c:a pcm_s24le \
        "$OUTPUT" \
        -v warning -stats 2>&1 | grep -v "^$"
    
    if [ $? -eq 0 ]; then
        echo "  ✓ Done: $(basename "$OUTPUT")"
        return 0
    else
        echo "  ✗ Failed: $FILENAME"
        return 1
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
# BATCH CONVERSION
# ══════════════════════════════════════════════════════════════════════════════

convert_all() {
    print_banner
    
    mkdir -p "$OUTPUT_DIR"
    
    log_info "Finding files that need conversion..."
    
    # Get list of files needing conversion
    local TEMP_LIST=$(mktemp)
    
    sqlite3 "$FISH_DB" << SQL > "$TEMP_LIST"
SELECT filepath FROM tracks 
WHERE (sample_rate != 48000 OR sample_rate IS NULL OR bit_depth < 24 OR bit_depth IS NULL)
AND format IN ('wav', 'aiff', 'aif', 'flac')
ORDER BY file_size_bytes DESC;
SQL
    
    local TOTAL=$(wc -l < "$TEMP_LIST" | tr -d ' ')
    
    if [ "$TOTAL" -eq 0 ]; then
        log_info "All files already at 48kHz/24-bit! Nothing to convert."
        rm -f "$TEMP_LIST"
        return 0
    fi
    
    log_info "Converting $TOTAL files to 48kHz/24-bit..."
    echo ""
    
    local COUNT=0
    local SUCCESS=0
    local FAILED=0
    
    while IFS= read -r FILE; do
        ((COUNT++))
        echo "[$COUNT/$TOTAL] Processing..."
        
        if convert_file "$FILE" "$OUTPUT_DIR"; then
            ((SUCCESS++))
        else
            ((FAILED++))
        fi
        
    done < "$TEMP_LIST"
    
    rm -f "$TEMP_LIST"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════════════"
    echo "                    CONVERSION COMPLETE"
    echo "═══════════════════════════════════════════════════════════════════════"
    echo ""
    echo -e "  ${GREEN}Successful:${NC}  $SUCCESS"
    echo -e "  ${RED}Failed:${NC}      $FAILED"
    echo -e "  ${CYAN}Output:${NC}      $OUTPUT_DIR"
    echo ""
}

# ══════════════════════════════════════════════════════════════════════════════
# CONVERT SPECIFIC FILES FOR NOIZYVOX
# ══════════════════════════════════════════════════════════════════════════════

convert_for_noizyvox() {
    local SEARCH_TERM="$1"
    
    if [ -z "$SEARCH_TERM" ]; then
        echo "Usage: fish_convert_nv <search_term>"
        echo "Example: fish_convert_nv 'hero theme'"
        return 1
    fi
    
    mkdir -p "$NOIZYVOX_DIR/DEMO_CUES"
    
    log_info "Finding and converting tracks matching: $SEARCH_TERM"
    
    # Find matching files
    local FILES=$(sqlite3 "$FISH_DB" << SQL
SELECT filepath FROM tracks 
WHERE filename LIKE '%$SEARCH_TERM%' 
   OR title LIKE '%$SEARCH_TERM%'
   OR searchable LIKE '%$SEARCH_TERM%'
LIMIT 5;
SQL
)
    
    if [ -z "$FILES" ]; then
        log_warn "No matches found for: $SEARCH_TERM"
        return 1
    fi
    
    echo "$FILES" | while read -r FILE; do
        if [ -n "$FILE" ]; then
            convert_file "$FILE" "$NOIZYVOX_DIR/DEMO_CUES"
        fi
    done
    
    log_info "Converted files are in: $NOIZYVOX_DIR/DEMO_CUES/"
}

# ══════════════════════════════════════════════════════════════════════════════
# CONVERT BY CUE NUMBER
# ══════════════════════════════════════════════════════════════════════════════

convert_cue() {
    local CUE="$1"
    local SEARCH="$2"
    
    if [ -z "$CUE" ] || [ -z "$SEARCH" ]; then
        echo "Usage: fish_convert_cue <cue_number> <search_term>"
        echo "Example: fish_convert_cue M03 'heroic brass'"
        return 1
    fi
    
    local CUE_DIR="$NOIZYVOX_DIR/DEMO_CUES/$CUE"
    mkdir -p "$CUE_DIR"
    
    log_info "Converting for cue $CUE: $SEARCH"
    
    # Find best match
    local FILE=$(sqlite3 "$FISH_DB" << SQL
SELECT filepath FROM tracks_fts 
JOIN tracks ON tracks_fts.rowid = tracks.id
WHERE tracks_fts MATCH '$SEARCH'
ORDER BY rank
LIMIT 1;
SQL
)
    
    if [ -z "$FILE" ]; then
        log_warn "No match found. Trying filename search..."
        FILE=$(sqlite3 "$FISH_DB" "SELECT filepath FROM tracks WHERE filename LIKE '%$SEARCH%' LIMIT 1;")
    fi
    
    if [ -n "$FILE" ] && [ -f "$FILE" ]; then
        convert_file "$FILE" "$CUE_DIR"
        log_info "Ready: $CUE_DIR/"
    else
        log_error "No file found for: $SEARCH"
        return 1
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
# QUICK COMMANDS (for shell profile)
# ══════════════════════════════════════════════════════════════════════════════

# Export functions for use in profile
export -f convert_file convert_for_noizyvox convert_cue

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

case "${1:-analyze}" in
    analyze|--analyze|-a)
        analyze_library
        ;;
    all|--all|-A)
        convert_all
        ;;
    search|--search|-s)
        convert_for_noizyvox "$2"
        ;;
    cue|--cue|-c)
        convert_cue "$2" "$3"
        ;;
    help|--help|-h)
        echo ""
        echo "FISH MUSIC FORMAT CONVERTER"
        echo "==========================="
        echo ""
        echo "Usage: fish_convert.sh [command] [args]"
        echo ""
        echo "Commands:"
        echo "  analyze          Show library format statistics (default)"
        echo "  all              Convert ALL files to 48kHz/24-bit"
        echo "  search <term>    Convert matching files"
        echo "  cue <num> <term> Convert for specific NOIZYVOX cue"
        echo ""
        echo "Examples:"
        echo "  ./fish_convert.sh analyze"
        echo "  ./fish_convert.sh all"
        echo "  ./fish_convert.sh search 'epic brass'"
        echo "  ./fish_convert.sh cue M03 'heroic theme'"
        echo ""
        ;;
    *)
        log_error "Unknown command: $1"
        echo "Use --help for usage"
        exit 1
        ;;
esac
