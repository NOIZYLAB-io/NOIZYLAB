#!/usr/bin/env bash
set -euo pipefail

VOICE=0
for a in "$@"; do [[ "$a" == "--speak" ]] && VOICE=1; done
say_(){ [[ $VOICE -eq 1 ]] && command -v say >/dev/null 2>&1 && say "$1" || true; printf ">> %s\n" "$1"; }
need(){ command -v "$1" >/dev/null 2>&1 || { echo "Missing $1. Install and retry."; exit 1; }; }
need node; need npm

ROOT="$(pwd)"
CLI_DIR="$ROOT/m2g-claude"
MCP_DIR="$ROOT/claude-mcp"

mkdir -p "$CLI_DIR" "$MCP_DIR" "$CLI_DIR/bin" "$CLI_DIR/src" "$MCP_DIR/tools"

say_ "Creating Claude CLI (m2g-claude)"

cat > "$CLI_DIR/package.json" <<'JSON'
{
  "name": "m2g-claude",
  "version": "1.0.0",
  "type": "module",
  "bin": { "m2g-claude": "bin/m2g-claude" },
  "dependencies": { "dotenv": "^16.4.5" }
}
JSON

cat > "$CLI_DIR/bin/m2g-claude" <<'NODE'
#!/usr/bin/env node
import("../src/cli.js").catch(e => { console.error(e); process.exit(1); });
NODE
chmod +x "$CLI_DIR/bin/m2g-claude"

cat > "$CLI_DIR/src/stream.js" <<'JS'
export async function streamAnthropic({ endpoint, apiKey, body, onDelta }) {
  const headers = {
    "content-type": "application/json",
    ...(apiKey ? { "x-api-key": apiKey, "anthropic-version": "2023-06-01" } : {})
  };
  
  const resp = await fetch(endpoint, { method: "POST", headers, body: JSON.stringify(body) });
  if (!resp.ok) {
    const errText = await resp.text();
    throw new Error(`HTTP ${resp.status}: ${errText}`);
  }
  
  const ct = resp.headers.get("content-type") || "";
  if (!ct.includes("text/event-stream")) {
    const data = await resp.json();
    const text = data?.content?.[0]?.text || data?.output_text || JSON.stringify(data);
    onDelta(text, true);
    return;
  }
  
  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buf = "";
  
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    const lines = buf.split("\n");
    buf = lines.pop() || "";
    
    for (const line of lines) {
      const s = line.trim();
      if (!s || s.startsWith(":")) continue;
      if (s.startsWith("data:")) {
        const json = s.slice(5).trim();
        if (json === "[DONE]") {
          onDelta("", true);
          continue;
        }
        try {
          const evt = JSON.parse(json);
          if (evt.type === "content_block_delta" && evt.delta?.text) {
            onDelta(evt.delta.text, false);
          }
          if (evt.type === "message_delta" && evt.delta?.text) {
            onDelta(evt.delta.text, false);
          }
          if (evt.type === "message_stop") {
            onDelta("", true);
          }
        } catch (parseErr) {
          // Ignore parse errors for non-JSON lines
        }
      }
    }
  }
  
  // Ensure we signal completion if stream ends without message_stop
  onDelta("", true);
}
JS

cat > "$CLI_DIR/src/speech.js" <<'JS'
import { spawnSync } from "node:child_process";

