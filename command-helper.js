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
exports.createCommands = void 0;
const vscode_1 = require("vscode");
const MusicControlManager_1 = require("./music/MusicControlManager");
const Util_1 = require("./Util");
const cody_music_1 = require("cody-music");
const SocialShareManager_1 = require("./social/SocialShareManager");
const RecTypeSelectorManager_1 = require("./selector/RecTypeSelectorManager");
const SortPlaylistSelectorManager_1 = require("./selector/SortPlaylistSelectorManager");
const SpotifyDeviceSelectorManager_1 = require("./selector/SpotifyDeviceSelectorManager");
const MusicCommandUtil_1 = require("./music/MusicCommandUtil");
const SearchSelectorManager_1 = require("./selector/SearchSelectorManager");
const SpotifyManager_1 = require("./managers/SpotifyManager");
const UserStatusManager_1 = require("./managers/UserStatusManager");
const MusicTimeWebviewSidebar_1 = require("./sidebar/MusicTimeWebviewSidebar");
const Constants_1 = require("./Constants");
const PlaylistDataManager_1 = require("./managers/PlaylistDataManager");
const PlaylistControlManager_1 = require("./managers/PlaylistControlManager");
const Constants_2 = require("./Constants");
const DataController_1 = require("./DataController");
const MusicCommandManager_1 = require("./music/MusicCommandManager");
const queryString = require("query-string");
/**
 * add the commands to vscode....
 */
