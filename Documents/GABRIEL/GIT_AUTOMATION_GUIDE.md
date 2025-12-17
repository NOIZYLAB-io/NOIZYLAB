# 🔧 Git Automation Setup Guide

## Overview

Complete Git automation script for initializing repositories with SSH keys and auto-push hooks.

**Works on:** macOS, Linux, Windows (Git Bash)

---

## Quick Start

```bash
cd /Users/rsp_ms/GABRIEL
bash setup_git_automation.sh

# Select option 1 (Full Setup)
```

---

## Features

### 1. **Git Initialization**
- Creates new Git repository
- Sets default branch (main/master)
- Configures user name and email
- Smart detection of existing repos

### 2. **SSH Key Management**
- Generates ed25519 or RSA keys
- Adds keys to ssh-agent
- Backs up existing keys
- Auto-copies to clipboard
- Tests SSH connections

### 3. **Remote Repository**
- Adds GitHub/GitLab/Bitbucket remote
- Validates repository URLs
- Updates existing remotes
- Tests connectivity

### 4. **Auto-Push Hook**
- Creates post-commit hook
- Automatically pushes after every commit
- Smart branch detection
- Error handling

### 5. **Initial Setup**
- Creates .gitignore
- Creates README.md
- Makes initial commit
- Pushes to remote

---

## Menu Options

```
1. Full Setup (Recommended)
   - Complete end-to-end setup
   - Best for new repositories
   
2. Quick Setup (Existing repo)
   - Git config + SSH keys
   - Skip initialization
   
3. SSH Keys Only
   - Generate/manage SSH keys only
   - For existing Git setups
   
4. Auto-Push Hook Only
   - Add post-commit hook
   - Requires existing repo
   
5. Custom Setup
   - Pick individual steps
   - Advanced users

9. Exit
```

---

## Usage Examples

### **New Project Setup**

```bash
# 1. Create project directory
mkdir ~/Projects/my-new-project
cd ~/Projects/my-new-project

# 2. Run setup
bash /Users/rsp_ms/GABRIEL/setup_git_automation.sh

# 3. Select option 1 (Full Setup)

# 4. Enter details:
Enter your Git email: your@email.com
Enter your Git name: Your Name
Enter repository URL: git@github.com:username/my-new-project.git
Default branch name [main]: main
Choose key type [1]: 1

# 5. Add SSH key to GitHub (auto-copied to clipboard)
# Go to: https://github.com/settings/keys

# 6. Start coding!
echo "# My Project" > index.js
git add .
git commit -m "Add index file"
# ✅ Auto-pushes to GitHub!
```

### **Existing Project (Add Auto-Push)**

```bash
cd ~/Projects/existing-project

bash /Users/rsp_ms/GABRIEL/setup_git_automation.sh

# Select option 4 (Auto-Push Hook Only)
# Now commits will auto-push
```

### **SSH Keys Only (Multiple Machines)**

```bash
bash /Users/rsp_ms/GABRIEL/setup_git_automation.sh

# Select option 3 (SSH Keys Only)
# Copy public key to other services
```

---

## SSH Key Types

### **ED25519 (Recommended)**
```bash
Pros:
  ✅ Modern, secure
  ✅ Faster generation
  ✅ Smaller key size
  ✅ Better performance

When to use:
  - New setups
  - Modern systems
  - GitHub/GitLab (2020+)
```

### **RSA 4096-bit**
```bash
Pros:
  ✅ Universal compatibility
  ✅ Works everywhere
  ✅ Industry standard

When to use:
  - Legacy systems
  - Corporate environments
  - Older Git servers
```

---

## Auto-Push Hook Details

**Location**: `.git/hooks/post-commit`

**What it does**:
```bash
#!/bin/bash
# Runs after every commit

BRANCH=$(git rev-parse --abbrev-ref HEAD)
git push origin "$BRANCH"
```

**Behavior**:
- Triggers after `git commit`
- Pushes current branch to origin
- Shows success/failure message
- Does NOT block commit on push failure

