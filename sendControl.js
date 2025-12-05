export function sendControl(channel, type, payload) {
  if (channel.readyState !== "open") return;
  channel.send(JSON.stringify({ type, payload }));
}

