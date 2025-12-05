# TERMIUS BRIDGE SETUP - GORUNFREE EDITION

## 🎯 WHAT IS THIS?

**Termius Bridge** connects Claude.ai to your remote servers (like GABRIEL).

```
Claude.ai → Termius Bridge → Your Servers (GABRIEL, etc.)
```

**Why you'd want it:**
- Claude can SSH into GABRIEL for you
- Execute commands remotely through chat
- Automate server management via AI

---

## 🤔 DO YOU NEED IT?

### ✅ YES, if you want:
- Claude.ai to manage GABRIEL remotely
- AI-powered server automation
- Remote command execution via chat
- MCP integration with Termius

### ❌ NO, if you prefer:
- Manual SSH via Terminal
- AppleScript/Python SSH automation
- Standard remote workflows

**For MC96 ecosystem:** Probably YES - would let Claude help manage GABRIEL!

---

## 📋 PROPER SETUP (Step-by-Step)

### STEP 1: Install Termius (if not already done)

**Option A: Homebrew**
```bash
brew install --cask termius
```

**Option B: Direct Download**
https://termius.com/

### STEP 2: Get Termius Bridge Credentials

1. Open Termius app
2. Go to **Settings** → **Integrations**
3. Look for **"Termius Bridge"** or **"API Access"**
4. Click **"Generate Credentials"** or **"Create Bridge Credentials"**
5. Save the JSON file somewhere safe

**Recommended location:**
```bash
mkdir -p ~/.termius
# Save the JSON file to: ~/.termius/bridge-credentials.json
```

### STEP 3: Set the Environment Variable

**Temporary (current session only):**
```bash
export BRIDGE_CREDENTIALS_FILE=~/.termius/bridge-credentials.json
```

**Permanent (persists across sessions):**

For **Zsh** (macOS Catalina+):
```bash
echo 'export BRIDGE_CREDENTIALS_FILE=~/.termius/bridge-credentials.json' >> ~/.zshrc
source ~/.zshrc
```

For **Bash** (older macOS):
```bash
echo 'export BRIDGE_CREDENTIALS_FILE=~/.termius/bridge-credentials.json' >> ~/.bash_profile
source ~/.bash_profile
```

### STEP 4: Verify Setup

```bash
# Check if variable is set
echo $BRIDGE_CREDENTIALS_FILE

# Should output: /Users/rsp_ms/.termius/bridge-credentials.json

# Check if file exists
ls -la $BRIDGE_CREDENTIALS_FILE

# Should show the file with size > 0
```

### STEP 5: Add Your Servers to Termius

