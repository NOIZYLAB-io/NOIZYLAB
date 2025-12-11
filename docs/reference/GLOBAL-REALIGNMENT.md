# GLOBAL ACCOUNT RE-ALIGNMENT
## rsplowman@icloud.com = ONE IDENTITY • ZERO FRAGMENTATION

---

## 🚨 CURRENT STATE: BROKEN

```
┌─────────────────────────────────────────────────────────────┐
│  FRAGMENTED IDENTITY HELL                                   │
├─────────────────────────────────────────────────────────────┤
│  rsplowman@icloud.com ──┬── Apple ID ✅                     │
│                         ├── Microsoft Personal (blocked)    │
│                         ├── Google (?)                      │
│                         └── Other services (scattered)      │
│                                                             │
│  fishmusicinc.com ──────┬── Dead Azure AD Tenant ❌         │
│  (OLD BUSINESS)         ├── Edge keeps using this ❌        │
│                         └── Blocking your subscriptions ❌  │
│                                                             │
│  rsp@noizyfish.com ─────┬── Git commits                     │
│                         └── Business email                  │
│                                                             │
│  [Other emails?] ───────┬── ???                             │
│                         └── ???                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 TARGET STATE: UNIFIED

```
┌─────────────────────────────────────────────────────────────┐
│  rsplowman@icloud.com = MASTER IDENTITY                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   APPLE     │  │  MICROSOFT  │  │   GOOGLE    │         │
│  │   ✅ Done   │  │  ⬜ Fix Now │  │  ⬜ Align   │         │
│  │  - iCloud   │  │  - M365 Fam │  │  - Gmail    │         │
│  │  - Keychain │  │  - Copilot  │  │  - YouTube  │         │
│  │  - All devs │  │  - OneDrive │  │  - Drive    │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  CLOUDFLARE │  │   GITHUB    │  │   STRIPE    │         │
│  │  ⬜ Align   │  │  ⬜ Align   │  │  ⬜ Align   │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  AUTH: Apple Passkeys (Face ID) EVERYWHERE                  │
│  BACKUP: rsp@noizyfish.com (business alias only)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 PHASE 1: AUDIT (Do First)

### Step 1.1: List ALL Your Emails

Fill this in:

