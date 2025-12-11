# 📧 Gmail API Setup Guide

## Quick Setup

NoizyLab CORE v3.0's Inbox Scanner requires Gmail API credentials. Follow these steps:

---

## Step 1: Google Cloud Console

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Create a new project (or select existing)
   - Click "Select a project" > "New Project"
   - Name: "NoizyLab Email Intelligence"
   - Click "Create"

---

## Step 2: Enable Gmail API

1. In the project, go to **"APIs & Services"** > **"Library"**
2. Search for **"Gmail API"**
3. Click on **"Gmail API"**
4. Click **"Enable"**

---

## Step 3: Create OAuth 2.0 Credentials

1. Go to **"APIs & Services"** > **"Credentials"**
2. Click **"Create Credentials"** > **"OAuth client ID"**
3. If prompted, configure OAuth consent screen:
   - User Type: **External** (or Internal if using Google Workspace)
   - App name: **NoizyLab Email Intelligence**
   - User support email: Your email
   - Developer contact: Your email
   - Click **"Save and Continue"**
   - Scopes: Click **"Add or Remove Scopes"**
     - Search for: `gmail.readonly`
     - Check the box
     - Click **"Update"** > **"Save and Continue"**
   - Test users: Add your email
   - Click **"Save and Continue"** > **"Back to Dashboard"**

4. Create OAuth Client ID:
   - Application type: **"Desktop app"**
   - Name: **"NoizyLab Email Intelligence"**
   - Click **"Create"**

5. Download credentials:
   - Click **"Download JSON"**
   - Save the file

---

## Step 4: Install Credentials

1. Create config directory (if it doesn't exist):
   ```bash
   mkdir -p ~/NOIZYLAB/email-intelligence/config
   ```

2. Move the downloaded JSON file:
   ```bash
   mv ~/Downloads/client_secret_*.json ~/NOIZYLAB/email-intelligence/config/gmail_credentials.json
   ```

   Or copy it:
   ```bash
   cp /path/to/downloaded/credentials.json ~/NOIZYLAB/email-intelligence/config/gmail_credentials.json
   ```

---

## Step 5: Authenticate

1. Launch NoizyLab CORE:
   ```bash
   nz
   ```

2. Select option **2** (Inbox Scanner)

3. Browser will open automatically

4. Sign in with your Google account

5. Click **"Allow"** to grant permissions

6. Token will be saved automatically

---

## Verification

After setup, when you select "Inbox Scanner":
- ✅ Should show recent emails
- ✅ No error messages
- ✅ Gmail API working

---

## Troubleshooting

### "Gmail API not configured"
- Make sure `config/gmail_credentials.json` exists
- Check file permissions
- Verify JSON file is valid

### "Error fetching emails"
- Check internet connection
- Verify Gmail API is enabled in Google Cloud Console
- Try re-authenticating (delete `config/gmail_token.json` and try again)

### "Permission denied"
- Make sure you granted all requested permissions
- Check OAuth consent screen is configured
- Verify your email is in test users list

### Browser doesn't open
- Manually copy the URL from terminal
- Paste in browser
- Complete authentication
- Copy the code back to terminal

---

## File Structure

After setup, you should have:
```
config/
├── gmail_credentials.json  # OAuth credentials (from Google)
└── gmail_token.json        # Access token (auto-generated)
```

**Note**: `gmail_token.json` is created automatically after first authentication.

---

## Security Notes

- **Never commit** `gmail_credentials.json` or `gmail_token.json` to git
- Keep credentials secure
- Tokens auto-refresh when expired
- Revoke access in Google Account settings if needed

---

## Alternative: Use Without Gmail API

If you don't want to set up Gmail API:
- You can still use **Smart Composer** (option 1)
- You can still use **Data Vault** (option 3)
- Only **Inbox Scanner** (option 2) requires Gmail API

---

## Quick Reference

```bash
# Check if credentials exist
ls -la ~/NOIZYLAB/email-intelligence/config/gmail_credentials.json

# Setup helper
bash ~/NOIZYLAB/email-intelligence/setup-gmail-api.sh

# Launch app
nz
```

---

**Need Help?** The setup helper script will guide you through the process!

