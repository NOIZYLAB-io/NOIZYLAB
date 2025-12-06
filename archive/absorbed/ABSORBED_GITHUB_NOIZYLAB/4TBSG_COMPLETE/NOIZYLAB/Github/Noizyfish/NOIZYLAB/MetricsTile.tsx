export interface Metrics {
  latency: number;
  errorRate: number;
  queueDepth: number;
  circuitState: string;
  throughput: number;
}

export function MetricsTile({ label, value, unit = '', status = 'normal' }: {
  label: string;
  value: number | string;
  unit?: string;
  status?: 'normal' | 'warning' | 'error';
}) {
  const statusClass = status === 'error' ? 'error' : status === 'warning' ? 'warning' : '';
  
  return (
    <div className={`metrics-tile ${statusClass}`} role="status" aria-live="polite">
      <div className="metrics-label">{label}</div>
      <div className="metrics-value">
        {typeof value === 'number' ? value.toFixed(2) : value}
        {unit && <span className="metrics-unit">{unit}</span>}
      </div>
    </div>
  );
}

