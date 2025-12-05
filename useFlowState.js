import { useState, useCallback } from "react";

export default function useFlowState(initialState = "normal") {
  const [flowState, setFlowState] = useState(initialState);
  const [history, setHistory] = useState([initialState]);

  const updateFlow = useCallback((newState) => {
    setFlowState(newState);
    setHistory((prev) => [...prev.slice(-9), newState]);
  }, []);

  const resetFlow = useCallback(() => {
    setFlowState("normal");
  }, []);

  const getFlowColor = useCallback(() => {
    switch (flowState) {
      case "calm": return "#00E5FF";
      case "emergency": return "#FF3747";
      case "soften": return "#FFAA00";
      default: return "#F5C542";
    }
  }, [flowState]);

  const getBgColor = useCallback(() => {
    switch (flowState) {
      case "calm": return "#001F2F";
      case "emergency": return "#2F0000";
      case "soften": return "#332200";
      default: return "#000000";
    }
  }, [flowState]);

  return {
    flowState,
    setFlowState: updateFlow,
    resetFlow,
    getFlowColor,
    getBgColor,
    history
  };
}

