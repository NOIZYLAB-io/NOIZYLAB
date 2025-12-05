import { exec } from "child_process";

export function startVPN(configPath) {
  return new Promise((resolve, reject) => {
    exec(`wg-quick up ${configPath}`, (err) =>
      err ? reject(err) : resolve("VPN connected")
    );
  });
}

export function stopVPN(configPath) {
  return new Promise((resolve, reject) => {
    exec(`wg-quick down ${configPath}`, (err) =>
      err ? reject(err) : resolve("VPN disconnected")
    );
  });
}

export function startOpenVPN(configPath) {
  return new Promise((resolve, reject) => {
    exec(`openvpn --config "${configPath}"`, (err) =>
      err ? reject(err) : resolve("OpenVPN started")
    );
  });
}
