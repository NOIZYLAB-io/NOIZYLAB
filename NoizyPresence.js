/**
 * NoizyPresence - Moves avatar based on engagement
 */
export default function NoizyPresence(ref, distance) {
  if (!ref.current) return;

  const distanceMap = { close: -0.5, neutral: -1, far: -1.5 };
  const targetZ = distanceMap[distance] || -1;
  ref.current.position.z += (targetZ - ref.current.position.z) * 0.05;
}

