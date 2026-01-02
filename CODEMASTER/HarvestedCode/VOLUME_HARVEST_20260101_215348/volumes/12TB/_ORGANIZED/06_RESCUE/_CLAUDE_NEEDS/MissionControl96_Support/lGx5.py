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
