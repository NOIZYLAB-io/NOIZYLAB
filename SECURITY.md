# Security Best Practices

This document outlines security best practices for the NOIZYLAB DNS & Email Management System.

## Table of Contents

1. [API Key Security](#api-key-security)
2. [Environment Variables](#environment-variables)
3. [DKIM Key Management](#dkim-key-management)
4. [DNS Security](#dns-security)
5. [Email Security](#email-security)
6. [Access Control](#access-control)
7. [Monitoring & Alerts](#monitoring--alerts)
8. [Incident Response](#incident-response)

## API Key Security

### GoDaddy API Keys

1. **Never commit API keys to version control**
   - Always use `.env` files (already in `.gitignore`)
   - Never hardcode credentials in source code
   - Review commits before pushing

2. **API Key Rotation**
   - Rotate API keys every 90 days minimum
   - Update `.env` file after rotation
   - Test configuration after rotation

3. **Access Permissions**
   - Use API keys with minimum required permissions
   - Create separate keys for development/production
   - Revoke unused or compromised keys immediately

4. **Storage**
   - Store API keys in secure password manager
   - Encrypt backups containing credentials
   - Never share API keys via email or chat

## Environment Variables

### Best Practices

1. **File Permissions**
   ```bash
   chmod 600 .env
   ```
   Only the owner can read/write the .env file

2. **Environment Separation**
   - Use separate `.env` files for:
     - `.env.development`
     - `.env.staging`
     - `.env.production`
   - Never copy production credentials to development

3. **Validation**
   - Verify all required variables are set
   - Use strong, unique passwords
   - Validate IP addresses and domains

## DKIM Key Management

### Generation

1. **Key Strength**
   - Use 2048-bit RSA keys minimum
   - Consider 4096-bit for enhanced security
   - Regenerate keys annually

2. **Private Key Security**
   - Never share private keys
   - Store private keys encrypted
   - Keep backups in secure location
   - Restrict file permissions:
     ```bash
     chmod 400 backups/dkim-private-*.pem
     ```

3. **Key Rotation**
   ```bash
   # Generate new keys
   npm run generate:dkim

   # Update DNS with new public key
   npm run dns:setup

   # Wait 48 hours for propagation

   # Remove old keys from DNS
   ```

### Storage Best Practices

- Store private keys offline when possible
- Use hardware security modules (HSM) for production
- Maintain encrypted backups
- Document key rotation procedures

## DNS Security

### Record Protection

1. **DNSSEC (Recommended)**
   - Enable DNSSEC in GoDaddy dashboard
   - Validates DNS record authenticity
   - Prevents DNS spoofing attacks

2. **Record Monitoring**
   - Regularly verify DNS records: `npm run dns:verify`
   - Enable GoDaddy change notifications
   - Monitor for unauthorized changes

3. **Backup Strategy**
   ```bash
   # Backup before changes
   npm run dns:backup

   # Make changes
   npm run dns:setup

   # Verify changes
   npm run dns:verify
   ```

4. **TTL Configuration**
   - Use lower TTL (600s) during changes
   - Increase TTL (3600s+) when stable
   - Balance between flexibility and caching

## Email Security

### SPF Configuration

Current SPF record:
```
v=spf1 a mx ip4:YOUR_IP ~all
```

Best Practices:
- Use `~all` (soft fail) during testing
- Switch to `-all` (hard fail) in production
- List all authorized mail servers
- Keep record under 255 characters

### DKIM Configuration

Best Practices:
- Use unique selector per mail server
- Rotate DKIM keys annually
- Monitor DKIM validation failures
- Test with mail-tester.com

### DMARC Policy

Current DMARC record:
```
v=DMARC1; p=quarantine; rua=mailto:dmarc@noizylab.ca
```

**Policy Progression:**
1. Start: `p=none` (monitoring only)
2. Testing: `p=quarantine` (current)
3. Production: `p=reject` (maximum security)

**Monitor DMARC Reports:**
- Check dmarc@noizylab.ca daily
- Analyze authentication failures
- Identify unauthorized senders
- Adjust policy based on results

## Access Control

### System Access

1. **Server Security**
   - Use SSH keys, not passwords
   - Disable root login
   - Enable firewall (UFW/iptables)
   - Keep system updated

2. **File Permissions**
   ```bash
   # Scripts should be executable by owner only
   chmod 700 scripts/*.js

   # Sensitive files read-only by owner
   chmod 400 .env backups/*.pem

   # Backups directory owner-only access
   chmod 700 backups/
   ```

3. **User Management**
   - Use separate accounts per person
   - Implement principle of least privilege
   - Review access quarterly
   - Revoke access immediately on termination

### GoDaddy Account

1. **Enable Two-Factor Authentication (2FA)**
   - Required for all users
   - Use authenticator app, not SMS
   - Store backup codes securely

2. **Account Security**
   - Use strong, unique password
   - Enable login alerts
   - Review account activity regularly
   - Whitelist IP addresses if possible

## Monitoring & Alerts

### DNS Monitoring

1. **Automated Checks**
   ```bash
   # Setup cron job to check daily
   0 9 * * * cd /path/to/NOIZYLAB && npm run dns:verify
   ```

2. **Alert on Changes**
   - Enable GoDaddy email notifications
   - Monitor DNS propagation
   - Track API usage
   - Log all DNS modifications

### Email Monitoring

1. **DMARC Reports**
   - Review daily
   - Track authentication pass/fail rates
   - Identify spoofing attempts
   - Maintain report archives

2. **Delivery Monitoring**
   - Track bounce rates
   - Monitor spam complaints
   - Check blacklist status
   - Test deliverability regularly

### Security Monitoring

1. **System Logs**
   - Review authentication logs
   - Monitor failed login attempts
   - Track API errors
   - Alert on anomalies

2. **Tools & Services**
   - MXToolbox Monitoring
   - Google Postmaster Tools
   - Blacklist monitoring
   - SSL/TLS certificate monitoring

## Incident Response

### Security Incident Procedure

1. **API Key Compromise**
   ```bash
   # Immediately revoke compromised key in GoDaddy
   # Generate new API key
   # Update .env file
   # Test configuration
   npm run dns:verify
   # Review recent API activity
   # Change related passwords
   ```

2. **DKIM Key Compromise**
   ```bash
   # Generate new DKIM keys
   npm run generate:dkim

   # Update DNS immediately
   npm run dns:setup

   # Monitor email authentication
   # Notify email recipients if needed
   ```

3. **DNS Hijacking**
   ```bash
   # Restore from backup
   npm run dns:restore

   # Verify all records
   npm run dns:verify

   # Enable DNSSEC
   # Review account access logs
   # Change all passwords
   # Enable additional security measures
   ```

4. **Unauthorized Access**
   - Disconnect affected systems
   - Review access logs
   - Revoke all API keys
   - Reset all passwords
   - Enable additional 2FA
   - Audit all configurations
   - Document incident

### Contact Information

**Emergency Contacts:**
- GoDaddy Support: 1-480-505-8877
- Domain Administrator: [YOUR CONTACT]
- Security Team: [YOUR CONTACT]

**Reporting:**
- Security issues: security@noizylab.ca
- Abuse reports: abuse@noizylab.ca

## Compliance & Standards

### Recommendations

1. **Regular Audits**
   - Quarterly security review
   - Annual penetration testing
   - Compliance verification
   - Documentation updates

2. **Documentation**
   - Maintain change log
   - Document incidents
   - Update procedures
   - Track configuration changes

3. **Training**
   - Security awareness training
   - Phishing prevention
   - Incident response drills
   - Tool usage training

## Security Checklist

Use this checklist for regular security reviews:

- [ ] API keys rotated within last 90 days
- [ ] DKIM keys rotated within last 365 days
- [ ] All .env files have chmod 600 permissions
- [ ] Backups are encrypted and tested
- [ ] GoDaddy 2FA is enabled
- [ ] DNS records verified within last week
- [ ] DMARC reports reviewed
- [ ] No unauthorized DNS changes detected
- [ ] System packages updated
- [ ] Access list reviewed and current
- [ ] Monitoring alerts functioning
- [ ] Backup restoration tested
- [ ] Incident response plan updated
- [ ] Security documentation current

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CIS Controls](https://www.cisecurity.org/controls)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [GoDaddy Security Best Practices](https://www.godaddy.com/security)

## Updates

This document should be reviewed and updated:
- Quarterly at minimum
- After security incidents
- When adding new features
- When threats evolve

Last Updated: 2025-11-22
