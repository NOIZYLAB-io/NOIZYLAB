#!/usr/bin/env node

/**
 * ╔════════════════════════════════════════════════════════════════════╗
 * ║  GORUNFREE: THE MONOLITH (v1.0)                                    ║
 * ║  Server • Client • Installer • Automation • Zero Dependencies      ║
 * ╚════════════════════════════════════════════════════════════════════╝
 */

const http = require('http');
const { spawn, exec } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

// --- CONFIGURATION ---
const PORT = 9999;
const BROWSER = 'Safari'; // Change to 'Google Chrome' or 'Arc' if needed
const SOUNDS = true;

// --- CLI ROUTER ---
const args = process.argv.slice(2);
const command = args[0];
const subArg = args[1];

const HELP_TEXT = `
⚡ GORUNFREE MONOLITH CLI ⚡

USAGE:
  ./gorunfree server        → Start the bridge (Keep window open)

  ./gorunfree fix           → Send clipboard to Claude (Bug Fix Mode)
  ./gorunfree roast         → Send clipboard to Claude (Roast Mode)
  ./gorunfree fast          → Send clipboard to Claude (Optimize Mode)
  ./gorunfree explain       → Send clipboard to Claude (Explain Mode)
  ./gorunfree raw           → Send clipboard as-is

  ./gorunfree back          → Retrieve code from Claude & Paste to Cursor

  ./gorunfree install       → Installs to /usr/local/bin (Requires sudo)
`;

if (!command) { console.log(HELP_TEXT); process.exit(0); }

// Route commands
switch (command) {
    case 'server': runServer(); break;
    case 'fix':     sendClient('fix'); break;
    case 'roast':   sendClient('roast'); break;
    case 'fast':    sendClient('optimize'); break;
    case 'explain': sendClient('explain'); break;
    case 'raw':     sendClient('default'); break;
    case 'back':    retrieveClient(); break;
    case 'install': installCLI(); break;
    default: console.log(`Unknown command: ${command}`);
}

// ==========================================
// 1. CLIENT LOGIC (Replaces curl/jq)
// ==========================================

async function sendClient(mode) {
    try {
        const code = await getClipboard();
        if (!code) { console.error("❌ Clipboard is empty"); process.exit(1); }

        const postData = JSON.stringify({ code, mode });

        const req = http.request({
            hostname: 'localhost', port: PORT, path: '/upload',
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(postData) }
        }, (res) => {
            res.on('data', () => {}); // Consume stream
            res.on('end', () => {
                if (res.statusCode === 200) console.log(`✅ Sent to Claude [${mode.toUpperCase()}]`);
                else console.log(`❌ Server Error: ${res.statusCode}`);
                process.exit(0);
            });
        });

        req.on('error', (e) => {
            console.error(`❌ Connection Failed. Is the server running? (Run './gorunfree server')`);
            process.exit(1);
        });

        req.write(postData);
        req.end();
    } catch (e) { console.error(e); }
}

async function retrieveClient() {
    const req = http.request({
        hostname: 'localhost', port: PORT, path: '/download', method: 'POST'
    }, (res) => {
        let data = '';
        res.on('data', c => data += c);
        res.on('end', () => {
            const json = JSON.parse(data);
            if (json.status === 'received') console.log(`✅ Retrieved ${json.length} chars -> Pasted to Cursor`);
            else console.log(`❌ Error: ${json.error}`);
            process.exit(0);
        });
    });

    req.on('error', () => {
        console.error("❌ Bridge server is offline.");
        process.exit(1);
    });
    req.end();
}

// ==========================================
// 2. SERVER LOGIC (The Background Process)
// ==========================================

