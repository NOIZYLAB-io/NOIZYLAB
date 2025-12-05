#!/usr/bin/env node

import fs from 'fs';

import path from 'path';

import { fileURLToPath } from 'url';

import { execSync } from 'child_process';



const __dirname = path.dirname(fileURLToPath(import.meta.url));

const S = path.join(process.cwd(), '.mc96.json');

const state = () => (fs.existsSync(S) ? JSON.parse(fs.readFileSync(S, 'utf8')) : {});

const save = (s) => fs.writeFileSync(S, JSON.stringify(s, null, 2));

const put = (f, c) => { fs.mkdirSync(path.dirname(path.join(process.cwd(),f)), { recursive: true }); fs.writeFileSync(path.join(process.cwd(),f), c); console.log(`+ ${f}`); };



const help = `

MC96 CLI — Local, hands-free super-cursor scaffold

Commands:

  init --scope @mc96 --name mc96-stack

  generate all | infra | packages | worker | ui | tests | webhook | pipeline

  agent <Name> --kind modern|legacy --mods text,vision,audio

  migrate [--env staging|production]

  prompts

  deploy [--env staging|production]

  setup:cloudflare

`;



const args = process.argv.slice(2);

const cmd = args[0];



function arg(flag, def) {

  const i = args.indexOf(flag);

  return i >= 0 ? args[i + 1] : def;

}



function init() {

  const scope = arg('--scope', '@mc96');

  const name = arg('--name', 'mc96-stack');

  save({ scope, name, env: 'dev' });



  put('package.json', JSON.stringify({

    name, private: true,

    workspaces: ["apps/*","packages/*","infra/*","tests"],

    scripts: {

      build: "echo build",

      lint: "echo lint",

      test: "echo test",

      migrate: "echo migrate D1 locally",

      "agent:new": "node mc96-cli.mjs agent",

      start: "echo 'Open Cursor and start coding locally.'"

    },

    devDependencies: { typescript: "^5.6.3", vitest: "^2.1.3" }

  }, null, 2));



  put('tsconfig.json', JSON.stringify({

    compilerOptions: { target: "ES2022", module: "ESNext", strict: true, jsx: "react-jsx" }

  }, null, 2));



  console.log('Initialized. Run `generate all` next.');

}



function genInfra() {

  put('infra/schemas/audit.sql', `

CREATE TABLE IF NOT EXISTS requests (

  id TEXT PRIMARY KEY,

  agent TEXT NOT NULL,

  method TEXT,

  path TEXT,

  ts INTEGER,

  ms INTEGER,

  status INTEGER

);

CREATE TABLE IF NOT EXISTS traces (

  id TEXT,

  step INTEGER,

  label TEXT,

  data TEXT,

  ts INTEGER,

  PRIMARY KEY (id, step)

);

`.trim());

}



