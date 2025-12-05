export function sendInput(channel, type, payload) {
  if (!channel || channel.readyState !== "open") return;
  channel.send(JSON.stringify({ type, payload }));
}
