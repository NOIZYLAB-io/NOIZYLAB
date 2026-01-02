import { useEffect, useState } from "react";
import {
  RealtimeKitProvider,
  useRealtimeKitClient,
} from "@cloudflare/realtimekit-react";
import { MeetingShell } from "./MeetingShell";

type StartResp = {
  ok: boolean;
  roomId: string;
  code: string;
  expiresAt: string;
  meetingId: string;
  staffAuthToken: string;
  wsUrl?: string;
  ticketId?: number;
};

async function startSession(ticketId?: number) {
  const r = await fetch("/staff/rtk/start", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ticketId, staffName: "Rob/NoizyLab" }),
  });
  return await r.json();
}

export default function StaffSession({ ticketId }: { ticketId?: number }) {
  const [session, setSession] = useState<StartResp | null>(null);
  const [wsUrl, setWsUrl] = useState<string | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [meeting, initMeeting] = useRealtimeKitClient();

  const handleStart = async () => {
    setErr(null);
    const res = (await startSession(ticketId)) as StartResp;
    if (!res.ok) return setErr("Failed to start session");
    setSession(res);
    
    // Build wsUrl for chat
    const origin = window.location.origin;
    const wsProtocol = origin.startsWith('https') ? 'wss' : 'ws';
    const wsOrigin = origin.replace(/^http/, wsProtocol);
    setWsUrl(`${wsOrigin}/ws/room/${res.roomId}`);
  };

  useEffect(() => {
    if (!session?.staffAuthToken) return;
    initMeeting({
      authToken: session.staffAuthToken,
      defaults: { audio: true, video: true },
    });
  }, [session?.staffAuthToken]);

  if (!session || !wsUrl) {
    return (
      <div style={{ maxWidth: 420, margin: "40px auto", fontFamily: "system-ui" }}>
        <h2>Staff: Start Live Help</h2>
        {ticketId && <p style={{ opacity: 0.7 }}>Ticket #{ticketId}</p>}
        <button
          style={{ width: "100%", padding: 12, fontSize: 16 }}
          onClick={handleStart}
        >
          Start Session
        </button>
        {err && <p style={{ color: "crimson" }}>{err}</p>}
      </div>
    );
  }

  return (
    <div style={{ fontFamily: "system-ui" }}>
      <div style={{ background: "#222", color: "#fff", padding: 16, textAlign: "center" }}>
        <p>
          Client Code: <strong style={{ fontSize: 24, letterSpacing: 4 }}>{session.code}</strong>
        </p>
        <p style={{ opacity: 0.7 }}>Expires: {new Date(session.expiresAt).toLocaleTimeString()}</p>
      </div>
      <RealtimeKitProvider value={meeting}>
        <MeetingShell wsUrl={wsUrl} ticketId={ticketId} isStaff={true} />
      </RealtimeKitProvider>
    </div>
  );
}
