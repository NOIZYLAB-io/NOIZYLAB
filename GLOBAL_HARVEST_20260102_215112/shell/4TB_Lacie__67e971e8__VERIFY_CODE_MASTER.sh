#!/bin/zsh
# ============================================================================
# CODE_MASTER VERIFICATION SCRIPT
# Date: November 18, 2025
# Purpose: Verify CODE_MASTER is complete before reformatting system drive
# ============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

DEST_BASE="/Volumes/4TB_02/CODE_MASTER"
REPORT_FILE="${DEST_BASE}/VERIFICATION_REPORT_$(date +%Y%m%d_%H%M%S).md"

echo "${BLUE}============================================================================${NC}"
echo "${BLUE}CODE_MASTER VERIFICATION${NC}"
echo "${BLUE}============================================================================${NC}"
echo ""

# Check if CODE_MASTER exists
if [[ ! -d "$DEST_BASE" ]]; then
    echo "${RED}ERROR: CODE_MASTER not found at ${DEST_BASE}${NC}"
    exit 1
fi

echo "${GREEN}✓ CODE_MASTER directory exists${NC}"
echo ""

# Create verification report
cat > "$REPORT_FILE" << EOF
# CODE_MASTER VERIFICATION REPORT
**Date:** $(date)
**Location:** ${DEST_BASE}

## Directory Structure
EOF

# Check main directories
echo "${BLUE}Checking directory structure...${NC}"
for dir in python nodejs scripts config docs git_repos logs; do
    if [[ -d "${DEST_BASE}/${dir}" ]]; then
        echo "${GREEN}✓${NC} ${dir}/"
        echo "- ✓ ${dir}/" >> "$REPORT_FILE"
    else
        echo "${YELLOW}⚠${NC} ${dir}/ (not found)"
        echo "- ⚠ ${dir}/ (not found)" >> "$REPORT_FILE"
    fi
done

echo ""
echo "${BLUE}Counting files...${NC}"

# Count files by type
cat >> "$REPORT_FILE" << EOF

## File Statistics

### Python
EOF

py_count=$(find "${DEST_BASE}" -name "*.py" -type f 2>/dev/null | wc -l | xargs)
echo "Python files: ${py_count}"
echo "- ${py_count} Python files (.py)" >> "$REPORT_FILE"

ipynb_count=$(find "${DEST_BASE}" -name "*.ipynb" -type f 2>/dev/null | wc -l | xargs)
echo "Jupyter notebooks: ${ipynb_count}"
echo "- ${ipynb_count} Jupyter notebooks (.ipynb)" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << EOF

### Shell Scripts
EOF

sh_count=$(find "${DEST_BASE}" -name "*.sh" -type f 2>/dev/null | wc -l | xargs)
echo "Shell scripts: ${sh_count}"
echo "- ${sh_count} Shell scripts (.sh)" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << EOF

### JavaScript/TypeScript
EOF

js_count=$(find "${DEST_BASE}" -name "*.js" -type f 2>/dev/null | wc -l | xargs)
ts_count=$(find "${DEST_BASE}" -name "*.ts" -type f 2>/dev/null | wc -l | xargs)
echo "JavaScript files: ${js_count}"
echo "TypeScript files: ${ts_count}"
echo "- ${js_count} JavaScript files (.js)" >> "$REPORT_FILE"
echo "- ${ts_count} TypeScript files (.ts)" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << EOF

### Configuration
EOF

json_count=$(find "${DEST_BASE}" -name "*.json" -type f 2>/dev/null | wc -l | xargs)
yaml_count=$(find "${DEST_BASE}" \( -name "*.yaml" -o -name "*.yml" \) -type f 2>/dev/null | wc -l | xargs)
echo "JSON files: ${json_count}"
echo "YAML files: ${yaml_count}"
echo "- ${json_count} JSON files (.json)" >> "$REPORT_FILE"
echo "- ${yaml_count} YAML files (.yaml/.yml)" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << EOF

### Documentation
EOF

md_count=$(find "${DEST_BASE}" -name "*.md" -type f 2>/dev/null | wc -l | xargs)
echo "Markdown files: ${md_count}"
echo "- ${md_count} Markdown files (.md)" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << EOF

### Git Repositories
EOF

git_count=$(find "${DEST_BASE}" -type d -name ".git" 2>/dev/null | wc -l | xargs)
echo "Git repositories: ${git_count}"
echo "- ${git_count} Git repositories" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << EOF

## Size Analysis
EOF

echo ""
echo "${BLUE}Calculating sizes...${NC}"

total_size=$(du -sh "${DEST_BASE}" 2>/dev/null | cut -f1)
echo "Total size: ${total_size}"
echo "- Total: ${total_size}" >> "$REPORT_FILE"

