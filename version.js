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
exports.getKeployVersion = getKeployVersion;
exports.getCurrentKeployVersion = getCurrentKeployVersion;
exports.getCurrentKeployWindowsVersion = getCurrentKeployWindowsVersion;
const execShell_1 = require("./execShell");
const path = __importStar(require("path"));
const fs = __importStar(require("fs"));
const child_process_1 = require("child_process");
const util_1 = require("util");
const execAsync = (0, util_1.promisify)(child_process_1.exec);
const os_1 = require("os");
const logger_1 = require("./logger");
function getKeployVersion() {
    return __awaiter(this, void 0, void 0, function* () {
        const packagePath = path.resolve(__dirname, '../../package.json');
        const packageContent = fs.readFileSync(packagePath, 'utf-8');
        const packageData = JSON.parse(packageContent);
        const keployVersionJsonPath = path.resolve(__dirname, '../../keploy-version.json');
        const keployVersionJsonContent = fs.readFileSync(keployVersionJsonPath, 'utf-8');
        const keployVersionJson = JSON.parse(keployVersionJsonContent);
        const keployVersion = keployVersionJson[`${packageData.version}`];
        logger_1.Logger.info('Package json Keploy version:', keployVersion);
        return keployVersion;
    });
}
function getCurrentKeployVersion() {
    return __awaiter(this, void 0, void 0, function* () {
        let output = '';
        try {
            output = yield (0, execShell_1.execShell)('~/.keploy/bin/keploy --version');
        }
        catch (error) {
            logger_1.Logger.info("Error Fetching keploy version " + error);
            return '';
        }
        logger_1.Logger.info('~/.keploy/bin/keploy --version output:', output);
        const keployIndex = output.indexOf('Keploy');
        logger_1.Logger.info('keployIndex:', keployIndex);
        let keployVersion = '';
        if (keployIndex !== -1) {
            keployVersion = output.substring(keployIndex + 'Keploy'.length).trim();
        }
        logger_1.Logger.info('Current installed Keploy version:', keployVersion);
        return keployVersion;
    });
}
function getCurrentKeployWindowsVersion() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const { stdout } = yield execAsync('keploy.exe --version', {
                cwd: path.join(process.env.APPDATA || (0, os_1.tmpdir)(), ".keploy", "bin"),
            });
            const match = stdout.match(/Keploy\s*([\d.]+(?:-[\w\d]+)?)\s*/i);
            return match ? match[1] : null;
        }
        catch (_a) {
            return null; // If the command fails, Keploy is not installed
        }
    });
}
//# sourceMappingURL=version.js.map