function genPackages(scope) {

  put('packages/attribute-router/index.ts', `

import { chooseAgent } from './weights.js';

import { adapters } from './adapters.js';

export async function routeRequest({ req, env }) {

  const body = await req.json().catch(() => ({}));

  const attrs = { modality: body.modality ?? 'text', tokens: body.max_tokens ?? 1000, latency_target: body.latency_target ?? 1000, brand: body.brand ?? 'LIFELUV' };

  const agent = chooseAgent(attrs);

  const adapter = adapters[agent.kind];

  const result = await adapter.invoke(agent, body, env);

  return { result, agent };

}

`.trim());



  put('packages/attribute-router/weights.ts', `

export function chooseAgent(attrs) {

  const c = [

    { name: 'VisionFast', kind: 'modern', score: score(attrs, { l:1.0, q:0.85, c:0.8 }) },

    { name: 'modern-fast', kind: 'modern', score: score(attrs, { l:0.9, q:0.8, c:0.85 }) },

    { name: 'legacy-bridge', kind: 'legacy', score: score(attrs, { l:0.5, q:0.6, c:0.7 }) }

  ];

  return c.sort((a,b)=>b.score-a.score)[0];

}

function score(attrs, w){ const l = Math.max(0, 1 - (attrs.latency_target/2000)); return w.l*l + w.q*0.9 + w.c*0.85; }

`.trim());



  put('packages/attribute-router/adapters.ts', `

export const adapters = {

  modern: { invoke: modernInvoke },

  legacy: { invoke: legacyInvoke }

};

async function modernInvoke(agent, body, env) {

  // Local stub — replace with real endpoint when ready

  return { text: \`Modern(\${agent.name}) → \${body.prompt ?? ''}\` };

}

async function legacyInvoke(agent, body, env) {

  return { text: \`Legacy(\${agent.name}) → \${body.prompt ?? ''}\` };

}

`.trim());



  put('packages/audit-core/index.ts', `

export async function auditStart(env, { id, method, path }) {

  // Local stub: emulate D1 insert

  console.log('[audit:start]', { id, method, path });

}

export async function auditEnd(env, { id, ms, status, agent }) {

  console.log('[audit:end]', { id, ms, status, agent });

}

`.trim());



  put('packages/accessibility/useVoice.ts', `

export function useVoice(onResult) {

  const Speech = window.webkitSpeechRecognition || window.SpeechRecognition;

  const recognition = Speech ? new Speech() : null;

  let active = false;

  function toggle(){

    if(!recognition) return;

    if(active){ recognition.stop(); active=false; return; }

    recognition.lang='en-US'; recognition.continuous=false; recognition.interimResults=false;

    recognition.onresult = (e)=>{ const text = Array.from(e.results).map(r=>r[0].transcript).join(' '); onResult({ text }); };

    recognition.start(); active=true;

  }

  return { active, toggle };

}

`.trim());



  put('packages/accessibility/useSwitchScan.ts', `

export function useSwitchScan(select, intervalMs=1200) {

  let idx=0, timer;

  function start(){

    const tiles = Array.from(document.querySelectorAll('.tile'));

    timer = setInterval(()=>{

      tiles.forEach(t=>t.classList.remove('scan-focus'));

      const current = tiles[idx % tiles.length];

      current.classList.add('scan-focus'); current.focus(); idx++;

    }, intervalMs);

    window.addEventListener('keydown', (e)=>{ if(e.key==='Enter'||e.key===' ') select(document.activeElement); });

  }

  function stop(){ clearInterval(timer); }

  return { start, stop };

}

`.trim());

}



function genWorker(scope) {

  put('apps/worker-edge/src/index.ts', `

import { routeRequest } from '${scope}/attribute-router/index.js';

import { auditStart, auditEnd } from '${scope}/audit-core/index.js';



export default {

  async fetch(req, env, ctx) {

    const url = new URL(req.url);

    if (url.pathname === '/healthz') return new Response('OK');

    const id = 'local-' + Math.random().toString(36).slice(2);

    const start = Date.now();



    await auditStart(env, { id, method: req.method, path: url.pathname });

    const { result, agent } = await routeRequest({ req, env });



    const resp = new Response(JSON.stringify({ agent, result }), { headers: { 'content-type': 'application/json' } });

    await auditEnd(env, { id, ms: Date.now()-start, status: resp.status, agent: agent.name });

    return resp;

  }

};

`.trim());

}



