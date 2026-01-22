---
description: NOIZYLAB
auto_execution_mode: 1
---

## Goal
NOIZYLAB workspace ready: rules active, agents loaded, storage split configured.

## Steps
1. Open workspace: `$NOIZYLAB_HOME/AG_HOME.code-workspace` (set NOIZYLAB_HOME env var first)
2. Confirm `.windsurfrules` active (GORUNFREE protocol)
3. Sanity checks:
// turbo
   - `git status`
   - `python3 --version`
   - `./AGENTS/launch.sh list`

## Environment Setup
```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export NOIZYLAB_HOME="$HOME/NOIZYLAB"
export NOIZYLAB_GDRIVE="$HOME/Library/CloudStorage/GoogleDrive-YOUR_EMAIL/My Drive/NOIZYLAB_MEDIA"
```

## Storage
- **Code** → GitHub: `NOIZYLAB-io/NOIZYLAB`
- **Media** → Google Drive: `NOIZYLAB_MEDIA/`

## Agents
- `./AGENTS/launch.sh gabriel` - Voice + Control
- `./AGENTS/launch.sh mc96` - Core Engine
- `./AGENTS/sync-media.sh push` - Media → Google Drive
