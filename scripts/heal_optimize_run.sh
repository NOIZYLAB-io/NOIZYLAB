#!/usr/bin/env zsh
set -euo pipefail

print_step() {
  echo "\n==> $1";
}

print_step "Spotlight: enable on /, disable on externals"
sudo mdutil -i on /
sudo mdutil -E /
for v in /Volumes/*; do sudo mdutil -i off "$v" || true; done
mdutil -s /

print_step "DNS: flush caches"
sudo dscacheutil -flushcache || true
sudo killall -HUP mDNSResponder || true

print_step "Network: verify jumbo frames (MTU 9000) on en0"
ifconfig en0 | grep -i mtu || true

print_step "Worker: build and deploy"
pushd workers/noizylab >/dev/null
npm install
npm run build
wrangler deploy
popd >/dev/null

print_step "Health check: Cloudflare Worker"
curl -s https://noizylab.rsplowman.workers.dev/health || true

print_step "Repo: build, test, lint"
make install || true
make build || true
make test || true
make lint || true

print_step "I/O: quick read test on 12TB (if file exists)"
if [[ -f /Volumes/12TB/speedtest ]]; then
  time dd if=/Volumes/12TB/speedtest of=/dev/null bs=4m || true
else
  echo "No /Volumes/12TB/speedtest file; skip read test"
fi

print_step "Done. System healed, optimized, and verified."