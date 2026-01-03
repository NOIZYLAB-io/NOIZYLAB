# GABRIEL Codebase Cleanup Plan

## Current State Analysis

### Active Code (Keep)
| Directory | Lines | Purpose |
|-----------|-------|---------|
| `noizylab-os/workers/` | 50,636 | 67 specialized AI workers |
| `src/workers/noizylab` | 3,955 | Original unified worker |
| `src/workers/noizylab-v1` | 1,984 | Simplified v1 refactor |
| `ANTIGRAVITY_COMPLETE/` | 5,569 | 10 creative workers |
| `scripts/` | 5,582 | Shell utilities |
| `mcp_servers/` | 848 | MCP tools (turbo.py, etc) |
| `portal/` | ~600 | Landing + frontend |

### Bloat Identified (Archive Externally)
| Directory | Size | Contents |
|-----------|------|----------|
| `CODEMASTER/_ORGANIZED/07_LEGACY/noizylab_workspaces/` | 34GB | Old workspaces |
| `CODEMASTER/gemini_config/antigravity/` | 37GB | Browser profile |
| `CODEMASTER/_ORGANIZED/07_LEGACY/claude_needs/` | 7.6GB | Legacy claude data |
| `CODEMASTER/_ORGANIZED/06_CONFIG/ai_tools/` | 6.8GB | IDE caches (.cursor, .codeium, etc) |
| `CODEMASTER/gemini_config/antigravity-browser-profile/` | 6.3GB | Browser profile |
| `CODEMASTER/_ORGANIZED/07_LEGACY/6tb_archive/` | 5GB | Old archive |

**Total bloat: ~100GB**

## Cleanup Actions

### Phase 1: External Archive (100GB → External Drive)
```bash
# Move CODEMASTER to external storage
mv CODEMASTER /Volumes/ARCHIVE/GABRIEL_CODEMASTER_BACKUP_$(date +%Y%m%d)
```

### Phase 2: Clean Up Archive Folder
The `archive/` folder has proper archived content:
- `CODE_LEGACY/` - Legacy agents
- `duplicate_agents/` - Duplicate cleanup
- `workers-legacy/` - Old workers
- Keep this - it's only 75MB

### Phase 3: Directory Structure

```
GABRIEL/
├── src/
│   └── workers/
│       ├── noizylab/       # Full-featured API
│       └── noizylab-v1/    # Simplified v1
├── noizylab-os/
│   └── workers/            # 67 specialized workers
├── ANTIGRAVITY_COMPLETE/   # 10 creative workers
├── portal/
│   ├── api/                # Backend API
│   ├── frontend/           # React app
│   └── landing/            # Marketing site
├── mcp_servers/
│   └── gabriel_mcp/        # MCP tools (turbo.py)
├── scripts/                # Shell utilities
├── docs/                   # Documentation
├── config/                 # Configuration
├── archive/                # Legacy code (75MB)
└── tools/                  # Dev tools

# REMOVE FROM REPO:
- CODEMASTER/               # 115GB IDE caches → External
- titanhive/                # Has .venv → Clean or archive
- SystemGuardian/           # Duplicate in projects/
- widget/                   # macOS app bundle
- node_modules/             # Root level (regenerate)
- __pycache__/              # Python cache
- .mypy_cache/              # Type checking cache
```

### Phase 4: Consolidate Duplicate Projects
- `SystemGuardian/` appears in root AND `projects/SystemGuardian/`
- Decide which is canonical and archive the other

### Phase 5: Git Cleanup
```bash
# After moving CODEMASTER externally
git rm -r --cached CODEMASTER/
echo "CODEMASTER/" >> .gitignore

# Clean caches
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null
find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null

# Re-add to gitignore
cat >> .gitignore << 'EOF'
# Caches
__pycache__/
.mypy_cache/
node_modules/
*.pyc
.DS_Store

# IDE configs (already in repos)
CODEMASTER/

# Build artifacts
dist/
build/
.wrangler/
EOF
```

## Recommended Final Structure

After cleanup, repo should be ~200MB instead of 120GB:

```
GABRIEL/ (~200MB active code)
├── src/workers/           # Core workers
├── noizylab-os/workers/   # 67 specialized workers
├── ANTIGRAVITY_COMPLETE/  # Creative workers
├── portal/                # Web apps
├── mcp_servers/           # MCP tools
├── scripts/               # Utilities
├── docs/                  # Documentation
├── config/                # Config files
├── archive/               # Legacy (compressed)
└── tools/                 # Dev tools
```

## Execute Commands

```bash
# 1. Backup CODEMASTER to external drive
tar -cvzf /Volumes/ARCHIVE/GABRIEL_CODEMASTER_$(date +%Y%m%d).tar.gz CODEMASTER/

# 2. Remove from git tracking
git rm -r --cached CODEMASTER/

# 3. Delete local CODEMASTER (after confirming backup)
rm -rf CODEMASTER/

# 4. Update .gitignore
echo "CODEMASTER/" >> .gitignore

# 5. Clean caches
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find . -name ".mypy_cache" -type d -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete 2>/dev/null
find . -name ".DS_Store" -delete 2>/dev/null

# 6. Commit cleanup
git add .
git commit -m "chore: clean 115GB IDE caches, reorganize structure"
```
