#!/bin/zsh
# ============================================================================
# DEEP SYSTEM-WIDE CODE SCAN
# Date: November 18, 2025
# Purpose: Find ALL code files across entire system before reformat
# ============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

SCAN_REPORT="/Volumes/4TB_02/CODE_MASTER/DEEP_SCAN_REPORT_$(date +%Y%m%d_%H%M%S).txt"
COPY_SCRIPT="/Volumes/4TB_02/CODE_MASTER/COPY_DISCOVERED_FILES.sh"

mkdir -p "$(dirname "$SCAN_REPORT")"

echo "${BLUE}============================================================================${NC}"
echo "${BLUE}DEEP SYSTEM-WIDE CODE SCAN${NC}"
echo "${BLUE}============================================================================${NC}"
echo ""
echo "Scanning all volumes and system locations..."
echo "Report: ${SCAN_REPORT}"
echo ""

# Initialize report
cat > "$SCAN_REPORT" << 'EOF'
# DEEP SYSTEM-WIDE CODE SCAN REPORT
================================================================================
Scan Date: $(date)
Purpose: Locate ALL code before system reformat

LOCATIONS SCANNED:
- /Volumes/4TBSG (primary workspace)
- /Volumes/4TB_02 (backup drive)
- /Users/M2ULTRA (home directory)
- /Users/Shared (shared user data)
- /Applications (app scripts and resources)
- /Library (system libraries)
- /opt (optional software)

================================================================================

EOF

