#!/bin/bash
# CURSOR WORKSPACE BOOTSTRAP SCRIPT
# Creates full NOIZYLAB OS repo structure instantly

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "🚀 Bootstrapping NOIZYLAB OS workspace..."

# Core directories
mkdir -p workers/{super-worker,agent-arbiter,dreamchamber,intake,events}
mkdir -p portal/{public,src/{components,pages,utils},api}
mkdir -p ai/{router,agents}
mkdir -p ipad-app/{SwiftUI,Assets}
mkdir -p db/{schema,queries}
mkdir -p migrations/sql
mkdir -p router/{routes,middleware}
mkdir -p scripts

# Worker configs
cat > workers/super-worker/wrangler.toml << 'EOF'
name = "super-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[env.production]
routes = [{ pattern = "api.noizylab.ca/*", zone_name = "noizylab.ca" }]
EOF

# Package files
cat > package.json << 'EOF'
{
  "name": "noizylab-os",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "workers/*",
    "portal",
    "ai/router"
  ],
  "scripts": {
    "dev": "wrangler dev",
    "deploy": "wrangler deploy",
    "migrate": "wrangler d1 migrations apply",
    "db:studio": "wrangler d1 execute --local"
  },
  "devDependencies": {
    "@cloudflare/workers-types": "^4.20240101.0",
    "wrangler": "^3.0.0",
    "typescript": "^5.3.0"
  }
}
EOF

# TypeScript config
cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "bundler",
    "types": ["@cloudflare/workers-types"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["workers/**/*", "ai/**/*"],
  "exclude": ["node_modules"]
}
EOF

# Git ignore
cat > .gitignore << 'EOF'
node_modules/
.wrangler/
dist/
*.log
.env
.env.local
.DS_Store
EOF

# Cursor rules
mkdir -p .cursor/rules
cat > .cursor/rules/noizylab-os.md << 'EOF'
# NOIZYLAB OS Development Rules

- Use TypeScript for all workers
- Cloudflare Workers runtime (no Node.js APIs)
- D1 for database
- R2 for storage
- KV for caching
- Keep workers lightweight (<10MB)
- Use wrangler for local dev
EOF

echo "✅ Workspace bootstrapped!"
echo "📁 Structure created in: $ROOT"

