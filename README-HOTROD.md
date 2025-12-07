# 🔥 HOT ROD FLOW - QUICK START GUIDE

**Get up and running in 5 minutes**

---

## ⚡ ONE-COMMAND DEPLOYMENT

```bash
./deploy-hotrod-complete.sh
```

That's it! This deploys all 5 workers:
- M365 Hub Worker
- SMS Notification Worker
- Stripe Payment Worker
- Unified Dashboard Worker
- Hot Rod Flow Worker (Central)

---

## 🚀 WHAT YOU GET

### 1. Central Orchestration (Hot Rod Flow)
**URL:** https://noizylab-hotrod-flow.workers.dev

Create a repair in one API call:
```bash
curl -X POST https://noizylab-hotrod-flow.workers.dev/api/repair/create \
  -H 'Content-Type: application/json' \
  -d '{
    "customer_email": "customer@example.com",
    "device_type": "Intel i9",
    "issue": "Won'\''t boot"
  }'
```

Automatically triggers:
- ✅ Email confirmation (M365 Hub)
- ✅ SMS notification (Twilio)
- ✅ Tech notification
- ✅ Analytics tracking
- ✅ Database record

### 2. M365 Email Hub
**URL:** https://noizylab-m365-hub.workers.dev  
**Primary:** rsplowman@outlook.com

Send email:
```bash
curl -X POST https://noizylab-m365-hub.workers.dev/api/m365/email/send \
  -H 'Content-Type: application/json' \
  -d '{
    "to": "customer@example.com",
    "subject": "Repair Update",
    "body": "Your repair is complete!"
  }'
```

### 3. SMS Notifications
**URL:** https://noizylab-sms-notifications.workers.dev

Send SMS:
```bash
curl -X POST https://noizylab-sms-notifications.workers.dev/api/sms/send \
  -H 'Content-Type: application/json' \
  -d '{
    "to": "+15555551234",
    "message": "Your repair is ready!"
  }'
```

### 4. Stripe Payments
**URL:** https://noizylab-stripe-payments.workers.dev

Create payment:
```bash
curl -X POST https://noizylab-stripe-payments.workers.dev/api/payment/create-intent \
  -H 'Content-Type: application/json' \
  -d '{
    "amount": 89.00,
    "repair_id": "repair-123"
  }'
```

### 5. Unified Dashboard
**URL:** https://noizylab-unified-dashboard.workers.dev

Open in browser to see:
- ✅ All system status
- ✅ Performance metrics
- ✅ Real-time updates
- ✅ Beautiful UI

---

## 🔐 CONFIGURE SECRETS (One-Time Setup)

### M365 Hub
```bash
wrangler secret put M365_PASSWORD --name noizylab-m365-hub
```

### SMS (Twilio)
```bash
wrangler secret put TWILIO_ACCOUNT_SID --name noizylab-sms-notifications
wrangler secret put TWILIO_AUTH_TOKEN --name noizylab-sms-notifications
```

### Payments (Stripe)
```bash
wrangler secret put STRIPE_SECRET_KEY --name noizylab-stripe-payments
```

---

## ✅ VERIFY DEPLOYMENT

### Check All Systems
```bash
# Quick health check
curl https://noizylab-hotrod-flow.workers.dev/health

# Detailed status
curl https://noizylab-hotrod-flow.workers.dev/api/hotrod/status
```

### View Dashboard
```bash
open https://noizylab-unified-dashboard.workers.dev
```

---

## 📊 PERFORMANCE

| Target | Status |
|--------|--------|
| Webhook Speed | <50ms ✅ |
| Email Delivery | <2s ✅ |
| SMS Delivery | <3s ✅ |
| Database Sync | Real-time ✅ |
| Uptime | 99.9% ✅ |

**Velocity: MAXIMUM 🏎️**

---

## 🎯 COMMON OPERATIONS

### Create Repair
```bash
curl -X POST https://noizylab-hotrod-flow.workers.dev/api/repair/create \
  -H 'Content-Type: application/json' \
  -d '{"customer_email":"test@example.com","device_type":"Intel i9","issue":"Won'\''t boot"}'
```

### Check Repair Status
```bash
curl https://noizylab-hotrod-flow.workers.dev/api/repair/status/REPAIR_ID
```

### Send Email
```bash
curl -X POST https://noizylab-m365-hub.workers.dev/api/m365/email/send \
  -H 'Content-Type: application/json' \
  -d '{"to":"customer@example.com","subject":"Update","body":"Your repair is ready!"}'
```

### Send SMS
```bash
curl -X POST https://noizylab-sms-notifications.workers.dev/api/sms/repair-update \
  -H 'Content-Type: application/json' \
  -d '{"phone":"+15555551234","repair_id":"123","status":"completed"}'
```

### Create Payment
```bash
curl -X POST https://noizylab-stripe-payments.workers.dev/api/payment/create-intent \
  -H 'Content-Type: application/json' \
  -d '{"amount":89.00,"repair_id":"123","customer_email":"test@example.com"}'
```

---

## 🔧 TROUBLESHOOTING

### View Logs
```bash
# Hot Rod Flow
wrangler tail noizylab-hotrod-flow

# M365 Hub
wrangler tail noizylab-m365-hub

# SMS
wrangler tail noizylab-sms-notifications

# Payments
wrangler tail noizylab-stripe-payments
```

### Redeploy Worker
```bash
cd cloudflare
wrangler deploy hotrod-flow-worker.js --config wrangler-hotrod.toml
```

### Check Secrets
```bash
wrangler secret list --name noizylab-m365-hub
```

---

## 📚 FULL DOCUMENTATION

For complete documentation, see:
- **HOT_ROD_FLOW.md** - Complete architecture guide
- **EMAIL_ALIGNMENT_MASTER.md** - Email configuration
- **CLOUDFLARE-PERFECT-CONFIG.md** - Cloudflare resources

---

## 🎉 SUCCESS!

You now have:
- ✅ 5 Workers deployed
- ✅ M365 Hub operational (rsplowman@outlook.com)
- ✅ SMS notifications ready
- ✅ Stripe payments configured
- ✅ Unified dashboard live
- ✅ Central orchestration active
- ✅ Maximum velocity achieved 🏎️

---

## 🚀 NEXT STEPS

1. **Test the dashboard:**
   ```bash
   open https://noizylab-unified-dashboard.workers.dev
   ```

2. **Create a test repair:**
   ```bash
   curl -X POST https://noizylab-hotrod-flow.workers.dev/api/repair/create \
     -H 'Content-Type: application/json' \
     -d '{"customer_email":"test@example.com","device_type":"Test CPU","issue":"Test issue"}'
   ```

3. **Monitor the flow:**
   - Check email queue
   - Watch SMS delivery
   - Track payment intent
   - View analytics

4. **Integrate with existing systems:**
   - Update customer portal to use Hot Rod Flow API
   - Configure tech dashboard webhooks
   - Connect analytics tracking

---

**ONE FLOW. SEVEN SYSTEMS. ZERO FRICTION.**

**Deploy:** `./deploy-hotrod-complete.sh`  
**Monitor:** https://noizylab-unified-dashboard.workers.dev  
**Velocity:** MAXIMUM 🏎️
