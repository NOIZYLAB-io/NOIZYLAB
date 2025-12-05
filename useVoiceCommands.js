/**
 * useVoiceCommands - Voice Command Hook
 * ======================================
 * React hook for voice input and command processing.
 */

import { useState, useRef, useCallback } from "react";

export default function useVoiceCommands(options = {}) {
  const {
    requireWakeword = false,
    autoProcess = true,
    onTranscript = null,
    onCommand = null,
    onEmotion = null,
    onError = null,
  } = options;

  const [isListening, setIsListening] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [emotion, setEmotion] = useState(null);
  const [lastCommand, setLastCommand] = useState(null);
  const [error, setError] = useState(null);

  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);
  const streamRef = useRef(null);

  const startListening = useCallback(async () => {
    try {
      setError(null);
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      streamRef.current = stream;

      mediaRecorderRef.current = new MediaRecorder(stream);
      chunksRef.current = [];

      mediaRecorderRef.current.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunksRef.current.push(e.data);
        }
      };

      mediaRecorderRef.current.onstop = async () => {
        if (autoProcess && chunksRef.current.length > 0) {
          const blob = new Blob(chunksRef.current, { type: "audio/webm" });
          await processAudio(blob);
        }
      };

      mediaRecorderRef.current.start(100); // Collect data every 100ms
      setIsListening(true);
    } catch (err) {
      const errorMsg = "Microphone access denied";
      setError(errorMsg);
      onError?.(errorMsg);
    }
  }, [autoProcess, onError]);

  const stopListening = useCallback(() => {
    if (mediaRecorderRef.current && isListening) {
      mediaRecorderRef.current.stop();
      setIsListening(false);
    }

    if (streamRef.current) {
      streamRef.current.getTracks().forEach((t) => t.stop());
      streamRef.current = null;
    }
  }, [isListening]);

  const processAudio = useCallback(async (blob) => {
    setIsProcessing(true);

    const formData = new FormData();
    formData.append("file", blob, "audio.webm");

    try {
      const params = new URLSearchParams({
        device: "web",
        require_wakeword: requireWakeword.toString(),
        generate_speech: "false",
      });

      const res = await fetch(
        `http://localhost:8080/voice/process?${params}`,
        { method: "POST", body: formData }
      );

      const data = await res.json();

      // Update state
      const text = data.transcription?.text || "";
      setTranscript(text);
      onTranscript?.(text);

      if (data.emotion) {
        setEmotion(data.emotion);
        onEmotion?.(data.emotion);
      }

      if (data.command_result) {
        setLastCommand(data.command_result);
        onCommand?.(data.command_result);
      }

      return data;
    } catch (err) {
      const errorMsg = "Voice processing failed";
      setError(errorMsg);
      onError?.(errorMsg);
      return null;
    } finally {
      setIsProcessing(false);
    }
  }, [requireWakeword, onTranscript, onCommand, onEmotion, onError]);

  const sendTextCommand = useCallback(async (text) => {
    setIsProcessing(true);

    try {
      const res = await fetch("http://localhost:8080/voice/command", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, device: "web" }),
      });

      const data = await res.json();

      setTranscript(text);
      if (data.command_result) {
        setLastCommand(data.command_result);
        onCommand?.(data.command_result);
      }

      return data;
    } catch (err) {
      const errorMsg = "Command failed";
      setError(errorMsg);
      onError?.(errorMsg);
      return null;
    } finally {
      setIsProcessing(false);
    }
  }, [onCommand, onError]);

  const speak = useCallback(async (text, voice = "default") => {
    try {
      const res = await fetch("http://localhost:8080/voice/speak", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, voice }),
      });

      const data = await res.json();

      if (data.success && data.audio_base64) {
        // Play audio
        const audio = new Audio(`data:audio/aiff;base64,${data.audio_base64}`);
        await audio.play();
      }

      return data;
    } catch (err) {
      console.error("TTS error:", err);
      return null;
    }
  }, []);

  const clearState = useCallback(() => {
    setTranscript("");
    setEmotion(null);
    setLastCommand(null);
    setError(null);
  }, []);

  return {
    // State
    isListening,
    isProcessing,
    transcript,
    emotion,
    lastCommand,
    error,

    // Actions
    startListening,
    stopListening,
    processAudio,
    sendTextCommand,
    speak,
    clearState,
  };
}

