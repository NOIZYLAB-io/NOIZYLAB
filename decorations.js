"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WolfDecorationsController = exports.wolfDecorationStoreFactory = void 0;
const vscode_1 = require("vscode");
const colors_1 = require("./colors");
const icons_1 = require("./icons");
const helpers_1 = require("./helpers");
const utils_1 = require("./utils");
const js_beautify_1 = require("js-beautify");
function wolfDecorationStoreFactory(context) {
    return new WolfDecorationsController(context);
}
exports.wolfDecorationStoreFactory = wolfDecorationStoreFactory;
class WolfDecorationsController {
    constructor(context) {
        this.context = context;
        this._decorations = {};
        this._decorationTypes = null;
        this._preparedDecorations = null;
        this.getDecorationTypes = () => {
            if (this._decorationTypes)
                return this._decorationTypes;
        };
        this.getEmptyDecorations = () => {
            return { success: [], error: [] };
        };
        this.getPreparedDecorations = () => {
            if (this._preparedDecorations) {
                return this._preparedDecorations;
            }
            else {
                return this.getEmptyDecorations();
            }
        };
        this.prepareParsedPythonData = (data) => {
            for (const line of data !== null && data !== void 0 ? data : []) {
                this.setDecorationAtLine(line);
            }
        };
        this.reInitDecorationCollection = () => {
            this._decorations = {};
        };
        this.setDefaultDecorationOptions = (successColor, errorColor) => {
            this._decorationTypes = {
                success: this.createGutterDecorations(successColor),
                error: this.createGutterDecorations(errorColor),
            };
        };
        this.setPreparedDecorationsForEditor = (editor) => {
            const decorations = [];
            const errorDecorations = [];
            Object.keys(this._decorations).forEach(key => {
                const lineNo = parseInt(key, 10);
                const lineIndex = lineNo - 1;
                const decorationData = this.getDecorationAtLine(lineNo);
                if (!decorationData.data || editor.document.lineCount < lineNo) {
                    return;
                }
                const textLine = editor.document.lineAt(lineIndex);
                const source = textLine.text;
                const decoRange = new vscode_1.Range(new vscode_1.Position(lineIndex, textLine.firstNonWhitespaceCharacterIndex), new vscode_1.Position(lineIndex, textLine.text.indexOf(source) + source.length));
                const decoration = this.createWolfDecorationOptions({
                    range: decoRange,
                    text: decorationData.data.join(" => "),
                    hoverText: decorationData.pretty.join("\n"),
                    color: decorationData.error ? "red" : "cornflower"
                });
                if (decorationData.error)
                    errorDecorations.push(decoration);
                else
                    decorations.push(decoration);
            });
            this._preparedDecorations = {
                success: decorations,
                error: errorDecorations
            };
        };
        this.createWolfDecorationOptions = (options) => {
            var _a;
            const truncLength = (_a = vscode_1.workspace
                .getConfiguration("wolf")
                .get("maxLineLength")) !== null && _a !== void 0 ? _a : 100;
            const textLength = options.text.length;
            const ellipsis = textLength > truncLength ? " ..." : "";
            return {
                range: options.range,
                hoverMessage: {
                    language: options.language || "python",
                    value: options.hoverText
                },
                renderOptions: {
                    after: {
                        contentText: options.text.slice(0, utils_1.clamp(1, 1000, truncLength)) + ellipsis,
                        fontWeight: "normal",
                        fontStyle: "normal",
                        color: colors_1.wolfTextColorProvider(options.color)
                    }
                }
            };
        };
        this.createGutterDecorations = (gutterIconColor, leftMargin = 3) => {
            return vscode_1.window.createTextEditorDecorationType({
                after: {
                    margin: `0 0 0 ${leftMargin}em`,
                    textDecoration: "none"
                },
                isWholeLine: true,
                rangeBehavior: 1,
                overviewRulerLane: 1,
                overviewRulerColor: colors_1.wolfTextColorProvider(gutterIconColor),
                gutterIconPath: icons_1.wolfIconProvider(this.context, gutterIconColor, this.pawprints),
                gutterIconSize: "cover"
            });
        };
        this.getDecorationAtLine = (lineNo) => {
            return this._decorations[lineNo];
        };
        this.getDecorationAtLineOrDefault = (lineNo) => {
            return (this.getDecorationAtLine(lineNo) || { data: [], pretty: [] });
        };
        this.setDecorationAtLine = (line) => {
            const lineNo = line.lineno;
            const { data, pretty } = this.getDecorationAtLineOrDefault(lineNo);
            const annotation = helpers_1.formatWolfResponseElement(line);
            this._decorations[lineNo] = {
                data: [...data, utils_1.stringEscape(annotation)],
                lineno: lineNo,
                error: line.error ? true : false,
                loop: line["_loop"],
                pretty: [...pretty, js_beautify_1.js(line.value, {
                        indent_size: 4,
                        space_in_empty_paren: true
                    })]
            };
        };
    }
    get hasDecorations() {
        return Object.keys(this._decorations).length > 0;
    }
    get pawprints() {
        var _a;
        return (_a = vscode_1.workspace
            .getConfiguration("wolf")
            .get("pawPrintsInGutter")) !== null && _a !== void 0 ? _a : false;
    }
}
exports.WolfDecorationsController = WolfDecorationsController;
//# sourceMappingURL=decorations.js.map