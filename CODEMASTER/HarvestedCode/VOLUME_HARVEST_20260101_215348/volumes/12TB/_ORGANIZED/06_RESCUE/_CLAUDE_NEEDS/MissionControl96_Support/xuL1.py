import asyncio, json, time, requests, websockets

async def forward_events():
    async with websockets.connect("ws://127.0.0.1:5051") as ws:
        print("🎧 Chat bridge connected to Noizy Stream")
        seen = {}
        while True:
            try:
                topics = ["diagnostics","repairs","voice_monitor","dns_sync","net_opt","telemetry","remote_sync","predictions","autoupdate"]
                for t in topics:
                    r = requests.get(f"http://127.0.0.1:8765/fetch_since/{t}?since={seen.get(t, time.time()-5)}")
                    if r.status_code == 200:
                        data = r.json()
                        if data:
                            seen[t] = max(e["ts"] for e in data)
                            for e in data:
                                txt = f"{t.upper()}: {json.dumps(e['payload'])}"
                                await ws.send(txt)
                await asyncio.sleep(2)
            except Exception as e:
                print("bridge error:", e)
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(forward_events())