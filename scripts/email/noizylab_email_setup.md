# noizylab.ca Email Setup

## Email Accounts
- **rsp@noizylab.ca**
- **help@noizylab.ca**

## Email Server Settings (Common Configurations)

### Option 1: Google Workspace (if using Gmail for Business)
If noizylab.ca uses Google Workspace:
- **IMAP Server:** imap.gmail.com (Port 993, SSL/TLS)
- **SMTP Server:** smtp.gmail.com (Port 587, STARTTLS)
- **Username:** rsp@noizylab.ca or help@noizylab.ca
- **Password:** Your Google Workspace password

### Option 2: Microsoft 365 (if using Outlook)
If noizylab.ca uses Microsoft 365:
- **IMAP Server:** outlook.office365.com (Port 993, SSL/TLS)
- **SMTP Server:** smtp.office365.com (Port 587, STARTTLS)
- **Username:** rsp@noizylab.ca or help@noizylab.ca
- **Password:** Your Microsoft 365 password

### Option 3: cPanel / Standard Web Hosting
If using standard web hosting (most common):
- **IMAP Server:** mail.noizylab.ca or imap.noizylab.ca (Port 993, SSL/TLS)
- **SMTP Server:** mail.noizylab.ca or smtp.noizylab.ca (Port 587, STARTTLS)
- **Username:** rsp@noizylab.ca or help@noizylab.ca (or sometimes just "rsp" or "help")
- **Password:** Your email account password

### Option 4: Zoho Mail
If using Zoho:
- **IMAP Server:** imap.zoho.com (Port 993, SSL/TLS)
- **SMTP Server:** smtp.zoho.com (Port 587, STARTTLS)
- **Username:** rsp@noizylab.ca or help@noizylab.ca
- **Password:** Your Zoho password

## Finding Your Exact Settings

1. **Check with your web hosting provider** or IT administrator
2. **Check your hosting control panel** (cPanel, Plesk, etc.)
3. **Check your email provider's documentation:**
   - Google Workspace: admin.google.com
   - Microsoft 365: admin.microsoft.com
   - cPanel: Check your hosting control panel

## Adding to Mac Mail

1. **Mail → Settings → Accounts**
2. Click **"+"** button
3. Select **"Other Mail Account"**
4. Enter:
   - **Name:** Your name
   - **Email:** rsp@noizylab.ca or help@noizylab.ca
   - **Password:** Your email password
5. If auto-detect fails, click **"Configure Manually"**
6. Enter the IMAP/SMTP settings from above

## Adding to Gmail

1. **Gmail → Settings → Accounts and Import**
2. Under **"Check mail from other accounts"**, click **"Add a mail account"**
3. Enter: rsp@noizylab.ca or help@noizylab.ca
4. Use the IMAP settings from above

## Verification Email to rp@fishmusicinc.com

To check verification emails sent to **rp@fishmusicinc.com**:

1. **Access the email account:**
   - Log into the email client where rp@fishmusicinc.com is configured
   - Or access via webmail (check with your email provider)

2. **Check spam/junk folder** - verification emails sometimes go there

3. **Common webmail URLs:**
   - If using cPanel: yourdomain.com/webmail
   - If using Google Workspace: mail.google.com
   - If using Microsoft 365: outlook.office365.com

4. **If using Mac Mail:**
   - Open Mail app
   - Check the inbox for rp@fishmusicinc.com
   - Look in Spam folder if not in inbox

5. **Search for verification:**
   - Search for "verification" or "verify" in the email
   - Check emails from Google, Microsoft, or your hosting provider

## Quick Setup in IT Genius

Run IT Genius and use:
- **Email Setup → Option 5** (Custom Domain Email)
- Enter: rsp@noizylab.ca or help@noizylab.ca
- Follow the prompts to enter server settings

