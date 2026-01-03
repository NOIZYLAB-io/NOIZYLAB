#!/bin/bash
#═══════════════════════════════════════════════════════════════════════════════
#
#  ███████╗██╗███████╗██╗  ██╗    ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗
#  ██╔════╝██║██╔════╝██║  ██║    ████╗ ████║██║   ██║██╔════╝██║██╔════╝
#  █████╗  ██║███████╗███████║    ██╔████╔██║██║   ██║███████╗██║██║     
#  ██╔══╝  ██║╚════██║██╔══██║    ██║╚██╔╝██║██║   ██║╚════██║██║██║     
#  ██║     ██║███████║██║  ██║    ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗
#  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝
#
#  SUPERSONIC AUDIO CATALOGER — GORUNFREE EDITION
#  40 Years • One Command • Zero Friction
#
#═══════════════════════════════════════════════════════════════════════════════

set -e

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION — EDIT THESE FOR YOUR SETUP
# ══════════════════════════════════════════════════════════════════════════════

# Primary music library location
FISH_ROOT="${FISH_ROOT:-/Volumes/FishMusic}"

# Additional locations to scan (space-separated)
EXTRA_LOCATIONS=(
    "/Volumes/Archive_01"
    "/Volumes/Archive_02"
    "$HOME/Music/FishMusic"
)

# Catalog output location
CATALOG_DIR="${FISH_ROOT}/_CATALOG"

# Database file
DB_FILE="${CATALOG_DIR}/fish_music_master.db"

# Supported audio extensions
AUDIO_EXTENSIONS="wav|aiff|aif|mp3|m4a|flac|ogg|opus|mp2|wma|ac3"

# Parallel processing (adjust based on CPU cores)
PARALLEL_JOBS=8

# ══════════════════════════════════════════════════════════════════════════════
# COLORS & FORMATTING
# ══════════════════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# ══════════════════════════════════════════════════════════════════════════════
# BANNER
# ══════════════════════════════════════════════════════════════════════════════

print_banner() {
    echo -e "${CYAN}"
    echo "╔═══════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                       ║"
    echo "║   🎵 FISH MUSIC INC — SUPERSONIC CATALOGER                           ║"
    echo "║                                                                       ║"
    echo "║   40 Years of Broadcast-Quality Music                                ║"
    echo "║   Ed Edd n Eddy • Dragon Tales • Johnny Test • Transformers          ║"
    echo "║   Care Bears • Barbie • Hot Wheels • And Thousands More              ║"
    echo "║                                                                       ║"
    echo "║   GORUNFREE: One command. Everything cataloged.                      ║"
    echo "║                                                                       ║"
    echo "╚═══════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_step() {
    echo -e "${PURPLE}[STEP]${NC} $1"
}

progress_bar() {
    local current=$1
    local total=$2
    local width=50
    local percent=$((current * 100 / total))
    local filled=$((current * width / total))
    local empty=$((width - filled))
    
    printf "\r${CYAN}[${NC}"
    printf "%${filled}s" | tr ' ' '█'
    printf "%${empty}s" | tr ' ' '░'
    printf "${CYAN}]${NC} %3d%% (%d/%d)" $percent $current $total
}

# ══════════════════════════════════════════════════════════════════════════════
# DEPENDENCY CHECK
# ══════════════════════════════════════════════════════════════════════════════

