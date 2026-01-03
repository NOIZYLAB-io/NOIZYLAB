# 🖥️ NoizyLab OS - Desktop Widgets & Integrations

Four ways to access NoizyLab OS from your desktop!

## 1. 📊 Übersicht Widget

Beautiful desktop widget showing NoizyLab OS status.

### Installation
```bash
# Install Übersicht
brew install --cask ubersicht

# Copy widget
cp -R ubersicht/noizylab-status.widget ~/Library/Application\ Support/Übersicht/widgets/
```

### Features
- Real-time worker status
- 57 worker count display
- Round 3 Computing Legends section
- Auto-refresh every 30 seconds

---

## 2. ⚡ macOS Shortcuts

Native macOS Shortcuts integration for quick actions.

### Installation
1. Open **Shortcuts** app
2. File → Import
3. Select `shortcuts/NoizyLab-CLI.shortcut.applescript`
4. Or create new shortcut with "Run AppleScript" action

### Available Actions
- 🔧 Worker Status
- 🧠 Ask AI Question
- 💻 CPU Info
- 🖥️ OS History
- 🎮 GPU Info
- 📊 All Workers
- 🚀 Deploy All
- 📝 View Logs

---

## 3. 🚀 Raycast Extension

Full Raycast integration with search and commands.

### Installation
```bash
cd raycast/noizylab-extension
npm install
npm run dev
```

### Commands
| Command | Shortcut | Description |
|---------|----------|-------------|
| Worker Status | `nl status` | View all 57 workers |
| Ask AI | `nl ask` | Query any computing topic |
| Browse Workers | `nl workers` | Browse all workers |
| Deploy | `nl deploy` | Deploy to Cloudflare |
| CPU Architecture | `nl cpu` | CPU knowledge |
| GPU Computing | `nl gpu` | GPU knowledge |
| Operating Systems | `nl os` | OS knowledge |

---

## 4. 🍎 SwiftUI Menu Bar App

Native macOS menu bar app with popover.

### Build & Install
```bash
cd menubar-app/NoizyLabStatus
swift build -c release
cp .build/release/NoizyLabStatus /Applications/
```

### Features
- Always-visible status in menu bar
- Worker count badge
- Quick deploy button
- Open CLI in Terminal
- Category breakdown
- Real-time status indicator

---

## 🎯 Quick Setup (All Tools)

```bash
# Install all tools at once
cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os/tools/widgets

# 1. Übersicht
brew install --cask ubersicht
cp -R ubersicht/noizylab-status.widget ~/Library/Application\ Support/Übersicht/widgets/

# 2. Raycast (if installed)
cd raycast/noizylab-extension && npm install && npm run dev

# 3. Menu Bar App
cd ../menubar-app/NoizyLabStatus && swift build -c release

# 4. Shortcuts - import manually via Shortcuts app
```

---

## 📸 Screenshots

### Übersicht Widget
```
┌────────────────────────────┐
│ 🧠 NoizyLab OS            │
│ OMNI-SOVEREIGN AI PLATFORM │
│                            │
│  ┌────┐ ┌────┐ ┌────┐     │
│  │ 57 │ │ 21 │ │ 3  │     │
│  │Work│ │ R3 │ │Rnds│     │
│  └────┘ └────┘ └────┘     │
│                            │
│ 🟢 All Systems Operational │
│                            │
│ 🏆 Round 3: Computing...   │
│   • CPU Architecture       │
│   • Operating Systems      │
│   • GPU Computing          │
│   • + 17 more...           │
└────────────────────────────┘
```

---

**NoizyLab OS - The Best OS in the Universe! 🌌**
