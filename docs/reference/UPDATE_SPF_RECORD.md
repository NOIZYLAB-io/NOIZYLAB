# ⚠️ IMPORTANT: Update Existing SPF Record

## Current Status

Your domain **noizyfish.com** already has an SPF record:
```
v=spf1 include:secureserver.net -all
```

This is **GoDaddy-only**. You need to **UPDATE** it to include Microsoft 365.

## ⚠️ CRITICAL: Edit, Don't Add!

**You can only have ONE SPF record per domain.**

- ❌ **DON'T** add a new SPF record
- ✅ **DO** edit the existing SPF record

## Update Steps for GoDaddy

### 1. Access GoDaddy DNS
Go to: https://dcc.godaddy.com/control/portfolio/noizyfish.com/settings

### 2. Find Existing SPF Record
- Look for the TXT record containing `v=spf1`
- It should show: `v=spf1 include:secureserver.net -all`

### 3. Edit the Record
- Click **Edit** (pencil icon) on that TXT record
- **DO NOT** click "Add Record"

### 4. Update the Value

#### Option A: Microsoft 365 Only (Recommended)
Replace the value with:
```
v=spf1 include:spf.protection.outlook.com -all
```

#### Option B: Microsoft 365 + GoDaddy (Hybrid)
Replace the value with:
```
v=spf1 include:spf.protection.outlook.com include:secureserver.net -all
```

### 5. Save
- Click **Save**
- Wait 5-15 minutes for DNS propagation

## What to Change

**Current (GoDaddy only):**
```
v=spf1 include:secureserver.net -all
```

**New (Microsoft 365 only - Recommended):**
```
v=spf1 include:spf.protection.outlook.com -all
```

**New (Microsoft 365 + GoDaddy - Hybrid):**
```
v=spf1 include:spf.protection.outlook.com include:secureserver.net -all
```

## Recommendation

Since you're using Microsoft 365, use **Option A** (Microsoft 365 only):
```
v=spf1 include:spf.protection.outlook.com -all
```

Only use the hybrid version if you actually send emails from GoDaddy servers too.

## Verification

After updating, wait 15 minutes, then verify:

```bash
dig TXT noizyfish.com | grep spf
```

Expected output:
```
"v=spf1 include:spf.protection.outlook.com -all"
```

## Quick Reference

**Domain**: noizyfish.com  
**Action**: **EDIT** existing SPF record (don't add new)  
**New Value**: `v=spf1 include:spf.protection.outlook.com -all`  
**GoDaddy URL**: https://dcc.godaddy.com/control/portfolio/noizyfish.com/settings

---

**Remember: EDIT the existing record, don't add a new one!** ✅

