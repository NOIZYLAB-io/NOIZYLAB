# 📧 Complete Email Routing Guide - noizylab.ca

## Your Cloudflare Dashboard

**Direct Link**: https://dash.cloudflare.com/1323e14ace0c8d7362612d5b5c0d41bb/noizylab.ca/email/routing/overview

## What Email Routing Does

Cloudflare Email Routing lets you:
- ✅ Receive emails at `@noizylab.ca` addresses
- ✅ Forward them to your Gmail (rspplowman@gmail.com)
- ✅ No email server needed
- ✅ Free with Cloudflare
- ✅ Works with SPF/DKIM

## Setup Steps

### Step 1: Enable Email Routing

**In Cloudflare Dashboard:**
1. Go to: https://dash.cloudflare.com/1323e14ace0c8d7362612d5b5c0d41bb/noizylab.ca/email/routing/overview
2. Click **"Get Started"** or **"Enable Email Routing"**
3. Follow the setup wizard

**Or Automated:**
```bash
cd ~/NOIZYLAB/cloudflare
export CLOUDFLARE_API_TOKEN="your-token"
./setup-noizylab-email-routing.sh
```

### Step 2: Add Destination Address

1. In Email Routing dashboard
2. Click **"Destination addresses"**
3. Click **"Create address"**
4. Enter: `rspplowman@gmail.com`
5. Verify the email address (check Gmail)

### Step 3: Create Routing Rules

Create rules to forward emails:

| Rule | Match | Forward To |
|------|-------|------------|
| rsp@noizylab.ca | rsp@noizylab.ca | rspplowman@gmail.com |
| help@noizylab.ca | help@noizylab.ca | rspplowman@gmail.com |
| hello@noizylab.ca | hello@noizylab.ca | rspplowman@gmail.com |

**To Create:**
1. Click **"Routing rules"**
2. Click **"Create rule"**
3. Enter match: `rsp@noizylab.ca`
4. Select action: Forward to `rspplowman@gmail.com`
5. Save

### Step 4: Set Catch-All (Optional)

Forward all other emails to `*@noizylab.ca`:
1. Click **"Catch-all address"**
2. Set to: `rspplowman@gmail.com`

## Testing

Send test emails to:
- `rsp@noizylab.ca` → Should arrive at rspplowman@gmail.com
- `help@noizylab.ca` → Should arrive at rspplowman@gmail.com
- `hello@noizylab.ca` → Should arrive at rspplowman@gmail.com

## Integration with iOS Setup

After Email Routing is set up:

1. **Emails arrive** at rspplowman@gmail.com (via Cloudflare)
2. **Use iOS Mail** to read from Gmail
3. **Send emails** from @noizylab.ca addresses using Gmail

## Complete Flow

```
Email sent to rsp@noizylab.ca
    ↓
Cloudflare Email Routing
    ↓
Forwards to rspplowman@gmail.com
    ↓
Received in Gmail
    ↓
Read on iPhone/iPad via iOS Mail
```

## Benefits

✅ **Free** - No cost for Email Routing
✅ **Reliable** - Cloudflare's global network
✅ **Simple** - No server management
✅ **Integrated** - Works with existing Gmail
✅ **Professional** - Use @noizylab.ca addresses

## Next Steps

1. ✅ Enable Email Routing in Cloudflare
2. ✅ Add destination address
3. ✅ Create routing rules
4. ✅ Test email delivery
5. ✅ Set up iOS Mail (use Cloudflare AI helper)

---

**Email Routing + iOS Setup = Complete Email System!** 🚀

