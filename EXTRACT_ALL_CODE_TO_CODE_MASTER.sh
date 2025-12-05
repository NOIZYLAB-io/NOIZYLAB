#!/bin/zsh
# ============================================================================
# COMPLETE CODE EXTRACTION TO CODE_MASTER
# Date: November 18, 2025
# Purpose: Extract and organize ALL code from 4TBSG to 4TB_02/CODE_MASTER
# ============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Source and destination
SOURCE_DRIVE="/Volumes/4TBSG"
DEST_BASE="/Volumes/4TB_02/CODE_MASTER"
LOG_FILE="${DEST_BASE}/logs/transfer_$(date +%Y%m%d_%H%M%S).log"

# Create log directory
mkdir -p "${DEST_BASE}/logs"

echo "${BLUE}============================================================================${NC}"
echo "${BLUE}STARTING COMPLETE CODE EXTRACTION${NC}"
echo "${BLUE}============================================================================${NC}"
echo "Source: ${SOURCE_DRIVE}"
echo "Destination: ${DEST_BASE}"
echo "Log: ${LOG_FILE}"
echo ""

# Function to log and print
log_action() {
    echo "$1" | tee -a "${LOG_FILE}"
}

# Function to safely copy with mkdir
safe_copy() {
    local src="$1"
    local dst="$2"
    
    mkdir -p "$(dirname "$dst")"
    
    if [[ -e "$src" ]]; then
        if [[ -d "$src" ]]; then
            log_action "${GREEN}[COPY DIR]${NC} $src -> $dst"
            rsync -av --progress "$src/" "$dst/" 2>&1 | tee -a "${LOG_FILE}"
        else
            log_action "${GREEN}[COPY FILE]${NC} $src -> $dst"
            cp -p "$src" "$dst" 2>&1 | tee -a "${LOG_FILE}"
        fi
        return 0
    else
        log_action "${YELLOW}[SKIP]${NC} Source not found: $src"
        return 1
    fi
}

log_action "${BLUE}[START]${NC} Code extraction started at $(date)"

# ============================================================================
# 1. PYTHON CODE
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING PYTHON CODE ===${NC}"

# Extensions/magenta-realtime-main
if [[ -d "${SOURCE_DRIVE}/Extensions/magenta-realtime-main" ]]; then
    safe_copy "${SOURCE_DRIVE}/Extensions/magenta-realtime-main" \
              "${DEST_BASE}/python/projects/magenta-realtime"
fi

# Extensions/VSCodeMaster/TrackFilter
if [[ -d "${SOURCE_DRIVE}/Extensions/VSCodeMaster/TrackFilter" ]]; then
    safe_copy "${SOURCE_DRIVE}/Extensions/VSCodeMaster/TrackFilter" \
              "${DEST_BASE}/python/projects/trackfilter"
fi

# organize_libraries.py
if [[ -f "${SOURCE_DRIVE}/KTK 2026 TO SORT/organize_libraries.py" ]]; then
    safe_copy "${SOURCE_DRIVE}/KTK 2026 TO SORT/organize_libraries.py" \
              "${DEST_BASE}/python/scripts/organize_libraries.py"
fi

# Find all standalone Python files
log_action "${YELLOW}[SEARCH]${NC} Finding all standalone Python files..."
find "${SOURCE_DRIVE}" -name "*.py" -type f 2>/dev/null | while read -r pyfile; do
    # Skip if already in a copied directory
    if [[ "$pyfile" != *"magenta-realtime"* ]] && \
       [[ "$pyfile" != *"TrackFilter"* ]] && \
       [[ "$pyfile" != *"__pycache__"* ]] && \
       [[ "$pyfile" != *".venv"* ]] && \
       [[ "$pyfile" != *"node_modules"* ]]; then
        
        # Create relative path structure
        rel_path="${pyfile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/python/extracted/${rel_path}"
        safe_copy "$pyfile" "$dest_path"
    fi
done

# ============================================================================
# 2. SHELL SCRIPTS
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING SHELL SCRIPTS ===${NC}"

find "${SOURCE_DRIVE}" -name "*.sh" -type f 2>/dev/null | while read -r shfile; do
    if [[ "$shfile" != *".venv"* ]] && [[ "$shfile" != *"node_modules"* ]]; then
        rel_path="${shfile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/scripts/shell/${rel_path}"
        safe_copy "$shfile" "$dest_path"
    fi
done

# ============================================================================
# 3. JAVASCRIPT/TYPESCRIPT/NODE.JS
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING JAVASCRIPT/TYPESCRIPT CODE ===${NC}"

# Find all JS/TS files and package.json files
find "${SOURCE_DRIVE}" \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" -o -name "package.json" \) -type f 2>/dev/null | while read -r jsfile; do
    if [[ "$jsfile" != *"node_modules"* ]] && \
       [[ "$jsfile" != *".venv"* ]] && \
       [[ "$jsfile" != *"__pycache__"* ]]; then
        
        rel_path="${jsfile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/nodejs/${rel_path}"
        safe_copy "$jsfile" "$dest_path"
    fi
