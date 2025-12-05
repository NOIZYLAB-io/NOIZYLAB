import { useEffect } from 'react'
import { useSystemStore } from '../stores/systemStore'

export function useLogs() {
  const addLog = useSystemStore((s) => s.addLog)

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/logs/stream')
    ws.onmessage = (e) => addLog(JSON.parse(e.data))
    return () => ws.close()
  }, [addLog])
}

