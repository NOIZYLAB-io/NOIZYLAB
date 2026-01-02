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