export function maybeSpeak(text, voice) {
  if (!voice || !text) return;
  try {
    // Sanitize text to prevent command injection
    const sanitized = text.slice(0, 200).replace(/["`$\\]/g, "");
    spawnSync("say", ["-v", voice, sanitized], { stdio: "ignore", timeout: 30000 });
  } catch (err) {
    // Silently ignore speech errors
  }
}
JS

cat > "$CLI_DIR/src/cli.js" <<'JS'
import "dotenv/config";
import { streamAnthropic } from "./stream.js";
import { maybeSpeak } from "./speech.js";

async function main() {
  const args = process.argv.slice(2);
  const flags = new Map();
  let prompt = "";
  
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a.startsWith("--")) {
      if (a.includes("=")) {
        const [k, v] = a.slice(2).split("=");
        flags.set(k, v);
      } else {
        const k = a.slice(2);
        const nextArg = args[i + 1];
        if (nextArg && !nextArg.startsWith("--")) {
          flags.set(k, nextArg);
          i++;
        } else {
          flags.set(k, "true");
        }
      }
    } else {
      prompt += (prompt ? " " : "") + a;
    }
  }
  
  if (!prompt) {
    console.error("Usage: m2g-claude <prompt> [--model MODEL] [--speak VOICE] [--json] [--system SYSTEM]");
    process.exit(1);
  }

  const model = flags.get("model") || process.env.M2G_MODEL || "claude-sonnet-4-20250514";
  const speak = flags.get("speak") || "";
  const jsonMode = flags.has("json") && flags.get("json") !== "false";
  const system = flags.get("system") || "You are M2G's Claude CLI assistant.";
  const budgetUsd = Number(flags.get("budget") || process.env.M2G_BUDGET_USD || 0);
  const maxTokens = Number(flags.get("maxTokens") || process.env.M2G_MAX_TOKENS || 1024);

  const endpointMode = (flags.get("endpoint") || process.env.M2G_ENDPOINT || "direct").toLowerCase();
  let endpoint, apiKey;
  
  if (endpointMode === "relay") {
    const base = (process.env.M2G_RELAY_BASE || "").replace(/\/$/, "");
    if (!base) {
      throw new Error("Set M2G_RELAY_BASE to your Worker origin, e.g. https://ai-genius.workers.dev");
    }
    endpoint = `${base}/v1/relay?provider=anthropic`;
    apiKey = null; // relay holds the secret
  } else {
    endpoint = process.env.ANTHROPIC_BASE || "https://api.anthropic.com/v1/messages";
    apiKey = process.env.ANTHROPIC_API_KEY;
    if (!apiKey) {
      throw new Error("Missing ANTHROPIC_API_KEY environment variable");
    }
  }

  // Build the message content
  let messageContent = prompt;
  if (jsonMode) {
    messageContent = `Answer in STRICT JSON format only. No markdown, no explanation outside JSON.\n\n${prompt}`;
  }

  const body = {
    model,
    max_tokens: maxTokens,
    stream: true,
    system,
    messages: [{ role: "user", content: messageContent }]
  };

  const start = Date.now();
  let collected = "";
  let finished = false;

  await streamAnthropic({
    endpoint,
    apiKey,
    body,
    onDelta: (chunk, done) => {
      if (finished) return;
      
      if (chunk) {
        process.stdout.write(chunk);
        collected += chunk;
      }
      
      if (done && !finished) {
        finished = true;
        process.stdout.write("\n");
        
        const usdApprox = estimateUsd(prompt, collected, model);
        if (budgetUsd && usdApprox > budgetUsd) {
          console.error(`⚠️  Approx $${usdApprox.toFixed(4)} exceeded budget $${budgetUsd.toFixed(4)}`);
          process.exitCode = 2;
        }
        
        maybeSpeak(collected.slice(0, 180), speak);
        
        const ms = Date.now() - start;
        process.stderr.write(`\n✓ ${model} | ${ms}ms | ~$${usdApprox.toFixed(4)}\n`);
      }
    }
  });
}

function estimateUsd(input, output, model) {
  const inTokens = Math.ceil((input || "").length / 4);
  const outTokens = Math.ceil((output || "").length / 4);
  
  // Default costs for Claude 3.5 Sonnet (per 1K tokens)
  let inCost = Number(process.env.ANTHROPIC_IN_COST || 0.003);
  let outCost = Number(process.env.ANTHROPIC_OUT_COST || 0.015);
  
  // Adjust for different models
  if (model.includes("opus")) {
    inCost = 0.015;
    outCost = 0.075;
  } else if (model.includes("haiku")) {
    inCost = 0.00025;
    outCost = 0.00125;
  }
  
  return (inTokens / 1000) * inCost + (outTokens / 1000) * outCost;
}

main().catch(err => {
  console.error("Error:", err.message);
  process.exit(1);
});
JS

cat > "$CLI_DIR/.env.example" <<'ENV'
# ========================================
# M2G-CLAUDE CONFIGURATION
# ========================================

# --- DIRECT MODE (uses your Anthropic API key) ---
ANTHROPIC_API_KEY=sk-ant-api03-...

# --- RELAY MODE (route through Cloudflare ai-proxy Worker) ---
# M2G_ENDPOINT=relay
# M2G_RELAY_BASE=https://ai-genius.workers.dev

