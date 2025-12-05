"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.SSHManager = void 0;
const ssh2_1 = require("ssh2");
const ssh2_sftp_client_1 = __importDefault(require("ssh2-sftp-client"));
class SSHManager {
    constructor() {
        this.connections = new Map();
    }
    async connect(host, username, password, port = 22) {
        const connectionId = `${username}@${host}:${port}`;
        if (this.connections.has(connectionId)) {
            throw new Error(`Already connected to ${connectionId}`);
        }
        return new Promise((resolve, reject) => {
            const client = new ssh2_1.Client();
            client.on('ready', () => {
                const connection = {
                    id: connectionId,
                    config: { host, port, username, password },
                    client,
                    isConnected: true,
                    connectedAt: new Date()
                };
                this.connections.set(connectionId, connection);
                console.log(`SSH connection established: ${connectionId}`);
                resolve(connectionId);
            });
            client.on('error', (err) => {
                console.error(`SSH connection error for ${connectionId}:`, err);
                reject(err);
            });
            client.on('close', () => {
                const connection = this.connections.get(connectionId);
                if (connection) {
                    connection.isConnected = false;
                }
                console.log(`SSH connection closed: ${connectionId}`);
            });
            client.connect({
                host,
                port,
                username,
                password
            });
        });
    }
    async executeCommand(connectionId, command) {
        const connection = this.connections.get(connectionId);
        if (!connection || !connection.isConnected) {
            throw new Error(`Not connected to ${connectionId}`);
        }
        return new Promise((resolve, reject) => {
            connection.client.exec(command, (err, stream) => {
                if (err) {
                    reject(err);
                    return;
                }
                let output = '';
                let errorOutput = '';
                stream.on('close', (code) => {
                    if (code === 0) {
                        resolve(output);
                    }
                    else {
                        reject(new Error(`Command failed with code ${code}: ${errorOutput}`));
                    }
                });
                stream.on('data', (data) => {
                    output += data.toString();
                });
                stream.stderr.on('data', (data) => {
                    errorOutput += data.toString();
                });
            });
        });
    }
    async uploadFile(connectionId, localPath, remotePath) {
        const connection = this.connections.get(connectionId);
        if (!connection || !connection.isConnected) {
            throw new Error(`Not connected to ${connectionId}`);
        }
        if (!connection.sftp) {
            connection.sftp = new ssh2_sftp_client_1.default();
            await connection.sftp.connect({
                host: connection.config.host,
                port: connection.config.port,
                username: connection.config.username,
                password: connection.config.password
            });
        }
        await connection.sftp.put(localPath, remotePath);
    }
    async downloadFile(connectionId, remotePath, localPath) {
        const connection = this.connections.get(connectionId);
        if (!connection || !connection.isConnected) {
            throw new Error(`Not connected to ${connectionId}`);
        }
        if (!connection.sftp) {
            connection.sftp = new ssh2_sftp_client_1.default();
            await connection.sftp.connect({
                host: connection.config.host,
                port: connection.config.port,
                username: connection.config.username,
                password: connection.config.password
            });
        }
        await connection.sftp.get(remotePath, localPath);
    }
    listConnections() {
        return Array.from(this.connections.keys());
    }
    disconnect(connectionId) {
        const connection = this.connections.get(connectionId);
        if (connection) {
            if (connection.sftp) {
                connection.sftp.end();
            }
            connection.client.end();
            this.connections.delete(connectionId);
            console.log(`Disconnected from ${connectionId}`);
        }
    }
    disconnectAll() {
        for (const connectionId of this.connections.keys()) {
            this.disconnect(connectionId);
        }
    }
    isConnected(connectionId) {
        const connection = this.connections.get(connectionId);
        return connection ? connection.isConnected : false;
    }
}
exports.SSHManager = SSHManager;
//# sourceMappingURL=sshManager.js.map