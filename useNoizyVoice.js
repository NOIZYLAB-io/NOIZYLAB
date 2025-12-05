import { useState, useRef, useCallback } from "react";

/**
 * useNoizyVoice Hook
 * ==================
 * Handles microphone recording, Whisper transcription, and emotion-based UI.
 * 
 * Features:
 * - 3-second auto-capture
 * - Voice → Text → Emotion → UI pipeline
 * - Automatic CalmMode triggering
 * - Chat message integration
 * 
 * Usage:
 *   const { start, stop, recording, transcript } = useNoizyVoice(setFlowState, setMessages);
 */
export default function useNoizyVoice(setFlowState, setMessages) {
  const [recording, setRecording] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [error, setError] = useState(null);
  
  const mediaRef = useRef(null);
  const recorderRef = useRef(null);
  const chunksRef = useRef([]);

  const start = useCallback(async () => {
    setError(null);
    setRecording(true);
    chunksRef.current = [];

    try {
      // Request microphone access
      const stream = await navigator.mediaDevices.getUserMedia({ 
        audio: {
          echoCancellation: true,
          noiseSuppression: true,
          autoGainControl: true
        } 
      });
      
      mediaRef.current = stream;
      
      // Create recorder
      const recorder = new MediaRecorder(stream, {
        mimeType: MediaRecorder.isTypeSupported('audio/webm') 
          ? 'audio/webm' 
          : 'audio/mp4'
      });
      recorderRef.current = recorder;

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunksRef.current.push(e.data);
        }
      };

      recorder.onstop = async () => {
        // Stop all tracks
        stream.getTracks().forEach(track => track.stop());
        
        if (chunksRef.current.length === 0) {
          setRecording(false);
          return;
        }

        // Create blob from chunks
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        
        // Send to backend
        const form = new FormData();
        form.append("file", blob, "voice.webm");

        try {
          const res = await fetch("http://localhost:8080/voice/transcribe", {
            method: "POST",
            body: form,
          });

          const data = await res.json();
          setTranscript(data.text);

          // Update UI mode based on emotion
          if (setFlowState) {
            setFlowState(data.ui_mode || "normal");
          }

          // Add to chat messages
          if (setMessages && data.text) {
            setMessages(prev => [
              ...prev,
              { 
                type: "user", 
                text: `🎤 ${data.text}`,
                mood: data.mood || "neutral"
              }
            ]);

            // If there's an empathy response, add it
            if (data.empathy_response) {
              setMessages(prev => [
                ...prev,
                {
                  type: "ai",
                  text: `🤖 ${data.empathy_response}`,
                  mood: data.mood
                }
              ]);
            }
          }
        } catch (err) {
          setError("Failed to transcribe audio");
          console.error("Transcription error:", err);
        }
        
        setRecording(false);
      };

      // Start recording
      recorder.start(100); // Collect data every 100ms

      // Auto-stop after 3 seconds
      setTimeout(() => {
        if (recorderRef.current && recorderRef.current.state === "recording") {
          recorderRef.current.stop();
        }
      }, 3000);

    } catch (err) {
      setError("Microphone access denied");
      setRecording(false);
      console.error("Microphone error:", err);
    }
  }, [setFlowState, setMessages]);

  const stop = useCallback(() => {
    if (recorderRef.current && recorderRef.current.state === "recording") {
      recorderRef.current.stop();
    }
    setRecording(false);
  }, []);

  return { 
    start, 
    stop, 
    recording, 
    transcript,
    error
  };
}

