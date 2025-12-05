export function createControlChannel(pc, onInput) {
  const channel = pc.createDataChannel("control");

  channel.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    onInput(data);
  };

  return channel;
}

