import { useEffect, useState } from "react";

/**
 * useEmotionUI Hook
 * =================
 * Watches user input text and automatically adjusts UI mood.
 * Connects to GEN-4 Emotional AI backend.
 * 
 * Usage:
 *   const emotionData = useEmotionUI(text, setFlowState);
 */
export default function useEmotionUI(text, setFlowState) {
  const [emotionData, setEmotionData] = useState(null);

  useEffect(() => {
    // Don't analyze very short text
    if (!text || text.length < 3) return;

    // Debounce to avoid too many requests
    const timer = setTimeout(() => {
      fetch("http://localhost:8080/ai/emotion", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
      })
        .then((r) => r.json())
        .then((data) => {
          setEmotionData(data);

          // Auto-adjust flow state based on UI mode
          if (setFlowState) {
            if (data.ui_mode === "calm") {
              setFlowState("calm");
            } else if (data.mood === "distress") {
              setFlowState("emergency");
            } else if (data.ui_mode === "soft" || data.mood === "anxious") {
              setFlowState("calm");
            } else {
              setFlowState("normal");
            }
          }
        })
        .catch((err) => {
          console.error("Emotion analysis failed:", err);
        });
    }, 300); // 300ms debounce

    return () => clearTimeout(timer);
  }, [text, setFlowState]);

  return emotionData;
}

