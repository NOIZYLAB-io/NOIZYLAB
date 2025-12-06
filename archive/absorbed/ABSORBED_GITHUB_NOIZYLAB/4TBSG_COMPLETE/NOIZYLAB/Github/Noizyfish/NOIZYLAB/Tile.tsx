export function Tile({ label, metric, onActivate }) {
  return (
    <button className="tile" aria-label={label} onClick={onActivate}>
      <div className="tile-label">{label}</div>
      <div className="tile-metric">{metric}</div>
    </button>
  );
}

