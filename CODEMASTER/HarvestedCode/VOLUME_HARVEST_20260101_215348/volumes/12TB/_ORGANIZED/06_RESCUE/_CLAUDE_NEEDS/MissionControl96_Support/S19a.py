from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import logging
import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Noizy.ai cockpit is live"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        timestamp = datetime.datetime.now().isoformat()
        logging.info(f"[{timestamp}] Received: {data}")
        await websocket.send_text(f"Echo: {data}")
        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
