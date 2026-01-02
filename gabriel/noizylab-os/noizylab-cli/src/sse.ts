import { http } from "./http.js";

export async function tailEvents(ticketId: number) {
  const base = process.env.NOIZYLAB_BASE_URL!.replace(/\/+$/, "");
  const url = `${base}/staff/events/stream?ticketId=${ticketId}`;

  const r = await fetch(url, {
    headers: (await import("./http.js")).http ? {} : {} // no-op; Access headers are added only via http()
  });

  // Use http() for Access headers by hitting a tiny helper endpoint:
  // Simpler: just duplicate Access headers here:
  const id = process.env.CF_ACCESS_CLIENT_ID;
  const secret = process.env.CF_ACCESS_CLIENT_SECRET;
  const rr = await fetch(url, {
    headers: {
      ...(id && secret ? { "CF-Access-Client-Id": id, "CF-Access-Client-Secret": secret } : {})
    }
  });

  if (!rr.ok || !rr.body) throw new Error(`SSE failed: ${rr.status}`);

  const reader = rr.body.getReader();
  const dec = new TextDecoder();
  let buf = "";

  console.log("Tailing events (Ctrl+C to quit)");
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });

    // crude SSE parse: print full data lines
    const parts = buf.split("\n\n");
    buf = parts.pop() ?? "";
    for (const block of parts) {
      const dataLine = block.split("\n").find(l => l.startsWith("data: "));
      if (dataLine) {
        try { console.log(JSON.stringify(JSON.parse(dataLine.slice(6)), null, 2)); }
        catch { console.log(dataLine.slice(6)); }
      }
    }
  }
}