done

# ============================================================================
# 4. JSON/YAML CONFIGURATION FILES
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING CONFIGURATION FILES ===${NC}"

find "${SOURCE_DRIVE}" \( -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name ".env*" -o -name "*.toml" \) -type f 2>/dev/null | while read -r conffile; do
    if [[ "$conffile" != *"node_modules"* ]] && \
       [[ "$conffile" != *".venv"* ]] && \
       [[ "$conffile" != *"Library"* ]] && \
       [[ "$conffile" != *"System"* ]]; then
        
        rel_path="${conffile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/config/${rel_path}"
        safe_copy "$conffile" "$dest_path"
    fi
done

# ============================================================================
# 5. GIT REPOSITORIES
# ============================================================================
log_action ""
log_action "${BLUE}=== FINDING GIT REPOSITORIES ===${NC}"

find "${SOURCE_DRIVE}" -name ".git" -type d 2>/dev/null | while read -r gitdir; do
    repo_dir=$(dirname "$gitdir")
    repo_name=$(basename "$repo_dir")
    
    log_action "${YELLOW}[GIT REPO FOUND]${NC} $repo_dir"
    safe_copy "$repo_dir" "${DEST_BASE}/git_repos/${repo_name}"
done

# ============================================================================
# 6. DOCUMENTATION
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING DOCUMENTATION ===${NC}"

find "${SOURCE_DRIVE}" \( -name "*.md" -o -name "README*" -o -name "LICENSE*" \) -type f 2>/dev/null | while read -r docfile; do
    if [[ "$docfile" != *"node_modules"* ]] && \
       [[ "$docfile" != *".venv"* ]]; then
        
        rel_path="${docfile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/docs/${rel_path}"
        safe_copy "$docfile" "$dest_path"
    fi
done

# ============================================================================
# 7. SPECIAL: CODE_FILES and DOCUMENT_FILES directories
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING SPECIAL CODE DIRECTORIES ===${NC}"

if [[ -d "${SOURCE_DRIVE}/KTK 2026 TO SORT/CODE_FILES" ]]; then
    safe_copy "${SOURCE_DRIVE}/KTK 2026 TO SORT/CODE_FILES" \
              "${DEST_BASE}/other_code/ktk_code_files"
fi

if [[ -d "${SOURCE_DRIVE}/KTK 2026 TO SORT/DOCUMENT_FILES" ]]; then
    safe_copy "${SOURCE_DRIVE}/KTK 2026 TO SORT/DOCUMENT_FILES" \
              "${DEST_BASE}/docs/ktk_documents"
fi

# ============================================================================
# 8. VISUAL STUDIO CODE / IDE CONFIGURATIONS
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING IDE CONFIGURATIONS ===${NC}"

find "${SOURCE_DRIVE}" \( -name ".vscode" -o -name ".idea" -o -name "*.code-workspace" \) 2>/dev/null | while read -r idefile; do
    if [[ -e "$idefile" ]]; then
        rel_path="${idefile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/config/ide/${rel_path}"
        safe_copy "$idefile" "$dest_path"
    fi
done

# ============================================================================
# 9. JUPYTER NOTEBOOKS
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING JUPYTER NOTEBOOKS ===${NC}"

find "${SOURCE_DRIVE}" -name "*.ipynb" -type f 2>/dev/null | while read -r notebook; do
    if [[ "$notebook" != *".venv"* ]] && [[ "$notebook" != *"node_modules"* ]]; then
        rel_path="${notebook#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/python/notebooks/${rel_path}"
        safe_copy "$notebook" "$dest_path"
    fi
done

# ============================================================================
# 10. REQUIREMENTS AND DEPENDENCY FILES
# ============================================================================
log_action ""
log_action "${BLUE}=== EXTRACTING DEPENDENCY FILES ===${NC}"

find "${SOURCE_DRIVE}" \( -name "requirements.txt" -o -name "Pipfile" -o -name "poetry.lock" -o -name "package-lock.json" -o -name "yarn.lock" -o -name "Gemfile" -o -name "Cargo.toml" \) -type f 2>/dev/null | while read -r depfile; do
    if [[ "$depfile" != *"node_modules"* ]] && [[ "$depfile" != *".venv"* ]]; then
        rel_path="${depfile#${SOURCE_DRIVE}/}"
        dest_path="${DEST_BASE}/config/dependencies/${rel_path}"
        safe_copy "$depfile" "$dest_path"
    fi
done

# ============================================================================
# GENERATE SUMMARY REPORT
# ============================================================================
log_action ""
log_action "${BLUE}=== GENERATING SUMMARY REPORT ===${NC}"

SUMMARY_FILE="${DEST_BASE}/EXTRACTION_SUMMARY_$(date +%Y%m%d_%H%M%S).md"

