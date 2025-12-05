"use strict";
/**
 * Types and interfaces for the transcription history
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.TRANSCRIPTION_HISTORY_CONSTANTS = exports.DateGroupCategory = exports.RecordingMode = void 0;
/**
 * Recording modes (duplicated from extension.ts to avoid circular dependencies)
 */
var RecordingMode;
(function (RecordingMode) {
    RecordingMode["INSERT_OR_CLIPBOARD"] = "insertOrClipboard";
    RecordingMode["INSERT_AT_CURRENT_CHAT"] = "insertAtCurrentChat"; // Ctrl+Shift+N - insert into the current chat Cursor
})(RecordingMode || (exports.RecordingMode = RecordingMode = {}));
/**
 * Categories of grouping by date
 */
var DateGroupCategory;
(function (DateGroupCategory) {
    DateGroupCategory["TODAY"] = "today";
    DateGroupCategory["YESTERDAY"] = "yesterday";
    DateGroupCategory["THIS_WEEK"] = "thisWeek";
    DateGroupCategory["OLDER"] = "older";
})(DateGroupCategory || (exports.DateGroupCategory = DateGroupCategory = {}));
/**
 * Constants for the transcription history
 */
exports.TRANSCRIPTION_HISTORY_CONSTANTS = {
    /** Maximum number of entries in the history */
    MAX_ENTRIES: 100,
    /** Version of the current data format */
    CURRENT_VERSION: '1.0.0',
    /** Maximum length of the preview text */
    PREVIEW_LENGTH: 50,
    /** Key for storing in VS Code storage */
    STORAGE_KEY: 'transcriptionHistory'
};
//# sourceMappingURL=TranscriptionHistory.js.map