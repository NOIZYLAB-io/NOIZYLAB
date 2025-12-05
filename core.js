"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MochaAdapterCore = void 0;
const tslib_1 = require("tslib");
const path = tslib_1.__importStar(require("path"));
const child_process_1 = require("child_process");
const util = tslib_1.__importStar(require("util"));
const vscode_test_adapter_remoting_util_1 = require("vscode-test-adapter-remoting-util");
const util_1 = require("./util");
class MochaAdapterCore {
    constructor(outputChannel, log) {
        this.outputChannel = outputChannel;
        this.log = log;
        this.nodesById = new Map();
        this.skipNextLoadRequest = false;
        this.workerScript = require.resolve('../out/worker/bundle.js');
        this.nextTestRunId = 0;
    }
    load(changedFiles_1) {
        return tslib_1.__awaiter(this, arguments, void 0, function* (changedFiles, reloadConfig = true) {
            if (this.skipNextLoadRequest) {
                if (this.log.enabled)
                    this.log.info(`Skipping the initial load request for ${this.workspaceFolderPath}`);
                this.skipNextLoadRequest = false;
                this.testsEmitter.fire({ type: 'started' });
                this.testsEmitter.fire({ type: 'finished' });
                return;
            }
            try {
                if (this.log.enabled)
                    this.log.info(`Loading test files of ${this.workspaceFolderPath}`);
                this.testsEmitter.fire({ type: 'started' });
                if (reloadConfig) {
                    this.configReader.reloadConfig();
                }
                const config = yield this.configReader.currentConfig;
                if (!config) {
                    this.log.info('Adapter disabled for this folder, loading cancelled');
                    this.nodesById.clear();
                    this.testsEmitter.fire({ type: 'finished' });
                    return;
                }
                let testsLoaded = false;
                yield new Promise((resolve) => tslib_1.__awaiter(this, void 0, void 0, function* () {
                    const childProcScript = config.launcherScript ?
                        path.resolve(this.workspaceFolderPath, config.launcherScript) :
                        this.workerScript;
                    const childProc = this.launchWorkerProcess(config, childProcScript, config.nodeArgv);
                    if (this.log.enabled) {
                        childProc.stdout.on('data', data => this.log.info(`Worker (stdout): ${data.toString()}`));
                        childProc.stderr.on('data', data => this.log.error(`Worker (stderr): ${data.toString()}`));
                    }
                    const args = {
                        action: 'loadTests',
                        cwd: config.cwd,
                        testFiles: config.extraFiles.concat(config.testFiles),
                        env: config.env,
                        mochaPath: config.mochaPath,
                        mochaOpts: config.mochaOpts,
                        monkeyPatch: config.monkeyPatch,
                        multiFileSuites: config.multiFileSuites,
                        logEnabled: this.log.enabled,
                        workerScript: this.workerScript,
                        esmLoader: config.esmLoader
                    };
                    const handler = (info) => {
                        if (typeof info === 'string') {
                            if (this.log.enabled)
                                this.log.info(`Worker: ${info}`);
                        }
                        else {
                            this.nodesById.clear();
                            if (info) {
                                if (info.type === 'suite') {
                                    this.log.info('Received tests from worker');
                                    info.id = `${this.workspaceFolderPath}: Mocha`;
                                    info.label = 'Mocha';
                                    this.collectNodesById(info);
                                    this.testsEmitter.fire({ type: 'finished', suite: info });
                                    if (changedFiles) {
                                        const changedTests = (0, util_1.findTests)(info, { tests: info => ((info.file !== undefined) && (changedFiles.indexOf(info.file) >= 0))
                                        });
                                        this.retireEmitter.fire({ tests: [...changedTests].map(info => info.id) });
                                    }
                                    else {
                                        this.retireEmitter.fire({});
                                    }
                                }
                                else {
                                    this.log.info('Received error from worker');
                                    this.testsEmitter.fire({ type: 'finished', errorMessage: info.errorMessage });
                                }
                            }
                            else {
                                this.log.info('Worker found no tests');
                                this.testsEmitter.fire({ type: 'finished' });
                            }
                            testsLoaded = true;
                            if (config.mochaOpts.exit && !config.launcherScript) {
                                childProc.kill();
                            }
                            resolve();
                        }
                    };
                    try {
                        yield this.connectToWorkerProcess(config, childProc, args, handler);
                    }
                    catch (err) {
                        this.log.error(`Couldn't establish IPC: ${util.inspect(err)}`);
                        if (!testsLoaded) {
                            this.testsEmitter.fire({ type: 'finished', errorMessage: `Couldn't establish IPC:\n${err.stack}` });
                            testsLoaded = true;
                            resolve();
                        }
                    }
                    childProc.on('exit', (code, signal) => {
                        if (this.log.enabled)
                            this.log.info(`Worker finished with code ${code} and signal ${signal}`);
                        if (!testsLoaded) {
                            if (code || signal) {
                                this.testsEmitter.fire({ type: 'finished', errorMessage: `The worker process finished with code ${code} and signal ${signal}` });
                            }
                            else {
                                this.testsEmitter.fire({ type: 'finished', suite: undefined });
                            }
                            testsLoaded = true;
                            resolve();
                        }
                    });
                    childProc.on('error', err => {
                        if (this.log.enabled)
                            this.log.error(`Error from child process: ${util.inspect(err)}`);
                        if (!testsLoaded) {
                            this.testsEmitter.fire({ type: 'finished', errorMessage: util.inspect(err) });
                            testsLoaded = true;
                            resolve();
                        }
                    });
                }));
            }
            catch (err) {
                if (this.log.enabled)
                    this.log.error(`Error while loading tests: ${util.inspect(err)}`);
                this.testsEmitter.fire({ type: 'finished', errorMessage: util.inspect(err) });
            }
        });
    }
    run(testsToRun_1) {
        return tslib_1.__awaiter(this, arguments, void 0, function* (testsToRun, debug = false) {
            const testRunId = String(this.nextTestRunId++);
            try {
                if (this.log.enabled)
                    this.log.info(`Running test(s) ${JSON.stringify(testsToRun)} of ${this.workspaceFolderPath}`);
                const config = yield this.configReader.currentConfig;
                if (!config) {
                    this.log.info('Adapter disabled for this folder, running cancelled');
                    return;
                }
                this.testStatesEmitter.fire({ type: 'started', tests: testsToRun, testRunId });
                const testInfos = [];
                for (const suiteOrTestId of testsToRun) {
                    const node = this.nodesById.get(suiteOrTestId);
                    if (node) {
                        this.collectTests(node, testInfos);
                    }
                }
                if (testInfos.length === 0) {
                    this.testStatesEmitter.fire({ type: 'finished', testRunId });
                    return;
                }
                const tests = testInfos.map(test => {
                    const separatorIndex = test.id.indexOf(': ');
                    if (separatorIndex >= 0) {
                        return test.id.substr(separatorIndex + 2);
                    }
                    else {
                        return test.id;
                    }
                });
                let _testFiles = undefined;
                if (config.pruneFiles) {
                    const testFileSet = new Set(testInfos.map(test => test.file).filter(file => (file !== undefined)));
                    if (testFileSet.size > 0) {
                        _testFiles = [...testFileSet];
                        if (this.log.enabled)
                            this.log.debug(`Using test files ${JSON.stringify(_testFiles)}`);
                    }
                }
                if (_testFiles === undefined) {
                    _testFiles = config.testFiles;
                }
                const testFiles = config.extraFiles.concat(_testFiles);
                let childProcessFinished = false;
                yield new Promise((resolve) => tslib_1.__awaiter(this, void 0, void 0, function* () {
                    let runningTest = undefined;
                    const childProcScript = config.launcherScript ?
                        path.resolve(this.workspaceFolderPath, config.launcherScript) :
                        this.workerScript;
                    const execArgv = [...config.nodeArgv];
                    if (debug && !config.launcherScript) {
                        config.launcherScript
                            ? config.env.MOCHA_WORKER_DEBUG = "true"
                            : execArgv.push(`--inspect-brk=${config.debuggerPort}`);
                    }
                    this.runningTestProcess = this.launchWorkerProcess(config, childProcScript, execArgv);
                    const processOutput = (data) => {
                        this.outputChannel.append(data.toString());
                        if (runningTest) {
                            this.testStatesEmitter.fire({
                                type: 'test',
                                state: 'running',
                                test: runningTest,
                                message: data.toString(),
                                testRunId
                            });
                        }
                    };
                    this.runningTestProcess.stdout.on('data', processOutput);
                    this.runningTestProcess.stderr.on('data', processOutput);
                    const args = {
                        action: 'runTests',
                        cwd: config.cwd,
                        testFiles,
                        tests,
                        env: config.env,
                        mochaPath: config.mochaPath,
                        mochaOpts: config.mochaOpts,
                        multiFileSuites: config.multiFileSuites,
                        logEnabled: this.log.enabled,
                        workerScript: this.workerScript,
                        debuggerPort: debug ? config.debuggerPort : undefined,
                        esmLoader: config.esmLoader
                    };
                    const handler = (message) => {
                        if (typeof message === 'string') {
                            if (this.log.enabled)
                                this.log.info(`Worker: ${message}`);
                        }
                        else {
                            if (this.log.enabled)
                                this.log.info(`Received ${JSON.stringify(message)}`);
                            if (message.type !== 'finished') {
                                this.testStatesEmitter.fire(Object.assign(Object.assign({}, message), { testRunId }));
                                if (message.type === 'test') {
                                    if (message.state === 'running') {
                                        runningTest = (typeof message.test === 'string') ? message.test : message.test.id;
                                    }
                                    else {
                                        runningTest = undefined;
                                    }
                                }
                            }
                            else if (config.mochaOpts.exit && !config.launcherScript && this.runningTestProcess) {
                                this.runningTestProcess.kill();
                            }
                        }
                    };
                    try {
                        yield this.connectToWorkerProcess(config, this.runningTestProcess, args, handler);
                    }
                    catch (err) {
                        this.log.error(`Couldn't establish IPC: ${util.inspect(err)}`);
                        if (!childProcessFinished) {
                            childProcessFinished = true;
                            this.testsEmitter.fire({ type: 'finished', errorMessage: `Couldn't establish IPC:\n${err.stack}` });
                            resolve();
                        }
                    }
                    this.runningTestProcess.on('exit', () => {
                        this.log.info('Worker finished');
                        runningTest = undefined;
                        this.runningTestProcess = undefined;
                        if (!childProcessFinished) {
                            childProcessFinished = true;
                            this.testStatesEmitter.fire({ type: 'finished', testRunId });
                            resolve();
                        }
                    });
                    this.runningTestProcess.on('error', err => {
                        if (this.log.enabled)
                            this.log.error(`Error from child process: ${util.inspect(err)}`);
                        runningTest = undefined;
                        this.runningTestProcess = undefined;
                        if (!childProcessFinished) {
                            childProcessFinished = true;
                            this.testStatesEmitter.fire({ type: 'finished', testRunId });
                            resolve();
                        }
                    });
                }));
            }
            catch (err) {
                if (this.log.enabled)
                    this.log.error(`Error while running tests: ${util.inspect(err)}`);
                this.testStatesEmitter.fire({ type: 'finished', testRunId });
            }
        });
    }
    debug(testsToRun) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            if (this.log.enabled)
                this.log.info(`Debugging test(s) ${JSON.stringify(testsToRun)} of ${this.workspaceFolderPath}`);
            const config = yield this.configReader.currentConfig;
            if (!config) {
                this.log.info('Adapter disabled for this folder, debugging cancelled');
                return;
            }
            const testRunPromise = this.run(testsToRun, true);
            this.log.info('Starting the debug session');
            let debugSession;
            try {
                debugSession = yield this.startDebugging(config);
            }
            catch (err) {
                this.log.error('Failed starting the debug session - aborting', err);
                this.cancel();
                return;
            }
            const subscription = this.onDidTerminateDebugSession((session) => {
                if (debugSession != session)
                    return;
                this.log.info('Debug session ended');
                this.cancel();
                subscription.dispose();
            });
            yield testRunPromise;
        });
    }
    cancel() {
        if (this.runningTestProcess) {
            this.log.info('Killing running test process');
            this.runningTestProcess.kill();
        }
    }
    launchWorkerProcess(config, childProcScript, execArgv) {
        const ipcOpts = {
            role: config.ipcRole ? ((config.ipcRole === 'client') ? 'server' : 'client') : undefined,
            port: config.ipcRole ? config.ipcPort : undefined,
            host: config.ipcRole ? config.ipcHost : undefined
        };
        const ipcOptsString = JSON.stringify(ipcOpts);
        const env = (0, util_1.stringsOnly)(Object.assign(Object.assign({}, process.env), config.env));
        if (config.ipcRole) {
            env['VSCODE_WORKSPACE_PATH'] = this.workspaceFolderPath;
            env['MOCHA_WORKER_PATH'] = this.workerScript;
        }
        const stdio = ['pipe', 'pipe', 'pipe', 'ipc'];
        const cwd = config.cwd;
        if (config.nodePath) {
            if (this.log.enabled)
                this.log.debug(`Spawning ${childProcScript} with IPC options ${ipcOptsString}`);
            return (0, child_process_1.spawn)(config.nodePath, [...execArgv, childProcScript, ipcOptsString], { env, stdio, cwd });
        }
        else {
            if (this.log.enabled)
                this.log.debug(`Forking ${childProcScript} with IPC options ${ipcOptsString}`);
            return (0, child_process_1.fork)(childProcScript, [ipcOptsString], { execArgv, env, stdio, cwd });
        }
    }
    connectToWorkerProcess(config, childProc, args, handler) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            if (config.ipcRole) {
                let ipcSocket;
                if (config.ipcRole === 'client') {
                    ipcSocket = yield (0, vscode_test_adapter_remoting_util_1.createConnection)(config.ipcPort, { host: config.ipcHost, timeout: config.ipcTimeout });
                }
                else {
                    ipcSocket = yield (0, vscode_test_adapter_remoting_util_1.receiveConnection)(config.ipcPort, { host: config.ipcHost, timeout: config.ipcTimeout });
                }
                (0, vscode_test_adapter_remoting_util_1.readMessages)(ipcSocket, handler);
                (0, vscode_test_adapter_remoting_util_1.writeMessage)(ipcSocket, args);
            }
            else {
                childProc.on('message', handler);
                childProc.send(args);
            }
        });
    }
    collectNodesById(info) {
        this.nodesById.set(info.id, info);
        if (info.type === 'suite') {
            for (const child of info.children) {
                this.collectNodesById(child);
            }
        }
    }
    collectTests(info, tests) {
        if (info.type === 'suite') {
            for (const child of info.children) {
                this.collectTests(child, tests);
            }
        }
        else {
            tests.push(info);
        }
    }
}
exports.MochaAdapterCore = MochaAdapterCore;
//# sourceMappingURL=core.js.map