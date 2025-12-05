"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WalletIdentityProvider = void 0;
const vscode = require("vscode");
const ShellCommand_1 = require("../utilities/ShellCommand");
const Logger_1 = require("../utilities/Logger");
const Constants_1 = require("../utilities/Constants");
const TelemetryLogger_1 = require("../utilities/TelemetryLogger");
class WalletIdentityProvider {
    async createIdentity() {
        TelemetryLogger_1.TelemetryLogger.instance().sendTelemetryEvent('CreateIdentity');
        const username = await vscode.window.showInputBox({ prompt: 'Provide a username for the identity',
            placeHolder: "Username" });
        if (username) {
            if (username.search(/^[a-zA-Z0-9_-]+$/g) === -1) {
                Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `Enter alphanumeric, hyphen (-) and underscore (_) characters only in username`);
                return;
            }
            if ((await WalletIdentityProvider.getwallets()).findIndex(element => {
                return element.toLowerCase() === username.toLowerCase();
            }) === -1) {
                const identityArgs = [username];
                const result = await ShellCommand_1.ShellCommand.execDockerComposeSh(Constants_1.DockerComposeFiles.localCa, Constants_1.Settings.singleOrgSettings.caDomain, "/etc/hyperledger/fabric/scripts/registerEnrollIdentity.sh", identityArgs);
                if (result.search(/service .* is not running container .*/gi) > -1) {
                    Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, "Start the Network or Start Debugging(F5) before creating an identity");
                }
                else {
                    vscode.commands.executeCommand('hlf.identity.refresh');
                    Logger_1.Logger.instance().showMessageOnly(Constants_1.LogType.info, `Created and enrolled identity for user: ${username}`);
                }
            }
            else {
                Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `The user '${username}' already exists`);
            }
        }
    }
    async removeIdentity(element) {
        TelemetryLogger_1.TelemetryLogger.instance().sendTelemetryEvent('RemoveIdentity');
        if (element && element.label) {
            const username = element.label.toString();
            const identityArgs = [username];
            const result = await ShellCommand_1.ShellCommand.execDockerComposeSh(Constants_1.DockerComposeFiles.localCa, Constants_1.Settings.singleOrgSettings.caDomain, "/etc/hyperledger/fabric/scripts/removeIdentity.sh", identityArgs);
            if (result.search(/service .* is not running container .*/gi) > -1) {
                Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, "Start the Network or Start Debugging(F5) before modifying an identity");
            }
            else {
                vscode.commands.executeCommand('hlf.identity.refresh');
                Logger_1.Logger.instance().showMessageOnly(Constants_1.LogType.info, `Removed identity for user: ${username}`);
            }
        }
    }
    static async getwallets() {
        try {
            const result = await ShellCommand_1.ShellCommand.execDockerComposeSh(Constants_1.DockerComposeFiles.localCa, Constants_1.Settings.singleOrgSettings.caDomain, "/etc/hyperledger/fabric/scripts/getWallets.sh", [], false);
            if (result) {
                return result.split("\n").filter(user => user && user !== "/" && user.indexOf("/") > -1).map(user => user.replace("/", ""));
            }
            else {
                return [];
            }
        }
        catch (error) {
            Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `Cannot retrieve wallets. ${error}`);
            return [];
        }
    }
}
exports.WalletIdentityProvider = WalletIdentityProvider;
//# sourceMappingURL=WalletIdentityProvider.js.map