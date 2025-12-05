export function bindKeyboard(channel) {
  window.addEventListener("keydown", (e) => {
    if (channel.readyState !== "open") return;

    channel.send(JSON.stringify({
      type: "keyboard",
      payload: { key: e.key }
    }));
  });
}

