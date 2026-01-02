import asyncio, json, time, requests, websockets

async def bridge():
    uri = "ws://127.0.0.1:5051"
    async with websockets.connect(uri) as ws:
        print("🔁 Noizy Chat Bridge online")
        seen = {}
        while True:
            try:
                # Listen for messages from chat UI
                try:
                    msg = await asyncio.wait_for(ws.recv(), timeout=1)
                    if msg.startswith("@"):
                        parts = msg.split()
                        agent, *args = parts
                        payload = {"cmd": args, "timestamp": time.time()}
                        requests.post("http://127.0.0.1:8765/publish",
                                      json={"topic": "chat_command", "payload": {"agent": agent[1:], **payload}})
                        print("Sent command:", payload)
                except asyncio.TimeoutError:
                    pass

                # Forward recent agent events into chat
                for t in ["diagnostics","repairs","dns_sync","voice_monitor","drive_scan","remote_bridge"]:
                    r = requests.get(f"http://127.0.0.1:8765/fetch/{t}")
                    if r.status_code == 200:
                        data = r.json()[-1:]  # latest
                        if data:
                            await ws.send(f"{t.upper()}: {json.dumps(data[0]['payload'])}")
                await asyncio.sleep(2)
            except Exception as e:
                print("bridge loop:", e)
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(bridge())