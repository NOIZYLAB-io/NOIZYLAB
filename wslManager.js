"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WSLManager = void 0;
const child_process_1 = require("child_process");
const util_1 = require("util");
const execAsync = (0, util_1.promisify)(child_process_1.exec);
class WSLManager {
    constructor() {
        this.activeConnections = new Set();
    }
    async listDistributions() {
        try {
            const { stdout } = await execAsync('wsl --list --verbose');
            const cleanOutput = stdout.replace(/\0/g, '').replace(/\r/g, '');
            const lines = cleanOutput.split('\n').filter(line => line.trim());
            const distributions = [];
            for (let i = 1; i < lines.length; i++) {
                const line = lines[i].trim();
                if (line) {
                    const cleanLine = line.replace('*', '').trim();
                    const parts = cleanLine.split(/\s+/).filter(part => part.length > 0);
                    if (parts.length >= 1) {
                        distributions.push(parts[0].trim());
                    }
                }
            }
            return distributions;
        }
        catch (error) {
            throw new Error(`Failed to list WSL distributions: ${error}`);
        }
    }
    async connect(distribution) {
        const connectionId = `wsl-${distribution}`;
        this.activeConnections.add(connectionId);
        return connectionId;
    }
    async executeCommand(command, distribution) {
        const bashCommand = `bash -c "${command.replace(/"/g, '\\"')}"`;
        const wslCommand = distribution ? `wsl -d ${distribution} ${bashCommand}` : `wsl ${bashCommand}`;
        try {
            const { stdout, stderr } = await execAsync(wslCommand);
            if (stderr) {
                console.warn('WSL command stderr:', stderr);
            }
            return stdout;
        }
        catch (error) {
            throw new Error(`WSL command failed: ${error}`);
        }
    }
    async copyFile(sourcePath, destPath, direction) {
        let command;
        if (direction === 'to_wsl') {
            const wslSourcePath = this.windowsToWSLPath(sourcePath);
            command = `cp "${wslSourcePath}" "${destPath}"`;
        }
        else {
            const wslDestPath = this.windowsToWSLPath(destPath);
            command = `cp "${sourcePath}" "${wslDestPath}"`;
        }
        await this.executeCommand(command);
    }
    async convertPath(path, toWSL = true) {
        if (toWSL) {
            return this.windowsToWSLPath(path);
        }
        else {
            return this.wslToWindowsPath(path);
        }
    }
    windowsToWSLPath(windowsPath) {
        const normalized = windowsPath.replace(/\\/g, '/');
        if (normalized.match(/^[A-Za-z]:/)) {
            const drive = normalized.charAt(0).toLowerCase();
            return `/mnt/${drive}${normalized.substring(2)}`;
        }
        return normalized;
    }
    wslToWindowsPath(wslPath) {
        if (wslPath.startsWith('/mnt/')) {
            const parts = wslPath.split('/');
            if (parts.length >= 3) {
                const drive = parts[2].toUpperCase();
                const restPath = parts.slice(3).join('\\');
                return `${drive}:\\${restPath}`;
            }
        }
        return wslPath;
    }
    listConnections() {
        return Array.from(this.activeConnections);
    }
    disconnect(connectionId) {
        this.activeConnections.delete(connectionId);
    }
    disconnectAll() {
        this.activeConnections.clear();
    }
}
exports.WSLManager = WSLManager;
//# sourceMappingURL=wslManager.js.map