**Enable/Disable**:
```bash
# Disable temporarily
mv .git/hooks/post-commit .git/hooks/post-commit.disabled

# Re-enable
mv .git/hooks/post-commit.disabled .git/hooks/post-commit

# Disable permanently
rm .git/hooks/post-commit
```

---

## Configuration Files

### **Created/Modified Files**:

```
~/.ssh/
├── id_ed25519              # Private key (keep secret!)
├── id_ed25519.pub          # Public key (share this)
└── config                  # SSH config (macOS only)

.git/
├── config                  # Local Git config
└── hooks/
    └── post-commit         # Auto-push hook

.gitignore                  # Ignore patterns
README.md                   # Project readme
```

---

## SSH Key Locations

### **macOS/Linux**:
```bash
Private: ~/.ssh/id_ed25519
Public:  ~/.ssh/id_ed25519.pub
```

### **Windows (Git Bash)**:
```bash
Private: C:\Users\YourName\.ssh\id_ed25519
Public:  C:\Users\YourName\.ssh\id_ed25519.pub
```

---

## Adding SSH Key to Git Services

### **GitHub**

1. Copy public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   # Or script auto-copies to clipboard
   ```

2. Go to: https://github.com/settings/keys

3. Click **"New SSH key"**

4. Paste key and save

5. Test:
   ```bash
   ssh -T git@github.com
   # Should see: "Hi username! You've successfully authenticated"
   ```

### **GitLab**

1. Go to: https://gitlab.com/-/profile/keys

2. Paste public key

3. Test:
   ```bash
   ssh -T git@gitlab.com
   # Should see: "Welcome to GitLab, @username!"
   ```

### **Bitbucket**

1. Go to: https://bitbucket.org/account/settings/ssh-keys/

2. Click **"Add key"**

3. Paste and save

4. Test:
   ```bash
   ssh -T git@bitbucket.org
   # Should see: "authenticated via ssh key"
   ```

---

## Workflow Examples

### **Daily Development Workflow**

```bash
# 1. Pull latest changes
git pull

# 2. Make changes
vim myfile.js

# 3. Stage changes
git add myfile.js

# 4. Commit (auto-pushes!)
git commit -m "Update feature X"
# ✅ Automatically pushed to origin

# 5. Continue working
# No need to remember 'git push'!
```

### **Working on Feature Branch**

```bash
# 1. Create branch
git checkout -b feature/new-thing

# 2. Make changes and commit
git add .
git commit -m "Add new feature"
# ✅ Auto-pushes to origin/feature/new-thing

# 3. Continue committing
git commit -m "Refine feature"
# ✅ Auto-pushes again

# 4. Merge to main (manual)
git checkout main
git merge feature/new-thing
git commit -m "Merge feature"
# ✅ Auto-pushes to origin/main
```

### **Handling Push Failures**

```bash
# If remote is ahead:
git commit -m "My changes"
# ⚠️  Push failed

# Pull first:
git pull

# Then commit merges automatically
# ✅ Auto-push succeeds
```

---

## Troubleshooting

### **SSH Key Not Working**

```bash
# Check key exists
ls -la ~/.ssh/id_ed25519*

# Check ssh-agent
ssh-add -l

# Add key manually
ssh-add ~/.ssh/id_ed25519

# Test connection
ssh -T git@github.com
```

### **Auto-Push Failing**

```bash
# Check remote
git remote -v

# Check if ahead of remote
git status

# Pull first
git pull

# Try push manually
git push

# Check hook exists and is executable
ls -la .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

### **Permission Denied (publickey)**

```bash
# 1. Verify key is added to ssh-agent
ssh-add -l

# 2. Add key if missing
ssh-add ~/.ssh/id_ed25519

# 3. Verify key is on GitHub/GitLab
# Check: https://github.com/settings/keys

# 4. Test with verbose mode
ssh -vT git@github.com
```

### **Wrong Email/Name in Commits**

```bash
# Check current config
git config --local user.email
git config --local user.name

# Update
git config --local user.email "correct@email.com"
git config --local user.name "Correct Name"

# Fix last commit
git commit --amend --reset-author --no-edit
```