check_dependencies() {
    log_step "Checking dependencies..."
    
    local missing=()
    
    # Required
    command -v sqlite3 >/dev/null 2>&1 || missing+=("sqlite3")
    command -v ffprobe >/dev/null 2>&1 || missing+=("ffmpeg (for ffprobe)")
    
    # Optional but recommended
    if ! command -v parallel >/dev/null 2>&1; then
        log_warn "GNU parallel not found. Install with: brew install parallel"
        log_warn "Falling back to sequential processing (slower)"
        PARALLEL_JOBS=1
    fi
    
    if [ ${#missing[@]} -gt 0 ]; then
        log_error "Missing required dependencies: ${missing[*]}"
        echo ""
        echo "Install with:"
        echo "  brew install sqlite ffmpeg"
        exit 1
    fi
    
    log_info "All dependencies satisfied ✓"
}

# ══════════════════════════════════════════════════════════════════════════════
# DATABASE SETUP
# ══════════════════════════════════════════════════════════════════════════════

setup_database() {
    log_step "Setting up database..."
    
    mkdir -p "$CATALOG_DIR"
    
    sqlite3 "$DB_FILE" << 'SCHEMA'
-- ═══════════════════════════════════════════════════════════════════════════
-- FISH MUSIC INC — DATABASE SCHEMA
-- ═══════════════════════════════════════════════════════════════════════════

-- Main tracks table
CREATE TABLE IF NOT EXISTS tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- File info
    filepath TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    directory TEXT,
    format TEXT,
    file_size_bytes INTEGER,
    checksum_md5 TEXT,
    
    -- Metadata
    title TEXT,
    artist TEXT DEFAULT 'Fish Music Inc',
    album TEXT,
    year INTEGER,
    track_number INTEGER,
    
    -- Classification
    project TEXT,
    genre TEXT,
    subgenre TEXT,
    mood TEXT,
    energy TEXT,
    tags TEXT,
    
    -- Audio properties
    duration_seconds REAL,
    sample_rate INTEGER,
    bit_depth INTEGER,
    channels INTEGER,
    bitrate_kbps INTEGER,
    
    -- Musical analysis
    tempo_bpm REAL,
    key_signature TEXT,
    time_signature TEXT,
    
    -- Timestamps
    date_created TEXT,
    date_modified TEXT,
    date_cataloged TEXT DEFAULT CURRENT_TIMESTAMP,
    date_analyzed TEXT,
    
    -- NOIZYVOX integration
    noizyvox_cue TEXT,
    noizyvox_persona TEXT,
    
    -- Notes
    notes TEXT,
    
    -- Search optimization
    searchable TEXT GENERATED ALWAYS AS (
        COALESCE(filename, '') || ' ' ||
        COALESCE(title, '') || ' ' ||
        COALESCE(project, '') || ' ' ||
        COALESCE(genre, '') || ' ' ||
        COALESCE(mood, '') || ' ' ||
        COALESCE(tags, '')
    ) STORED
);

-- Full-text search virtual table
CREATE VIRTUAL TABLE IF NOT EXISTS tracks_fts USING fts5(
    filename,
    title,
    project,
    genre,
    mood,
    tags,
    notes,
    content='tracks',
    content_rowid='id'
);

-- FTS triggers
CREATE TRIGGER IF NOT EXISTS tracks_ai AFTER INSERT ON tracks BEGIN
    INSERT INTO tracks_fts(rowid, filename, title, project, genre, mood, tags, notes)
    VALUES (new.id, new.filename, new.title, new.project, new.genre, new.mood, new.tags, new.notes);
END;

CREATE TRIGGER IF NOT EXISTS tracks_ad AFTER DELETE ON tracks BEGIN
    INSERT INTO tracks_fts(tracks_fts, rowid, filename, title, project, genre, mood, tags, notes)
    VALUES ('delete', old.id, old.filename, old.title, old.project, old.genre, old.mood, old.tags, old.notes);
END;

CREATE TRIGGER IF NOT EXISTS tracks_au AFTER UPDATE ON tracks BEGIN
    INSERT INTO tracks_fts(tracks_fts, rowid, filename, title, project, genre, mood, tags, notes)
    VALUES ('delete', old.id, old.filename, old.title, old.project, old.genre, old.mood, old.tags, old.notes);
    INSERT INTO tracks_fts(rowid, filename, title, project, genre, mood, tags, notes)
    VALUES (new.id, new.filename, new.title, new.project, new.genre, new.mood, new.tags, new.notes);
END;

-- Projects catalog
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    display_name TEXT,
    year_start INTEGER,
    year_end INTEGER,
    client TEXT,
    track_count INTEGER DEFAULT 0,
    notes TEXT
);

-- Known projects (Rob's credits)
INSERT OR IGNORE INTO projects (name, display_name, client) VALUES
    ('ED_EDD_EDDY', 'Ed, Edd n Eddy', 'Cartoon Network'),
    ('DRAGON_TALES', 'Dragon Tales', 'PBS'),
    ('JOHNNY_TEST', 'Johnny Test', 'Cartoon Network'),
    ('TRANSFORMERS', 'Transformers', 'Hasbro'),
    ('CARE_BEARS', 'Care Bears', 'American Greetings'),
    ('BARBIE', 'Barbie Films', 'Mattel'),
    ('HOT_WHEELS', 'Hot Wheels', 'Mattel'),
    ('POLLY_POCKET', 'Polly Pocket', 'Mattel'),
    ('HE_MAN', 'He-Man', 'Mattel');

-- Genre categories
CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    parent TEXT,
    track_count INTEGER DEFAULT 0
);

INSERT OR IGNORE INTO genres (name, parent) VALUES
    ('ACTION', NULL),
    ('AMBIENT', NULL),
    ('ANIMATION', NULL),
    ('CINEMATIC', NULL),
    ('COMEDY', NULL),
    ('CORPORATE', NULL),
    ('DOCUMENTARY', NULL),
    ('DRAMA', NULL),
    ('ELECTRONIC', NULL),
    ('EPIC', NULL),
    ('HORROR', NULL),
    ('JAZZ', NULL),
    ('KIDS', NULL),
    ('ORCHESTRAL', NULL),
    ('POP', NULL),
    ('ROCK', NULL),
    ('ROMANTIC', NULL),
    ('SUSPENSE', NULL),
    ('TRAILER', NULL),
    ('WORLD', NULL);

-- Mood categories
CREATE TABLE IF NOT EXISTS moods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    energy_level TEXT,
    track_count INTEGER DEFAULT 0
);

