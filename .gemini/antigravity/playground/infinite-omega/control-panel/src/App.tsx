import React, { useState, useEffect } from 'react';
import { Mic2, Settings, History, Play, Database, Server, Volume2 } from 'lucide-react';

// Hardcoded for demo/local persistence, or fetch from worker
const PERSONAS = [
  { id: 'titan', name: 'Thunder Titan', desc: 'Deep, Resonant, Stormy' },
  { id: 'solar', name: 'Solar Sentinel', desc: 'Bright, Warm, Optimistic' },
  { id: 'void', name: 'Void Ranger', desc: 'Calm, Technical, Mysterious' },
  { id: 'architect', name: 'Mythic Architect', desc: 'Wise, Structured, Visionary' },
  { id: 'director', name: 'The Director', desc: 'Screenplay, Cinematic Commands' }
];

const DSP_PRESETS = [
  { id: 'balanced', name: 'Balanced', desc: 'Default Clarity' },
  { id: 'stable', name: 'Hyper-Stable', desc: 'News/Reporting' },
  { id: 'expressive', name: 'High Expression', desc: 'Dynamic/Drama' },
  { id: 'extreme', name: 'Extreme', desc: 'Experimental/Chaos' }
];

function App() {
  const [mode, setMode] = useState<'solo' | 'dialogue'>('solo');
  const [dialogueLines, setDialogueLines] = useState<{id: string, personaId: string, text: string, audioUrl?: string}[]>([
    { id: '1', personaId: 'titan', text: 'I am the storm.' },
    { id: '2', personaId: 'solar', text: 'And I am the light that breaks it.' }
  ]);
  const [playingScene, setPlayingScene] = useState(false);

  // Poll logs (mock/demo implementation - replace with actual fetch from worker /audit if CORS allows)
  useEffect(() => {
    // Mock Logs for UI Demo
    setLogs([
      { id: '1', timestamp: new Date().toISOString(), persona: 'Thunder Titan', originalText: 'System initialized.', dsp: 'Balanced' },
    ]);
  }, []);

  const handleGenerate = async () => {
    setLoading(true);
    setVisemeData([]); // Reset visualizer
    try {
      const WORKER_URL = "https://voice-worker.rsplowman.workers.dev"; 
      
      const res = await fetch(`${WORKER_URL}/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          text, 
          personaId: persona, 
          dspId: dsp, 
          rewrite 
        })
      });

      if (!res.ok) throw new Error(await res.text());
      
      const data = await res.json();
      const fullAudioUrl = `${WORKER_URL}${data.data.url}`;
      setAudioUrl(fullAudioUrl);
      
      if (data.data.visemes) setVisemeData(data.data.visemes);
      
      setLogs(prev => [{
        id: data.data.id,
        timestamp: new Date().toISOString(),
        persona: PERSONAS.find(p => p.id === persona)?.name,
        originalText: text,
        dsp: DSP_PRESETS.find(d => d.id === dsp)?.name
      }, ...prev]);

    } catch (e: any) {
      alert("Generation Failed: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateScene = async () => {
      setLoading(true);
      const WORKER_URL = "https://voice-worker.rsplowman.workers.dev";
      const newLines = [...dialogueLines];

      for (let i = 0; i < newLines.length; i++) {
          const line = newLines[i];
          if (line.audioUrl) continue; // Skip if already generated

          try {
              const res = await fetch(`${WORKER_URL}/generate`, {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ 
                      text: line.text, 
                      personaId: line.personaId, 
                      dspId: dsp 
                  })
              });
              if (res.ok) {
                  const data = await res.json();
                  newLines[i].audioUrl = `${WORKER_URL}${data.data.url}`;
                  setDialogueLines([...newLines]); // Update incrementally
              }
          } catch (e) {
              console.error(e);
          }
      }
      setLoading(false);
  };

  const playScene = async () => {
      setPlayingScene(true);
      for (const line of dialogueLines) {
          if (line.audioUrl) {
              const audio = new Audio(line.audioUrl);
              await new Promise(resolve => {
                  audio.onended = resolve;
                  audio.play();
              });
          }
      }
      setPlayingScene(false);
  };

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 p-8 flex flex-col items-center">
      <header className="w-full max-w-4xl mb-10 flex items-center justify-between border-b border-gray-800 pb-4">
        <div className="flex items-center gap-2">
          <Server className="text-cyan-400" size={32} />
          <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
            VOICE FORGE <span className="text-gray-600 font-mono text-lg">COCKPIT</span>
          </h1>
        </div>
        <div className="flex gap-4 text-sm text-gray-500 font-mono">
           <button onClick={() => setMode('solo')} className={`px-2 hover:text-white ${mode === 'solo' ? 'text-blue-400 font-bold' : 'text-gray-600'}`}>SOLO</button>
           <button onClick={() => setMode('dialogue')} className={`px-2 hover:text-white ${mode === 'dialogue' ? 'text-blue-400 font-bold' : 'text-gray-600'}`}>DIALOGUE</button>
        </div>
      </header>

      <main className="w-full max-w-4xl grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* CONTROL PANEL */}
        <div className="space-y-6">
          
          {/* Persona Select */}
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-2xl">
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2"><Mic2 size={20} className="text-purple-400"/> Persona</h2>
            <div className="grid grid-cols-1 gap-2">
              {PERSONAS.map(p => (
                <button 
                  key={p.id}
                  onClick={() => setPersona(p.id)}
                  title={p.desc}
                  className={`p-3 rounded-lg text-left transition-all ${persona === p.id ? 'bg-purple-900/40 border border-purple-500/50 text-white' : 'bg-gray-800/50 text-gray-400 hover:bg-gray-800 border border-transparent'}`}
                >
                  <div className="font-medium">{p.name}</div>
                  <div className="text-xs opacity-70">{p.desc}</div>
                </button>
              ))}
            </div>
          </div>

          {/* DSP Select */}
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-2xl">
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2"><Settings size={20} className="text-green-400"/> DSP Engine</h2>
            <div className="grid grid-cols-2 gap-2">
              {DSP_PRESETS.map(d => (
                <button 
                  key={d.id}
                  onClick={() => setDsp(d.id)}
                  title={d.desc}
                  className={`p-3 rounded-lg text-left transition-all ${dsp === d.id ? 'bg-green-900/30 border border-green-500/50 text-white' : 'bg-gray-800/50 text-gray-400 hover:bg-gray-800 border border-transparent'}`}
                >
                  <div className="font-medium text-sm">{d.name}</div>
                </button>
              ))}
            </div>
          </div>

        </div>

        {/* INPUT & STATUS */}
        <div className="space-y-6 flex flex-col">
          
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-2xl flex-grow flex flex-col">
             
             {mode === 'solo' ? (
                <>
                <div className="mb-4 flex justify-between items-center">
                    <h2 className="text-xl font-semibold flex items-center gap-2"><Database size={20} className="text-blue-400"/> Input</h2>
                    <div className="flex items-center gap-2">
                    <span className="text-sm text-gray-400">Claude Director</span>
                    <button 
                        onClick={() => setRewrite(!rewrite)}
                        className={`w-10 h-5 rounded-full transition-colors ${rewrite ? 'bg-blue-500' : 'bg-gray-700'}`}
                    >
                        <div className={`w-4 h-4 bg-white rounded-full mt-0.5 ml-0.5 transition-transform ${rewrite ? 'translate-x-5' : 'translate-x-0'}`}></div>
                    </button>
                    </div>
                </div>
                
                <textarea 
                    value={text}
                    onChange={e => setText(e.target.value)}
                    placeholder={persona === 'director' ? "Describe the scene..." : "Enter text here..."}
                    className="w-full bg-gray-950 border border-gray-700 rounded-lg p-4 text-gray-200 focus:outline-none focus:border-blue-500 font-mono text-sm flex-grow min-h-[150px]"
                />
                
                <button 
                    onClick={handleGenerate}
                    disabled={loading || !text}
                    title="Generate Audio"
                    className="mt-4 w-full py-4 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-bold rounded-lg shadow-lg shadow-blue-900/20 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 transition-transform active:scale-[0.98]"
                >
                    {loading ? (
                        <span className="animate-spin mr-2">⟳</span> 
                    ) : <Play fill="currentColor" />}
                    {loading ? "DIRECTING..." : "ACTION"}
                </button>
                </>
             ) : (
                 <>
                 <div className="mb-4 flex justify-between items-center">
                    <h2 className="text-xl font-semibold flex items-center gap-2"><History size={20} className="text-blue-400"/> Dialogue Script</h2>
                 </div>
                 <div className="flex-grow overflow-y-auto space-y-2 mb-4 max-h-[400px]">
                    {dialogueLines.map((line, idx) => (
                        <div key={line.id} className="flex gap-2 p-2 bg-gray-950/50 rounded border border-gray-800">
                            <select 
                                value={line.personaId}
                                onChange={e => {
                                    const newLines = [...dialogueLines];
                                    newLines[idx].personaId = e.target.value;
                                    setDialogueLines(newLines);
                                }}
                                className="bg-gray-900 text-xs text-purple-400 border border-gray-700 rounded p-1 w-24"
                            >
                                {PERSONAS.map(p => <option key={p.id} value={p.id}>{p.name.split(' ')[0]}</option>)}
                            </select>
                            <input 
                                value={line.text}
                                onChange={e => {
                                    const newLines = [...dialogueLines];
                                    newLines[idx].text = e.target.value;
                                    setDialogueLines(newLines);
                                }}
                                className="bg-transparent border-none text-sm text-gray-300 flex-grow focus:outline-none"
                            />
                            {line.audioUrl && <div className="w-2 h-2 rounded-full bg-green-500 mt-2"></div>}
                        </div>
                    ))}
                    <button 
                        onClick={() => setDialogueLines([...dialogueLines, { id: crypto.randomUUID(), personaId: 'titan', text: '' }])}
                        className="w-full py-2 bg-gray-800 text-xs text-gray-400 rounded hover:bg-gray-700"
                    >
                        + Add Line
                    </button>
                 </div>
                 <div className="flex gap-2">
                     <button 
                        onClick={handleGenerateScene}
                        className="flex-1 py-3 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded"
                        disabled={loading}
                     >
                        {loading ? 'GENERATING...' : 'GENERATE SCENE'}
                     </button>
                     <button 
                        onClick={playScene}
                        disabled={playingScene}
                        className="flex-1 py-3 bg-green-600 hover:bg-green-500 text-white font-bold rounded"
                     >
                        {playingScene ? 'PLAYING...' : 'PLAY SCENE'}
                     </button>
                 </div>
                 </>
             )}
          </div>

          {/* VISUALIZER / PLAYER */}
          {mode === 'solo' && audioUrl && (
            <div className="bg-gray-800 border border-gray-700 rounded-xl p-4 animate-in fade-in slide-in-from-bottom-4 duration-500">
               <div className="flex items-center gap-4 mb-3">
                   <div className="bg-blue-500/20 p-3 rounded-full text-blue-400">
                      <Volume2 size={24} />
                   </div>
                   <div className="flex-grow">
                     <div className="flex justify-between items-center mb-1">
                        <div className="text-xs text-gray-400 uppercase tracking-widest">Playback</div>
                        {visemeData.length > 0 && <div className="text-xs text-green-400 font-mono">ANIMATION DATA: FOUND</div>}
                     </div>
                     <audio controls src={audioUrl} className="w-full h-8" autoPlay />
                   </div>
               </div>
               {/* Dummy Visualizer Bar */}
               <div className="h-2 w-full bg-gray-900 rounded-full overflow-hidden flex gap-0.5">
                  {Array.from({ length: 40 }).map((_, i) => (
                      <div key={i} className="flex-1 bg-blue-500/50 animate-pulse" style={{ animationDelay: `${i * 0.05}s`, opacity: Math.random() }}></div>
                  ))}
               </div>
            </div>
          )}

          {/* AUDIT LOG PREVIEW */}
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-2xl overflow-hidden flex-grow max-h-[300px] overflow-y-auto">
             <h2 className="text-sm font-semibold mb-4 flex items-center gap-2 text-gray-400 uppercase tracking-wider"><History size={16}/> Recent Audit Log</h2>
             <div className="space-y-2">
                {logs.map((log, i) => (
                  <div key={i} className="bg-gray-950/50 p-3 rounded border border-gray-800/50 text-xs font-mono grid grid-cols-[auto_1fr] gap-4">
                     <div className="text-gray-500">{new Date(log.timestamp).toLocaleTimeString()}</div>
                     <div>
                        <span className="text-purple-400">[{log.persona}]</span> <span className="text-gray-300">{log.originalText.substring(0, 40)}...</span>
                     </div>
                  </div>
                ))}
             </div>
          </div>

        </div>
      </main>
    </div>
  )
}

export default App
