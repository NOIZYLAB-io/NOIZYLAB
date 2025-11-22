# NOIZYLAB DNS & Email Management System

Complete GoDaddy DNS management and email configuration system for `noizylab.ca`.

## Features

- Automated DNS record management via GoDaddy API
- Complete email authentication setup (SPF, DKIM, DMARC)
- Interactive setup wizard
- DNS verification and testing
- DKIM key generation
- Backup and restore functionality
- Email sending test suite

## Prerequisites

- Node.js 18.0.0 or higher
- GoDaddy account with API access
- Domain: `noizylab.ca` (configured in GoDaddy)

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Credentials

Run the interactive setup wizard:

```bash
npm run setup:wizard
```

Or manually copy and configure:

```bash
cp .env.example .env
# Edit .env with your credentials
```

### 3. Generate DKIM Keys

```bash
npm run generate:dkim
```

This will generate a new DKIM key pair and automatically update your `.env` file.

### 4. Setup DNS Records

```bash
npm run dns:setup
```

This configures all email DNS records:
- MX record (mail routing)
- SPF record (sender authentication)
- DKIM record (email signing)
- DMARC record (email policy)
- A record (mail server)

### 5. Verify Configuration

```bash
npm run dns:verify
```

### 6. Test Email Sending

```bash
npm run test:email
```

## Available Commands

| Command | Description |
|---------|-------------|
| `npm start` | Show help and status |
| `npm run setup:wizard` | Interactive configuration wizard |
| `npm run generate:dkim` | Generate new DKIM key pair |
| `npm run dns:setup` | Configure all DNS records |
| `npm run dns:verify` | Verify DNS configuration |
| `npm run dns:list` | List all current DNS records |
| `npm run dns:backup` | Backup current DNS configuration |
| `npm run dns:restore` | Restore from backup |
| `npm run dns:check-propagation` | Check DNS propagation status |
| `npm run test:email` | Send test email |

## Configuration

### Required Environment Variables

```bash
# GoDaddy API Credentials
# Get from: https://developer.godaddy.com/keys
GODADDY_API_KEY=your_api_key_here
GODADDY_API_SECRET=your_api_secret_here

# Domain Configuration
DOMAIN=noizylab.ca

# Mail Server Configuration
MAIL_SERVER_IP=your_mail_server_ip

# DKIM Configuration
DKIM_SELECTOR=selector1
DKIM_PUBLIC_KEY=your_public_key_here
DKIM_PRIVATE_KEY=your_private_key_here

# Email Test Configuration (optional)
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_email@noizylab.ca
SMTP_PASS=your_smtp_password
TEST_EMAIL_TO=test@example.com
```

## DNS Records Explained

### MX Record
Routes incoming email to your mail server.
```
Type: MX
Name: @
Data: mail.noizylab.ca
Priority: 10
```

### SPF Record
Specifies which servers can send email on your domain's behalf.
```
Type: TXT
Name: @
Data: v=spf1 a mx ip4:YOUR_IP ~all
```

### DKIM Record
Adds a digital signature to your emails for authentication.
```
Type: TXT
Name: selector1._domainkey
Data: v=DKIM1; k=rsa; p=YOUR_PUBLIC_KEY
```

### DMARC Record
Defines email authentication policy and reporting.
```
Type: TXT
Name: _dmarc
Data: v=DMARC1; p=quarantine; rua=mailto:dmarc@noizylab.ca
```

### A Record (Mail Server)
Points mail subdomain to your server's IP.
```
Type: A
Name: mail
Data: YOUR_MAIL_SERVER_IP
```

## DNS Propagation

After making DNS changes, allow 24-48 hours for full propagation. Check status:

```bash
npm run dns:check-propagation
```

Or manually check:
- https://dnschecker.org
- https://mxtoolbox.com

## Troubleshooting

### API Authentication Errors

1. Verify your GoDaddy API credentials
2. Ensure API key has proper permissions
3. Check that the domain is in your GoDaddy account

### DNS Not Updating

1. Check API response for errors
2. Verify DNS record format
3. Wait for propagation (up to 48 hours)
4. Clear DNS cache: `npm run dns:clear-cache`

### Email Not Working

1. Verify all DNS records: `npm run dns:verify`
2. Check DNS propagation
3. Test email sending: `npm run test:email`
4. Check mail server logs
5. Use online tools:
   - https://mxtoolbox.com/SuperTool.aspx
   - https://www.mail-tester.com

## Security Best Practices

1. **Never commit `.env` file** - It contains sensitive credentials
2. **Rotate API keys regularly** - Every 90 days recommended
3. **Use environment-specific configs** - Separate dev/staging/production
4. **Enable 2FA on GoDaddy account**
5. **Monitor DMARC reports** - Check dmarc@noizylab.ca regularly
6. **Keep dependencies updated** - Run `npm audit` regularly

## File Structure

```
NOIZYLAB/
├── .env.example              # Environment template
├── .gitignore               # Git ignore rules
├── package.json             # Dependencies and scripts
├── README.md                # This file
├── godaddy-dns-manager.js   # Main DNS management script
├── scripts/
│   ├── setup-wizard.js      # Interactive setup
│   ├── generate-dkim.js     # DKIM key generation
│   ├── backup-dns.js        # DNS backup utility
│   ├── restore-dns.js       # DNS restore utility
│   ├── check-propagation.js # Propagation checker
│   └── test-email.js        # Email testing tool
├── backups/                 # DNS backups (auto-created)
└── CODE_MASTER/             # Documentation
    └── NOIZYLAB_EMAIL_SYSTEM_COMPLETE.md
```

## Advanced Usage

### Backup Before Changes

Always backup before making DNS changes:

```bash
npm run dns:backup
npm run dns:setup
```

### Restore from Backup

If something goes wrong:

```bash
npm run dns:restore
```

### Custom DNS Records

Edit `godaddy-dns-manager.js` to add custom records:

```javascript
async function setCustomRecord() {
  const record = [{
    type: "A",
    name: "subdomain",
    data: "192.168.1.1",
    ttl: 600
  }];
  await api("/records/A/subdomain", "PUT", record);
}
```

## Support & Resources

- [GoDaddy API Documentation](https://developer.godaddy.com/doc)
- [SPF Record Syntax](http://www.open-spf.org/SPF_Record_Syntax/)
- [DKIM Explained](https://dkim.org/)
- [DMARC Guide](https://dmarc.org/)

## License

Proprietary - NOIZYLAB 2025

## Changelog

### v1.0.0 (2025-11-22)
- Initial release
- GoDaddy DNS management
- Complete email authentication setup
- Interactive setup wizard
- DKIM key generation
- Backup/restore functionality
- DNS propagation checking