INSERT OR IGNORE INTO moods (name, energy_level) VALUES
    ('heroic', 'high'),
    ('triumphant', 'high'),
    ('epic', 'high'),
    ('action', 'high'),
    ('exciting', 'high'),
    ('happy', 'medium-high'),
    ('uplifting', 'medium-high'),
    ('playful', 'medium'),
    ('mysterious', 'medium'),
    ('romantic', 'medium'),
    ('peaceful', 'low'),
    ('ambient', 'low'),
    ('sad', 'low'),
    ('dark', 'low'),
    ('tense', 'medium'),
    ('suspenseful', 'medium');

-- NOIZYVOX cue assignments
CREATE TABLE IF NOT EXISTS noizyvox_cues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cue_name TEXT NOT NULL,
    cue_number TEXT,
    track_id INTEGER,
    start_time REAL DEFAULT 0,
    end_time REAL,
    status TEXT DEFAULT 'candidate',
    notes TEXT,
    FOREIGN KEY (track_id) REFERENCES tracks(id)
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_tracks_project ON tracks(project);
CREATE INDEX IF NOT EXISTS idx_tracks_genre ON tracks(genre);
CREATE INDEX IF NOT EXISTS idx_tracks_mood ON tracks(mood);
CREATE INDEX IF NOT EXISTS idx_tracks_tempo ON tracks(tempo_bpm);
CREATE INDEX IF NOT EXISTS idx_tracks_key ON tracks(key_signature);
CREATE INDEX IF NOT EXISTS idx_tracks_duration ON tracks(duration_seconds);
CREATE INDEX IF NOT EXISTS idx_tracks_format ON tracks(format);
CREATE INDEX IF NOT EXISTS idx_tracks_directory ON tracks(directory);

-- Stats view
CREATE VIEW IF NOT EXISTS library_stats AS
SELECT
    COUNT(*) as total_tracks,
    SUM(duration_seconds) / 3600.0 as total_hours,
    SUM(file_size_bytes) / 1073741824.0 as total_gb,
    COUNT(DISTINCT project) as unique_projects,
    COUNT(DISTINCT genre) as unique_genres,
    AVG(tempo_bpm) as avg_tempo,
    MIN(date_modified) as oldest_file,
    MAX(date_modified) as newest_file
FROM tracks;

SCHEMA

    log_info "Database schema initialized ✓"
}

# ══════════════════════════════════════════════════════════════════════════════
# FILE SCANNING
# ══════════════════════════════════════════════════════════════════════════════

scan_files() {
    log_step "Scanning for audio files..."
    
    local temp_file=$(mktemp)
    local locations=("$FISH_ROOT")
    
    # Add extra locations if they exist
    for loc in "${EXTRA_LOCATIONS[@]}"; do
        if [ -d "$loc" ]; then
            locations+=("$loc")
            log_info "Including: $loc"
        fi
    done
    
    # Find all audio files
    for loc in "${locations[@]}"; do
        find "$loc" -type f -iregex ".*\.\(${AUDIO_EXTENSIONS}\)$" 2>/dev/null
    done | sort -u > "$temp_file"
    
    TOTAL_FILES=$(wc -l < "$temp_file" | tr -d ' ')
    log_info "Found $TOTAL_FILES audio files"
    
    echo "$temp_file"
}

# ══════════════════════════════════════════════════════════════════════════════
# METADATA EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

