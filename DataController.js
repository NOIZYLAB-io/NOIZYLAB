"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.displayReadmeIfNotExists = void 0;
const vscode_1 = require("vscode");
const Util_1 = require("./Util");
function displayReadmeIfNotExists(override = false) {
    const vscode_musictime_initialized = (0, Util_1.getItem)("displayedMtReadme");
    if (!vscode_musictime_initialized || override) {
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.displaySidebar");
        }, 1000);
        const readmeUri = vscode_1.Uri.file((0, Util_1.getLocalREADMEFile)());
        vscode_1.commands.executeCommand("markdown.showPreview", readmeUri, vscode_1.ViewColumn.One);
        (0, Util_1.setItem)("displayedMtReadme", true);
    }
}
exports.displayReadmeIfNotExists = displayReadmeIfNotExists;
//# sourceMappingURL=DataController.js.map