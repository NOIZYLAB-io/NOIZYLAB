"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.execShell = void 0;
const child_process_1 = require("child_process");
const os = __importStar(require("os"));
const agent_1 = require("../@types/agent");
const logger_1 = require("./logger");
const execShell = (cmd) => {
    return new Promise((resolve, reject) => {
        let commandToExecute;
        if (os.platform() === agent_1.OS.WINDOWS) {
            // Execute the command in the WSL environment if on Windows
            commandToExecute = `wsl ${cmd}`;
        }
        else {
            // Execute the command in the default shell if on other platforms
            commandToExecute = cmd;
        }
        logger_1.Logger.info(`Executing command: ${commandToExecute}`);
        (0, child_process_1.exec)(commandToExecute, { cwd: "/tmp" }, (err, stdout, stderr) => {
            if (err) {
                reject(err.message);
                return;
            }
            if (stderr) {
                logger_1.Logger.info(stderr); // Log stderr but don't reject the promise
            }
            resolve(stdout);
        });
    });
};
exports.execShell = execShell;
//# sourceMappingURL=execShell.js.map