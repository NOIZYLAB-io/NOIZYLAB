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
exports.getContainerPasswordFromALTestRunnerConfig = exports.discoverTestWorkspaceFolder = exports.getWorkspaceFolder = exports.getTestFolderFromConfig = exports.getLaunchConfiguration = exports.getALTestRunnerLaunchConfig = exports.getCurrentWorkspaceConfig = exports.selectLaunchConfig = exports.getLaunchJsonPath = exports.getDebugConfigurationsFromLaunchJson = exports.launchConfigIsValid = exports.setALTestRunnerConfig = exports.getALTestRunnerConfig = exports.getALTestRunnerConfigPath = exports.getALTestRunnerPath = void 0;
const fs_1 = require("fs");
const vscode = require("vscode");
const telemetry_1 = require("./telemetry");
const types = require("./types");
const alFileHelper_1 = require("./alFileHelper");
const extension_1 = require("./extension");
const powershell_1 = require("./powershell");
function getALTestRunnerPath() {
    const alTestRunnerPath = (0, alFileHelper_1.getTestFolderPath)() + '\\.altestrunner';
    return alTestRunnerPath;
}
exports.getALTestRunnerPath = getALTestRunnerPath;
function getALTestRunnerConfigPath() {
    return getALTestRunnerPath() + '\\config.json';
}
exports.getALTestRunnerConfigPath = getALTestRunnerConfigPath;
function getALTestRunnerConfig() {
    (0, telemetry_1.sendDebugEvent)('getALTestRunnerConfig-start');
    let alTestRunnerConfigPath = getALTestRunnerConfigPath();
    let data;
    try {
        data = (0, fs_1.readFileSync)(alTestRunnerConfigPath, { encoding: 'utf-8' });
    }
    catch (error) {
        (0, telemetry_1.sendDebugEvent)('getALTestRunnerConfig-unableToReadConfigFile');
        createALTestRunnerConfig();
        data = (0, fs_1.readFileSync)(alTestRunnerConfigPath, { encoding: 'utf-8' });
    }
    let alTestRunnerConfig = JSON.parse(data);
    return alTestRunnerConfig;
}
exports.getALTestRunnerConfig = getALTestRunnerConfig;
function setALTestRunnerConfig(keyName, keyValue) {
    let debugKeyValue = '';
    if (keyValue) {
        debugKeyValue = keyValue;
    }
    (0, telemetry_1.sendDebugEvent)('setALTestRunnerConfig', { keyName: keyName, keyValue: debugKeyValue });
    let config = getALTestRunnerConfig();
    //@ts-ignore
    config[keyName] = keyValue;
    (0, fs_1.writeFileSync)(getALTestRunnerConfigPath(), JSON.stringify(config), { encoding: 'utf-8' });
}
exports.setALTestRunnerConfig = setALTestRunnerConfig;
function createALTestRunnerConfig() {
    let config = {
        containerResultPath: "",
        launchConfigName: "",
        securePassword: "",
        userName: "",
        companyName: "",
        testSuiteName: "",
        vmUserName: "",
        vmSecurePassword: "",
        remoteContainerName: "",
        dockerHost: "",
        newPSSessionOptions: "",
        testRunnerServiceUrl: "",
        codeCoveragePath: ".//.altestrunner//codecoverage.json",
        culture: "en-US"
    };
    createALTestRunnerDir();
    (0, fs_1.writeFileSync)(getALTestRunnerConfigPath(), JSON.stringify(config, null, 2), { encoding: 'utf-8' });
}
function createALTestRunnerDir() {
    if (getALTestRunnerPath() === '') {
        return;
    }
    if (!((0, fs_1.existsSync)(getALTestRunnerPath()))) {
        (0, fs_1.mkdirSync)(getALTestRunnerPath());
    }
}
function launchConfigIsValid(alTestRunnerConfig) {
    (0, telemetry_1.sendDebugEvent)('launchConfigIsValid-start');
    if (alTestRunnerConfig === undefined) {
        alTestRunnerConfig = getALTestRunnerConfig();
    }
    if (alTestRunnerConfig.launchConfigName === '') {
        return types.launchConfigValidity.Invalid;
    }
    else {
        let debugConfigurations = getDebugConfigurationsFromLaunchJson('launch');
        const filteredDebugConfigurations = debugConfigurations.filter(element => element.name === alTestRunnerConfig.launchConfigName);
        switch (filteredDebugConfigurations.length) {
            case 0:
                return types.launchConfigValidity.Invalid;
            case 1:
                return types.launchConfigValidity.Valid;
            default:
                vscode.window.showErrorMessage(`There are ${filteredDebugConfigurations.length} launch configurations with the name "${alTestRunnerConfig.launchConfigName}". Please make sure that each launch configuration has a unique name.`, {}, "Open config").then(action => {
                    if (action == "Open config") {
                        vscode.commands.executeCommand("workbench.action.debug.configure");
                    }
                });
                return types.launchConfigValidity.NeverValid;
        }
    }
}
exports.launchConfigIsValid = launchConfigIsValid;
function getDebugConfigurationsFromLaunchJson(type) {
    const testWorkspaceFolder = vscode.workspace.getWorkspaceFolder(vscode.Uri.file(getALTestRunnerConfigPath()));
    var configuration = vscode.workspace.getConfiguration('launch', testWorkspaceFolder);
    var debugConfigurations = configuration.configurations;
    if (debugConfigurations.length === 0) {
        configuration = vscode.workspace.getConfiguration('launch');
        debugConfigurations = configuration.configurations;
    }
    return debugConfigurations.filter(element => { return element.request === type; }).slice();
}
exports.getDebugConfigurationsFromLaunchJson = getDebugConfigurationsFromLaunchJson;
function getLaunchJsonPath() {
    return (0, alFileHelper_1.getTestFolderPath)() + '\\.vscode\\launch.json';
}
exports.getLaunchJsonPath = getLaunchJsonPath;
function selectLaunchConfig() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            (0, telemetry_1.sendDebugEvent)('selectLaunchConfig-start');
            let debugConfigurations = getDebugConfigurationsFromLaunchJson('launch');
            let selectedConfig;
            if (debugConfigurations.length === 1) {
                selectedConfig = debugConfigurations.shift().name;
            }
            else if (debugConfigurations.length > 1) {
                let configNames = debugConfigurations.map(element => element.name);
                selectedConfig = yield vscode.window.showQuickPick(configNames, { canPickMany: false, placeHolder: 'Please select a configuration to run tests against' });
            }
            setALTestRunnerConfig('launchConfigName', selectedConfig);
            resolve(selectedConfig);
        }));
    });
}
exports.selectLaunchConfig = selectLaunchConfig;
function getCurrentWorkspaceConfig(forTestFolder = true, section = 'al-test-runner') {
    let testFolderPath;
    if (forTestFolder) {
        testFolderPath = (0, alFileHelper_1.getTestFolderPath)();
    }
    if (testFolderPath) {
        return vscode.workspace.getConfiguration(section, vscode.Uri.file(testFolderPath));
    }
    else {
        return vscode.workspace.getConfiguration(section);
    }
}
exports.getCurrentWorkspaceConfig = getCurrentWorkspaceConfig;
//get the launch config currently selected as the config for test runner
//if not specified then select one
function getALTestRunnerLaunchConfig() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            let launchConfig = getALTestRunnerConfig().launchConfigName;
            if (!launchConfig) {
                let selectedConfig = yield selectLaunchConfig();
                if (selectedConfig) {
                    launchConfig = selectedConfig;
                }
            }
            resolve(JSON.parse(getLaunchConfiguration(launchConfig)));
        }));
    });
}
exports.getALTestRunnerLaunchConfig = getALTestRunnerLaunchConfig;
function getLaunchConfiguration(configName) {
    const configs = getDebugConfigurationsFromLaunchJson('launch');
    const config = JSON.stringify(configs.filter(element => element.name == configName)[0]);
    return config;
}
exports.getLaunchConfiguration = getLaunchConfiguration;
function getTestFolderFromConfig(config) {
    if (!config.testFolderName) {
        return undefined;
    }
    let workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders) {
        return undefined;
    }
    workspaceFolders = workspaceFolders.filter(folder => {
        return folder.name === config.testFolderName;
    });
    if (workspaceFolders.length > 0) {
        return workspaceFolders[0].uri.fsPath;
    }
}
exports.getTestFolderFromConfig = getTestFolderFromConfig;
function getWorkspaceFolder() {
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders) {
        return '';
    }
    if (workspaceFolders.length === 1) {
        return workspaceFolders[0].uri.fsPath;
    }
    const discoveredTestFolder = discoverTestWorkspaceFolder(workspaceFolders);
    if (discoveredTestFolder) {
        return discoveredTestFolder;
    }
    if (extension_1.activeEditor) {
        const workspace = vscode.workspace.getWorkspaceFolder(extension_1.activeEditor.document.uri);
        if (workspace) {
            return workspace.uri.fsPath;
        }
    }
    if (vscode.window.visibleTextEditors.length > 0) {
        const workspace = vscode.workspace.getWorkspaceFolder(vscode.window.visibleTextEditors[0].document.uri);
        if (workspace) {
            return workspace.uri.fsPath;
        }
    }
    throw new Error('Please open a file in the project you want to run the tests for.');
}
exports.getWorkspaceFolder = getWorkspaceFolder;
function discoverTestWorkspaceFolder(workspaceFolders) {
    if (!workspaceFolders) {
        return undefined;
    }
    let testFolder = '';
    const config = getCurrentWorkspaceConfig(false);
    const identifiers = config.testWorkspaceFolderIdentifiers;
    identifiers.forEach(identifier => {
        if (!testFolder) {
            const testFolders = workspaceFolders.filter(folder => {
                if (folder.name.toLowerCase().endsWith(identifier.toLowerCase()) || folder.name.toLowerCase().startsWith(identifier.toLowerCase())) {
                    return true;
                }
            });
            if (testFolders[0]) {
                testFolder = testFolders[0].uri.fsPath;
            }
        }
    });
    if (testFolder !== '') {
        return testFolder;
    }
    else {
        return undefined;
    }
}
exports.discoverTestWorkspaceFolder = discoverTestWorkspaceFolder;
function getContainerPasswordFromALTestRunnerConfig() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const securePassword = getALTestRunnerConfig().securePassword;
            if (securePassword === '') {
                vscode.window.showWarningMessage('Please set the credentials for the container with the AL Test Runner: Set Container Credentials command.');
                resolve('');
                return;
            }
            const command = `[System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR((ConvertTo-SecureString -String '${securePassword}')))`;
            const result = yield (0, powershell_1.invokePowerShellCommand)(command);
            resolve(result);
        }));
    });
}
exports.getContainerPasswordFromALTestRunnerConfig = getContainerPasswordFromALTestRunnerConfig;
//# sourceMappingURL=config.js.map