import { exec } from "child_process";

export function runSSH(host, user, command) {
  return new Promise((resolve, reject) => {
    exec(`ssh ${user}@${host} "${command}"`, (err, stdout, stderr) => {
      if (err) return reject(stderr);
      resolve(stdout.trim());
    });
  });
}

export function sftpDownload(host, user, remotePath, localPath) {
  return new Promise((resolve, reject) => {
    exec(`scp ${user}@${host}:${remotePath} ${localPath}`, (err) => {
      if (err) return reject(err);
      resolve(true);
    });
  });
}

export function sftpUpload(host, user, localPath, remotePath) {
  return new Promise((resolve, reject) => {
    exec(`scp ${localPath} ${user}@${host}:${remotePath}`, (err) => {
      if (err) return reject(err);
      resolve(true);
    });
  });
}
