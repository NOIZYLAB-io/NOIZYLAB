# 🚀 Quick Git Setup Scripts

Three levels of automation for Git project setup:

---

## 1. ⚡ Ultra Quick (No Prompts)

**One command, zero interaction:**

```bash
bash ultra-quick-git.sh my-project github-username
```

**What it does:**
- Creates `~/Projects/my-project`
- Initializes Git (main branch)
- Generates SSH key if needed
- Creates .gitignore + README.md
- Adds GitHub remote
- Enables auto-push
- Makes initial commit

**Time:** 5 seconds ⚡

---

## 2. 🎯 Quick Setup (Smart Defaults)

**Minimal prompts, smart detection:**

```bash
bash quick-git-setup.sh my-project
# OR
bash quick-git-setup.sh my-project github-username
# OR
bash quick-git-setup.sh
# (prompts for project name)
```

**What it does:**
- Detects Git config from global settings
- Guides SSH key setup with clipboard copy
- Creates GitHub repo reminder
- Tests SSH connection
- Pushes initial commit

**Time:** 2 minutes 🚀

---

## 3. 🛠️ Full Setup (Complete Control)

**Interactive menu with all options:**

```bash
bash setup_git_automation.sh
```

**Features:**
- 5 setup modes
- Custom SSH key types
- Multiple remotes
- Advanced configuration
- Troubleshooting tools

**Time:** 5 minutes 🔧

---

## Quick Comparison

| Feature | Ultra Quick | Quick Setup | Full Setup |
|---------|-------------|-------------|------------|
| **Commands** | 1 | 1-2 | Multiple |
| **Prompts** | 0 | 3-5 | 10+ |
| **Time** | 5 sec | 2 min | 5 min |
| **SSH Key** | Auto | Guided | Full control |
| **Validation** | Minimal | Smart | Complete |
| **Best for** | Speed | Daily use | First time |

---

## Usage Examples

### **Ultra Quick (Fastest)**

```bash
# New project in 5 seconds
bash ultra-quick-git.sh awesome-app myusername

# Then:
cd ~/Projects/awesome-app
# Start coding!
```

### **Quick Setup (Recommended)**

```bash
# Interactive but fast
bash quick-git-setup.sh

# Enter:
# - Project name: awesome-app
# - (auto-detects email/name from git config)
# - GitHub username: myusername

# Follows prompts to:
# - Add SSH key to GitHub
# - Create repo on GitHub
# - Push initial commit

# Done!
```

### **Full Setup (First Time)**

```bash
# Complete guided setup
bash setup_git_automation.sh

# Menu:
# 1. Full Setup (Recommended)
# 2. Quick Setup (Existing repo)
# 3. SSH Keys Only
# 4. Auto-Push Hook Only
# 5. Custom Setup

# Select 1, follow prompts
```

---

## What Each Script Creates

```
~/Projects/my-project/
├── .git/
│   ├── config               # Local Git config
│   └── hooks/
│       └── post-commit      # Auto-push hook
├── .gitignore               # Standard ignores
└── README.md                # Project readme

~/.ssh/
├── id_ed25519               # Private key (if new)
└── id_ed25519.pub           # Public key (add to GitHub)
```

---

## Auto-Push Feature

All scripts enable **auto-push**:

```bash
# After setup, just commit:
git add .
git commit -m "Add feature"
# ✅ Automatically pushes to GitHub!

# No need for:
git push  # ← Not needed anymore!
```

---

## Common Workflows

### **Workflow 1: New Project (Ultra Fast)**

```bash
# Terminal 1 - Setup
bash ultra-quick-git.sh my-app username

# Browser - Create repo
# Go to: https://github.com/new
# Name: my-app
# Click "Create repository"

# Terminal 2 - Start coding
cd ~/Projects/my-app
git push -u origin main      # First push
# Now edit files...
git commit -m "Add code"     # Auto-pushes!
```

**Time:** ~1 minute total

### **Workflow 2: Multiple Projects Same Day**

```bash
# Project 1
bash ultra-quick-git.sh project-a username
# (SSH key created once)

# Project 2
bash ultra-quick-git.sh project-b username
# (Reuses SSH key)

# Project 3
bash ultra-quick-git.sh project-c username
# (Reuses SSH key)

# All projects auto-push!
```

### **Workflow 3: Team Collaboration**

```bash
# Team member 1 (project creator)
bash quick-git-setup.sh team-project
# Creates repo, pushes initial commit

# Team member 2 (joins project)
git clone git@github.com:username/team-project.git
cd team-project

# Add auto-push hook
bash /path/to/setup_git_automation.sh
# Select: 4 (Auto-Push Hook Only)

# Now both team members have auto-push!
```

