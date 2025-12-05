"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WolfSessionController = exports.wolfSessionStoreFactory = void 0;
function wolfSessionStoreFactory() {
    return new WolfSessionController();
}
exports.wolfSessionStoreFactory = wolfSessionStoreFactory;
class WolfSessionController {
    constructor() {
        this._sessions = {};
    }
    clearAllSessions() {
        this._sessions = {};
    }
    createSessionFromEditor(editor) {
        this._sessions[editor.document.fileName] = editor;
    }
    getSessionByFileName(fileName) {
        return this._sessions[fileName];
    }
    sessionIsActiveByDocument(document) {
        return !!this._sessions[document.fileName];
    }
    get sessionNames() {
        return Object.keys(this._sessions);
    }
}
exports.WolfSessionController = WolfSessionController;
//# sourceMappingURL=sessions.js.map