---

## Advanced Usage

### **Multiple SSH Keys (Different Services)**

```bash
# Create service-specific keys
ssh-keygen -t ed25519 -C "work@company.com" -f ~/.ssh/id_ed25519_work
ssh-keygen -t ed25519 -C "personal@email.com" -f ~/.ssh/id_ed25519_personal

# Configure ~/.ssh/config
cat >> ~/.ssh/config << EOF

# Work GitHub
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work

# Personal GitHub
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
EOF

# Use in Git URLs
git remote add origin git@github-work:company/repo.git
git remote add personal git@github-personal:username/repo.git
```

### **Conditional Auto-Push (Only Certain Branches)**

Edit `.git/hooks/post-commit`:
```bash
#!/bin/bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Only auto-push main and develop
if [[ "$BRANCH" == "main" ]] || [[ "$BRANCH" == "develop" ]]; then
    echo "🚀 Auto-pushing $BRANCH..."
    git push origin "$BRANCH"
else
    echo "⏭️  Skipping auto-push for $BRANCH"
fi
```

### **Auto-Push with Pull First**

Edit `.git/hooks/post-commit`:
```bash
#!/bin/bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)

echo "🔄 Pulling latest changes..."
git pull origin "$BRANCH" --rebase

echo "🚀 Pushing to origin/$BRANCH..."
git push origin "$BRANCH"
```

### **Backup SSH Keys**

```bash
# Backup keys to USB drive
cp ~/.ssh/id_ed25519* /Volumes/USBDrive/ssh-backup/

# Or encrypted backup
tar czf ssh-keys-backup.tar.gz ~/.ssh/id_ed25519*
gpg -c ssh-keys-backup.tar.gz
rm ssh-keys-backup.tar.gz

# Restore
gpg -d ssh-keys-backup.tar.gz.gpg | tar xz -C ~/
```

---

## Security Best Practices

### ✅ **Do:**
- Use passphrase for SSH keys (production systems)
- Keep private keys private (`~/.ssh/id_ed25519`)
- Add keys to ssh-agent
- Use different keys for different services
- Backup keys securely
- Rotate keys periodically (yearly)

### ❌ **Don't:**
- Commit private keys to Git
- Share private keys
- Use same key everywhere (work/personal)
- Store keys in cloud without encryption
- Use weak passphrases

### **Check for Exposed Keys:**
```bash
# Search Git history for keys
git log --all --full-history --source -- "*id_rsa*" "*id_ed25519*"

# If found, rotate immediately!
```

---

## Platform-Specific Notes

### **macOS**
```bash
# SSH keys stored in keychain
# UseKeychain setting auto-added

# Clipboard: pbcopy (built-in)
```

### **Linux**
```bash
# May need xclip or xsel for clipboard
sudo apt install xclip

# Or:
sudo apt install xsel
```

### **Windows (Git Bash)**
```bash
# Use Git Bash terminal (not CMD)
# SSH agent may need manual start:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Clipboard: clip (built-in)
```

---

## Integration with GABRIEL

### **Add Git Commands to GABRIEL Ultimate**

```python
# In gabriel_ultimate.py

def git_status(self):
    """Show Git status"""
    subprocess.run(["git", "status"])

def git_commit(self, message):
    """Quick commit"""
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    # Auto-push via hook!

# Interactive commands
>>> git status
>>> git commit "Updated feature"
```

---

## Summary

✅ **Complete Git automation**
✅ **SSH key management**
✅ **Auto-push after commits**
✅ **Cross-platform (Mac/Linux/Windows)**
✅ **GitHub/GitLab/Bitbucket support**

**Get started:**
```bash
bash setup_git_automation.sh
# Select option 1 (Full Setup)
```

**Daily workflow:**
```bash
git add .
git commit -m "Your message"
# ✅ Automatically pushed!
```

---

**Created**: November 11, 2025
**Version**: 1.0
**Status**: Production Ready 🚀