function genUI(scope) {

  put('apps/cockpit-ui/src/components/Tile.tsx', `

export function Tile({ label, metric, onActivate }) {

  return (

    <button className="tile" aria-label={label} onClick={onActivate}>

      <div className="tile-label">{label}</div>

      <div className="tile-metric">{metric}</div>

    </button>

  );

}

`.trim());



  put('apps/cockpit-ui/src/commands.ts', `

export function parseCommand(text) {

  const s = text.toLowerCase();

  if (s.includes('run ritual')) return { action: 'run', payload: s.replace('run ritual','').trim() || 'default' };

  if (s.includes('open audit')) return { action: 'audit' };

  return { action: 'none' };

}

`.trim());



  put('apps/cockpit-ui/src/App.tsx', `

import { useState } from 'react';

import { Tile } from './components/Tile';

import { useVoice } from '${scope}/accessibility/useVoice.ts';

import { useSwitchScan } from '${scope}/accessibility/useSwitchScan.ts';

import { parseCommand } from './commands';

import './styles.css';



export default function App(){

  const [metric, setMetric] = useState('—');

  const [status, setStatus] = useState('Ready');

  const voice = useVoice(({ text }) => {

    const cmd = parseCommand(text);

    if (cmd.action === 'run') runRitual(cmd.payload);

    if (cmd.action === 'audit') setStatus('Opening audit…');

  });

  const scan = useSwitchScan(el => (el as HTMLButtonElement).click(), 1200);



  async function runRitual(prompt){

    // Local call placeholder — wire to your dev API

    const json = { agent: { name: 'VisionFast' }, result: { text: \`VisionFast → \${prompt}\` } };

    setMetric(\`\${json.agent.name} • \${json.result.text}\`);

    setStatus('Done');

  }



  return (

    <main className="grid">

      <Tile label="Run ritual" metric={metric} onActivate={() => runRitual('Hello world')} />

      <aside aria-live="polite" className="status">{status}</aside>

      <div className="controls">

        <button className="voice" onClick={voice.toggle} aria-label="Toggle voice">{voice.active ? 'Listening…' : 'Start voice'}</button>

        <button onClick={() => scan.start()} aria-label="Start scan">Start scan</button>

        <button onClick={() => scan.stop()} aria-label="Stop scan">Stop scan</button>

      </div>

    </main>

  );

}

`.trim());



  put('apps/cockpit-ui/src/styles.css', `

:root { color-scheme: light dark; }

.grid { display: grid; gap: 24px; padding: 24px; }

.tile { font-size: 18px; padding: 24px; min-height: 96px; min-width: 240px; border: 2px solid currentColor; border-radius: 12px; background: transparent; }

.tile:focus-visible { outline: 6px solid #5CC; }

.tile.scan-focus { outline: 8px solid #FFAA00; }

.tile-label { font-weight: 600; margin-bottom: 8px; }

.tile-metric { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }

.voice { padding: 16px 24px; border-radius: 12px; border: 2px dashed currentColor; }

.status { font-size: 16px; margin-top: 8px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }

`.trim());

}



function genTests() {

  put('tests/router.spec.ts', `

import { describe, it, expect } from 'vitest';

import { chooseAgent } from '../packages/attribute-router/weights';



describe('router', () => {

  it('prefers VisionFast for tight latency', () => {

    const a = chooseAgent({ latency_target: 500 });

    expect(a.name).toBe('VisionFast');

  });

});

`.trim());

}



function genWebhook(scope) {
  put('packages/webhook-normalizer/index.ts', `
import { detectPlatform } from './detector.js';
import { normalize } from './normalizers.js';
import { enrichWithAI, forwardToEndpoint } from './enrich.js';
import { auditStart, auditEnd, auditTrace } from '${scope}/audit-core/index.js';
import { withRetry } from '${scope}/retry/index.js';
import type { NormalizedWebhook, EnrichedEvent } from './types.js';

export async function processWebhook(request, env, ctx, options = {}) {
  // Implementation
}
`.trim());

  put('apps/webhook-worker/src/index.ts', `
import { processWebhook } from '${scope}/webhook-normalizer/index.js';
import { metrics } from '${scope}/observability/index.js';

export default {
  async fetch(request, env, ctx) {
    // Implementation
  }
};
`.trim());
}