function runServer() {
    console.clear();
    console.log(`\x1b[32m
    ╔══════════════════════════════════╗
    ║   GORUNFREE BRIDGE ONLINE        ║
    ║   Port: ${PORT}                     ║
    ╚══════════════════════════════════╝\x1b[0m`);
    playSound('PowerOn');

    const server = http.createServer(async (req, res) => {
        res.setHeader('Access-Control-Allow-Origin', '*');

        if (req.method !== 'POST') return res.end();

        let body = '';
        req.on('data', c => body += c);

        req.on('end', async () => {
            try {
                if (req.url === '/upload') {
                    const { code, mode } = JSON.parse(body);
                    const prompt = wrapPrompt(code, mode);

                    await copyToClipboard(prompt);
                    await runAppleScript(getBrowserScript('PASTE'));

                    playSound('Tink');
                    console.log(`[${new Date().toLocaleTimeString()}] 📥 RECEIVED: ${mode}`);
                    res.end(JSON.stringify({ success: true }));
                }

                if (req.url === '/download') {
                    const raw = await runAppleScript(getBrowserScript('READ'));
                    if (raw.includes('ERROR_NO_MSG')) throw new Error('No response found');

                    const clean = sanitize(raw);
                    await copyToClipboard(clean);
                    await runAppleScript(getBrowserScript('CURSOR'));

                    playSound('Hero');
                    console.log(`[${new Date().toLocaleTimeString()}] 📤 SENT TO CURSOR`);
                    res.end(JSON.stringify({ status: 'received', length: clean.length }));
                }
            } catch (e) {
                playSound('Basso');
                console.error("ERR:", e.message);
                res.end(JSON.stringify({ error: e.message }));
            }
        });
    });

    server.listen(PORT);
}

// ==========================================
// 3. UTILITIES & AUTOMATION
// ==========================================

function wrapPrompt(code, mode) {
    if (mode === 'fix') return "🚨 BUG REPORT. Analyze this, find the error, and rewrite the fixed version:\n\n" + code;
    if (mode === 'roast') return "🔥 ROAST ME. Criticize this code brutally:\n\n" + code;
    if (mode === 'optimize') return "🚀 SPEED RUN. Refactor for speed and cleanliness:\n\n" + code;
    if (mode === 'explain') return "👨‍🏫 EXPLAIN LIKE I'M 5. What does this do?\n\n" + code;
    return code;
}

function sanitize(text) {
    // Strip markdown blocks
    const match = text.match(/```[\w]*\n([\s\S]*?)```/);
    return (match && match[1]) ? match[1].trim() : text;
}

function getClipboard() {
    return new Promise((resolve) => {
        const proc = spawn('pbpaste');
        let data = '';
        proc.stdout.on('data', d => data += d);
        proc.on('close', () => resolve(data));
    });
}

function copyToClipboard(text) {
    return new Promise((resolve) => {
        const proc = spawn('pbcopy');
        proc.stdin.write(text);
        proc.stdin.end();
        proc.on('close', resolve);
    });
}

function playSound(name) {
    if(SOUNDS) spawn('afplay', [`/System/Library/Sounds/${name}.aiff`]);
}

function runAppleScript(script) {
    return new Promise((resolve, reject) => {
        const proc = spawn('osascript', ['-e', script]);
        let out = '';
        proc.stdout.on('data', d => out += d);
        proc.on('close', () => resolve(out.trim()));
    });
}

function getBrowserScript(action) {
    const js = `
        var msgs = document.querySelectorAll('div[data-message-author-role="assistant"]');
        var last = msgs[msgs.length - 1];
        last ? last.innerText : "ERROR_NO_MSG";
    `.replace(/\n/g, ' ');

    if (action === 'PASTE') return `
        tell application "${BROWSER}"
            activate
            open location "https://claude.ai/new"
            delay 1.5
        end tell
        tell application "System Events"
            keystroke "v" using command down
            delay 0.5
            keystroke return
        end tell`;

    if (action === 'READ') return BROWSER === 'Safari'
        ? `tell application "Safari" to do JavaScript "${js}" in document 1`
        : `tell application "${BROWSER}" to tell active tab of window 1 to execute javascript "${js}"`;

    if (action === 'CURSOR') return `
        tell application "Cursor" to activate
        delay 0.5
        tell application "System Events" to keystroke "v" using command down`;
}

function installCLI() {
    const dest = '/usr/local/bin/gorunfree';
    const currentPath = fs.realpathSync(process.argv[1]);

    console.log(`Installing ${currentPath} to ${dest}...`);
    try {
        if (fs.existsSync(dest)) fs.unlinkSync(dest);
        fs.symlinkSync(currentPath, dest);
        console.log(`✅ INSTALLED! You can now run 'gorunfree server' from anywhere.`);
    } catch (e) {
        console.error("❌ Permission denied. Try: sudo ./gorunfree install");
    }
}
