#!/bin/bash
#═══════════════════════════════════════════════════════════════════════════════
#
#  FISH MUSIC INC — GORUNFREE SHELL PROFILE
#
#  Add this to your ~/.zshrc or ~/.bashrc:
#  source /path/to/fish_profile.sh
#
#═══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

export FISH_ROOT="${FISH_ROOT:-/Volumes/FishMusic}"
export FISH_CATALOG="${FISH_ROOT}/_CATALOG"
export FISH_DB="${FISH_CATALOG}/fish_music_master.db"
export FISH_NOIZYVOX="${FISH_ROOT}/NOIZYVOX"

# ══════════════════════════════════════════════════════════════════════════════
# CATALOG COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

# Run full catalog
alias fishcat='bash ${FISH_CATALOG}/fish_catalog.sh'

# Quick re-scan (new files only)
fishupdate() {
    echo "🔄 Updating catalog with new files..."
    local NEW_FILES=$(find "$FISH_ROOT" -type f \( -iname "*.wav" -o -iname "*.aiff" -o -iname "*.mp3" -o -iname "*.flac" \) -newer "$FISH_DB" 2>/dev/null | wc -l)
    echo "Found $NEW_FILES new files"
    fishcat
}

# ══════════════════════════════════════════════════════════════════════════════
# SEARCH COMMANDS — GORUNFREE
# ══════════════════════════════════════════════════════════════════════════════