---

## Smart Features

### **Ultra Quick Script:**
- ✅ Zero prompts (all from arguments)
- ✅ Uses Git global config
- ✅ Fallback to GitHub noreply email
- ✅ Sanitizes project names
- ✅ Silent operation
- ✅ Error-free execution

### **Quick Setup Script:**
- ✅ Detects existing SSH keys
- ✅ Auto-copies key to clipboard
- ✅ Tests GitHub connection
- ✅ Smart project name sanitization
- ✅ Infers GitHub username from email
- ✅ Creates repo reminder

### **Full Setup Script:**
- ✅ Interactive menu system
- ✅ Multiple key types (ed25519/RSA)
- ✅ Key backup before regeneration
- ✅ Platform detection (Mac/Linux/Windows)
- ✅ Comprehensive error handling
- ✅ Status verification

---

## SSH Key Handling

### **First Run (No Key):**
```bash
bash ultra-quick-git.sh my-project username
# ✅ Generates ~/.ssh/id_ed25519
# ⚠️  Displays public key
# 📋 Add to: https://github.com/settings/keys
```

### **Subsequent Runs (Key Exists):**
```bash
bash ultra-quick-git.sh another-project username
# ✅ Reuses existing key
# ✓ No prompts needed
```

### **Manual Key Check:**
```bash
# Check if key exists
ls -la ~/.ssh/id_ed25519*

# View public key
cat ~/.ssh/id_ed25519.pub

# Test GitHub connection
ssh -T git@github.com
```

---

## Troubleshooting

### **Script Not Executable**
```bash
chmod +x ultra-quick-git.sh quick-git-setup.sh setup_git_automation.sh
```

### **Project Already Exists**
```bash
# Ultra quick (fails gracefully)
bash ultra-quick-git.sh existing-project username
# Error: directory exists

# Quick setup (asks to use existing)
bash quick-git-setup.sh existing-project
# Prompt: Use existing directory? [Y/n]
```

### **SSH Key Not Working**
```bash
# Add to agent
ssh-add ~/.ssh/id_ed25519

# Test connection
ssh -T git@github.com

# Check if key is on GitHub
# Go to: https://github.com/settings/keys
```

### **Auto-Push Not Working**
```bash
cd ~/Projects/my-project

# Check hook exists
ls -la .git/hooks/post-commit

# Make executable
chmod +x .git/hooks/post-commit

# Test manually
git commit -m "test"
# Should see: "🚀 Auto-pushing..."
```

---

## Advanced Usage

### **Custom Project Directory**
```bash
# Edit ultra-quick-git.sh
# Change: PROJECT_PATH="$HOME/Projects/$PROJECT_NAME"
# To:     PROJECT_PATH="$HOME/Code/$PROJECT_NAME"
```

### **Different Default Branch**
```bash
# Edit script
# Change: git init -b main
# To:     git init -b master
```

### **Custom .gitignore Template**
```bash
# Create: ~/.gitignore_global
# Then scripts will copy it automatically
```

### **Disable Auto-Push for Specific Project**
```bash
cd ~/Projects/my-project
rm .git/hooks/post-commit

# Or disable temporarily:
mv .git/hooks/post-commit .git/hooks/post-commit.disabled
```

---

## Integration with GABRIEL

Add to `start_gabriel.sh`:

```bash
# Menu option 10
10)
    echo ""
    read -p "Project name: " PROJ_NAME
    bash setup_git_automation.sh "$PROJ_NAME"
    ;;
```

Or create GABRIEL command:

```bash
# In gabriel_ultimate.py
>>> new project my-app
# Runs: ultra-quick-git.sh my-app username
```

---

## Summary

**Choose your speed:**

🏃 **Need it NOW?**
```bash
bash ultra-quick-git.sh project-name username
```

🚶 **Want guidance?**
```bash
bash quick-git-setup.sh project-name
```

🧘 **First time setup?**
```bash
bash setup_git_automation.sh
```

**All scripts:**
- ✅ Create Git repo
- ✅ Generate SSH keys
- ✅ Enable auto-push
- ✅ Add GitHub remote
- ✅ Make initial commit

**Pick based on your need for speed! 🚀**

---

**Created:** November 11, 2025  
**Scripts:** 3 (ultra-quick, quick, full)  
**Total Lines:** 1,200+  
**Setup Time:** 5 seconds to 5 minutes  
**Status:** Production Ready ⚡