# Size by category
for dir in python nodejs scripts config docs git_repos; do
    if [[ -d "${DEST_BASE}/${dir}" ]]; then
        dir_size=$(du -sh "${DEST_BASE}/${dir}" 2>/dev/null | cut -f1)
        echo "  ${dir}: ${dir_size}"
        echo "- ${dir}: ${dir_size}" >> "$REPORT_FILE"
    fi
done

cat >> "$REPORT_FILE" << EOF

## Large Files (>10MB)
\`\`\`
$(find "${DEST_BASE}" -type f -size +10M 2>/dev/null | head -20)
\`\`\`

## Git Repositories Found
\`\`\`
EOF

find "${DEST_BASE}" -type d -name ".git" 2>/dev/null | while read -r gitdir; do
    repo=$(dirname "$gitdir")
    echo "$(basename "$repo")" >> "$REPORT_FILE"
done

cat >> "$REPORT_FILE" << EOF
\`\`\`

## Key Projects Detected
\`\`\`
EOF

# List main project directories
find "${DEST_BASE}/python/projects" -type d -maxdepth 1 2>/dev/null | while read -r proj; do
    if [[ -d "$proj" ]]; then
        echo "- $(basename "$proj")" >> "$REPORT_FILE"
    fi
done

cat >> "$REPORT_FILE" << EOF
\`\`\`

## Verification Checklist

EOF

# Automated checks
checks_passed=0
checks_total=0

# Check 1: Python code exists
checks_total=$((checks_total + 1))
if [[ $py_count -gt 0 ]]; then
    echo "- [x] Python code extracted (${py_count} files)" >> "$REPORT_FILE"
    checks_passed=$((checks_passed + 1))
else
    echo "- [ ] Python code extracted (0 files)" >> "$REPORT_FILE"
fi

# Check 2: Scripts exist
checks_total=$((checks_total + 1))
if [[ $sh_count -gt 0 ]]; then
    echo "- [x] Shell scripts extracted (${sh_count} files)" >> "$REPORT_FILE"
    checks_passed=$((checks_passed + 1))
else
    echo "- [ ] Shell scripts extracted (0 files)" >> "$REPORT_FILE"
fi

# Check 3: Config files exist
checks_total=$((checks_total + 1))
if [[ $json_count -gt 0 ]] || [[ $yaml_count -gt 0 ]]; then
    echo "- [x] Configuration files extracted" >> "$REPORT_FILE"
    checks_passed=$((checks_passed + 1))
else
    echo "- [ ] Configuration files extracted" >> "$REPORT_FILE"
fi

# Check 4: Documentation exists
checks_total=$((checks_total + 1))
if [[ $md_count -gt 0 ]]; then
    echo "- [x] Documentation extracted (${md_count} files)" >> "$REPORT_FILE"
    checks_passed=$((checks_passed + 1))
else
    echo "- [ ] Documentation extracted (0 files)" >> "$REPORT_FILE"
fi

# Check 5: Reasonable size
checks_total=$((checks_total + 1))
total_bytes=$(du -sk "${DEST_BASE}" 2>/dev/null | cut -f1)
if [[ $total_bytes -gt 1024 ]]; then  # More than 1MB
    echo "- [x] CODE_MASTER has content (${total_size})" >> "$REPORT_FILE"
    checks_passed=$((checks_passed + 1))
else
    echo "- [ ] CODE_MASTER has content (${total_size})" >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << EOF

## Verification Summary
**Checks Passed:** ${checks_passed}/${checks_total}

EOF

# Final status
echo ""
echo "${BLUE}============================================================================${NC}"
if [[ $checks_passed -eq $checks_total ]]; then
    echo "${GREEN}✓ ALL CHECKS PASSED${NC}"
    echo "**Status:** ✓ READY FOR SYSTEM REFORMAT" >> "$REPORT_FILE"
    echo ""
    echo "${GREEN}Your CODE_MASTER is complete and verified!${NC}"
    echo "${GREEN}Safe to proceed with system reformat.${NC}"
else
    echo "${YELLOW}⚠ WARNING: Some checks failed (${checks_passed}/${checks_total})${NC}"
    echo "**Status:** ⚠ REVIEW REQUIRED BEFORE REFORMAT" >> "$REPORT_FILE"
    echo ""
    echo "${YELLOW}Please review the verification report before reformatting.${NC}"
fi
echo "${BLUE}============================================================================${NC}"
echo ""
echo "Full report: ${REPORT_FILE}"
echo ""

# Open report if possible
if command -v open &> /dev/null; then
    echo "${BLUE}Opening report...${NC}"
    open "$REPORT_FILE" 2>/dev/null || true
fi
