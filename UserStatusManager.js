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
exports.getCachedSpotifyIntegrations = exports.getCachedSlackIntegrations = exports.processNewSpotifyIntegration = exports.authenticationCompleteHandler = exports.launchLogin = exports.showSignUpMenuOptions = exports.showLogInMenuOptions = exports.getUser = void 0;
const vscode_1 = require("vscode");
const Constants_1 = require("../Constants");
const HttpClient_1 = require("../HttpClient");
const MenuManager_1 = require("../MenuManager");
const Util_1 = require("../Util");
const websockets_1 = require("../websockets");
const PlaylistDataManager_1 = require("./PlaylistDataManager");
const SpotifyManager_1 = require("./SpotifyManager");
const queryString = require("query-string");
let currentUser = null;
function getUser() {
    return __awaiter(this, arguments, void 0, function* (useCache = false) {
        if (useCache && currentUser) {
            (0, SpotifyManager_1.updateCodyConfig)();
            return currentUser;
        }
        const resp = yield (0, HttpClient_1.appGet)('/api/v1/user');
        if ((0, HttpClient_1.isResponseOk)(resp) && resp.data) {
            currentUser = resp.data;
            (0, SpotifyManager_1.updateCodyConfig)();
            return currentUser;
        }
        return null;
    });
}
exports.getUser = getUser;
function showLogInMenuOptions() {
    showAuthMenuOptions("Log in", false /*isSignup*/);
}
exports.showLogInMenuOptions = showLogInMenuOptions;
function showSignUpMenuOptions() {
    showAuthMenuOptions("Sign up", true /*isSignup*/);
}
exports.showSignUpMenuOptions = showSignUpMenuOptions;
function showAuthMenuOptions(authText, isSignup = true) {
    const items = [];
    const placeholder = `${authText} using...`;
    items.push({
        label: `${authText} with Google`,
        command: "musictime.googleLogin",
        commandArgs: [null /*KpmItem*/, true /*switching_account*/],
    });
    items.push({
        label: `${authText} with GitHub`,
        command: "musictime.githubLogin",
        commandArgs: [null /*KpmItem*/, true /*switching_account*/],
    });
    if (isSignup) {
        items.push({
            label: `${authText} with Email`,
            command: "musictime.emailSignup",
            commandArgs: [null /*KpmItem*/, true /*switching_account*/],
        });
    }
    else {
        items.push({
            label: `${authText} with Email`,
            command: "musictime.emailLogin",
            commandArgs: [null /*KpmItem*/, true /*switching_account*/],
        });
    }
    const menuOptions = {
        items,
        placeholder,
    };
    (0, MenuManager_1.showQuickPick)(menuOptions);
}
function launchLogin() {
    return __awaiter(this, arguments, void 0, function* (loginType = "software", switching_account = false) {
        (0, Util_1.setItem)("authType", loginType);
        (0, Util_1.setItem)("switching_account", switching_account);
        const jwt = (0, Util_1.getItem)("jwt");
        const name = (0, Util_1.getItem)("name");
        const auth_callback_state = (0, Util_1.getAuthCallbackState)(true);
        let url = "";
        const obj = {
            plugin_id: (0, Util_1.getMusicTimePluginId)(),
            plugin_uuid: (0, Util_1.getPluginUuid)(),
            auth_callback_state,
            login: true,
        };
        if (!name) {
            obj["plugin_token"] = jwt;
        }
        if (loginType === "github") {
            // github signup/login flow
            url = `${Constants_1.app_endpoint}/auth/github`;
        }
        else if (loginType === "google") {
            // google signup/login flow
            url = `${Constants_1.app_endpoint}/auth/google`;
        }
        else {
            // email login
            obj["token"] = (0, Util_1.getItem)("jwt");
            obj["auth"] = "software";
            if (switching_account) {
                obj["login"] = true;
                url = `${Constants_1.app_endpoint}/onboarding`;
            }
            else {
                url = `${Constants_1.app_endpoint}/email-signup`;
            }
        }
        const qryStr = queryString.stringify(obj);
        url = `${url}?${qryStr}`;
        (0, Util_1.launchWebUrl)(url);
    });
}
exports.launchLogin = launchLogin;
function authenticationCompleteHandler(user) {
    return __awaiter(this, void 0, void 0, function* () {
        // clear the auth callback state
        (0, Util_1.setAuthCallbackState)(null);
        // set the email and jwt
        if ((user === null || user === void 0 ? void 0 : user.registered) === 1) {
            currentUser = user;
            if (user.plugin_jwt) {
                (0, Util_1.setItem)("jwt", user.plugin_jwt);
            }
            (0, Util_1.setItem)('name', user.email);
            vscode_1.window.showInformationMessage(`Successfully registered`);
            try {
                (0, websockets_1.initializeWebsockets)();
            }
            catch (e) {
                console.error("Failed to initialize websockets", e);
            }
            yield getUser();
            // this will reload the playlist for both slack and spotify
            yield processNewSpotifyIntegration(false);
            if ((0, Util_1.codeTimeExtInstalled)()) {
                setTimeout(() => {
                    vscode_1.commands.executeCommand("codetime.refreshCodeTimeView");
                }, 1000);
            }
            if ((0, Util_1.editorOpsExtInstalled)()) {
                setTimeout(() => {
                    vscode_1.commands.executeCommand("editorOps.refreshEditorOpsView");
                }, 1000);
            }
        }
    });
}
exports.authenticationCompleteHandler = authenticationCompleteHandler;
function processNewSpotifyIntegration() {
    return __awaiter(this, arguments, void 0, function* (showSuccess = true) {
        (0, Util_1.setItem)("requiresSpotifyReAuth", false);
        if (showSuccess) {
            // update the login status
            vscode_1.window.showInformationMessage(`Successfully connected to Spotify. Loading playlists...`);
        }
        // initialize spotify and playlists
        yield (0, PlaylistDataManager_1.initializeSpotify)();
    });
}
exports.processNewSpotifyIntegration = processNewSpotifyIntegration;
function getCachedSlackIntegrations() {
    return __awaiter(this, void 0, void 0, function* () {
        var _a, _b;
        if (!currentUser) {
            currentUser = yield getUser(true);
        }
        if ((_a = currentUser === null || currentUser === void 0 ? void 0 : currentUser.integration_connections) === null || _a === void 0 ? void 0 : _a.length) {
            return (_b = currentUser === null || currentUser === void 0 ? void 0 : currentUser.integration_connections) === null || _b === void 0 ? void 0 : _b.filter((integration) => integration.status === 'ACTIVE' && (integration.integration_type_id === 14));
        }
        return [];
    });
}
exports.getCachedSlackIntegrations = getCachedSlackIntegrations;
function getCachedSpotifyIntegrations() {
    return __awaiter(this, void 0, void 0, function* () {
        var _a, _b;
        if (!currentUser) {
            currentUser = yield getUser(true);
        }
        if ((_a = currentUser === null || currentUser === void 0 ? void 0 : currentUser.integration_connections) === null || _a === void 0 ? void 0 : _a.length) {
            return (_b = currentUser === null || currentUser === void 0 ? void 0 : currentUser.integration_connections) === null || _b === void 0 ? void 0 : _b.filter((integration) => integration.status === 'ACTIVE' && (integration.integration_type_id === 12));
        }
        return [];
    });
}
exports.getCachedSpotifyIntegrations = getCachedSpotifyIntegrations;
//# sourceMappingURL=UserStatusManager.js.map