function genPipeline(scope) {
  console.log('Generating complete pipeline: INGEST → NORMALIZE → AI → MC96 → REWARD...');
  
  // Ingestion Worker
  put('apps/ingestion-worker/src/index.ts', `
import { detectPlatform } from '${scope}/webhook-normalizer/detector.js';
import { auditStart, auditEnd, auditTrace } from '${scope}/audit-core/index.js';
import { metrics } from '${scope}/observability/index.js';
import { withRetry } from '${scope}/retry/index.js';

export default {
  async fetch(request, env, ctx) {
    // Ingestion worker implementation
  }
};
`.trim());

  put('apps/ingestion-worker/wrangler.toml', `
name = "mc96-ingestion-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "NOIZY_EVENTS"
id = "YOUR_KV_NAMESPACE_ID"

[vars]
NORMALIZER_ENDPOINT = "https://mc96-normalizer-worker.workers.dev"
`.trim());

  // Normalizer Worker
  put('apps/normalizer-worker/src/index.ts', `
import { processWebhook } from '${scope}/webhook-normalizer/index.js';
import { metrics } from '${scope}/observability/index.js';

export default {
  async fetch(request, env, ctx) {
    // Normalizer worker implementation
  }
};
`.trim());

  put('apps/normalizer-worker/wrangler.toml', `
name = "mc96-normalizer-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "NOIZY_EVENTS"
id = "YOUR_KV_NAMESPACE_ID"

[vars]
AI_ANALYSIS_ENDPOINT = "https://mc96-ai-worker.workers.dev"
`.trim());

  // AI Worker
  put('apps/ai-worker/src/index.ts', `
import { analyzeEvent } from '${scope}/ai-analyzer/index.js';
import { auditStart, auditEnd, auditTrace } from '${scope}/audit-core/index.js';
import { metrics } from '${scope}/observability/index.js';
import { withRetry } from '${scope}/retry/index.js';

export default {
  async fetch(request, env, ctx) {
    // AI worker implementation
  }
};
`.trim());

  put('apps/ai-worker/wrangler.toml', `
name = "mc96-ai-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "NOIZY_EVENTS"
id = "YOUR_KV_NAMESPACE_ID"

[ai]
binding = "AI"

[vars]
AI_MODEL = "@cf/meta/llama-3.1-8b-instruct"
MC96_ENDPOINT = "https://mc96-main.workers.dev"
`.trim());

  // MC96 Main
  put('apps/mc96-main/src/index.ts', `
import { auditStart, auditEnd, auditTrace } from '${scope}/audit-core/index.js';
import { metrics } from '${scope}/observability/index.js';
import { withRetry } from '${scope}/retry/index.js';

export default {
  async fetch(request, env, ctx) {
    // MC96 main implementation
  }
};
`.trim());

  put('apps/mc96-main/wrangler.toml', `
name = "mc96-main"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "NOIZY_EVENTS"
id = "YOUR_KV_NAMESPACE_ID"

[vars]
REWARD_ENGINE_ENDPOINT = "https://mc96-reward-engine.workers.dev"
`.trim());

  // Reward Engine
  put('apps/reward-engine/src/index.ts', `
import { auditStart, auditEnd, auditTrace } from '${scope}/audit-core/index.js';
import { metrics } from '${scope}/observability/index.js';
import { withRetry } from '${scope}/retry/index.js';

export default {
  async fetch(request, env, ctx) {
    // Reward engine implementation
  }
};
`.trim());

  put('apps/reward-engine/wrangler.toml', `
name = "mc96-reward-engine"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "NOIZY_EVENTS"
id = "YOUR_KV_NAMESPACE_ID"

[vars]
EMAIL_SERVICE_ENDPOINT = "https://email-service.workers.dev"
REWARD_STORAGE_ENDPOINT = "https://reward-storage.workers.dev"
`.trim());

  console.log('✅ Complete pipeline generated: INGEST → NORMALIZE → AI → MC96 → REWARD');
}

function generate(which) {

  const s = state(); const scope = s.scope || '@mc96';

  if (which === 'all') { genInfra(); genPackages(scope); genWorker(scope); genUI(scope); genTests(); genWebhook(scope); genPipeline(scope); return; }

  if (which === 'infra') genInfra();

  if (which === 'packages') genPackages(scope);

  if (which === 'worker') genWorker(scope);

  if (which === 'ui') genUI(scope);

  if (which === 'tests') genTests();

  if (which === 'webhook') genWebhook(scope);

  if (which === 'pipeline') genPipeline(scope);

}



function agent() {

  const name = args[1] || 'NewAgent';

  const kind = arg('--kind', 'modern');

  const mods = (arg('--mods', 'text') || 'text').split(',');



  // Manifest

  put(`manifests/agents/${name}.json`, JSON.stringify({

    name, kind, capabilities: mods, weights: { quality: 0.9, latency: 0.95, cost: 0.8 }

  }, null, 2));



  // Adapter stub injection

  const f = 'packages/attribute-router/adapters.ts';

  const src = fs.readFileSync(f, 'utf8');

  const stub = `

export async function ${name}Invoke(agent, body, env) {

  return { text: \`${name} → \${body.prompt ?? ''}\` };

}

`;

  const updated = src.replace('export const adapters = {', `${stub}\nexport const adapters = {`);

  fs.writeFileSync(f, updated);



  // Weight entry

  const wfile = 'packages/attribute-router/weights.ts';

  const wsrc = fs.readFileSync(wfile, 'utf8');

  const insert = `, { name: '${name}', kind: '${kind}', score: score(attrs, { l:1.0, q:0.9, c:0.8 }) }`;

  fs.writeFileSync(wfile, wsrc.replace('];', insert + '\n];'));



  console.log(`Agent ${name} scaffolded locally. Add endpoint when ready.`);

}



