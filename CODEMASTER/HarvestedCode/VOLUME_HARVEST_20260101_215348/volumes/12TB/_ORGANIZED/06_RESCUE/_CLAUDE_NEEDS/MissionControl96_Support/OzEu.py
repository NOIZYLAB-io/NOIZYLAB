from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log_queue = asyncio.Queue()

async def generate_advice(event: str) -> str:
    if not openai.api_key:
        return "OpenAI API key not set. Please set the OPENAI_API_KEY environment variable."
    prompt = f"You are Watchtower, overseeing Mission Control. Bobby just logged: {event}. What advice or strategy should you give?"
    try:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Be concise, strategic, and proactive."},
                      {"role": "user", "content": prompt}]
        )
        return resp["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error from OpenAI: {e}"

@app.post("/feed")
async def receive_log(event: dict):
    text = event.get("message", "")
    advice = await generate_advice(text)
    await log_queue.put({"from": "watchtower", "message": advice})
    return {"ok": True, "advice": advice}

@app.get("/stream")
async def stream():
    async def event_generator():
        while True:
            data = await log_queue.get()
            yield f"data: {json.dumps(data)}\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")
