"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HlfRequestCommandProvider = void 0;
const vscode = require("vscode");
const ShellCommand_1 = require("../utilities/ShellCommand");
const Constants_1 = require("../utilities/Constants");
const HlfResponseWebview_1 = require("../views/HlfResponseWebview");
const Logger_1 = require("../utilities/Logger");
const JSON5 = require("json5");
const WalletIdentityProvider_1 = require("./WalletIdentityProvider");
const TelemetryLogger_1 = require("../utilities/TelemetryLogger");
class HlfRequestCommandProvider {
    constructor() {
        this.lineSplit = /\r?\n/g;
    }
    async exec(range) {
        const editor = vscode.window.activeTextEditor;
        const document = vscode.window.activeTextEditor?.document;
        if (!editor || !document) {
            return;
        }
        //Parse the input in the range as a valid Json
        const lines = document.getText(range);
        const requestJson = JSON5.parse(lines);
        //Get the transaction type and method name. Assume that the transaction type is case-insensitive
        let transactionType = "query";
        let methodName = this.getValueWithoutCase(requestJson, "query");
        if (!methodName) {
            transactionType = "invoke";
            methodName = this.getValueWithoutCase(requestJson, "invoke");
        }
        TelemetryLogger_1.TelemetryLogger.instance().sendTelemetryEvent('RequestCommand', { transactionType: transactionType });
        //Get the identity to be used for the request
        const wallet = this.getValueWithoutCase(requestJson, "identity");
        //Fabric expects all arguments to be strings even when the argument type declared in a method is not a string.
        //Since we are allowing users to declare the arguments as a Json array, we will accept any valid JSON array
        //including any valid native type (number, boolean) or any JSON object as elements in the array.
        //Convert all elements as strings before sending the transaction to Fabric
        let payloadArgs = [];
        for (const arg in requestJson.args) {
            if (typeof requestJson.args[arg] === 'object') {
                payloadArgs.push(`'\"${JSON.stringify(requestJson.args[arg]).split('"').join('\\"')}\"'`);
            }
            else {
                payloadArgs.push(`'\"${requestJson.args[arg].toString().split('"').join('\\"')}\"'`);
            }
        }
        const payloadLines = `[${[payloadArgs.join(',')]}]`;
        //Send the transaction to Fabric
        const chaincodeArgs = [transactionType, Constants_1.Settings.defaultChaincodeId, methodName, payloadLines];
        if (wallet) {
            if ((await WalletIdentityProvider_1.WalletIdentityProvider.getwallets()).findIndex(element => {
                return element.toLowerCase() === wallet.toLowerCase();
            }) === -1) {
                Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `The user '${wallet}' does not exist. Create the user in the wallet first before submitting a request`);
                return;
            }
            chaincodeArgs.push(wallet);
        }
        var startTime = process.hrtime();
        let result = await ShellCommand_1.ShellCommand.execDockerComposeBash(Constants_1.DockerComposeFiles.localNetwork, "debug-cli", "/etc/hyperledger/fabric/scripts/sendTransactionInternal.sh", chaincodeArgs);
        const elapsedTime = TelemetryLogger_1.TelemetryLogger.instance().parseHrtimeToMs(process.hrtime(startTime));
        if (result.indexOf("error building chaincode: error building image: failed to get chaincode package for external build:") > -1
            || result.indexOf("connect: connection refused") > -1
            || result.indexOf("make sure the chaincode asset has been successfully defined on channel") > -1) {
            Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, "Start Debugging(F5) before submitting a transaction to Fabric");
            result = "Error: cannot debug Chaincode. response: status:500 message: \"Start Debugging(F5) before submitting a transaction to Fabric. If you have already started debugging, wait for the debug symbols to appear at the top of the window.\"";
        }
        if (result.indexOf("service \"debug-cli\" is not running container") > -1) {
            Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, "Start the Network or Start Debugging(F5) before submitting a transaction to Fabric");
            result = "Error: cannot connect to local Fabric environment. response: status:500 message: \"Start the Network or Start Debugging(F5) before submitting a transaction to Fabric. If you have already started debugging, wait for the debug symbols to appear at the top of the window.\"";
        }
        else if (result.startsWith("Error: chaincode argument error: invalid character")) {
            Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `Syntax error in query/invoke request. Chaincode arguments supplied: ${payloadLines}.`);
        }
        //Render the result
        const responseWebView = HlfResponseWebview_1.HlfResponseWebview.instance();
        responseWebView.render(result, elapsedTime);
    }
    getValueWithoutCase(requestJson, transactionType) {
        return requestJson[Object.keys(requestJson).find(key => key.toLowerCase() === transactionType)];
    }
}
exports.HlfRequestCommandProvider = HlfRequestCommandProvider;
//# sourceMappingURL=HlfRequestCommandProvider.js.map