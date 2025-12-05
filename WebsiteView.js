"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WebsiteView = void 0;
const vscode = require("vscode");
const Constants_1 = require("../utilities/Constants");
const TelemetryLogger_1 = require("../utilities/TelemetryLogger");
class WebsiteView {
    static showMessage() {
        if (Constants_1.Settings.spdrLinkMessageShown === 0) {
            setTimeout(() => {
                vscode.window.showInformationMessage("Limited time offer!! Get $400 worth of credits FREE. Checkout Spydra's fully managed platform and no-code features for Hyperledger Fabric.", "Try Spydra Platform", "Contact Spydra").then(selection => {
                    if (selection === 'Contact Spydra') {
                        vscode.env.openExternal(vscode.Uri.parse(Constants_1.Links.contactUs));
                        TelemetryLogger_1.TelemetryLogger.instance().sendTelemetryEvent('OpenExternalLink', { 'link': Constants_1.Links.contactUs, linkTitle: "Contact Spydra Popup" });
                    }
                    else if (selection === 'Try Spydra Platform') {
                        vscode.env.openExternal(vscode.Uri.parse(Constants_1.Links.spydra));
                        TelemetryLogger_1.TelemetryLogger.instance().sendTelemetryEvent('OpenExternalLink', { 'link': Constants_1.Links.spydra, linkTitle: "Try Spydra Platform" });
                    }
                });
            }, 30000);
            Constants_1.Settings.spdrLinkMessageShown = 1;
        }
    }
}
exports.WebsiteView = WebsiteView;
//# sourceMappingURL=WebsiteView.js.map