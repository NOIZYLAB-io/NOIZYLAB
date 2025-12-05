import { exec } from "child_process";

export function testMC96Jumbo(targetIP) {
  const cmd = process.platform === "darwin"
    ? `ping -D -s 9000 -c 4 ${targetIP}`
    : `ping -l 9000 -n 4 ${targetIP}`;

  return new Promise((resolve, reject) => {
    exec(cmd, (err, stdout) => {
      if (err) return reject("Jumbo frame test failed.");
      resolve(stdout.trim());
    });
  });
}
