# Quick Start Guide

Get your NOIZYLAB DNS & Email system up and running in 5 minutes.

## Prerequisites

- Node.js 18+ installed
- GoDaddy account with API access
- Domain `noizylab.ca` in your GoDaddy account
- Mail server (IP address required)

## Step-by-Step Setup

### Step 1: Install Dependencies (1 minute)

```bash
npm install
```

### Step 2: Get GoDaddy API Credentials (2 minutes)

1. Go to https://developer.godaddy.com/keys
2. Log in to your GoDaddy account
3. Click "Create New API Key"
4. Choose "Production" environment
5. Copy your API Key and Secret

### Step 3: Run Setup Wizard (2 minutes)

```bash
npm run setup:wizard
```

Answer the prompts:
- Enter your GoDaddy API credentials
- Confirm domain: `noizylab.ca`
- Enter your mail server IP
- Generate DKIM keys: `yes`
- Configure email testing (optional)

### Step 4: Configure DNS Records (30 seconds)

```bash
npm run dns:setup
```

This will create:
- MX record (mail routing)
- SPF record (sender verification)
- DKIM record (email signing)
- DMARC record (email policy)
- A record (mail server)

### Step 5: Verify Setup (30 seconds)

```bash
npm run dns:verify
```

Expected output:
```
✅ MX Record:      OK
✅ SPF Record:     OK
✅ DKIM Record:    OK
✅ DMARC Record:   OK
✅ Mail A Record:  OK
```

## Done!

Your DNS and email authentication is now configured!

## Next Steps

### Wait for DNS Propagation

DNS changes take 24-48 hours to propagate globally.

Check propagation status:
```bash
npm run dns:check-propagation
```

### Test Email Sending

After DNS propagates, test email:
```bash
npm run test:email
```

### Regular Maintenance

Create backups before making changes:
```bash
npm run dns:backup
```

## Troubleshooting

### Issue: API Authentication Failed

**Solution:**
1. Verify API credentials in `.env`
2. Check API key is for "Production" environment
3. Ensure domain is in your GoDaddy account

### Issue: DNS Records Not Updating

**Solution:**
1. Check GoDaddy dashboard manually
2. Verify API key has proper permissions
3. Wait 10 minutes and try again

### Issue: Email Test Failed

**Solution:**
1. Verify SMTP credentials in `.env`
2. Check DNS records are propagated
3. Ensure mail server is running
4. Check firewall allows SMTP traffic

## Need Help?

- Full documentation: `README.md`
- Security guide: `SECURITY.md`
- Check DNS: `npm run dns:list`
- Verify config: `npm run dns:verify`

## Common Commands

```bash
# Show help
npm start

# List all DNS records
npm run dns:list

# Backup DNS
npm run dns:backup

# Restore DNS
npm run dns:restore

# Check propagation
npm run dns:check-propagation

# Test email
npm run test:email
```

## Success Checklist

- [x] npm install completed
- [x] GoDaddy API credentials configured
- [x] DKIM keys generated
- [x] DNS records created
- [x] DNS verification passed
- [ ] DNS propagated (wait 24-48 hours)
- [ ] Email test successful

## Important Notes

1. **Never commit `.env` file** - Contains sensitive credentials
2. **Backup before changes** - Always run `npm run dns:backup`
3. **Wait for propagation** - DNS changes take time
4. **Monitor DMARC reports** - Check dmarc@noizylab.ca

## What's Next?

1. **Monitor DNS Propagation**
   - Check every few hours
   - Full propagation: 24-48 hours

2. **Configure Mail Server**
   - Install mail server software
   - Configure DKIM signing
   - Set up mail aliases

3. **Test Email Delivery**
   - Send test emails
   - Check spam score: https://mail-tester.com
   - Verify DKIM/SPF/DMARC pass

4. **Setup Monitoring**
   - Enable DMARC reports
   - Monitor delivery rates
   - Track authentication failures

Congratulations! Your email system is configured! 🎉
