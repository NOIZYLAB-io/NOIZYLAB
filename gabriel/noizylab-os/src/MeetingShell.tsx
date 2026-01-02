import { useEffect, useMemo, useRef, useState } from "react";
import { RTKMeeting } from "@cloudflare/realtimekit-react-ui";

// Voice "Calm Mode" - reads NOW/NEXT/WHEN status updates
export function speakStatus(now: string, next: string, when: string, enabled: boolean, rate = 0.95) {
  if (!enabled || !("speechSynthesis" in window)) return;
  const u = new SpeechSynthesisUtterance(`${now}. Next: ${next}. Next update: ${when}.`);
  u.rate = rate;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(u);
}

type Props = {
  wsUrl: string;
  ticketId?: number; // optional if you wire staff console
  isStaff?: boolean; // if Access-gated staff UI
};

export function MeetingShell({ wsUrl, ticketId, isStaff }: Props) {
  const [tab, setTab] = useState<"chat" | "ai">("chat");

  // Chat state
  const [online, setOnline] = useState<number>(0);
  const [messages, setMessages] = useState<any[]>([]);
  const [text, setText] = useState("");
  const wsRef = useRef<WebSocket | null>(null);

  // AI state
  const [question, setQuestion] = useState<string>("");
  const [notes, setNotes] = useState<string[]>([]);
  const [aiBusy, setAiBusy] = useState(false);

  // Keep a running transcript from chat messages for AI notes
  const transcript = useMemo(() => {
    const last = messages.slice(-30);
    return last.map((m) => {
      const p = m?.payload ?? m;
      const who = p?.who ?? "user";
      const msg = p?.text ?? JSON.stringify(p);
      return `${who}: ${msg}`;
    }).join("\n");
  }, [messages]);

  useEffect(() => {
    const ws = new WebSocket(wsUrl);
    wsRef.current = ws;

    ws.onmessage = (evt) => {
      let data: any = evt.data;
      try { data = JSON.parse(String(evt.data)); } catch {}
      if (data?.type === "presence") setOnline(Number(data.online ?? 0));
      if (data?.type === "chat") setMessages((m) => [...m, data.payload ?? data]);
    };

    ws.onclose = () => {};
    return () => ws.close();
  }, [wsUrl]);

  function sendChat() {
    const ws = wsRef.current;
    if (!ws || ws.readyState !== 1) return;
    if (!text.trim()) return;

    ws.send(JSON.stringify({ who: isStaff ? "staff" : "client", text: text.trim() }));
    setText("");
  }

  async function getNextQuestion() {
    if (!ticketId) return setQuestion("Wire ticketId for staff AI.");
    setAiBusy(true);
    try {
      const r = await fetch("/staff/ai/next-question", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticketId, context: transcript }),
      });
      const j = await r.json();
      setQuestion(j.question || "");
    } finally {
      setAiBusy(false);
    }
  }

  async function getLiveNotes() {
    if (!ticketId) return setNotes(["Wire ticketId for staff AI."]);
    setAiBusy(true);
    try {
      const r = await fetch("/staff/ai/live-notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticketId, transcript }),
      });
      const j = await r.json();
      setNotes(Array.isArray(j.notes) ? j.notes : []);
    } finally {
      setAiBusy(false);
    }
  }

  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 360px", height: "100vh" }}>
      <div style={{ minWidth: 0 }}>
        <RTKMeeting />
      </div>

      <div style={{ borderLeft: "1px solid #ddd", padding: 12, fontFamily: "system-ui" }}>
        <div style={{ display: "flex", gap: 8, marginBottom: 10 }}>
          <button onClick={() => setTab("chat")} style={{ flex: 1, padding: 10 }}>
            Chat ({online})
          </button>
          <button onClick={() => setTab("ai")} style={{ flex: 1, padding: 10 }}>
            AI
          </button>
        </div>

        {tab === "chat" && (
          <>
            <div style={{ height: "70vh", overflow: "auto", border: "1px solid #eee", padding: 8 }}>
              {messages.map((m, i) => (
                <div key={i} style={{ marginBottom: 8 }}>
                  <div style={{ opacity: 0.6, fontSize: 12 }}>
                    {(m?.who ?? m?.payload?.who ?? "user")}
                  </div>
                  <div style={{ whiteSpace: "pre-wrap" }}>
                    {(m?.text ?? m?.payload?.text ?? JSON.stringify(m))}
                  </div>
                </div>
              ))}
            </div>

            <div style={{ display: "flex", gap: 8, marginTop: 10 }}>
              <input
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Type…"
                style={{ flex: 1, padding: 10 }}
                onKeyDown={(e) => e.key === "Enter" && sendChat()}
              />
              <button onClick={sendChat} style={{ padding: "10px 14px" }}>
                Send
              </button>
            </div>
          </>
        )}

        {tab === "ai" && (
          <>
            <div style={{ marginBottom: 12 }}>
              <div style={{ fontWeight: 700, marginBottom: 6 }}>Next-best question</div>
              <div style={{ border: "1px solid #eee", padding: 10, minHeight: 60 }}>
                {question || "—"}
              </div>
              <button
                disabled={!isStaff || aiBusy}
                onClick={getNextQuestion}
                style={{ width: "100%", padding: 10, marginTop: 8 }}
              >
                {aiBusy ? "Working…" : "Generate question"}
              </button>
            </div>

            <div>
              <div style={{ fontWeight: 700, marginBottom: 6 }}>Live notes (5 bullets)</div>
              <div style={{ border: "1px solid #eee", padding: 10, minHeight: 120 }}>
                {notes.length ? (
                  <ul style={{ margin: 0, paddingLeft: 18 }}>
                    {notes.map((n, i) => <li key={i}>{n}</li>)}
                  </ul>
                ) : "—"}
              </div>
              <button
                disabled={!isStaff || aiBusy}
                onClick={getLiveNotes}
                style={{ width: "100%", padding: 10, marginTop: 8 }}
              >
                {aiBusy ? "Working…" : "Generate notes"}
              </button>
            </div>

            {!isStaff && (
              <div style={{ marginTop: 12, opacity: 0.7, fontSize: 12 }}>
                AI controls are staff-only.
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
