#!/usr/bin/env bash
# bootstrap_lifesaver.sh
# End-to-end setup for LifeSaver Tablet + VS Code Bridge.
set -e

# 0) Config — edit TOKEN and paths
TOKEN="${TOKEN:-$(LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 32)}"
WORKDIR="${WORKDIR:-$HOME/LifeSaverTablet}"
NOIZYFISH_ROOT="${NOIZYFISH_ROOT:-$HOME/NoizyFish}"
PORT="${PORT:-8080}"
VSC_PORT="${VSC_PORT:-37373}"
PY="${PY:-python3}"

echo "Using token: $TOKEN"
echo "Workdir: $WORKDIR"
echo "NoizyFish root: $NOIZYFISH_ROOT"

mkdir -p "$WORKDIR"
cd "$WORKDIR"

# 1) Python venv and requirements
$PY -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
cat > requirements.txt <<'REQ'
flask==3.0.0
tqdm==4.66.4
requests==2.32.3
msal==1.31.0
python-dotenv==1.0.1
watchdog==4.0.0
pydantic==2.9.2
REQ
pip install -r requirements.txt

# 2) Create .env for Genie + Cockpit
cat > .env <<ENV
TENANT_ID=REPLACE_WITH_TENANT_ID
CLIENT_ID=REPLACE_WITH_CLIENT_ID
CLIENT_SECRET=REPLACE_WITH_CLIENT_SECRET
NOIZYFISH_ROOT=$NOIZYFISH_ROOT
LIFESAVER_HOST=0.0.0.0
LIFESAVER_PORT=$PORT
VSC_BRIDGE_TOKEN=$TOKEN
VSC_BRIDGE_PORT=$VSC_PORT
ENV

# 3) Place unified pipeline (noizy_genie_all.py)
cat > noizy_genie_all.py <<'PY'
# [PASTE YOUR existing noizy_genie_all.py here exactly as provided earlier]
# If you want me to reprint it, ask and I’ll paste the full file again.
PY

# 4) LifeSaver Flask app, templates, static
mkdir -p templates static static/audio playlists
cat > lifesafer_tablet.py <<'PY'
# [PASTE lifesafer_tablet.py from earlier Emotional Tech version]
# If you need me to reprint, I’ll paste it again fully.
PY

# Basic dashboard template
cat > templates/dashboard.html <<'HTML'
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>LifeSaver Tablet</title>
<meta name="viewport" content="width=device-width, initial-scale=1"><link href="{{ url_for('static', filename='styles.css') }}" rel="stylesheet"></head>
<body>
<header><h1>LifeSaver Tablet</h1><div class="mode {{ status.mode }}"><span>Mode:</span><strong>{{ status.mode|capitalize }}</strong></div></header>
<section class="grid">
  <a class="btn primary" href="{{ url_for('ritual_align') }}"><span class="title">Align Ecosystem</span><span class="desc">Tree + Organize + Mail + Archive</span>{% if status.align_running %}<span class="status">Running…</span>{% else %}<span class="status">Last: {{ status.last_align or "—" }}</span>{% endif %}</a>
  <a class="btn" href="{{ url_for('ritual_archive') }}"><span class="title">Archive Designer Assets</span><span class="desc">Sidecar metadata</span><span class="status">Last: {{ status.last_archive or "—" }}</span></a>
  <a class="btn emotech" href="{{ url_for('emotech') }}"><span class="title">Emotional Tech</span><span class="desc">Voices, neuroacoustics</span></a>
  <a class="btn creative" href="{{ url_for('vsc_run_task', label='Genie: Align') }}"><span class="title">VS Code: Run Genie Align</span><span class="desc">Run Task</span></a>
  <a class="btn" href="{{ url_for('vsc_workspace') }}?path={{ '%s' % '/'.join(['', 'path', 'to', 'NoizyFish']) }}"><span class="title">VS Code: Open NoizyFish</span><span class="desc">Switch workspace</span></a>
