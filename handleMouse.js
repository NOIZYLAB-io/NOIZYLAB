export function bindMouseToChannel(channel, element) {
  element.addEventListener("mousemove", (e) => {
    send("move", { x: e.clientX, y: e.clientY });
  });

  element.addEventListener("click", () => {
    send("click", {});
  });

  function send(type, payload) {
    if (channel.readyState !== "open") return;
    channel.send(JSON.stringify({ type, payload }));
  }
}

