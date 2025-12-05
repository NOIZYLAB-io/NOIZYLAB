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
exports.getSlackAccessToken = exports.hasSlackWorkspaces = exports.getSlackWorkspaces = exports.showSlackChannelMenu = exports.connectSlackWorkspace = void 0;
const Constants_1 = require("../Constants");
const Util_1 = require("../Util");
const MenuManager_1 = require("../MenuManager");
const vscode_1 = require("vscode");
const UserStatusManager_1 = require("./UserStatusManager");
const { WebClient } = require("@slack/web-api");
function connectSlackWorkspace() {
    return __awaiter(this, void 0, void 0, function* () {
        const registered = yield checkRegistration();
        if (!registered) {
            return;
        }
        const url = `${Constants_1.app_endpoint}/code_time/integration_type/slack`;
        // authorize the user for slack
        (0, Util_1.launchWebUrl)(url);
    });
}
exports.connectSlackWorkspace = connectSlackWorkspace;
function showSlackChannelMenu() {
    return __awaiter(this, void 0, void 0, function* () {
        const menuOptions = {
            items: [],
            placeholder: "Select a channel",
        };
        // get the available channels
        let { channels, access_token } = yield getChannels();
        channels.sort(compareLabels);
        // make sure the object array has labels
        channels = channels.map((n) => {
            return Object.assign(Object.assign({}, n), { label: n.name });
        });
        menuOptions.items = channels;
        const pick = yield (0, MenuManager_1.showQuickPick)(menuOptions);
        if (pick && pick.label) {
            return { selectedChannel: pick.id, access_token };
        }
        return { selectedChannel: null, access_token };
    });
}
exports.showSlackChannelMenu = showSlackChannelMenu;
// get saved slack integrations
function getSlackWorkspaces() {
    return __awaiter(this, void 0, void 0, function* () {
        return yield (0, UserStatusManager_1.getCachedSlackIntegrations)();
    });
}
exports.getSlackWorkspaces = getSlackWorkspaces;
function hasSlackWorkspaces() {
    return __awaiter(this, void 0, void 0, function* () {
        return !!(yield getSlackWorkspaces()).length;
    });
}
exports.hasSlackWorkspaces = hasSlackWorkspaces;
// get the access token of a selected slack workspace
function getSlackAccessToken() {
    return __awaiter(this, void 0, void 0, function* () {
        const selectedTeamDomain = yield showSlackWorkspaceSelection();
        if (selectedTeamDomain) {
            return yield getWorkspaceAccessToken(selectedTeamDomain);
        }
        return null;
    });
}
exports.getSlackAccessToken = getSlackAccessToken;
//////////////////////////
// PRIVATE FUNCTIONS
//////////////////////////
function getChannels() {
    return __awaiter(this, void 0, void 0, function* () {
        const access_token = yield getSlackAccessToken();
        if (!access_token) {
            return;
        }
        const web = new WebClient(access_token);
        const result = yield web.conversations.list({ exclude_archived: true, limit: 1000 }).catch((err) => {
            (0, Util_1.logIt)("Unable to retrieve slack channels: " + err.message);
            return [];
        });
        if (result && result.ok) {
            /**
            created:1493157509
            creator:'U54G1N6LC'
            id:'C53QCUUKS'
            is_archived:false
            is_channel:true
            is_ext_shared:false
            is_general:true
            is_group:false
            is_im:false
            is_member:true
            is_mpim:false
            is_org_shared:false
            is_pending_ext_shared:false
            is_private:false
            is_shared:false
            name:'company-announcements'
            name_normalized:'company-announcements'
            num_members:20
            */
            return { channels: result.channels, access_token };
        }
        return { channels: [], access_token: null };
    });
}
function showSlackWorkspaceSelection() {
    return __awaiter(this, void 0, void 0, function* () {
        const menuOptions = {
            items: [],
            placeholder: `Select a Slack workspace`,
        };
        const integrations = yield getSlackWorkspaces();
        integrations.forEach((integration) => {
            const teamName = integration.meta.team.name;
            menuOptions.items.push({
                label: teamName,
                value: teamName,
            });
        });
        menuOptions.items.push({
            label: "Connect a Slack workspace",
            command: "musictime.connectSlack",
        });
        const pick = yield (0, MenuManager_1.showQuickPick)(menuOptions);
        if (pick) {
            if (pick.value) {
                return pick.value;
            }
            else if (pick.command) {
                vscode_1.commands.executeCommand(pick.command);
                return null;
            }
        }
        return null;
    });
}
function getWorkspaceAccessToken(team_domain) {
    return __awaiter(this, void 0, void 0, function* () {
        const integration = (yield getSlackWorkspaces()).find((n) => {
            if (n.team_domain && n.team_domain === team_domain) {
                return n;
            }
            else if (n.meta.team.name === team_domain) {
                return n;
            }
        });
        if (integration) {
            return integration.access_token;
        }
        return null;
    });
}
function checkRegistration() {
    return __awaiter(this, arguments, void 0, function* (showSignup = true) {
        if (!(0, Util_1.getItem)("name")) {
            if (showSignup) {
                vscode_1.window
                    .showInformationMessage("Connecting Slack requires a registered account. Sign up or register for a web.com account at Software.com.", {
                    modal: true,
                }, "Sign up")
                    .then((selection) => __awaiter(this, void 0, void 0, function* () {
                    if (selection === "Sign up") {
                        vscode_1.commands.executeCommand("musictime.signUpAccount");
                    }
                }));
            }
            return false;
        }
        return true;
    });
}
function compareLabels(a, b) {
    if (a.name > b.name)
        return 1;
    if (b.name > a.name)
        return -1;
    return 0;
}
//# sourceMappingURL=SlackManager.js.map