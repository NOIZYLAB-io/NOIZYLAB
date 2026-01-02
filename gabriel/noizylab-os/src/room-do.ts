export class RoomDO {
  constructor(private state: DurableObjectState) {}

  private broadcast(msg: any) {
    const data = JSON.stringify(msg);
    for (const ws of this.state.getWebSockets("room")) {
      try { ws.send(data); } catch {}
    }
  }

  async fetch(request: Request) {
    if (request.headers.get("Upgrade") !== "websocket") {
      return new Response("Expected websocket", { status: 400 });
    }

    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);

    // Hibernation API: accept + tag
    this.state.acceptWebSocket(server, ["room"]);

    // Attach tiny identity payload (survives hibernation)
    server.serializeAttachment({ joinedAt: Date.now() });

    this.broadcast({ type: "presence", online: this.state.getWebSockets("room").length });
    return new Response(null, { status: 101, webSocket: client });
  }

  // Hibernation handlers
  webSocketMessage(ws: WebSocket, message: string | ArrayBuffer) {
    let payload: any = message;
    try { payload = JSON.parse(String(message)); } catch {}

    // Minimal schema: {who, text, kind}
    this.broadcast({ type: "chat", at: Date.now(), payload });
  }

  webSocketClose(ws: WebSocket) {
    this.broadcast({ type: "presence", online: this.state.getWebSockets("room").length });
  }
}