extract_metadata() {
    local FILE="$1"
    
    # Basic file info
    local FILENAME=$(basename "$FILE")
    local DIRECTORY=$(dirname "$FILE")
    local FORMAT="${FILE##*.}"
    local FILESIZE=$(stat -f%z "$FILE" 2>/dev/null || stat --printf="%s" "$FILE" 2>/dev/null || echo "0")
    
    # Get dates
    local DATE_MOD=$(stat -f%Sm -t%Y-%m-%d "$FILE" 2>/dev/null || \
                     date -r "$FILE" +%Y-%m-%d 2>/dev/null || echo "")
    
    # Extract with ffprobe
    local FFPROBE_JSON=$(ffprobe -v quiet -print_format json \
        -show_format -show_streams "$FILE" 2>/dev/null || echo "{}")
    
    # Parse JSON with Python (more reliable than jq for complex data)
    local METADATA=$(python3 << PYPARSE
import json
import sys

data = '''$FFPROBE_JSON'''

try:
    j = json.loads(data)
    fmt = j.get('format', {})
    streams = j.get('streams', [])
    audio = next((s for s in streams if s.get('codec_type') == 'audio'), {})
    tags = fmt.get('tags', {})
    
    # Handle case-insensitive tags
    tags_lower = {k.lower(): v for k, v in tags.items()}
    
    print(fmt.get('duration', '0'))
    print(audio.get('sample_rate', '0'))
    print(audio.get('bits_per_sample', audio.get('bits_per_raw_sample', '0')))
    print(audio.get('channels', '0'))
    print(int(float(fmt.get('bit_rate', '0')) / 1000))
    print(tags_lower.get('title', ''))
    print(tags_lower.get('artist', ''))
    print(tags_lower.get('album', ''))
    print(tags_lower.get('genre', ''))
    print(tags_lower.get('date', tags_lower.get('year', '')))
except:
    print('0\n0\n0\n0\n0\n\n\n\n\n')
PYPARSE
)
    
    # Parse metadata lines
    IFS=$'\n' read -rd '' -a META_ARRAY <<< "$METADATA" || true
    
    local DURATION="${META_ARRAY[0]:-0}"
    local SAMPLE_RATE="${META_ARRAY[1]:-0}"
    local BIT_DEPTH="${META_ARRAY[2]:-0}"
    local CHANNELS="${META_ARRAY[3]:-0}"
    local BITRATE="${META_ARRAY[4]:-0}"
    local TITLE="${META_ARRAY[5]:-}"
    local ARTIST="${META_ARRAY[6]:-Fish Music Inc}"
    local ALBUM="${META_ARRAY[7]:-}"
    local GENRE="${META_ARRAY[8]:-}"
    local YEAR="${META_ARRAY[9]:-}"
    
    # Infer project from path
    local PROJECT=""
    for proj in ED_EDD_EDDY DRAGON_TALES JOHNNY_TEST TRANSFORMERS CARE_BEARS BARBIE HOT_WHEELS POLLY_POCKET HE_MAN; do
        if [[ "$FILE" == *"$proj"* ]] || [[ "$FILE" == *"${proj//_/ }"* ]]; then
            PROJECT="$proj"
            break
        fi
    done
    
    # Infer genre from path if not in metadata
    if [ -z "$GENRE" ]; then
        for g in ACTION AMBIENT ANIMATION CINEMATIC COMEDY CORPORATE DOCUMENTARY DRAMA ELECTRONIC EPIC HORROR JAZZ KIDS ORCHESTRAL POP ROCK ROMANTIC SUSPENSE TRAILER WORLD; do
            if [[ "$FILE" == *"$g"* ]] || [[ "$FILE" == *"${g,,}"* ]]; then
                GENRE="$g"
                break
            fi
        done
    fi
    
    # Calculate MD5 (fast, first 1MB only for speed)
    local CHECKSUM=$(head -c 1048576 "$FILE" 2>/dev/null | md5 -q 2>/dev/null || \
                     head -c 1048576 "$FILE" 2>/dev/null | md5sum 2>/dev/null | cut -d' ' -f1 || echo "")
    
    # Escape for SQL
    FILE="${FILE//\'/\'\'}"
    FILENAME="${FILENAME//\'/\'\'}"
    DIRECTORY="${DIRECTORY//\'/\'\'}"
    TITLE="${TITLE//\'/\'\'}"
    ARTIST="${ARTIST//\'/\'\'}"
    ALBUM="${ALBUM//\'/\'\'}"
    GENRE="${GENRE//\'/\'\'}"
    
    # Insert into database
    sqlite3 "$DB_FILE" << SQL
INSERT OR REPLACE INTO tracks (
    filepath, filename, directory, format, file_size_bytes, checksum_md5,
    title, artist, album, year, project, genre,
    duration_seconds, sample_rate, bit_depth, channels, bitrate_kbps,
    date_modified
) VALUES (
    '$FILE', '$FILENAME', '$DIRECTORY', '$FORMAT', $FILESIZE, '$CHECKSUM',
    '$TITLE', '$ARTIST', '$ALBUM', ${YEAR:-NULL}, '$PROJECT', '$GENRE',
    ${DURATION:-0}, ${SAMPLE_RATE:-0}, ${BIT_DEPTH:-0}, ${CHANNELS:-0}, ${BITRATE:-0},
    '$DATE_MOD'
);
SQL
}

