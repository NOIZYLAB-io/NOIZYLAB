"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ConfigReader = void 0;
const tslib_1 = require("tslib");
const path = tslib_1.__importStar(require("path"));
const module_1 = tslib_1.__importDefault(require("module"));
const util_1 = require("./util");
const vscode = tslib_1.__importStar(require("vscode"));
const glob_1 = require("glob");
const minimatch_1 = require("minimatch");
const chokidar_1 = tslib_1.__importDefault(require("chokidar"));
const assert_1 = tslib_1.__importDefault(require("assert"));
const dotenv_1 = require("dotenv");
const vscode_test_adapter_util_1 = require("vscode-test-adapter-util");
const optsReader_1 = require("./optsReader");
const configKeys_1 = require("./configKeys");
const debouncer_1 = require("./debouncer");
class ConfigReader {
    get currentConfig() {
        if (this._currentConfig === undefined) {
            this._currentConfig = this.readConfig();
        }
        return this._currentConfig;
    }
    constructor(workspaceFolder, workspaceState, load, retire, log) {
        this.workspaceFolder = workspaceFolder;
        this.workspaceState = workspaceState;
        this.load = load;
        this.retire = retire;
        this.log = log;
        this.disposables = [];
        this.enabledStateKey = `enable ${this.workspaceFolder.uri.fsPath}`;
        this.disposables.push(vscode.workspace.onDidChangeConfiguration((configChange) => tslib_1.__awaiter(this, void 0, void 0, function* () {
            this.log.info('Configuration changed');
            let configKey;
            if (configKey = this.configChangeRequires(configChange, 'reloadTests')) {
                const config = yield this.currentConfig;
                if ((config === null || config === void 0 ? void 0 : config.autoload) === true) {
                    if (this.log.enabled)
                        this.log.info(`Reloading tests because ${configKey} changed`);
                    load();
                }
                else {
                    if (this.log.enabled)
                        this.log.info(`Reloading tests cancelled because the adapter or autoloading is disabled`);
                    this.reloadConfig();
                    retire();
                }
                return;
            }
            if (configKey = this.configChangeRequires(configChange, 'retire')) {
                if (this.log.enabled)
                    this.log.info(`Sending retire event because ${configKey} changed`);
                this.reloadConfig();
                retire();
                return;
            }
            if (configKey = this.configChangeRequires(configChange, 'reloadConfig')) {
                if (this.log.enabled)
                    this.log.info(`Reloading configuration because ${configKey} changed`);
                this.reloadConfig();
                return;
            }
        })));
        this.disposables.push(vscode.workspace.onDidSaveTextDocument((document) => tslib_1.__awaiter(this, void 0, void 0, function* () {
            this.onFileChanged(document.uri.fsPath, false);
        })));
    }
    reloadConfig() {
        this._currentConfig = this.readConfig();
    }
    enableAdapter() {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            yield this.workspaceState.update(this.enabledStateKey, true);
        });
    }
    disableAdapter() {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            yield this.workspaceState.update(this.enabledStateKey, false);
        });
    }
    getAutoload(config) {
        const autoload = config.get(configKeys_1.configKeys.autoload.key);
        return (autoload !== undefined) ? autoload : true;
    }
    onFileChanged(filename, fromWatcher) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            var _a;
            const config = yield this.currentConfig;
            if ((config === null || config === void 0 ? void 0 : config.autoload) !== true) {
                if (this.log.enabled)
                    this.log.info(`Reloading cancelled because the adapter or autoloading is disabled`);
                return;
            }
            if (this.log.enabled)
                this.log.info(`${filename} was saved - checking if this affects ${this.workspaceFolder.uri.fsPath}`);
            const isTestFile = yield this.isTestFile(filename);
            if (!isTestFile && !filename.startsWith(this.workspaceFolder.uri.fsPath)) {
                return;
            }
            if (isTestFile === 'config') {
                if (!fromWatcher) {
                    if (this.log.enabled)
                        this.log.info(`Reloading because ${filename} is a config file`);
                    (_a = this.debouncer) === null || _a === void 0 ? void 0 : _a.reset();
                    this.load();
                }
                return;
            }
            if (fromWatcher) {
                (0, assert_1.default)(this.debouncer);
                this.debouncer.fileChanged(isTestFile ? filename : undefined);
            }
            else if (!this.watcher) {
                this.filesChangedCallback(isTestFile, isTestFile ? [filename] : undefined);
            }
        });
    }
    filesChangedCallback(reload, testFiles) {
        if (reload) {
            if (testFiles) {
                if (this.log.enabled)
                    this.log.info(`Reloading because ${JSON.stringify(testFiles)} are test files`);
                this.load(testFiles.map(util_1.normalizePath), false);
            }
            else {
                if (this.log.enabled)
                    this.log.info('Reloading because of changed files');
                this.load(undefined, false);
            }
        }
        else {
            this.log.info('Sending retire event');
            this.retire();
        }
    }
    readConfig() {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            if (this.watcher) {
                this.watcher.close();
                this.watcher = undefined;
            }
            if (this.debouncer) {
                this.debouncer.dispose();
                this.debouncer = undefined;
            }
            const config = vscode.workspace.getConfiguration(configKeys_1.configSection, this.workspaceFolder.uri);
            if (!(yield this.checkEnabled(config))) {
                return undefined;
            }
            const cwd = this.getCwd(config);
            const nodePath = yield this.getNodePath(config);
            const nodeArgv = this.getNodeArgv(config);
            let optsFromFiles;
            const optsReader = new optsReader_1.MochaOptsReader(this.log);
            const defaultMochaOptsFile = 'test/mocha.opts';
            let mochaOptsFile = this.getMochaOptsFile(config);
            let mochaConfigFile;
            let packageFile = 'package.json';
            if (!mochaOptsFile) {
                if (yield (0, util_1.fileExists)(path.resolve(this.workspaceFolder.uri.fsPath, defaultMochaOptsFile))) {
                    mochaOptsFile = defaultMochaOptsFile;
                }
            }
            if (mochaOptsFile) {
                const resolvedFile = path.resolve(this.workspaceFolder.uri.fsPath, mochaOptsFile);
                optsFromFiles = yield optsReader.readMochaOptsFile(resolvedFile);
            }
            else {
                const argv = [];
                const configFile = this.getMochaConfigFile(config);
                if (configFile !== 'default') {
                    if (configFile === null) {
                        argv.push('--no-config');
                    }
                    else {
                        mochaConfigFile = path.resolve(this.workspaceFolder.uri.fsPath, configFile);
                        argv.push('--config', mochaConfigFile);
                    }
                }
                const pkgFile = this.getPkgFile(config);
                if (pkgFile !== 'default') {
                    if (pkgFile === null) {
                        packageFile = undefined;
                        argv.push('--no-package');
                    }
                    else {
                        packageFile = path.resolve(this.workspaceFolder.uri.fsPath, pkgFile);
                        argv.push('--package', packageFile);
                    }
                }
                optsFromFiles = yield optsReader.readOptsUsingMocha(cwd, nodePath, nodeArgv, argv);
            }
            const mochaOpts = yield this.getMochaOpts(config, optsFromFiles.mochaOpts);
            const envFile = this.getEnvFile(config);
            const testFiles = yield this.lookupFiles(config, optsFromFiles.globs, optsFromFiles.ignores);
            const extraFiles = optsFromFiles.files
                .map(file => path.resolve(this.workspaceFolder.uri.fsPath, file));
            if (this.log.enabled && (extraFiles.length > 0)) {
                this.log.debug(`Adding files ${JSON.stringify(extraFiles)}`);
            }
            const watcherConfig = this.getWatcherConfig(config);
            if (watcherConfig) {
                this.watcher = chokidar_1.default.watch(watcherConfig.files, {
                    ignored: watcherConfig.ignore,
                    ignoreInitial: true
                });
                this.debouncer = new debouncer_1.FileChangeDebouncer(watcherConfig.debounce, (reload, changedFiles) => this.filesChangedCallback(reload, changedFiles));
                this.watcher.on('add', filename => this.onFileChanged(filename, true));
                this.watcher.on('change', filename => this.onFileChanged(filename, true));
                this.watcher.on('unlink', filename => this.onFileChanged(filename, true));
            }
            return {
                nodePath,
                nodeArgv,
                mochaPath: yield this.getMochaPath(config, cwd),
                cwd,
                env: yield this.getEnv(config, mochaOpts),
                monkeyPatch: this.getMonkeyPatch(config),
                multiFileSuites: this.getMultiFileSuites(config),
                pruneFiles: this.getPruneFiles(config),
                debuggerPort: this.getDebuggerPort(config),
                debuggerConfig: this.getDebuggerConfig(config),
                mochaOpts,
                testFiles,
                extraFiles,
                mochaConfigFile,
                packageFile,
                mochaOptsFile,
                envFile,
                globs: this.getTestFilesGlobs(config, optsFromFiles.globs),
                ignores: this.getIgnores(config, optsFromFiles.ignores),
                esmLoader: this.getEsmLoader(config),
                launcherScript: this.getLauncherScript(config),
                ipcRole: this.getIpcRole(config),
                ipcPort: this.getIpcPort(config),
                ipcHost: this.getIpcHost(config),
                ipcTimeout: this.getIpcTimeout(config),
                autoload: this.getAutoload(config)
            };
        });
    }
    checkEnabled(config) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            if (this.workspaceFolder.uri.scheme !== 'file') {
                return false;
            }
            const enabledState = this.workspaceState.get(this.enabledStateKey);
            if (enabledState !== undefined) {
                return enabledState;
            }
            for (const configKey in configKeys_1.configKeys) {
                const configValues = config.inspect(configKey);
                if (configValues && (configValues.workspaceFolderValue !== undefined)) {
                    yield this.enableAdapter();
                    return true;
                }
            }
            for (const configFile of ['.mocharc.js', '.mocharc.json', '.mocharc.yaml', '.mocharc.yml', 'test/mocha.opts']) {
                const resolvedConfigFile = path.resolve(this.workspaceFolder.uri.fsPath, configFile);
                if (yield (0, util_1.fileExists)(resolvedConfigFile)) {
                    yield this.enableAdapter();
                    return true;
                }
            }
            try {
                const packageJson = JSON.parse(yield (0, util_1.readFile)(path.resolve(this.workspaceFolder.uri.fsPath, 'package.json')));
                if (packageJson.mocha ||
                    (packageJson.dependencies && packageJson.dependencies.mocha) ||
                    (packageJson.devDependencies && packageJson.devDependencies.mocha)) {
                    yield this.enableAdapter();
                    return true;
                }
            }
            catch (err) {
            }
            const filePaths = yield this.globFiles(config, 'test/**/*.js');
            if (filePaths.length > 0) {
                let msg = `The workspace folder ${this.workspaceFolder.name} contains test files, but I'm not sure if they should be run using Mocha. `;
                msg += 'Do you want to enable Mocha Test Explorer for this workspace folder?';
                const userChoice = yield vscode.window.showInformationMessage(msg, 'Enable', 'Disable');
                if (userChoice === 'Enable') {
                    yield this.enableAdapter();
                    return true;
                }
                else if (userChoice === 'Disable') {
                    yield this.disableAdapter();
                    return false;
                }
            }
            return false;
        });
    }
    getMochaConfigFile(config) {
        return config.get(configKeys_1.configKeys.configFile.key) || null;
    }
    getPkgFile(config) {
        return config.get(configKeys_1.configKeys.pkgFile.key) || null;
    }
    getMochaOptsFile(config) {
        const configValues = config.inspect(configKeys_1.configKeys.optsFile.key);
        if (configValues.workspaceFolderValue !== undefined) {
            return configValues.workspaceFolderValue;
        }
        else if (configValues.workspaceValue !== undefined) {
            return configValues.workspaceValue;
        }
        else if (configValues.globalValue !== undefined) {
            return configValues.globalValue;
        }
        else {
            return undefined;
        }
    }
    getTestFilesGlobs(config, globsFromOptsFile) {
        const globConfigValues = config.inspect(configKeys_1.configKeys.files.key);
        let globFromConfig = globConfigValues.workspaceFolderValue ||
            globConfigValues.workspaceValue ||
            globConfigValues.globalValue;
        if (globFromConfig) {
            if (typeof globFromConfig === 'string') {
                globFromConfig = [globFromConfig];
            }
            return [...globFromConfig, ...globsFromOptsFile];
        }
        else if (globsFromOptsFile.length > 0) {
            return globsFromOptsFile;
        }
        else {
            return [globConfigValues.defaultValue];
        }
    }
    getIgnores(config, ignoresFromOptsFile) {
        let ignoresFromConfig = config.get(configKeys_1.configKeys.ignore.key) || [];
        if (typeof ignoresFromConfig === 'string') {
            ignoresFromConfig = [ignoresFromConfig];
        }
        return [...ignoresFromConfig, ...ignoresFromOptsFile];
    }
    getWatcherConfig(config) {
        const rawConfig = config.get(configKeys_1.configKeys.watch.key);
        if (!rawConfig) {
            return undefined;
        }
        const normalizeArray = (files) => files.map(file => path.resolve(this.workspaceFolder.uri.fsPath, file));
        const defaultIgnore = normalizeArray(['**/node_modules/**']);
        const defaultDebounce = 200;
        if (typeof rawConfig === 'string') {
            return {
                files: normalizeArray([rawConfig]),
                ignore: defaultIgnore,
                debounce: defaultDebounce
            };
        }
        else if (Array.isArray(rawConfig)) {
            return {
                files: normalizeArray(rawConfig),
                ignore: defaultIgnore,
                debounce: defaultDebounce
            };
        }
        else {
            return {
                files: normalizeArray((typeof rawConfig.files === 'string') ? [rawConfig.files] : rawConfig.files),
                ignore: normalizeArray(rawConfig.ignore ? (Array.isArray(rawConfig.ignore) ? rawConfig.ignore : [rawConfig.ignore]) : []),
                debounce: (rawConfig.debounce === undefined) ? defaultDebounce : rawConfig.debounce
            };
        }
    }
    lookupFiles(config, globsFromOptsFile, ignoresFromOptsFile) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            const globs = this.getTestFilesGlobs(config, globsFromOptsFile);
            const ignores = this.getIgnores(config, ignoresFromOptsFile);
            if (this.log.enabled)
                this.log.debug(`Looking for test files ${JSON.stringify(globs)} in ${this.workspaceFolder.uri.fsPath}`);
            const testFiles = [];
            for (let testFilesGlob of globs) {
                for (const path of yield this.globFiles(config, testFilesGlob)) {
                    if (ignores.every(ignore => !this.absolutePathMatchesRelativeGlob(path, ignore))) {
                        testFiles.push(path);
                    }
                }
            }
            if (this.log.enabled) {
                this.log.debug(`Found test files ${JSON.stringify(testFiles)}`);
            }
            return testFiles;
        });
    }
    globFiles(config, relativeGlob) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            if (this.getGlobImplementation(config) === 'glob') {
                const cwdRelativeGlob = config.cwd ? path.join(config.cwd, relativeGlob) : relativeGlob;
                const absoluteGlob = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, cwdRelativeGlob));
                const matches = yield (0, glob_1.glob)(absoluteGlob, { nodir: true, windowsPathsNoEscape: true });
                return matches.map(util_1.normalizePath);
            }
            else {
                if (relativeGlob.startsWith('./')) {
                    relativeGlob = relativeGlob.substring(2);
                }
                const relativePattern = new vscode.RelativePattern(this.workspaceFolder, relativeGlob);
                const fileUris = yield vscode.workspace.findFiles(relativePattern, null);
                return fileUris.map(uri => (0, util_1.normalizePath)(uri.fsPath));
            }
        });
    }
    absolutePathMatchesRelativeGlob(absolutePath, relativeGlob) {
        absolutePath = (0, util_1.normalizePath)(absolutePath);
        const absoluteGlob = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, relativeGlob));
        return (0, minimatch_1.minimatch)(absolutePath, absoluteGlob, { windowsPathsNoEscape: true });
    }
    isTestFile(absolutePath) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            absolutePath = (0, util_1.normalizePath)(absolutePath);
            if (!absolutePath.startsWith((0, util_1.normalizePath)(this.workspaceFolder.uri.fsPath))) {
                return false;
            }
            const settingsPath = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, '.vscode/settings.json'));
            if (absolutePath === settingsPath) {
                return false;
            }
            const config = yield this.currentConfig;
            if (!(config === null || config === void 0 ? void 0 : config.mochaConfigFile)) {
                for (const configFile of ['.mocharc.js', '.mocharc.json', '.mocharc.yaml', '.mocharc.yml']) {
                    const resolvedConfigFile = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, configFile));
                    if (absolutePath === resolvedConfigFile) {
                        return 'config';
                    }
                }
            }
            if (!config) {
                const testFolderPath = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, 'test'));
                return absolutePath.startsWith(testFolderPath);
            }
            for (const configFile of [config.mochaConfigFile, config.packageFile, config.mochaOptsFile, config.envFile, config.launcherScript]) {
                if (configFile) {
                    const resolvedConfigFile = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, configFile));
                    if (absolutePath === resolvedConfigFile) {
                        return 'config';
                    }
                }
            }
            const globs = config.globs;
            for (const relativeGlob of globs) {
                const absoluteGlob = (0, util_1.normalizePath)(path.resolve(this.workspaceFolder.uri.fsPath, relativeGlob));
                if ((0, minimatch_1.minimatch)(absolutePath, absoluteGlob, { windowsPathsNoEscape: true }) &&
                    config.ignores.every(ignore => !this.absolutePathMatchesRelativeGlob(absolutePath, ignore))) {
                    return true;
                }
            }
            for (const file of config.extraFiles) {
                if (absolutePath === file) {
                    return true;
                }
            }
            return false;
        });
    }
    getEnv(config, mochaOpts) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            let resultEnv = config.get(configKeys_1.configKeys.env.key) || {};
            if (this.log.enabled)
                this.log.debug(`Using environment variables from config: ${JSON.stringify(resultEnv)}`);
            let envPath = config.get(configKeys_1.configKeys.envPath.key);
            if (envPath) {
                envPath = path.resolve(this.workspaceFolder.uri.fsPath, envPath);
                if (this.log.enabled)
                    this.log.debug(`Reading environment variables from ${envPath}`);
                try {
                    const dotenvFile = yield (0, util_1.readFile)(envPath);
                    resultEnv = Object.assign(Object.assign({}, (0, dotenv_1.parse)(dotenvFile)), resultEnv);
                }
                catch (e) {
                    const envPathSettings = config.inspect(configKeys_1.configKeys.envPath.key);
                    if ((envPathSettings === null || envPathSettings === void 0 ? void 0 : envPathSettings.workspaceFolderValue) || (envPathSettings === null || envPathSettings === void 0 ? void 0 : envPathSettings.workspaceValue)) {
                        throw e;
                    }
                    else {
                        if (this.log.enabled)
                            this.log.info(`Ignoring globally configured envPath because ${envPath} can't be read`);
                    }
                }
            }
            if ((mochaOpts.requires.indexOf('esm') >= 0) && !resultEnv.hasOwnProperty('NYC_ROOT_ID')) {
                resultEnv['NYC_ROOT_ID'] = '';
            }
            return resultEnv;
        });
    }
    getCwd(config) {
        const dirname = (0, util_1.normalizePath)(this.workspaceFolder.uri.fsPath);
        const configCwd = config.get(configKeys_1.configKeys.cwd.key);
        const cwd = configCwd ? path.resolve(dirname, configCwd) : dirname;
        if (this.log.enabled)
            this.log.debug(`Using working directory: ${cwd}`);
        return cwd;
    }
    getMochaOpts(config, mochaOptsFromFile) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            let requires = this.mergeOpts(configKeys_1.configKeys.require.key, mochaOptsFromFile.requires, config);
            if (typeof requires === 'string') {
                if (requires.length > 0) {
                    requires = [requires];
                }
                else {
                    requires = [];
                }
            }
            else if (typeof requires === 'undefined') {
                requires = [];
            }
            const mochaOpts = {
                ui: this.mergeOpts(configKeys_1.configKeys.ui.key, mochaOptsFromFile.ui, config),
                timeout: this.mergeOpts(configKeys_1.configKeys.timeout.key, mochaOptsFromFile.timeout, config),
                retries: this.mergeOpts(configKeys_1.configKeys.retries.key, mochaOptsFromFile.retries, config),
                requires,
                delay: this.mergeOpts(configKeys_1.configKeys.delay.key, mochaOptsFromFile.delay, config),
                fullTrace: this.mergeOpts(configKeys_1.configKeys.fullTrace.key, mochaOptsFromFile.fullTrace, config),
                exit: this.mergeOpts(configKeys_1.configKeys.exit.key, mochaOptsFromFile.exit, config),
                asyncOnly: this.mergeOpts(configKeys_1.configKeys.asyncOnly.key, mochaOptsFromFile.asyncOnly, config),
                parallel: this.mergeOpts(configKeys_1.configKeys.parallel.key, mochaOptsFromFile.parallel, config),
                jobs: this.mergeOpts(configKeys_1.configKeys.jobs.key, mochaOptsFromFile.jobs, config) || undefined
            };
            if (this.log.enabled)
                this.log.debug(`Using Mocha options: ${JSON.stringify(mochaOpts)}`);
            return mochaOpts;
        });
    }
    mergeOpts(configKey, fileConfigValue, config) {
        const vsCodeConfigValues = config.inspect(configKey);
        if (vsCodeConfigValues.workspaceFolderValue !== undefined) {
            return vsCodeConfigValues.workspaceFolderValue;
        }
        else if (vsCodeConfigValues.workspaceValue !== undefined) {
            return vsCodeConfigValues.workspaceValue;
        }
        else if (vsCodeConfigValues.globalValue !== undefined) {
            return vsCodeConfigValues.globalValue;
        }
        else if (fileConfigValue !== undefined) {
            return fileConfigValue;
        }
        else {
            return vsCodeConfigValues.defaultValue;
        }
    }
    getMochaPath(config, cwd) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            const configuredMochaPath = config.get(configKeys_1.configKeys.mochaPath.key);
            if (configuredMochaPath === 'default') {
                const cwdRequire = module_1.default.createRequire(path.join(cwd, "index.js"));
                try {
                    return path.dirname(cwdRequire.resolve('mocha'));
                }
                catch (_a) { }
            }
            else if (configuredMochaPath) {
                return path.resolve(this.workspaceFolder.uri.fsPath, configuredMochaPath);
            }
            return path.dirname(require.resolve('mocha'));
        });
    }
    getNodePath(config) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            let nodePath = config.get(configKeys_1.configKeys.nodePath.key) || undefined;
            if (nodePath === 'default') {
                nodePath = yield (0, vscode_test_adapter_util_1.detectNodePath)();
            }
            if (this.log.enabled)
                this.log.debug(`Using nodePath: ${nodePath}`);
            return nodePath;
        });
    }
    getNodeArgv(config) {
        return config.get(configKeys_1.configKeys.nodeArgv.key) || [];
    }
    getMonkeyPatch(config) {
        let monkeyPatch = config.get(configKeys_1.configKeys.monkeyPatch.key);
        return (monkeyPatch !== undefined) ? monkeyPatch : true;
    }
    getMultiFileSuites(config) {
        return config.get(configKeys_1.configKeys.multiFileSuites.key) || false;
    }
    getDebuggerPort(config) {
        return config.get(configKeys_1.configKeys.debuggerPort.key) || 9229;
    }
    getDebuggerConfig(config) {
        return config.get(configKeys_1.configKeys.debuggerConfig.key) || undefined;
    }
    getPruneFiles(config) {
        return config.get(configKeys_1.configKeys.pruneFiles.key) || false;
    }
    getEsmLoader(config) {
        const esmLoader = config.get(configKeys_1.configKeys.esmLoader.key);
        return (esmLoader !== undefined) ? esmLoader : true;
    }
    getEnvFile(config) {
        return config.get(configKeys_1.configKeys.envPath.key) || undefined;
    }
    getGlobImplementation(config) {
        return config.get(configKeys_1.configKeys.globImplementation.key) || 'glob';
    }
    getLauncherScript(config) {
        return config.get(configKeys_1.configKeys.launcherScript.key) || undefined;
    }
    getIpcRole(config) {
        return config.get('ipcRole') || undefined;
    }
    getIpcPort(config) {
        return config.get('ipcPort') || 9449;
    }
    getIpcHost(config) {
        return config.get('ipcHost') || undefined;
    }
    getIpcTimeout(config) {
        return config.get('ipcTimeout') || 5000;
    }
    configChangeRequires(configChange, action) {
        for (const configKeyInfo of Object.values(configKeys_1.configKeys)) {
            if ((configKeyInfo.onChange === action) && configChange.affectsConfiguration(configKeyInfo.fullKey, this.workspaceFolder.uri)) {
                return configKeyInfo.fullKey;
            }
        }
        return undefined;
    }
    dispose() {
        if (this.watcher) {
            this.watcher.close();
            this.watcher = undefined;
        }
        for (const disposable of this.disposables) {
            disposable.dispose();
        }
        this.disposables = [];
    }
}
exports.ConfigReader = ConfigReader;
//# sourceMappingURL=configReader.js.map