| Email | Purpose | Keep? |
|-------|---------|-------|
| rsplowman@icloud.com | PRIMARY IDENTITY | ✅ MASTER |
| rsp@noizyfish.com | NOIZYLAB business | ✅ Business alias |
| [Carolina's email] | Family member | ✅ Keep |
| @fishmusicinc.com | Old business | ❌ DELETE/ARCHIVE |
| | | |
| | | |

### Step 1.2: Subscription Audit

**Check each and report back:**

| Subscription | Check URL | Status | Tied To |
|--------------|-----------|--------|---------|
| Microsoft 365 Family | [account.microsoft.com/services](https://account.microsoft.com/services) | ⬜ | ? |
| Copilot Pro | Same page | ⬜ | ? |
| OneDrive Storage | Same page | ⬜ | ? |
| Xbox Game Pass | Same page | ⬜ | ? |
| Apple One | Settings → Apple ID → Subscriptions | ⬜ | ? |
| Claude Max | [claude.ai/settings](https://claude.ai/settings) | ⬜ | ? |
| GitHub Copilot | [github.com/settings/copilot](https://github.com/settings/copilot) | ⬜ | ? |
| Cloudflare Pro | [dash.cloudflare.com](https://dash.cloudflare.com) | ⬜ | ? |
| Spotify | [spotify.com/account](https://spotify.com/account) | ⬜ | ? |
| Netflix | | ⬜ | ? |
| Other: | | ⬜ | ? |
| Other: | | ⬜ | ? |

### Step 1.3: Microsoft Account Aliases

**Go to:** [account.live.com/names/manage](https://account.live.com/names/manage)

List all emails attached:
```
1. 
2. 
3. 
4. 
5. 
```

**Which is PRIMARY?** _______________

---

## 📋 PHASE 2: KILL THE DEAD TENANT

### The Problem
**fishmusicinc.com** has an Azure AD tenant that's intercepting your sign-ins.

### Option A: Delete the Tenant (If You Have Admin)

```
1. Go to: portal.azure.com
2. Sign in with: [admin]@fishmusicinc.com (whatever the original admin was)
3. Search: "Azure Active Directory"
4. Click: "Manage tenants"
5. Select: fishmusicinc.com tenant
6. Click: "Delete"
7. Follow prompts
```

### Option B: Remove Association (If No Admin Access)

```
1. Go to: myaccount.microsoft.com/organizations
2. Sign in with: rsplowman@icloud.com
3. Find: fishmusicinc.com
4. Click: "Leave organization"
```

### Option C: Nuclear - Contact Microsoft Support

If locked out of both:
```
1. Go to: support.microsoft.com
2. Request: Tenant deletion / account unlinking
3. Prove identity with subscription payment receipts
```

---

## 📋 PHASE 3: MICROSOFT REALIGNMENT

### Step 3.1: Verify Personal Account Access

```
1. Open SAFARI (not Edge)
2. Go to: account.microsoft.com
3. Sign in: rsplowman@icloud.com
4. Should see: Microsoft 365 Family subscription
```

If you see your subscription → Continue
If blocked → Phase 2 first (kill tenant)

### Step 3.2: Set Primary Alias

```
1. Go to: account.live.com/names/manage
2. Make rsplowman@icloud.com PRIMARY
3. Remove old/unused aliases
4. Keep rsp@noizyfish.com as secondary (optional)
```

### Step 3.3: Add Passkey

```
1. Go to: account.microsoft.com/security
2. Click: "Advanced security options"
3. Click: "Add a new way to sign in"
4. Select: "Face, fingerprint, PIN, or security key"
5. Face ID → Done
```

### Step 3.4: Fix Edge Sync

```
1. Open Edge
2. Settings → Profiles → Sign out
3. Sign back in with: rsplowman@icloud.com
4. If it tries fishmusicinc.com → Cancel → "Use personal account"
```

### Step 3.5: Fix Windows Sign-in (If Applicable)

```
1. Settings → Accounts → Your info
2. Sign in with Microsoft account
3. Use: rsplowman@icloud.com
4. NOT work/school account
```

---

## 📋 PHASE 4: APPLE ECOSYSTEM (Verify)

Should already be correct:

| Service | Account | Status |
|---------|---------|--------|
| iCloud | rsplowman@icloud.com | ✅ |
| App Store | rsplowman@icloud.com | ✅ |
| Apple Music | rsplowman@icloud.com | ✅ |
| iCloud Keychain | rsplowman@icloud.com | ✅ |
| Family Sharing | rsplowman@icloud.com (organizer) | ✅ |

**Verify:**
```
Mac: System Settings → [Your Name] → Confirm email
iPhone: Settings → [Your Name] → Confirm email
iPad: Settings → [Your Name] → Confirm email
```

---

## 📋 PHASE 5: GOOGLE REALIGNMENT

### Step 5.1: Check Current State

```
1. Go to: myaccount.google.com
2. What email are you signed in with?
3. Check: Personal info → Email
```

### Step 5.2: Decide Google Strategy

**Option A:** Use rsplowman@icloud.com to SIGN INTO Google
- Create Google account using iCloud email as username
- OR link iCloud email to existing Google account

**Option B:** Keep separate Gmail but forward to iCloud
- Gmail settings → Forwarding → rsplowman@icloud.com

### Step 5.3: Add Passkey to Google

```
1. Go to: g.co/passkeys
2. Click: "Create a passkey"
3. Face ID → Done
```

---

## 📋 PHASE 6: ALL OTHER SERVICES

Once Microsoft/Google/Apple are aligned, cascade to all others:

### Tier 1: CRITICAL (Today)
| Service | Update Email | Add Passkey |
|---------|--------------|-------------|
| GitHub | ⬜ | ⬜ |
| Cloudflare | ⬜ | ⬜ |
| Stripe | ⬜ | ⬜ |

### Tier 2: BUSINESS (This Week)
| Service | Update Email | Add Passkey |
|---------|--------------|-------------|
| PayPal | ⬜ | ⬜ |
| Shopify | ⬜ | ⬜ |
| Domain registrars | ⬜ | ⬜ |

### Tier 3: MUSIC / NOIZYLAB
| Service | Update Email | Add Passkey |
|---------|--------------|-------------|
| SOCAN | ⬜ | ⬜ |
| DistroKid | ⬜ | ⬜ |
| Spotify Artists | ⬜ | ⬜ |
| Plugin vendors | ⬜ | ⬜ |

---

## 📋 PHASE 7: CLEANUP

### Delete/Archive Old Accounts
- [ ] fishmusicinc.com tenant deleted
- [ ] Old email forwards set up
- [ ] Unused accounts closed
- [ ] Password manager updated

### Verify Everything Works
- [ ] Microsoft 365 perks accessible
- [ ] Copilot Pro working
- [ ] OneDrive syncing
- [ ] Edge signed into correct account
- [ ] All devices on same identity
- [ ] Passkeys syncing via iCloud Keychain

---

## 🔥 IMMEDIATE ACTION ITEMS

### RIGHT NOW:
```
1. Safari → account.microsoft.com
2. Sign in: rsplowman@icloud.com
3. Tell me what you see:
   - Subscriptions?
   - Blocked?
   - Error message?
```

### TELL ME:
1. What subscriptions show on that page?
2. Can you access portal.azure.com with any @fishmusicinc.com email?
3. What other premium subscriptions are you paying for?

---

## 📞 ESCALATION PATH

If self-service fails:

**Microsoft Support:** [support.microsoft.com/contactus](https://support.microsoft.com/contactus)
- Reference: AADSTS50020 error
- Request: Personal account unlinked from business tenant
- Have ready: Subscription payment proof

**Apple Support:** Call for Family Sharing issues

---

## 🏆 SUCCESS CRITERIA

```
✅ rsplowman@icloud.com = ONLY login everywhere
✅ Microsoft 365 Family perks WORKING
✅ Copilot Pro ACCESSIBLE  
✅ fishmusicinc.com tenant DEAD
✅ Apple Passkeys on ALL services
✅ Carolina set up in Family
✅ Zero orphaned accounts
✅ Zero payment leakage
```

---

## START NOW

**Go to:** [account.microsoft.com/services](https://account.microsoft.com/services)

**Use:** Safari (NOT Edge)

**Sign in:** rsplowman@icloud.com

**Screenshot or tell me what subscriptions you see.**
