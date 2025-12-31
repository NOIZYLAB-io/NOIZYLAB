#!/usr/bin/env python3
"""
🧠 GOD AI BRAIN 🧠
==================
The intelligent orchestration core for CODEMASTER.

GOD (Grand Orchestration Director) is the AI brain that:
- Understands context across all services
- Makes autonomous decisions
- Orchestrates complex workflows
- Learns from evidence packs
- Manages the fleet intelligently

This is the THINKING part of CODEMASTER.
"""

import os
import json
import asyncio
import hashlib
from datetime import datetime
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

# Ollama / Local LLM
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")

# Service URLs
SERVICES = {
    "vault":    os.environ.get("VAULT_URL", "http://localhost:8000"),
    "catalog":  os.environ.get("CATALOG_URL", "http://localhost:8001"),
    "evidence": os.environ.get("EVIDENCE_URL", "http://localhost:8002"),
    "fleet":    os.environ.get("FLEET_URL", "http://localhost:8200"),
    "mc96":     os.environ.get("MC96_URL", "http://localhost:8300"),
}

# Brain settings
BRAIN_MEMORY_SIZE = int(os.environ.get("BRAIN_MEMORY_SIZE", "100"))
BRAIN_CONTEXT_WINDOW = int(os.environ.get("BRAIN_CONTEXT_WINDOW", "8000"))


# ═══════════════════════════════════════════════════════════════
# 📊 MODELS
# ═══════════════════════════════════════════════════════════════

class ThinkRequest(BaseModel):
    """Request for GOD to think about something"""
    question: str
    context: Optional[Dict] = None
    include_services: bool = True
    include_evidence: bool = True


class PlanRequest(BaseModel):
    """Request for GOD to create a plan"""
    goal: str
    constraints: Optional[List[str]] = None
    resources: Optional[Dict] = None


class ActRequest(BaseModel):
    """Request for GOD to take action"""
    action: str
    target: str
    parameters: Optional[Dict] = None


class LearnRequest(BaseModel):
    """Request for GOD to learn from evidence"""
    evidence_ids: List[str]
    summary: Optional[str] = None


# ═══════════════════════════════════════════════════════════════
# 🧠 BRAIN CORE
# ═══════════════════════════════════════════════════════════════

class BrainMemory:
    """Short-term memory for the brain"""
    
    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.memories: List[Dict] = []
    
    def remember(self, memory_type: str, content: Any, metadata: Dict = None):
        """Add a memory"""
        memory = {
            "type": memory_type,
            "content": content,
            "metadata": metadata or {},
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "id": hashlib.sha256(
                f"{memory_type}{content}{datetime.utcnow()}".encode()
            ).hexdigest()[:12],
        }
        
        self.memories.append(memory)
        
        # Trim if too large
        if len(self.memories) > self.max_size:
            self.memories = self.memories[-self.max_size:]
        
        return memory["id"]
    
    def recall(self, memory_type: str = None, limit: int = 10) -> List[Dict]:
        """Recall memories"""
        if memory_type:
            memories = [m for m in self.memories if m["type"] == memory_type]
        else:
            memories = self.memories
        
        return memories[-limit:]
    
    def forget(self, memory_id: str):
        """Forget a specific memory"""
        self.memories = [m for m in self.memories if m["id"] != memory_id]
    
    def context_string(self, limit: int = 5) -> str:
        """Get recent memories as context string"""
        recent = self.recall(limit=limit)
        if not recent:
            return "No recent memories."
        
        lines = []
        for m in recent:
            lines.append(f"[{m['type']}] {m['content']}")
        return "\n".join(lines)


