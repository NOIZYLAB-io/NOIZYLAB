# Complete Upgrade + Improvement Plan
## noizylab.ca and fishmusicinc.com

**Version:** 1.0  
**Date:** 2024-11-22  
**Status:** Production-Ready

---

## 1. Final Goals (What "Perfect" Means Here)

✅ **Reliable inbound/outbound mail** for:
- `rsp@noizylab.ca`, `help@noizylab.ca`, `hello@noizylab.ca`
- `rp@fishmusicinc.com`, `info@fishmusicinc.com`

✅ **Full email authentication**:
- SPF: Properly configured
- DKIM: Active and verified
- DMARC: Gradually enforced to `p=reject`

✅ **Enforced TLS for mail delivery**:
- MTA-STS: Policy enforced, HTTPS-hosted
- TLSRPT: Reporting enabled for monitoring

✅ **BIMI-ready brand treatment**:
- Verified Mark Certificate (VMC) ready
- Logo configured for email clients

✅ **Continuous telemetry**:
- DMARC aggregate reports
- TLS reports
- Alerting on authentication failures
- Dashboard for monitoring

✅ **Reproducible infrastructure**:
- Terraform-managed DNS records
- Version-controlled configuration
- Auditable changes

---

## 2. What's Already Delivered

✅ Terraform modules for Cloudflare DNS:
- MX records (5 per domain)
- SPF TXT records
- DKIM placeholders
- DMARC records
- MTA-STS DNS records
- TLSRPT records

✅ README runbook with:
- `terraform init/plan/apply` procedures
- Verification commands (`dig`)
- Safety and rollback procedures

✅ Configuration files:
- `versions.tf` - Provider configuration
- `variables.tf` - All variables defined
- `main.tf` - DNS resource blocks
- `terraform.tfvars` - Placeholder values
- `.gitignore` - Security protections

---

## 3. Upgrade Phases & Timeline

### Phase 0: Pre-Flight Checklist (Day 0)
**Goal:** Verify prerequisites and prepare environment

- [ ] **Google Workspace Setup**
  - [ ] Verify domains verified in Google Admin Console
  - [ ] Enable Gmail for both domains
  - [ ] Generate DKIM keys for both domains
  - [ ] Test mailbox creation (`rsp@noizylab.ca`, `help@noizylab.ca`, `hello@noizylab.ca`)
  - [ ] Test mailbox creation (`rp@fishmusicinc.com`, `info@fishmusicinc.com`)

- [ ] **Cloudflare Setup**
  - [ ] Create API token with Zone.DNS (Edit) and Zone.Zone (Read)
  - [ ] Note Zone IDs for both domains
  - [ ] Verify DNS management access

- [ ] **Terraform Setup**
  - [ ] Install Terraform >= 1.6.0
  - [ ] Verify Cloudflare provider available
  - [ ] Clone/access Terraform configuration

- [ ] **Email Infrastructure**
  - [ ] Set up DMARC reporting email (`dmarc-reports@noizylab.ca`)
  - [ ] Set up TLS reporting email (`tlsrpt@noizylab.ca`)
  - [ ] Set up DMARC reporting email (`dmarc-reports@fishmusicinc.com`)
  - [ ] Set up TLS reporting email (`tlsrpt@fishmusicinc.com`)

**Estimated Time:** 1-2 hours

---

### Phase 1: Initial DNS Deployment (Week 1, Day 1)
**Goal:** Deploy all DNS records with relaxed DMARC policy

**DMARC Policy:** `p=none` (monitoring only)

- [ ] **Fill Terraform Variables**
  ```bash
  # Edit terraform.tfvars
  cloudflare_api_token = "your_token"
  zone_noizylab_ca = "your_zone_id"
  zone_fishmusicinc_com = "your_zone_id"
  dkim_public_key_noizylab = "your_dkim_key"
  dkim_public_key_fish = "your_dkim_key"
  dmarc_policy_noizylab = "none"
  dmarc_policy_fish = "none"
  dmarc_rua_noizylab = "dmarc-reports@noizylab.ca"
  dmarc_rua_fish = "dmarc-reports@fishmusicinc.com"
  ```

