"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.installHunter = void 0;
const vscode = require("vscode");
const child_process_1 = require("child_process");
const installerMessage = { title: "Install Package" };
function installHunter(pythonPath, postInstall, onError = () => null) {
    // This means the 'hunter' package is not installed .. Notify
    // and offer to install for user automatically.
    vscode.window
        .showInformationMessage("Wolf requires the hunter package. Install now or run 'pip install hunter --user' manually.", installerMessage)
        .then(result => {
        if (result === installerMessage) {
            const child = child_process_1.spawn(pythonPath, ["-m", "pip", "install", "hunter", "--user"]);
            child.stderr.on("data", data => {
                console.error("INSTALL_ERROR:", data + "");
                onError();
            });
            child.on("close", code => {
                if (code !== 0) {
                    vscode.window.showWarningMessage([
                        "There was an error attempting to install hunter. Please try running",
                        "'pip install hunter --user' manually."
                    ].join(" "));
                    onError();
                }
                else {
                    vscode.window.showInformationMessage("Hunter installed successfully. Re-running Wolf..");
                    postInstall();
                }
            });
        }
    });
}
exports.installHunter = installHunter;
//# sourceMappingURL=hunterInstaller.js.map