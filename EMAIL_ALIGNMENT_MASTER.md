# 📧 NOIZYLAB EMAIL ALIGNMENT MASTER

## PRIMARY LOGIN ACCOUNTS

### 🥇 Microsoft 365 (PRIMARY)
- **Login:** rsplowman@outlook.com
- **Use For:** All Microsoft services, Office apps, Teams, OneDrive, Outlook
- **IMAP:** outlook.office365.com:993 (SSL/TLS)
- **SMTP:** smtp.office365.com:587 (STARTTLS)
- **Priority:** #1 - Primary account for all Microsoft ecosystem services

### 🥈 Apple/iCloud (SECONDARY)
- **Login:** rsplowman@icloud.com
- **Use For:** Apple devices, iCloud, Passkeys, Apple ID services
- **IMAP:** imap.mail.me.com:993 (SSL/TLS)
- **SMTP:** smtp.mail.me.com:587 (STARTTLS)
- **Priority:** #2 - Primary for Apple ecosystem and passkey authentication

### 🥉 Fish Music Inc (BUSINESS)
- **Primary:** rp@fishmusicinc.com
- **Secondary:** info@fishmusicinc.com
- **Use For:** Music business, professional communications
- **Forward To:** rsplowman@outlook.com
- **Priority:** #3 - Main business identity

### 🔧 NOIZYLAB (BUSINESS)
- **Accounts:**
  - rsp@noizylab.ca (Primary - Owner direct, Git commits)
  - help@noizylab.ca (Customer support)
  - hello@noizylab.ca (New customer contact)
- **Use For:** CPU repair business, customer support, development
- **Forward To:** rsplowman@outlook.com
- **Git Identity:** rsp@noizylab.ca
- **Priority:** #4 - Business operations and developer identity

---

## EMAIL FORWARDING CHAIN

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ALL BUSINESS EMAILS → rsplowman@outlook.com           │
│                                                         │
│  ✉️  rp@fishmusicinc.com      ──┐                      │
│  ✉️  info@fishmusicinc.com    ──┤                      │
│  ✉️  rsp@noizylab.ca          ──┼──►  📥 OUTLOOK INBOX │
│  ✉️  help@noizylab.ca         ──┤                      │
│  ✉️  hello@noizylab.ca        ──┘                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Forwarding Setup Instructions:

**For Custom Domains (fishmusicinc.com, noizylab.ca):**
1. Log into your email hosting control panel (cPanel, Google Workspace Admin, etc.)
2. Navigate to Email Forwarding or Email Routing
3. Create forwarding rules:
   - rp@fishmusicinc.com → rsplowman@outlook.com
   - info@fishmusicinc.com → rsplowman@outlook.com
   - rsp@noizylab.ca → rsplowman@outlook.com
   - help@noizylab.ca → rsplowman@outlook.com
   - hello@noizylab.ca → rsplowman@outlook.com

**Alternative: Cloudflare Email Routing**
- If domains are on Cloudflare, use their free Email Routing
- Dashboard → Email → Email Routing → Create Routes

---

## MICROSOFT 365 SERVER SETTINGS

### IMAP (Incoming Mail)
```
Server:     outlook.office365.com
Port:       993
Security:   SSL/TLS
Username:   rsplowman@outlook.com
Password:   [M365 Password or App Password]
```

### SMTP (Outgoing Mail)
```
Server:     smtp.office365.com
Port:       587
Security:   STARTTLS
Username:   rsplowman@outlook.com
Password:   [M365 Password or App Password]
Auth:       Required
```

### App Password Generation
If 2FA is enabled on Microsoft 365:
1. Visit: https://account.microsoft.com/security
2. Click "Advanced security options"
3. Under "App passwords", click "Create a new app password"
4. Name it "Email Client" or similar
5. Use generated password in email client settings

---

## APPLE iCLOUD SERVER SETTINGS

### IMAP (Incoming Mail)
```
Server:     imap.mail.me.com
Port:       993
Security:   SSL/TLS
Username:   rsplowman@icloud.com
Password:   [App-Specific Password - REQUIRED]
```

