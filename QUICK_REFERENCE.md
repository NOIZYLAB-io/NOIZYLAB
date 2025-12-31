# NOIZYLAB Quick Reference Card

> **GORUNFREE** - One command, everything done.

---

## System Commands

| Command | Description |
|---------|-------------|
| `gabrielstatus` | Check GABRIEL system status |
| `gabdiag` | Full system diagnostic |
| `nlstatus` | NOIZYLAB ecosystem status |
| `sysinfo` | Complete system information |
| `gorunfree health` | Quick health check |

---

## Navigation

| Command | Destination |
|---------|-------------|
| `cdgab` | ~/NOIZYLAB/GABRIEL |
| `cdnl` | ~/NOIZYLAB |
| `cdcm` | ~/NOIZYLAB/GABRIEL/CODEMASTER |
| `..` / `...` / `....` | Up 1/2/3 directories |
| `mkcd <dir>` | Create and enter directory |

---

## Git Shortcuts

| Command | Action |
|---------|--------|
| `gs` | Status (short) |
| `gaa` | Add all |
| `gc "msg"` | Commit with message |
| `gp` | Push |
| `gpl` | Pull |
| `gcm "msg"` | Add all + commit |
| `gpc` | Push current branch |
| `glog` | Pretty log |
| `gabsync` | Sync GABRIEL to GitHub |

---

## GORUNFREE Commands

```bash
# Deployment
gorunfree deploy [target]    # Deploy to Cloudflare
gorunfree sync               # Sync to GitHub

# Status & Monitoring
gorunfree status             # Show all status
gorunfree health             # Quick health check
gorunfree logs [worker]      # Tail logs

# AI Agents
gorunfree gabriel            # Launch GABRIEL
gorunfree brain              # Launch God Brain
gorunfree dream              # Launch DreamChamber

# Database
gorunfree db list            # List databases

# Maintenance
gorunfree clean              # Clean temp files
gorunfree maintain           # Daily maintenance
gorunfree backup             # Backup system
gorunfree update             # Update dependencies
gorunfree version            # Show version
```

---

## Development

### Python
| Command | Action |
|---------|--------|
| `py` | Python 3 |
| `venv` | Create virtualenv |
| `activate` | Activate venv |
| `pyvenv [name]` | Create + activate venv |
| `pipr` | Install requirements |

### Node
| Command | Action |
|---------|--------|
| `ni` | npm install |
| `nr <script>` | npm run |
| `ns` | npm start |
| `nb` | npm run build |

### Swift
| Command | Action |
|---------|--------|
| `swb` | swift build |
| `swr` | swift run |
| `swt` | swift test |
| `swinfo` | Swift version info |
| `xopen` | Open Xcode project |
| `xcpurge` | Clean derived data |

---

## Ollama / AI

| Command | Action |
|---------|--------|
| `models` | List Ollama models |
| `llama70` | Run llama3.1:70b |
| `qwen72` | Run qwen2.5:72b |
| `code` | Run codestral |

---

## Network

| Command | Action |
|---------|--------|
| `myip` | Public IP |
| `localip` | Local IP |
| `ports` | Show listening ports |
| `isup <host>` | Check host status |
| `httpstatus <url>` | Get HTTP code |
| `serve [port]` | Quick HTTP server |

### Tailscale
| Command | Action |
|---------|--------|
| `tss` | Status |
| `tsip` | Show IP |
| `ts-up` | Connect |
| `ts-down` | Disconnect |

---

## Docker

| Command | Action |
|---------|--------|
| `dkps` | List running |
| `dkpsa` | List all |
| `dkl <name>` | Tail logs |
| `dkcu` | Compose up |
| `dkcd` | Compose down |

---

## File Operations

| Command | Action |
|---------|--------|
| `ll` | List with details |
| `lt` | List by time |
| `lS` | List by size |
| `ff <name>` | Find files |
| `fd <name>` | Find directories |
| `search <text>` | Grep in files |
| `extract <file>` | Extract any archive |
| `backup <file>` | Create timestamped backup |

---

## Utilities

| Command | Action |
|---------|--------|
| `weather` | Show weather |
| `now` | Current timestamp |
| `randstr [len]` | Random string |
| `genuuid` | Generate UUID |
| `b64e/b64d` | Base64 encode/decode |
| `jsonpp` | Pretty print JSON |
| `clip` / `paste` | Clipboard |
| `copypath` | Copy current path |

---

## Quick Edits

| Command | Opens |
|---------|-------|
| `zshrc` | ~/.zshrc |
| `zshenv` | ~/.config/zsh/ |
| `secrets` | ~/.env.secrets |
| `claudemd` | ~/CLAUDE.md |

---

## macOS

| Command | Action |
|---------|--------|
| `finder` | Open Finder here |
| `showfiles` | Show hidden files |
| `hidefiles` | Hide hidden files |
| `cleanup` | Delete .DS_Store files |
| `emptytrash` | Empty trash |
| `flushdns` | Flush DNS cache |
| `cpu` | Show CPU info |
| `mem` | Show memory info |

---

## Key Directories

```
~/NOIZYLAB/               # Main repo
~/NOIZYLAB/GABRIEL/       # GABRIEL system
~/NOIZYLAB/GABRIEL/CODEMASTER/  # Code organization
~/NOIZYLAB/GABRIEL/workers/     # Cloudflare workers
~/NOIZYLAB/GABRIEL/scripts/     # System scripts
~/.config/zsh/            # Shell config
~/.env.secrets            # API keys (secure)
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+A` | Beginning of line |
| `Ctrl+E` | End of line |
| `Ctrl+R` | Search history |
| `Ctrl+K` | Delete to end |
| `Ctrl+U` | Delete to start |
| `Alt+S` | Insert sudo |
| `Alt+G` | Git status |
| `Alt+L` | List directory |

---

## Help Commands

| Command | Shows |
|---------|-------|
| `functions_help` | Custom functions |
| `keybindings_help` | Keyboard shortcuts |
| `gorunfree help` | GORUNFREE commands |
| `swinfo` | Swift environment |
| `gabrielstatus` | GABRIEL status |

---

## Maintenance

| Command | Action |
|---------|--------|
| `gorunfree maintain` | Daily maintenance |
| `gorunfree backup` | Backup system |
| `gorunfree clean` | Clean caches |
| `gorunfree update` | Update deps |

---

**MC96ECOUNIVERSE** | GOD (M2 Ultra) | GABRIEL (HP Omen) | DaFixer (MacBook Pro)

*Last Updated: 2025-12-29*
