"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TelemetryLogger = void 0;
const extension_telemetry_1 = require("@vscode/extension-telemetry");
class TelemetryLogger {
    static instance() {
        return TelemetryLogger._instance;
    }
    constructor() {
        this.instrumentationKey = Buffer.from('NTMwMTliNjctNGIyZS00NDg5LWFlNmYtZmE3MjIxYjRhNTg1', 'base64').toString();
        this.telemetryReporter = new extension_telemetry_1.default(this.instrumentationKey);
    }
    async sendTelemetryEvent(eventName, properties, measurements) {
        this.telemetryReporter.sendRawTelemetryEvent(eventName, properties, measurements);
    }
    async sendTelemetryErrorEvent(eventName, properties, measurements) {
        this.telemetryReporter.sendTelemetryErrorEvent(eventName, properties, measurements);
    }
    parseHrtimeToMs(hrtime) {
        var ms = Math.round((hrtime[0] * 1000000000 + hrtime[1]) / 1000000);
        return ms;
    }
    dispose() {
        this.telemetryReporter.dispose();
    }
}
exports.TelemetryLogger = TelemetryLogger;
TelemetryLogger._instance = new TelemetryLogger();
//# sourceMappingURL=TelemetryLogger.js.map