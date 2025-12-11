# 📱 Manual Setup Instructions
## iPad/iPhone Development Access - Manual Setup

Since automated setup requires sudo access, follow these manual steps:

---

## 🔧 Step 1: Enable SSH on Mac

### Option A: Via System Settings (Recommended)

1. Open **System Settings** (or System Preferences on older macOS)
2. Go to **General** → **Sharing**
3. Enable **Remote Login**:
   - ✅ Check "Remote Login"
   - ✅ Note the message showing "Remote Login: On"

**Or use Command Line:**

1. Open **Terminal**
2. Run (will prompt for password):
   ```bash
   sudo systemsetup -setremotelogin on
   ```
3. Enter your Mac password when prompted

### Verify SSH is Enabled

Check if SSH is enabled:
```bash
sudo systemsetup -getremotelogin
```

Should show: **"Remote Login: On"**

---

## 📋 Step 2: Get Connection Information

Run these commands to get your connection info:

```bash
# Get your username
whoami

# Get your Mac's IP address
ipconfig getifaddr en0
# or if that doesn't work:
ipconfig getifaddr en1
# or check all interfaces:
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**Note these values:**
- **Username:** `___________`
- **IP Address:** `___________`
- **Hostname:** `$(hostname).local` (can use instead of IP)

---

## 🔐 Step 3: Create SSH Key (Optional - for passwordless access)

Create SSH key pair for easier access:

```bash
cd ~/.ssh
ssh-keygen -t rsa -b 4096 -f id_rsa_ipad -N "" -C "ipad-dev-access"
```

Add public key to authorized_keys:

```bash
cat ~/.ssh/id_rsa_ipad.pub >> ~/.ssh/authorized_keys
```

**Note:** You'll need to copy the private key (`id_rsa_ipad`) to your iPad/iPhone for passwordless access.

---

## 📱 Step 4: Install App on iPad/iPhone

### Recommended: Blink Shell

1. Open **App Store** on iPad/iPhone
2. Search for **"Blink Shell"**
3. Install (Price: ~$20 one-time)
4. Open Blink Shell

### Alternative: Termius

1. Open **App Store**
2. Search for **"Termius"**
3. Install (Free tier available)
4. Open Termius

---

## 🔌 Step 5: Connect from iPad/iPhone

### Using Blink Shell:

1. Open **Blink Shell** on iPad/iPhone
2. Tap **+** to add new host
3. Enter:
   - **Host:** Your Mac's IP address (from Step 2)
   - **User:** Your Mac username (from Step 2)
   - **Port:** `22`
   - **Name:** `My Mac` (or any name)

4. **For passwordless access:**
   - Tap **SSH Keys**
   - Tap **+**
   - Import the private key (`id_rsa_ipad`) you created in Step 3

5. **Save** and **Connect**

6. Enter your Mac password (first time only, if not using key)

### Using Termius:

1. Open **Termius** on iPad/iPhone
2. Tap **+** → **New Host**
3. Enter:
   - **Label:** `My Mac`
   - **Address:** Your Mac's IP address
   - **Username:** Your Mac username
   - **Port:** `22`

4. **For passwordless access:**
   - Tap **Keys**
   - Import your private key

5. **Save** and **Connect**

---

## ✅ Step 6: Test Connection

Once connected via SSH:

1. **Verify you're on your Mac:**
   ```bash
   hostname
   whoami
   pwd
   ```

2. **Navigate to NOIZYLAB:**
   ```bash
   cd ~/NOIZYLAB
   ls -la
   ```

3. **Test basic commands:**
   ```bash
   git status
   python --version
   ```

**Success!** 🎉 You're now connected from iPad/iPhone to your Mac!

---

## 📋 Quick Reference

### Connection Details

**SSH Command (from iPad/iPhone terminal):**
```bash
ssh username@ip-address
```

**Or using hostname:**
```bash
ssh username@hostname.local
```

### File Locations

- **SSH Key (if created):** `~/.ssh/id_rsa_ipad`
- **Projects:** `~/NOIZYLAB/`
- **Setup Scripts:** `~/NOIZYLAB/ipad-dev-setup/`

---

## 🆘 Troubleshooting

### Can't Connect

1. **Check Mac and iPad/iPhone are on same WiFi:**
   - Both must be on same network

2. **Check SSH is enabled:**
   ```bash
   sudo systemsetup -getremotelogin
   ```
   Should show: **"Remote Login: On"**

3. **Check Firewall:**
   - System Settings → Network → Firewall
   - Ensure SSH connections are allowed

4. **Verify IP address:**
   ```bash
   ipconfig getifaddr en0
   # Try en1 if en0 doesn't work
   ```

### Connection Refused

1. **SSH might not be enabled** - Enable it (see Step 1)
2. **Wrong IP address** - Check IP again
3. **Firewall blocking** - Check firewall settings
4. **Different network** - Ensure same WiFi

### Password Issues

1. **Use SSH key instead** (see Step 3)
2. **Reset Mac password** if needed
3. **Check username** - Must match exactly

---

## 🎉 Next Steps

Once connected:

1. **Navigate to projects:**
   ```bash
   cd ~/NOIZYLAB
   ```

2. **Start developing:**
   - Edit files with `nano` or `vim`
   - Run scripts with `python`, `node`, etc.
   - Use `git` for version control

3. **Use Claude for assistance:**
   - Open Claude.ai in Safari on iPad/iPhone
   - Copy/paste code between terminal and Claude

4. **Optional - Setup code-server:**
   ```bash
   cd ~/NOIZYLAB/ipad-dev-setup
   ./setup-code-server.sh
   ```
   This gives you VS Code in browser!

---

## 📚 Additional Resources

- **iPad Guide:** `IPAD_DEVELOPMENT_GUIDE.md`
- **iPhone Guide:** `IPHONE_DEVELOPMENT_GUIDE.md`
- **Code Server Setup:** `setup-code-server.sh`

---

**Last Updated:** 2024-11-22  
**Status:** ✅ Manual Setup Instructions

