
# --- Multi-Agent Orchestration Backend ---
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
import asyncio, uuid, time

app = FastAPI(title="Bobby Mission Control - 96 Agents")

AGENT_COUNT = 96
TASK_QUEUE = asyncio.Queue()
AGENTS = {}
AGENT_STATUS = {}
AGENT_RESULTS = {}

class Task:
  def __init__(self, task_id, payload):
    self.task_id = task_id
    self.payload = payload
    self.status = "pending"
    self.result = None

async def agent_worker(agent_id):
  while True:
    task: Task = await TASK_QUEUE.get()
    AGENT_STATUS[agent_id] = f"working on {task.task_id}"
    # Simulate work (replace with real logic)
    await asyncio.sleep(0.5)
    result = {"agent": agent_id, "task": task.task_id, "result": f"Processed by agent {agent_id}"}
    AGENT_RESULTS[task.task_id] = result
    AGENT_STATUS[agent_id] = "idle"
    TASK_QUEUE.task_done()

@app.on_event("startup")
async def startup_agents():
  for i in range(AGENT_COUNT):
    agent_id = f"agent-{i+1:02d}"
    AGENT_STATUS[agent_id] = "idle"
    AGENTS[agent_id] = asyncio.create_task(agent_worker(agent_id))

@app.post("/submit-task")
async def submit_task(request: Request):
  data = await request.json()
  task_id = str(uuid.uuid4())
  task = Task(task_id, data)
  await TASK_QUEUE.put(task)
  return {"task_id": task_id, "status": "queued"}

@app.get("/agent-status")
async def agent_status():
  return AGENT_STATUS

@app.get("/task-result/{task_id}")
async def task_result(task_id: str):
  result = AGENT_RESULTS.get(task_id)
  if result:
    return result
  return JSONResponse({"status": "pending"}, status_code=202)

@app.get("/events")
async def events():
  async def event_stream():
    while True:
      yield f"data: {AGENT_STATUS}\n\n"
      await asyncio.sleep(1)
  return StreamingResponse(event_stream(), media_type="text/event-stream")

# Health endpoint
@app.get("/health")
def health():
  return {"status": "green", "agents": AGENT_COUNT, "queue": TASK_QUEUE.qsize()}

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
