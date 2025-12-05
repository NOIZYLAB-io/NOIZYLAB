"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DecoratorTypeOptions = void 0;
const vscode_1 = require("vscode");
const enums_1 = require("./enums");
const settings_1 = require("./settings");
class DecoratorTypeOptions {
    ClearCache() {
        this.cache.forEach((decOp) => {
            decOp.dispose();
        });
        this.cache.clear();
    }
    MaskDecorationTypeCache(langId) {
        if (this.cache.has(langId)) {
            return this.cache.get(langId);
        }
        const decorationType = this.MatchedDecorationType(langId);
        this.cache.set(langId, decorationType);
        return decorationType;
    }
    constructor() {
        this.cache = new Map();
        this.UnfoldDecorationType = (langId) => {
            return vscode_1.window.createTextEditorDecorationType({
                rangeBehavior: vscode_1.DecorationRangeBehavior.ClosedOpen,
                opacity: settings_1.ExtSettings.Get(enums_1.Settings.unfoldedOpacity, langId).toString()
            });
        };
        this.MatchedDecorationType = (langId) => {
            return vscode_1.window.createTextEditorDecorationType({
                before: {
                    contentText: settings_1.ExtSettings.Get(enums_1.Settings.maskChar, langId),
                    color: settings_1.ExtSettings.Get(enums_1.Settings.maskColor, langId),
                },
                after: {
                    contentText: settings_1.ExtSettings.Get(enums_1.Settings.after, langId),
                },
                textDecoration: "none; display: none;"
            });
        };
        this.PlainDecorationType = () => vscode_1.window.createTextEditorDecorationType({});
    }
}
exports.DecoratorTypeOptions = DecoratorTypeOptions;
//# sourceMappingURL=decoration.js.map