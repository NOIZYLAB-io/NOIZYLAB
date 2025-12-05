export function attachControl(pc, onMessage) {
  const channel = pc.createDataChannel("control");
  channel.onmessage = (event) => onMessage(JSON.parse(event.data));
  return channel;
}
