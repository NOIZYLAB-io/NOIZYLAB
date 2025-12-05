/**
 * NoizyLipSync - Voice-reactive mouth animation
 */
export default function NoizyLipSync(ref, activity) {
  if (!ref.current) return;
  const mesh = ref.current.children?.find(c => c.morphTargetInfluences);
  if (!mesh || !mesh.morphTargetInfluences) return;

  const mouthIndex = 3;
  if (mesh.morphTargetInfluences.length > mouthIndex) {
    mesh.morphTargetInfluences[mouthIndex] = activity ? Math.random() * 0.4 : 0;
  }
}