# ══════════════════════════════════════════════════════════════════════════════
# MAIN CATALOGING
# ══════════════════════════════════════════════════════════════════════════════

run_catalog() {
    log_step "Cataloging audio files..."
    
    local FILE_LIST="$1"
    local TOTAL=$(wc -l < "$FILE_LIST" | tr -d ' ')
    local COUNT=0
    local START_TIME=$(date +%s)
    
    # Export function for parallel (if available)
    export -f extract_metadata
    export DB_FILE
    
    if [ "$PARALLEL_JOBS" -gt 1 ] && command -v parallel >/dev/null 2>&1; then
        # Parallel processing
        log_info "Using parallel processing ($PARALLEL_JOBS jobs)..."
        
        cat "$FILE_LIST" | parallel -j "$PARALLEL_JOBS" --bar extract_metadata {}
    else
        # Sequential processing
        while IFS= read -r FILE; do
            ((COUNT++))
            
            # Progress every 50 files
            if (( COUNT % 50 == 0 )) || (( COUNT == TOTAL )); then
                progress_bar $COUNT $TOTAL
            fi
            
            extract_metadata "$FILE"
            
        done < "$FILE_LIST"
        echo ""
    fi
    
    local END_TIME=$(date +%s)
    local ELAPSED=$((END_TIME - START_TIME))
    
    log_info "Cataloging complete in ${ELAPSED}s"
}

# ══════════════════════════════════════════════════════════════════════════════
# STATISTICS & REPORTS
# ══════════════════════════════════════════════════════════════════════════════

generate_reports() {
    log_step "Generating reports..."
    
    # JSON index for quick access
    sqlite3 "$DB_FILE" << 'SQL' > "${CATALOG_DIR}/fish_music_index.json"
.mode json
SELECT 
    id, filename, title, project, genre, mood,
    tempo_bpm, key_signature, duration_seconds,
    filepath
FROM tracks
ORDER BY genre, filename;
SQL
    
    # CSV export
    sqlite3 -header -csv "$DB_FILE" << 'SQL' > "${CATALOG_DIR}/fish_music_catalog.csv"
SELECT 
    id, filename, title, artist, project, genre, mood,
    tempo_bpm, key_signature, duration_seconds,
    sample_rate, bit_depth, format, filepath
FROM tracks
ORDER BY project, genre, filename;
SQL
    
    # Stats summary
    sqlite3 "$DB_FILE" << 'SQL' > "${CATALOG_DIR}/library_stats.txt"
.mode column
.headers on

SELECT '═══════════════════════════════════════════════════════════════════════' as '';
SELECT '                    FISH MUSIC INC — LIBRARY STATISTICS                ' as '';
SELECT '═══════════════════════════════════════════════════════════════════════' as '';
SELECT '' as '';

SELECT 'TOTALS' as '═══════════════════════════════════════════════════════════════════════';
SELECT 
    COUNT(*) as "Total Tracks",
    printf("%.1f", SUM(duration_seconds)/3600) as "Total Hours",
    printf("%.1f GB", SUM(file_size_bytes)/1073741824.0) as "Total Size"
FROM tracks;

SELECT '' as '';
SELECT 'BY GENRE' as '═══════════════════════════════════════════════════════════════════════';
SELECT 
    COALESCE(genre, 'Uncategorized') as Genre,
    COUNT(*) as Tracks,
    printf("%.1f hrs", SUM(duration_seconds)/3600) as Duration
FROM tracks
GROUP BY genre
ORDER BY COUNT(*) DESC
LIMIT 20;

SELECT '' as '';
SELECT 'BY PROJECT' as '═══════════════════════════════════════════════════════════════════════';
SELECT 
    COALESCE(project, 'Unassigned') as Project,
    COUNT(*) as Tracks
FROM tracks
WHERE project IS NOT NULL AND project != ''
GROUP BY project
ORDER BY COUNT(*) DESC
LIMIT 15;

SELECT '' as '';
SELECT 'BY FORMAT' as '═══════════════════════════════════════════════════════════════════════';
SELECT 
    UPPER(format) as Format,
    COUNT(*) as Tracks,
    printf("%.1f GB", SUM(file_size_bytes)/1073741824.0) as Size
FROM tracks
GROUP BY format
ORDER BY COUNT(*) DESC;

SELECT '' as '';
SELECT 'BY SAMPLE RATE' as '═══════════════════════════════════════════════════════════════════════';
SELECT 
    sample_rate as "Sample Rate",
    COUNT(*) as Tracks
FROM tracks
WHERE sample_rate > 0
GROUP BY sample_rate
ORDER BY sample_rate DESC;

SELECT '' as '';
SELECT 'TEMPO DISTRIBUTION' as '═══════════════════════════════════════════════════════════════════════';
SELECT 
    CASE 
        WHEN tempo_bpm < 60 THEN 'Slow (<60)'
        WHEN tempo_bpm < 90 THEN 'Medium-Slow (60-89)'
        WHEN tempo_bpm < 120 THEN 'Medium (90-119)'
        WHEN tempo_bpm < 150 THEN 'Medium-Fast (120-149)'
        ELSE 'Fast (150+)'
    END as "Tempo Range",
    COUNT(*) as Tracks
FROM tracks
WHERE tempo_bpm > 0
GROUP BY 1
ORDER BY MIN(tempo_bpm);
SQL
    
    log_info "Reports generated ✓"
}