# Full-text search: fishs "epic brass trailer"
fishs() {
    if [ -z "$1" ]; then
        echo "Usage: fishs <search terms>"
        echo "Example: fishs \"epic brass heroic\""
        return 1
    fi
    
    local QUERY="$*"
    echo "🔍 Searching: $QUERY"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT 
    filename,
    COALESCE(genre, '-') as genre,
    COALESCE(project, '-') as project,
    printf("%.1f", duration_seconds) as dur,
    printf("%.0f", tempo_bpm) as bpm
FROM tracks_fts 
JOIN tracks ON tracks_fts.rowid = tracks.id
WHERE tracks_fts MATCH '$QUERY'
ORDER BY rank
LIMIT 25;
SQL
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# Search by genre: fishg "orchestral"
fishg() {
    local GENRE="$1"
    echo "🎭 Genre: $GENRE"
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT filename, project, printf("%.1f", duration_seconds) as dur, tempo_bpm
FROM tracks 
WHERE UPPER(genre) LIKE UPPER('%$GENRE%')
ORDER BY filename
LIMIT 30;
SQL
}

# Search by mood: fishm "heroic"
fishm() {
    local MOOD="$1"
    echo "💫 Mood: $MOOD"
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT filename, genre, printf("%.1f", duration_seconds) as dur
FROM tracks 
WHERE LOWER(mood) LIKE LOWER('%$MOOD%')
   OR LOWER(filename) LIKE LOWER('%$MOOD%')
   OR LOWER(tags) LIKE LOWER('%$MOOD%')
ORDER BY duration_seconds DESC
LIMIT 30;
SQL
}

# Search by BPM range: fishbpm 100 130
fishbpm() {
    local MIN="${1:-60}"
    local MAX="${2:-180}"
    echo "🎵 Tempo: ${MIN}-${MAX} BPM"
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT filename, genre, tempo_bpm, key_signature
FROM tracks 
WHERE tempo_bpm BETWEEN $MIN AND $MAX
ORDER BY tempo_bpm
LIMIT 50;
SQL
}

# Search by key: fishkey "D major"
fishkey() {
    local KEY="$1"
    echo "🎹 Key: $KEY"
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT filename, genre, tempo_bpm, key_signature
FROM tracks 
WHERE LOWER(key_signature) LIKE LOWER('%$KEY%')
ORDER BY tempo_bpm
LIMIT 50;
SQL
}

# Search by project: fishp "JOHNNY_TEST"
fishp() {
    local PROJECT="$1"
    echo "📁 Project: $PROJECT"
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT filename, genre, printf("%.1f", duration_seconds) as dur
FROM tracks 
WHERE UPPER(project) LIKE UPPER('%$PROJECT%')
ORDER BY filename;
SQL
}

# Search by duration range: fishdur 30 60 (30-60 seconds)
fishdur() {
    local MIN="${1:-0}"
    local MAX="${2:-9999}"
    echo "⏱️ Duration: ${MIN}-${MAX} seconds"
    sqlite3 -header -column "$FISH_DB" << SQL
SELECT filename, genre, printf("%.1f", duration_seconds) as dur, tempo_bpm
FROM tracks 
WHERE duration_seconds BETWEEN $MIN AND $MAX
ORDER BY duration_seconds
LIMIT 50;
SQL
}

# Get full path for a track: fishpath "filename"
fishpath() {
    sqlite3 "$FISH_DB" "SELECT filepath FROM tracks WHERE filename LIKE '%$1%' LIMIT 1;"
}

# ══════════════════════════════════════════════════════════════════════════════
# PLAYBACK COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

# Play a track: fishplay "filename"
fishplay() {
    local FILE=$(fishpath "$1")
    if [ -n "$FILE" ] && [ -f "$FILE" ]; then
        echo "▶️ Playing: $(basename "$FILE")"
        afplay "$FILE" &
        echo "   (fishstop to stop)"
    else
        echo "❌ Not found: $1"
    fi
}

# Stop playback
alias fishstop='killall afplay 2>/dev/null && echo "⏹️ Stopped"'

# Preview first 10 seconds: fishpreview "filename"
fishpreview() {
    local FILE=$(fishpath "$1")
    if [ -n "$FILE" ] && [ -f "$FILE" ]; then
        echo "▶️ Preview (10s): $(basename "$FILE")"
        afplay -t 10 "$FILE"
    else
        echo "❌ Not found: $1"
    fi
}

# Queue multiple tracks: fishqueue "track1" "track2" "track3"
fishqueue() {
    echo "📋 Queuing ${#@} tracks..."
    for term in "$@"; do
        local FILE=$(fishpath "$term")
        if [ -n "$FILE" ]; then
            echo "   + $(basename "$FILE")"
            afplay "$FILE"
        fi
    done
    echo "✅ Queue complete"
}

# ══════════════════════════════════════════════════════════════════════════════
# FILE OPERATIONS
# ══════════════════════════════════════════════════════════════════════════════

# Copy to NOIZYVOX folder: fishcopy "filename"
fishcopy() {
    local FILE=$(fishpath "$1")
    if [ -n "$FILE" ] && [ -f "$FILE" ]; then
        mkdir -p "$FISH_NOIZYVOX/DEMO_CUES"
        cp "$FILE" "$FISH_NOIZYVOX/DEMO_CUES/"
        echo "✅ Copied: $(basename "$FILE") → NOIZYVOX/DEMO_CUES/"
    else
        echo "❌ Not found: $1"
    fi
}

# Copy to specific cue folder: fishcue "filename" "M03"
fishcue() {
    local FILE=$(fishpath "$1")
    local CUE="$2"
    if [ -n "$FILE" ] && [ -f "$FILE" ] && [ -n "$CUE" ]; then
        mkdir -p "$FISH_NOIZYVOX/DEMO_CUES/$CUE"
        cp "$FILE" "$FISH_NOIZYVOX/DEMO_CUES/$CUE/"
        echo "✅ Copied: $(basename "$FILE") → NOIZYVOX/DEMO_CUES/$CUE/"
        
        # Log to database
        local TRACK_ID=$(sqlite3 "$FISH_DB" "SELECT id FROM tracks WHERE filepath='$FILE';")
        sqlite3 "$FISH_DB" "INSERT INTO noizyvox_cues (cue_name, track_id, status) VALUES ('$CUE', $TRACK_ID, 'assigned');"
    else
        echo "Usage: fishcue <filename> <cue_number>"
        echo "Example: fishcue hero_theme M03"
    fi
}

# Open file location in Finder: fishfind "filename"
fishfind() {
    local FILE=$(fishpath "$1")
    if [ -n "$FILE" ] && [ -f "$FILE" ]; then
        open -R "$FILE"
    else
        echo "❌ Not found: $1"
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
# STATISTICS & INFO
# ══════════════════════════════════════════════════════════════════════════════

# Show library stats
fishstats() {
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════════╗"
    echo "║                 FISH MUSIC INC — LIBRARY STATISTICS                  ║"
    echo "╚═══════════════════════════════════════════════════════════════════════╝"
    echo ""
    
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT 
    COUNT(*) as "Total Tracks",
    printf("%.1f", SUM(duration_seconds)/3600) as "Hours",
    printf("%.1f GB", SUM(file_size_bytes)/1073741824.0) as "Size"
FROM tracks;
SQL
    
    echo ""
    echo "BY GENRE:"
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT COALESCE(genre, 'Uncat.') as Genre, COUNT(*) as Tracks
FROM tracks GROUP BY genre ORDER BY Tracks DESC LIMIT 10;
SQL
    
    echo ""
    echo "BY PROJECT:"
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT COALESCE(project, 'Unassigned') as Project, COUNT(*) as Tracks
FROM tracks WHERE project != '' GROUP BY project ORDER BY Tracks DESC LIMIT 10;
SQL
}

# Show track info: fishinfo "filename"
fishinfo() {
    local FILE=$(fishpath "$1")
    if [ -z "$FILE" ]; then
        echo "❌ Not found: $1"
        return 1
    fi
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════════════"
    sqlite3 -line "$FISH_DB" << SQL
SELECT 
    filename,
    title,
    project,
    genre,
    mood,
    printf("%.1f sec", duration_seconds) as duration,
    printf("%d BPM", tempo_bpm) as tempo,
    key_signature,
    sample_rate || ' Hz' as sample_rate,
    bit_depth || '-bit' as bit_depth,
    channels || ' ch' as channels,
    printf("%.1f MB", file_size_bytes/1048576.0) as file_size,
    filepath
FROM tracks 
WHERE filepath = '$FILE';
SQL
    echo "═══════════════════════════════════════════════════════════════════════"
}

# ══════════════════════════════════════════════════════════════════════════════
# NOIZYVOX INTEGRATION
# ══════════════════════════════════════════════════════════════════════════════

# Match tracks to NOIZYVOX cues
fishnv() {
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════════╗"
    echo "║              NOIZYVOX — FISH MUSIC CUE MATCHER                       ║"
    echo "╚═══════════════════════════════════════════════════════════════════════╝"
    echo ""
    
    # Cue definitions
    declare -A CUES
    CUES["M01"]="ambient underscore tension drone"
    CUES["M02"]="magical transformation reveal strings"
    CUES["M03"]="heroic triumphant hopeful brass warm"
    CUES["M04"]="action military tactical percussion tense"
    CUES["M05"]="jazz noir mystery intimate piano"
    CUES["M06"]="corporate building inspiring technology"
    CUES["M07"]="trailer epic anticipation cinematic"
    CUES["M08"]="blockbuster climax epic orchestra"
    CUES["M09"]="anthem inspirational unity choir"
    CUES["M10"]="ending peaceful resolution ambient"
    
    for CUE in M01 M02 M03 M04 M05 M06 M07 M08 M09 M10; do
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "🎵 $CUE — ${CUES[$CUE]}"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        
        fishs "${CUES[$CUE]}" 2>/dev/null | head -8
        echo ""
    done
}

# Show NOIZYVOX cue assignments
fishnv_status() {
    echo "NOIZYVOX Cue Assignments:"
    sqlite3 -header -column "$FISH_DB" << 'SQL'
SELECT 
    nc.cue_name,
    t.filename,
    nc.status
FROM noizyvox_cues nc
JOIN tracks t ON nc.track_id = t.id
ORDER BY nc.cue_name;
SQL
}

# ══════════════════════════════════════════════════════════════════════════════
# QUICK ACCESS
# ══════════════════════════════════════════════════════════════════════════════

# Open Fish Music folder
alias fishopen='open "$FISH_ROOT"'

# Open NOIZYVOX folder
alias fishnvopen='open "$FISH_NOIZYVOX"'

# Open catalog folder
alias fishcatopen='open "$FISH_CATALOG"'

# Quick help
fishhelp() {
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════════╗"
    echo "║              FISH MUSIC INC — GORUNFREE COMMANDS                     ║"
    echo "╠═══════════════════════════════════════════════════════════════════════╣"
    echo "║                                                                       ║"
    echo "║  CATALOG:                                                             ║"
    echo "║    fishcat          Full catalog scan                                ║"
    echo "║    fishupdate       Update with new files only                       ║"
    echo "║                                                                       ║"
    echo "║  SEARCH:                                                              ║"
    echo "║    fishs <terms>    Full-text search                                 ║"
    echo "║    fishg <genre>    Search by genre                                  ║"
    echo "║    fishm <mood>     Search by mood                                   ║"
    echo "║    fishbpm 100 130  Search by BPM range                              ║"
    echo "║    fishkey <key>    Search by key (e.g., 'D major')                  ║"
    echo "║    fishp <project>  Search by project                                ║"
    echo "║    fishdur 30 60    Search by duration (seconds)                     ║"
    echo "║                                                                       ║"
    echo "║  PLAYBACK:                                                            ║"
    echo "║    fishplay <name>  Play track                                       ║"
    echo "║    fishpreview      Preview first 10 seconds                         ║"
    echo "║    fishstop         Stop playback                                    ║"
    echo "║                                                                       ║"
    echo "║  FILES:                                                               ║"
    echo "║    fishcopy <name>  Copy to NOIZYVOX folder                          ║"
    echo "║    fishcue <n> M03  Copy to specific cue folder                      ║"
    echo "║    fishfind <name>  Open in Finder                                   ║"
    echo "║    fishpath <name>  Get full path                                    ║"
    echo "║                                                                       ║"
    echo "║  INFO:                                                                ║"
    echo "║    fishstats        Library statistics                               ║"
    echo "║    fishinfo <name>  Track details                                    ║"
    echo "║                                                                       ║"
    echo "║  NOIZYVOX:                                                            ║"
    echo "║    fishnv           Match tracks to demo cues                        ║"
    echo "║    fishnv_status    Show cue assignments                             ║"
    echo "║                                                                       ║"
    echo "║  FOLDERS:                                                             ║"
    echo "║    fishopen         Open Fish Music folder                           ║"
    echo "║    fishnvopen       Open NOIZYVOX folder                             ║"
    echo "║                                                                       ║"
    echo "╚═══════════════════════════════════════════════════════════════════════╝"
    echo ""
}

# ══════════════════════════════════════════════════════════════════════════════
# FORMAT CONVERSION (44.1/16 → 48/24)
# ══════════════════════════════════════════════════════════════════════════════

# Analyze library formats
alias fishanalyze='${FISH_CATALOG}/fish_convert.sh analyze'

# Convert all files to 48/24
alias fishconvertall='${FISH_CATALOG}/fish_convert.sh all'

# Convert specific track: fishcv "hero theme"
fishcv() {
    ${FISH_CATALOG}/fish_convert.sh search "$*"
}

# Convert for specific cue: fishcvcue M03 "heroic brass"
fishcvcue() {
    ${FISH_CATALOG}/fish_convert.sh cue "$1" "${@:2}"
}

# Quick cue conversion aliases
alias fishM01='fishcvcue M01'
alias fishM02='fishcvcue M02'
alias fishM03='fishcvcue M03'
alias fishM04='fishcvcue M04'
alias fishM05='fishcvcue M05'
alias fishM06='fishcvcue M06'
alias fishM07='fishcvcue M07'
alias fishM08='fishcvcue M08'
alias fishM09='fishcvcue M09'
alias fishM10='fishcvcue M10'

# Check format of specific file: fishfmt "filename"
fishfmt() {
    local FILE=$(fishpath "$1")
    if [ -n "$FILE" ] && [ -f "$FILE" ]; then
        echo "═══════════════════════════════════════════════════════════════════════"
        echo "FILE: $(basename "$FILE")"
        echo "═══════════════════════════════════════════════════════════════════════"
        ffprobe -v quiet -select_streams a:0 \
            -show_entries stream=sample_rate,bits_per_sample,channels,codec_name \
            -of default=noprint_wrappers=1 "$FILE"
        
        local SR=$(ffprobe -v quiet -select_streams a:0 -show_entries stream=sample_rate -of csv=p=0 "$FILE")
        local BD=$(ffprobe -v quiet -select_streams a:0 -show_entries stream=bits_per_sample -of csv=p=0 "$FILE")
        
        echo ""
        if [ "$SR" = "48000" ] && [ "$BD" -ge 24 ]; then
            echo "✅ BROADCAST READY (48kHz/${BD}-bit)"
        elif [ "$SR" = "44100" ] && [ "$BD" = "16" ]; then
            echo "⚠️  CD FORMAT (44.1kHz/16-bit) — Convert with: fishcv \"$1\""
        else
            echo "ℹ️  Format: ${SR}Hz/${BD}-bit"
        fi
        echo "═══════════════════════════════════════════════════════════════════════"
    else
        echo "❌ Not found: $1"
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
# STARTUP MESSAGE
# ══════════════════════════════════════════════════════════════════════════════

echo "🎵 Fish Music Inc loaded. Type 'fishhelp' for commands."
echo "   44.1/16 → 48/24 conversion: fishanalyze, fishcv, fishM01-M10"