- [ ] **Deploy DNS Records**
  ```bash
  terraform init
  terraform plan -out=tfplan
  terraform show -json tfplan | jq '.planned_values.root_module.resources[] | {address, type, name, values}'
  terraform apply tfplan
  ```

- [ ] **Verify DNS Records**
  ```bash
  # MX Records
  dig +short MX noizylab.ca
  dig +short MX fishmusicinc.com
  
  # SPF
  dig +short TXT noizylab.ca | grep spf
  
  # DKIM
  dig +short TXT google._domainkey.noizylab.ca
  
  # DMARC
  dig +short TXT _dmarc.noizylab.ca
  
  # MTA-STS
  dig +short TXT _mta-sts.noizylab.ca
  
  # TLSRPT
  dig +short TXT _smtp._tls.noizylab.ca
  ```

- [ ] **Test Email Delivery**
  - [ ] Send test email from `rsp@noizylab.ca` to Gmail
  - [ ] Verify in Gmail "Show original": SPF: PASS, DKIM: PASS, DMARC: PASS
  - [ ] Send test email from `rp@fishmusicinc.com` to Gmail
  - [ ] Verify authentication passes

**Expected Results:**
- All DNS records created
- Email delivery working
- DMARC reports starting to arrive
- No email delivery issues

**Estimated Time:** 2-3 hours  
**Monitoring Period:** 7 days

---

### Phase 2: MTA-STS Policy Deployment (Week 1, Day 2-3)
**Goal:** Deploy and enforce TLS for mail delivery

- [ ] **Host MTA-STS Policy Files**

  **For noizylab.ca:** Create `https://mta-sts.noizylab.ca/.well-known/mta-sts.txt`
  
  **For fishmusicinc.com:** Create `https://mta-sts.fishmusicinc.com/.well-known/mta-sts.txt`

  Policy file content (see `mta-sts-policies/` directory for templates):
  ```
  version: STSv1
  mode: enforce
  max_age: 604800
  mx: aspmx.l.google.com
  mx: alt1.aspmx.l.google.com
  mx: alt2.aspmx.l.google.com
  mx: alt3.aspmx.l.google.com
  mx: alt4.aspmx.l.google.com
  ```

- [ ] **Update Terraform MTA-STS Records**
  - [ ] Update `main.tf` MTA-STS records with timestamp ID
  - [ ] Apply changes

- [ ] **Verify MTA-STS**
  ```bash
  # Check DNS record
  dig +short TXT _mta-sts.noizylab.ca
  
  # Check policy file
  curl https://mta-sts.noizylab.ca/.well-known/mta-sts.txt
  
  # Test with online validator
  # https://www.hardenize.com/test/mta-sts
  ```

- [ ] **Monitor TLS Reports**
  - [ ] Check TLSRPT email for reports
  - [ ] Verify TLS connections succeeding
  - [ ] Monitor for failures

**Expected Results:**
- MTA-STS policy files accessible
- DNS records point to policy
- TLS enforced for mail delivery
- TLS reports received

**Estimated Time:** 3-4 hours  
**Monitoring Period:** 7 days

---

### Phase 3: DMARC Gradual Enforcement (Weeks 2-4)
**Goal:** Gradually tighten DMARC policy from `none` → `quarantine` → `reject`

#### Week 2: Monitor and Baseline (DMARC: `p=none`)
**Day 8-14:**
- [ ] **Monitor DMARC Reports**
  - [ ] Daily check of DMARC aggregate reports
  - [ ] Identify legitimate senders
  - [ ] Identify unauthorized senders
  - [ ] Calculate authentication pass rate
  
- [ ] **Create DMARC Dashboard**
  - [ ] Set up DMARC report parser (e.g., dmarcian, Postmark)
  - [ ] Track authentication rates
  - [ ] Identify patterns and issues

- [ ] **Document Baseline Metrics**
  - [ ] SPF pass rate
  - [ ] DKIM pass rate
  - [ ] DMARC alignment rate
  - [ ] Total volume of emails

