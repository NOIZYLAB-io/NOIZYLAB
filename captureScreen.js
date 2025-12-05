export async function captureScreen(pc) {
  const stream = await navigator.mediaDevices.getDisplayMedia({
    video: { frameRate: 20, width: 1920, height: 1080 },
    audio: false
  });

  stream.getTracks().forEach((t) => pc.addTrack(t, stream));
  return stream;
}

