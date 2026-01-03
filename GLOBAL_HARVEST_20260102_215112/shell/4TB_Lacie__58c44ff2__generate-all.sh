#!/bin/bash
# GENERATE ALL COMPONENTS
# Creates Portal UI, Intake App, MC96 Dashboard, TeamViewer, Auto-deploy

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "🔥 Generating all components..."

# Portal UI v2
mkdir -p portal/src/{components,pages,api}
cat > portal/src/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
  <title>NoizyLab Portal</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
EOF

# Intake iPad App Endpoint
mkdir -p workers/intake/src
cat > workers/intake/src/index.ts << 'EOF'
// INTAKE IPAD APP ENDPOINT
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    if (req.method === "POST") {
      const data = await req.json();
      const id = crypto.randomUUID();
      
      await env.DB.prepare(
        `INSERT INTO clients (id, name, email, plan, created_at)
         VALUES (?, ?, ?, ?, ?)`
      ).bind(id, data.name, data.email, data.plan, Date.now()).run();
      
      return new Response(JSON.stringify({ ok: true, id }), {
        headers: { "Content-Type": "application/json" }
      });
    }
    
    return new Response("Intake API", { status: 200 });
  }
};
EOF

# MC96 Dashboard API
mkdir -p workers/mc96/src
cat > workers/mc96/src/index.ts << 'EOF'
// MC96 DASHBOARD API
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    
    if (url.pathname === "/api/stats") {
      const clients = await env.DB.prepare("SELECT COUNT(*) as count FROM clients").first();
      const tickets = await env.DB.prepare("SELECT COUNT(*) as count FROM tickets WHERE status != 'closed'").first();
      
      return new Response(JSON.stringify({
        clients: clients?.count || 0,
        open_tickets: tickets?.count || 0
      }), {
        headers: { "Content-Type": "application/json" }
      });
    }
    
    return new Response("MC96 Dashboard API", { status: 200 });
  }
};
EOF

# TeamViewer Integration Worker
mkdir -p workers/teamviewer/src
cat > workers/teamviewer/src/index.ts << 'EOF'
// TEAMVIEWER INTEGRATION WORKER
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    
    if (url.pathname === "/api/connect") {
      const { device_id } = await req.json();
      
      // TeamViewer API integration
      const session = await fetch(`https://webapi.teamviewer.com/api/v1/sessions`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${env.TEAMVIEWER_TOKEN}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ device_id })
      });
      
      return new Response(JSON.stringify(await session.json()), {
        headers: { "Content-Type": "application/json" }
      });
    }
    
    return new Response("TeamViewer API", { status: 200 });
  }
};
EOF

# Auto-deployment script
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash
# AUTO-DEPLOYMENT SCRIPT
set -e

echo "🚀 Deploying NOIZYLAB OS..."

# Deploy super-worker
cd workers/super-worker
wrangler deploy
cd ../..

# Deploy intake
cd workers/intake
wrangler deploy
cd ../..

# Deploy MC96
cd workers/mc96
wrangler deploy
cd ../..

# Apply migrations
wrangler d1 migrations apply noizylab-db --remote

echo "✅ Deployment complete!"
EOF

chmod +x scripts/deploy.sh

# Create tar.gz export script
cat > scripts/export-repo.sh << 'EOF'
#!/bin/bash
# EXPORT ENTIRE REPO AS TAR.GZ
set -e

VERSION=$(date +%Y%m%d_%H%M%S)
OUTPUT="noizylab-os-${VERSION}.tar.gz"

echo "📦 Creating export: $OUTPUT"

tar -czf "$OUTPUT" \
  --exclude='node_modules' \
  --exclude='.wrangler' \
  --exclude='.git' \
  --exclude='*.log' \
  .

echo "✅ Export created: $OUTPUT"
ls -lh "$OUTPUT"
EOF

chmod +x scripts/export-repo.sh

echo "✅ All components generated!"
echo ""
echo "📁 Created:"
echo "   • Portal UI structure"
echo "   • Intake iPad App endpoint"
echo "   • MC96 Dashboard API"
echo "   • TeamViewer Integration Worker"
echo "   • Auto-deployment script"
echo "   • Export script"