**Success Criteria:**
- >95% SPF pass rate
- >95% DKIM pass rate
- >98% DMARC alignment rate
- All legitimate senders identified

---

#### Week 3: Quarantine Phase (DMARC: `p=quarantine`)
**Day 15-21:**

- [ ] **Update Terraform Configuration**
  ```hcl
  # terraform.tfvars
  dmarc_policy_noizylab = "quarantine"
  dmarc_policy_fish = "quarantine"
  ```

- [ ] **Apply Changes**
  ```bash
  terraform plan
  terraform apply
  ```

- [ ] **Monitor Intensely**
  - [ ] Check spam folders daily
  - [ ] Monitor authentication failures
  - [ ] Respond to user complaints
  - [ ] Track quarantine rate

- [ ] **Optimize**
  - [ ] Fix SPF/DKIM issues
  - [ ] Update DMARC policy if needed
  - [ ] Whitelist legitimate services

**Success Criteria:**
- <1% false positives (legitimate emails quarantined)
- >99% DMARC compliance
- No user complaints about missed emails
- Authentication rates maintained

**Rollback Plan:**
If issues occur, revert to `p=none` immediately:
```bash
# Edit terraform.tfvars
dmarc_policy_noizylab = "none"
terraform apply
```

---

#### Week 4: Reject Phase (DMARC: `p=reject`)
**Day 22-28:**

- [ ] **Final Verification**
  - [ ] 7 days at `p=quarantine` with no issues
  - [ ] Authentication rates >99%
  - [ ] No legitimate senders failing

- [ ] **Update to Reject**
  ```hcl
  # terraform.tfvars
  dmarc_policy_noizylab = "reject"
  dmarc_policy_fish = "reject"
  ```

- [ ] **Apply Changes**
  ```bash
  terraform plan
  terraform apply
  ```

- [ ] **Monitor Strictly**
  - [ ] Daily authentication reports
  - [ ] User feedback monitoring
  - [ ] Automated alerting on failures

**Success Criteria:**
- >99.5% DMARC compliance
- Zero false positives
- All email delivery working correctly
- Full email authentication enforced

**Estimated Time (All Phases):** 4 weeks  
**Total Monitoring:** 28 days minimum

---

### Phase 4: BIMI Setup (Week 3-4)
**Goal:** Enable Brand Indicators for Message Identification

- [ ] **Prerequisites**
  - [ ] DMARC at `p=quarantine` or `p=reject` (required for BIMI)
  - [ ] Obtain Verified Mark Certificate (VMC) from Certificate Authority
  - [ ] Create brand logo (SVG format, square, 200x200px minimum)
  - [ ] Validate logo meets BIMI requirements

- [ ] **Add BIMI to Terraform**
  - [ ] Add BIMI TXT record resource to `main.tf`
  - [ ] Configure VMC location URL
  - [ ] Set logo URL

- [ ] **Deploy BIMI Records**
  ```bash
  terraform plan
  terraform apply
  ```

- [ ] **Verify BIMI**
  ```bash
  dig +short TXT default._bimi.noizylab.ca
  ```

- [ ] **Test in Email Clients**
  - [ ] Send test email
  - [ ] Verify logo appears in Gmail, Yahoo, FastMail, etc.
  - [ ] Verify brand protection

**Estimated Time:** 4-8 hours (including VMC procurement)  
**VMC Procurement:** 1-2 weeks (external dependency)

---

### Phase 5: Telemetry & Monitoring (Ongoing, Week 1+)
**Goal:** Continuous monitoring and alerting

#### DMARC Report Processing

- [ ] **Set Up DMARC Report Parser**
  
  **Option A: dmarcian (Commercial)**
  - [ ] Sign up at https://dmarcian.com
  - [ ] Configure domain forwarding
  - [ ] Set up dashboard access

  **Option B: Postmark (Commercial)**
  - [ ] Sign up at https://postmarkapp.com/dmarc-digest
  - [ ] Configure reporting emails
  - [ ] Set up notifications

  **Option C: Self-Hosted (DMARCLY)**
  - [ ] Deploy DMARCLY or similar
  - [ ] Configure email processing
  - [ ] Set up dashboard

