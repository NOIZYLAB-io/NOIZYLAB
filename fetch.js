"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.fetch = void 0;
// exposition-only
const dynImport = () => import("node-fetch");
let esmPromise;
const fetch = async (...args) => {
    if (typeof esmPromise === "undefined") {
        esmPromise = import("node-fetch");
    }
    const fetch = (await esmPromise).default;
    return fetch(...args);
};
exports.fetch = fetch;
//# sourceMappingURL=fetch.js.map