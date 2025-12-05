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
exports.handleIntegrationConnectionSocketEvent = void 0;
const vscode_1 = require("vscode");
const Util_1 = require("../Util");
const UserStatusManager_1 = require("../managers/UserStatusManager");
function handleIntegrationConnectionSocketEvent(body) {
    return __awaiter(this, void 0, void 0, function* () {
        // integration_type_id = 14 (slack), 12 (spotify)
        // action = add, update, remove
        const { integration_type_id, integration_type, action } = body;
        yield (0, UserStatusManager_1.getUser)();
        if (integration_type_id === 14) {
            if (action === "add") {
                // clear the auth callback state
                (0, Util_1.setAuthCallbackState)(null);
                vscode_1.window.showInformationMessage("Successfully connected to Slack");
                // refresh the tree view
                setTimeout(() => {
                    // refresh the playlist to show the device button update
                    vscode_1.commands.executeCommand("musictime.reloadMusicTimeView");
                }, 1000);
            }
        }
        else if (integration_type_id === 12) {
            // clear the auth callback state
            (0, Util_1.setAuthCallbackState)(null);
            (0, UserStatusManager_1.processNewSpotifyIntegration)();
        }
    });
}
exports.handleIntegrationConnectionSocketEvent = handleIntegrationConnectionSocketEvent;
//# sourceMappingURL=integration_connection.js.map