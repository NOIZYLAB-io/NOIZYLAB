import WebSocket from "ws";

export async function wsSend(wsUrl: string, payload: any): Promise<void> {
  await new Promise<void>((resolve, reject) => {
    const ws = new WebSocket(wsUrl);

    ws.on("open", () => {
      ws.send(JSON.stringify(payload));
      ws.close();
    });

    ws.on("close", () => resolve());
    ws.on("error", (e) => reject(e));
  });
}

export async function wsListen(wsUrl: string): Promise<void> {
  const ws = new WebSocket(wsUrl);

  ws.on("open", () => {
    console.log("WS connected");
  });

  ws.on("message", (msg) => {
    try {
      console.log(JSON.stringify(JSON.parse(msg.toString()), null, 2));
    } catch {
      console.log(msg.toString());
    }
  });

  ws.on("close", () => console.log("WS closed"));
  ws.on("error", (e) => console.error("WS error", e));
}
