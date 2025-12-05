export async function startScreenCapture(pc) {
  const stream = await navigator.mediaDevices.getDisplayMedia({
    video: { frameRate: 20 },
    audio: false,
  });
  stream.getTracks().forEach((t) => pc.addTrack(t, stream));
  return stream;
}
