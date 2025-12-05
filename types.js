"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.enableCodeCoverage = exports.launchConfigValidity = exports.OutputType = exports.CodeCoverageDisplay = exports.RunType = exports.PublishType = void 0;
var PublishType;
(function (PublishType) {
    PublishType[PublishType["None"] = 0] = "None";
    PublishType[PublishType["Publish"] = 1] = "Publish";
    PublishType[PublishType["Rapid"] = 2] = "Rapid";
})(PublishType = exports.PublishType || (exports.PublishType = {}));
var RunType;
(function (RunType) {
    RunType[RunType["All"] = 0] = "All";
    RunType[RunType["Codeunit"] = 1] = "Codeunit";
    RunType[RunType["Test"] = 2] = "Test";
    RunType[RunType["Selection"] = 3] = "Selection";
})(RunType = exports.RunType || (exports.RunType = {}));
var CodeCoverageDisplay;
(function (CodeCoverageDisplay) {
    CodeCoverageDisplay["Off"] = "Off";
    CodeCoverageDisplay["Previous"] = "Previous";
    CodeCoverageDisplay["All"] = "All";
})(CodeCoverageDisplay = exports.CodeCoverageDisplay || (exports.CodeCoverageDisplay = {}));
var OutputType;
(function (OutputType) {
    OutputType["Editor"] = "Editor";
    OutputType["Channel"] = "Output";
})(OutputType = exports.OutputType || (exports.OutputType = {}));
var launchConfigValidity;
(function (launchConfigValidity) {
    launchConfigValidity[launchConfigValidity["Valid"] = 0] = "Valid";
    launchConfigValidity[launchConfigValidity["Invalid"] = 1] = "Invalid";
    launchConfigValidity[launchConfigValidity["NeverValid"] = 2] = "NeverValid";
})(launchConfigValidity = exports.launchConfigValidity || (exports.launchConfigValidity = {}));
var enableCodeCoverage;
(function (enableCodeCoverage) {
    enableCodeCoverage["No"] = "No";
    enableCodeCoverage["When running all tests"] = "When running all tests";
    enableCodeCoverage["Always"] = "Always";
})(enableCodeCoverage = exports.enableCodeCoverage || (exports.enableCodeCoverage = {}));
//# sourceMappingURL=types.js.map