### SMTP (Outgoing Mail)
```
Server:     smtp.mail.me.com
Port:       587
Security:   STARTTLS
Username:   rsplowman@icloud.com
Password:   [App-Specific Password - REQUIRED]
Auth:       Required
```

### App-Specific Password Generation (REQUIRED)
iCloud REQUIRES app-specific passwords for email clients:
1. Visit: https://appleid.apple.com
2. Sign in with Apple ID
3. Security → App-Specific Passwords
4. Click "Generate password"
5. Label it "Email Client"
6. Copy the generated password (format: xxxx-xxxx-xxxx-xxxx)
7. Use this password in email client (not your Apple ID password)

---

## SPF RECORD CONFIGURATION

### Recommended SPF Record
```
v=spf1 include:spf.protection.outlook.com -all
```

**Why This Configuration:**
- Authorizes Microsoft 365 to send email on your behalf
- `-all` means strict policy (reject unauthorized senders)
- Protects against email spoofing
- Improves email deliverability

### DNS Setup (for custom domains)
```
Type:  TXT
Name:  @ (or your domain name)
Value: v=spf1 include:spf.protection.outlook.com -all
TTL:   3600 (or default)
```

### Verification
Test your SPF record:
```bash
dig TXT yourdomain.com
# or
nslookup -type=TXT yourdomain.com
```

Online tools:
- https://mxtoolbox.com/spf.aspx
- https://dmarcian.com/spf-survey/

---

## DKIM & DMARC SETUP

### DKIM (DomainKeys Identified Mail)
For Microsoft 365 domains:
1. Go to Microsoft 365 Admin Center
2. Settings → Domains → [Your Domain]
3. DNS Records → DKIM
4. Enable DKIM signing
5. Copy the CNAME records
6. Add to your DNS provider

### DMARC (Domain-based Message Authentication)
Recommended DMARC record:
```
Type:  TXT
Name:  _dmarc
Value: v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com; ruf=mailto:dmarc@yourdomain.com; fo=1
```

**Policy Options:**
- `p=none` - Monitor only (recommended for testing)
- `p=quarantine` - Send suspicious emails to spam
- `p=reject` - Reject suspicious emails (strictest)

---

## EMAIL CLIENT CONFIGURATION

### Priority Setup Order:
1. **Microsoft 365** (rsplowman@outlook.com) - Configure first
2. **Business emails** - Set up forwarding to M365
3. **iCloud** (rsplowman@icloud.com) - Configure for Apple services

### Recommended Email Clients:

**Windows:**
- Microsoft Outlook (native M365 support)
- Thunderbird (cross-platform, open source)

**macOS:**
- Apple Mail (native iCloud support)
- Microsoft Outlook
- Spark (modern interface)

**Mobile (iOS/Android):**
- Microsoft Outlook app (recommended)
- Native mail apps
- Spark Mobile

---

## SENDING AS DIFFERENT ADDRESSES

### In Microsoft Outlook:
1. File → Account Settings → Account Settings
2. Select your M365 account → Change
3. More Settings → Advanced → Add additional SMTP servers
4. Configure each business email as send-as address

### In Outlook Web (outlook.office365.com):
1. Settings → Mail → Compose and reply
2. Email signature → Add signature for each send-as address
3. Or use Outlook desktop for full send-as configuration

---

## GIT CONFIGURATION FOR DEVELOPERS

### Global Git Identity (Business)
```bash
git config --global user.name "Rob Plowman"
git config --global user.email "rsp@noizylab.ca"
```

### Per-Repository Override (if needed)
```bash
cd /path/to/repo
git config user.email "rsp@noizylab.ca"
git config user.name "Rob Plowman"
```

### GitHub Authentication
- **Login Email:** rsplowman@icloud.com (with Passkey)
- **Commit Email:** rsp@noizylab.ca (business identity)
- **Public Email:** Can be hidden or set to noreply address

---

## TROUBLESHOOTING

### Microsoft 365 Authentication Issues
**Problem:** Cannot connect or authenticate fails
**Solutions:**
1. Verify credentials: rsplowman@outlook.com
2. Check if 2FA is enabled → Use app password
3. Enable IMAP in M365 settings if disabled
4. Verify Modern Authentication is enabled
5. Check firewall/antivirus blocking ports 993/587

