export function parseCommand(text) {
  const s = text.toLowerCase();
  if (s.includes('run ritual')) return { action: 'run', payload: s.replace('run ritual','').trim() || 'default' };
  if (s.includes('open audit')) return { action: 'audit' };
  return { action: 'none' };
}

