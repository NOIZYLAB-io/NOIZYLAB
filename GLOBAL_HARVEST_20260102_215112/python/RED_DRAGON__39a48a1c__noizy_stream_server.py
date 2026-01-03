import os, asyncio, json
import websockets
from noizy_router import ask

CLIENTS = set()
CHAT_LOG = "chat_history.jsonl"

async def handle(ws):
    CLIENTS.add(ws)
    try:
        async for msg in ws:
            data = json.loads(msg)
            model = data.get("model", "openai")
            prompt = data.get("prompt", "")
            # append to history
            with open(CHAT_LOG, "a") as f:
                f.write(json.dumps({"role":"user","model":model,"text":prompt})+"\n")
            # stream the answer token by token
            reply = ask(model, prompt)
            for token in reply.split():
                await ws.send(token+" ")
                await asyncio.sleep(0.03)
            with open(CHAT_LOG, "a") as f:
                f.write(json.dumps({"role":"assistant","model":model,"text":reply})+"\n")
            await ws.send("\n<END>\n")
    finally:
        CLIENTS.remove(ws)

async def main():
    async with websockets.serve(handle, "127.0.0.1", 5051):
        print("🟢 Noizy Stream Server on ws://127.0.0.1:5051")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())