function migrate() {
  const env = arg('--env', 'staging');
  const schemaPath = 'infra/schemas/audit.sql';
  
  if (!fs.existsSync(schemaPath)) {
    console.error(`Schema file not found: ${schemaPath}`);
    process.exit(1);
  }

  console.log(`Migrating D1 database for environment: ${env}`);
  
  try {
    const schema = fs.readFileSync(schemaPath, 'utf8');
    console.log('Schema loaded. For Cloudflare D1, run:');
    console.log(`  wrangler d1 execute mc96-audit${env === 'production' ? '' : '-staging'} --file=${schemaPath}`);
    console.log('\nOr use the deploy command to automate this.');
  } catch (error) {
    console.error('Error reading schema:', error.message);
    process.exit(1);
  }
}

function setupCloudflare() {
  console.log('Setting up Cloudflare deployment configuration...');
  
  // Create root wrangler.toml if it doesn't exist
  const rootWrangler = 'wrangler.toml';
  if (!fs.existsSync(rootWrangler)) {
    put(rootWrangler, `
name = "mc96-worker-edge"
main = "apps/worker-edge/src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[env.production]
name = "mc96-worker-edge-prod"

[env.staging]
name = "mc96-worker-edge-staging"

[[env.production.d1_databases]]
binding = "DB"
database_name = "mc96-audit"
database_id = "YOUR_PROD_DATABASE_ID"

[[env.staging.d1_databases]]
binding = "DB"
database_name = "mc96-audit-staging"
database_id = "YOUR_STAGING_DATABASE_ID"

[build]
command = "npm run build"
`.trim());
  } else {
    console.log('⚠️  wrangler.toml already exists, skipping...');
  }

  const devVarsExample = '.dev.vars.example';
  if (!fs.existsSync(devVarsExample)) {
    put(devVarsExample, `
CLOUDFLARE_ACCOUNT_ID=your-account-id
CLOUDFLARE_API_TOKEN=your-api-token
`.trim());
  }

  console.log('✅ Cloudflare configuration ready.');
  console.log('📝 Update wrangler.toml with your database IDs.');
  console.log('📝 Copy .dev.vars.example to .dev.vars and fill in your credentials.');
}

function deploy() {
  const env = arg('--env', 'staging');
  console.log(`Deploying to Cloudflare ${env} environment...`);
  
  if (!fs.existsSync('wrangler.toml')) {
    console.error('wrangler.toml not found. Run "node mc96-cli.mjs setup:cloudflare" first.');
    process.exit(1);
  }

  try {
    console.log('Building worker...');
    execSync('npm run build', { stdio: 'inherit' });
    
    console.log(`Deploying worker to ${env}...`);
    const deployCmd = env === 'production' 
      ? 'wrangler deploy --env production'
      : 'wrangler deploy --env staging';
    
    execSync(deployCmd, { stdio: 'inherit' });
    
    console.log(`✅ Successfully deployed to ${env}!`);
  } catch (error) {
    console.error('Deployment failed:', error.message);
    process.exit(1);
  }
}



function prompts() {

  put('manifests/prompts/cursor.md', `

# Cursor prompt pack (local-first)



## Agent scaffold

"Create a new agent named VisionFast: vision + text. Strict types, resilience (retries, timeouts, circuit breaker), unit tests, audit hooks. Wire into attribute-router and adapters."



## Reliability refactor

"Convert adapters to async/await, add exponential backoff with jitter and per-adapter timeouts. Implement circuit breaker. Generate Vitest coverage for error paths."



## Accessibility audit

"WCAG 2.2 AA: aria-live narration, focus-visible, switch scanning interval control, keyboard-only navigation tests."



## Observability

"Add tiles for latency, error rate, queue depth, circuit state. Write labeled audit traces and show cockpit summaries."

`.trim());

}



if (!cmd) { console.log(help); process.exit(0); }

if (cmd === 'init') init();

else if (cmd === 'generate') generate(args[1] || 'all');

else if (cmd === 'agent') agent();

else if (cmd === 'migrate') migrate();

else if (cmd === 'prompts') prompts();

else if (cmd === 'deploy') deploy();

else if (cmd === 'setup:cloudflare') setupCloudflare();

else { console.log(help); }

