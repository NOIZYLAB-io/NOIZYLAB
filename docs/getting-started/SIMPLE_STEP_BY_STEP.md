# Simple Step-by-Step Guide - Update SPF Record

## What You Need to Do

You have an existing SPF record that only includes GoDaddy. You need to **update it** to include Microsoft 365.

## Step-by-Step Instructions

### Step 1: Open GoDaddy
1. Go to: **https://dcc.godaddy.com/control/portfolio/noizyfish.com/settings**
2. Or: Log into GoDaddy → My Products → Find "noizyfish.com" → Click "DNS"

### Step 2: Find Your SPF Record
Look for a **TXT record** that says:
```
v=spf1 include:secureserver.net -all
```

You'll see it in a table with columns like:
- **Type**: TXT
- **Name**: @ (or blank)
- **Value**: v=spf1 include:secureserver.net -all

### Step 3: Click EDIT
- Find the **Edit** button (usually a pencil icon ✏️) next to that TXT record
- **DO NOT** click "Add Record" or "Add"
- Click **Edit** on the existing record

### Step 4: Change the Value
In the **Value** field, replace:
```
v=spf1 include:secureserver.net -all
```

With this (Microsoft 365 only - recommended):
```
v=spf1 include:spf.protection.outlook.com -all
```

Or this (if you also send from GoDaddy):
```
v=spf1 include:spf.protection.outlook.com include:secureserver.net -all
```

### Step 5: Save
- Click **Save** or **Update**
- Wait 15 minutes for changes to take effect

### Step 6: Verify (Optional)
After 15 minutes, check if it worked:
```bash
dig TXT noizyfish.com | grep spf
```

You should see:
```
"v=spf1 include:spf.protection.outlook.com -all"
```

## Visual Guide

```
GoDaddy DNS Page
┌─────────────────────────────────────────┐
│ DNS Records                             │
├──────┬──────┬──────────────────────────┤
│ Type │ Name │ Value                     │
├──────┼──────┼──────────────────────────┤
│ TXT  │ @    │ v=spf1 include:...        │ ← Find this row
│      │      │ [Edit] [Delete]            │ ← Click EDIT here
└──────┴──────┴──────────────────────────┘
```

## Which Value to Use?

### ✅ Recommended: Microsoft 365 Only
```
v=spf1 include:spf.protection.outlook.com -all
```
**Use this if:** You only send emails from Microsoft 365/Outlook

### ⚠️ Alternative: Microsoft 365 + GoDaddy
```
v=spf1 include:spf.protection.outlook.com include:secureserver.net -all
```
**Use this if:** You send emails from BOTH Microsoft 365 AND GoDaddy

## Common Questions

### Q: What if I can't find the SPF record?
A: Look for any TXT record. The SPF record is a TXT type record.

### Q: What if there's no Edit button?
A: Some GoDaddy interfaces use a pencil icon ✏️ or three dots ⋮ menu. Click that.

### Q: What if I accidentally add a new record?
A: Delete the new one and edit the old one. You can only have ONE SPF record.

### Q: How long does it take?
A: Usually 5-15 minutes, but can take up to 48 hours (rare).

### Q: How do I know it worked?
A: Wait 15 minutes, then run: `dig TXT noizyfish.com | grep spf`

## Quick Checklist

- [ ] Opened GoDaddy DNS settings
- [ ] Found the TXT record with `v=spf1`
- [ ] Clicked **EDIT** (not Add)
- [ ] Changed value to include Microsoft 365
- [ ] Clicked **Save**
- [ ] Waited 15 minutes
- [ ] Verified with `dig` command (optional)

## Need Help?

Run this command for interactive help:
```bash
cd ~/NOIZYLAB/email-intelligence
python3 godaddy-dns-helper.py
```

---

**That's it! Just edit the existing record and change the value.** ✅

