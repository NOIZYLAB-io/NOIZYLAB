export class RoomDO {
  constructor(private state: DurableObjectState) {}

  broadcast(data: any) {
    const msg = JSON.stringify(data);
    for (const ws of this.state.getWebSockets("room")) {
      try { ws.send(msg); } catch {}
    }
  }

  async fetch(request: Request) {
    if (request.headers.get("Upgrade") !== "websocket") {
      return new Response("Expected websocket", { status: 400 });
    }

    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);

    this.state.acceptWebSocket(server, ["room"]);

    // Presence ping
    this.broadcast({ type: "presence", online: this.state.getWebSockets("room").length });

    server.addEventListener("message", (evt) => {
      let payload: any = evt.data;
      try { payload = JSON.parse(String(evt.data)); } catch {}
      this.broadcast({ type: "chat", at: Date.now(), payload });
    });

    server.addEventListener("close", () => {
      this.broadcast({ type: "presence", online: this.state.getWebSockets("room").length });
    });

    return new Response(null, { status: 101, webSocket: client });
  }
}