function createCommands(ctx) {
    const cmds = [];
    const controller = MusicControlManager_1.MusicControlManager.getInstance();
    // DISPLAY README CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.launchReadme", () => {
        (0, DataController_1.displayReadmeIfNotExists)(true /*override*/);
    }));
    // PLAY NEXT CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.next", () => __awaiter(this, void 0, void 0, function* () {
        yield controller.nextSong();
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    // PLAY PREV CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.previous", () => __awaiter(this, void 0, void 0, function* () {
        yield controller.previousSong();
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    // PLAY CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.play", () => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedTrackStatus)(cody_music_1.TrackStatus.Playing);
        controller.playSong(1);
    })));
    // MUTE CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.mute", () => __awaiter(this, void 0, void 0, function* () {
        controller.setMuteOn();
    })));
    // UNMUTE CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.unMute", () => __awaiter(this, void 0, void 0, function* () {
        controller.setMuteOff();
    })));
    // REMOVE TRACK CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.removeTrack", (p) => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.removeTrackFromPlaylist)(p);
    })));
    // SHARE CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.shareTrack", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        SocialShareManager_1.SocialShareManager.getInstance().showMenu(trackItem.id, trackItem.name, false);
    })));
    // SEARCH CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.searchTracks", () => {
        // show the search input popup
        (0, SearchSelectorManager_1.showSearchInput)();
    }));
    // PAUSE CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.pause", () => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedTrackStatus)(cody_music_1.TrackStatus.Paused);
        yield controller.pauseSong();
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    // LIKE CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.like", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        yield controller.setLiked(trackItem, true);
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    // UNLIKE CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.unlike", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        yield controller.setLiked(trackItem, false);
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.shuffleOff", () => {
        controller.setShuffleOff();
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.shuffleOn", () => {
        controller.setShuffleOn();
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.muteOn", () => {
        controller.setMuteOn();
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.muteOff", () => {
        controller.setMuteOff();
    }));
    // REPEAT OFF CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.repeatOn", () => __awaiter(this, void 0, void 0, function* () {
        const trackItem = (0, PlaylistDataManager_1.getSelectedTrackItem)();
        if (trackItem) {
            trackItem['repeat'] = true;
            (0, PlaylistDataManager_1.updateSelectedTrackItem)(trackItem, cody_music_1.TrackStatus.Playing);
        }
        yield controller.setRepeatOnOff(true);
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.repeatTrack", () => __awaiter(this, void 0, void 0, function* () {
        const trackItem = (0, PlaylistDataManager_1.getSelectedTrackItem)();
        if (trackItem) {
            trackItem['repeat'] = true;
            (0, PlaylistDataManager_1.updateSelectedTrackItem)(trackItem, cody_music_1.TrackStatus.Playing);
            (0, PlaylistControlManager_1.playSelectedItem)(trackItem);
        }
        else {
            yield controller.setRepeatOnOff(true);
            setTimeout(() => {
                vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
            }, 500);
        }
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.repeatPlaylist", () => {
        controller.setRepeatPlaylistOn();
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    }));
    // REPEAT ON OFF CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.repeatOff", () => __awaiter(this, void 0, void 0, function* () {
        const trackItem = (0, PlaylistDataManager_1.getSelectedTrackItem)();
        if (trackItem) {
            trackItem['repeat'] = false;
            (0, PlaylistDataManager_1.updateSelectedTrackItem)(trackItem, cody_music_1.TrackStatus.Playing);
        }
        yield controller.setRepeatOnOff(false);
        setTimeout(() => {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }, 500);
    })));
    // SHOW MENU CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.menu", () => {
        controller.showMenu();
    }));
    // FOLLOW PLAYLIST CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.follow", (p) => {
        (0, PlaylistDataManager_1.followSpotifyPlaylist)(p);
    }));
    // DISPLAY CURRENT SONG CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.currentSong", () => {
        (0, PlaylistControlManager_1.launchTrackPlayer)();
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.songTitleRefresh", () => __awaiter(this, void 0, void 0, function* () {
        if (!(0, PlaylistDataManager_1.getBestActiveDevice)()) {
            yield (0, PlaylistDataManager_1.populateSpotifyDevices)(false);
        }
        setTimeout(() => __awaiter(this, void 0, void 0, function* () {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
            MusicCommandManager_1.MusicCommandManager.syncControls();
        }), 500);
    })));
    // SWITCH SPOTIFY
    cmds.push(vscode_1.commands.registerCommand("musictime.switchSpotifyAccount", () => __awaiter(this, void 0, void 0, function* () {
        (0, SpotifyManager_1.switchSpotifyAccount)();
    })));
    // CONNECT SPOTIFY CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.connectSpotify", () => __awaiter(this, void 0, void 0, function* () {
        const qryStr = queryString.stringify({
            plugin_uuid: (0, Util_1.getPluginUuid)(),
            plugin_id: (0, Util_1.getMusicTimePluginId)()
        });
        const url = `${Constants_2.app_endpoint}/code_time/integration_type/spotify}?${qryStr}`;
        (0, Util_1.launchWebUrl)(url);
    })));
    // CONNECT SLACK
    cmds.push(vscode_1.commands.registerCommand("musictime.connectSlack", () => {
        (0, Util_1.launchWebUrl)(`${Constants_2.app_endpoint}/code_time/integration_type/slack`);
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.connectSlackWorkspace", () => {
        (0, Util_1.launchWebUrl)(`${Constants_2.app_endpoint}/code_time/integration_type/slack`);
    }));
    // DISCONNECT SPOTIFY
    cmds.push(vscode_1.commands.registerCommand("musictime.disconnectSpotify", () => {
        (0, Util_1.launchWebUrl)(`${Constants_2.app_endpoint}/code_time/integration_type/spotify`);
    }));
    // DISCONNECT SLACK
    cmds.push(vscode_1.commands.registerCommand("musictime.disconnectSlack", () => {
        (0, Util_1.launchWebUrl)(`${Constants_2.app_endpoint}/code_time/integration_type/slack`);
    }));
    // this should only be attached to the refresh button
    cmds.push(vscode_1.commands.registerCommand("musictime.refreshDeviceInfo", () => __awaiter(this, void 0, void 0, function* () {
        if (!(yield (0, PlaylistDataManager_1.requiresSpotifyAccess)())) {
            yield (0, PlaylistDataManager_1.populateSpotifyDevices)(false);
        }
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.launchSpotify", () => {
        (0, PlaylistControlManager_1.launchTrackPlayer)(cody_music_1.PlayerName.SpotifyWeb);
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.launchSpotifyDesktop", () => {
        (0, PlaylistControlManager_1.launchTrackPlayer)(cody_music_1.PlayerName.SpotifyDesktop);
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.launchAnalytics", () => {
        (0, Util_1.launchMusicAnalytics)();
    }));
    const deviceSelectTransferCmd = vscode_1.commands.registerCommand("musictime.transferToDevice", (d) => __awaiter(this, void 0, void 0, function* () {
        // transfer to this device
        vscode_1.window.showInformationMessage(`Connected to ${d.name}`);
        yield MusicCommandUtil_1.MusicCommandUtil.getInstance().runSpotifyCommand(cody_music_1.playSpotifyDevice, [d.id]);
        setTimeout(() => {
            // refresh the tree, no need to refresh playlists
            vscode_1.commands.executeCommand("musictime.refreshDeviceInfo");
        }, 3000);
    }));
    cmds.push(deviceSelectTransferCmd);
    const genreRecListCmd = vscode_1.commands.registerCommand("musictime.songGenreSelector", () => {
        (0, RecTypeSelectorManager_1.showGenreSelections)();
    });
    cmds.push(genreRecListCmd);
    const categoryRecListCmd = vscode_1.commands.registerCommand("musictime.songMoodSelector", () => {
        (0, RecTypeSelectorManager_1.showMoodSelections)();
    });
    cmds.push(categoryRecListCmd);
    const deviceSelectorCmd = vscode_1.commands.registerCommand("musictime.deviceSelector", () => {
        (0, SpotifyDeviceSelectorManager_1.showDeviceSelectorMenu)();
    });
    cmds.push(deviceSelectorCmd);
    // UPDATE RECOMMENDATIONS CMD
    cmds.push(vscode_1.commands.registerCommand("musictime.updateRecommendations", (args) => {
        // there's always at least 3 args
        const label = args[0];
        const likedSongSeedLimit = args[1];
        const seed_genres = args[2];
        const features = args.length > 3 ? args[3] : {};
        (0, PlaylistDataManager_1.getRecommendations)(label, likedSongSeedLimit, seed_genres, features);
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.refreshRecommendations", () => {
        (0, PlaylistDataManager_1.refreshRecommendations)();
    }));
    // signup button click
    cmds.push(vscode_1.commands.registerCommand("musictime.signUpAccount", () => __awaiter(this, void 0, void 0, function* () {
        (0, UserStatusManager_1.showSignUpMenuOptions)();
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.logInAccount", () => __awaiter(this, void 0, void 0, function* () {
        (0, UserStatusManager_1.showLogInMenuOptions)();
    })));
    // login button click
    cmds.push(vscode_1.commands.registerCommand("musictime.googleLogin", () => __awaiter(this, void 0, void 0, function* () {
        (0, UserStatusManager_1.launchLogin)("google", true);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.githubLogin", () => __awaiter(this, void 0, void 0, function* () {
        (0, UserStatusManager_1.launchLogin)("github", true);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.emailSignup", () => __awaiter(this, void 0, void 0, function* () {
        (0, UserStatusManager_1.launchLogin)("software", false);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.emailLogin", () => __awaiter(this, void 0, void 0, function* () {
        (0, UserStatusManager_1.launchLogin)("software", true);
    })));
    // WEB VIEW PROVIDER
    const mtWebviewSidebar = new MusicTimeWebviewSidebar_1.MusicTimeWebviewSidebar(ctx.extensionUri);
    cmds.push(vscode_1.window.registerWebviewViewProvider("musictime.webView", mtWebviewSidebar, {
        webviewOptions: {
            retainContextWhenHidden: true,
        },
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.reInitializeSpotify", () => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.initializeSpotify)();
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.refreshMusicTimeView", (...args_1) => __awaiter(this, [...args_1], void 0, function* (payload = { refreshOpenFolder: true, playlistId: (0, PlaylistDataManager_1.getSelectedPlaylistId)(), tabView: (0, PlaylistDataManager_1.getSelectedTabView)() }) {
        let reload = false;
        if (payload.playlistId) {
            if ((0, PlaylistDataManager_1.getSelectedPlaylistId)() !== payload.playlistId) {
                yield (0, PlaylistDataManager_1.fetchTracksForPlaylist)(payload.playlistId);
            }
        }
        if (payload.tabView) {
            if ((0, PlaylistDataManager_1.getSelectedTabView)() !== payload.tabView) {
                reload = true;
            }
            (0, PlaylistDataManager_1.updateSelectedTabView)(payload.tabView);
        }
        const refreshOpenFolder = !!payload.refreshOpenFolder;
        mtWebviewSidebar.refresh(reload, refreshOpenFolder);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.reloadMusicTimeView", () => {
        mtWebviewSidebar.refresh(true);
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.submitAnIssue", () => {
        (0, Util_1.launchWebUrl)(Constants_2.vscode_mt_issues_url);
    }));
    // SORT TITLE COMMAND
    cmds.push(vscode_1.commands.registerCommand("musictime.sortIcon", () => {
        (0, SortPlaylistSelectorManager_1.showSortPlaylistMenu)();
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.sortAlphabetically", () => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSort)(true);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.sortToOriginal", () => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSort)(false);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.getTrackRecommendations", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        (0, PlaylistDataManager_1.getTrackRecommendations)(trackItem);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.getAudioFeatureRecommendations", () => __awaiter(this, void 0, void 0, function* () {
        const features = yield (0, PlaylistDataManager_1.getCachedFeaturesForRecomendations)();
        (0, PlaylistDataManager_1.getMixedAudioFeatureRecs)(features);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.showAlbum", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        (0, PlaylistDataManager_1.getAlbumForTrack)(trackItem);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.fetchPlaylistTracks", (playlist_id) => __awaiter(this, void 0, void 0, function* () {
        if (playlist_id === Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID) {
            (0, PlaylistDataManager_1.fetchTracksForLikedSongs)();
        }
        else {
            (0, PlaylistDataManager_1.fetchTracksForPlaylist)(playlist_id);
        }
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.updateSelectedPlaylist", (playlist_id) => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedPlaylistId)(playlist_id);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.playTrack", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        if (trackItem) {
            (0, PlaylistDataManager_1.updateSelectedPlaylistId)(trackItem["playlist_id"]);
            (0, PlaylistDataManager_1.updateSelectedTrackStatus)(cody_music_1.TrackStatus.Playing);
            (0, PlaylistControlManager_1.playSelectedItem)(trackItem);
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView", { tabView: 'playlists', playlistId: trackItem["playlist_id"], refreshOpenFolder: true });
        }
        else {
            vscode_1.commands.executeCommand("musictime.play");
        }
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.playPlaylist", (items) => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedPlaylistId)(null);
        (0, PlaylistControlManager_1.playSelectedItems)(items);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.playRecommendations", (payload) => __awaiter(this, void 0, void 0, function* () {
        const recs = (0, PlaylistDataManager_1.getCachedRecommendationInfo)();
        // find the track index
        const offset = recs.tracks.findIndex(n => {
            return n.id === payload.trackId;
        });
        const slicedTracks = [
            ...recs.tracks.slice(offset),
            ...recs.tracks.slice(0, offset)
        ];
        yield (0, PlaylistControlManager_1.playSelectedItems)(slicedTracks.slice(0, 100));
        setTimeout(() => __awaiter(this, void 0, void 0, function* () {
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }), 500);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.updateMetricSelection", (userMetricsSelection) => __awaiter(this, void 0, void 0, function* () {
        (0, PlaylistDataManager_1.updateSelectedMetricSelection)(userMetricsSelection);
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.tabSelection", (options) => __awaiter(this, void 0, void 0, function* () {
        const selectedTabView = (options === null || options === void 0 ? void 0 : options.tab_view) || 'playlists';
        if (selectedTabView === "recommendations") {
            // populate familiar recs, but don't refreshMusicTimeView
            // as the final logic will make that call
            yield (0, PlaylistDataManager_1.getCurrentRecommendations)();
        }
        else {
            // refresh the music time view
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView", { tabView: selectedTabView });
        }
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.installCodeTime", () => __awaiter(this, void 0, void 0, function* () {
        (0, Util_1.launchWebUrl)("vscode:extension/softwaredotcom.swdc-vscode");
    })));
    cmds.push(vscode_1.commands.registerCommand("musictime.displaySidebar", () => {
        // logic to open the sidebar (need to figure out how to reveal the sidebar webview)
        vscode_1.commands.executeCommand("workbench.view.extension.music-time-sidebar");
    }));
    cmds.push(vscode_1.commands.registerCommand("musictime.addToPlaylist", (payload) => __awaiter(this, void 0, void 0, function* () {
        const trackItem = yield getTrackByPayload(payload);
        controller.addToPlaylistMenu(trackItem);
    })));
    return vscode_1.Disposable.from(...cmds);
}
exports.createCommands = createCommands;
function getTrackByPayload() {
    return __awaiter(this, arguments, void 0, function* (payload = {}) {
        var _a;
        const playlistId = !(payload === null || payload === void 0 ? void 0 : payload.playlistId) ? (0, PlaylistDataManager_1.getSelectedPlaylistId)() : payload.playlistId;
        const trackId = !(payload === null || payload === void 0 ? void 0 : payload.trackId) ? (_a = (0, PlaylistDataManager_1.getSelectedTrackItem)()) === null || _a === void 0 ? void 0 : _a.id : payload.trackId;
        return yield (0, PlaylistDataManager_1.getTrackByPlaylistIdAndTrackId)(playlistId, trackId);
    });
}
//# sourceMappingURL=command-helper.js.map