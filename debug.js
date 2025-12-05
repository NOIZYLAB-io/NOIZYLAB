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
exports.readyToDebug = void 0;
const fs_1 = require("fs");
const path_1 = require("path");
const config_1 = require("./config");
const extension_1 = require("./extension");
const file_1 = require("./file");
function readyToDebug() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const terminal = (0, extension_1.getALTestRunnerTerminal)((0, extension_1.getTerminalName)());
            const path = getDebugReadyPath();
            if ((0, fs_1.existsSync)(path)) {
                (0, fs_1.unlinkSync)(path);
            }
            terminal.sendText(`Get-ReadyToDebug -Path '${path}' -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`);
            terminal.show();
            const ready = yield (0, file_1.awaitFileExistence)(path, 30000);
            resolve(ready);
        }));
    });
}
exports.readyToDebug = readyToDebug;
function getDebugReadyPath() {
    return (0, path_1.join)((0, config_1.getALTestRunnerPath)(), "debug.txt");
}
//# sourceMappingURL=debug.js.map