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
exports.updateCodyConfig = exports.getSpotifyIntegration = exports.switchSpotifyAccount = exports.populateSpotifyUser = exports.updateSpotifyClientInfo = exports.isPremiumUser = exports.hasSpotifyUser = exports.getConnectedSpotifyUser = exports.clearSpotifyAccessToken = void 0;
const cody_music_1 = require("cody-music");
const vscode_1 = require("vscode");
const Constants_1 = require("../Constants");
const HttpClient_1 = require("../HttpClient");
const Util_1 = require("../Util");
const UserStatusManager_1 = require("./UserStatusManager");
const PlaylistDataManager_1 = require("./PlaylistDataManager");
const DeviceManager_1 = require("./DeviceManager");
let spotifyUser = null;
let spotifyAccessToken = "";
let spotifyAccessTokenTimer = undefined;
function clearSpotifyAccessToken() {
    if (spotifyAccessTokenTimer) {
        clearTimeout(spotifyAccessTokenTimer);
        spotifyAccessTokenTimer = null;
    }
}
exports.clearSpotifyAccessToken = clearSpotifyAccessToken;
function getConnectedSpotifyUser() {
    return __awaiter(this, void 0, void 0, function* () {
        if (!spotifyUser || !spotifyUser.id) {
            spotifyUser = yield (0, cody_music_1.getUserProfile)();
        }
        return spotifyUser;
    });
}
exports.getConnectedSpotifyUser = getConnectedSpotifyUser;
function hasSpotifyUser() {
    return !!(spotifyUser && spotifyUser.product);
}
exports.hasSpotifyUser = hasSpotifyUser;
function isPremiumUser() {
    return __awaiter(this, void 0, void 0, function* () {
        if ((spotifyUser === null || spotifyUser === void 0 ? void 0 : spotifyUser.id) && spotifyUser.product !== "premium") {
            // check 1 more time
            yield populateSpotifyUser(true);
        }
        return !!((spotifyUser === null || spotifyUser === void 0 ? void 0 : spotifyUser.id) && spotifyUser.product === "premium");
    });
}
exports.isPremiumUser = isPremiumUser;
function updateSpotifyClientInfo() {
    return __awaiter(this, void 0, void 0, function* () {
        const resp = yield (0, HttpClient_1.appGet)("/api/v1/integration_connection/spotify/access_token");
        if ((0, HttpClient_1.isResponseOk)(resp)) {
            spotifyAccessToken = resp.data.access_token;
            if (resp.data.expires_at) {
                // start the timer
                refetchSpotifyAccessTokenTimer(resp.data.expires_at);
            }
        }
    });
}
exports.updateSpotifyClientInfo = updateSpotifyClientInfo;
function refetchSpotifyAccessTokenTimer(expires_at) {
    const millisTimeout = new Date(expires_at).getTime() - new Date().getTime();
    if (spotifyAccessTokenTimer) {
        clearTimeout(spotifyAccessTokenTimer);
        spotifyAccessTokenTimer = null;
    }
    spotifyAccessTokenTimer = setTimeout(() => {
        // initialize spotify access token with cody music
        (0, PlaylistDataManager_1.initializeSpotify)(false);
    }, millisTimeout);
}
function populateSpotifyUser() {
    return __awaiter(this, arguments, void 0, function* (hardRefresh = false) {
        let spotifyIntegration = yield getSpotifyIntegration();
        if (!spotifyIntegration) {
            spotifyIntegration = yield getSpotifyIntegration();
        }
        if (spotifyIntegration && (hardRefresh || !spotifyUser || !spotifyUser.id)) {
            // get the user
            spotifyUser = yield (0, cody_music_1.getUserProfile)();
        }
    });
}
exports.populateSpotifyUser = populateSpotifyUser;
function switchSpotifyAccount() {
    return __awaiter(this, void 0, void 0, function* () {
        const selection = yield vscode_1.window.showInformationMessage(`Are you sure you would like to connect to a different Spotify account?`, ...[Constants_1.YES_LABEL]);
        if (selection === Constants_1.YES_LABEL) {
            (0, Util_1.launchWebUrl)(`${Constants_1.app_endpoint}/code_time/integration_type/spotify`);
        }
    });
}
exports.switchSpotifyAccount = switchSpotifyAccount;
function getSpotifyIntegration() {
    return __awaiter(this, void 0, void 0, function* () {
        const spotifyIntegrations = yield (0, UserStatusManager_1.getCachedSpotifyIntegrations)();
        if (spotifyIntegrations === null || spotifyIntegrations === void 0 ? void 0 : spotifyIntegrations.length) {
            // get the last one in case we have more than one.
            // the last one is the the latest one created.
            return spotifyIntegrations[spotifyIntegrations.length - 1];
        }
        return null;
    });
}
exports.getSpotifyIntegration = getSpotifyIntegration;
/**
 * Update the cody config settings for cody-music
 */
function updateCodyConfig() {
    return __awaiter(this, void 0, void 0, function* () {
        const spotifyIntegration = yield getSpotifyIntegration();
        if (!spotifyIntegration) {
            spotifyUser = null;
        }
        if (!spotifyAccessToken) {
            yield updateSpotifyClientInfo();
        }
        const codyConfig = new cody_music_1.CodyConfig();
        codyConfig.enableItunesDesktop = false;
        codyConfig.enableItunesDesktopSongTracking = (0, DeviceManager_1.isMac)();
        codyConfig.enableSpotifyDesktop = (0, DeviceManager_1.isMac)();
        codyConfig.spotifyAccessToken = spotifyAccessToken;
        (0, cody_music_1.setConfig)(codyConfig);
    });
}
exports.updateCodyConfig = updateCodyConfig;
//# sourceMappingURL=SpotifyManager.js.map