- [ ] **Configure Alerting**
  - [ ] Authentication rate drops below 95%
  - [ ] Unauthorized senders detected
  - [ ] DMARC policy failures
  - [ ] DKIM signature failures

#### TLS Report Processing

- [ ] **Set Up TLS Report Parser**
  - [ ] Configure email inbox for TLS reports
  - [ ] Parse TLS report JSON files
  - [ ] Monitor TLS connection failures

- [ ] **Configure Alerts**
  - [ ] TLS handshake failures
  - [ ] Certificate validation errors
  - [ ] Policy violations

#### Dashboard & Reporting

- [ ] **Create Monitoring Dashboard**
  - [ ] DMARC authentication rates
  - [ ] SPF/DKIM pass rates
  - [ ] Email volume trends
  - [ ] Failed authentication breakdown

- [ ] **Set Up Weekly Reports**
  - [ ] Automated DMARC summary
  - [ ] TLS report summary
  - [ ] Anomaly detection
  - [ ] Email to stakeholders

**Estimated Time:** 8-16 hours  
**Ongoing Maintenance:** 1-2 hours/month

---

### Phase 6: Hardening & Optimization (Week 4+)
**Goal:** Final security hardening and performance optimization

#### Additional DNS Security

- [ ] **Add CAA Records** (if not present)
  ```hcl
  resource "cloudflare_record" "caa_noizylab" {
    zone_id = var.zone_noizylab_ca
    name    = "noizylab.ca"
    type    = "CAA"
    content = "0 issue \"letsencrypt.org\""
    comment = "Certificate Authority Authorization"
  }
  ```

- [ ] **Add DNSSEC** (if not enabled)
  - [ ] Enable DNSSEC in Cloudflare
  - [ ] Verify DNSSEC chain
  - [ ] Monitor DNSSEC validation

#### Email Security Headers

- [ ] **Configure ARC (Authenticated Received Chain)**
  - [ ] Verify Google Workspace ARC support
  - [ ] Monitor ARC headers

- [ ] **Review SPF Record**
  - [ ] Ensure no unnecessary includes
  - [ ] Optimize SPF record size (<255 bytes)
  - [ ] Use redirects if needed

#### Performance Optimization

- [ ] **MX Record Priority Optimization**
  - [ ] Verify priority order is correct
  - [ ] Monitor MX lookup performance

- [ ] **DNS TTL Optimization**
  - [ ] Set appropriate TTLs for records
  - [ ] Balance between caching and agility

**Estimated Time:** 4-8 hours

---

## 4. Terraform Enhancements

### Additional Resources Needed

#### BIMI Records
Add to `main.tf`:

```hcl
# BIMI Record for noizylab.ca
resource "cloudflare_record" "bimi_noizylab" {
  zone_id = var.zone_noizylab_ca
  name    = "default._bimi.noizylab.ca"
  type    = "TXT"
  content = "v=BIMI1; l=https://noizylab.ca/.well-known/logo.svg; a=https://noizylab.ca/.well-known/vmc.pem;"
  comment = "BIMI Brand Indicator"
}

# BIMI Record for fishmusicinc.com
resource "cloudflare_record" "bimi_fish" {
  zone_id = var.zone_fishmusicinc_com
  name    = "default._bimi.fishmusicinc.com"
  type    = "TXT"
  content = "v=BIMI1; l=https://fishmusicinc.com/.well-known/logo.svg; a=https://fishmusicinc.com/.well-known/vmc.pem;"
  comment = "BIMI Brand Indicator"
}
```

#### CAA Records
Add to `main.tf`:

```hcl
# CAA Record for noizylab.ca
resource "cloudflare_record" "caa_noizylab" {
  zone_id = var.zone_noizylab_ca
  name    = "noizylab.ca"
  type    = "CAA"
  data {
    flags = 0
    tag   = "issue"
    value = "letsencrypt.org"
  }
  comment = "Certificate Authority Authorization"
}

# CAA Record for fishmusicinc.com
resource "cloudflare_record" "caa_fish" {
  zone_id = var.zone_fishmusicinc_com
  name    = "fishmusicinc.com"
  type    = "CAA"
  data {
    flags = 0
    tag   = "issue"
    value = "letsencrypt.org"
  }
  comment = "Certificate Authority Authorization"
}
```

