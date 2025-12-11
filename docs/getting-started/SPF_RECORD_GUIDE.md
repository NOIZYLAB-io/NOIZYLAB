# SPF Record Guide

## Recommended SPF Records

### ✅ Microsoft 365 Only (Primary - Recommended)
```
v=spf1 include:spf.protection.outlook.com -all
```

**Use this if:** You only send emails from Microsoft 365/Outlook

### ⚠️ Microsoft 365 + GoDaddy (Hybrid - Only if needed)
```
v=spf1 include:spf.protection.outlook.com include:secureserver.net -all
```

**Use this if:** You actually send emails from both Microsoft 365 AND GoDaddy

## What This Means

- **`v=spf1`** - SPF version 1
- **`include:spf.protection.outlook.com`** - Include Microsoft/Outlook's SPF records
- **`include:secureserver.net`** - Include GoDaddy's SPF records (only if needed)
- **`-all`** - **Strict policy**: Reject all emails from sources not listed above

## SPF Qualifiers

| Qualifier | Meaning | Action |
|-----------|---------|--------|
| `-all` | Fail | **Reject** emails from unauthorized sources (Strict) |
| `~all` | SoftFail | **Quarantine** emails from unauthorized sources |
| `?all` | Neutral | **Accept** but mark as neutral |
| `+all` | Pass | **Accept** all (Not recommended) |

## Recommendation

✅ **Use Microsoft 365 Only** - Keep it simple!
- One provider = simpler management
- Better security
- Easier troubleshooting
- Less chance of errors

⚠️ **Only add GoDaddy if:**
- You actually send emails from GoDaddy servers
- You have verified GoDaddy email sending is needed
- You understand the implications

**Best Practice:** Start with Microsoft 365 only. Add GoDaddy only if you encounter delivery issues from GoDaddy.

## Common SPF Records

### Microsoft 365 / Outlook
```
v=spf1 include:spf.protection.outlook.com -all
```

### Google Workspace
```
v=spf1 include:_spf.google.com ~all
```

### Combined (Microsoft + Google)
```
v=spf1 include:spf.protection.outlook.com include:_spf.google.com -all
```

### With Custom IPs
```
v=spf1 include:spf.protection.outlook.com ip4:1.2.3.4 ip4:5.6.7.8 -all
```

## DNS Setup

Add this as a **TXT record** in your DNS:

- **Name/Host**: `@` (or your domain name)
- **Type**: `TXT`
- **Value**: `v=spf1 include:spf.protection.outlook.com -all`
- **TTL**: `3600` (or default)

## Verification

### Check SPF Record
```bash
dig TXT example.com
# or
nslookup -type=TXT example.com
```

### Online Tools
- https://mxtoolbox.com/spf.aspx
- https://www.spf-record.com/

## Best Practices

1. ✅ Use `-all` for strict security
2. ✅ Keep SPF record under 255 characters
3. ✅ Include all email providers you use
4. ✅ Test before deploying
5. ✅ Monitor DMARC reports

## Tools

### SPF Manager
```bash
cd ~/NOIZYLAB/email-intelligence
python3 spf-manager.py
```

### DNS Security Manager
```bash
python3 dns-security-manager.py
```

## Related Records

### DKIM
Add DKIM for email signing:
```
selector._domainkey.example.com TXT "v=DKIM1; k=rsa; p=..."
```

### DMARC
Add DMARC for policy enforcement:
```
_dmarc.example.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"
```

## Complete Email Security Setup

1. **SPF** ✅ (You have this)
2. **DKIM** - Add signing
3. **DMARC** - Add policy
4. **BIMI** - Optional branding

---

**Your SPF record is correctly configured for Microsoft 365/Outlook!** ✅

