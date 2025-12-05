"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getOsUsername = exports.getOs = exports.getHostname = exports.isMac = exports.isWindows = exports.isLinux = void 0;
const ExecManager_1 = require("./ExecManager");
const os = require("os");
function isLinux() {
    return isWindows() || isMac() ? false : true;
}
exports.isLinux = isLinux;
// process.platform return the following...
//   -> 'darwin', 'freebsd', 'linux', 'sunos' or 'win32'
function isWindows() {
    return process.platform.indexOf("win32") !== -1;
}
exports.isWindows = isWindows;
function isMac() {
    return process.platform.indexOf("darwin") !== -1;
}
exports.isMac = isMac;
function getHostname() {
    return __awaiter(this, void 0, void 0, function* () {
        const hostname = (0, ExecManager_1.execCmd)("hostname");
        return hostname;
    });
}
exports.getHostname = getHostname;
function getOs() {
    const parts = [];
    const osType = os.type();
    if (osType) {
        parts.push(osType);
    }
    const osRelease = os.release();
    if (osRelease) {
        parts.push(osRelease);
    }
    const platform = os.platform();
    if (platform) {
        parts.push(platform);
    }
    if (parts.length > 0) {
        return parts.join("_");
    }
    return "";
}
exports.getOs = getOs;
function getOsUsername() {
    return __awaiter(this, void 0, void 0, function* () {
        let username = os.userInfo().username;
        if (!username || username.trim() === "") {
            username = (0, ExecManager_1.execCmd)("whoami");
        }
        return username;
    });
}
exports.getOsUsername = getOsUsername;
//# sourceMappingURL=DeviceManager.js.map