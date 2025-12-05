import { useEffect } from 'react'
import { useSystemStore } from '../stores/systemStore'

export function useSnapshot(interval = 3000) {
  const setSnapshot = useSystemStore((s) => s.setSnapshot)

  useEffect(() => {
    const load = async () => {
      const r = await fetch('http://localhost:8000/snapshots')
      setSnapshot(await r.json())
    }
    load()
    const timer = setInterval(load, interval)
    return () => clearInterval(timer)
  }, [interval, setSnapshot])
}

