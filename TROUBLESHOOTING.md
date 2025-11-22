# Troubleshooting Guide

Common issues and solutions for NOIZYLAB DNS & Email Management System.

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [API & Authentication](#api--authentication)
3. [DNS Configuration](#dns-configuration)
4. [DKIM Setup](#dkim-setup)
5. [Email Sending](#email-sending)
6. [DNS Propagation](#dns-propagation)
7. [Debugging Tools](#debugging-tools)

## Installation Issues

### npm install fails

**Symptoms:**
```
Error: Cannot find module 'node-fetch'
npm ERR! code ELIFECYCLE
```

**Solutions:**

1. **Check Node.js version:**
   ```bash
   node --version  # Should be 18.0.0 or higher
   ```

2. **Clear npm cache:**
   ```bash
   npm cache clean --force
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Use specific npm version:**
   ```bash
   npm install -g npm@latest
   ```

### Permission denied errors

**Symptoms:**
```
Error: EACCES: permission denied
```

**Solutions:**

1. **Fix npm permissions:**
   ```bash
   sudo chown -R $USER:$USER ~/.npm
   sudo chown -R $USER:$USER .
   ```

2. **Don't use sudo with npm:**
   ```bash
   # Wrong
   sudo npm install

   # Right
   npm install
   ```

## API & Authentication

### GoDaddy API authentication failed

**Symptoms:**
```
❌ API Error: 401 Unauthorized
Error: GoDaddy API credentials not configured
```

**Solutions:**

1. **Verify credentials in .env:**
   ```bash
   cat .env | grep GODADDY
   ```

2. **Check API key format:**
   - Should be alphanumeric string
   - No spaces or special characters
   - Format: `GODADDY_API_KEY=xxxxxxxxxxxxx`

3. **Verify API key is Production:**
   - Go to https://developer.godaddy.com/keys
   - Ensure key environment is "Production"
   - Test keys are not supported

4. **Regenerate API keys:**
   - Delete old keys in GoDaddy dashboard
   - Create new Production keys
   - Update .env file

### API rate limiting

**Symptoms:**
```
❌ API Error: 429 Too Many Requests
```

**Solutions:**

1. **Wait before retrying:**
   - GoDaddy limits: 60 requests/minute
   - Wait 60 seconds between attempts

2. **Reduce API calls:**
   - Don't run multiple scripts simultaneously
   - Use `--verify` instead of `--setup` for checking

## DNS Configuration

### DNS records not being created

**Symptoms:**
```
✅ DNS email records updated
But records don't appear in GoDaddy dashboard
```

**Solutions:**

1. **Verify API response:**
   ```bash
   node godaddy-dns-manager.js --list
   ```

2. **Check domain ownership:**
   - Verify domain is in your GoDaddy account
   - Check domain is not locked
   - Ensure domain is active (not expired)

3. **Try manual record creation:**
   - Test creating one record in GoDaddy dashboard
   - If manual creation works, API keys may need permissions

### DNS verification fails

**Symptoms:**
```
❌ MX Record:      MISSING
❌ SPF Record:     MISSING
```

**Solutions:**

1. **Wait for propagation:**
   ```bash
   # Check again in 10 minutes
   sleep 600 && npm run dns:verify
   ```

2. **Verify records exist:**
   ```bash
   npm run dns:list
   ```

3. **Check GoDaddy dashboard:**
   - Log in to GoDaddy
   - Go to DNS Management
   - Verify records are present

4. **Re-run setup:**
   ```bash
   npm run dns:backup
   npm run dns:setup
   ```

### Wrong DNS values

**Symptoms:**
```
Records exist but have incorrect values
```

**Solutions:**

1. **Check environment variables:**
   ```bash
   cat .env
   ```

2. **Verify configuration:**
   - DOMAIN should be `noizylab.ca`
   - MAIL_SERVER_IP should be valid IP
   - No typos in .env file

3. **Restore and reconfigure:**
   ```bash
   npm run dns:restore
   # Fix .env file
   npm run dns:setup
   ```

## DKIM Setup

### DKIM key generation fails

**Symptoms:**
```
Error: Cannot find module 'crypto'
```

**Solutions:**

1. **Use Node.js 18+:**
   ```bash
   node --version
   # Should be 18.0.0 or higher
   ```

2. **Reinstall Node.js:**
   - Download from https://nodejs.org
   - Install latest LTS version

### DKIM record too long

**Symptoms:**
```
GoDaddy error: TXT record value too long
```

**Solutions:**

1. **Split DKIM record:**
   - Some DNS providers require split records
   - GoDaddy usually accepts full records
   - Try shorter 1024-bit key (less secure)

2. **Verify record format:**
   ```bash
   # Check DKIM_PUBLIC_KEY length
   echo $DKIM_PUBLIC_KEY | wc -c
   ```

### DKIM verification fails

**Symptoms:**
```
❌ DKIM Record:    MISSING
```

**Solutions:**

1. **Check DNS propagation:**
   ```bash
   npm run dns:check-propagation
   ```

2. **Verify DKIM record name:**
   ```bash
   # Should be: selector1._domainkey.noizylab.ca
   dig TXT selector1._domainkey.noizylab.ca
   ```

3. **Test DKIM online:**
   - https://mxtoolbox.com/dkim.aspx
   - Enter domain and selector
   - Check for errors

## Email Sending

### SMTP connection failed

**Symptoms:**
```
❌ SMTP connection failed: Connection timeout
```

**Solutions:**

1. **Check SMTP credentials:**
   ```bash
   cat .env | grep SMTP
   ```

2. **Verify SMTP server:**
   - Test server: `telnet smtp.example.com 587`
   - Check server is running
   - Verify port is correct (587 for TLS, 465 for SSL)

3. **Check firewall:**
   ```bash
   # Allow outbound SMTP
   sudo ufw allow out 587/tcp
   sudo ufw allow out 465/tcp
   ```

### Email authentication fails

**Symptoms:**
```
Email sends but fails SPF/DKIM/DMARC checks
```

**Solutions:**

1. **Verify DNS records:**
   ```bash
   npm run dns:verify
   ```

2. **Check DNS propagation:**
   ```bash
   npm run dns:check-propagation
   ```

3. **Test email headers:**
   - Send test email
   - View full headers
   - Look for Authentication-Results

4. **Use mail testing tools:**
   - https://mail-tester.com
   - https://mxtoolbox.com/diagnostic.aspx

### DKIM signature invalid

**Symptoms:**
```
DKIM-Signature: header.i=@noizylab.ca
dkim=fail (signature verification failed)
```

**Solutions:**

1. **Verify private key matches public key:**
   ```bash
   npm run generate:dkim
   npm run dns:setup
   ```

2. **Check DKIM configuration:**
   - Ensure DKIM_PRIVATE_KEY is set correctly
   - Verify no extra spaces/newlines
   - Format should be PEM with `\n`

3. **Test DKIM signing:**
   ```bash
   npm run test:email
   # Check email headers for DKIM-Signature
   ```

## DNS Propagation

### Propagation taking too long

**Symptoms:**
```
⚠️ Partial propagation after 48 hours
```

**Solutions:**

1. **Check TTL values:**
   ```bash
   dig noizylab.ca | grep TTL
   ```

2. **Flush DNS cache:**
   ```bash
   # Linux
   sudo systemd-resolve --flush-caches

   # macOS
   sudo dscacheutil -flushcache

   # Windows
   ipconfig /flushdns
   ```

3. **Use different DNS servers:**
   - Test with 8.8.8.8 (Google)
   - Test with 1.1.1.1 (Cloudflare)
   - Check GoDaddy nameservers directly

### Propagation not starting

**Symptoms:**
```
All DNS servers show old/missing records
```

**Solutions:**

1. **Verify records in GoDaddy:**
   - Log in to dashboard
   - Check DNS Management
   - Ensure records saved

2. **Check nameservers:**
   ```bash
   dig NS noizylab.ca
   ```

3. **Force propagation:**
   - Delete and recreate records
   - Lower TTL to 300 seconds
   - Wait 5 minutes and check

## Debugging Tools

### Check DNS records

```bash
# Check MX records
dig MX noizylab.ca

# Check A record
dig A mail.noizylab.ca

# Check TXT records (SPF, DMARC)
dig TXT noizylab.ca

# Check DKIM
dig TXT selector1._domainkey.noizylab.ca

# Check DMARC
dig TXT _dmarc.noizylab.ca
```

### Test email authentication

```bash
# Test SPF
dig TXT noizylab.ca +short | grep spf

# Test DKIM
openssl rsa -in backups/dkim-private-*.pem -pubout

# Send test email
npm run test:email
```

### Validate configuration

```bash
# Show all environment variables
cat .env

# List all DNS records
npm run dns:list

# Verify DNS setup
npm run dns:verify

# Check propagation
npm run dns:check-propagation
```

### Enable verbose logging

Modify scripts to add debug logging:

```javascript
// In godaddy-dns-manager.js
console.log("DEBUG: API Request:", url);
console.log("DEBUG: Request Body:", body);
console.log("DEBUG: Response:", await response.text());
```

## Common Error Messages

### "Domain not found"

**Cause:** Domain not in your GoDaddy account

**Fix:** Verify domain ownership, check API credentials

### "Invalid DNS record"

**Cause:** Record format incorrect

**Fix:** Check record syntax, verify IP addresses

### "Rate limit exceeded"

**Cause:** Too many API requests

**Fix:** Wait 60 seconds, reduce request frequency

### "DNS propagation timeout"

**Cause:** Changes taking longer than expected

**Fix:** Wait 24-48 hours, check nameservers

## Getting Help

If you're still stuck:

1. **Check logs:**
   ```bash
   npm run dns:list > debug.log 2>&1
   ```

2. **Test with online tools:**
   - https://mxtoolbox.com
   - https://dnschecker.org
   - https://mail-tester.com

3. **Review documentation:**
   - README.md
   - SECURITY.md
   - QUICKSTART.md

4. **Contact support:**
   - GoDaddy: 1-480-505-8877
   - Check GoDaddy status: https://status.godaddy.com

## Preventive Measures

1. **Always backup before changes:**
   ```bash
   npm run dns:backup
   ```

2. **Test in staging first:**
   - Use test domain
   - Verify before production

3. **Monitor regularly:**
   - Weekly verification
   - Check DMARC reports
   - Review authentication rates

4. **Keep documentation updated:**
   - Document custom changes
   - Track configuration versions
   - Maintain change log
