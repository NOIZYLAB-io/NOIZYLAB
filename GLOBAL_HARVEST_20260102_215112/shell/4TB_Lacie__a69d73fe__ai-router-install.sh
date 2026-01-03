#!/bin/bash
set -e

echo "🚀 Installing NoizyLab Multi-AI Router..."

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
AI_DIR="$BASE/ai"
SUPERCODE_DIR="$BASE/supercode"

# Create directories
mkdir -p "$AI_DIR/router/bin"
mkdir -p "$AI_DIR/agents"

# Install Node dependencies if needed
if [ -f "$AI_DIR/router/package.json" ]; then
    cd "$AI_DIR/router"
    npm install --silent
fi

# Create CLI wrappers
cat > "$AI_DIR/router/bin/cfw-cli.js" << 'EOF'
#!/usr/bin/env node
/**
 * Cloudflare AI CLI
 */
import { config } from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
config({ path: join(__dirname, '../../.env') });

const prompt = process.argv.slice(2).join(' ');
if (!prompt) {
  console.error('Usage: cfw <prompt>');
  process.exit(1);
}

// Call Cloudflare AI Worker
const response = await fetch('https://ai-router.noizylab.workers.dev/ai', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    provider: 'cloudflare',
    prompt 
  })
});

const data = await response.json();
console.log(data.response || data.error);
EOF

cat > "$AI_DIR/router/bin/gemini-cli.js" << 'EOF'
#!/usr/bin/env node
/**
 * Gemini CLI
 */
import { config } from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
config({ path: join(__dirname, '../../.env') });

const prompt = process.argv.slice(2).join(' ');
if (!prompt) {
  console.error('Usage: gemini <prompt>');
  process.exit(1);
}

if (!process.env.GEMINI_API_KEY) {
  console.error('❌ GEMINI_API_KEY not set in .env');
  process.exit(1);
}

const response = await fetch('https://ai-router.noizylab.workers.dev/ai', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    provider: 'gemini',
    prompt 
  })
});

const data = await response.json();
console.log(data.response || data.error);
EOF

cat > "$AI_DIR/router/bin/claude-cli.js" << 'EOF'
#!/usr/bin/env node
/**
 * Claude CLI
 */
import { config } from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
config({ path: join(__dirname, '../../.env') });

const prompt = process.argv.slice(2).join(' ');
if (!prompt) {
  console.error('Usage: claude <prompt>');
  process.exit(1);
}

if (!process.env.ANTHROPIC_API_KEY) {
  console.error('❌ ANTHROPIC_API_KEY not set in .env');
  process.exit(1);
}

const response = await fetch('https://ai-router.noizylab.workers.dev/ai', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    provider: 'claude',
    prompt 
  })
});

const data = await response.json();
console.log(data.response || data.error);
EOF

# Make executables
chmod +x "$AI_DIR/router/bin/cfw-cli.js"
chmod +x "$AI_DIR/router/bin/gemini-cli.js"
chmod +x "$AI_DIR/router/bin/claude-cli.js"

# Create symlinks
echo "➡️  Creating global symlinks..."
sudo ln -sf "$AI_DIR/router/bin/cfw-cli.js" /usr/local/bin/cfw 2>/dev/null || true
sudo ln -sf "$AI_DIR/router/bin/gemini-cli.js" /usr/local/bin/gemini 2>/dev/null || true
sudo ln -sf "$AI_DIR/router/bin/claude-cli.js" /usr/local/bin/claude 2>/dev/null || true

# Deploy AI Router Worker
echo "➡️  Deploying AI Router Worker..."
if [ -d "$AI_DIR/router" ] && [ -f "$AI_DIR/router/wrangler.toml" ]; then
    cd "$AI_DIR/router"
    wrangler deploy 2>&1 || echo "⚠️  AI Router deployment failed (may need manual setup)"
fi

# Test providers
echo ""
echo "➡️  Testing Providers..."
echo ""

if command -v cfw >/dev/null 2>&1; then
    echo "  ✓ cfw CLI installed"
    # cfw "Hello from Cloudflare" || echo "  ⚠️  Cloudflare AI test failed"
fi

if command -v gemini >/dev/null 2>&1; then
    echo "  ✓ gemini CLI installed"
    # gemini "Hello from Gemini" || echo "  ⚠️  Gemini test failed"
fi

if command -v claude >/dev/null 2>&1; then
    echo "  ✓ claude CLI installed"
    # claude "Hello from Claude" || echo "  ⚠️  Claude test failed"
fi

echo ""
echo "✨ Multi-AI Router Installation Complete!"
echo ""
echo "Usage:"
echo "  cfw <prompt>      - Use Cloudflare AI"
echo "  gemini <prompt>    - Use Google Gemini"
echo "  claude <prompt>    - Use Anthropic Claude"
echo ""