1. Open Termius
2. Click **"New Host"**
3. Add GABRIEL:
   - **Label:** GABRIEL
   - **Address:** [GABRIEL's IP address]
   - **Username:** [your username]
   - **Authentication:** SSH Key or Password
4. Test connection in Termius first
5. Once working, Claude.ai can use it!

---

## 🔐 SECURITY NOTES

**The credentials file contains:**
- API access to your Termius account
- Ability to connect to your saved servers
- Sensitive authentication data

**Keep it safe:**
```bash
# Set proper permissions (only you can read)
chmod 600 ~/.termius/bridge-credentials.json

# Never commit to Git
echo ".termius/" >> ~/.gitignore
```

---

## 🚀 USING IT WITH CLAUDE.AI

Once set up, you can ask Claude to:

```
"Connect to GABRIEL and check disk space"
"SSH into my HP OMEN and restart the service"
"Run this script on GABRIEL"
```

Claude will use Termius Bridge to execute commands remotely!

---

## 🛠️ TROUBLESHOOTING

### Problem: "File not found"
```bash
# Check the path is correct
echo $BRIDGE_CREDENTIALS_FILE
ls -la $BRIDGE_CREDENTIALS_FILE

# If file doesn't exist, regenerate in Termius app
```

### Problem: "Permission denied"
```bash
# Fix permissions
chmod 600 ~/.termius/bridge-credentials.json
```

### Problem: "Variable not set after restart"
```bash
# Make sure you added to the RIGHT file
# Zsh users: ~/.zshrc
# Bash users: ~/.bash_profile

# Check which shell you're using
echo $SHELL

# Re-source the file
source ~/.zshrc  # or source ~/.bash_profile
```

### Problem: "Can't connect to server"
```bash
# Test SSH connection manually first
ssh user@gabriel-ip-address

# Make sure GABRIEL is on and reachable
ping gabriel-ip-address

# Verify Termius has the correct credentials
```

---

## 🎯 ALTERNATIVE: Simple SSH Without Termius Bridge

If you just want to SSH to GABRIEL from Python/Shell scripts:

**Python:**
```python
import subprocess

def ssh_to_gabriel(command):
    """Execute command on GABRIEL via SSH"""
    result = subprocess.run(
        ['ssh', 'user@gabriel-ip', command],
        capture_output=True,
        text=True
    )
    return result.stdout

# Use it
output = ssh_to_gabriel('df -h')
print(output)
```

**Shell:**
```bash
#!/bin/bash
# SSH to GABRIEL and run command

ssh user@gabriel-ip 'df -h'
```

**AppleScript:**
```applescript
-- SSH via Terminal
tell application "Terminal"
    do script "ssh user@gabriel-ip"
end tell
```

---

## 🎮 RECOMMENDED SETUP FOR YOUR USE CASE

**For MC96 Ecosystem (GOD ↔ GABRIEL):**

1. **Set up SSH keys** (passwordless authentication)
2. **Use Python/Shell scripts** for automation
3. **Optional:** Add Termius Bridge for Claude.ai integration
4. **Create wrapper functions** in your automation hub

**Example wrapper:**
```python
#!/usr/bin/env python3
"""
GABRIEL Remote Control
Execute commands on GABRIEL from GOD
"""

import subprocess
import json

def gabriel_command(cmd, use_bridge=False):
    """
    Execute command on GABRIEL
    
    Parameters:
        cmd (str): Command to execute
        use_bridge (bool): Use Termius Bridge or direct SSH
    
    Returns:
        str: Command output
    """
    if use_bridge:
        # Use Termius Bridge (if set up)
        result = subprocess.run(
            ['termius-bridge', 'exec', 'GABRIEL', cmd],
            capture_output=True,
            text=True
        )
    else:
        # Direct SSH
        result = subprocess.run(
            ['ssh', 'user@gabriel-ip', cmd],
            capture_output=True,
            text=True
        )
    
    return result.stdout

# Test it
if __name__ == "__main__":
    print("Checking GABRIEL disk space...")
    output = gabriel_command('df -h')
    print(output)
```

---

## 📝 QUICK REFERENCE CARD

```bash
# Set environment variable (temporary)
export BRIDGE_CREDENTIALS_FILE=/path/to/file.json

# Set permanently (Zsh)
echo 'export BRIDGE_CREDENTIALS_FILE=~/.termius/bridge-credentials.json' >> ~/.zshrc
source ~/.zshrc

# Check if set
echo $BRIDGE_CREDENTIALS_FILE

# Test SSH manually
ssh user@server-ip

# Test with Termius Bridge (if installed)
termius-bridge exec HOST "command"
```

---

## 🎯 WHAT I RECOMMEND FOR YOU, ROB

**Short-term (this week):**
1. Skip Termius Bridge for now
2. Use standard SSH via Terminal/Python
3. Build your automation with simple SSH commands
4. Get GOD ↔ GABRIEL communication working first

**Medium-term (next month):**
1. Add Termius Bridge if you want Claude.ai integration
2. Set up the environment variable properly
3. Test remote execution through AI

**Long-term (production):**
1. Passwordless SSH with keys
2. Python wrappers for all remote commands
3. Voice-activated remote control via GABRIEL SUPREME
4. Full MC96 ecosystem integration

---

## 💡 THE BOTTOM LINE

**That command you pasted:**
```bash
export BRIDGE_CREDENTIALS_FILE=/path/to/termius-bridge-credentials.json
```

**Is incomplete. It should be:**
```bash
export BRIDGE_CREDENTIALS_FILE=~/.termius/bridge-credentials.json
```

**But you need to:**
1. Generate the credentials file in Termius first
2. Save it to that location
3. Then set the variable
4. Then test it

**OR** just use standard SSH and skip Termius Bridge entirely until you need it.

---

## 🚀 GORUNFREE ACTION PLAN

**If you want Termius Bridge NOW:**
```bash
# 1. Install Termius
brew install --cask termius

# 2. Open Termius, generate bridge credentials, save to:
#    ~/.termius/bridge-credentials.json

# 3. Set variable permanently
echo 'export BRIDGE_CREDENTIALS_FILE=~/.termius/bridge-credentials.json' >> ~/.zshrc
source ~/.zshrc

# 4. Verify
echo $BRIDGE_CREDENTIALS_FILE
```

**If you want simple SSH NOW:**
```bash
# Just SSH directly
ssh user@gabriel-ip

# Or in Python
python3 -c "import subprocess; subprocess.run(['ssh', 'user@ip', 'ls'])"
```

---

**Pick your path and GO!** 🚀

Want me to help you set up whichever option you choose?
