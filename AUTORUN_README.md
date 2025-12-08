**Mission Autorun — Usage & Outputs**

**Purpose**
- Run core diagnostics quickly: MTU validation, storage speed baseline, Wrangler auth/dry-run, and environment snapshots.

**Prerequisites**
- macOS with zsh; Cloudflare Wrangler installed (`npm i -g wrangler`).
- Access to `/Volumes/12TB` or adjust the path in `autorun.sh`.

**Run**
```
chmod +x ./autorun.sh
./autorun.sh
```

**Outputs**
- Created under `mission-run-YYYYMMDD-HHMMSS/`:
  - `mtu.txt` — MTU status for Ethernet/Thunderbolt/en0
  - `speedtest.txt` — 16GiB `dd` test with `oflag=direct`
  - `wrangler.txt` — `whoami` and `deploy --dry-run`
  - `env.txt` — Spotlight/DNS/uptime snapshot
  - `run.log` — overall steps and status

**Next Steps**
- Tune storage per `STORAGE_TUNING.md` and re-run to compare MB/s.
- If `wrangler deploy` fails, follow `WRANGLER_DEPLOY_GUIDE.md`.
- Track metrics in `KPI_DASHBOARD.md`.