# ══════════════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ══════════════════════════════════════════════════════════════════════════════

print_summary() {
    echo ""
    echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║                                                                       ║${NC}"
    echo -e "${CYAN}║   ${WHITE}✅ FISH MUSIC INC — CATALOG COMPLETE${CYAN}                              ║${NC}"
    echo -e "${CYAN}║                                                                       ║${NC}"
    
    # Get stats
    local STATS=$(sqlite3 "$DB_FILE" "SELECT COUNT(*), printf('%.1f', SUM(duration_seconds)/3600), printf('%.1f', SUM(file_size_bytes)/1073741824.0) FROM tracks;")
    IFS='|' read -r TRACKS HOURS GB <<< "$STATS"
    
    echo -e "${CYAN}║   ${GREEN}Total Tracks:${NC}     $TRACKS"
    echo -e "${CYAN}║   ${GREEN}Total Duration:${NC}   $HOURS hours"
    echo -e "${CYAN}║   ${GREEN}Total Size:${NC}       $GB GB"
    echo -e "${CYAN}║                                                                       ║${NC}"
    echo -e "${CYAN}║   ${WHITE}Files:${NC}"
    echo -e "${CYAN}║   ${NC}  Database:  $DB_FILE"
    echo -e "${CYAN}║   ${NC}  JSON:      ${CATALOG_DIR}/fish_music_index.json"
    echo -e "${CYAN}║   ${NC}  CSV:       ${CATALOG_DIR}/fish_music_catalog.csv"
    echo -e "${CYAN}║   ${NC}  Stats:     ${CATALOG_DIR}/library_stats.txt"
    echo -e "${CYAN}║                                                                       ║${NC}"
    echo -e "${CYAN}║   ${YELLOW}GORUNFREE: Knowledge stored. Instant access enabled.${NC}"
    echo -e "${CYAN}║                                                                       ║${NC}"
    echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

main() {
    print_banner
    check_dependencies
    setup_database
    
    local FILE_LIST=$(scan_files)
    run_catalog "$FILE_LIST"
    
    rm -f "$FILE_LIST"
    
    generate_reports
    print_summary
    
    # Update genre/project counts
    sqlite3 "$DB_FILE" << 'SQL'
UPDATE genres SET track_count = (
    SELECT COUNT(*) FROM tracks WHERE tracks.genre = genres.name
);
UPDATE projects SET track_count = (
    SELECT COUNT(*) FROM tracks WHERE tracks.project = projects.name
);
SQL
    
    log_info "🎵 Catalog ready. Use 'fishs' to search!"
}

# Run if executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