# --- OPTIONAL SETTINGS ---
# Default model (claude-sonnet-4-20250514, claude-3-5-sonnet-20241022, etc.)
# M2G_MODEL=claude-sonnet-4-20250514

# Max tokens for responses
# M2G_MAX_TOKENS=1024

# Budget limit per request (USD)
# M2G_BUDGET_USD=0.10

# Cost per 1K tokens (for budget calculation)
# ANTHROPIC_IN_COST=0.003
# ANTHROPIC_OUT_COST=0.015
ENV

cat > "$CLI_DIR/README.md" <<'MD'
# m2g-claude

Local CLI for Anthropic Claude with streaming, JSON mode, budgets, and optional voice.

## Installation

```bash
npm install
cp .env.example .env  # Edit with your ANTHROPIC_API_KEY
npm link
```

## Usage

```bash
# Basic usage
m2g-claude "What is the capital of France?"

# With specific model
m2g-claude "Explain quantum computing" --model claude-3-5-sonnet-20241022

# JSON output mode
m2g-claude "List 3 programming languages" --json

# With voice output (macOS only)
m2g-claude "Hello world" --speak Samantha

# Custom system prompt
m2g-claude "Write a haiku" --system "You are a poet"

# With budget limit
m2g-claude "Write an essay" --budget 0.05

# Relay mode (via Cloudflare Worker)
M2G_ENDPOINT=relay M2G_RELAY_BASE=https://ai-genius.workers.dev \
  m2g-claude "Hello via relay"
```

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `--model` | Claude model to use | `claude-sonnet-4-20250514` |
| `--speak` | Voice name for TTS (macOS) | disabled |
| `--json` | Request JSON output | false |
| `--system` | Custom system prompt | default |
| `--budget` | Max USD per request | unlimited |
| `--maxTokens` | Max response tokens | 1024 |
| `--endpoint` | `direct` or `relay` | direct |

## Environment Variables

See `.env.example` for all configuration options.
MD

say_ "Creating Claude MCP server (claude-mcp)"

cat > "$MCP_DIR/package.json" <<'JSON'
{
  "name": "claude-mcp",
  "version": "1.0.0",
  "type": "module",
  "main": "server.js",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0"
  }
}
JSON

cat > "$MCP_DIR/server.js" <<'JS'
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import * as fs from "node:fs/promises";

