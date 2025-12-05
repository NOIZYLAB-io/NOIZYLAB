"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.hotModeWarning = void 0;
const vscode_1 = require("vscode");
function hotModeWarning() {
    const config = vscode_1.workspace.getConfiguration("wolf");
    const disableWarnings = { title: "Don't ask again" };
    const notificationText = "Wolf evalutes your code when you stop typing for a while. You can " +
        'change the delay by editing "updateFrequency" in settings. If you ' +
        "are writing changes to the filesystem or calling external API's you " +
        "should consider cacheing the calls or increasing this value.";
    if (config.get("disableHotModeWarning") !== true) {
        vscode_1.window
            .showInformationMessage(notificationText, disableWarnings)
            .then(result => {
            if (result === disableWarnings) {
                config.update("disableHotModeWarning", true);
            }
        });
    }
}
exports.hotModeWarning = hotModeWarning;
//# sourceMappingURL=hotWarning.js.map