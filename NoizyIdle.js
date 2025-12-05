/**
 * NoizyIdle - Subtle breathing and micro-movements
 */
export default function NoizyIdle(ref) {
  if (!ref.current) return;
  const t = performance.now() / 1500;
  ref.current.position.y = Math.sin(t) * 0.02;
  ref.current.rotation.y = Math.sin(t * 0.3) * 0.02;
}

