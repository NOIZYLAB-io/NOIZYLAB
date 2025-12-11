# Email Security Setup - Complete Guide

## Your Current SPF Record

```
v=spf1 include:spf.protection.outlook.com -all
```

**Status**: ✅ Correctly configured for Microsoft 365/Outlook

## Quick Setup

### 1. SPF Record (You Have This)
```
Type: TXT
Name: @
Value: v=spf1 include:spf.protection.outlook.com -all
```

### 2. DKIM (Recommended)
Get from Microsoft 365 Admin Center:
- Go to Microsoft 365 Admin Center
- Settings → Domains → Your Domain
- DNS Records → DKIM
- Copy the selector and public key

### 3. DMARC (Recommended)
```
Type: TXT
Name: _dmarc
Value: v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com
```

## Tools Available

### SPF Manager
```bash
cd ~/NOIZYLAB/email-intelligence
python3 spf-manager.py
```

### DNS Security Manager
```bash
python3 dns-security-manager.py
```

## Verification Commands

```bash
# Check SPF
dig TXT yourdomain.com | grep spf

# Check DKIM
dig TXT selector._domainkey.yourdomain.com

# Check DMARC
dig TXT _dmarc.yourdomain.com
```

## Next Steps

1. ✅ SPF - Already configured
2. ⏳ Add DKIM records
3. ⏳ Add DMARC policy
4. ⏳ Monitor DMARC reports

---

**Your email security is being managed by NoizyLab Email Intelligence!** 🚀

