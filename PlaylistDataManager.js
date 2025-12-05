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
var __asyncValues = (this && this.__asyncValues) || function (o) {
    if (!Symbol.asyncIterator) throw new TypeError("Symbol.asyncIterator is not defined.");
    var m = o[Symbol.asyncIterator], i;
    return m ? m.call(o) : (o = typeof __values === "function" ? __values(o) : o[Symbol.iterator](), i = {}, verb("next"), verb("throw"), verb("return"), i[Symbol.asyncIterator] = function () { return this; }, i);
    function verb(n) { i[n] = o[n] && function (v) { return new Promise(function (resolve, reject) { v = o[n](v), settle(resolve, reject, v.done, v.value); }); }; }
    function settle(resolve, reject, d, v) { Promise.resolve(v).then(function(v) { resolve({ value: v, done: d }); }, reject); }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getMixedAudioFeatureRecs = exports.getQuietMusicRecs = exports.getInstrumentalRecs = exports.getDanceableRecs = exports.getEnergeticRecs = exports.getHappyRecs = exports.getFamiliarRecs = exports.getCurrentRecommendations = exports.populateLikedSongs = exports.getAudioFeatures = exports.fetchTracksForPlaylist = exports.fetchTracksForLikedSongs = exports.getSoftwareTop40Playlist = exports.getSpotifyLikedPlaylist = exports.getSpotifyPlaylists = exports.getRecommendationURIsFromTrackId = exports.getLikedURIsFromTrackId = exports.isLikedSongPlaylistSelected = exports.getTrackByPlaylistIdAndTrackId = exports.getPlaylistById = exports.getUserMetricsSelected = exports.getSelectedTabView = exports.getSelectedTrackItems = exports.getSelectedTrackItem = exports.getSelectedPlayerName = exports.getExpandedPlaylistId = exports.getSelectedPlaylistId = exports.getCachedRunningTrack = exports.getPlayerContext = exports.getCachedRecommendationMetadata = exports.getCachedRecommendationInfo = exports.getCachedSoftwareTop40Playlist = exports.getCachedLikedSongsTracks = exports.sortingAlphabetically = exports.getCachedPlaylistTracks = exports.getCachedSpotifyPlaylists = exports.updateLikedStatusInPlaylist = exports.getCachedFeaturesForRecomendations = exports.getCachedAudioMetrics = exports.updateSort = exports.updateSelectedMetricSelection = exports.updateSelectedTabView = exports.updateSelectedPlayer = exports.updateExpandedPlaylistId = exports.updateSelectedPlaylistId = exports.updateSelectedTrackItems = exports.updateSelectedTrackItem = exports.updateSelectedTrackStatus = exports.addTrackToLikedPlaylist = exports.removeTrackFromLikedPlaylist = void 0;
exports.sortPlaylists = exports.createPlaylistItemFromTrack = exports.createSpotifyIdFromUri = exports.isLikedTrackId = exports.isLikedSong = exports.followSpotifyPlaylist = exports.removeTrackFromPlaylist = exports.isTrackRepeating = exports.initializeSpotify = exports.requiresSpotifyAccess = exports.populatePlayerContext = exports.getBestActiveDevice = exports.getDeviceMenuInfo = exports.getDeviceSet = exports.showReconnectPrompt = exports.requiresSpotifyReAuthentication = exports.getCurrentDevices = exports.populateSpotifyDevices = exports.removeTracksFromRecommendations = exports.populateRecommendationTracks = exports.getRecommendations = exports.refreshRecommendations = exports.getAlbumForTrack = exports.getTrackRecommendations = void 0;
const cody_music_1 = require("cody-music");
const vscode_1 = require("vscode");
const Constants_1 = require("../Constants");
const Constants_2 = require("../Constants");
const AudioFeatures_1 = require("../model/AudioFeatures");
const MusicCommandManager_1 = require("../music/MusicCommandManager");
const MusicCommandUtil_1 = require("../music/MusicCommandUtil");
const MusicControlManager_1 = require("../music/MusicControlManager");
const Util_1 = require("../Util");
const SpotifyManager_1 = require("./SpotifyManager");
const DeviceManager_1 = require("./DeviceManager");
let currentDevices = [];
let spotifyLikedTracks = undefined;
let spotifyPlaylists = undefined;
let softwareTop40Playlist = undefined;
let recommendedTracks = undefined;
const playlistTracks = {};
let selectedPlaylistId = undefined;
let expandedPlaylistId = '';
let selectedTrackItem = undefined;
let selectedTrackItems = undefined;
let cachedRunningTrack = undefined;
let spotifyContext = undefined;
let selectedPlayerName = cody_music_1.PlayerName.SpotifyWeb;
// playlists, recommendations, metrics
let selectedTabView = "playlists";
let metricsTypeSelected = "you";
let recommendationMetadata = undefined;
let recommendationInfo = undefined;
let sortAlphabetically = false;
let audioFeatures = undefined;
////////////////////////////////////////////////////////////////
// UPDATE EXPORTS
////////////////////////////////////////////////////////////////
function removeTrackFromLikedPlaylist(trackId) {
    spotifyLikedTracks = spotifyLikedTracks.filter((n) => n.id !== trackId);
}
exports.removeTrackFromLikedPlaylist = removeTrackFromLikedPlaylist;
function addTrackToLikedPlaylist(playlistItem) {
    playlistItem["liked"] = true;
    playlistItem["playlist_id"] = Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID;
    spotifyLikedTracks.unshift(playlistItem);
}
exports.addTrackToLikedPlaylist = addTrackToLikedPlaylist;
function updateSelectedTrackStatus(status) {
    if (selectedTrackItem) {
        selectedTrackItem.state = status;
    }
}
exports.updateSelectedTrackStatus = updateSelectedTrackStatus;
function updateSelectedTrackItem(item, status) {
    selectedTrackItem = item;
    selectedTrackItem.state = status;
    selectedPlaylistId = item["playlist_id"];
}
exports.updateSelectedTrackItem = updateSelectedTrackItem;
function updateSelectedTrackItems(items) {
    selectedTrackItems = items;
}
exports.updateSelectedTrackItems = updateSelectedTrackItems;
function updateSelectedPlaylistId(playlist_id) {
    selectedPlaylistId = playlist_id;
}
exports.updateSelectedPlaylistId = updateSelectedPlaylistId;
function updateExpandedPlaylistId(playlist_id) {
    expandedPlaylistId = playlist_id;
}
exports.updateExpandedPlaylistId = updateExpandedPlaylistId;
function updateSelectedPlayer(player) {
    selectedPlayerName = player;
}
exports.updateSelectedPlayer = updateSelectedPlayer;
function updateSelectedTabView(tabView) {
    selectedTabView = tabView;
}
exports.updateSelectedTabView = updateSelectedTabView;
function updateSelectedMetricSelection(type) {
    metricsTypeSelected = type;
}
exports.updateSelectedMetricSelection = updateSelectedMetricSelection;
function updateSort(alphabetically) {
    sortAlphabetically = alphabetically;
    sortPlaylists(spotifyPlaylists, alphabetically);
    vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
}
exports.updateSort = updateSort;
function getCachedAudioMetrics() {
    return __awaiter(this, void 0, void 0, function* () {
        if (!audioFeatures || Object.keys(audioFeatures).length === 0) {
            audioFeatures = new AudioFeatures_1.default(yield getAudioFeatures());
        }
        return audioFeatures.getMetrics();
    });
}
exports.getCachedAudioMetrics = getCachedAudioMetrics;
function getCachedFeaturesForRecomendations() {
    return __awaiter(this, void 0, void 0, function* () {
        yield getCachedAudioMetrics();
        return audioFeatures.getFeaturesForRecommendations();
    });
}
exports.getCachedFeaturesForRecomendations = getCachedFeaturesForRecomendations;
function updateLikedStatusInPlaylist(playlist_id, track_id, liked_state) {
    var _a, _b;
    let item = ((_a = playlistTracks[playlist_id]) === null || _a === void 0 ? void 0 : _a.length) ? playlistTracks[playlist_id].find((n) => n.id === track_id) : null;
    if (item) {
        item["liked"] = liked_state;
    }
    if (recommendationInfo === null || recommendationInfo === void 0 ? void 0 : recommendationInfo.tracks) {
        // it might be in the recommendations list
        item = (_b = recommendationInfo.tracks) === null || _b === void 0 ? void 0 : _b.find((n) => n.id === track_id);
        if (item) {
            item["liked"] = liked_state;
        }
    }
}
exports.updateLikedStatusInPlaylist = updateLikedStatusInPlaylist;
////////////////////////////////////////////////////////////////
// CACHE GETTERS
////////////////////////////////////////////////////////////////
function getCachedSpotifyPlaylists() {
    return __awaiter(this, void 0, void 0, function* () {
        if (!spotifyPlaylists || spotifyPlaylists.length === 0) {
            spotifyPlaylists = yield getSpotifyPlaylists();
        }
        return spotifyPlaylists;
    });
}
exports.getCachedSpotifyPlaylists = getCachedSpotifyPlaylists;
function getCachedPlaylistTracks() {
    return playlistTracks !== null && playlistTracks !== void 0 ? playlistTracks : {};
}
exports.getCachedPlaylistTracks = getCachedPlaylistTracks;
function sortingAlphabetically() {
    return sortAlphabetically;
}
exports.sortingAlphabetically = sortingAlphabetically;
function getCachedLikedSongsTracks() {
    return __awaiter(this, void 0, void 0, function* () {
        if (!spotifyLikedTracks || spotifyLikedTracks.length === 0) {
            yield populateLikedSongs();
        }
        return spotifyLikedTracks;
    });
}
exports.getCachedLikedSongsTracks = getCachedLikedSongsTracks;
function getCachedSoftwareTop40Playlist() {
    return __awaiter(this, void 0, void 0, function* () {
        if (!softwareTop40Playlist) {
            softwareTop40Playlist = yield getSoftwareTop40Playlist();
        }
        return softwareTop40Playlist;
    });
}
exports.getCachedSoftwareTop40Playlist = getCachedSoftwareTop40Playlist;
function getCachedRecommendationInfo() {
    return recommendationInfo;
}
exports.getCachedRecommendationInfo = getCachedRecommendationInfo;
function getCachedRecommendationMetadata() {
    return recommendationMetadata;
}
exports.getCachedRecommendationMetadata = getCachedRecommendationMetadata;
function getPlayerContext() {
    return __awaiter(this, void 0, void 0, function* () {
        return yield (0, cody_music_1.getSpotifyPlayerContext)();
    });
}
exports.getPlayerContext = getPlayerContext;
function getCachedRunningTrack() {
    return cachedRunningTrack;
}
exports.getCachedRunningTrack = getCachedRunningTrack;
function getSelectedPlaylistId() {
    return selectedPlaylistId;
}
exports.getSelectedPlaylistId = getSelectedPlaylistId;
function getExpandedPlaylistId() {
    return expandedPlaylistId;
}
exports.getExpandedPlaylistId = getExpandedPlaylistId;
function getSelectedPlayerName() {
    return selectedPlayerName;
}
exports.getSelectedPlayerName = getSelectedPlayerName;
function getSelectedTrackItem() {
    return selectedTrackItem;
}
exports.getSelectedTrackItem = getSelectedTrackItem;
function getSelectedTrackItems() {
    return selectedTrackItems;
}
exports.getSelectedTrackItems = getSelectedTrackItems;
function getSelectedTabView() {
    return selectedTabView;
}
exports.getSelectedTabView = getSelectedTabView;
function getUserMetricsSelected() {
    return metricsTypeSelected;
}
exports.getUserMetricsSelected = getUserMetricsSelected;
// only playlists (not liked or recommendations)
function getPlaylistById(playlist_id) {
    if (Constants_1.SOFTWARE_TOP_40_PLAYLIST_ID === playlist_id) {
        return softwareTop40Playlist;
    }
    return spotifyPlaylists === null || spotifyPlaylists === void 0 ? void 0 : spotifyPlaylists.find((n) => n.id === playlist_id);
}
exports.getPlaylistById = getPlaylistById;
function getTrackByPlaylistIdAndTrackId(playlist_id, track_id) {
    return __awaiter(this, void 0, void 0, function* () {
        if (!track_id) {
            // get the current spotify context
            const playerContext = yield getPlayerContext();
            if (playerContext === null || playerContext === void 0 ? void 0 : playerContext.item) {
                track_id = playerContext.item.id;
            }
        }
        let tracks = [];
        if (!playlist_id) {
            tracks.push(...yield getCachedLikedSongsTracks());
            tracks.push(...Object.keys(playlistTracks).map((key) => {
                return playlistTracks[key];
            }));
        }
        else if (playlist_id === Constants_1.RECOMMENDATION_PLAYLIST_ID) {
            tracks = recommendedTracks;
        }
        else if (playlist_id === Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID) {
            tracks = yield getCachedLikedSongsTracks();
        }
        else {
            tracks = playlistTracks[playlist_id];
        }
        if (tracks === null || tracks === void 0 ? void 0 : tracks.length) {
            const trackItem = tracks.find(n => { return n.id === track_id; });
            if (trackItem) {
                return trackItem;
            }
        }
        const currentTrack = yield (0, cody_music_1.getRunningTrack)();
        if (currentTrack) {
            return createPlaylistItemFromTrack(currentTrack);
        }
        return null;
    });
}
exports.getTrackByPlaylistIdAndTrackId = getTrackByPlaylistIdAndTrackId;
function isLikedSongPlaylistSelected() {
    return !!(selectedPlaylistId === Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID);
}
exports.isLikedSongPlaylistSelected = isLikedSongPlaylistSelected;
function getLikedURIsFromTrackId(trackId) {
    return getTracksFromTrackId(trackId, spotifyLikedTracks);
}
exports.getLikedURIsFromTrackId = getLikedURIsFromTrackId;
function getRecommendationURIsFromTrackId(trackId) {
    return getTracksFromTrackId(trackId, recommendationInfo === null || recommendationInfo === void 0 ? void 0 : recommendationInfo.tracks);
}
exports.getRecommendationURIsFromTrackId = getRecommendationURIsFromTrackId;
function createUriFromTrackId(track_id) {
    if (track_id && !track_id.includes("spotify:track:")) {
        track_id = `spotify:track:${track_id}`;
    }
    return track_id;
}
function getTracksFromTrackId(trackId, existingTracks) {
    const uris = [];
    let foundTrack = false;
    if (existingTracks === null || existingTracks === void 0 ? void 0 : existingTracks.length) {
        for (const track of existingTracks) {
            if (!foundTrack && track.id === trackId) {
                foundTrack = true;
            }
            if (foundTrack) {
                uris.push(createUriFromTrackId(track.id));
            }
        }
    }
    if ((existingTracks === null || existingTracks === void 0 ? void 0 : existingTracks.length) && uris.length < 10) {
        const limit = 10;
        // add the ones to the beginning until we've reached 10 or the found track
        let idx = 0;
        for (const track of existingTracks) {
            if (idx >= 10 || (!foundTrack && track.id === trackId)) {
                break;
            }
            uris.push(createUriFromTrackId(track.id));
            idx++;
        }
    }
    return uris;
}
////////////////////////////////////////////////////////////////
// PLAYLIST AND TRACK EXPORTS
////////////////////////////////////////////////////////////////
// PLAYLISTS
function getSpotifyPlaylists() {
    return __awaiter(this, arguments, void 0, function* (clear = false) {
        if (yield requiresSpotifyAccess()) {
            return [];
        }
        if (!clear && (spotifyPlaylists === null || spotifyPlaylists === void 0 ? void 0 : spotifyPlaylists.length)) {
            return spotifyPlaylists;
        }
        try {
            spotifyPlaylists = yield (0, cody_music_1.getPlaylists)(cody_music_1.PlayerName.SpotifyWeb, { all: true });
        }
        catch (e) {
            (0, Util_1.logIt)(`Error fetching playlists. ${e.message}`);
        }
        spotifyPlaylists = spotifyPlaylists === null || spotifyPlaylists === void 0 ? void 0 : spotifyPlaylists.map((n, index) => {
            return Object.assign(Object.assign({}, n), { index });
        });
        return spotifyPlaylists;
    });
}
exports.getSpotifyPlaylists = getSpotifyPlaylists;
// LIKED SONGS
function getSpotifyLikedPlaylist() {
    const item = new cody_music_1.PlaylistItem();
    item.type = "playlist";
    item.id = Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID;
    item.tracks = new cody_music_1.PlaylistTrackInfo();
    // set a number so it shows up
    item.tracks.total = 1;
    item.playerType = cody_music_1.PlayerType.WebSpotify;
    item.tag = "spotify-liked-songs";
    item.itemType = "playlist";
    item.name = Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_NAME;
    return item;
}
exports.getSpotifyLikedPlaylist = getSpotifyLikedPlaylist;
// SOFTWARE TOP 40
function getSoftwareTop40Playlist() {
    return __awaiter(this, void 0, void 0, function* () {
        softwareTop40Playlist = yield (0, cody_music_1.getSpotifyPlaylist)(Constants_1.SOFTWARE_TOP_40_PLAYLIST_ID);
        if (softwareTop40Playlist && softwareTop40Playlist.tracks && softwareTop40Playlist.tracks["items"]) {
            softwareTop40Playlist.tracks["items"] = softwareTop40Playlist.tracks["items"].map((n) => {
                const albumName = getAlbumName(n.track);
                const description = getArtistAlbumDescription(n.track);
                n.track = Object.assign(Object.assign({}, n.track), { albumName, description, playlist_id: Constants_1.SOFTWARE_TOP_40_PLAYLIST_ID });
                return Object.assign({}, n);
            });
        }
        return softwareTop40Playlist;
    });
}
exports.getSoftwareTop40Playlist = getSoftwareTop40Playlist;
// LIKED PLAYLIST TRACKS
function fetchTracksForLikedSongs() {
    return __awaiter(this, void 0, void 0, function* () {
        selectedPlaylistId = Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID;
        if (!spotifyLikedTracks) {
            yield populateLikedSongs();
        }
        // refresh the webview
        vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
    });
}
exports.fetchTracksForLikedSongs = fetchTracksForLikedSongs;
// TRACKS FOR A SPECIFIED PLAYLIST
function fetchTracksForPlaylist(playlist_id) {
    return __awaiter(this, void 0, void 0, function* () {
        var _a, e_1, _b, _c;
        updateSelectedPlaylistId(playlist_id);
        if (!playlistTracks[playlist_id] && playlist_id !== Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID) {
            const results = yield (0, cody_music_1.getPlaylistTracks)(cody_music_1.PlayerName.SpotifyWeb, playlist_id);
            const tracks = yield getPlaylistItemTracksFromCodyResponse(results);
            // add the playlist id to the tracks
            if (tracks === null || tracks === void 0 ? void 0 : tracks.length) {
                try {
                    for (var _d = true, tracks_1 = __asyncValues(tracks), tracks_1_1; tracks_1_1 = yield tracks_1.next(), _a = tracks_1_1.done, !_a; _d = true) {
                        _c = tracks_1_1.value;
                        _d = false;
                        const t = _c;
                        const albumName = getAlbumName(t);
                        const description = getArtistAlbumDescription(t);
                        t["playlist_id"] = playlist_id;
                        t["albumName"] = albumName;
                        t["description"] = description;
                        t["liked"] = yield isLikedSong(t);
                    }
                }
                catch (e_1_1) { e_1 = { error: e_1_1 }; }
                finally {
                    try {
                        if (!_d && !_a && (_b = tracks_1.return)) yield _b.call(tracks_1);
                    }
                    finally { if (e_1) throw e_1.error; }
                }
            }
            playlistTracks[playlist_id] = tracks;
        }
        else if (playlist_id === Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID) {
            yield getCachedLikedSongsTracks();
        }
    });
}
exports.fetchTracksForPlaylist = fetchTracksForPlaylist;
////////////////////////////////////////////////////////////////
// METRICS EXPORTS
////////////////////////////////////////////////////////////////
function getAudioFeatures() {
    return __awaiter(this, void 0, void 0, function* () {
        const ids = (yield getCachedLikedSongsTracks()).map((n) => {
            return n.id;
        });
        return yield (0, cody_music_1.getSpotifyAudioFeatures)(ids.slice(0, 100));
    });
}
exports.getAudioFeatures = getAudioFeatures;
function populateLikedSongs() {
    return __awaiter(this, void 0, void 0, function* () {
        var _a;
        const tracks = (_a = (yield (0, cody_music_1.getSpotifyLikedSongs)())) !== null && _a !== void 0 ? _a : [];
        // add the playlist id to the tracks
        if (tracks === null || tracks === void 0 ? void 0 : tracks.length) {
            spotifyLikedTracks = tracks.map((t, idx) => {
                const playlistItem = createPlaylistItemFromTrack(t, idx);
                playlistItem["playlist_id"] = Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID;
                playlistItem["liked"] = true;
                return playlistItem;
            });
        }
    });
}
exports.populateLikedSongs = populateLikedSongs;
////////////////////////////////////////////////////////////////
// RECOMMENDATION TRACKS EXPORTS
////////////////////////////////////////////////////////////////
function getCurrentRecommendations() {
    if (recommendationMetadata) {
        getRecommendations(recommendationMetadata.length, recommendationMetadata.seedLimit, recommendationMetadata.seed_genres, recommendationMetadata.features, 0);
    }
    else {
        getFamiliarRecs();
    }
}
exports.getCurrentRecommendations = getCurrentRecommendations;
function getFamiliarRecs() {
    return getRecommendations("Familiar", 5);
}
exports.getFamiliarRecs = getFamiliarRecs;
function getHappyRecs() {
    return getRecommendations("Happy", 5, [], { min_valence: 0.7, target_valence: 1 });
}
exports.getHappyRecs = getHappyRecs;
function getEnergeticRecs() {
    return getRecommendations("Energetic", 5, [], { min_energy: 0.7, target_energy: 1 });
}
exports.getEnergeticRecs = getEnergeticRecs;
function getDanceableRecs() {
    return getRecommendations("Danceable", 5, [], { min_danceability: 0.5, target_danceability: 1 });
}
exports.getDanceableRecs = getDanceableRecs;
function getInstrumentalRecs() {
    return getRecommendations("Instrumental", 5, [], { min_instrumentalness: 0.6, target_instrumentalness: 1 });
}
exports.getInstrumentalRecs = getInstrumentalRecs;
function getQuietMusicRecs() {
    return getRecommendations("Quiet music", 5, [], { min_loudness: -40, target_loudness: 0 });
}
exports.getQuietMusicRecs = getQuietMusicRecs;
function getMixedAudioFeatureRecs(features) {
    if (!features) {
        // fetch familiar
        getFamiliarRecs();
        return;
    }
    return getRecommendations("Audio mix", 5, [], features);
}
exports.getMixedAudioFeatureRecs = getMixedAudioFeatureRecs;
function getTrackRecommendations(playlistItem) {
    return getRecommendations(playlistItem.name, 5, [], {}, 0, [playlistItem]);
}
exports.getTrackRecommendations = getTrackRecommendations;
function getAlbumForTrack(playlistItem) {
    return __awaiter(this, void 0, void 0, function* () {
        var _a, e_2, _b, _c;
        let albumId = playlistItem["albumId"];
        const albumName = playlistItem["album"] ? playlistItem["album"]["name"] : "";
        if (!albumId && playlistItem["album"]) {
            albumId = playlistItem["album"]["id"];
        }
        if (albumId) {
            const albumTracks = yield (0, cody_music_1.getSpotifyAlbumTracks)(albumId);
            const items = [];
            if (albumTracks === null || albumTracks === void 0 ? void 0 : albumTracks.length) {
                let idx = 1;
                try {
                    for (var _d = true, albumTracks_1 = __asyncValues(albumTracks), albumTracks_1_1; albumTracks_1_1 = yield albumTracks_1.next(), _a = albumTracks_1_1.done, !_a; _d = true) {
                        _c = albumTracks_1_1.value;
                        _d = false;
                        const t = _c;
                        const playlistItem = createPlaylistItemFromTrack(t, idx);
                        if (!t["albumName"]) {
                            t["albumName"] = albumName;
                        }
                        playlistItem["liked"] = yield isLikedSong(t);
                        idx++;
                        items.push(playlistItem);
                    }
                }
                catch (e_2_1) { e_2 = { error: e_2_1 }; }
                finally {
                    try {
                        if (!_d && !_a && (_b = albumTracks_1.return)) yield _b.call(albumTracks_1);
                    }
                    finally { if (e_2) throw e_2.error; }
                }
            }
            populateRecommendationTracks(playlistItem["albumName"], items);
        }
    });
}
exports.getAlbumForTrack = getAlbumForTrack;
function refreshRecommendations() {
    if (!recommendationInfo) {
        return getFamiliarRecs();
    }
    else {
        let offset = (recommendationMetadata.offset += 5);
        if (offset.length - 5 < offset) {
            // start back at the beginning
            offset = 0;
        }
        getRecommendations(recommendationMetadata.label, recommendationMetadata.seedLimit, recommendationMetadata.seed_genres, recommendationMetadata.features, offset);
    }
}
exports.refreshRecommendations = refreshRecommendations;
function getRecommendations() {
    return __awaiter(this, arguments, void 0, function* (label = "Familiar", seedLimit = 5, seed_genres = [], features = {}, offset = 0, seedTracks = []) {
        // fetching recommendations based on a set of genre requires 0 seed track IDs
        seedLimit = seed_genres.length ? 0 : Math.max(seedLimit, 5);
        recommendationMetadata = {
            label,
            seedLimit,
            seed_genres,
            features,
            offset,
        };
        recommendedTracks = yield getTrackIdsForRecommendations(seedLimit, seedTracks, offset).then((trackIds) => __awaiter(this, void 0, void 0, function* () {
            var _a, e_3, _b, _c;
            const tracks = yield (0, cody_music_1.getRecommendationsForTracks)(trackIds, Constants_1.RECOMMENDATION_LIMIT, "" /*market*/, 20, 100, seed_genres, [] /*artists*/, features);
            const items = [];
            if (tracks === null || tracks === void 0 ? void 0 : tracks.length) {
                let idx = 1;
                try {
                    for (var _d = true, tracks_2 = __asyncValues(tracks), tracks_2_1; tracks_2_1 = yield tracks_2.next(), _a = tracks_2_1.done, !_a; _d = true) {
                        _c = tracks_2_1.value;
                        _d = false;
                        const t = _c;
                        const playlistItem = createPlaylistItemFromTrack(t, idx);
                        playlistItem["playlist_id"] = Constants_1.RECOMMENDATION_PLAYLIST_ID;
                        playlistItem["liked"] = yield isLikedSong(t);
                        items.push(playlistItem);
                        idx++;
                    }
                }
                catch (e_3_1) { e_3 = { error: e_3_1 }; }
                finally {
                    try {
                        if (!_d && !_a && (_b = tracks_2.return)) yield _b.call(tracks_2);
                    }
                    finally { if (e_3) throw e_3.error; }
                }
            }
            return items;
        }));
        populateRecommendationTracks(label, recommendedTracks);
    });
}
exports.getRecommendations = getRecommendations;
function populateRecommendationTracks(label, tracks) {
    if (tracks === null || tracks === void 0 ? void 0 : tracks.length) {
        tracks = tracks.map((t) => {
            t["playlist_id"] = Constants_1.RECOMMENDATION_PLAYLIST_ID;
            const albumName = getAlbumName(t);
            const description = getArtistAlbumDescription(t);
            return Object.assign(Object.assign({}, t), { albumName, description });
        });
    }
    selectedPlaylistId = Constants_1.RECOMMENDATION_PLAYLIST_ID;
    recommendationInfo = {
        label,
        tracks,
    };
    // refresh the webview
    vscode_1.commands.executeCommand("musictime.refreshMusicTimeView", { tabView: "recommendations", playlistId: Constants_1.RECOMMENDATION_PLAYLIST_ID });
}
exports.populateRecommendationTracks = populateRecommendationTracks;
function removeTracksFromRecommendations(trackId) {
    let foundIdx = -1;
    for (let i = 0; i < recommendationInfo.tracks.length; i++) {
        if (recommendationInfo.tracks[i].id === trackId) {
            foundIdx = i;
            break;
        }
    }
    if (foundIdx > -1) {
        // splice it out
        recommendationInfo.tracks.splice(foundIdx, 1);
    }
    if (recommendationInfo.tracks.length < 2) {
        // refresh
        vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
    }
}
exports.removeTracksFromRecommendations = removeTracksFromRecommendations;
////////////////////////////////////////////////////////////////
// DEVICE EXPORTS
////////////////////////////////////////////////////////////////
// POPULATE
function populateSpotifyDevices() {
    return __awaiter(this, arguments, void 0, function* (tryAgain = false) {
        const devices = yield MusicCommandUtil_1.MusicCommandUtil.getInstance().runSpotifyCommand(cody_music_1.getSpotifyDevices);
        if (devices.status && devices.status === 429 && tryAgain) {
            // try one more time in lazily since its not a device launch request.
            // the device launch requests retries a few times every couple seconds.
            setTimeout(() => {
                // use true to specify its a device launch so this doens't try continuously
                populateSpotifyDevices(false);
            }, 5000);
            return;
        }
        const fetchedDeviceIds = [];
        if (devices.length) {
            devices.forEach((el) => {
                fetchedDeviceIds.push(el.id);
            });
        }
        let diffDevices = [];
        if (currentDevices.length) {
            // get any differences from the fetched devices if any
            diffDevices = currentDevices.filter((n) => !fetchedDeviceIds.includes(n.id));
        }
        else if (fetchedDeviceIds.length) {
            // no current devices, set diff to whatever we fetched
            diffDevices = [...devices];
        }
        if (diffDevices.length || currentDevices.length !== diffDevices.length) {
            // new devices available or setting to empty
            currentDevices = devices;
        }
    });
}
exports.populateSpotifyDevices = populateSpotifyDevices;
function getCurrentDevices() {
    return currentDevices;
}
exports.getCurrentDevices = getCurrentDevices;
function requiresSpotifyReAuthentication() {
    const requiresSpotifyReAuth = (0, Util_1.getItem)("requiresSpotifyReAuth");
    return requiresSpotifyReAuth ? true : false;
}
exports.requiresSpotifyReAuthentication = requiresSpotifyReAuthentication;
function showReconnectPrompt(email) {
    return __awaiter(this, void 0, void 0, function* () {
        const reconnectButtonLabel = "Reconnect";
        const msg = `To continue using Music Time, please reconnect your Spotify account (${email}).`;
        const selection = yield vscode_1.window.showInformationMessage(msg, ...[reconnectButtonLabel]);
        if (selection === reconnectButtonLabel) {
            // now launch re-auth
            (0, Util_1.launchWebUrl)(`${Constants_2.app_endpoint}/code_time/integration_type/spotify`);
        }
    });
}
exports.showReconnectPrompt = showReconnectPrompt;
/**
 * returns { webPlayer, desktop, activeDevice, activeComputerDevice, activeWebPlayerDevice }
 * Either of these values can be null
 */
function getDeviceSet() {
    const webPlayer = currentDevices === null || currentDevices === void 0 ? void 0 : currentDevices.find((d) => d.name.toLowerCase().includes("web player"));
    const desktop = currentDevices === null || currentDevices === void 0 ? void 0 : currentDevices.find((d) => d.type.toLowerCase() === "computer" && !d.name.toLowerCase().includes("web player"));
    const activeDevice = currentDevices === null || currentDevices === void 0 ? void 0 : currentDevices.find((d) => d.is_active);
    const activeComputerDevice = currentDevices === null || currentDevices === void 0 ? void 0 : currentDevices.find((d) => d.is_active && d.type.toLowerCase() === "computer");
    const activeWebPlayerDevice = currentDevices === null || currentDevices === void 0 ? void 0 : currentDevices.find((d) => d.is_active && d.type.toLowerCase() === "computer" && d.name.toLowerCase().includes("web player"));
    const activeDesktopPlayerDevice = currentDevices === null || currentDevices === void 0 ? void 0 : currentDevices.find((d) => d.is_active && d.type.toLowerCase() === "computer" && !d.name.toLowerCase().includes("web player"));
    const deviceData = {
        webPlayer,
        desktop,
        activeDevice,
        activeComputerDevice,
        activeWebPlayerDevice,
        activeDesktopPlayerDevice,
    };
    return deviceData;
}
exports.getDeviceSet = getDeviceSet;
function getDeviceMenuInfo() {
    var _a;
    const { webPlayer, desktop, activeDevice, activeComputerDevice, activeWebPlayerDevice } = getDeviceSet();
    const devices = (_a = getCurrentDevices()) !== null && _a !== void 0 ? _a : [];
    let primaryText = "";
    let secondaryText = "";
    let isActive = true;
    if (activeDevice) {
        // found an active device
        primaryText = `Listening on your ${activeDevice.name}`;
    }
    else if ((0, DeviceManager_1.isMac)() && desktop) {
        // show that the desktop player is an active device
        primaryText = `Listening on your ${desktop.name}`;
    }
    else if (webPlayer) {
        // show that the web player is an active device
        primaryText = `Listening on your ${webPlayer.name}`;
    }
    else if (desktop) {
        // show that the desktop player is an active device
        primaryText = `Listening on your ${desktop.name}`;
    }
    else if (devices.length) {
        // no active device but found devices
        const names = devices.map((d) => d.name);
        primaryText = `Spotify devices available`;
        secondaryText = `${names.join(", ")}`;
        isActive = false;
    }
    else if (devices.length === 0) {
        // no active device and no devices
        primaryText = "Connect to a Spotify device";
        secondaryText = "Launch the web or desktop player";
        isActive = false;
    }
    return { primaryText, secondaryText, isActive };
}
exports.getDeviceMenuInfo = getDeviceMenuInfo;
function getBestActiveDevice() {
    const { webPlayer, desktop, activeDevice } = getDeviceSet();
    const device = activeDevice ? activeDevice : desktop ? desktop : webPlayer ? webPlayer : null;
    return device;
}
exports.getBestActiveDevice = getBestActiveDevice;
////////////////////////////////////////////////////////////////
// PLAYER CONTEXT FUNCTIONS
////////////////////////////////////////////////////////////////
function populatePlayerContext() {
    return __awaiter(this, void 0, void 0, function* () {
        spotifyContext = yield (0, cody_music_1.getSpotifyPlayerContext)();
        MusicCommandManager_1.MusicCommandManager.syncControls();
    });
}
exports.populatePlayerContext = populatePlayerContext;
////////////////////////////////////////////////////////////////
// UTIL FUNCTIONS
////////////////////////////////////////////////////////////////
function requiresSpotifyAccess() {
    return __awaiter(this, void 0, void 0, function* () {
        const spotifyIntegration = yield (0, SpotifyManager_1.getSpotifyIntegration)();
        // no spotify access token then return true, the user requires spotify access
        return !spotifyIntegration ? true : false;
    });
}
exports.requiresSpotifyAccess = requiresSpotifyAccess;
function initializeSpotify() {
    return __awaiter(this, arguments, void 0, function* (reload = true) {
        // get the client id and secret
        yield (0, SpotifyManager_1.updateSpotifyClientInfo)();
        // ensure cody-music has the latest access token
        yield (0, SpotifyManager_1.updateCodyConfig)();
        // get the spotify user
        yield (0, SpotifyManager_1.populateSpotifyUser)(true);
        yield populateSpotifyDevices(false);
        // initialize the status bar music controls
        MusicCommandManager_1.MusicCommandManager.initialize();
        setTimeout(() => {
            if (reload) {
                vscode_1.commands.executeCommand("musictime.reloadMusicTimeView");
            }
            else {
                vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
            }
        }, 1000);
    });
}
exports.initializeSpotify = initializeSpotify;
function isTrackRepeating() {
    return __awaiter(this, void 0, void 0, function* () {
        // get the current repeat state
        if (!spotifyContext) {
            spotifyContext = yield (0, cody_music_1.getSpotifyPlayerContext)();
        }
        // "off", "track", "context", ""
        const repeatState = spotifyContext ? spotifyContext.repeat_state : "";
        return repeatState && repeatState === "track" ? true : false;
    });
}
exports.isTrackRepeating = isTrackRepeating;
function removeTrackFromPlaylist(trackItem) {
    return __awaiter(this, void 0, void 0, function* () {
        // get the playlist it's in
        const currentPlaylistId = trackItem["playlist_id"];
        const foundPlaylist = getPlaylistById(currentPlaylistId);
        if (foundPlaylist) {
            // if it's the liked songs, then send it to the setLiked(false) api
            if (foundPlaylist.id === Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_NAME) {
                const buttonSelection = yield vscode_1.window.showInformationMessage(`Are you sure you would like to remove '${trackItem.name}' from your '${Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_NAME}' playlist?`, ...[Constants_1.YES_LABEL]);
                if (buttonSelection === Constants_1.YES_LABEL) {
                    yield MusicControlManager_1.MusicControlManager.getInstance().setLiked(trackItem, false);
                }
            }
            else {
                // remove it from a playlist
                const tracks = [trackItem.id];
                const result = yield (0, cody_music_1.removeTracksFromPlaylist)(currentPlaylistId, tracks);
                const errMsg = (0, Util_1.getCodyErrorMessage)(result);
                if (errMsg) {
                    vscode_1.window.showInformationMessage(`Unable to remove the track from your playlist. ${errMsg}`);
                }
                else {
                    // remove it from the cached list
                    playlistTracks[currentPlaylistId] = playlistTracks[currentPlaylistId].filter((n) => n.id !== trackItem.id);
                    vscode_1.window.showInformationMessage("Song removed successfully");
                    vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
                }
            }
        }
    });
}
exports.removeTrackFromPlaylist = removeTrackFromPlaylist;
function followSpotifyPlaylist(playlist) {
    return __awaiter(this, void 0, void 0, function* () {
        const codyResp = yield (0, cody_music_1.followPlaylist)(playlist.id);
        if (codyResp.state === cody_music_1.CodyResponseType.Success) {
            vscode_1.window.showInformationMessage(`Successfully following the '${playlist.name}' playlist.`);
            // repopulate the playlists since we've changed the state of the playlist
            yield getSpotifyPlaylists();
            vscode_1.commands.executeCommand("musictime.refreshMusicTimeView");
        }
        else {
            vscode_1.window.showInformationMessage(`Unable to follow ${playlist.name}. ${codyResp.message}`, ...[Constants_1.OK_LABEL]);
        }
    });
}
exports.followSpotifyPlaylist = followSpotifyPlaylist;
function isLikedSong(song) {
    return __awaiter(this, void 0, void 0, function* () {
        if (!song) {
            return false;
        }
        const trackId = getSongId(song);
        if (!trackId) {
            return false;
        }
        if (!spotifyLikedTracks || spotifyLikedTracks.length === 0) {
            // fetch the liked tracks
            yield populateLikedSongs();
        }
        return !!(spotifyLikedTracks === null || spotifyLikedTracks === void 0 ? void 0 : spotifyLikedTracks.find((n) => n.id === trackId));
    });
}
exports.isLikedSong = isLikedSong;
function isLikedTrackId(trackId) {
    return __awaiter(this, void 0, void 0, function* () {
        if (!spotifyLikedTracks || spotifyLikedTracks.length === 0) {
            // fetch the liked tracks
            yield populateLikedSongs();
        }
        return !!(spotifyLikedTracks === null || spotifyLikedTracks === void 0 ? void 0 : spotifyLikedTracks.find((n) => n.id === trackId));
    });
}
exports.isLikedTrackId = isLikedTrackId;
////////////////////////////////////////////////////////////////
// PRIVATE FUNCTIONS
////////////////////////////////////////////////////////////////
function getSongId(song) {
    if (song.id) {
        return createSpotifyIdFromUri(song.id);
    }
    else if (song.uri) {
        return createSpotifyIdFromUri(song.uri);
    }
    else if (song.song_id) {
        return createSpotifyIdFromUri(song.song_id);
    }
    return null;
}
function createSpotifyIdFromUri(id) {
    if (id && id.indexOf("spotify:") === 0) {
        return id.substring(id.lastIndexOf(":") + 1);
    }
    return id;
}
exports.createSpotifyIdFromUri = createSpotifyIdFromUri;
function getPlaylistItemTracksFromCodyResponse(codyResponse) {
    return __awaiter(this, void 0, void 0, function* () {
        var _a, e_4, _b, _c;
        const playlistItems = [];
        if (codyResponse && codyResponse.state === cody_music_1.CodyResponseType.Success) {
            const paginationItem = codyResponse.data;
            if (paginationItem && paginationItem.items) {
                let idx = 1;
                try {
                    for (var _d = true, _e = __asyncValues(paginationItem.items), _f; _f = yield _e.next(), _a = _f.done, !_a; _d = true) {
                        _c = _f.value;
                        _d = false;
                        const t = _c;
                        const playlistItem = createPlaylistItemFromTrack(t, idx);
                        playlistItem["liked"] = yield isLikedSong(t);
                        playlistItems.push(playlistItem);
                        idx++;
                    }
                }
                catch (e_4_1) { e_4 = { error: e_4_1 }; }
                finally {
                    try {
                        if (!_d && !_a && (_b = _e.return)) yield _b.call(_e);
                    }
                    finally { if (e_4) throw e_4.error; }
                }
            }
        }
        return playlistItems;
    });
}
function createPlaylistItemFromTrack(track, position = undefined) {
    var _a;
    if (position === undefined) {
        position = track.track_number;
    }
    const playlistItem = new cody_music_1.PlaylistItem();
    playlistItem.type = "track";
    playlistItem.name = track.name;
    playlistItem.tooltip = getTrackTooltip(track);
    playlistItem.id = track.id;
    playlistItem.uri = track.uri;
    playlistItem.popularity = track.popularity;
    playlistItem.position = position;
    playlistItem.artist = getArtist(track);
    playlistItem.playerType = track.playerType;
    playlistItem.itemType = "track";
    playlistItem["albumId"] = (_a = track === null || track === void 0 ? void 0 : track.album) === null || _a === void 0 ? void 0 : _a.id;
    playlistItem["albumName"] = getAlbumName(track);
    playlistItem["description"] = getArtistAlbumDescription(track);
    delete playlistItem.tracks;
    return playlistItem;
}
exports.createPlaylistItemFromTrack = createPlaylistItemFromTrack;
function getTrackTooltip(track) {
    let tooltip = track.name;
    const artistName = getArtist(track);
    if (artistName) {
        tooltip += ` - ${artistName}`;
    }
    if (track.popularity) {
        tooltip += ` (Popularity: ${track.popularity})`;
    }
    return tooltip;
}
function getArtistAlbumDescription(track) {
    let artistName = getArtist(track);
    let albumName = getAlbumName(track);
    // return artist - album (but abbreviate both if the len is too large)
    if (artistName && albumName && artistName.length + albumName.length > 100) {
        // start abbreviating
        if (artistName.length > 50) {
            artistName = artistName.substring(0, 50) + "...";
        }
        if (albumName.length > 50) {
            albumName = albumName.substring(0, 50) + "...";
        }
    }
    return albumName ? `${artistName} - ${albumName}` : artistName;
}
function getArtist(track) {
    if (!track) {
        return null;
    }
    if (track.artist) {
        return track.artist;
    }
    if (track.artists && track.artists.length > 0) {
        const trackArtist = track.artists[0];
        return trackArtist.name;
    }
    return null;
}
function getTrackIdsForRecommendations() {
    return __awaiter(this, arguments, void 0, function* (seedLimit = 5, seedTracks = [], offset = 0) {
        if (seedLimit === 0) {
            return [];
        }
        if (!spotifyLikedTracks) {
            yield populateLikedSongs();
        }
        seedLimit = offset + seedLimit;
        // up until limit
        if (spotifyLikedTracks === null || spotifyLikedTracks === void 0 ? void 0 : spotifyLikedTracks.length) {
            if (offset > spotifyLikedTracks.length - 1) {
                offset = 0;
            }
            seedTracks.push(...spotifyLikedTracks.slice(offset, seedLimit));
        }
        const remainingLen = seedLimit - seedTracks.length;
        if (remainingLen < seedLimit) {
            // find a few more
            Object.keys(playlistTracks).every((playlist_id) => {
                if (playlist_id !== Constants_1.SPOTIFY_LIKED_SONGS_PLAYLIST_ID && playlistTracks[playlist_id] && playlistTracks[playlist_id].length >= remainingLen) {
                    seedTracks.push(...playlistTracks[playlist_id].splice(0, remainingLen));
                    return;
                }
            });
        }
        const trackIds = seedTracks.map((n) => n.id);
        return trackIds;
    });
}
function getAlbumName(track) {
    let albumName = track["albumName"];
    if (!albumName && track["album"] && track["album"].name) {
        albumName = track["album"].name;
    }
    return albumName;
}
function sortPlaylists(playlists, alphabetically = sortAlphabetically) {
    if (playlists && playlists.length > 0) {
        playlists.sort((a, b) => {
            if (alphabetically) {
                const nameA = a.name.toLowerCase(), nameB = b.name.toLowerCase();
                if (nameA < nameB)
                    //sort string ascending
                    return -1;
                if (nameA > nameB)
                    return 1;
                return 0; // default return value (no sorting)
            }
            else {
                const indexA = a["index"], indexB = b["index"];
                if (indexA < indexB)
                    // sort ascending
                    return -1;
                if (indexA > indexB)
                    return 1;
                return 0; // default return value (no sorting)
            }
        });
    }
}
exports.sortPlaylists = sortPlaylists;
//# sourceMappingURL=PlaylistDataManager.js.map