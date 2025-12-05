"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.assertDefined = void 0;
function assertDefined(val, msg) {
    if (val === null || val === undefined) {
        throw new Error(msg !== null && msg !== void 0 ? msg : "Assert value not to be undefined");
    }
}
exports.assertDefined = assertDefined;
//# sourceMappingURL=assertDefined.js.map