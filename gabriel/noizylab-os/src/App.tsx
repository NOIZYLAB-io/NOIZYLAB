import { useEffect, useMemo, useState } from "react";
import {
  RealtimeKitProvider,
  useRealtimeKitClient,
} from "@cloudflare/realtimekit-react";
import { MeetingShell } from "./MeetingShell";

type JoinResp = { ok: boolean; authToken: string; meetingId: string; roomId: string; wsUrl: string };

function JoinForm({ onJoin }: { onJoin: (authToken: string, roomId: string, wsUrl: string) => void }) {
  const [code, setCode] = useState("");
  const [name, setName] = useState("");
  const [err, setErr] = useState<string | null>(null);

  return (
    <div style={{ maxWidth: 420, margin: "40px auto", fontFamily: "system-ui" }}>
      <h2>NoizyLab Live Help</h2>
      <p>Enter your 6-character code.</p>

      <input
        value={code}
        onChange={(e) => setCode(e.target.value.toUpperCase())}
        placeholder="CODE"
        style={{ width: "100%", padding: 12, fontSize: 18, marginBottom: 10 }}
      />
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Your name (optional)"
        style={{ width: "100%", padding: 12, fontSize: 16, marginBottom: 10 }}
      />

      <button
        style={{ width: "100%", padding: 12, fontSize: 16 }}
        onClick={async () => {
          setErr(null);
          const r = await fetch("/public/rtk/join", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code, name }),
          });
          const j = (await r.json()) as JoinResp;
          if (!j.ok) return setErr("Join failed. Check the code.");
          onJoin(j.authToken, j.roomId, j.wsUrl);
        }}
      >
        Join
      </button>

      {err && <p style={{ color: "crimson" }}>{err}</p>}
      <p style={{ opacity: 0.7, marginTop: 16 }}>
        If video is unstable, we can switch to audio-only in-call.
      </p>
    </div>
  );
}

export default function App() {
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [roomId, setRoomId] = useState<string | null>(null);
  const [wsUrl, setWsUrl] = useState<string | null>(null);

  const [meeting, initMeeting] = useRealtimeKitClient();

  useEffect(() => {
    if (!authToken) return;
    initMeeting({
      authToken,
      defaults: { audio: false, video: false },
    });
  }, [authToken]);

  if (!authToken || !roomId || !wsUrl) {
    return (
      <JoinForm
        onJoin={(t, rId, ws) => {
          setAuthToken(t);
          setRoomId(rId);
          setWsUrl(ws);
        }}
      />
    );
  }

  return (
    <RealtimeKitProvider value={meeting}>
      <MeetingShell wsUrl={wsUrl} ticketId={undefined} isStaff={false} />
    </RealtimeKitProvider>
  );
}
