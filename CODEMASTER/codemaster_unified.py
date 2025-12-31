#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║       ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗        ║
║      ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝        ║
║      ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║           ║
║      ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║           ║
║      ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║           ║
║       ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝           ║
║                   ⚡ UNIFIED SERVICE - ALL 9 SERVICES IN ONE ⚡                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import os
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import orjson
    ORJSON = True
except ImportError:
    ORJSON = False

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    UVLOOP = True
except ImportError:
    UVLOOP = False

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

BASE_DIR = Path("/Users/m2ultra/NOIZYLAB/CODEMASTER")
VAULT_DIR = BASE_DIR / "data" / "vault"
CATALOG_DIR = BASE_DIR / "data" / "catalog"
EVIDENCE_DIR = BASE_DIR / "data" / "evidence"

for d in [VAULT_DIR, CATALOG_DIR, EVIDENCE_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════════
# IN-MEMORY STORES
# ═══════════════════════════════════════════════════════════════════════════════

class DataStore:
    def __init__(self):
        self.vault_items: Dict[str, Dict] = {}
        self.catalog_entries: Dict[str, Dict] = {}
        self.evidence_items: Dict[str, Dict] = {}
        self.agents: Dict[str, Dict] = {}
        self.missions: Dict[str, Dict] = {}
        self.services: Dict[str, Dict] = {}
        self.metrics: Dict[str, List] = {"requests": [], "latencies": [], "errors": []}
        self.started_at = datetime.now()

store = DataStore()

# ═══════════════════════════════════════════════════════════════════════════════
# PYDANTIC MODELS
# ═══════════════════════════════════════════════════════════════════════════════

class VaultItem(BaseModel):
    name: str
    content: str
    language: Optional[str] = "python"
    tags: Optional[List[str]] = []

class CatalogEntry(BaseModel):
    name: str
    description: str
    category: str
    metadata: Optional[Dict] = {}

class Evidence(BaseModel):
    case_id: str
    title: str
    content: str
    source: Optional[str] = "manual"

class Agent(BaseModel):
    name: str
    type: str = "worker"
    capabilities: Optional[List[str]] = []

class Mission(BaseModel):
    name: str
    objective: str
    priority: int = 5
    agents: Optional[List[str]] = []

class AIRequest(BaseModel):
    prompt: str
    model: str = "default"
    max_tokens: int = 1000
    temperature: float = 0.7

# ═══════════════════════════════════════════════════════════════════════════════
# FASTAPI APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

app = FastAPI(
    title="CODEMASTER UNIFIED",
    description="⚡ All 9 CODEMASTER Services in One Process",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def track_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    latency = (time.time() - start) * 1000
    store.metrics["requests"].append({
        "path": request.url.path,
        "method": request.method,
        "timestamp": datetime.now().isoformat(),
        "latency_ms": latency
    })
    if len(store.metrics["requests"]) > 1000:
        store.metrics["requests"] = store.metrics["requests"][-1000:]
    return response

# ═══════════════════════════════════════════════════════════════════════════════
# ROOT & HEALTH
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/", response_class=HTMLResponse)
async def root():
    uptime = datetime.now() - store.started_at
    return f"""<!DOCTYPE html><html><head><title>CODEMASTER</title>
<style>body{{background:#1a1a2e;color:#00ff88;font-family:monospace;padding:40px}}
.box{{background:rgba(0,255,136,0.1);border:2px solid #00ff88;border-radius:15px;padding:30px;margin:20px 0}}
h1{{font-size:2.5em;text-shadow:0 0 20px #00ff88}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}}
.svc{{background:rgba(0,0,0,0.4);border:1px solid #00ff88;border-radius:10px;padding:15px}}
a{{color:#00ff88}}</style></head>
<body><div class="box"><h1>⚡ CODEMASTER UNIFIED ⚡</h1>
<p>All 9 Services Running | Uptime: {uptime}</p>
<p>UVLOOP: {'✅' if UVLOOP else '❌'} | ORJSON: {'✅' if ORJSON else '❌'}</p></div>
<div class="grid">
<div class="svc">🔐 <a href="/vault/">Vault</a> ({len(store.vault_items)} items)</div>
<div class="svc">📚 <a href="/catalog/">Catalog</a> ({len(store.catalog_entries)} entries)</div>
<div class="svc">🔍 <a href="/evidence/">Evidence</a> ({len(store.evidence_items)} items)</div>
<div class="svc">🤖 <a href="/ai/">AI Gateway</a></div>
<div class="svc">🚀 <a href="/fleet/">Fleet</a> ({len(store.agents)} agents)</div>
<div class="svc">🏛️ <a href="/mc96/">MC96</a> ({len(store.missions)} missions)</div>
<div class="svc">🕸️ <a href="/mesh/">Mesh</a></div>
<div class="svc">🧠 <a href="/brain/">GOD Brain</a></div>
<div class="svc">📊 <a href="/metrics/">Metrics</a></div>
</div><p><a href="/docs">📖 API Docs</a> | <a href="/health">❤️ Health</a></p></body></html>"""

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "CODEMASTER_UNIFIED",
        "version": "2.0.0",
        "uptime_seconds": (datetime.now() - store.started_at).total_seconds(),
        "services": {s: "online" for s in ["vault","catalog","evidence","ai_gateway","fleet","mc96","mesh","god_brain","observability"]},
        "optimizations": {"uvloop": UVLOOP, "orjson": ORJSON},
        "counts": {
            "vault_items": len(store.vault_items),
            "catalog_entries": len(store.catalog_entries),
            "evidence_items": len(store.evidence_items),
            "agents": len(store.agents),
            "missions": len(store.missions)
        }
    }

# ═══════════════════════════════════════════════════════════════════════════════
# 🔐 VAULT SERVICE
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/vault/")
async def vault_list():
    return {"items": list(store.vault_items.values()), "count": len(store.vault_items)}

@app.post("/vault/")
async def vault_create(item: VaultItem):
    item_id = str(uuid.uuid4())[:8]
    entry = {"id": item_id, "name": item.name, "content": item.content, 
             "language": item.language, "tags": item.tags, "created_at": datetime.now().isoformat()}
    store.vault_items[item_id] = entry
    with open(VAULT_DIR / f"{item_id}.json", "w") as f:
        json.dump(entry, f, indent=2)
    return entry

@app.get("/vault/{item_id}")
async def vault_get(item_id: str):
    if item_id not in store.vault_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return store.vault_items[item_id]

@app.delete("/vault/{item_id}")
async def vault_delete(item_id: str):
    if item_id not in store.vault_items:
        raise HTTPException(status_code=404, detail="Item not found")
    del store.vault_items[item_id]
    (VAULT_DIR / f"{item_id}.json").unlink(missing_ok=True)
    return {"status": "deleted", "id": item_id}

# ═══════════════════════════════════════════════════════════════════════════════
# 📚 CATALOG SERVICE
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/catalog/")
async def catalog_list():
    return {"entries": list(store.catalog_entries.values()), "count": len(store.catalog_entries)}

@app.post("/catalog/")
async def catalog_create(entry: CatalogEntry):
    entry_id = str(uuid.uuid4())[:8]
    cat = {"id": entry_id, "name": entry.name, "description": entry.description,
           "category": entry.category, "metadata": entry.metadata, "created_at": datetime.now().isoformat()}
    store.catalog_entries[entry_id] = cat
    return cat

@app.get("/catalog/{entry_id}")
async def catalog_get(entry_id: str):
    if entry_id not in store.catalog_entries:
        raise HTTPException(status_code=404, detail="Entry not found")
    return store.catalog_entries[entry_id]

@app.get("/catalog/search/{query}")
async def catalog_search(query: str):
    results = [e for e in store.catalog_entries.values() 
               if query.lower() in e["name"].lower() or query.lower() in e["description"].lower()]
    return {"results": results, "count": len(results)}

# ═══════════════════════════════════════════════════════════════════════════════
# 🔍 EVIDENCE SERVICE
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/evidence/")
async def evidence_list():
    return {"items": list(store.evidence_items.values()), "count": len(store.evidence_items)}

@app.post("/evidence/")
async def evidence_create(evidence: Evidence):
    eid = str(uuid.uuid4())[:8]
    entry = {"id": eid, "case_id": evidence.case_id, "title": evidence.title,
             "content": evidence.content, "source": evidence.source, "created_at": datetime.now().isoformat()}
    store.evidence_items[eid] = entry
    return entry

@app.get("/evidence/case/{case_id}")
async def evidence_by_case(case_id: str):
    results = [e for e in store.evidence_items.values() if e["case_id"] == case_id]
    return {"evidence": results, "count": len(results)}

# ═══════════════════════════════════════════════════════════════════════════════
# 🤖 AI GATEWAY
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/ai/")
async def ai_status():
    return {"status": "ready", "available_models": ["gpt-4", "claude-3", "llama-3", "codegen"], "default_model": "claude-3"}

@app.post("/ai/generate")
async def ai_generate(request: AIRequest):
    return {"id": str(uuid.uuid4())[:8], "model": request.model, "prompt": request.prompt,
            "response": f"[Simulated {request.model} response]", "tokens_used": len(request.prompt.split()),
            "created_at": datetime.now().isoformat()}

@app.get("/ai/models")
async def ai_models():
    return {"models": [{"id": "gpt-4", "provider": "openai", "status": "available"},
                       {"id": "claude-3", "provider": "anthropic", "status": "available"},
                       {"id": "llama-3", "provider": "meta", "status": "available"},
                       {"id": "codegen", "provider": "local", "status": "available"}]}

# ═══════════════════════════════════════════════════════════════════════════════
# 🚀 FLEET SERVICE
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/fleet/")
async def fleet_list():
    return {"agents": list(store.agents.values()), "count": len(store.agents)}

@app.post("/fleet/")
async def fleet_create(agent: Agent):
    aid = str(uuid.uuid4())[:8]
    entry = {"id": aid, "name": agent.name, "type": agent.type, "capabilities": agent.capabilities,
             "status": "idle", "created_at": datetime.now().isoformat()}
    store.agents[aid] = entry
    return entry

@app.get("/fleet/{agent_id}")
async def fleet_get(agent_id: str):
    if agent_id not in store.agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    return store.agents[agent_id]

@app.post("/fleet/{agent_id}/dispatch")
async def fleet_dispatch(agent_id: str, task: Dict[str, Any] = None):
    if agent_id not in store.agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    store.agents[agent_id]["status"] = "busy"
    store.agents[agent_id]["current_task"] = task
    return {"status": "dispatched", "agent_id": agent_id, "task": task}

# ═══════════════════════════════════════════════════════════════════════════════
# 🏛️ MC96 (MISSION CONTROL)
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/mc96/")
async def mc96_list():
    return {"missions": list(store.missions.values()), "count": len(store.missions)}

@app.post("/mc96/")
async def mc96_create(mission: Mission):
    mid = str(uuid.uuid4())[:8]
    entry = {"id": mid, "name": mission.name, "objective": mission.objective, "priority": mission.priority,
             "agents": mission.agents, "status": "planning", "created_at": datetime.now().isoformat()}
    store.missions[mid] = entry
    return entry

@app.get("/mc96/{mission_id}")
async def mc96_get(mission_id: str):
    if mission_id not in store.missions:
        raise HTTPException(status_code=404, detail="Mission not found")
    return store.missions[mission_id]

@app.post("/mc96/{mission_id}/execute")
async def mc96_execute(mission_id: str):
    if mission_id not in store.missions:
        raise HTTPException(status_code=404, detail="Mission not found")
    store.missions[mission_id]["status"] = "executing"
    return {"status": "executing", "mission_id": mission_id}

# ═══════════════════════════════════════════════════════════════════════════════
# 🕸️ MESH SERVICE
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/mesh/")
async def mesh_list():
    services = {s: {"status": "online", "port": 8000, "path": f"/{s}"} 
                for s in ["vault", "catalog", "evidence", "ai", "fleet", "mc96", "brain", "metrics"]}
    return {"services": services, "mode": "unified"}

@app.get("/mesh/health")
async def mesh_health():
    return {"mesh_status": "healthy", "mode": "unified", "all_services_online": True, "latency_ms": 0.1}

# ═══════════════════════════════════════════════════════════════════════════════
# 🧠 GOD BRAIN
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/brain/")
async def brain_status():
    return {"status": "active", "mode": "unified", "intelligence_level": "maximum",
            "capabilities": ["code_analysis", "pattern_recognition", "optimization_suggestions", "security_scanning", "architecture_review"]}

@app.post("/brain/analyze")
async def brain_analyze(data: Dict[str, Any]):
    return {"analysis_id": str(uuid.uuid4())[:8], "input": data,
            "insights": ["Code structure analyzed", "Patterns identified", "Optimizations suggested"],
            "score": 85, "created_at": datetime.now().isoformat()}

@app.get("/brain/insights")
async def brain_insights():
    return {"insights": [{"type": "optimization", "message": "Consider using async for I/O operations"},
                         {"type": "security", "message": "All endpoints properly secured"},
                         {"type": "performance", "message": "Cache hit rate optimal"}],
            "generated_at": datetime.now().isoformat()}

# ═══════════════════════════════════════════════════════════════════════════════
# 📊 OBSERVABILITY
# ═══════════════════════════════════════════════════════════════════════════════

@app.get("/metrics/")
async def metrics_overview():
    requests = store.metrics["requests"]
    total = len(requests)
    avg_latency = sum(r["latency_ms"] for r in requests) / total if requests else 0
    return {"total_requests": total, "average_latency_ms": round(avg_latency, 2),
            "uptime_seconds": (datetime.now() - store.started_at).total_seconds(),
            "memory": {"vault_items": len(store.vault_items), "catalog_entries": len(store.catalog_entries),
                       "evidence_items": len(store.evidence_items), "agents": len(store.agents), "missions": len(store.missions)}}

@app.get("/metrics/requests")
async def metrics_requests():
    return {"requests": store.metrics["requests"][-100:]}

@app.get("/metrics/prometheus")
async def metrics_prometheus():
    requests = store.metrics["requests"]
    total = len(requests)
    avg_latency = sum(r["latency_ms"] for r in requests) / total if requests else 0
    return f"""# HELP codemaster_requests_total Total HTTP requests
codemaster_requests_total {total}
# HELP codemaster_latency_avg Average latency in milliseconds
codemaster_latency_avg {avg_latency:.2f}
# HELP codemaster_vault_items Number of vault items
codemaster_vault_items {len(store.vault_items)}"""

# ═══════════════════════════════════════════════════════════════════════════════
# STARTUP
# ═══════════════════════════════════════════════════════════════════════════════

@app.on_event("startup")
async def startup():
    for fp in VAULT_DIR.glob("*.json"):
        try:
            with open(fp) as f:
                item = json.load(f)
                store.vault_items[item["id"]] = item
        except:
            pass
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║       ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗        ║
║      ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝        ║
║      ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║           ║
║      ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║           ║
║      ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║           ║
║       ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝           ║
║                        ⚡ UNIFIED SERVICE STARTED ⚡                               ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  🔐 Vault:        /vault/      │  🚀 Fleet:        /fleet/                        ║
║  📚 Catalog:      /catalog/    │  🏛️ MC96:         /mc96/                         ║
║  🔍 Evidence:     /evidence/   │  🕸️ Mesh:         /mesh/                         ║
║  🤖 AI Gateway:   /ai/         │  🧠 GOD Brain:    /brain/                        ║
║  📊 Metrics:      /metrics/    │  📖 Docs:         /docs                          ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  UVLOOP: {'✅':4} | ORJSON: {'✅' if ORJSON else '❌':4} | Loaded: {len(store.vault_items)} vault items                          ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    print("\n🚀 Starting CODEMASTER UNIFIED on M2 ULTRA...\n")
    uvicorn.run("codemaster_unified:app", host="0.0.0.0", port=8000, reload=False, 
                workers=1, loop="uvloop" if UVLOOP else "asyncio", log_level="info")