const server = new Server(
  { name: "m2g-claude-mcp", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Define available tools
const tools = [
  {
    name: "m2g_files",
    description: "Read or write small text files (UTF-8). Use op='read' to read, op='write' to write.",
    inputSchema: {
      type: "object",
      properties: {
        op: { type: "string", enum: ["read", "write"], description: "Operation: read or write" },
        path: { type: "string", description: "File path" },
        text: { type: "string", description: "Text content (for write operation)" }
      },
      required: ["op", "path"]
    }
  },
  {
    name: "m2g_fetch",
    description: "HTTP GET request to fetch text or JSON content from a URL.",
    inputSchema: {
      type: "object",
      properties: {
        url: { type: "string", description: "URL to fetch" }
      },
      required: ["url"]
    }
  },
  {
    name: "m2g_relay",
    description: "Call Cloudflare ai-proxy relay endpoint with Anthropic provider.",
    inputSchema: {
      type: "object",
      properties: {
        base: { type: "string", description: "Base URL of the relay Worker" },
        model: { type: "string", description: "Claude model name" },
        content: { type: "string", description: "User message content" },
        system: { type: "string", description: "System prompt (optional)" },
        max_tokens: { type: "number", description: "Max tokens (default 1024)" }
      },
      required: ["base", "model", "content"]
    }
  }
];

// Handle list tools request
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "m2g_files": {
        const { op, path, text } = args;
        if (op === "read") {
          const content = await fs.readFile(path, "utf8");
          return { content: [{ type: "text", text: content }] };
        } else if (op === "write") {
          await fs.writeFile(path, text || "", "utf8");
          return { content: [{ type: "text", text: `Successfully wrote to ${path}` }] };
        }
        throw new Error(`Invalid operation: ${op}`);
      }

      case "m2g_fetch": {
        const { url } = args;
        const response = await fetch(url);
        const ct = response.headers.get("content-type") || "";
        
        if (ct.includes("application/json")) {
          const json = await response.json();
          return { 
            content: [{ 
              type: "text", 
              text: JSON.stringify({ status: response.status, json }, null, 2) 
            }] 
          };
        }
        
        const text = await response.text();
        return { 
          content: [{ 
            type: "text", 
            text: JSON.stringify({ status: response.status, text }, null, 2) 
          }] 
        };
      }

      case "m2g_relay": {
        const { base, model, content, system, max_tokens = 1024 } = args;
        const url = `${base.replace(/\/$/, "")}/v1/relay?provider=anthropic`;
        
        const body = {
          model,
          max_tokens,
          stream: false,
          system: system || "M2G MCP assistant",
          messages: [{ role: "user", content }]
        };
        
        const response = await fetch(url, {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(body)
        });
        
        const ct = response.headers.get("content-type") || "";
        const data = ct.includes("json") ? await response.json() : await response.text();
        
        return { 
          content: [{ 
            type: "text", 
            text: JSON.stringify({ status: response.status, data }, null, 2) 
          }] 
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      content: [{ type: "text", text: `Error: ${error.message}` }],
      isError: true
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("M2G Claude MCP server running on stdio");
}

main().catch((error) => {
  console.error("Failed to start MCP server:", error);
  process.exit(1);
});
JS

cat > "$MCP_DIR/README.md" <<'MD'
# claude-mcp

MCP (Model Context Protocol) server exposing m2g tools for Claude Desktop and other MCP clients.

## Tools Available

| Tool | Description |
|------|-------------|
| `m2g_files` | Read/write text files |
| `m2g_fetch` | HTTP GET requests |
| `m2g_relay` | Proxy to Cloudflare ai-proxy Worker |

## Installation

```bash
cd claude-mcp
npm install
```

## Configuration

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "m2g-claude": {
      "command": "node",
      "args": ["/full/path/to/claude-mcp/server.js"]
    }
  }
}
```

### VS Code / Cursor

Add to your MCP configuration:

```json
{
  "servers": {
    "m2g-claude": {
      "command": "node",
      "args": ["./claude-mcp/server.js"]
    }
  }
}
```

## Usage Examples

Once configured, you can ask Claude to use these tools:

- "Read the contents of package.json using m2g_files"
- "Fetch https://api.github.com/users/octocat using m2g_fetch"
- "Use m2g_relay to ask Claude about TypeScript via the ai-genius worker"
MD

say_ "Installing dependencies"

if ! ( cd "$CLI_DIR" && npm install --loglevel=error ); then
  echo "Error: Failed to install CLI dependencies"
  exit 1
fi

if ! ( cd "$CLI_DIR" && npm link --loglevel=error 2>/dev/null ); then
  echo "Note: npm link failed (may need sudo). You can run directly with: node $CLI_DIR/bin/m2g-claude"
fi

if ! ( cd "$MCP_DIR" && npm install --loglevel=error ); then
  echo "Error: Failed to install MCP dependencies"
  exit 1
fi

say_ "Done. Configure environment and test."

cat <<NEXT

══════════════════════════════════════════════════════════════
  M2G-CLAUDE SETUP COMPLETE
══════════════════════════════════════════════════════════════

📁 Created:
   • $CLI_DIR (CLI tool)
   • $MCP_DIR (MCP server)

🔧 CONFIGURATION

1. Set up your API key (choose one method):

   # DIRECT MODE - uses your Anthropic API key
   cd "$CLI_DIR"
   cp .env.example .env
   # Edit .env and set: ANTHROPIC_API_KEY=sk-ant-...

   # RELAY MODE - route via Cloudflare Worker
   export M2G_ENDPOINT=relay
   export M2G_RELAY_BASE=https://ai-genius.workers.dev

🧪 TEST COMMANDS

   # CLI (direct mode):
   m2g-claude "Hello from M2G!" --model claude-sonnet-4-20250514

   # CLI (relay mode):
   M2G_ENDPOINT=relay M2G_RELAY_BASE=https://ai-genius.workers.dev \\
     m2g-claude "Test via relay" --speak Samantha

   # CLI with JSON output:
   m2g-claude "List 3 colors" --json

   # MCP server (start manually):
   node "$MCP_DIR/server.js"

🗑️  ROLLBACK

   npm unlink -g m2g-claude 2>/dev/null || true
   rm -rf "$CLI_DIR" "$MCP_DIR"

══════════════════════════════════════════════════════════════
NEXT

say_ "Claude CLI + MCP server installed successfully!"
