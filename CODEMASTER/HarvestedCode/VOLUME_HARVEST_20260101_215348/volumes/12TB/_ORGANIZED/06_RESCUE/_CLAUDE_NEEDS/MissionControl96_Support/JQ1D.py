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

.chat-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}
