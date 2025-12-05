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
exports.invokePowerShellCommand = void 0;
const alFileHelper_1 = require("./alFileHelper");
const child_process_1 = require("child_process");
const vscode = require("vscode");
function invokePowerShellCommand(command, cwd) {
    var _a;
    if (cwd === void 0) { cwd = (_a = (0, alFileHelper_1.getTestFolderPath)()) !== null && _a !== void 0 ? _a : ''; }
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            //why this hideous looking code? I've had trouble with the node-powershell module, deep in the dependency tree something doesn't compile and causes the extenion to fail to load
            const ps = (0, child_process_1.spawn)('pwsh', ['-Command', command]);
            ps.stdout.on('data', (data) => {
                resolve(data.toString().trim('\n'));
                return;
            });
            ps.stderr.on('data', (data) => {
                vscode.window.showErrorMessage(`Error calling PowerShell: ${data.toString()}`);
                return;
            });
        }));
    });
}
exports.invokePowerShellCommand = invokePowerShellCommand;
//# sourceMappingURL=powershell.js.map