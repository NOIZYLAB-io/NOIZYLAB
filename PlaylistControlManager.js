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
exports.showPlayerLaunchConfirmation = exports.playInitialization = exports.launchTrackPlayer = exports.playSelectedItem = exports.playSelectedItems = void 0;
const cody_music_1 = require("cody-music");
const vscode_1 = require("vscode");
const Constants_1 = require("../Constants");
const MusicCommandUtil_1 = require("../music/MusicCommandUtil");
const MusicControlManager_1 = require("../music/MusicControlManager");
const Util_1 = require("../Util");
const PlaylistDataManager_1 = require("./PlaylistDataManager");
const SpotifyManager_1 = require("./SpotifyManager");
const DeviceManager_1 = require("./DeviceManager");
// Play selected tracks
function playSelectedItems(playlistItems) {
    return __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedTrackItems)(playlistItems);
        // ask to launch web or desktop if neither are running
        yield playInitialization(playSelectedTrackItems);
    });
}
exports.playSelectedItems = playSelectedItems;
// PLAY SELECTED TRACK
function playSelectedItem(playlistItem) {
    return __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedTrackItem)(playlistItem, cody_music_1.TrackStatus.Playing);
        // ask to launch web or desktop if neither are running
        yield playInitialization(playMusicSelection);
    });
}
exports.playSelectedItem = playSelectedItem;
function launchTrackPlayer() {
    return __awaiter(this, arguments, void 0, function* (playerName = null, callback = null) {
        const { desktop, activeDesktopPlayerDevice } = (0, PlaylistDataManager_1.getDeviceSet)();
        const hasDesktopDevice = activeDesktopPlayerDevice || desktop ? true : false;
        const requiresDesktopLaunch = !(0, SpotifyManager_1.isPremiumUser)() && (0, DeviceManager_1.isMac)() && !hasDesktopDevice ? true : false;
        if (requiresDesktopLaunch && playerName !== cody_music_1.PlayerName.SpotifyDesktop) {
            vscode_1.window.showInformationMessage("Launching Spotify desktop instead of the web player to allow playback as a non-premium account");
        }
        if (requiresDesktopLaunch || playerName === cody_music_1.PlayerName.SpotifyDesktop) {
            (0, PlaylistDataManager_1.updateSelectedPlayer)(cody_music_1.PlayerName.SpotifyDesktop);
        }
        else {
            (0, PlaylistDataManager_1.updateSelectedPlayer)(cody_music_1.PlayerName.SpotifyWeb);
        }
        // {playlist_id | album_id | track_id, quietly }
        const options = {
            quietly: false,
        };
        const selectedTrack = (0, PlaylistDataManager_1.getSelectedTrackItem)();
        if (selectedTrack) {
            const selectedPlaylist = (0, PlaylistDataManager_1.getPlaylistById)(selectedTrack["playlist_id"]);
            if (selectedPlaylist) {
                options["playlist_id"] = selectedTrack["playlist_id"];
            }
            else if (selectedTrack) {
                options["track_id"] = selectedTrack.id;
            }
        }
        // spotify device launch error would look like ..
        // error:"Command failed: open -a spotify\nUnable to find application named 'spotify'\n"
        const result = yield (0, cody_music_1.launchPlayer)(playerName, options);
        // test if there was an error, fallback to the web player
        if (playerName === cody_music_1.PlayerName.SpotifyDesktop && result && result.error && result.error.includes("failed")) {
            // start the process of launching the web player
            playerName = cody_music_1.PlayerName.SpotifyWeb;
            yield (0, cody_music_1.launchPlayer)(playerName, options);
        }
        setTimeout(() => __awaiter(this, void 0, void 0, function* () {
            yield (0, cody_music_1.play)((0, PlaylistDataManager_1.getSelectedPlayerName)());
            checkDeviceLaunch(playerName, 5, callback);
        }), 3000);
    });
}
exports.launchTrackPlayer = launchTrackPlayer;
// PRIVATE FUNCTIONS
function playInitialization(callback) {
    return __awaiter(this, void 0, void 0, function* () {
        const { desktop } = (0, PlaylistDataManager_1.getDeviceSet)();
        const device = (0, PlaylistDataManager_1.getBestActiveDevice)();
        if (!(0, SpotifyManager_1.hasSpotifyUser)()) {
            // try again
            yield (0, SpotifyManager_1.populateSpotifyUser)();
        }
        const requiresDesktopLaunch = !(0, SpotifyManager_1.isPremiumUser)() && (0, DeviceManager_1.isMac)() && !desktop ? true : false;
        if (!device || requiresDesktopLaunch) {
            return yield showPlayerLaunchConfirmation(callback);
        }
        else {
            // check to see if we need to change the selected player type
            if (device.type === "Computer" && (0, PlaylistDataManager_1.getSelectedPlayerName)() !== cody_music_1.PlayerName.SpotifyDesktop) {
                (0, PlaylistDataManager_1.updateSelectedPlayer)(cody_music_1.PlayerName.SpotifyDesktop);
            }
        }
        // we have a device, continue to the callback if we have it
        if (callback) {
            callback();
        }
    });
}
exports.playInitialization = playInitialization;
function showPlayerLaunchConfirmation(callback) {
    return __awaiter(this, void 0, void 0, function* () {
        // if they're a mac non-premium user, just launch the desktop player
        if ((0, DeviceManager_1.isMac)() && !(0, SpotifyManager_1.isPremiumUser)()) {
            return launchTrackPlayer(cody_music_1.PlayerName.SpotifyDesktop, callback);
        }
        else {
            const buttons = ["Web Player", "Desktop Player"];
            // no devices found at all OR no active devices and a computer device is not found in the list
            const selectedButton = yield vscode_1.window.showInformationMessage(`Music Time requires a running Spotify player. Choose a player to launch.`, ...buttons);
            if (selectedButton === "Desktop Player" || selectedButton === "Web Player") {
                (0, PlaylistDataManager_1.updateSelectedPlayer)(selectedButton === "Desktop Player" ? cody_music_1.PlayerName.SpotifyDesktop : cody_music_1.PlayerName.SpotifyWeb);
                // start the launch process and pass the callback when complete
                return launchTrackPlayer((0, PlaylistDataManager_1.getSelectedPlayerName)(), callback);
            }
        }
        return;
    });
}
exports.showPlayerLaunchConfirmation = showPlayerLaunchConfirmation;
function checkDeviceLaunch(playerName_1) {
    return __awaiter(this, arguments, void 0, function* (playerName, tries = 5, callback) {
        setTimeout(() => __awaiter(this, void 0, void 0, function* () {
            yield (0, PlaylistDataManager_1.populateSpotifyDevices)(true /*retry*/);
            const devices = (0, PlaylistDataManager_1.getCurrentDevices)();
            if ((!devices || devices.length == 0) && tries >= 0) {
                tries--;
                checkDeviceLaunch(playerName, tries, callback);
            }
            else {
                const device = (0, PlaylistDataManager_1.getBestActiveDevice)();
                if (!device && !(0, DeviceManager_1.isMac)()) {
                    vscode_1.window.showInformationMessage("Unable to detect a connected Spotify device. Please make sure you are logged into your account.");
                }
                vscode_1.commands.executeCommand("musictime.refreshDeviceInfo");
                if (callback) {
                    callback();
                }
            }
        }), 1100);
    });
}
function checkPlayingState(deviceId_1) {
    return __awaiter(this, arguments, void 0, function* (deviceId, tries = 3) {
        tries--;
        const playerContext = yield (0, PlaylistDataManager_1.getPlayerContext)();
        // is_playing is true whether the track is paused or playing
        if (!playerContext || !playerContext.is_playing) {
            if (tries >= 0) {
                setTimeout(() => {
                    checkPlayingState(deviceId, tries);
                }, 2000);
                return;
            }
            else {
                // try to play it
                yield (0, cody_music_1.transferSpotifyDevice)(deviceId, true);
                (0, cody_music_1.play)((0, PlaylistDataManager_1.getSelectedPlayerName)());
            }
        }
        // get the selected track and execute post play commands like 'repeat'
        setTimeout(() => {
            const trackItem = (0, PlaylistDataManager_1.getSelectedTrackItem)();
            if (trackItem && trackItem['repeat']) {
                MusicControlManager_1.MusicControlManager.getInstance().setRepeatTrackOn();
            }
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 1000);
    });
}
function playSelectedTrackItems() {
    return __awaiter(this, void 0, void 0, function* () {
        const selectedTrackItems = (0, PlaylistDataManager_1.getSelectedTrackItems)();
        const device = (0, PlaylistDataManager_1.getBestActiveDevice)();
        const uris = selectedTrackItems.map((item) => {
            let track_id = item.id ? item.id : item["song_id"];
            if (track_id && !track_id.includes("spotify:track:")) {
                track_id = `spotify:track:${track_id}`;
            }
            return track_id;
        });
        (0, cody_music_1.play)(cody_music_1.PlayerName.SpotifyWeb, { device_id: device === null || device === void 0 ? void 0 : device.id, uris, offset: 0 });
        setTimeout(() => {
            checkPlayingState(device.id);
        }, 1500);
    });
}
function playMusicSelection() {
    return __awaiter(this, void 0, void 0, function* () {
        const selectedPlaylistItem = (0, PlaylistDataManager_1.getSelectedTrackItem)();
        if (!selectedPlaylistItem) {
            return;
        }
        const musicCommandUtil = MusicCommandUtil_1.MusicCommandUtil.getInstance();
        // get the playlist id, track id, and device id
        const device = (0, PlaylistDataManager_1.getBestActiveDevice)();
        const playlist_id = (0, PlaylistDataManager_1.getSelectedPlaylistId)();
        const selectedPlayer = (0, PlaylistDataManager_1.getSelectedPlayerName)() || cody_music_1.PlayerName.SpotifyWeb;
        const isLikedSong = !!(playlist_id === Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID);
        const desktopSelected = !!(selectedPlayer === cody_music_1.PlayerName.SpotifyDesktop);
        const isRecommendationTrack = !!(selectedPlaylistItem.type === "recommendation" ||
            selectedPlaylistItem["playlist_id"] === Constants_1.RECOMMENDATION_PLAYLIST_ID);
        const isRankedTrack = !!(selectedPlaylistItem["rank"]);
        const songId = selectedPlaylistItem.id ? selectedPlaylistItem.id : selectedPlaylistItem["song_id"];
        const trackId = (0, Util_1.createSpotifyIdFromUri)(songId);
        const trackUri = (0, Util_1.createUriFromTrackId)(songId);
        let result = undefined;
        if (isRecommendationTrack || isLikedSong || isRankedTrack) {
            try {
                if (isRankedTrack) {
                    (0, cody_music_1.play)(cody_music_1.PlayerName.SpotifyWeb, { device_id: device === null || device === void 0 ? void 0 : device.id, uris: [trackUri], offset: 0 });
                }
                else if (isRecommendationTrack) {
                    const recommendationTrackUris = (0, PlaylistDataManager_1.getRecommendationURIsFromTrackId)(trackId);
                    (0, cody_music_1.play)(cody_music_1.PlayerName.SpotifyWeb, { device_id: device === null || device === void 0 ? void 0 : device.id, uris: recommendationTrackUris, offset: 0 });
                }
                else {
                    const likedTrackUris = (0, PlaylistDataManager_1.getLikedURIsFromTrackId)(trackId);
                    (0, cody_music_1.play)(cody_music_1.PlayerName.SpotifyWeb, { device_id: device === null || device === void 0 ? void 0 : device.id, uris: likedTrackUris, offset: 0 });
                }
            }
            catch (e) {
                (0, Util_1.logIt)(`Unable to play the selected track: ${e.message}`, true);
            }
        }
        else {
            if ((0, DeviceManager_1.isMac)() && desktopSelected) {
                // play it using applescript
                const playlistUri = (0, Util_1.createUriFromPlaylistId)(playlist_id);
                const params = [trackUri, playlistUri];
                try {
                    result = yield (0, cody_music_1.playTrackInContext)(selectedPlayer, params);
                }
                catch (e) {
                    (0, Util_1.logIt)(`Unable to play the selected track: ${e.message}`, true);
                }
            }
            if (!result || result !== "ok") {
                // try with the web player
                result = yield musicCommandUtil.runSpotifyCommand(cody_music_1.playSpotifyPlaylist, [playlist_id, trackId, device === null || device === void 0 ? void 0 : device.id]);
            }
        }
        setTimeout(() => {
            checkPlayingState(device.id);
        }, 1500);
    });
}
function getNextOrPrevLikedIndex(get_next) {
    return __awaiter(this, void 0, void 0, function* () {
        const likedSongs = yield (0, PlaylistDataManager_1.getCachedLikedSongsTracks)();
        const selectedTrack = (0, PlaylistDataManager_1.getSelectedTrackItem)();
        const nextIdx = likedSongs === null || likedSongs === void 0 ? void 0 : likedSongs.findIndex((n) => n.id === selectedTrack.id);
        if (get_next) {
            // get next
            if (nextIdx + 1 >= likedSongs.length) {
                return 0;
            }
            return nextIdx + 1;
        }
        // get prev
        if (nextIdx - 1 < 0) {
            return likedSongs.length - 1;
        }
        else {
            return nextIdx - 1;
        }
    });
}
//# sourceMappingURL=PlaylistControlManager.js.map