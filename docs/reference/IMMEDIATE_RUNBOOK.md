# Immediate Actionable Runbook
## Cloudflare DNS Configuration for Google Workspace Email
### noizylab.ca and fishmusicinc.com

**Purpose:** Copy-paste safe commands for immediate deployment

---

## Prerequisites Check

```bash
# Check Terraform is installed
terraform version

# Check DNS tools are available
which dig
which jq
```

---

## Step 1: Configure Variables

Edit `terraform.tfvars` with your actual values:

```hcl
cloudflare_api_token = "YOUR_CF_API_TOKEN"
zone_noizylab_ca     = "ZONE_ID_NOIZYLAB"
zone_fishmusicinc_com = "ZONE_ID_FISH"
dkim_public_key_noizylab = "NOIZYLAB_DKIM_PUBLIC_KEY_BASE64_NO_HEADERS"
dkim_public_key_fish     = "FISH_DKIM_PUBLIC_KEY_BASE64_NO_HEADERS"
```

**Where to find values:**
- **Cloudflare API Token:** https://dash.cloudflare.com/profile/api-tokens
- **Zone IDs:** Cloudflare Dashboard > Select Domain > Overview > Zone ID (right sidebar)
- **DKIM Keys:** Google Admin Console > Apps > Google Workspace > Gmail > Authenticate email

---

## Step 2: Initialize Terraform

```bash
terraform init
```

Expected output:
```
Initializing the backend...
Initializing provider plugins...
Terraform has been successfully initialized!
```

---

## Step 3: Review Planned Changes

```bash
# Create plan file
terraform plan -out=tfplan

# Review plan in human-readable format
terraform plan -out=tfplan

# View planned resources in JSON format
terraform show -json tfplan | jq '.planned_values.root_module.resources[] | {address, type, name, values}'
```

**What to check:**
- Number of resources being created (should be 12 per domain = 24 total)
- DNS record values are correct
- MX records point to Google servers
- DKIM keys are populated

---

## Step 4: Apply Changes

```bash
terraform apply tfplan
```

Expected output:
```
Plan: 24 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

Enter a value: yes
```

**Type `yes` when prompted.**

---

## Step 5: Verify DNS Records

### Verify MX Records

```bash
dig +short MX noizylab.ca
```

**Expected output:**
```
1 aspmx.l.google.com.
5 alt1.aspmx.l.google.com.
5 alt2.aspmx.l.google.com.
10 alt3.aspmx.l.google.com.
10 alt4.aspmx.l.google.com.
```

```bash
dig +short MX fishmusicinc.com
```

**Expected output:**
```
1 aspmx.l.google.com.
5 alt1.aspmx.l.google.com.
5 alt2.aspmx.l.google.com.
10 alt3.aspmx.l.google.com.
10 alt4.aspmx.l.google.com.
```

---

### Verify SPF/DKIM/DMARC Records

**noizylab.ca:**
```bash
dig +short TXT noizylab.ca
dig +short TXT _dmarc.noizylab.ca
dig +short TXT google._domainkey.noizylab.ca
dig +short TXT _mta-sts.noizylab.ca
dig +short TXT _smtp._tls.noizylab.ca
```

**Expected results:**
- **SPF:** `"v=spf1 include:_spf.google.com ~all"`
- **DMARC:** `"v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@noizylab.ca; fo=1"`
- **DKIM:** `"v=DKIM1; k=rsa; p=[YOUR_DKIM_PUBLIC_KEY]"`
- **MTA-STS:** `"v=STSv1; id=20240101000000"`
- **TLSRPT:** `"v=TLSRPTv1; rua=mailto:tlsrpt@noizylab.ca"`

**fishmusicinc.com:**
```bash
dig +short TXT fishmusicinc.com
dig +short TXT _dmarc.fishmusicinc.com
dig +short TXT google._domainkey.fishmusicinc.com
dig +short TXT _mta-sts.fishmusicinc.com
dig +short TXT _smtp._tls.fishmusicinc.com
```

**Expected results:** Same as above but for fishmusicinc.com

---

## Step 6: Verify MTA-STS Policy Files (After Hosting)

Once you've hosted the MTA-STS policy files, verify they're accessible:

```bash
curl https://mta-sts.noizylab.ca/.well-known/mta-sts.txt
curl https://mta-sts.fishmusicinc.com/.well-known/mta-sts.txt
```

**Expected output:**
```
version: STSv1
mode: enforce
mx: aspmx.l.google.com
mx: alt1.aspmx.l.google.com
mx: alt2.aspmx.l.google.com
mx: alt3.aspmx.l.google.com
mx: alt4.aspmx.l.google.com
max_age: 86400
```

---

## Step 7: Test Email Delivery

1. **Send test email** from `rsp@noizylab.ca` or `rp@fishmusicinc.com` to Gmail
2. **In Gmail:** Open email → Three dots → "Show original"
3. **Verify authentication:**
   - SPF: PASS ✓
   - DKIM: PASS ✓
   - DMARC: PASS ✓

