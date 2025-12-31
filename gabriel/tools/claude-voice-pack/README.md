# M2G Claude Voice Pack

Cross-platform voice wrapper for Claude CLI tools. Speaks status: **start → done** (or **error**).

## Quick Install

### macOS
```bash
bash install-macos.sh
```

### Windows
```powershell
powershell -ExecutionPolicy Bypass -File install-windows.ps1
```
(Open a **new terminal** after install)

---

## Commands

| Command | Description |
|---------|-------------|
| `m2g-say "text"` | Speak text using OS voice |
| `claudev "prompt"` | Run Claude CLI with voice status |
| `m2g-ask "question"` | Quick Claude question (or use clipboard) |

---

## Usage Examples

```bash
# Basic Claude query with voice
claudev "Explain recursion in one sentence"

# Use clipboard content as prompt
m2g-ask

# Disable voice for this command
SAY=0 claudev "silent mode"

# Force specific Claude CLI
CLAUDE_BIN=m2g-claude claudev "use my custom cli"

# Just speak something
m2g-say "Build complete"
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SAY` | `1` | Set to `0` to disable voice |
| `CLAUDE_BIN` | auto | Force specific CLI: `m2g-claude`, `claude`, `claude-code` |

---

## CLI Auto-Detection

`claudev` automatically finds your Claude CLI in this order:
1. `m2g-claude` (custom M2G CLI)
2. `claude` (official Anthropic CLI)
3. `claude-code` (VS Code extension CLI)

Override with `CLAUDE_BIN=your-cli`.

---

## Voice Selection

### macOS
Uses `say` command. Prefers high-quality voices:
- Samantha (Enhanced)
- Alex (Enhanced)
- Jamie (Enhanced)
- Falls back to system default

### Windows
Uses System.Speech (SAPI). Prefers:
- Microsoft David Desktop
- Microsoft Zira Desktop
- Falls back to system default

---

## Uninstall

### macOS
```bash
~/m2g/claude-voice/uninstall.sh
```

### Windows
```powershell
powershell -File "$env:USERPROFILE\m2g\claude-voice\uninstall.ps1"
```

---

## File Locations

### macOS
```
~/m2g/claude-voice/
├── m2g-say          # Voice script
├── claudev          # Claude wrapper
├── m2g-ask          # Quick question helper
└── uninstall.sh

/usr/local/bin/
├── m2g-say → symlink
├── claudev → symlink
└── m2g-ask → symlink
```

### Windows
```
%USERPROFILE%\m2g\claude-voice\
├── say.ps1          # PowerShell voice script
├── m2g-say.cmd      # Batch wrapper
├── claudev.cmd      # Claude wrapper
├── m2g-ask.cmd      # Quick question helper
└── uninstall.ps1
```

---

## Integration with M2G Tools

This voice pack works with:
- **m2g-claude** - Custom streaming CLI (from `setup-m2g-claude.sh`)
- **claude** - Official Anthropic CLI
- **claude-code** - VS Code Copilot CLI

For the full M2G toolchain, also install:
```bash
# M2G Claude CLI with streaming + MCP
~/NOIZYLAB/GABRIEL/scripts/setup-m2g-claude.sh

# Worker add-ons (dashboard, model registry)
cd ~/NOIZYLAB/GABRIEL/workers/noizylab-main
~/NOIZYLAB/GABRIEL/scripts/setup-worker-addons.sh
```

---

*Part of the GABRIEL / MC96ECOUNIVERSE system*