class GODBrain:
    """The Grand Orchestration Director"""
    
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=60.0)
        self.memory = BrainMemory(BRAIN_MEMORY_SIZE)
        self.model = OLLAMA_MODEL
        self.system_prompt = self._build_system_prompt()
    
    async def close(self):
        await self.client.aclose()
    
    def _build_system_prompt(self) -> str:
        """Build the GOD system prompt"""
        return """You are GOD (Grand Orchestration Director), the AI brain of CODEMASTER.

Your responsibilities:
1. UNDERSTAND - Analyze questions and context deeply
2. PLAN - Create step-by-step plans for complex tasks
3. ORCHESTRATE - Coordinate actions across services
4. LEARN - Extract insights from evidence packs
5. PROTECT - Ensure security and data integrity

Available services:
- VAULT: File storage and ingestion
- CATALOG: Asset indexing and search
- EVIDENCE: Immutable truth records
- FLEET: Device management and control
- MC96: Network automation
- MESH: Remote control sessions

Guidelines:
- Always create evidence for important actions
- Verify claims before accepting them as truth
- Consider security implications
- Optimize for efficiency and reliability
- Learn from past actions and their outcomes

When asked to ACT, respond with a JSON action plan:
{
  "action": "action_name",
  "target": "service_or_device",
  "steps": ["step1", "step2"],
  "expected_outcome": "description",
  "evidence_required": true/false
}

Be concise, accurate, and helpful."""
    
    async def _call_ollama(self, prompt: str, system: str = None) -> str:
        """Call Ollama for inference"""
        try:
            response = await self.client.post(
                f"{OLLAMA_HOST}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "system": system or self.system_prompt,
                    "stream": False,
                    "options": {
                        "num_ctx": BRAIN_CONTEXT_WINDOW,
                        "temperature": 0.7,
                    }
                }
            )
            
            if response.status_code == 200:
                return response.json().get("response", "")
            return f"Error: {response.status_code}"
            
        except Exception as e:
            return f"Ollama error: {e}"
    
    async def _get_service_context(self) -> Dict:
        """Gather context from all services"""
        context = {}
        
        for name, url in SERVICES.items():
            try:
                response = await self.client.get(f"{url}/health", timeout=5.0)
                context[name] = {
                    "status": "online" if response.status_code == 200 else "offline",
                    "data": response.json() if response.status_code == 200 else None,
                }
            except:
                context[name] = {"status": "unreachable"}
        
        return context
    
    async def _get_recent_evidence(self, limit: int = 5) -> List[Dict]:
        """Get recent evidence packs"""
        try:
            response = await self.client.get(
                f"{SERVICES['evidence']}/packs",
                params={"limit": limit}
            )
            if response.status_code == 200:
                return response.json().get("packs", [])
        except:
            pass
        return []
    
    # ─────────────────────────────────────────────────────────
    # Core Capabilities
    # ─────────────────────────────────────────────────────────
    
    async def think(self, question: str, context: Dict = None,
                   include_services: bool = True,
                   include_evidence: bool = True) -> Dict:
        """Think about a question"""
        
        # Build context
        full_context = {}
        
        if include_services:
            full_context["services"] = await self._get_service_context()
        
        if include_evidence:
            full_context["recent_evidence"] = await self._get_recent_evidence()
        
        if context:
            full_context["provided"] = context
        
        full_context["memory"] = self.memory.context_string()
        
        # Build prompt
        prompt = f"""Context:
{json.dumps(full_context, indent=2)}

Question: {question}

Think step by step and provide a clear answer."""
        
        # Get response
        response = await self._call_ollama(prompt)
        
        # Remember this interaction
        self.memory.remember("thought", {
            "question": question,
            "response_summary": response[:200],
        })
        
        return {
            "question": question,
            "response": response,
            "context_used": list(full_context.keys()),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    
    async def plan(self, goal: str, constraints: List[str] = None,
                  resources: Dict = None) -> Dict:
        """Create a plan to achieve a goal"""
        
        # Get service status
        services = await self._get_service_context()
        
        prompt = f"""Goal: {goal}

Available Services:
{json.dumps({k: v['status'] for k, v in services.items()}, indent=2)}

Constraints:
{json.dumps(constraints or ['None specified'], indent=2)}

Resources:
{json.dumps(resources or {'None specified': True}, indent=2)}

Create a detailed step-by-step plan to achieve this goal.
Include which services to use and in what order.
Identify potential risks and mitigation strategies.

Respond in this JSON format:
{{
  "plan_name": "short name",
  "steps": [
    {{"step": 1, "action": "description", "service": "service_name", "critical": true/false}}
  ],
  "estimated_duration": "X minutes",
  "risks": ["risk1", "risk2"],
  "success_criteria": ["criterion1", "criterion2"]
}}"""
        
        response = await self._call_ollama(prompt)
        
        # Try to parse as JSON
        try:
            # Find JSON in response
            start = response.find('{')
            end = response.rfind('}') + 1
            if start >= 0 and end > start:
                plan = json.loads(response[start:end])
            else:
                plan = {"raw_response": response}
        except:
            plan = {"raw_response": response}
        
        # Remember the plan
        self.memory.remember("plan", {
            "goal": goal,
            "plan_name": plan.get("plan_name", "unnamed"),
        })
        
        return {
            "goal": goal,
            "plan": plan,
            "services_available": {k: v['status'] for k, v in services.items()},
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    
    async def act(self, action: str, target: str, 
                 parameters: Dict = None) -> Dict:
        """Execute an action"""
        
        # Determine target service
        service = None
        for name in SERVICES.keys():
            if name in target.lower() or name in action.lower():
                service = name
                break
        
        if not service:
            return {
                "status": "error",
                "error": f"Could not determine target service for: {action} -> {target}",
            }
        
        # Build action request
        prompt = f"""Execute this action:
Action: {action}
Target: {target}
Service: {service}
Parameters: {json.dumps(parameters or {})}

What API endpoint should I call and with what payload?
Respond in JSON format:
{{
  "endpoint": "/path",
  "method": "GET/POST/PUT/DELETE",
  "payload": {{}}
}}"""
        
        response = await self._call_ollama(prompt)
        
        # Parse response
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            if start >= 0 and end > start:
                action_spec = json.loads(response[start:end])
            else:
                return {"status": "error", "error": "Could not parse action spec"}
        except:
            return {"status": "error", "error": "Could not parse action spec"}
        
        # Execute the action
        try:
            url = f"{SERVICES[service]}{action_spec['endpoint']}"
            method = action_spec.get("method", "GET").upper()
            payload = action_spec.get("payload")
            
            if method == "GET":
                result = await self.client.get(url, params=payload)
            elif method == "POST":
                result = await self.client.post(url, json=payload)
            elif method == "PUT":
                result = await self.client.put(url, json=payload)
            elif method == "DELETE":
                result = await self.client.delete(url)
            else:
                return {"status": "error", "error": f"Unknown method: {method}"}
            
            # Create evidence
            evidence_payload = {
                "type": f"god_action_{action}",
                "actor": "god_brain",
                "target": target,
                "data": {
                    "action": action,
                    "service": service,
                    "endpoint": action_spec["endpoint"],
                    "result_status": result.status_code,
                },
            }
            
            await self.client.post(
                f"{SERVICES['evidence']}/packs/create",
                json=evidence_payload
            )
            
            # Remember the action
            self.memory.remember("action", {
                "action": action,
                "target": target,
                "service": service,
                "success": result.status_code < 400,
            })
            
            return {
                "status": "success" if result.status_code < 400 else "failed",
                "action": action,
                "target": target,
                "service": service,
                "http_status": result.status_code,
                "response": result.json() if result.status_code < 400 else result.text,
            }
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def learn(self, evidence_ids: List[str], 
                   summary: str = None) -> Dict:
        """Learn from evidence packs"""
        
        # Fetch evidence packs
        packs = []
        for eid in evidence_ids:
            try:
                response = await self.client.get(
                    f"{SERVICES['evidence']}/packs/{eid}"
                )
                if response.status_code == 200:
                    packs.append(response.json())
            except:
                pass
        
        if not packs:
            return {"status": "error", "error": "No evidence packs found"}
        
        # Analyze with AI
        prompt = f"""Analyze these evidence packs and extract learnings:

Evidence Packs:
{json.dumps(packs, indent=2)}

User Summary (if provided): {summary or 'None'}

Extract:
1. Key patterns and insights
2. Success/failure factors
3. Recommendations for future actions
4. Any anomalies or concerns

Respond in JSON:
{{
  "insights": ["insight1", "insight2"],
  "patterns": ["pattern1"],
  "recommendations": ["rec1"],
  "concerns": ["concern1"] or null
}}"""
        
        response = await self._call_ollama(prompt)
        
        # Parse response
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            if start >= 0 and end > start:
                learnings = json.loads(response[start:end])
            else:
                learnings = {"raw_analysis": response}
        except:
            learnings = {"raw_analysis": response}
        
        # Remember the learnings
        self.memory.remember("learning", {
            "evidence_count": len(packs),
            "insights_count": len(learnings.get("insights", [])),
        })
        
        return {
            "status": "success",
            "evidence_analyzed": len(packs),
            "learnings": learnings,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }


# ═══════════════════════════════════════════════════════════════
# 🚀 FASTAPI APP
# ═══════════════════════════════════════════════════════════════

brain: Optional[GODBrain] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage brain lifecycle"""
    global brain
    brain = GODBrain()
    yield
    await brain.close()


app = FastAPI(
    title="🧠 GOD AI Brain",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health():
    """Brain health check"""
    return {
        "status": "ok",
        "service": "god_brain",
        "model": OLLAMA_MODEL,
        "memory_count": len(brain.memory.memories) if brain else 0,
    }


@app.post("/think")
async def think(req: ThinkRequest):
    """Ask GOD to think about something"""
    return await brain.think(
        req.question,
        req.context,
        req.include_services,
        req.include_evidence
    )


@app.post("/plan")
async def plan(req: PlanRequest):
    """Ask GOD to create a plan"""
    return await brain.plan(req.goal, req.constraints, req.resources)


@app.post("/act")
async def act(req: ActRequest):
    """Ask GOD to take action"""
    return await brain.act(req.action, req.target, req.parameters)


@app.post("/learn")
async def learn(req: LearnRequest):
    """Ask GOD to learn from evidence"""
    return await brain.learn(req.evidence_ids, req.summary)


@app.get("/memory")
async def memory(memory_type: str = None, limit: int = 10):
    """View brain memories"""
    return {
        "memories": brain.memory.recall(memory_type, limit),
        "total": len(brain.memory.memories),
    }


@app.delete("/memory/{memory_id}")
async def forget(memory_id: str):
    """Delete a memory"""
    brain.memory.forget(memory_id)
    return {"status": "forgotten", "memory_id": memory_id}


# ═══════════════════════════════════════════════════════════════
# 🎯 MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    import uvicorn
    import argparse
    
    parser = argparse.ArgumentParser(description='🧠 GOD AI Brain')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8500)
    parser.add_argument('--model', default=OLLAMA_MODEL)
    parser.add_argument('--reload', action='store_true')
    
    args = parser.parse_args()
    
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  🧠 GOD AI BRAIN                                              ║
║  Grand Orchestration Director                                 ║
║                                                               ║
║  Model: {args.model:<50} ║
║  Port: {args.port:<51} ║
║                                                               ║
║  Capabilities:                                                ║
║    /think  - Reason about questions                           ║
║    /plan   - Create action plans                              ║
║    /act    - Execute actions                                  ║
║    /learn  - Learn from evidence                              ║
║    /memory - View/manage memories                             ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "god_brain:app" if args.reload else app,
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
