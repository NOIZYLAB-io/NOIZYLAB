from fastapi import APIRouter,WebSocket,WebSocketDisconnect
router=APIRouter()
crew=[]
@router.websocket("/crew")
async def crewchat(ws:WebSocket):
    await ws.accept(); crew.append(ws)
    try:
        while True:
            msg=await ws.receive_text()
            for m in crew: await m.send_text(msg)
    except WebSocketDisconnect:
        crew.remove(ws)