#### Enhanced Variables
Add to `variables.tf`:

```hcl
variable "bimi_logo_url_noizylab" {
  type        = string
  default     = "https://noizylab.ca/.well-known/logo.svg"
  description = "BIMI logo URL for noizylab.ca"
}

variable "bimi_vmc_url_noizylab" {
  type        = string
  default     = "https://noizylab.ca/.well-known/vmc.pem"
  description = "BIMI VMC certificate URL for noizylab.ca"
}

variable "bimi_logo_url_fish" {
  type        = string
  default     = "https://fishmusicinc.com/.well-known/logo.svg"
  description = "BIMI logo URL for fishmusicinc.com"
}

variable "bimi_vmc_url_fish" {
  type        = string
  default     = "https://fishmusicinc.com/.well-known/vmc.pem"
  description = "BIMI VMC certificate URL for fishmusicinc.com"
}
```

---

## 5. MTA-STS Policy Files

### noizylab.ca
**File:** `https://mta-sts.noizylab.ca/.well-known/mta-sts.txt`

```
version: STSv1
mode: enforce
max_age: 604800
mx: aspmx.l.google.com
mx: alt1.aspmx.l.google.com
mx: alt2.aspmx.l.google.com
mx: alt3.aspmx.l.google.com
mx: alt4.aspmx.l.google.com
```

### fishmusicinc.com
**File:** `https://mta-sts.fishmusicinc.com/.well-known/mta-sts.txt`

```
version: STSv1
mode: enforce
max_age: 604800
mx: aspmx.l.google.com
mx: alt1.aspmx.l.google.com
mx: alt2.aspmx.l.google.com
mx: alt3.aspmx.l.google.com
mx: alt4.aspmx.l.google.com
```

**Deployment Notes:**
- Must be served over HTTPS
- Must be accessible at `/.well-known/mta-sts.txt`
- MIME type should be `text/plain`
- File must be valid and parseable

---

## 6. Monitoring & Alerting

### Key Metrics to Monitor

1. **DMARC Authentication Rate**
   - Target: >99%
   - Alert: <95%
   - Frequency: Daily

2. **SPF Pass Rate**
   - Target: >98%
   - Alert: <95%
   - Frequency: Daily

3. **DKIM Pass Rate**
   - Target: >98%
   - Alert: <95%
   - Frequency: Daily

4. **Email Volume**
   - Track: Daily/monthly trends
   - Alert: Sudden drops (>50%)
   - Frequency: Weekly

5. **Authentication Failures**
   - Track: Count by type (SPF/DKIM/DMARC)
   - Alert: Any unauthorized sender
   - Frequency: Real-time

6. **TLS Connection Failures**
   - Target: 0 failures
   - Alert: Any failures
   - Frequency: Weekly

### Alerting Configuration

#### Email Alerts
- **Recipients:** `alerts@noizylab.ca`, `alerts@fishmusicinc.com`
- **Frequency:** Immediate for critical, daily digest for summary
- **Channels:** Email, optional Slack/Teams integration

#### Dashboard
- **Tool:** Grafana, DataDog, or cloud-native solution
- **Refresh:** Real-time or 5-minute intervals
- **Retention:** 90 days minimum

---

## 7. Rollback Procedures

### DMARC Policy Rollback

If issues occur during enforcement:

```bash
# 1. Immediately revert policy
# Edit terraform.tfvars
dmarc_policy_noizylab = "none"  # or "quarantine"
dmarc_policy_fish = "none"

# 2. Apply changes
terraform plan
terraform apply

# 3. Verify
dig +short TXT _dmarc.noizylab.ca
```

### DNS Record Rollback

If a DNS record causes issues:

```bash
# 1. List resources
terraform state list

# 2. Destroy specific resource
terraform destroy -target=cloudflare_record.spf_noizylab

# 3. Or edit main.tf to remove resource
# Then apply
terraform plan
terraform apply
```

