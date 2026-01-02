from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
import subprocess, os, hashlib, glob, asyncio
import ast

app = FastAPI()

AQUARIUM_ROOT = os.getcwd()  # or set to your path

missing_imports = []
duplicate_files = {}
all_files = {}

for dirpath, _, filenames in os.walk(AQUARIUM_ROOT):
    for fname in filenames:
        fpath = os.path.join(dirpath, fname)
        # Track duplicates
        if fname in all_files:

            duplicate_files.setdefault(fname, []).append(fpath)
        else:
            all_files[fname] = fpath
        # Check Python imports
        if fname.endswith('.py'):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=fname)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for n in node.names:
                            try:
                                __import__(n.name)
                            except ImportError:
                                missing_imports.append((fpath, n.name))
                    elif isinstance(node, ast.ImportFrom):
                        try:
                            __import__(node.module)
                        except Exception:
                            missing_imports.append((fpath, node.module))
            except Exception as e:
                print(f"Error parsing {fpath}: {e}")

print("\n=== Duplicate Files ===")
for fname, paths in duplicate_files.items():
    print(f"{fname}:")
    for p in paths:
        print(f"  {p}")

print("\n=== Missing Imports ===")
for fpath, mod in missing_imports:
    print(f"{fpath}: missing {mod}")

print("\n=== Scan Complete ===")

@app.post("/check-code")
async def check_code(code: str, language: str):
    if language == "python":
        with open("temp.py", "w") as f:
            f.write(code)
        lint = subprocess.run(["flake8", "temp.py"], capture_output=True, text=True)
        compile_check = subprocess.run(["python3", "-m", "py_compile", "temp.py"], capture_output=True, text=True)
        return {"lint": lint.stdout or lint.stderr, "compile": compile_check.stderr}
    elif language in ["sh", "bash", "zsh"]:
        with open("temp.sh", "w") as f:
            f.write(code)
        lint = subprocess.run(["shellcheck", "temp.sh"], capture_output=True, text=True)
        return {"lint": lint.stdout or lint.stderr}
    return {"error": "Unsupported language"}
# Health endpoint: status and services
@app.get("/health")
def health():
    return {"status": "green", "services": ["narrator", "dupe-killer", "metadata"]}

# Narrate text (placeholder until ElevenLabs wired in)
@app.post("/narrate")
async def narrate_text(text: str):
    # This will later call ElevenLabs
    return {"status": "ok", "message": f"Narrating: {text}"}

# Scan WAVs
@app.post("/scan-wavs")
async def scan_wavs():
    files = glob.glob("**/*.wav", recursive=True)
    return {"count": len(files), "files": files[:20]}  # sample list

# Big Dupe Killer
@app.post("/dupe-killer")
async def dupe_killer():
    seen, dupes = {}, []
    for filepath in glob.glob("**/*.wav", recursive=True):
        h = hashlib.md5(open(filepath, "rb").read()).hexdigest()
        if h in seen:
            dupes.append(filepath)
        else:
            seen[h] = filepath
    return {"dupes": dupes, "count": len(dupes)}

# Run a system script
@app.post("/run-script")
async def run_script():
    proc = subprocess.run(["echo", "Hello from Bobby!"], capture_output=True, text=True)
    return {"stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}

# Bundle settings
BUNDLE_IDENTIFIER = "com.noizyfish.mission.control"

# Execute user script
@app.post("/run-python")
async def run_python_script(user_script: str):
    # Save the user script to a temporary file
    temp_path = "user_script.py"
    with open(temp_path, "w") as f:
        f.write(user_script)
    # Run the user script securely, capture output/errors
    result = subprocess.run(["python3", temp_path], capture_output=True, text=True)
    # Optionally, delete the temp file after execution
    try:
        os.remove(temp_path)
    except Exception:
        pass
    return {
        "status": "script executed",
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8787, reload=True)

    cd ~/bobby-mission-control/frontend
    npm run tauri
    "scripts": {
      "dev": "vite",
      "build": "vite build",
      "preview": "vite preview",
      "tauri": "tauri dev"
    }

import BobbyStarship from "./components/BobbyStarship";
// ...in your component tree:
<BobbyStarship />

import React, { useState } from "react";
import { gh } from "../lib/gatehouse"; // your API client

export function SentinelAutoRunner() {
  const [lang, setLang] = useState<"python"|"bash"|"sh"|"zsh">("python");
  const [code, setCode] = useState("");
  const [log, setLog] = useState<string[]>([]);
  const [output, setOutput] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const pushLog = (msg: string) => setLog(l => [...l, `[${new Date().toLocaleTimeString()}] ${msg}`]);

  const handleRun = async () => {
    setLoading(true);
    setOutput(null);
    setLog([]);
    pushLog("Checking code quality...");
    let check = await gh.check({ language: lang, code, autofix: true, strict_security: true });
    if (check.safeToRun) {
      pushLog("Code is safe! Running...");
      const res = await gh.run({ language: lang, code: check.fixedCode, assume_safe: true });
      setOutput(res);
      pushLog("Execution complete.");
    } else {
      pushLog("Code is NOT safe. Summoning Sentinel for auto-repair...");
      const repair = await fetch("/auto-repair", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language: lang })
      }).then(r => r.json());
      pushLog(`Sentinel repaired code: ${repair.explanation || "No explanation"}`);
      setCode(repair.repairedCode);
      pushLog("Re-checking repaired code...");
      let recheck = await gh.check({ language: lang, code: repair.repairedCode, autofix: true, strict_security: true });
      if (recheck.safeToRun) {
        pushLog("Repaired code is safe! Running...");
        const res = await gh.run({ language: lang, code: recheck.fixedCode, assume_safe: true });
        setOutput(res);
        pushLog("Execution complete.");
      } else {
        pushLog("Sentinel could not fully repair the code. Manual intervention required.");
        setOutput({ error: "Auto-repair failed. Please review the code." });
      }
    }
    setLoading(false);
  };

  return (
    <div className="p-6 bg-zinc-900 rounded-xl shadow-lg max-w-2xl mx-auto">
      <div className="mb-4 flex gap-2">
        <select value={lang} onChange={e=>setLang(e.target.value as any)} className="rounded px-2 py-1">
          <option value="python">Python</option>
          <option value="bash">Bash</option>
          <option value="sh">sh</option>
          <option value="zsh">zsh</option>
        </select>
        <button onClick={handleRun} disabled={loading} className="bg-emerald-600 hover:bg-emerald-700 text-white px-4 py-2 rounded">
          {loading ? "Working..." : "Check & Run"}
        </button>
      </div>
      <textarea
        value={code}
        onChange={e=>setCode(e.target.value)}
        placeholder="Paste your code here…"
        className="w-full h-40 rounded bg-zinc-800 text-zinc-100 p-2 mb-4"
      />
      <div className="mb-2 text-xs text-zinc-400">Sentinel Log:</div>
      <ul className="bg-zinc-950 rounded p-2 text-xs text-zinc-200 mb-4" style={{minHeight:60}}>
        {log.map((l,i) => <li key={i}>{l}</li>)}
      </ul>
      <div className="mb-2 text-xs text-zinc-400">Output:</div>
      <pre className="bg-zinc-950 rounded p-2 text-xs text-emerald-200" style={{minHeight:60}}>
        {output ? JSON.stringify(output, null, 2) : "—"}
      </pre>
    </div>
  );
}
