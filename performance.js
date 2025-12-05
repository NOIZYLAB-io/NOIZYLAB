"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.showPerformanceProfile = exports.updatePerformanceStatusBarItemVisibility = exports.createPerformanceStatusBarItem = void 0;
const vscode = require("vscode");
const config_1 = require("./config");
const fs_1 = require("fs");
const path_1 = require("path");
let performanceStatusBarItem;
const performanceProfileWatcher = vscode.workspace.createFileSystemWatcher('**/.altestrunner/PerformanceProfile.alcpuprofile');
performanceProfileWatcher.onDidChange(e => updatePerformanceStatusBarItemVisibility());
performanceProfileWatcher.onDidCreate(e => updatePerformanceStatusBarItemVisibility());
performanceProfileWatcher.onDidDelete(e => updatePerformanceStatusBarItemVisibility());
function createPerformanceStatusBarItem() {
    performanceStatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right);
    performanceStatusBarItem.command = 'altestrunner.showPerformanceProfile';
    performanceStatusBarItem.text = 'Performance ⏱️';
    performanceStatusBarItem.tooltip = 'Show the performance profile that was downloaded from the previous test run.';
    updatePerformanceStatusBarItemVisibility();
    return performanceStatusBarItem;
}
exports.createPerformanceStatusBarItem = createPerformanceStatusBarItem;
function updatePerformanceStatusBarItemVisibility() {
    if ((0, fs_1.existsSync)(getPerformanceProfilePath())) {
        performanceStatusBarItem.show();
    }
    else {
        performanceStatusBarItem.hide();
    }
}
exports.updatePerformanceStatusBarItemVisibility = updatePerformanceStatusBarItemVisibility;
function showPerformanceProfile() {
    vscode.commands.executeCommand('vscode.openWith', vscode.Uri.file(getPerformanceProfilePath()), 'alProfileVisualizer.topDown');
}
exports.showPerformanceProfile = showPerformanceProfile;
function getPerformanceProfilePath() {
    return (0, path_1.join)((0, config_1.getALTestRunnerPath)(), 'PerformanceProfile.alcpuprofile');
}
//# sourceMappingURL=performance.js.map