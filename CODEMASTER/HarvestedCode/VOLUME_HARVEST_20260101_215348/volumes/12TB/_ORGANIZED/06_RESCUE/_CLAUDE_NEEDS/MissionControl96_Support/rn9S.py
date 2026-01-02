import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
/** @type {import('tailwindcss').Config} */
export default defineConfig({
  plugins: [react()],
  css: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },
});

<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bobby’s Mission Control</title>
  </head>
  <body class="bg-zinc-950 text-zinc-100">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import './index.css'

createRoot(document.getElementById('root')!).render(<App />)

@tailwind base;
@tailwind components;
@tailwind utilities;

const BASE = import.meta.env.VITE_BOBBY_API || 'http://127.0.0.1:8765';
export const endpoints = {
  health: () => fetch(`${BASE}/health`).then(r => r.json()),
  narrate: (text: string) => fetch(`${BASE}/narrate`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text }) }).then(r => r.json()),
  scan: () => fetch(`${BASE}/scan-wavs`).then(r => r.json()),
  dupes: (quarantine = true) => fetch(`${BASE}/dupe-killer`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ quarantine }) }).then(r => r.json()),
  runScript: () => fetch(`${BASE}/run-script`).then(r => r.json()),
  feed: () => new EventSource(`${BASE}/feed`),
};

export function CrewBoard({ status }: { status: Record<string, string> }) {
  const badge = (s: string) => s === 'online' ? 'bg-emerald-500' : s === 'busy' ? 'bg-amber-500' : 'bg-rose-500';
  return (
    <section className="space-y-3">
      <h2 className="text-lg font-semibold">The Crew</h2>
      <div className="grid grid-cols-2 gap-3">
        {Object.entries(status).map(([name, st]) => (
          <div key={name} className="rounded-2xl border border-zinc-800 bg-zinc-900 p-4">
            <div className="flex items-center justify-between">
              <div className="capitalize text-sm font-medium">{name}</div>
              <span className={`inline-block w-2.5 h-2.5 rounded-full ${badge(st)}`} title={st} />
            </div>
            <div className="mt-1 text-xs text-zinc-400">{st}</div>
          </div>
        ))}
      </div>
    </section>
  )
}

import React, { useEffect, useRef } from 'react'

export function MissionFeed({ logs }: { logs: string[] }) {
  const endRef = useRef<HTMLDivElement|null>(null)
  useEffect(() => { endRef.current?.scrollIntoView({ behavior: 'smooth' }) }, [logs])
  return (
    <section className="space-y-3">
      <h2 className="text-lg font-semibold">Live Activity</h2>
      <div className="rounded-2xl border border-zinc-800 bg-zinc-900/60 p-0 overflow-hidden">
        <ul className="divide-y divide-zinc-800 max-h-[520px] overflow-auto">
          {logs.map((e, i) => (
            <li key={i} className="px-4 py-3 text-sm text-zinc-300">{e}</li>
          ))}
          <div ref={endRef} />
        </ul>
      </div>
    </section>
  )
}

import React, { useState } from 'react'

export function Playbook({ onNarrate, onScan, onDupes, onRun }: {
  onNarrate: (text: string) => void;
  onScan: () => void;
  onDupes: () => void;
  onRun: () => void;
}) {
  const [text, setText] = useState("")
  return (
    <section className="space-y-3">
      <h2 className="text-lg font-semibold">Playbook</h2>
      <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-4">
        <input className="w-full bg-zinc-800 rounded p-2 mb-2" placeholder="Text to narrate" value={text} onChange={e=>setText(e.target.value)} />
        <button className="w-full rounded bg-emerald-600 hover:bg-emerald-500 py-2 text-sm" onClick={()=> text && onNarrate(text)}>Narrate Text</button>
      </div>
      <button className="w-full rounded bg-zinc-800 hover:bg-zinc-700 py-2 text-sm" onClick={onScan}>Scan WAVs</button>
      <button className="w-full rounded bg-zinc-800 hover:bg-zinc-700 py-2 text-sm" onClick={onDupes}>Big Dupe Killer</button>
      <button className="w-full rounded bg-zinc-800 hover:bg-zinc-700 py-2 text-sm" onClick={onRun}>Run Script</button>
    </section>
  )
}

import React, { useEffect, useMemo, useState } from 'react'
import { endpoints } from './lib/api'
import { CrewBoard } from './components/CrewBoard'
import { MissionFeed } from './components/MissionFeed'
import { Playbook } from './components/Playbook'

export default function App(){
  const [logs, setLogs] = useState<string[]>([])
  const [status, setStatus] = useState<Record<string,string>>({ narrator: 'offline', dupeKiller: 'offline', metadataBot: 'offline', mcp: 'offline' })

  const pushLog = (msg: string) => setLogs(prev => [...prev, msg])

  useEffect(()=>{
    const es = endpoints.feed()
    es.onmessage = (e) => {
      try {
        const obj = JSON.parse(e.data)
        pushLog(`${obj.level?.toUpperCase?.() || 'LOG'} • ${obj.msg}`)
      } catch { pushLog(String(e.data)) }
    }
    endpoints.health().then(setStatus).catch(()=>{})
    const t = setInterval(()=> endpoints.health().then(setStatus).catch(()=>{}), 5000)
    return ()=>{ es.close(); clearInterval(t) }
  },[])

  const activePct = useMemo(()=>{
    const vals = Object.values(status)
    const active = vals.filter(v=>v==='online' || v==='busy').length
    return Math.round((active / Math.max(1, vals.length)) * 100)
  },[status])

  return (
    <div className="min-h-screen w-full bg-zinc-950 text-zinc-100">
      <header className="sticky top-0 z-20 backdrop-blur bg-zinc-900/60 border-b border-zinc-800">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold tracking-tight">Bobby’s Mission Control</h1>
            <p className="text-sm text-zinc-400">Live systems view • Playbook • Crew status</p>
          </div>
          <div className="flex items-center gap-4">
            <div className="text-xs text-zinc-400">{activePct}% crew active</div>
            <div className="w-40 h-2 bg-zinc-800 rounded-full overflow-hidden">
              <div className="h-full bg-emerald-500" style={{ width: `${activePct}%` }} />
            </div>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto px-4 py-6 grid grid-cols-12 gap-6">
        <section className="col-span-12 xl:col-span-4"><CrewBoard status={status}/></section>
        <section className="col-span-12 xl:col-span-5"><MissionFeed logs={logs}/></section>
        <section className="col-span-12 xl:col-span-3">
          <Playbook
            onNarrate={async (text)=>{ const r= await endpoints.narrate(text); if(r.status==='ok') pushLog(`OK • ${r.file}`); else pushLog(`ERR • ${r.message}`) }}
            onScan={async ()=>{ const r= await endpoints.scan(); pushLog(`SCAN • ${r.count} files`)} }
            onDupes={async ()=>{ const r= await endpoints.dupes(true); pushLog(`DUPES • groups ${Object.keys(r.groups||{}).length}`)} }
            onRun={async ()=>{ const r= await endpoints.runScript(); pushLog(r.output||'Ran')} }
          />
        </section>
      </main>
      <footer className="max-w-7xl mx-auto px-4 pb-8 text-xs text-zinc-500">Hook new actions in backend/actions/* — Bobby will pick them up.</footer>
    </div>
  )
}
