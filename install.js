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
exports.installKeploy = installKeploy;
exports.checkInstallationStatus = checkInstallationStatus;
const fs_1 = require("fs");
const crypto_1 = require("crypto");
const version_1 = require("./version"); // Using getKeployVersion for Linux/macOS
const progressTracker_1 = require("./progressTracker");
const path_1 = __importDefault(require("path"));
const https_1 = __importDefault(require("https"));
const fs = __importStar(require("fs"));
const fs_2 = require("fs");
const os_1 = require("os");
const vscode = __importStar(require("vscode"));
const agent_1 = require("../@types/agent");
const agent_2 = require("../@types/agent");
const logger_1 = require("./logger");
// Main function to install Keploy for any OS
function installKeploy() {
    return __awaiter(this, void 0, void 0, function* () {
        logger_1.Logger.info("Starting Keploy installation...");
        const status = yield checkInstallationStatus();
        if (status.isInstalled && !status.needsUpdate) {
            logger_1.Logger.info("Keploy is up to date, skipping installation");
            return;
        }
        const platform = process.platform;
        const architecture = getArchitecture();
        let currentKeployVersion;
        let keployFolderPath;
        let keployBinaryPath;
        let tempBinaryPath = '';
        const keployVersion = yield (0, version_1.getKeployVersion)();
        const baseDownloadUrl = `https://keploy-enterprise.s3.us-west-2.amazonaws.com/releases/${keployVersion}`;
        try {
            progressTracker_1.progressEmitter.fire({
                phase: agent_1.Status.INSTALLING,
                progress: 0,
                message: 'Getting the latest version...'
            });
            // Determine current version and installation path based on platform
            switch (platform) {
                case agent_2.OS.WINDOWS:
                    currentKeployVersion = (yield (0, version_1.getCurrentKeployWindowsVersion)()) || "";
                    const appDataPath = process.env.APPDATA || (0, os_1.tmpdir)(); // Use tmpdir() if APPDATA is undefined
                    keployFolderPath = path_1.default.join(appDataPath, ".keploy", "bin");
                    keployBinaryPath = path_1.default.join(keployFolderPath, "keploy.exe");
                    tempBinaryPath = path_1.default.join((0, os_1.tmpdir)(), "keploy_temp.exe");
                    break;
                case agent_2.OS.LINUX:
                case agent_2.OS.MAC:
                    currentKeployVersion = yield (0, version_1.getCurrentKeployVersion)();
                    const homePath = process.env.HOME || "~/"; // Use HOME or fallback to ~
                    keployFolderPath = path_1.default.join(homePath, ".keploy", "bin");
                    keployBinaryPath = path_1.default.join(keployFolderPath, "keploy");
                    tempBinaryPath = path_1.default.join((0, os_1.tmpdir)(), "keploy_temp");
                    break;
                default:
                    throw new Error("Unsupported OS.");
            }
            if (!(0, fs_1.existsSync)(keployFolderPath)) {
                logger_1.Logger.info(`Creating Keploy directory at ${keployFolderPath}`);
                (0, fs_1.mkdirSync)(keployFolderPath, { recursive: true });
            }
            logger_1.Logger.info(`Current Keploy version: ${currentKeployVersion}`);
            logger_1.Logger.info(`Latest Keploy version: ${keployVersion}`);
            if ((currentKeployVersion && currentKeployVersion !== "" && currentKeployVersion === keployVersion)) {
                logger_1.Logger.info("Keploy is already installed and up-to-date.");
                return;
            }
            logger_1.Logger.info(currentKeployVersion ? "Updating Keploy..." : "Installing Keploy for the first time...");
            // Remove the old temp file if it exists
            if ((0, fs_1.existsSync)(tempBinaryPath)) {
                fs.unlinkSync(tempBinaryPath);
            }
            let downloadUrl;
            let checksumsUrl;
            switch (platform) {
                case agent_2.OS.WINDOWS:
                    const architectureWindows = architecture === agent_2.ARCH.ARM64 ? agent_2.ARCH.ARM64 : agent_2.ARCH.AMD64;
                    downloadUrl = `${baseDownloadUrl}/enterprise_windows_${architectureWindows}.exe`;
                    checksumsUrl = `${baseDownloadUrl}/enterprise_${keployVersion}_checksums.txt`;
                    break;
                case agent_2.OS.LINUX:
                    downloadUrl = architecture === agent_2.ARCH.ARM64
                        ? `${baseDownloadUrl}/enterprise_linux_arm64`
                        : `${baseDownloadUrl}/enterprise_linux_amd64`;
                    checksumsUrl = `${baseDownloadUrl}/enterprise_${keployVersion}_checksums.txt`;
                    break;
                case agent_2.OS.MAC:
                    downloadUrl = `${baseDownloadUrl}/enterprise_darwin_all`;
                    checksumsUrl = `${baseDownloadUrl}/enterprise_darwin_${keployVersion}_checksums.txt`;
                    break;
                default:
                    throw new Error("Unsupported OS.");
            }
            logger_1.Logger.info(`Downloading Keploy for ${platform} (${architecture}) from ${downloadUrl}...`);
            yield downloadFile(downloadUrl, tempBinaryPath);
            if (!(0, fs_1.existsSync)(tempBinaryPath)) {
                throw new Error("Failed to download Keploy binary.");
            }
            // Validate download (example: check file size)
            const fileSize = fs.statSync(tempBinaryPath).size;
            if (fileSize < 1024) {
                throw new Error("Downloaded file appears to be incomplete.");
            }
            // Verify checksum
            logger_1.Logger.info("Verifying checksum...");
            yield verifyChecksum(tempBinaryPath, checksumsUrl, platform, architecture);
            // Replace the old binary with the new one
            if ((0, fs_1.existsSync)(keployBinaryPath)) {
                fs.unlinkSync(keployBinaryPath);
                logger_1.Logger.info("Removed old Keploy binary.");
            }
            fs.copyFileSync(tempBinaryPath, keployBinaryPath);
            fs.unlinkSync(tempBinaryPath);
            /*In linux "/home/" and  "/tmp/" are stored on different file systems(partitions of the disc)
            renameSync calls rename function during execution which is not permitted to rename parameters present in
            different file systems, hence replaced it with copyFileSync that works with different file systems
            and unlinkSync to remove the temporary path of keploy binary*/
            // fs.renameSync(tempBinaryPath, keployBinaryPath);
            logger_1.Logger.info(`Keploy successfully installed at ${keployBinaryPath}`);
            // Grant execute permissions on Linux and macOS
            if (platform === agent_2.OS.LINUX || platform === agent_2.OS.MAC) {
                try {
                    (0, fs_2.chmodSync)(keployBinaryPath, "755"); // Set permissions to rwxr-xr-x
                    logger_1.Logger.info(`Execution permissions granted for Keploy binary at ${keployBinaryPath} on ${platform}.`);
                }
                catch (err) {
                    logger_1.Logger.error(`Failed to set execution permissions: ${err.message}`);
                    throw new Error("Could not set executable permissions on Keploy binary.");
                }
            }
            progressTracker_1.progressEmitter.fire({
                phase: agent_1.Status.INSTALLING,
                progress: 100,
                message: 'Starting Keploy AI Agent...'
            });
            vscode.window.showInformationMessage("(Keploy)  AI Agent installed successfully.");
        }
        catch (err) {
            logger_1.Logger.error(`Installation failed: ${err.message}`);
            progressTracker_1.progressEmitter.fire({
                phase: agent_1.Status.ERROR,
                progress: 0,
                message: `Installation failed: ${err.message}`
            });
            if ((0, fs_1.existsSync)(tempBinaryPath)) {
                try {
                    fs.unlinkSync(tempBinaryPath);
                }
                catch (unlinkError) {
                    logger_1.Logger.error(`Failed to remove temp binary: ${unlinkError.message}`);
                }
            }
            throw err;
        }
    });
}
// Function to download a file from a URL
function downloadFile(url, destination) {
    return new Promise((resolve, reject) => {
        const file = fs.createWriteStream(destination);
        let downloadedBytes = 0;
        let totalBytes = 0;
        let lastEmittedProgress = 0;
        function handleRedirect(response) {
            if (response.statusCode === 302 || response.statusCode === 301) {
                const redirectUrl = response.headers.location;
                logger_1.Logger.info(`Redirecting to: ${redirectUrl}`);
                downloadFile(redirectUrl, destination).then(resolve).catch(reject);
            }
            else if (response.statusCode !== 200) {
                if ((0, fs_1.existsSync)(destination)) {
                    (0, fs_1.unlinkSync)(destination); // Cleanup on failure
                }
                return reject(new Error(`HTTP Status ${response.statusCode}`));
            }
            else {
                totalBytes = parseInt(response.headers['content-length'] || '0', 10);
                response.on('data', (chunk) => {
                    downloadedBytes += chunk.length;
                    if (totalBytes > 0) {
                        const currentProgress = Math.floor((downloadedBytes / totalBytes) * 100);
                        if (currentProgress > lastEmittedProgress) {
                            lastEmittedProgress = currentProgress;
                            progressTracker_1.progressEmitter.fire({
                                phase: agent_1.Status.DOWNLOADING,
                                progress: currentProgress,
                                message: `Downloading the latest version...`
                            });
                        }
                    }
                });
                response.pipe(file);
                file.on("finish", () => file.close(() => resolve()));
            }
        }
        https_1.default.get(url, handleRedirect).on("error", (err) => {
            if ((0, fs_1.existsSync)(destination)) {
                (0, fs_1.unlinkSync)(destination); // Cleanup on error
            }
            reject(err);
        });
    });
}
// Function to calculate the checksum of a file
function calculateChecksum(filePath) {
    const fileBuffer = (0, fs_1.readFileSync)(filePath);
    const hashSum = (0, crypto_1.createHash)("sha256");
    hashSum.update(fileBuffer);
    return hashSum.digest("hex");
}
// Function to verify checksum
function verifyChecksum(binaryPath, checksumsUrl, platform, architecture) {
    return __awaiter(this, void 0, void 0, function* () {
        var _a;
        const checksumFilePath = path_1.default.join((0, os_1.tmpdir)(), "keploy_checksums.txt");
        // Download checksum file
        yield downloadFile(checksumsUrl, checksumFilePath);
        if (!(0, fs_1.existsSync)(checksumFilePath)) {
            throw new Error("Checksum file could not be downloaded.");
        }
        // Determine the target file based on the platform and architecture
        let targetFile;
        switch (platform) {
            case agent_2.OS.WINDOWS:
                targetFile = `enterprise_windows_${architecture}.exe`;
                break;
            case agent_2.OS.MAC:
                targetFile = `enterprise_darwin_all`;
                break;
            case agent_2.OS.LINUX:
                targetFile = `enterprise_linux_${architecture}`;
                break;
            default:
                throw new Error("Unsupported platform for checksum verification.");
        }
        // Read and parse checksum file
        const checksumFileContent = (0, fs_1.readFileSync)(checksumFilePath, "utf-8");
        const checksumLines = checksumFileContent.split("\n").filter(line => line.trim().length > 0);
        const expectedChecksum = (_a = checksumLines.find(line => line.includes(targetFile))) === null || _a === void 0 ? void 0 : _a.split(" ")[0];
        if (!expectedChecksum) {
            throw new Error(`No checksum found for ${targetFile} in checksum file.`);
        }
        // Calculate the checksum of the downloaded binary
        const actualChecksum = calculateChecksum(binaryPath);
        if (expectedChecksum !== actualChecksum) {
            throw new Error(`Checksum verification failed. Expected: ${expectedChecksum}, Actual: ${actualChecksum}`);
        }
        logger_1.Logger.info(`Checksum verified successfully for ${binaryPath}`);
    });
}
// Function to detect architecture
function getArchitecture() {
    const arch = process.arch;
    return arch === agent_2.ARCH.ARM64 ? agent_2.ARCH.ARM64 : agent_2.ARCH.AMD64;
}
function checkInstallationStatus() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const latestVersion = yield (0, version_1.getKeployVersion)();
            let currentVersion;
            if (process.platform === agent_2.OS.WINDOWS) {
                currentVersion = (yield (0, version_1.getCurrentKeployWindowsVersion)()) || "";
            }
            else {
                currentVersion = yield (0, version_1.getCurrentKeployVersion)();
            }
            return {
                isInstalled: !!currentVersion,
                needsUpdate: currentVersion !== latestVersion,
                currentVersion,
                latestVersion
            };
        }
        catch (error) {
            logger_1.Logger.error("Error checking installation status:", error);
            return {
                isInstalled: false,
                needsUpdate: true
            };
        }
    });
}
//# sourceMappingURL=install.js.map