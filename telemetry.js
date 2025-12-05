"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.setSendDebugEvents = exports.sendEvent = exports.sendDebugEvent = exports.sendFailedToPublishError = exports.sendNoTestFolderNameError = exports.sendShowRelatedTestsEvent = exports.sendShowTableDataEvent = exports.sendTestDebugStartEvent = exports.sendTestRunFinishedEvent = exports.sendTestRunStartEvent = exports.createTelemetryReporter = void 0;
const vscode = require("vscode");
const extension_telemetry_1 = require("@vscode/extension-telemetry");
const constants_1 = require("./constants");
const extension_1 = require("./extension");
const testController_1 = require("./testController");
const config_1 = require("./config");
const types_1 = require("./types");
function createTelemetryReporter() {
    const extensionId = (0, extension_1.getExtension)().id;
    const extensionVersion = (0, extension_1.getExtension)().packageJSON.version;
    return new extension_telemetry_1.default(extensionId, extensionVersion, constants_1.appInsightsKey);
}
exports.createTelemetryReporter = createTelemetryReporter;
function sendTestRunStartEvent(request) {
    if ((0, config_1.getCurrentWorkspaceConfig)().sendDebugTelemetry) {
        vscode.window.showInformationMessage("Sending AL Test Runner debug telemetry events...", 'Disable').then(value => {
            if (value === 'Disable') {
                setSendDebugEvents(false);
            }
        });
    }
    sendTestRunEvent('001-TestStarted', request);
}
exports.sendTestRunStartEvent = sendTestRunStartEvent;
function sendTestRunFinishedEvent(request) {
    sendTestRunEvent('002-TestFinished', request);
}
exports.sendTestRunFinishedEvent = sendTestRunFinishedEvent;
function sendTestDebugStartEvent(request) {
    sendTestRunEvent('003-DebugStarted', request);
}
exports.sendTestDebugStartEvent = sendTestDebugStartEvent;
function sendShowTableDataEvent() {
    sendEvent('004-ShowTableData');
}
exports.sendShowTableDataEvent = sendShowTableDataEvent;
function sendShowRelatedTestsEvent() {
    sendEvent('005-ShowRelatedTests');
}
exports.sendShowRelatedTestsEvent = sendShowRelatedTestsEvent;
function sendNoTestFolderNameError() {
    return sendError('E01-NoTestFolderNameSet', 'Please set the name of the workspace folder which contains your test app in the extension settings (see "Test Folder Name").');
}
exports.sendNoTestFolderNameError = sendNoTestFolderNameError;
function sendFailedToPublishError(detail) {
    let message = '';
    if (detail) {
        message = detail;
    }
    else {
        message = constants_1.failedToPublishMessage;
    }
    return sendError('E02-PowerShellPublishingFailed', message);
}
exports.sendFailedToPublishError = sendFailedToPublishError;
function sendDebugEvent(name, properties) {
    const debugEventProperty = { 'isDebugEvent': 'true' };
    const combinedProperties = Object.assign(Object.assign({}, properties), debugEventProperty);
    if ((0, config_1.getCurrentWorkspaceConfig)().sendDebugTelemetry) {
        extension_1.telemetryReporter.sendTelemetryEvent('DEBUG-' + name, combinedProperties);
    }
}
exports.sendDebugEvent = sendDebugEvent;
function sendError(eventName, errorMessage) {
    extension_1.telemetryReporter.sendTelemetryErrorEvent(eventName);
    vscode.window.showErrorMessage(errorMessage);
    return errorMessage;
}
function sendTestRunEvent(eventName, request) {
    let runType;
    let testCount;
    let codeCoverageEnabled, publishBeforeTest, enablePublishingFromPowerShell;
    const config = (0, config_1.getCurrentWorkspaceConfig)();
    if ((0, config_1.getCurrentWorkspaceConfig)(true, 'telemetry').telemetryLevel === 'off') {
        return;
    }
    codeCoverageEnabled = config.enableCodeCoverage;
    publishBeforeTest = config.publishBeforeTest;
    if (config.enablePublishingFromPowerShell) {
        enablePublishingFromPowerShell = 'true';
    }
    else {
        enablePublishingFromPowerShell = 'false';
    }
    if (request.include === undefined) {
        runType = types_1.RunType.All;
        testCount = testController_1.numberOfTests;
    }
    else if (request.include.length > 1) {
        runType = types_1.RunType.Selection;
        testCount = (0, testController_1.getTestItemsIncludedInRequest)(request).length;
    }
    else {
        const testItem = request.include[0];
        if (testItem.parent) {
            runType = types_1.RunType.Test;
            testCount = 1;
        }
        else {
            runType = types_1.RunType.Codeunit;
            testCount = testItem.children.size;
        }
    }
    sendEvent(eventName, { 'codeCoverageEnabled': codeCoverageEnabled, 'publishBeforeTest': publishBeforeTest, 'enablePublishingFromPowerShell': enablePublishingFromPowerShell }, { 'runType': runType, 'testCount': testCount });
}
function sendEvent(eventName, properties, measurements) {
    extension_1.telemetryReporter.sendTelemetryEvent(eventName, properties, measurements);
}
exports.sendEvent = sendEvent;
function setSendDebugEvents(newSendTelemetryEvents) {
    vscode.workspace.getConfiguration().update('al-test-runner.sendDebugTelemetry', newSendTelemetryEvents);
}
exports.setSendDebugEvents = setSendDebugEvents;
//# sourceMappingURL=telemetry.js.map