# Function to scan and report
scan_location() {
    local location="$1"
    local description="$2"
    
    echo "${CYAN}[SCANNING]${NC} $description"
    echo "" >> "$SCAN_REPORT"
    echo "## $description" >> "$SCAN_REPORT"
    echo "Location: $location" >> "$SCAN_REPORT"
    echo "" >> "$SCAN_REPORT"
    
    if [[ ! -d "$location" && ! -f "$location" ]]; then
        echo "  ${YELLOW}Location not found, skipping${NC}"
        echo "Status: NOT FOUND" >> "$SCAN_REPORT"
        return
    fi
    
    # Python files
    echo "  ${GREEN}→${NC} Python files..."
    py_count=$(find "$location" -name "*.py" -type f 2>/dev/null | wc -l | xargs)
    echo "    Found: ${py_count} .py files"
    echo "Python files (.py): ${py_count}" >> "$SCAN_REPORT"
    if [[ $py_count -gt 0 ]]; then
        find "$location" -name "*.py" -type f 2>/dev/null | head -50 >> "$SCAN_REPORT"
        if [[ $py_count -gt 50 ]]; then
            echo "... and $((py_count - 50)) more" >> "$SCAN_REPORT"
        fi
    fi
    echo "" >> "$SCAN_REPORT"
    
    # Shell scripts
    echo "  ${GREEN}→${NC} Shell scripts..."
    sh_count=$(find "$location" -name "*.sh" -type f 2>/dev/null | wc -l | xargs)
    echo "    Found: ${sh_count} .sh files"
    echo "Shell scripts (.sh): ${sh_count}" >> "$SCAN_REPORT"
    if [[ $sh_count -gt 0 ]]; then
        find "$location" -name "*.sh" -type f 2>/dev/null | head -50 >> "$SCAN_REPORT"
        if [[ $sh_count -gt 50 ]]; then
            echo "... and $((sh_count - 50)) more" >> "$SCAN_REPORT"
        fi
    fi
    echo "" >> "$SCAN_REPORT"
    
    # JavaScript/TypeScript
    echo "  ${GREEN}→${NC} JavaScript/TypeScript..."
    js_count=$(find "$location" \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" \) -type f 2>/dev/null | wc -l | xargs)
    echo "    Found: ${js_count} JS/TS files"
    echo "JavaScript/TypeScript: ${js_count}" >> "$SCAN_REPORT"
    if [[ $js_count -gt 0 ]]; then
        find "$location" \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" \) -type f 2>/dev/null | head -30 >> "$SCAN_REPORT"
        if [[ $js_count -gt 30 ]]; then
            echo "... and $((js_count - 30)) more" >> "$SCAN_REPORT"
        fi
    fi
    echo "" >> "$SCAN_REPORT"
    
    # Git repositories
    echo "  ${GREEN}→${NC} Git repositories..."
    git_count=$(find "$location" -name ".git" -type d 2>/dev/null | wc -l | xargs)
    echo "    Found: ${git_count} Git repos"
    echo "Git repositories: ${git_count}" >> "$SCAN_REPORT"
    if [[ $git_count -gt 0 ]]; then
        find "$location" -name ".git" -type d 2>/dev/null | while read gitdir; do
            echo "$(dirname "$gitdir")" >> "$SCAN_REPORT"
        done
    fi
    echo "" >> "$SCAN_REPORT"
    
    # Configuration files
    echo "  ${GREEN}→${NC} Configuration files..."
    conf_count=$(find "$location" \( -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name ".env*" \) -type f 2>/dev/null | wc -l | xargs)
    echo "    Found: ${conf_count} config files"
    echo "Configuration files: ${conf_count}" >> "$SCAN_REPORT"
    echo "" >> "$SCAN_REPORT"
    
    # Jupyter notebooks
    echo "  ${GREEN}→${NC} Jupyter notebooks..."
    ipynb_count=$(find "$location" -name "*.ipynb" -type f 2>/dev/null | wc -l | xargs)
    echo "    Found: ${ipynb_count} notebooks"
    echo "Jupyter notebooks (.ipynb): ${ipynb_count}" >> "$SCAN_REPORT"
    if [[ $ipynb_count -gt 0 ]]; then
        find "$location" -name "*.ipynb" -type f 2>/dev/null >> "$SCAN_REPORT"
    fi
    echo "" >> "$SCAN_REPORT"
    
    # VS Code workspaces
    echo "  ${GREEN}→${NC} VS Code files..."
    vscode_count=$(find "$location" \( -name "*.code-workspace" -o -name ".vscode" \) 2>/dev/null | wc -l | xargs)
    echo "    Found: ${vscode_count} VS Code items"
    echo "VS Code workspaces/configs: ${vscode_count}" >> "$SCAN_REPORT"
    if [[ $vscode_count -gt 0 ]]; then
        find "$location" \( -name "*.code-workspace" -o -name ".vscode" \) 2>/dev/null >> "$SCAN_REPORT"
    fi
    echo "" >> "$SCAN_REPORT"
    
    # Executable scripts (no extension)
    echo "  ${GREEN}→${NC} Executable scripts..."
    exec_count=$(find "$location" -type f -perm +111 2>/dev/null | head -100 | file - | grep -i "script\|text" | wc -l | xargs)
    echo "    Found: ~${exec_count} executable scripts"
    echo "Executable scripts (sample): ${exec_count}" >> "$SCAN_REPORT"
    echo "" >> "$SCAN_REPORT"
    
    echo "  ${GREEN}✓${NC} Scan complete"
    echo "================================" >> "$SCAN_REPORT"
}

# ============================================================================
# SCAN ALL LOCATIONS
# ============================================================================

echo "${MAGENTA}[1/10]${NC} Scanning 4TBSG Extensions..."
scan_location "/Volumes/4TBSG/Extensions" "4TBSG - Extensions Directory"

echo ""
echo "${MAGENTA}[2/10]${NC} Scanning 4TBSG KTK folder..."
scan_location "/Volumes/4TBSG/KTK 2026 TO SORT" "4TBSG - KTK 2026 TO SORT"

echo ""
echo "${MAGENTA}[3/10]${NC} Scanning 4TBSG Projects..."
scan_location "/Volumes/4TBSG/Projects" "4TBSG - Projects"

echo ""
echo "${MAGENTA}[4/10]${NC} Scanning 4TB_02 CODE_MASTER..."
scan_location "/Volumes/4TB_02/CODE_MASTER" "4TB_02 - CODE_MASTER (backup location)"

echo ""
echo "${MAGENTA}[5/10]${NC} Scanning Home Directory..."
scan_location "/Users/M2ULTRA" "User Home Directory"

echo ""
echo "${MAGENTA}[6/10]${NC} Scanning Shared Directory..."
scan_location "/Users/Shared" "Shared User Directory"

echo ""
echo "${MAGENTA}[7/10]${NC} Scanning Desktop..."
scan_location "/Users/M2ULTRA/Desktop" "Desktop"

echo ""
echo "${MAGENTA}[8/10]${NC} Scanning Documents..."
scan_location "/Users/M2ULTRA/Documents" "Documents"

echo ""
echo "${MAGENTA}[9/10]${NC} Scanning Downloads..."
scan_location "/Users/M2ULTRA/Downloads" "Downloads"

echo ""
echo "${MAGENTA}[10/10]${NC} Scanning /opt..."
scan_location "/opt" "Optional Software (/opt)"

# ============================================================================
# SPECIAL SCANS
# ============================================================================

echo ""
echo "${CYAN}[SPECIAL]${NC} Looking for hidden dev directories..."
echo "" >> "$SCAN_REPORT"
echo "## SPECIAL: Hidden Development Directories" >> "$SCAN_REPORT"
echo "" >> "$SCAN_REPORT"

# Common hidden dev directories
for hidden_dir in .npm .nvm .pyenv .rbenv .cargo .rustup .local .config; do
    if [[ -d "/Users/M2ULTRA/${hidden_dir}" ]]; then
        echo "  ${YELLOW}Found:${NC} ~/${hidden_dir}"
        echo "~/${hidden_dir}" >> "$SCAN_REPORT"
        du -sh "/Users/M2ULTRA/${hidden_dir}" 2>/dev/null >> "$SCAN_REPORT"
    fi
done

echo ""
echo "${CYAN}[SPECIAL]${NC} Looking for .zshrc, .bashrc, .profile..."
echo "" >> "$SCAN_REPORT"
echo "## Shell Configuration Files" >> "$SCAN_REPORT"
echo "" >> "$SCAN_REPORT"

for config in .zshrc .bashrc .bash_profile .profile .zprofile .zshenv; do
    if [[ -f "/Users/M2ULTRA/${config}" ]]; then
        echo "  ${GREEN}✓${NC} ~/${config}"
        echo "~/${config}" >> "$SCAN_REPORT"
    fi
done

echo ""
echo "${CYAN}[SPECIAL]${NC} Looking for SSH keys..."
if [[ -d "/Users/M2ULTRA/.ssh" ]]; then
    echo "  ${RED}CRITICAL:${NC} SSH keys found at ~/.ssh"
    echo "" >> "$SCAN_REPORT"
    echo "## CRITICAL: SSH Keys Found" >> "$SCAN_REPORT"
    ls -la "/Users/M2ULTRA/.ssh" >> "$SCAN_REPORT"
else
    echo "  ${GREEN}✓${NC} No ~/.ssh directory"
fi

echo ""
echo "${CYAN}[SPECIAL]${NC} Looking for GPG keys..."
if [[ -d "/Users/M2ULTRA/.gnupg" ]]; then
    echo "  ${RED}CRITICAL:${NC} GPG keys found at ~/.gnupg"
    echo "" >> "$SCAN_REPORT"
    echo "## CRITICAL: GPG Keys Found" >> "$SCAN_REPORT"
    ls -la "/Users/M2ULTRA/.gnupg" >> "$SCAN_REPORT"
else
    echo "  ${GREEN}✓${NC} No ~/.gnupg directory"
fi

echo ""
echo "${CYAN}[SPECIAL]${NC} Looking for git config..."
if [[ -f "/Users/M2ULTRA/.gitconfig" ]]; then
    echo "  ${YELLOW}Found:${NC} ~/.gitconfig"
    echo "" >> "$SCAN_REPORT"
    echo "## Git Configuration" >> "$SCAN_REPORT"
    cat "/Users/M2ULTRA/.gitconfig" >> "$SCAN_REPORT"
fi

# ============================================================================
# GENERATE SUMMARY
# ============================================================================

echo ""
echo "${BLUE}============================================================================${NC}"
echo "${BLUE}GENERATING SUMMARY${NC}"
echo "${BLUE}============================================================================${NC}"

cat >> "$SCAN_REPORT" << 'SUMMARY_EOF'

================================================================================
OVERALL SUMMARY
================================================================================

SUMMARY_EOF

# Count totals across all locations
total_py=$(grep -c "\.py$" "$SCAN_REPORT" 2>/dev/null || echo "0")
total_sh=$(grep -c "\.sh$" "$SCAN_REPORT" 2>/dev/null || echo "0")
total_js=$(grep -c "\.js$\|\.ts$" "$SCAN_REPORT" 2>/dev/null || echo "0")

cat >> "$SCAN_REPORT" << SUMMARY_CONTENT

Total Files Found (approximate):
- Python files: ${total_py}+
- Shell scripts: ${total_sh}+
- JavaScript/TypeScript: ${total_js}+

CRITICAL ITEMS TO BACKUP MANUALLY:
- SSH keys (~/.ssh/)
- GPG keys (~/.gnupg/)
- Shell configurations (.zshrc, .bashrc, etc.)
- Git global config (~/.gitconfig)

NEXT STEPS:
1. Review this report carefully
2. Run EXTRACT_ALL_CODE_TO_CODE_MASTER.sh to copy code
3. Manually backup critical items listed above
4. Run VERIFY_CODE_MASTER.sh
5. Double-check everything before reformatting

================================================================================
SCAN COMPLETE - $(date)
================================================================================

SUMMARY_CONTENT

echo ""
echo "${GREEN}✓ Deep scan complete!${NC}"
echo ""
echo "${YELLOW}Report saved to:${NC}"
echo "  ${SCAN_REPORT}"
echo ""
echo "${YELLOW}Key findings:${NC}"
grep -E "Python files|Shell scripts|JavaScript|Git repositories" "$SCAN_REPORT" | head -20
echo ""
echo "${RED}⚠ CRITICAL: Review report for SSH keys, GPG keys, and configs!${NC}"
echo ""

# Create quick copy script
cat > "$COPY_SCRIPT" << 'COPY_EOF'
#!/bin/zsh
# Quick copy script for discovered files
# Generated by DEEP_SCAN_ALL_CODE.sh

DEST="/Volumes/4TB_02/CODE_MASTER"

echo "Copying critical configurations..."

# SSH keys (CRITICAL)
if [[ -d ~/.ssh ]]; then
    mkdir -p "$DEST/critical_backups/ssh"
    cp -R ~/.ssh/* "$DEST/critical_backups/ssh/" 2>/dev/null
    echo "✓ SSH keys backed up"
fi

# GPG keys (CRITICAL)
if [[ -d ~/.gnupg ]]; then
    mkdir -p "$DEST/critical_backups/gnupg"
    cp -R ~/.gnupg/* "$DEST/critical_backups/gnupg/" 2>/dev/null
    echo "✓ GPG keys backed up"
fi

# Shell configs
mkdir -p "$DEST/critical_backups/shell_configs"
for config in .zshrc .bashrc .bash_profile .profile .zprofile .zshenv .gitconfig; do
    if [[ -f ~/$config ]]; then
        cp ~/$config "$DEST/critical_backups/shell_configs/" 2>/dev/null
        echo "✓ Copied $config"
    fi
done

echo ""
echo "✓ Critical backups complete!"

COPY_EOF

chmod +x "$COPY_SCRIPT"

echo "${CYAN}Quick backup script created:${NC}"
echo "  ${COPY_SCRIPT}"
echo ""
echo "${YELLOW}Run it with:${NC}"
echo "  $COPY_SCRIPT"
echo ""