### iCloud Authentication Issues
**Problem:** Cannot connect with Apple ID password
**Solution:** 
- iCloud REQUIRES app-specific password
- Regular Apple ID password will NOT work
- Generate at: https://appleid.apple.com

### Email Not Forwarding
**Problem:** Business emails not arriving in Outlook inbox
**Checks:**
1. Verify forwarding rules are active in hosting control panel
2. Check spam/junk folder in Outlook
3. Verify SPF record is correct
4. Check email quotas aren't full
5. Test with a manual email send

### Send-As Not Working
**Problem:** Cannot send from business email addresses
**Solutions:**
1. Verify SMTP settings for each send-as address
2. Check business email passwords are correct
3. Ensure authentication is required
4. Verify business domain SPF includes M365

---

## SECURITY BEST PRACTICES

### ✅ DO:
- Use app passwords for email clients (M365 and iCloud)
- Enable 2FA/MFA on all accounts
- Use strong, unique passwords (password manager)
- Regularly review connected devices and apps
- Monitor email forwarding rules
- Keep SPF, DKIM, and DMARC records updated

### ❌ DON'T:
- Share passwords or app passwords
- Use SMS-only 2FA (use authenticator apps or passkeys)
- Ignore security alerts from Microsoft or Apple
- Click suspicious links in emails
- Forward to insecure email addresses
- Use weak passwords

---

## QUICK REFERENCE CARD

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 NOIZYLAB EMAIL HIERARCHY                  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                            ┃
┃  🥇 PRIMARY: rsplowman@outlook.com                        ┃
┃     └─ Microsoft 365, Office, Teams, OneDrive             ┃
┃                                                            ┃
┃  🥈 APPLE: rsplowman@icloud.com                           ┃
┃     └─ Apple devices, iCloud, Passkeys                    ┃
┃                                                            ┃
┃  🥉 BUSINESS: rp@fishmusicinc.com                         ┃
┃     ├─ info@fishmusicinc.com                              ┃
┃     └─ Music business communications                      ┃
┃                                                            ┃
┃  🔧 NOIZYLAB: rsp@noizylab.ca                             ┃
┃     ├─ help@noizylab.ca (support)                         ┃
┃     ├─ hello@noizylab.ca (contact)                        ┃
┃     └─ Git commits, development                           ┃
┃                                                            ┃
┃  📥 ALL ROUTE TO: rsplowman@outlook.com                   ┃
┃                                                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## SUCCESS CHECKLIST

Setup is complete when:

- [ ] rsplowman@outlook.com configured in email client
- [ ] rsplowman@icloud.com configured in email client
- [ ] All business emails forwarding to rsplowman@outlook.com
- [ ] Can send from any business email address
- [ ] SPF record updated: `v=spf1 include:spf.protection.outlook.com -all`
- [ ] DKIM enabled for custom domains (optional but recommended)
- [ ] DMARC record configured (optional but recommended)
- [ ] Email signatures set up for each send-as address
- [ ] Mobile devices configured with Microsoft Outlook app
- [ ] Git configured with rsp@noizylab.ca for commits
- [ ] All passwords stored securely in password manager
- [ ] App passwords generated for M365 and iCloud (if 2FA enabled)
- [ ] Forwarding rules tested and verified working
- [ ] Email filters/rules configured for organization

---

## SUPPORT RESOURCES

### Microsoft 365
- Admin Center: https://admin.microsoft.com
- Account Security: https://account.microsoft.com/security
- Support: https://support.microsoft.com

### Apple iCloud
- Apple ID Management: https://appleid.apple.com
- iCloud Settings: https://icloud.com/settings
- Support: https://support.apple.com

### Email Testing Tools
- SPF Check: https://mxtoolbox.com/spf.aspx
- DMARC Analyzer: https://dmarcian.com
- Email Header Analyzer: https://mxtoolbox.com/emailheaders.aspx
- Deliverability Test: https://www.mail-tester.com

---

**Last Updated:** 2025-12-07  
**Maintained by:** NOIZYLAB IT Department  
**Document Version:** 1.0

✅ **ALL SYSTEMS ALIGNED: Microsoft 365 Primary | Apple Secondary | Business Unified**
