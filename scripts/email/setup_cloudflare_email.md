# 📧 CLOUDFLARE EMAIL ROUTING SETUP GUIDE

## Domains to Configure:

### 1. fishmusicinc.com
- **Catch-all** → rsplowman@icloud.com
- Specific: rp@, gofish@

### 2. noizylab.ca  
- **Catch-all** → rsplowman@icloud.com
- Specific: rsp@, help@, hello@

### 3. noizy.ai
- **Catch-all** → rsplowman@icloud.com
- Specific: rsp@

### 4. noizyfish.com
- rsp@ = PRIMARY (PayPal, GitHub, Ko-fi)

---

## Setup Steps (Per Domain):

1. Go to: https://dash.cloudflare.com
2. Select domain
3. Click: Email → Email Routing
4. Enable Email Routing
5. Scroll to "Catch-all address"
6. Set: Forward to → rsplowman@icloud.com
7. Save
8. Verify destination (check iCloud for verification email)

---

## Required DNS Records (Auto-added):

```
MX  @  route1.mx.cloudflare.net  Priority: 69
MX  @  route2.mx.cloudflare.net  Priority: 15  
MX  @  route3.mx.cloudflare.net  Priority: 3
TXT @  v=spf1 include:_spf.mx.cloudflare.net ~all
```

---

## Test Emails:
- Send test to rp@fishmusicinc.com
- Send test to rsp@noizylab.ca
- Send test to rsp@noizy.ai
- Check rsplowman@icloud.com inbox

GORUNFREE! 🚀
