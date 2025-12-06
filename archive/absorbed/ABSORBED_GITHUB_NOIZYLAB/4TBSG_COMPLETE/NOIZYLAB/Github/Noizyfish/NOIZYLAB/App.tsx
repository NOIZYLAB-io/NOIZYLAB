import { useState, useEffect } from 'react';
import { Tile } from './components/Tile';
import { MetricsTile } from './components/MetricsTile';
import { useVoice } from '@mc96/accessibility/useVoice.ts';
import { useSwitchScan } from '@mc96/accessibility/useSwitchScan.ts';
import { parseCommand } from './commands';
import type { Metrics } from './components/MetricsTile';
import './styles.css';

export default function App(){
  const [metric, setMetric] = useState('—');
  const [status, setStatus] = useState('Ready');
  const [metrics, setMetrics] = useState<Metrics>({
    latency: 0,
    errorRate: 0,
    queueDepth: 0,
    circuitState: 'closed',
    throughput: 0
  });

  const voice = useVoice(({ text }) => {
    const cmd = parseCommand(text);
    if (cmd.action === 'run') runRitual(cmd.payload);
    if (cmd.action === 'audit') setStatus('Opening audit…');
  });
  const scan = useSwitchScan(el => (el as HTMLButtonElement).click(), 1200);

  // Fetch metrics periodically
  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch('/metrics');
        const data = await response.json();
        setMetrics(data);
      } catch (err) {
        console.error('Failed to fetch metrics:', err);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  async function runRitual(prompt: string){
    setStatus('Running…');
    try {
      // Local call placeholder — wire to your dev API
      const response = await fetch('/api/route', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, modality: 'text' })
      });
      
      const json = await response.json();
      setMetric(`${json.agent?.name || 'Unknown'} • ${json.result?.text || 'No result'}`);
      setStatus('Done');
    } catch (error) {
      setStatus(`Error: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  }

  const latencyStatus = metrics.latency > 1000 ? 'warning' : metrics.latency > 2000 ? 'error' : 'normal';
  const errorStatus = metrics.errorRate > 0.1 ? 'error' : metrics.errorRate > 0.05 ? 'warning' : 'normal';
  const circuitStatus = metrics.circuitState === 'open' ? 'error' : metrics.circuitState === 'half-open' ? 'warning' : 'normal';

  return (
    <main className="grid" role="main" aria-label="MC96 Cockpit">
      <Tile label="Run ritual" metric={metric} onActivate={() => runRitual('Hello world')} />
      
      <section className="metrics-section" aria-labelledby="metrics-heading">
        <h2 id="metrics-heading" className="sr-only">System Metrics</h2>
        <MetricsTile label="Latency" value={metrics.latency} unit="ms" status={latencyStatus} />
        <MetricsTile label="Error Rate" value={metrics.errorRate * 100} unit="%" status={errorStatus} />
        <MetricsTile label="Queue Depth" value={metrics.queueDepth} status="normal" />
        <MetricsTile label="Circuit State" value={metrics.circuitState} status={circuitStatus} />
        <MetricsTile label="Throughput" value={metrics.throughput} unit="req/s" status="normal" />
      </section>

      <aside aria-live="polite" className="status" role="status">{status}</aside>
      
      <div className="controls" role="toolbar" aria-label="Control Panel">
        <button 
          className="voice" 
          onClick={voice.toggle} 
          aria-label={voice.active ? 'Stop voice recognition' : 'Start voice recognition'}
          aria-pressed={voice.active}
        >
          {voice.active ? 'Listening…' : 'Start voice'}
        </button>
        <button 
          onClick={() => scan.start()} 
          aria-label="Start switch scanning"
        >
          Start scan
        </button>
        <button 
          onClick={() => scan.stop()} 
          aria-label="Stop switch scanning"
        >
          Stop scan
        </button>
      </div>
    </main>
  );
}
