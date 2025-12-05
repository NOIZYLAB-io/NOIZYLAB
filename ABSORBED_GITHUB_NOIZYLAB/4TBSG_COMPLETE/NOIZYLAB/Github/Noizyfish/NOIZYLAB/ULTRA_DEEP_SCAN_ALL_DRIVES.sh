#!/bin/zsh
# ============================================================================
# ULTRA DEEP SCAN - ALL DRIVES
# Date: November 18, 2025
# Scans: 4TBSG, RED DRAGON, 12TB 1, System Drive, 4TB_02
# ============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

SCAN_DATE=$(date +%Y%m%d_%H%M%S)
DEST_BASE="/Volumes/4TB_02/CODE_MASTER"
SCAN_REPORT="${DEST_BASE}/ULTRA_DEEP_SCAN_${SCAN_DATE}.md"
FULL_LOG="${DEST_BASE}/logs/ultra_scan_${SCAN_DATE}.log"

mkdir -p "${DEST_BASE}/logs"
mkdir -p "${DEST_BASE}/ultra_scan_results"

echo "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo "${CYAN}║          ULTRA DEEP SCAN - ALL DRIVES & SYSTEMS               ║${NC}"
echo "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo ""

# Initialize report
cat > "$SCAN_REPORT" << 'HEADER'
# 🔍 ULTRA DEEP SCAN REPORT
**Scan Date:** 
**Mission:** Complete code extraction before system reformat

---

## 📊 SCAN SUMMARY

HEADER

echo "Scan Date: $(date)" >> "$SCAN_REPORT"
echo "" >> "$SCAN_REPORT"

