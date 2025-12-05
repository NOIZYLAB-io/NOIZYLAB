/**
 * useSyncXR - WebSocket Sync for VR
 * ==================================
 * Connects to NoizySync for real-time updates in VR.
 */

import { useState, useEffect, useCallback } from "react";

const WS_URL = "ws://localhost:8080/ws/sync";

export default function useSyncXR(setFlowState) {
  const [syncData, setSyncData] = useState({
    nodes: [],
    flowState: "normal",
    mood: "neutral",
    threats: []
  });
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    let ws = null;
    let reconnectTimer = null;

    const connect = () => {
      try {
        ws = new WebSocket(WS_URL);

        ws.onopen = () => {
          console.log("NoizySync VR connected");
          setConnected(true);
        };

        ws.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data);

            // Handle different sync types
            if (data.type === "flowState" && setFlowState) {
              setFlowState(data.flowState);
              setSyncData(prev => ({ ...prev, flowState: data.flowState }));
            }

            if (data.type === "emergency") {
              if (setFlowState) setFlowState("emergency");
              setSyncData(prev => ({ 
                ...prev, 
                flowState: "emergency",
                threats: [...prev.threats, data.reason]
              }));
            }

            if (data.type === "omenStats") {
              setSyncData(prev => ({ ...prev, omenStats: data.stats }));
            }

            if (data.type === "voiceEvent") {
              setSyncData(prev => ({ ...prev, mood: data.mood }));
            }

          } catch (e) {
            console.error("Sync parse error:", e);
          }
        };

        ws.onclose = () => {
          console.log("NoizySync VR disconnected");
          setConnected(false);
          // Reconnect after 3 seconds
          reconnectTimer = setTimeout(connect, 3000);
        };

        ws.onerror = (error) => {
          console.error("NoizySync VR error:", error);
        };

      } catch (e) {
        console.error("WebSocket connection failed:", e);
        reconnectTimer = setTimeout(connect, 3000);
      }
    };

    connect();

    return () => {
      if (ws) ws.close();
      if (reconnectTimer) clearTimeout(reconnectTimer);
    };
  }, [setFlowState]);

  // Push updates to other devices
  const push = useCallback((data) => {
    // Would send via WebSocket
    console.log("Sync push:", data);
  }, []);

  return { syncData, connected, push };
}

