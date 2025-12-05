"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.wolfIconProvider = void 0;
const colors_1 = require("./colors");
function wolfIconProvider(context, color, pawprints) {
    const iconColor = colors_1.wolfIconColorProvider(color);
    return context
        .asAbsolutePath(`media\\wolf${pawprints ? "-paw" : ""}-${iconColor}.png`)
        .replace(/\\/g, "/");
}
exports.wolfIconProvider = wolfIconProvider;
//# sourceMappingURL=icons.js.map