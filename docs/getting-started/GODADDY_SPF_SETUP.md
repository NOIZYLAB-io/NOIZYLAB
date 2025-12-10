# GoDaddy SPF Setup for noizyfish.com

## Quick Setup Steps

### Access GoDaddy DNS
1. Go to: https://dcc.godaddy.com/control/portfolio/noizyfish.com/settings
2. Or: GoDaddy → My Products → Find `noizyfish.com` → DNS

### Add SPF Record

#### Option 1: Microsoft 365 Only (Recommended)
```
Type: TXT
Name: @
Value: v=spf1 include:spf.protection.outlook.com -all
TTL: 600 (or default)
```

#### Option 2: Microsoft 365 + GoDaddy (If needed)
```
Type: TXT
Name: @
Value: v=spf1 include:spf.protection.outlook.com include:secureserver.net -all
TTL: 600 (or default)
```

## Step-by-Step Instructions

### 1. Navigate to DNS Management
- Log into GoDaddy
- Go to **My Products**
- Find **noizyfish.com**
- Click **DNS** or **Manage DNS**

### 2. Add TXT Record
- Click **Add** or **Add Record**
- Select **TXT** from the Type dropdown
- **Name/Host**: Enter `@` (or leave blank, or enter `noizyfish.com`)
- **Value**: Enter `v=spf1 include:spf.protection.outlook.com -all`
- **TTL**: Leave default (usually 600 seconds)
- Click **Save**

### 3. Verify
- Wait 5-15 minutes for DNS propagation
- Check with: `dig TXT noizyfish.com | grep spf`
- Or use: https://mxtoolbox.com/spf.aspx

## Important Notes

### ⚠️ Only ONE SPF Record
- You can only have **ONE** SPF record per domain
- If you already have an SPF record, you must **edit** it, not add a new one
- Multiple SPF records will cause email delivery issues

### 🔍 Check Existing Records First
Before adding, check if you already have an SPF record:
1. Look for any TXT record containing `v=spf1`
2. If found, **edit** that record instead of adding new
3. Replace the value with the new SPF record

### ✅ Recommended Record
For Microsoft 365 only (cleanest setup):
```
v=spf1 include:spf.protection.outlook.com -all
```

## Troubleshooting

### Can't Find DNS Settings?
- Make sure you're logged into the correct GoDaddy account
- Domain must be in your account
- Try: https://dcc.godaddy.com/control/portfolio

### Record Not Showing?
- Wait 15-30 minutes for DNS propagation
- Clear browser cache
- Try incognito/private browsing mode

### Multiple SPF Records Error?
- You can only have ONE SPF record
- Delete old SPF records
- Keep only the new one

## Verification Commands

```bash
# Check SPF record
dig TXT noizyfish.com | grep spf

# Or using nslookup
nslookup -type=TXT noizyfish.com

# Online verification
# Visit: https://mxtoolbox.com/spf.aspx
# Enter: noizyfish.com
```

## Expected Result

After setup, you should see:
```
"v=spf1 include:spf.protection.outlook.com -all"
```

## Next Steps

1. ✅ Add SPF record (you're doing this now)
2. ⏳ Add DKIM records (from Microsoft 365 Admin)
3. ⏳ Add DMARC policy
4. ⏳ Test email delivery

## Quick Reference

**Domain**: noizyfish.com  
**DNS Provider**: GoDaddy  
**Control Panel**: https://dcc.godaddy.com/control/portfolio/noizyfish.com/settings

**Recommended SPF**:
```
v=spf1 include:spf.protection.outlook.com -all
```

---

**Ready to add? Follow the steps above!** 🚀

