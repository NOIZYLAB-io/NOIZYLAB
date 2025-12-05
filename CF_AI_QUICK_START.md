# Cloudflare AI - Complete CLI Quick Start

## 🚀 Bring Cloudflare AI Up to Speed

### One Command Full Setup

```bash
cd noizylab-os
./scripts/cf-ai-cli.sh full
```

This does **everything**:
- ✅ Checks prerequisites
- ✅ Sets up worker
- ✅ Configures Cloudflare
- ✅ Creates D1 database
- ✅ Creates KV namespace
- ✅ Creates R2 bucket
- ✅ Applies migrations

---

## 📋 Individual Commands

```bash
# Check what's installed
./scripts/cf-ai-cli.sh check

# Setup worker files
./scripts/cf-ai-cli.sh setup

# Configure Cloudflare (login, etc.)
./scripts/cf-ai-cli.sh config

# Setup database
./scripts/cf-ai-cli.sh db

# Setup KV
./scripts/cf-ai-cli.sh kv

# Setup R2
./scripts/cf-ai-cli.sh r2

# Test locally
./scripts/cf-ai-cli.sh test

# Deploy
./scripts/cf-ai-cli.sh deploy

# Check status
./scripts/cf-ai-cli.sh status

# Quick test
./scripts/cf-ai-cli.sh quick-test
```

---

## 🎯 After Full Setup

1. **Update wrangler.toml** with your IDs:
   - Database ID (from `wrangler d1 list`)
   - KV namespace ID (from `wrangler kv:namespace list`)
   - R2 bucket name

2. **Test locally:**
   ```bash
   ./scripts/cf-ai-cli.sh test
   ```

3. **Deploy:**
   ```bash
   ./scripts/cf-ai-cli.sh deploy
   ```

---

## 🔥 Ready for Forward Moves!

Once setup is complete, your Cloudflare AI is:
- ✅ Fully configured
- ✅ Database ready
- ✅ Caching enabled
- ✅ Ready to deploy
- ✅ Production-ready

---

## 📞 Need Help?

Run the interactive menu:
```bash
./scripts/cf-ai-cli.sh
```

Or check status anytime:
```bash
./scripts/cf-ai-cli.sh status
```

