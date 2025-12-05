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
exports.TestHistoryStorage = void 0;
const vscode = __importStar(require("vscode"));
const promises_1 = __importDefault(require("fs/promises"));
const path = __importStar(require("path"));
const proper_lockfile_1 = __importDefault(require("proper-lockfile"));
const uuid_1 = require("uuid");
const logger_1 = require("../../../util/logger");
const steps_1 = require("../../../@types/steps");
class TestHistoryStorage {
    constructor(context) {
        this.initialized = false;
        this.MAX_RETRIES = 3;
        this.LOCK_TIMEOUT = 5000;
        this.MAX_HISTORY_ITEMS = 50;
        const storagePath = context.globalStorageUri.fsPath;
        // this.historyDir = path.join(storagePath, 'test-history-dev');
        this.historyDir = path.join(storagePath, 'test-history-v2');
        this.indexFilePath = path.join(this.historyDir, 'index.json');
        logger_1.Logger.info(`Test history storage initialized with path: ${this.historyDir} and index: ${this.indexFilePath}`);
        this.lockOptions = {
            stale: this.LOCK_TIMEOUT,
            retries: {
                retries: this.MAX_RETRIES,
                factor: 2,
                minTimeout: 100,
                maxTimeout: 1000,
            },
            realpath: false, // Important for Windows compatibility
            onCompromised: (err) => {
                logger_1.Logger.error('Lock was compromised:', err);
                void vscode.window.showErrorMessage('(Keploy) Test history storage lock was compromised. Please try again.');
            }
        };
    }
    initializeStorage() {
        return __awaiter(this, void 0, void 0, function* () {
            if (this.initialized) {
                return;
            }
            try {
                yield this.ensureStorageDirectory();
                this.initialized = true;
                logger_1.Logger.info('Test history storage initialized successfully');
            }
            catch (error) {
                logger_1.Logger.error('Failed to initialize test history storage:', error);
                throw new Error(`Failed to initialize storage: ${error}`);
            }
        });
    }
    withLock(file_1, operation_1) {
        return __awaiter(this, arguments, void 0, function* (file, operation, retryCount = 0) {
            let release = null;
            try {
                release = yield proper_lockfile_1.default.lock(file, this.lockOptions);
                return yield operation();
            }
            catch (error) {
                const err = error;
                if (err.code === 'ELOCKED' && retryCount < this.MAX_RETRIES) {
                    yield new Promise(resolve => setTimeout(resolve, Math.random() * 1000));
                    return this.withLock(file, operation, retryCount + 1);
                }
                throw error;
            }
            finally {
                if (release) {
                    try {
                        yield release();
                    }
                    catch (error) {
                        logger_1.Logger.error('Failed to release lock:', error);
                    }
                }
            }
        });
    }
    atomicWrite(filePath, data) {
        return __awaiter(this, void 0, void 0, function* () {
            const tempPath = `${filePath}.tmp.${(0, uuid_1.v4)()}`;
            try {
                yield promises_1.default.writeFile(tempPath, data, 'utf8');
                yield promises_1.default.rename(tempPath, filePath);
            }
            catch (error) {
                try {
                    yield promises_1.default.unlink(tempPath).catch(() => { }); // Clean up temp file if exists
                }
                catch (unlinkError) {
                    if (unlinkError.code !== 'ENOENT') {
                        logger_1.Logger.error(`Failed to remove temp file ${tempPath}:`, unlinkError);
                    }
                }
                throw error;
            }
        });
    }
    ensureStorageDirectory() {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                // Logger.info('Ensuring storage directory exists:', this.historyDir);
                yield promises_1.default.mkdir(this.historyDir, { recursive: true });
                // Ensure index file exists
                try {
                    yield promises_1.default.access(this.indexFilePath);
                }
                catch (_a) {
                    yield this.atomicWrite(this.indexFilePath, '[]');
                }
            }
            catch (error) {
                logger_1.Logger.error('Failed to create storage directory:', error);
                throw error;
            }
        });
    }
    generateFilename(testResult) {
        const timestamp = new Date(testResult.timestamp).toISOString()
            .replace(/[:.]/g, '-');
        let fileName = 'unnamed-test';
        // find the file name from the steps.
        testResult.testGenInfo.steps.forEach((step) => {
            if (step.type !== steps_1.StepType.TestType) {
                return;
            }
            const testTypeStep = step.stepDetails;
            if (testTypeStep.fileName) {
                fileName = testTypeStep.fileName;
            }
        });
        const sanitizedFileName = fileName.replace(/[^a-zA-Z0-9-]/g, '-');
        return `${sanitizedFileName}-${timestamp}-${(0, uuid_1.v4)()}.json`;
    }
    cleanupOldFiles(index) {
        return __awaiter(this, void 0, void 0, function* () {
            if (index.length <= this.MAX_HISTORY_ITEMS) {
                return index;
            }
            const filesToRemove = index.slice(0, index.length - this.MAX_HISTORY_ITEMS);
            const remainingFiles = index.slice(index.length - this.MAX_HISTORY_ITEMS);
            yield Promise.all(filesToRemove.map((filename) => __awaiter(this, void 0, void 0, function* () {
                try {
                    yield promises_1.default.unlink(path.join(this.historyDir, filename));
                }
                catch (error) {
                    logger_1.Logger.error(`Failed to remove old file ${filename}:`, error);
                }
            })));
            return remainingFiles;
        });
    }
    updateIndex(filename) {
        return __awaiter(this, void 0, void 0, function* () {
            yield this.withLock(this.indexFilePath, () => __awaiter(this, void 0, void 0, function* () {
                const index = yield this.readIndex();
                index.push(filename);
                const cleanedIndex = yield this.cleanupOldFiles(index);
                yield this.atomicWrite(this.indexFilePath, JSON.stringify(cleanedIndex));
            }));
        });
    }
    readIndex() {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const data = yield promises_1.default.readFile(this.indexFilePath, 'utf8');
                return JSON.parse(data);
            }
            catch (error) {
                if (error.code === 'ENOENT') {
                    return [];
                }
                throw error;
            }
        });
    }
    saveTestResult(result) {
        return __awaiter(this, void 0, void 0, function* () {
            if (!this.initialized) {
                throw new Error('Storage not initialized');
            }
            // await this.ensureStorageDirectory();
            const filename = this.generateFilename(result);
            const filePath = path.join(this.historyDir, filename);
            try {
                yield this.atomicWrite(filePath, JSON.stringify(result, null, 2));
                yield this.updateIndex(filename);
            }
            catch (error) {
                logger_1.Logger.error('Failed to save test result:', error);
                // Try to clean up the test result file if index update failed
                try {
                    yield promises_1.default.unlink(filePath).catch(() => { });
                }
                finally {
                    throw error;
                }
            }
        });
    }
    getHistory() {
        return __awaiter(this, void 0, void 0, function* () {
            if (!this.initialized) {
                throw new Error('Storage not initialized');
            }
            return yield this.withLock(this.indexFilePath, () => __awaiter(this, void 0, void 0, function* () {
                try {
                    const index = yield this.readIndex();
                    if (index.length === 0) {
                        return [];
                    }
                    const results = [];
                    const validFiles = [];
                    for (const filename of index) {
                        try {
                            const filePath = path.join(this.historyDir, filename);
                            const data = yield promises_1.default.readFile(filePath, 'utf8');
                            results.push(JSON.parse(data));
                            validFiles.push(filename);
                        }
                        catch (error) {
                            logger_1.Logger.error(`Failed to read test result file: ${filename}`, error);
                        }
                    }
                    // If we found any invalid files, update the index to remove them
                    if (validFiles.length !== index.length) {
                        yield this.atomicWrite(this.indexFilePath, JSON.stringify(validFiles));
                    }
                    return results.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
                }
                catch (error) {
                    logger_1.Logger.error('Failed to get history:', error);
                    return [];
                }
            }));
        });
    }
    getFinalCoverage(steps) {
        var _a;
        const summary = (_a = steps.find((step) => step.type === steps_1.StepType.Summary)) === null || _a === void 0 ? void 0 : _a.stepDetails;
        return summary
            ? summary.isCoverageIncreased
                ? summary.coverageIncreased
                : summary.initialCoverage
            : 0;
    }
    getAddedTests(steps) {
        var _a;
        const summary = (_a = steps.find((step) => step.type === steps_1.StepType.Summary)) === null || _a === void 0 ? void 0 : _a.stepDetails;
        return (summary === null || summary === void 0 ? void 0 : summary.addedTests) || 0;
    }
    getSourceFile(steps) {
        let fileName = "unnamed-test";
        // find the file name from the steps.
        steps.forEach((step) => {
            if (step.type !== steps_1.StepType.TestType) {
                return;
            }
            const testTypeStep = step.stepDetails;
            if (testTypeStep.fileName) {
                fileName = testTypeStep.fileName;
            }
        });
        return fileName;
    }
    getTestFile(steps) {
        var _a;
        const summary = (_a = steps.find((step) => step.type === steps_1.StepType.RunSummary)) === null || _a === void 0 ? void 0 : _a.stepDetails;
        return (summary === null || summary === void 0 ? void 0 : summary.testFile) || "unknown-test-file";
    }
    getTestRunMetadata() {
        return __awaiter(this, void 0, void 0, function* () {
            const history = yield this.getHistory(); // history is TestResult[]
            return history.map((result) => {
                const { id, timestamp, testGenInfo } = result;
                if (!testGenInfo) {
                    throw new Error(`TestGenInfo not found in result with id: ${id}`);
                }
                const { steps, testStatus } = testGenInfo;
                return {
                    id,
                    timestamp,
                    finalCoverage: this.getFinalCoverage(steps),
                    testStatus,
                    addedTests: this.getAddedTests(steps),
                    sourceFile: this.getSourceFile(steps),
                    testFile: this.getTestFile(steps),
                };
            });
        });
    }
    // Utility method to repair storage if needed
    repairStorage() {
        return __awaiter(this, void 0, void 0, function* () {
            yield this.withLock(this.indexFilePath, () => __awaiter(this, void 0, void 0, function* () {
                yield this.ensureStorageDirectory();
                const index = yield this.readIndex();
                const validFiles = [];
                for (const filename of index) {
                    try {
                        yield promises_1.default.access(path.join(this.historyDir, filename));
                        validFiles.push(filename);
                    }
                    catch (_a) {
                        logger_1.Logger.warn(`Skipping missing file: ${filename}`);
                    }
                }
                yield this.atomicWrite(this.indexFilePath, JSON.stringify(validFiles));
            }));
        });
    }
}
exports.TestHistoryStorage = TestHistoryStorage;
//# sourceMappingURL=db.js.map