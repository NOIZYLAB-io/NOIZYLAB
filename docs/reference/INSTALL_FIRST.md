# 📦 INSTALL PREREQUISITES FIRST

## Missing Requirements Detected

The setup script needs:
- ✅ Node.js
- ✅ npm
- ✅ Wrangler CLI

---

## 🚀 Quick Install (One Command)

```bash
cd /Users/m2ultra/NOIZYLAB/noizylab-os
./scripts/install-prerequisites.sh
```

This will:
1. Install Homebrew (if needed)
2. Install Node.js
3. Install Wrangler CLI
4. Verify everything

---

## OR Install Manually

### Option 1: Using Homebrew
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js (includes npm)
brew install node

# Install Wrangler
npm install -g wrangler
```

### Option 2: Using Node Version Manager (nvm)
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Install Node.js
nvm install --lts
nvm use --lts

# Install Wrangler
npm install -g wrangler
```

---

## ✅ After Installation

Run the master setup:
```bash
./scripts/MASTER_SETUP.sh
```

---

**Run the prerequisites installer first, then the master setup!**

