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
    if __name__ == "__main__":
      import uvicorn
      uvicorn.run(app, host="127.0.0.1", port=8787, reload=True)
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
