
# iOS Email Setup Instructions

## Quick Setup (Recommended: Gmail App)

### Option 1: Gmail App (Easiest)
1. Download Gmail app from App Store
2. Sign in with: rspplowman@gmail.com
3. Add accounts:
   - Go to Settings → Add Account
   - Add each email address
   - Use Gmail for all (if using Google Workspace)

### Option 2: iOS Mail App (Native)

#### For Gmail (rspplowman@gmail.com):
1. Settings → Mail → Accounts → Add Account
2. Select "Google"
3. Enter email and password
4. Enable Mail, Contacts, Calendars
5. Use App Password (not regular password)

#### For NoizyLab emails:
1. Settings → Mail → Accounts → Add Account
2. Select "Other"
3. Enter:
   - Email: your@noizylab.ca
   - Password: App Password
   - IMAP Server: imap.gmail.com
   - SMTP Server: smtp.gmail.com
   - Port: 993 (IMAP), 587 (SMTP)
   - SSL: Enabled

#### For Fish Music emails:
Same as NoizyLab, but use fishmusicinc.com addresses

## App Passwords Setup

### Gmail App Passwords:
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Generate App Password
4. Use this password in iOS Mail settings

## Xcode Setup (For Development)

### 1. Install Xcode
```bash
xcode-select --install
```

### 2. Configure Signing
- Open Xcode
- Preferences → Accounts
- Add Apple ID
- Select team for signing

### 3. Device Setup
- Connect iOS device
- Trust computer on device
- Enable Developer Mode in Settings

## Automated Setup Script

Run the setup script:
```bash
cd ~/NOIZYLAB/email-intelligence
python3 setup-ios-emails.py
```

This generates configuration files you can use.
