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
exports.createAnonymousUser = exports.onboardPlugin = void 0;
const vscode_1 = require("vscode");
const Util_1 = require("./Util");
const HttpClient_1 = require("./HttpClient");
const DeviceManager_1 = require("./managers/DeviceManager");
let retry_counter = 0;
const one_min_millis = 1000 * 60;
function onboardPlugin(ctx, callback) {
    return __awaiter(this, void 0, void 0, function* () {
        const jwt = (0, Util_1.getItem)("jwt");
        if (jwt) {
            return callback(ctx);
        }
        const windowState = vscode_1.window.state;
        if (windowState.focused) {
            // perform primary window related work
            primaryWindowOnboarding(ctx, callback);
        }
        else {
            // call the secondary onboarding logic
            secondaryWindowOnboarding(ctx, callback);
            return callback(ctx);
        }
    });
}
exports.onboardPlugin = onboardPlugin;
function primaryWindowOnboarding(ctx, callback) {
    return __awaiter(this, void 0, void 0, function* () {
        const jwt = yield createAnonymousUser();
        if (jwt) {
            // great, it worked. call the callback
            return callback(ctx);
        }
        else {
            // call activate again later
            setTimeout(() => {
                retry_counter++;
                onboardPlugin(ctx, callback);
            }, one_min_millis * 2);
        }
    });
}
/**
 * This is called if there's no JWT. If it reaches a
 * 6th call it will create an anon user.
 * @param ctx
 * @param callback
 */
function secondaryWindowOnboarding(ctx, callback) {
    return __awaiter(this, void 0, void 0, function* () {
        if (retry_counter < 5) {
            retry_counter++;
            // call activate again in about 15 seconds
            setTimeout(() => {
                onboardPlugin(ctx, callback);
            }, 1000 * 15);
            return;
        }
        // tried enough times, create an anon user
        yield createAnonymousUser();
        // call the callback
        return callback(ctx);
    });
}
/**
 * create an anonymous user based on github email or mac addr
 */
function createAnonymousUser() {
    return __awaiter(this, void 0, void 0, function* () {
        const jwt = (0, Util_1.getItem)("jwt");
        // check one more time before creating the anon user
        if (!jwt) {
            // this should not be undefined if its an account reset
            const plugin_uuid = (0, Util_1.getPluginUuid)();
            const auth_callback_state = (0, Util_1.getAuthCallbackState)();
            const username = yield (0, DeviceManager_1.getOsUsername)();
            const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            const hostname = yield (0, DeviceManager_1.getHostname)();
            const resp = yield (0, HttpClient_1.appPost)("/api/v1/anonymous_user", {
                timezone,
                username,
                plugin_uuid,
                hostname,
                auth_callback_state,
            });
            if ((0, HttpClient_1.isResponseOk)(resp) && resp.data) {
                (0, Util_1.setItem)("jwt", resp.data.plugin_jwt);
                if (!resp.data.registered) {
                    (0, Util_1.setItem)('name', null);
                }
                (0, Util_1.setItem)('switching_account', false);
                (0, Util_1.setAuthCallbackState)('');
                return resp.data.plugin_jwt;
            }
        }
        return null;
    });
}
exports.createAnonymousUser = createAnonymousUser;
//# sourceMappingURL=OnboardManager.js.map