import { exec } from "child_process";

export function mountSMB(share, mountPoint, user = "", pass = "") {
  const cmd = process.platform === "darwin"
    ? `mkdir -p ${mountPoint} && mount_smbfs //${user}:${pass}@${share} ${mountPoint}`
    : `net use ${mountPoint} \\\\${share} /user:${user} ${pass}`;

  return new Promise((resolve, reject) => {
    exec(cmd, (err) => err ? reject(err) : resolve(true));
  });
}

export function unmountSMB(mountPoint) {
  const cmd = process.platform === "darwin"
    ? `umount ${mountPoint}`
    : `net use ${mountPoint} /delete`;

  return new Promise((resolve, reject) => {
    exec(cmd, (err) => err ? reject(err) : resolve(true));
  });
}
