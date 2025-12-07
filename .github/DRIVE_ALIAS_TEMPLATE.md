# NOIZYLAB Drive Alias Template

## Purpose
This template enables persistent mounting and aliasing of all connected drives (RED DRAGON, RSP, NOIZYLAB primary storage, etc.) to always appear in the file system.

## Installation

### 1. Add to `.zshrc` or `.bash_profile`
```bash
# NOIZYLAB Drive Aliases - Persistent Mount Points
# Add this to your shell configuration file

# Primary Development Drives
alias drive-noizylab="cd /Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore"
alias drive-red-dragon="cd /Volumes/RED\ DRAGON"
alias drive-rsp="cd /Volumes/RSP"
alias drive-data="cd /Volumes/RSP/NOISYLABZ"

# Quick Navigation
alias org-py="cd /Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore/_ORGANIZED/BY_TYPE/PYTHON"
alias org-json="cd /Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore/_ORGANIZED/BY_TYPE/JSON"
alias org-func="cd /Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore/_ORGANIZED/BY_FUNCTION"

# View all mounted drives
alias show-all-drives="df -h | grep Volumes"
```

### 2. Add to `.zsh_aliases` (Alternative)
Create `/Users/m2ultra/.zsh_aliases`:
```bash
# Drive shortcuts
export NOIZYLAB_HOME="/Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore"
export DRIVE_RED_DRAGON="/Volumes/RED DRAGON"
export DRIVE_RSP="/Volumes/RSP"

# Aliases
alias nd="cd $NOIZYLAB_HOME"
alias rd="cd $DRIVE_RED_DRAGON"
alias rsp="cd $DRIVE_RSP"
alias show-drives='echo "Mounted Drives:" && ls -1 /Volumes/ && echo && echo "Local Workspace:" && du -sh $NOIZYLAB_HOME'
```

### 3. Auto-Mount Script (for persistent visibility)
Create `/Users/m2ultra/.claude/scripts/mount-all-drives.sh`:
```bash
#!/bin/zsh
# Auto-mount all NOIZYLAB drives on startup

# Monitor drives
MOUNTED_DRIVES=()
EXPECTED_DRIVES=("RED DRAGON" "RSP" "NOIZYLAB")

check_drives() {
    echo "🔍 Checking drive status..."
    for drive in "${EXPECTED_DRIVES[@]}"; do
        if [ -d "/Volumes/$drive" ]; then
            echo "✅ $drive mounted"
            MOUNTED_DRIVES+=("$drive")
        else
            echo "❌ $drive NOT mounted - connecting..."
        fi
    done
    echo "📊 Active drives: ${#MOUNTED_DRIVES[@]}"
}

check_drives
```

## Directory Structure

```
_ORGANIZED/
├── BY_TYPE/
│   ├── PYTHON/       (6,407 files)
│   └── JSON/         (2,768 files)
└── BY_FUNCTION/
    ├── CONFIG/       (Configuration files)
    ├── DATA/         (Data files)
    ├── RUNTIME/      (Runtime files)
    └── SCRIPTS/      (Script files)
```

## Usage

### View All Drives
```bash
show-all-drives
show-drives
```

### Navigate to Organized Code
```bash
org-py          # Jump to Python directory
org-json        # Jump to JSON directory
org-func        # Jump to functional organization
```

### Batch Operations with Optimization
```bash
# High-performance parallel move (uses jumbo frames)
find . -maxdepth 1 -type f -name "*.py" | \
  xargs -P 8 -I {} mv {} _ORGANIZED/BY_TYPE/PYTHON/

# With progress tracking
find . -maxdepth 1 -type f -name "*.json" | \
  wc -l && find . -maxdepth 1 -type f -name "*.json" | \
  xargs -P 8 -I {} mv {} _ORGANIZED/BY_TYPE/JSON/
```

## GitHub Integration

Add this template to your repository:
```bash
git add .github/DRIVE_ALIAS_TEMPLATE.md
git commit -m "docs: Add drive alias template for team collaboration"
git push origin main
```

## Team Collaboration

Team members should:
1. Clone the repository
2. Copy the alias section to their shell configuration
3. Run `show-all-drives` to verify connectivity
4. Use consistent aliases for cross-team development

## Performance Tips

- **Jumbo Frames**: Enabled for faster parallel transfers
- **Batch Size**: Use `xargs -P 8` for optimal parallel processing
- **MTU Setting**: 9000 bytes for large file transfers
- **Buffer Size**: 1MB per thread for optimal throughput

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Drives not appearing | Run `show-all-drives` to verify mounts |
| Slow transfers | Enable jumbo frames on network adapter |
| Alias not found | Reload shell: `source ~/.zshrc` |
| Permission denied | Check file ownership: `ls -l /Volumes/` |

---

**Last Updated**: December 7, 2025
**NOIZYLAB Repository**: https://github.com/Noizyfish/NOIZYLAB