cat > "$SUMMARY_FILE" << EOF
# CODE EXTRACTION SUMMARY
**Date:** $(date)
**Source:** ${SOURCE_DRIVE}
**Destination:** ${DEST_BASE}

## Statistics

### Python Files
\`\`\`
$(find "${DEST_BASE}/python" -name "*.py" -type f 2>/dev/null | wc -l) Python files extracted
\`\`\`

### Shell Scripts
\`\`\`
$(find "${DEST_BASE}/scripts" -name "*.sh" -type f 2>/dev/null | wc -l) Shell scripts extracted
\`\`\`

### JavaScript/TypeScript Files
\`\`\`
$(find "${DEST_BASE}/nodejs" \( -name "*.js" -o -name "*.ts" \) -type f 2>/dev/null | wc -l) JS/TS files extracted
\`\`\`

### Configuration Files
\`\`\`
$(find "${DEST_BASE}/config" -type f 2>/dev/null | wc -l) Configuration files extracted
\`\`\`

### Documentation Files
\`\`\`
$(find "${DEST_BASE}/docs" -name "*.md" -type f 2>/dev/null | wc -l) Markdown documents extracted
\`\`\`

### Git Repositories
\`\`\`
$(find "${DEST_BASE}/git_repos" -type d -name ".git" 2>/dev/null | wc -l) Git repositories extracted
\`\`\`

### Jupyter Notebooks
\`\`\`
$(find "${DEST_BASE}/python/notebooks" -name "*.ipynb" -type f 2>/dev/null | wc -l) Jupyter notebooks extracted
\`\`\`

## Directory Structure
\`\`\`
$(tree -L 2 "${DEST_BASE}" 2>/dev/null || find "${DEST_BASE}" -type d -maxdepth 2 2>/dev/null)
\`\`\`

## Total Size
\`\`\`
$(du -sh "${DEST_BASE}" 2>/dev/null)
\`\`\`

## Detailed Log
See: ${LOG_FILE}

---
**Status:** EXTRACTION COMPLETE ✓
**Ready for system reformat:** YES
EOF

log_action ""
log_action "${GREEN}============================================================================${NC}"
log_action "${GREEN}EXTRACTION COMPLETE!${NC}"
log_action "${GREEN}============================================================================${NC}"
log_action ""
log_action "Summary report: ${SUMMARY_FILE}"
log_action "Detailed log: ${LOG_FILE}"
log_action ""
log_action "${YELLOW}Quick Stats:${NC}"
log_action "  Python files: $(find "${DEST_BASE}/python" -name "*.py" -type f 2>/dev/null | wc -l | xargs)"
log_action "  Shell scripts: $(find "${DEST_BASE}/scripts" -name "*.sh" -type f 2>/dev/null | wc -l | xargs)"
log_action "  JS/TS files: $(find "${DEST_BASE}/nodejs" \( -name "*.js" -o -name "*.ts" \) -type f 2>/dev/null | wc -l | xargs)"
log_action "  Total size: $(du -sh "${DEST_BASE}" 2>/dev/null | cut -f1)"
log_action ""
log_action "${GREEN}✓ Your CODE_MASTER is ready!${NC}"
log_action "${GREEN}✓ You can now safely reformat your system drive${NC}"
log_action ""

# Create a verification checklist
cat > "${DEST_BASE}/PRE_REFORMAT_CHECKLIST.md" << 'CHECKLIST'
# PRE-REFORMAT VERIFICATION CHECKLIST

Before reformatting your system drive, verify:

## ✓ Code Extraction
- [ ] All Python scripts backed up
- [ ] All shell scripts backed up
- [ ] All JavaScript/Node.js code backed up
- [ ] All configuration files backed up
- [ ] All Git repositories backed up
- [ ] All documentation backed up

## ✓ Critical Files
- [ ] SSH keys (~/.ssh/)
- [ ] GPG keys (~/.gnupg/)
- [ ] API keys and credentials
- [ ] Custom aliases and .zshrc/.bashrc
- [ ] Application settings
- [ ] Browser bookmarks and extensions

## ✓ Projects
- [ ] Active development projects
- [ ] Work in progress (uncommitted changes)
- [ ] Local databases
- [ ] Custom configurations

## ✓ Data
- [ ] Documents
- [ ] Downloads folder
- [ ] Desktop files
- [ ] Pictures/Media
- [ ] Any other personal data

## ✓ Applications
- [ ] List of installed applications
- [ ] License keys
- [ ] Custom plugins/extensions

## ✓ Verification
- [ ] Can access CODE_MASTER on 4TB_02
- [ ] All files readable and intact
- [ ] Total size matches expectations
- [ ] No broken symlinks

---
**Last Updated:** $(date)
CHECKLIST

log_action "${BLUE}Pre-reformat checklist created: ${DEST_BASE}/PRE_REFORMAT_CHECKLIST.md${NC}"
log_action ""
log_action "${RED}REMEMBER TO VERIFY EVERYTHING BEFORE REFORMATTING!${NC}"
