/**
 * useVoiceXR - Voice State for VR
 * ================================
 * Tracks speaking/listening state for VR visualization.
 */

import { useState, useEffect, useCallback } from "react";

export default function useVoiceXR() {
  const [speaking, setSpeaking] = useState(false);
  const [listening, setListening] = useState(false);
  const [transcript, setTranscript] = useState("");

  // Simulate voice activity for demo
  useEffect(() => {
    // In production, this would connect to actual voice system
    const simulateActivity = () => {
      // Random voice activity simulation
      const rand = Math.random();
      if (rand > 0.95) {
        setListening(true);
        setTimeout(() => setListening(false), 2000);
      } else if (rand > 0.9) {
        setSpeaking(true);
        setTimeout(() => setSpeaking(false), 3000);
      }
    };

    const interval = setInterval(simulateActivity, 5000);
    return () => clearInterval(interval);
  }, []);

  // Start listening
  const startListening = useCallback(() => {
    setListening(true);
    
    // Would integrate with actual voice recognition
    setTimeout(() => {
      setListening(false);
      setTranscript("Voice input received");
    }, 3000);
  }, []);

  // Stop listening
  const stopListening = useCallback(() => {
    setListening(false);
  }, []);

  // Speak text
  const speak = useCallback((text) => {
    setSpeaking(true);
    
    // Would integrate with TTS
    const duration = Math.min(text.length * 50, 5000);
    setTimeout(() => setSpeaking(false), duration);
  }, []);

  return {
    speaking,
    listening,
    transcript,
    startListening,
    stopListening,
    speak
  };
}