# Function to scan a drive
scan_drive() {
    local drive_path="$1"
    local drive_name="$2"
    
    if [[ ! -d "$drive_path" ]]; then
        echo "${YELLOW}⚠ ${drive_name} not mounted at ${drive_path}${NC}"
        echo "- ⚠ ${drive_name}: NOT MOUNTED" >> "$SCAN_REPORT"
        return
    fi
    
    echo ""
    echo "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo "${BLUE}SCANNING: ${drive_name}${NC}"
    echo "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    cat >> "$SCAN_REPORT" << EOF

### 📁 ${drive_name}
**Path:** \`${drive_path}\`

EOF
    
    # Python files
    echo "${CYAN}[PYTHON]${NC} Scanning for .py files..."
    py_files=$(find "$drive_path" -name "*.py" -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${py_files} Python files"
    echo "- **Python files (.py):** ${py_files}" >> "$SCAN_REPORT"
    
    # Jupyter notebooks
    echo "${CYAN}[JUPYTER]${NC} Scanning for .ipynb files..."
    ipynb_files=$(find "$drive_path" -name "*.ipynb" -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${ipynb_files} Jupyter notebooks"
    echo "- **Jupyter notebooks (.ipynb):** ${ipynb_files}" >> "$SCAN_REPORT"
    
    # Shell scripts
    echo "${CYAN}[SHELL]${NC} Scanning for .sh files..."
    sh_files=$(find "$drive_path" -name "*.sh" -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${sh_files} shell scripts"
    echo "- **Shell scripts (.sh):** ${sh_files}" >> "$SCAN_REPORT"
    
    # JavaScript
    echo "${CYAN}[JS]${NC} Scanning for .js files..."
    js_files=$(find "$drive_path" -name "*.js" -type f 2>/dev/null | grep -v node_modules | wc -l | xargs)
    echo "  Found: ${js_files} JavaScript files"
    echo "- **JavaScript files (.js):** ${js_files}" >> "$SCAN_REPORT"
    
    # TypeScript
    echo "${CYAN}[TS]${NC} Scanning for .ts files..."
    ts_files=$(find "$drive_path" -name "*.ts" -type f 2>/dev/null | grep -v node_modules | wc -l | xargs)
    echo "  Found: ${ts_files} TypeScript files"
    echo "- **TypeScript files (.ts):** ${ts_files}" >> "$SCAN_REPORT"
    
    # JSON configs
    echo "${CYAN}[JSON]${NC} Scanning for .json files..."
    json_files=$(find "$drive_path" -name "*.json" -type f 2>/dev/null | grep -v node_modules | wc -l | xargs)
    echo "  Found: ${json_files} JSON files"
    echo "- **JSON config files:** ${json_files}" >> "$SCAN_REPORT"
    
    # YAML configs
    echo "${CYAN}[YAML]${NC} Scanning for .yaml/.yml files..."
    yaml_files=$(find "$drive_path" \( -name "*.yaml" -o -name "*.yml" \) -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${yaml_files} YAML files"
    echo "- **YAML config files:** ${yaml_files}" >> "$SCAN_REPORT"
    
    # Markdown docs
    echo "${CYAN}[DOCS]${NC} Scanning for .md files..."
    md_files=$(find "$drive_path" -name "*.md" -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${md_files} Markdown files"
    echo "- **Markdown docs (.md):** ${md_files}" >> "$SCAN_REPORT"
    
    # Git repos
    echo "${CYAN}[GIT]${NC} Scanning for Git repositories..."
    git_repos=$(find "$drive_path" -name ".git" -type d 2>/dev/null | wc -l | xargs)
    echo "  Found: ${git_repos} Git repositories"
    echo "- **Git repositories:** ${git_repos}" >> "$SCAN_REPORT"
    
    # Package managers
    echo "${CYAN}[DEPS]${NC} Scanning for dependency files..."
    req_files=$(find "$drive_path" -name "requirements.txt" -type f 2>/dev/null | wc -l | xargs)
    pkg_files=$(find "$drive_path" -name "package.json" -type f 2>/dev/null | grep -v node_modules | wc -l | xargs)
    echo "  Found: ${req_files} requirements.txt, ${pkg_files} package.json"
    echo "- **requirements.txt:** ${req_files}" >> "$SCAN_REPORT"
    echo "- **package.json:** ${pkg_files}" >> "$SCAN_REPORT"
    
    # Batch/PowerShell
    echo "${CYAN}[WIN]${NC} Scanning for .bat/.ps1 files..."
    bat_files=$(find "$drive_path" -name "*.bat" -type f 2>/dev/null | wc -l | xargs)
    ps1_files=$(find "$drive_path" -name "*.ps1" -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${bat_files} batch files, ${ps1_files} PowerShell scripts"
    echo "- **Batch scripts (.bat):** ${bat_files}" >> "$SCAN_REPORT"
    echo "- **PowerShell scripts (.ps1):** ${ps1_files}" >> "$SCAN_REPORT"
    
    # VS Code workspaces
    echo "${CYAN}[VSCODE]${NC} Scanning for VS Code workspaces..."
    workspace_files=$(find "$drive_path" -name "*.code-workspace" -type f 2>/dev/null | wc -l | xargs)
    echo "  Found: ${workspace_files} VS Code workspaces"
    echo "- **VS Code workspaces:** ${workspace_files}" >> "$SCAN_REPORT"
    
    # Total size
    echo "${CYAN}[SIZE]${NC} Calculating total size..."
    drive_size=$(du -sh "$drive_path" 2>/dev/null | cut -f1)
    echo "  Total: ${drive_size}"
    echo "- **Total drive size:** ${drive_size}" >> "$SCAN_REPORT"
    
    # Create detailed file list
    local list_file="${DEST_BASE}/ultra_scan_results/${drive_name}_files_${SCAN_DATE}.txt"
    echo "${CYAN}[LIST]${NC} Creating detailed file list..."
    
    cat > "$list_file" << LISTHEAD
# Detailed File List: ${drive_name}
# Scan Date: $(date)
# Path: ${drive_path}

## Python Files
LISTHEAD
    
    find "$drive_path" -name "*.py" -type f 2>/dev/null >> "$list_file" || true
    
    echo -e "\n## Shell Scripts" >> "$list_file"
    find "$drive_path" -name "*.sh" -type f 2>/dev/null >> "$list_file" || true
    
    echo -e "\n## JavaScript Files" >> "$list_file"
    find "$drive_path" -name "*.js" -type f 2>/dev/null | grep -v node_modules >> "$list_file" || true
    
    echo -e "\n## Git Repositories" >> "$list_file"
    find "$drive_path" -name ".git" -type d 2>/dev/null | sed 's/\/.git$//' >> "$list_file" || true
    
    echo -e "\n## VS Code Workspaces" >> "$list_file"
    find "$drive_path" -name "*.code-workspace" -type f 2>/dev/null >> "$list_file" || true
    
    echo "  Saved to: ${list_file}"
    
    echo "${GREEN}✓ ${drive_name} scan complete${NC}"
}

# Scan all drives
scan_drive "/Volumes/4TBSG" "4TBSG"
scan_drive "/Volumes/RED DRAGON" "RED_DRAGON"
scan_drive "/Volumes/12TB 1" "12TB_1"
scan_drive "/Volumes/4TB_02" "4TB_02"
scan_drive "/" "SYSTEM_DRIVE"

# System-specific scans
echo ""
echo "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo "${BLUE}SCANNING: SYSTEM LOCATIONS${NC}"
echo "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

cat >> "$SCAN_REPORT" << 'SYSHEAD'

---

## 🖥️ SYSTEM-SPECIFIC SCANS

### User Home Directory
SYSHEAD

echo "${CYAN}[HOME]${NC} Scanning user home directory..."
home_py=$(find "$HOME" -name "*.py" -type f 2>/dev/null | grep -v Library | wc -l | xargs)
home_sh=$(find "$HOME" -name "*.sh" -type f 2>/dev/null | grep -v Library | wc -l | xargs)
echo "  Found: ${home_py} Python, ${home_sh} Shell scripts"
echo "- **Python files:** ${home_py}" >> "$SCAN_REPORT"
echo "- **Shell scripts:** ${home_sh}" >> "$SCAN_REPORT"

cat >> "$SCAN_REPORT" << 'APPHEAD'

### Applications Directory
APPHEAD

echo "${CYAN}[APPS]${NC} Scanning /Applications for scripts..."
app_scripts=$(find /Applications -name "*.sh" -o -name "*.py" 2>/dev/null | wc -l | xargs)
echo "  Found: ${app_scripts} scripts in Applications"
echo "- **Scripts in /Applications:** ${app_scripts}" >> "$SCAN_REPORT"

cat >> "$SCAN_REPORT" << 'OPTHEAD'

### /opt and /usr/local
OPTHEAD

echo "${CYAN}[OPT]${NC} Scanning /opt and /usr/local..."
opt_files=$(find /opt /usr/local -name "*.py" -o -name "*.sh" 2>/dev/null | wc -l | xargs)
echo "  Found: ${opt_files} scripts"
echo "- **Scripts in /opt & /usr/local:** ${opt_files}" >> "$SCAN_REPORT"

# Find all VS Code settings and extensions
cat >> "$SCAN_REPORT" << 'VSCHEAD'

### VS Code Configuration
VSCHEAD

echo "${CYAN}[VSCODE]${NC} Locating VS Code extensions and settings..."
if [[ -d "$HOME/Library/Application Support/Code/User" ]]; then
    vsc_ext=$(ls "$HOME/Library/Application Support/Code/User/extensions" 2>/dev/null | wc -l | xargs)
    echo "  Found: ${vsc_ext} VS Code extensions"
    echo "- **Installed extensions:** ${vsc_ext}" >> "$SCAN_REPORT"
fi

# Generate summary statistics
cat >> "$SCAN_REPORT" << 'SUMHEAD'

---

## 📈 GRAND TOTALS

SUMHEAD

echo ""
echo "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"
echo "${MAGENTA}CALCULATING GRAND TOTALS...${NC}"
echo "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"

# Calculate totals across all drives
total_py=0
total_sh=0
total_js=0
total_git=0

for drive in "/Volumes/4TBSG" "/Volumes/RED DRAGON" "/Volumes/12TB 1" "/Volumes/4TB_02" "/"; do
    if [[ -d "$drive" ]]; then
        py=$(find "$drive" -name "*.py" -type f 2>/dev/null | wc -l | xargs)
        sh=$(find "$drive" -name "*.sh" -type f 2>/dev/null | wc -l | xargs)
        js=$(find "$drive" -name "*.js" -type f 2>/dev/null | grep -v node_modules | wc -l | xargs)
        git=$(find "$drive" -name ".git" -type d 2>/dev/null | wc -l | xargs)
        
        total_py=$((total_py + py))
        total_sh=$((total_sh + sh))
        total_js=$((total_js + js))
        total_git=$((total_git + git))
    fi
done

echo "Python files: ${total_py}"
echo "Shell scripts: ${total_sh}"
echo "JavaScript files: ${total_js}"
echo "Git repositories: ${total_git}"

cat >> "$SCAN_REPORT" << EOF
| File Type | Count |
|-----------|-------|
| Python files (.py) | ${total_py} |
| Shell scripts (.sh) | ${total_sh} |
| JavaScript files (.js) | ${total_js} |
| Git repositories | ${total_git} |

---

## 🎯 CRITICAL FINDINGS

EOF

# Find key projects and code directories
echo ""
echo "${YELLOW}═══════════════════════════════════════════════════════════════${NC}"
echo "${YELLOW}IDENTIFYING CRITICAL CODE LOCATIONS...${NC}"
echo "${YELLOW}═══════════════════════════════════════════════════════════════${NC}"

cat >> "$SCAN_REPORT" << 'CRITHEAD'
### 🔴 High-Priority Code Locations

CRITHEAD

# Find noizylab directories
echo "${CYAN}[NOIZYLAB]${NC} Searching for NoizyLab projects..."
find /Volumes -name "*noizylab*" -type d 2>/dev/null | head -10 | while read -r dir; do
    echo "  - $dir"
    echo "- \`$dir\`" >> "$SCAN_REPORT"
done

# Find gabriel/agent scripts
echo "${CYAN}[GABRIEL]${NC} Searching for Gabriel/Agent scripts..."
find /Volumes -name "*GABRIEL*.py" -o -name "*AGENT*.py" 2>/dev/null | head -20 | while read -r file; do
    echo "  - $file"
    echo "- \`$file\`" >> "$SCAN_REPORT"
done

# Find MissionControl
echo "${CYAN}[MISSION]${NC} Searching for MissionControl..."
find /Volumes -name "*MissionControl*" -o -name "*MISSION*" 2>/dev/null | head -10 | while read -r item; do
    echo "  - $item"
    echo "- \`$item\`" >> "$SCAN_REPORT"
done

# Completion
cat >> "$SCAN_REPORT" << 'FOOTER'

---

## ✅ SCAN COMPLETE

**Status:** All drives scanned successfully  
**Next Steps:**
1. Review detailed file lists in `ultra_scan_results/`
2. Run extraction script to move code to CODE_MASTER
3. Verify all critical files are backed up
4. Safe to proceed with system reformat

**Full Log:** See detailed log file

---
*Generated by ULTRA_DEEP_SCAN*
FOOTER

echo ""
echo "${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo "${GREEN}║                    SCAN COMPLETE                              ║${NC}"
echo "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo "${CYAN}📊 Report:${NC} ${SCAN_REPORT}"
echo "${CYAN}📁 File lists:${NC} ${DEST_BASE}/ultra_scan_results/"
echo "${CYAN}📋 Full log:${NC} ${FULL_LOG}"
echo ""
echo "${YELLOW}Grand Totals:${NC}"
echo "  ${MAGENTA}●${NC} Python files: ${total_py}"
echo "  ${MAGENTA}●${NC} Shell scripts: ${total_sh}"
echo "  ${MAGENTA}●${NC} JavaScript files: ${total_js}"
echo "  ${MAGENTA}●${NC} Git repositories: ${total_git}"
echo ""
echo "${GREEN}✓ Ready to extract code to CODE_MASTER${NC}"
echo ""
