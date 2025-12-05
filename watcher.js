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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.FileWatcher = void 0;
const vscode = __importStar(require("vscode"));
const fs = __importStar(require("fs"));
const chokidar_1 = __importDefault(require("chokidar"));
const util_1 = require("./util");
const logger_1 = require("./logger");
class FileWatcher {
    constructor(disposable, keploy) {
        this.disposable = disposable;
        this.keploy = keploy;
    }
    /**
     * Start watching the extensions.json file for changes.
     */
    startWatching() {
        const extensionsJsonPath = (0, util_1.getExtensionJsonPath)();
        if (extensionsJsonPath === "") {
            return;
        }
        logger_1.Logger.info("extensions.json Path : " + extensionsJsonPath);
        if (!fs.existsSync(extensionsJsonPath)) {
            logger_1.Logger.error(`❌ extensions.json file does not exist: ${extensionsJsonPath}`);
            return;
        }
        logger_1.Logger.info(`👀 Watching extensions.json file: ${extensionsJsonPath}`);
        // Initialize the file watcher
        this.watcher = chokidar_1.default.watch(extensionsJsonPath, {
            persistent: true,
            ignoreInitial: false,
        });
        this.watcher.on("change", () => this.handleFileChange(extensionsJsonPath));
        this.watcher.on("add", () => this.handleFileChange(extensionsJsonPath));
        this.watcher.on("unlink", () => logger_1.Logger.info(`⚠️ extensions.json file was removed: ${extensionsJsonPath}`));
        this.disposable.push({ dispose: () => this.dispose() });
    }
    /**
     * Handle changes in the extensions.json file.
     */
    handleFileChange(extensionsJsonPath) {
        fs.readFile(extensionsJsonPath, "utf8", (err, data) => __awaiter(this, void 0, void 0, function* () {
            if (err) {
                logger_1.Logger.error("❌ Error reading extensions.json:", err);
                return;
            }
            try {
                const extensionsJson = JSON.parse(data);
                const version = (0, util_1.findExtensionVersion)(extensionsJson);
                if (!version) {
                    logger_1.Logger.info("🛑 Keploy extension uninstalled.");
                    this.onExtensionDeletion();
                    return;
                }
                const storedVersion = this.keploy.GetExtensionVersion();
                if (storedVersion !== "" && version !== "" && storedVersion !== version) {
                    logger_1.Logger.info(`🔄 Version changed from ${storedVersion} to ${version}`);
                    this.keploy.SetExtensionVersion(version);
                    this.onExtensionUpdate();
                }
            }
            catch (error) {
                logger_1.Logger.error("❌ Error parsing extensions.json:", error);
            }
        }));
    }
    /**
     * Cleanup the file watcher.
     */
    dispose() {
        if (this.watcher) {
            this.watcher.close();
            logger_1.Logger.info("🛑 Stopped watching extensions.json.");
        }
    }
    /** Hook: Called when the Keploy extension is uninstalled */
    onExtensionDeletion() {
        logger_1.Logger.info("⚠️ Keploy extension deleted. Performing cleanup actions...");
        this.keploy.ShutDown();
        this.keploy.CleanUpState(); // clean up the global and workspace states
    }
    /** Hook: Called when the Keploy extension is updated */
    onExtensionUpdate() {
        logger_1.Logger.info("🔄 Keploy extension updated.");
        let countdown = 3;
        const interval = setInterval(() => {
            vscode.window.showInformationMessage(`(Keploy) extension is updated, restarting in ${countdown} seconds...`);
            logger_1.Logger.info(`Keploy extension is updated, restarting in ${countdown} seconds...`);
            countdown--;
            if (countdown === 0) {
                clearInterval(interval);
                // wait for 500ms before reloading the window
                setTimeout(() => {
                }, 1000);
                vscode.commands.executeCommand("workbench.action.reloadWindow");
            }
        }, 1000);
    }
}
exports.FileWatcher = FileWatcher;
//# sourceMappingURL=watcher.js.map