---

## Quick Verification Script

Create and run this script to verify all DNS records:

```bash
#!/bin/bash
# verify-dns.sh

DOMAIN=$1
echo "Verifying DNS records for $DOMAIN..."
echo ""

echo "=== MX Records ==="
dig +short MX $DOMAIN
echo ""

echo "=== SPF Record ==="
dig +short TXT $DOMAIN | grep spf
echo ""

echo "=== DKIM Record ==="
dig +short TXT google._domainkey.$DOMAIN
echo ""

echo "=== DMARC Record ==="
dig +short TXT _dmarc.$DOMAIN
echo ""

echo "=== MTA-STS Record ==="
dig +short TXT _mta-sts.$DOMAIN
echo ""

echo "=== TLSRPT Record ==="
dig +short TXT _smtp._tls.$DOMAIN
echo ""
```

**Usage:**
```bash
chmod +x verify-dns.sh
./verify-dns.sh noizylab.ca
./verify-dns.sh fishmusicinc.com
```

---

## Rollback Commands

### Remove Specific Record

```bash
# List all resources
terraform state list

# Destroy specific resource
terraform destroy -target=cloudflare_record.mx_noizylab_1
terraform destroy -target=cloudflare_record.spf_noizylab
```

### Revert All Changes

```bash
terraform destroy
```

### Edit Configuration and Reapply

1. Edit `main.tf` or `terraform.tfvars`
2. Review changes:
   ```bash
   terraform plan
   ```
3. Apply changes:
   ```bash
   terraform apply
   ```

---

## Troubleshooting

### Terraform Not Found

```bash
# macOS (Homebrew)
brew install terraform

# Verify installation
terraform version
```

### Provider Authentication Errors

```bash
# Verify API token has correct permissions:
# - Zone.DNS (Edit)
# - Zone.Zone (Read)

# Test token manually:
curl -X GET "https://api.cloudflare.com/client/v4/user/tokens/verify" \
  -H "Authorization: Bearer YOUR_CF_API_TOKEN" \
  -H "Content-Type: application/json"
```

### DNS Records Not Updating

```bash
# Check DNS propagation
dig @8.8.8.8 +short MX noizylab.ca
dig @1.1.1.1 +short MX noizylab.ca

# Allow time for propagation (5-60 minutes)
# Cloudflare changes are usually instant
```

### DKIM Verification Fails

```bash
# Verify DKIM key format (no quotes, no headers)
# Should be base64 encoded string only

# Test DKIM record:
dig +short TXT google._domainkey.noizylab.ca

# Expected format: "v=DKIM1; k=rsa; p=YOUR_KEY_HERE"
```

---

## Complete Command Sequence (Copy-Paste)

```bash
# Step 1: Initialize
terraform init

# Step 2: Plan
terraform plan -out=tfplan

# Step 3: Review (JSON)
terraform show -json tfplan | jq '.planned_values.root_module.resources[] | {address, type, name, values}'

# Step 4: Apply
terraform apply tfplan

# Step 5: Verify MX
dig +short MX noizylab.ca
dig +short MX fishmusicinc.com

# Step 6: Verify TXT Records
dig +short TXT noizylab.ca
dig +short TXT _dmarc.noizylab.ca
dig +short TXT google._domainkey.noizylab.ca
dig +short TXT _mta-sts.noizylab.ca
dig +short TXT _smtp._tls.noizylab.ca

# Repeat for fishmusicinc.com
dig +short TXT fishmusicinc.com
dig +short TXT _dmarc.fishmusicinc.com
dig +short TXT google._domainkey.fishmusicinc.com
dig +short TXT _mta-sts.fishmusicinc.com
dig +short TXT _smtp._tls.fishmusicinc.com
```

---

## Next Steps

After successful deployment:

1. ✅ **Monitor DMARC Reports**
   - Check `dmarc-reports@noizylab.ca` for reports
   - Wait 7 days before tightening policy

2. ✅ **Host MTA-STS Policy Files**
   - Deploy policy files to web servers
   - Verify HTTPS access

3. ✅ **Test Email Delivery**
   - Send test emails to various providers
   - Verify authentication passes

4. ✅ **Gradual DMARC Enforcement**
   - Week 1: `p=none` (monitoring)
   - Week 2: `p=quarantine`
   - Week 3+: `p=reject`

See `UPGRADE_PLAN.md` for detailed timeline and procedures.

---

## Safety Reminders

⚠️ **Always run `terraform plan` before `terraform apply`**

⚠️ **Review the plan output carefully**

⚠️ **Keep backups of `main.tf` and `terraform.tfvars`**

⚠️ **Never commit `terraform.tfvars` to version control**

---

**Last Updated:** 2024-11-22  
**Version:** 1.0