</section>
<footer><div class="power"><div>Battery: <strong>{{ status.power.battery_pct if status.power.battery_pct is not none else "—" }}%</strong></div>
<div>Solar: <strong>{{ status.power.solar_input_w if status.power.solar_input_w is not none else "—" }} W</strong></div><div>Grid: <strong>{{ "Online" if status.power.grid else "Offgrid" }}</strong></div></div>
<a class="btn small" href="{{ url_for('dashboard') }}">Refresh</a></footer></body></html>
HTML

# Emotional Tech page
cat > templates/emotech.html <<'HTML'
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Emotional Tech</title>
<meta name="viewport" content="width=device-width, initial-scale=1"><link href="{{ url_for('static', filename='styles.css') }}" rel="stylesheet">
<style>.topbar{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid #222}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;padding:16px}.player{background:#151820;border:2px solid #222;border-radius:16px;padding:16px}.row{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:12px}select,input[type="range"]{background:#0f1115;color:#e6e6e6;border:1px solid #333;border-radius:8px;padding:8px}audio{width:100%;margin-top:8px}</style></head>
<body>
<div class="topbar"><div><h2>Emotional Tech</h2><div class="mode {{ status.mode }}"><span>Mode:</span> <strong>{{ status.mode|capitalize }}</strong></div></div><a class="btn small" href="{{ url_for('dashboard') }}">Back</a></div>
<div class="grid">
  <div class="player"><h3>Family Voices</h3><div class="row"><label for="playlist">Playlist</label>
    <select id="playlist">{% for pl in playlists %}<option value="{{ pl }}" {{ "selected" if pl == default_playlist else "" }}>{{ pl }}</option>{% endfor %}</select>
    <button class="btn small" id="loadPlaylist">Load</button></div><div id="trackList" class="row"></div>
    <audio id="audio" controls preload="none"></audio><div class="row"><button class="btn small" id="prev">Prev</button>
    <button class="btn small" id="play">Play</button><button class="btn small" id="pause">Pause</button><button class="btn small" id="next">Next</button>
    <label>Volume</label><input type="range" id="volume" min="0" max="1" step="0.05" value="0.8"></div></div>
  <div class="player"><h3>Neuroacoustic Session</h3><div class="row"><label>Base (Hz)</label><input type="number" id="base" value="220" step="1" min="100" max="600">
    <label>Beat (Hz)</label><input type="number" id="beat" value="7" step="0.5" min="0.5" max="20"><label>Duration (min)</label><input type="number" id="dur" value="10" step="1" min="1" max="120">
    <button class="btn small" id="startTone">Start Tone</button><button class="btn small" id="stopTone">Stop</button></div><audio id="tone" controls preload="none"></audio></div>
  <div class="player"><h3>Ritual Feedback</h3><div class="row"><input type="text" id="sayText" placeholder="What should the tablet say?" style="flex:1;"><button class="btn small" id="sayBtn">Speak</button></div>
  <p style="opacity:0.7">Uses system TTS where available.</p></div></div>
<script>
const audio=document.getElementById('audio'),tone=document.getElementById('tone'),playlistSel=document.getElementById('playlist'),trackList=document.getElementById('trackList'),volume=document.getElementById('volume');let playlist={name:null,tracks:[]},idx=0;
function renderTracks(){trackList.innerHTML='';playlist.tracks.forEach((t,i)=>{const b=document.createElement('button');b.className='btn small';b.textContent=`${i+1}. ${t.title||t.file}`;b.onclick=()=>{idx=i;loadCurrent();audio.play();};trackList.appendChild(b);});}
function loadPlaylist(name){fetch(`/api/playlist/${encodeURIComponent(name)}`).then(r=>r.json()).then(data=>{playlist=data;idx=0;renderTracks();loadCurrent();}).catch(console.error);}
function loadCurrent(){const t=playlist.tracks[idx];if(!t)return;audio.src=t.url?t.url:`/audio/${encodeURIComponent(t.file)}`;audio.load();}
document.getElementById('loadPlaylist').onclick=()=>loadPlaylist(playlistSel.value);
document.getElementById('prev').onclick=()=>{idx=(idx-1+playlist.tracks.length)%playlist.tracks.length;loadCurrent();audio.play();};
document.getElementById('play').onclick=()=>audio.play();
document.getElementById('pause').onclick=()=>audio.pause();
document.getElementById('next').onclick=()=>{idx=(idx+1)%playlist.tracks.length;loadCurrent();audio.play();};
volume.oninput=()=>audio.volume=parseFloat(volume.value);
document.getElementById('startTone').onclick=()=>{const base=document.getElementById('base').value,beat=document.getElementById('beat').value,durMin=document.getElementById('dur').value;tone.src=`/api/binaural?base=${base}&beat=${beat}&duration=${durMin*60}`;tone.load();tone.play();};
document.getElementById('stopTone').onclick=()=>{tone.pause();tone.src='';};
document.getElementById('sayBtn').onclick=()=>{const text=document.getElementById('sayText').value||'Alignment complete';fetch(`/api/say?text=${encodeURIComponent(text)}`).then(()=>{});};
{% if default_playlist %}loadPlaylist('{{ default_playlist }}');{% endif %}
</script></body></html>
HTML

# Styles
cat > static/styles.css <<'CSS'
:root{--bg:#0f1115;--fg:#e6e6e6;--accent:#27AE60;--warn:#F2C94C;--danger:#EB5757;--blue:#2D9CDB;--violet:#BB6BD9}
*{box-sizing:border-box}html,body{margin:0;padding:0;background:var(--bg);color:var(--fg);font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
header{display:flex;justify-content:space-between;align-items:center;padding:24px;border-bottom:1px solid #222}
h1{margin:0;font-size:28px;letter-spacing:.5px}.mode{font-size:18px}.mode strong{margin-left:8px;color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;padding:24px}
.btn{display:flex;flex-direction:column;justify-content:center;background:#151820;border:2px solid #222;border-radius:16px;padding:24px;text-decoration:none;color:var(--fg);min-height:140px;box-shadow:0 4px 12px rgba(0,0,0,.3)}
.btn:hover,.btn:focus{outline:none;border-color:#333;background:#1a1e27}.btn .title{font-size:22px;font-weight:600;margin-bottom:8px}.btn .desc{font-size:16px;opacity:.85;margin-bottom:16px}.btn .status{font-size:14px;color:#aaa}
.primary{border-color:var(--accent);box-shadow:0 0 0 3px rgba(39,174,96,.2)}.emotech{border-color:var(--violet)}.creative{border-color:var(--blue)}
footer{display:flex;justify-content:space-between;align-items:center;padding:24px;border-top:1px solid #222}.power{display:flex;gap:24px;align-items:center;font-size:18px}.small{min-height:auto;padding:12px 16px;font-size:16px;border-radius:10px}
CSS

# 5) Seed playlists
cat > playlists/Family_Voices.json <<'JSON'
{"name":"Family_Voices","tracks":[
  {"title":"Dad — Morning Blessing","file":"family/dad_morning.mp3"},
  {"title":"Mom — Storytime","file":"family/mom_storytime.mp3"},
  {"title":"Siblings — Laughter","file":"family/siblings_laugh.mp3"}
]}
JSON
mkdir -p static/audio/family static/audio/neuro

# 6) VS Code bridge extension project
mkdir -p noizy-genie-bridge/src
cat > noizy-genie-bridge/package.json <<'JSON'
{
  "name": "noizy-genie-bridge",
  "displayName": "Noizy Genie Bridge",
  "description": "Secure local HTTP bridge to control VS Code tasks, commands, files, and terminals from your LifeSaver Cockpit.",
  "version": "0.1.0",
  "publisher": "noizy",
  "engines": { "vscode": "^1.90.0" },
  "activationEvents": [ "onStartupFinished" ],
  "main": "./out/extension.js",
  "contributes": {
    "configuration": {
      "title": "Noizy Genie Bridge",
      "properties": {
        "noizyGenieBridge.token": { "type": "string", "default": "", "description": "Shared secret token." },
        "noizyGenieBridge.port": { "type": "number", "default": 37373, "description": "Local port." },
        "noizyGenieBridge.allowCommands": {
          "type": "array", "items": { "type": "string" },
          "default": ["workbench.action.files.save","workbench.action.reloadWindow","workbench.action.closeActiveEditor"],
          "description": "Allowlist of commands."
        }
      }
    }
  },
  "scripts": { "vscode:prepublish": "npm run compile", "compile": "tsc -p ./", "watch": "tsc -watch -p ./" },
  "devDependencies": { "@types/node": "^20.11.30", "typescript": "^5.4.5", "vsce": "^3.0.0", "vscode": "^1.1.38" }
}
JSON
cat > noizy-genie-bridge/tsconfig.json <<'JSON'
{"compilerOptions":{"module":"commonjs","target":"es2020","outDir":"out","lib":["es2020"],"strict":true,"sourceMap":true,"rootDir":"src"}}
JSON
cat > noizy-genie-bridge/.vscodeignore <<'TXT'
**/.git/**
**/node_modules/**
**/*.map
TXT
cat > noizy-genie-bridge/src/extension.ts <<'TS'
import * as vscode from 'vscode';
import * as http from 'http';
import * as url from 'url';

function ok(res: http.ServerResponse, body: any) {
  const data = typeof body === 'string' ? body : JSON.stringify(body);
  res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(data);
}
function bad(res: http.ServerResponse, code: number, msg: string) {
  res.writeHead(code, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ error: msg }));
}
async function runTaskByLabel(label: string) {
  const tasks = await vscode.tasks.fetchTasks();
  const task = tasks.find(t => t.name === label);
  if (!task) throw new Error(`Task not found: ${label}`);
  return new Promise<void>((resolve) => {
    const exec = vscode.tasks.executeTask(task);
    const d = vscode.tasks.onDidEndTaskProcess(e => {
      if (e.execution === exec) { d.dispose(); resolve(); }
    });
  });
}
export function activate(context: vscode.ExtensionContext) {
  const cfg = vscode.workspace.getConfiguration();
  const token = cfg.get<string>('noizyGenieBridge.token') || '';
  const port = cfg.get<number>('noizyGenieBridge.port') || 37373;
  const allow = new Set((cfg.get<string[]>('noizyGenieBridge.allowCommands') || []).map(s => s.trim()));
  const server = http.createServer(async (req, res) => {
    try {
      if (!token) return bad(res, 403, 'Token not configured');
      const hdr = req.headers['x-token'];
      if (hdr !== token) return bad(res, 401, 'Unauthorized');
      const parsed = url.parse(req.url || '', true);
      const path = parsed.pathname || '';
      const q = parsed.query;
      const ip = (req.socket.remoteAddress || '').replace('::ffff:', '');
      if (ip !== '127.0.0.1' && ip !== '::1') return bad(res, 403, 'Forbidden');
      if (path === '/run-task') {
        const label = String(q.label || ''); if (!label) return bad(res, 400, 'Missing label');
        await runTaskByLabel(label); return ok(res, { ok: true, task: label });
      }
      if (path === '/run-command') {
        const id = String(q.id || ''); if (!id) return bad(res, 400, 'Missing id');
        if (!allow.has(id)) return bad(res, 403, `Command not allowed: ${id}`);
        await vscode.commands.executeCommand(id); return ok(res, { ok: true, command: id });
      }
      if (path === '/open') {
        const p = String(q.path || ''); if (!p) return bad(res, 400, 'Missing path');
        const uri = vscode.Uri.file(p);
        const stat = await vscode.workspace.fs.stat(uri).catch(() => undefined);
        if (!stat) throw new Error(`Path not found: ${p}`);
        if (stat.type & vscode.FileType.Directory) { await vscode.commands.executeCommand('vscode.openFolder', uri, false); }
        else { await vscode.window.showTextDocument(uri, { preview: false }); }
        return ok(res, { ok: true, opened: p });
      }
      if (path === '/workspace') {
        const p = String(q.path || ''); if (!p) return bad(res, 400, 'Missing path');
        await vscode.commands.executeCommand('vscode.openFolder', vscode.Uri.file(p), false);
        return ok(res, { ok: true, workspace: p });
      }
      if (path === '/terminal') {
        const cmd = String(q.cmd || ''); if (!cmd) return bad(res, 400, 'Missing cmd');
        const cwd = q.cwd ? String(q.cwd) : undefined;
        const term = vscode.window.createTerminal({ name: 'Noizy Genie', cwd });
        term.show(true); term.sendText(cmd, true);
        return ok(res, { ok: true, cmd, cwd });
      }
      if (path === '/paste') {
        const text = String(q.text || ''); if (!text) return bad(res, 400, 'Missing text');
        const editor = vscode.window.activeTextEditor; if (!editor) throw new Error('No active editor');
        await editor.edit(edit => { edit.insert(editor.selection.active, text); });
        return ok(res, { ok: true, len: text.length });
      }
      if (path === '/save') { await vscode.workspace.saveAll(); return ok(res, { ok: true }); }
      return bad(res, 404, 'Not found');
    } catch (err: any) { return bad(res, 500, err?.message || 'Error'); }
  });
  server.listen(port, '127.0.0.1', () => { console.log(`[Noizy Genie Bridge] http://127.0.0.1:${port}`); });
  context.subscriptions.push({ dispose() { server.close(); } });
}
export function deactivate() {}
TS

# 7) Build and install VS Code extension via vsce
cd noizy-genie-bridge
npm init -y >/dev/null 2>&1 || true
npm install
npm run compile
npx vsce package
VSIX=$(ls *.vsix | head -n1)
echo "VSIX built: $VSIX"
# Install via VS Code CLI if available
if command -v code >/dev/null 2>&1; then
  code --install-extension "$VSIX" || true
  echo "Installed VSIX into VS Code (if VS Code CLI was available)."
else
  echo "Please install the VSIX manually via VS Code (Extensions -> Install from VSIX)."
fi
cd ..

# 8) Seed VS Code settings for voice and bridge
mkdir -p "$HOME/Library/Application Support/Code/User"
SETTINGS="$HOME/Library/Application Support/Code/User/settings.json"
touch "$SETTINGS"
python3 - <<PY
import json, os
p=os.path.expanduser("$SETTINGS")
data={}
if os.path.exists(p):
    try:
        import json; data=json.loads(open(p).read())
    except Exception:
        data={}
data.update({
  "accessibility.voice.keywordActivation": True,
  "accessibility.voice.autoSynthesize": True,
  "accessibility.voice.speechLanguage": "en-CA",
  "noizyGenieBridge.port": $VSC_PORT,
  "noizyGenieBridge.token": "$TOKEN"
})
open(p,"w").write(json.dumps(data,indent=2))
print("Updated VS Code settings:", p)
PY

# 9) VS Code tasks.json with Genie tasks
mkdir -p "$NOIZYFISH_ROOT/.vscode"
cat > "$NOIZYFISH_ROOT/.vscode/tasks.json" <<JSON
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Genie: Align",
      "type": "shell",
      "command": "python ${workspaceFolder}/noizy_genie_all.py align",
      "problemMatcher": []
    },
    {
      "label": "Genie: Archive Assets",
      "type": "shell",
      "command": "python ${workspaceFolder}/noizy_genie_all.py archive-assets",
      "problemMatcher": []
    }
  ]
}
JSON

# 10) Launch the cockpit server
echo "Starting LifeSaver Tablet cockpit..."
nohup .venv/bin/python lifesafer_tablet.py >/tmp/lifesaver.log 2>&1 & disown
echo "Cockpit running on http://localhost:$PORT"
echo "DONE. Next: open VS Code, ensure extension settings token matches, and visit the cockpit."
