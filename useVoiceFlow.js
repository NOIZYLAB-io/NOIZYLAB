import { useEffect } from "react";

export default function useVoiceFlow(setFlowState) {
  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8080/noizyflow/checkvoice")
        .then((res) => res.json())
        .then((data) => {
          if (data.emotion === "distress") setFlowState("calm");
          if (data.emotion === "panic") setFlowState("emergency");
        })
        .catch(() => {
          // Silent fail - backend might not be running
        });
    }, 1500);

    return () => clearInterval(interval);
  }, [setFlowState]);
}

