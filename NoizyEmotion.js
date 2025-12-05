/**
 * NoizyEmotion - Maps emotional states to blendshapes
 */
export default function NoizyEmotion(ref, emotion) {
  if (!ref.current) return;
  const mesh = ref.current.children?.find(c => c.morphTargetInfluences);
  if (!mesh || !mesh.morphTargetInfluences) return;

  const blend = mesh.morphTargetInfluences;
  blend.fill(0);

  if (emotion === "calm") blend[0] = 0.2;
  else if (emotion === "alert") blend[1] = 0.4;
  else if (emotion === "focused") blend[2] = 0.3;
  else if (emotion === "happy") blend[0] = 0.5;
  else if (emotion === "stressed") blend[1] = 0.3;
}

