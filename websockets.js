"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.initializeWebsockets = exports.clearWebsocketsClient = exports.clearRetryTimeout = exports.clearPingTimeout = exports.clearWebsocketClient = exports.websocketAlive = void 0;
const Constants_1 = require("./Constants");
const DeviceManager_1 = require("./managers/DeviceManager");
const authenticated_plugin_user_1 = require("./message_handlers/authenticated_plugin_user");
const integration_connection_1 = require("./message_handlers/integration_connection");
const Util_1 = require("./Util");
const WebSocket = require("ws");
const scheme = Constants_1.api_endpoint.includes('https') ? 'wss://' : 'ws://';
const host = Constants_1.api_endpoint.split('//')[1];
const websockets_url = `${scheme}${host}/websockets`;
const ONE_MINUTE = 1000 * 60;
const LONG_ERROR_DELAY = ONE_MINUTE * 5;
let retryTimeout;
let pingTimeout;
let pingInterval = ONE_MINUTE;
let ws;
let alive = false;
function websocketAlive() {
    return alive;
}
exports.websocketAlive = websocketAlive;
// dispose of the websocket and any timeouts that are waiting
function clearWebsocketClient() {
    clearWebsocketsClient();
    clearPingTimeout();
    clearRetryTimeout();
}
exports.clearWebsocketClient = clearWebsocketClient;
function clearPingTimeout() {
    if (pingTimeout) {
        clearTimeout(pingTimeout);
        pingTimeout = undefined;
    }
}
exports.clearPingTimeout = clearPingTimeout;
function clearRetryTimeout() {
    if (retryTimeout) {
        clearTimeout(retryTimeout);
        retryTimeout = undefined;
    }
}
exports.clearRetryTimeout = clearRetryTimeout;
function clearWebsocketsClient() {
    if (ws) {
        ws.close(1000, 're-initializing websocket');
        ws = null;
    }
}
exports.clearWebsocketsClient = clearWebsocketsClient;
function initializeWebsockets() {
    clearWebsocketClient();
    ws = new WebSocket(websockets_url, {
        headers: {
            Authorization: (0, Util_1.getItem)("jwt"),
            "X-SWDC-Plugin-Name": (0, Util_1.getPluginName)(),
            "X-SWDC-Plugin-Id": (0, Util_1.getMusicTimePluginId)(),
            "X-SWDC-Plugin-Version": (0, Util_1.getVersion)(),
            "X-SWDC-Plugin-OS": (0, DeviceManager_1.getOs)(),
            "X-SWDC-Plugin-TZ": Intl.DateTimeFormat().resolvedOptions().timeZone,
            "X-SWDC-Plugin-Offset": (0, Util_1.getOffsetSeconds)() / 60,
            "X-SWDC-Plugin-UUID": (0, Util_1.getPluginUuid)(),
        },
        perMessageDeflate: false
    });
    ws.on('open', function open() {
        (0, Util_1.logIt)("Websockets connection open");
    });
    ws.on('message', function message(data) {
        alive = true;
        handleIncomingMessage(data);
    });
    ws.on("ping", heartbeat);
    ws.on("close", function close(code, reason) {
        (0, Util_1.logIt)(`Websockets closed`, true);
        if (code !== 1000) {
            retryConnection();
        }
    });
    ws.on("error", function error(e) {
        (0, Util_1.logIt)(`Error connecting to websockets server: ${e.message}`);
        retryConnection(LONG_ERROR_DELAY);
    });
    ws.on('unexpected-response', function unexpectedResponse(request, response) {
        (0, Util_1.logIt)(`Unexpected websockets response: ${response.statusCode}`);
        if (response.statusCode === 426) {
            (0, Util_1.logIt)('Websockets request had invalid headers. Are you behind a proxy?');
        }
        else if (response.statusCode >= 500) {
            retryConnection();
        }
    });
    const handleIncomingMessage = (data) => {
        try {
            const message = JSON.parse(data);
            switch (message.type) {
                case "authenticated_plugin_user":
                    (0, authenticated_plugin_user_1.handleAuthenticatedPluginUser)(message.body);
                    break;
                case "user_integration_connection":
                    (0, integration_connection_1.handleIntegrationConnectionSocketEvent)(message.body);
                    break;
            }
        }
        catch (e) {
            (0, Util_1.logIt)(`Unable to handle incoming websockets message: ${e.message}`);
        }
    };
    function retryConnection(delay = getDelay()) {
        alive = false;
        if (retryTimeout) {
            return;
        }
        retryTimeout = setTimeout(() => {
            initializeWebsockets();
        }, delay);
    }
    ;
    function heartbeat(buf) {
        try {
            // convert the buffer to the json payload containing the server timeout
            const data = JSON.parse(buf.toString());
            if (data === null || data === void 0 ? void 0 : data.timeout) {
                // add a 1 minute buffer to the millisconds timeout the server provides
                pingInterval = data.timeout;
            }
        }
        catch (e) {
            pingInterval = ONE_MINUTE;
            (0, Util_1.logIt)(`Unable to handle incoming websockets heartbeat: ${e.message}`);
        }
        clearPingTimeout();
        pingTimeout = setTimeout(() => {
            if (ws) {
                ws.terminate();
            }
        }, pingInterval);
    }
    // delay between 30 and 59 seconds
    function getDelay() {
        return Math.floor(getRandomNumberWithinRange(30, 59) * 1000);
    }
    function getRandomNumberWithinRange(min, max) {
        return Math.floor(Math.random() * (max - min) + min);
    }
}
exports.initializeWebsockets = initializeWebsockets;
//# sourceMappingURL=websockets.js.map