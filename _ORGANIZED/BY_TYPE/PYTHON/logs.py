from fastapi import APIRouter, WebSocket
import asyncio, datetime

router = APIRouter()


@router.websocket("/stream")
async def stream_logs(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json({
            "time": str(datetime.datetime.now()),
            "event": "heartbeat",
            "status": "ok"
        })
        await asyncio.sleep(2)
