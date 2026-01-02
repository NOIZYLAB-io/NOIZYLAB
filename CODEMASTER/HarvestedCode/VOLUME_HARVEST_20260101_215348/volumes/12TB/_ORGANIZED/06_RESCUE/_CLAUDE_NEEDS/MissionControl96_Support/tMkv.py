from __future__ import annotations
import os, asyncio, json
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
app = FastAPI(title="Watchtower (Advisory Mode)")
advice_queue: asyncio.Queue[str] = asyncio.Queue()
class LogEvent(BaseModel):
    source: str
    message: str
SYSTEM_PROMPT = ("You are Watchtower, a concise, proactive strategist overseeing a creative code+audio pipeline. "
                 "Bobby is the executor. For each log event, reply with short, actionable advice (max ~2 sentences). "
                 "Prioritize performance, reliability, safety, and next-step momentum.")
async def make_advice(user_text: str) -> str:
    if not client:
        return "No LLM configured. Set OPENAI_API_KEY to enable strategic advice."
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":SYSTEM_PROMPT},
                  {"role":"user","content":f"Bobby log: {user_text}"}],
        temperature=0.2, max_tokens=120,
    )
    return resp.choices[0].message.content.strip()
@app.post("/log")
async def receive_log(event: LogEvent):
    msg = event.message.strip()
    if not msg: raise HTTPException(400, "Empty message")
    advice = await make_advice(msg)
    await advice_queue.put(json.dumps({"from":"watchtower","advice":advice}))
    return {"ok": True, "advice": advice}
@app.get("/stream")
async def stream():
    async def gen():
        while True:
            yield f"data: {await advice_queue.get()}\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")
