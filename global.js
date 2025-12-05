"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.GlobalState = void 0;
const state_1 = require("../../@types/state");
const agent_1 = require("../../@types/agent");
const logger_1 = require("../../util/logger");
class GlobalState {
    constructor(map) {
        this.map = map;
    }
    GetKeployInstallationProgress() {
        let progress = this.map.get(state_1.GlobalState.INSTALLATION_PROGRESS);
        if (progress) {
            return progress;
        }
        return { phase: agent_1.Status.ERROR, progress: 0, message: 'No installation progress found' };
    }
    SetKeployInstallationProgress(progress) {
        this.map.update(state_1.GlobalState.INSTALLATION_PROGRESS, progress);
    }
    ClearKeployInstallationProgress() {
        this.map.update(state_1.GlobalState.INSTALLATION_PROGRESS, undefined);
    }
    GetExtensionVersion() {
        return this.map.get(state_1.GlobalState.EXTENSION_VERSION) || '';
    }
    SetExtensionVersion(version) {
        this.map.update(state_1.GlobalState.EXTENSION_VERSION, version);
    }
    GetAuthState() {
        let state = {
            accessToken: this.map.get(state_1.GlobalState.ACCESS_TOKEN) || '',
            jwtToken: this.map.get(state_1.GlobalState.JWT_TOKEN) || '',
            signedIn: this.map.get(state_1.GlobalState.SIGNED_IN) || false,
            authType: this.map.get(state_1.GlobalState.AUTH_TYPE) || undefined
        };
        return state;
    }
    SetAuthState(state) {
        this.map.update(state_1.GlobalState.ACCESS_TOKEN, state.accessToken);
        this.map.update(state_1.GlobalState.JWT_TOKEN, state.jwtToken);
        this.map.update(state_1.GlobalState.SIGNED_IN, state.signedIn);
        this.map.update(state_1.GlobalState.AUTH_TYPE, state.authType);
    }
    GetSubscriptionEnded() {
        return this.map.get(state_1.GlobalState.SUBSCRIPTION_ENDED) || true;
    }
    SetSubscriptionEnded(status) {
        this.map.update(state_1.GlobalState.SUBSCRIPTION_ENDED, status);
    }
    SetCurrentServerStatus(status) {
        this.map.update(state_1.GlobalState.SERVER_STATUS, status);
    }
    GetCurrentServerStatus() {
        return this.map.get(state_1.GlobalState.SERVER_STATUS) || agent_1.Status.INACTIVE;
    }
    CleanUp() {
        // clean up all the global state
        this.map.keys().forEach(key => {
            logger_1.Logger.info(`Removing global state: ${key}`);
            this.map.update(key, undefined);
        });
    }
}
exports.GlobalState = GlobalState;
//# sourceMappingURL=global.js.map