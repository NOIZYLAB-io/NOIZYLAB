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
exports.SocialShareManager = void 0;
const Util_1 = require("../Util");
const MenuManager_1 = require("../MenuManager");
const MusicControlManager_1 = require("../music/MusicControlManager");
const SlackManager_1 = require("../managers/SlackManager");
const vscode_1 = require("vscode");
const queryString = require("query-string");
const { WebClient } = require("@slack/web-api");
let musicId = "";
let title = "";
let spotifyLinkUrl = "";
let playlistSelected = false;
class SocialShareManager {
    constructor() {
        //
    }
    static getInstance() {
        if (!SocialShareManager.instance) {
            SocialShareManager.instance = new SocialShareManager();
        }
        return SocialShareManager.instance;
    }
    shareIt(sharer, options) {
        const shareUrl = this.getShareUrl(sharer, options);
        (0, Util_1.launchWebUrl)(shareUrl);
    }
    getShareUrl(sharer, options) {
        const sharers = {
            facebook: {
                shareUrl: "https://www.facebook.com/sharer/sharer.php",
                params: {
                    u: options["url"],
                    hashtag: options["hashtag"],
                },
            },
            x: {
                shareUrl: "https://twitter.com/intent/tweet",
                params: {
                    text: options["title"],
                    url: options["url"],
                    hashtags: options["hashtags"],
                    via: options["via"],
                },
            },
        };
        const sharerObj = sharers[sharer.toLowerCase()];
        const shareUrl = `${sharerObj.shareUrl}?${queryString.stringify(sharerObj.params)}`;
        return shareUrl;
    }
    showMenu(id, label, isPlaylist) {
        return __awaiter(this, void 0, void 0, function* () {
            musicId = id;
            playlistSelected = isPlaylist;
            const menuOptions = {
                items: [],
            };
            const context = isPlaylist ? "Playlist" : "Song";
            title = `Check out this ${context}`;
            spotifyLinkUrl = (0, MusicControlManager_1.buildSpotifyLink)(musicId, isPlaylist);
            // facebook needs the hash
            menuOptions.items.push({
                label: "Facebook",
                detail: `Share '${label}' on Facebook.`,
                url: this.getShareUrl("facebook", {
                    url: spotifyLinkUrl,
                    hashtag: `#MusicTime`,
                }),
            });
            if (yield (0, SlackManager_1.hasSlackWorkspaces)()) {
                menuOptions.items.push({
                    label: "Slack",
                    detail: `Share '${label}' on Slack`,
                    cb: this.shareSlack,
                });
            }
            // twitter doesn't need the hash chars, "via" (optional: twitter username without @)
            menuOptions.items.push({
                label: "X.com",
                detail: `Post '${label}' on X.`,
                url: this.getShareUrl("x", {
                    url: spotifyLinkUrl,
                    title,
                    hashtags: ["MusicTime"],
                }),
            });
            menuOptions.items.push({
                label: `Copy ${context} Link`,
                detail: `Copy ${context.toLowerCase()} link to your clipboard.`,
                cb: this.copyLink,
            });
            const hasSlackAccess = yield (0, SlackManager_1.hasSlackWorkspaces)();
            if (!hasSlackAccess) {
                // show divider
                menuOptions.items.push({
                    label: "___________________________________________________________________",
                    cb: null,
                    url: null,
                    command: null,
                });
                menuOptions.items.push({
                    label: "Connect Slack",
                    detail: "To share a playlist or track on Slack, please connect your account",
                    url: null,
                    cb: SlackManager_1.connectSlackWorkspace,
                });
            }
            (0, MenuManager_1.showQuickPick)(menuOptions);
        });
    }
    copyLink() {
        MusicControlManager_1.MusicControlManager.getInstance().copySpotifyLink(musicId, playlistSelected);
    }
    showSlackMessageInputPrompt() {
        return __awaiter(this, void 0, void 0, function* () {
            return yield vscode_1.window.showInputBox({
                value: `${title}`,
                placeHolder: "Enter a message to appear in the selected channel",
                validateInput: (text) => {
                    return !text ? "Please enter a valid message to continue." : null;
                },
            });
        });
    }
    shareSlack() {
        return __awaiter(this, void 0, void 0, function* () {
            const { selectedChannel, access_token } = yield (0, SlackManager_1.showSlackChannelMenu)();
            if (!selectedChannel) {
                return;
            }
            // !!! important, need to use the get instance as this
            // method may be called within a callback and "this" will be undefined !!!
            const message = yield SocialShareManager.getInstance().showSlackMessageInputPrompt();
            if (!message) {
                return;
            }
            const msg = `${message}\n${spotifyLinkUrl}`;
            const web = new WebClient(access_token);
            yield web.chat
                .postMessage({
                text: msg,
                channel: selectedChannel,
                as_user: true,
            })
                .then((r) => {
                // notify the share is complete
                vscode_1.window.showInformationMessage(`Successfully shared the message to Slack.`);
            })
                .catch((err) => {
                (0, Util_1.logIt)("error posting slack message: " + err.message);
            });
        });
    }
}
exports.SocialShareManager = SocialShareManager;
//# sourceMappingURL=SocialShareManager.js.map