### Complete Rollback

If major issues occur:

```bash
# 1. Destroy all DNS records
terraform destroy

# 2. Restore from backup
git checkout HEAD~1 main.tf
terraform apply
```

---

## 8. Success Criteria

### Phase 1 Success
- ✅ All DNS records created
- ✅ Email delivery working
- ✅ DMARC reports arriving
- ✅ No delivery failures

### Phase 2 Success
- ✅ MTA-STS policy files hosted
- ✅ TLS enforced for mail
- ✅ TLS reports received

### Phase 3 Success
- ✅ DMARC at `p=reject`
- ✅ >99.5% authentication rate
- ✅ Zero false positives
- ✅ Full email security enforced

### Phase 4 Success
- ✅ BIMI logos appearing in email clients
- ✅ Brand protection active
- ✅ VMC validated

### Phase 5 Success
- ✅ Automated monitoring active
- ✅ Alerts configured and tested
- ✅ Dashboards operational
- ✅ Weekly reports delivered

---

## 9. Timeline Summary

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| Phase 0: Pre-Flight | 1-2 hours | Prerequisites verified |
| Phase 1: Initial DNS | 2-3 hours + 7 days monitoring | All DNS records deployed |
| Phase 2: MTA-STS | 3-4 hours + 7 days monitoring | TLS enforced |
| Phase 3: DMARC Enforcement | 21 days | Gradual policy tightening |
| Phase 4: BIMI | 4-8 hours | Brand indicators active |
| Phase 5: Telemetry | 8-16 hours + ongoing | Monitoring operational |
| Phase 6: Hardening | 4-8 hours | Security optimized |

**Total Estimated Time:** ~40-60 hours + 28 days monitoring

---

## 10. Risk Assessment

### Low Risk
- DNS record creation (reversible)
- SPF record updates (reversible)
- TLS reporting (monitoring only)

### Medium Risk
- DKIM key deployment (requires re-authentication)
- MTA-STS enforcement (can break mail if misconfigured)
- DMARC policy changes (can affect delivery)

### High Risk
- DMARC `p=reject` (irreversible mail rejection)
- Complete DNS changes (can break email delivery)

**Mitigation:**
- Gradual rollout with monitoring
- Rollback procedures documented
- Test in staging first (if possible)
- Keep backups of all configurations

---

## 11. Post-Deployment Checklist

- [ ] All DNS records verified
- [ ] Email delivery tested (inbound/outbound)
- [ ] DMARC reports being received
- [ ] TLS reports being received
- [ ] DMARC policy at `p=reject`
- [ ] Monitoring dashboard active
- [ ] Alerts configured and tested
- [ ] Documentation updated
- [ ] Team trained on procedures
- [ ] Incident response plan ready

---

## 12. Ongoing Maintenance

### Daily
- [ ] Monitor DMARC reports for anomalies
- [ ] Check authentication rates
- [ ] Review failed authentication alerts

### Weekly
- [ ] Review DMARC aggregate report summary
- [ ] Check TLS report summaries
- [ ] Update documentation if needed

### Monthly
- [ ] Review email volume trends
- [ ] Audit authentication rates
- [ ] Review and optimize DNS records
- [ ] Update Terraform if needed

### Quarterly
- [ ] Review and update DMARC policy if needed
- [ ] Audit BIMI logo and VMC
- [ ] Review monitoring and alerting
- [ ] Update security best practices

---

## Conclusion

This upgrade plan provides a comprehensive, phased approach to hardening email security for both domains. By following this plan, you'll achieve:

✅ Full email authentication (SPF, DKIM, DMARC)  
✅ Enforced TLS (MTA-STS)  
✅ Brand protection (BIMI)  
✅ Continuous monitoring and alerting  
✅ Reproducible infrastructure  

Follow each phase carefully, monitor results, and adjust as needed. The gradual DMARC enforcement approach minimizes risk while maximizing security.

**Remember:** Email security is an ongoing process. Regular monitoring and updates are essential for maintaining a secure email infrastructure.

