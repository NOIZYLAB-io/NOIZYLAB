import { useEffect, useState } from "react";
import {
  RealtimeKitProvider,
  useRealtimeKitClient,
} from "@cloudflare/realtimekit-react";
import { RTKMeeting } from "@cloudflare/realtimekit-react-ui";

type StartResp = {
  ok: boolean;
  roomId: string;
  code: string;
  expiresAt: string;
  meetingId: string;
  staffAuthToken: string;
};

async function startSession(ticketId?: number) {
  const r = await fetch("/staff/rtk/start", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ticketId, staffName: "Rob/NoizyLab" }),
  });
  return await r.json();
}

export default function StaffSession() {
  const [session, setSession] = useState<StartResp | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [meeting, initMeeting] = useRealtimeKitClient();

  const handleStart = async (ticketId?: number) => {
    setErr(null);
    const res = (await startSession(ticketId)) as StartResp;
    if (!res.ok) return setErr("Failed to start session");
    setSession(res);
  };

  useEffect(() => {
    if (!session?.staffAuthToken) return;
    initMeeting({
      authToken: session.staffAuthToken,
      defaults: { audio: true, video: true },
    });
  }, [session?.staffAuthToken]);

  if (!session) {
    return (
      <div style={{ maxWidth: 420, margin: "40px auto", fontFamily: "system-ui" }}>
        <h2>Staff: Start Live Help</h2>
        <button
          style={{ width: "100%", padding: 12, fontSize: 16 }}
          onClick={() => handleStart()}
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
        <RTKMeeting />
      </RealtimeKitProvider>
    </div>
  );
}
