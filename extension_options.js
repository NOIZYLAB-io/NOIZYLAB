"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ExtensionOptions = void 0;
const vscode = require("vscode");
class ExtensionOptions {
    static getFFmpegPath() {
        return vscode.workspace.getConfiguration().get(ExtensionOptions.FFmpegPathOptionKey);
    }
    static getFFprobePath() {
        return vscode.workspace.getConfiguration().get(ExtensionOptions.FFprobePathOptionKey);
    }
    static getTablePageSize() {
        const pageSize = vscode.workspace.getConfiguration().get(ExtensionOptions.TablePageSizeOptionKey);
        return pageSize > 0 ? pageSize : ExtensionOptions.kDefaultPageSize;
    }
}
exports.ExtensionOptions = ExtensionOptions;
ExtensionOptions.FFmpegPathOptionKey = 'avprobe.ffmpegPath';
ExtensionOptions.FFprobePathOptionKey = 'avprobe.ffprobePath';
ExtensionOptions.TablePageSizeOptionKey = 'avprobe.packetInfo.pageSize';
ExtensionOptions.kDefaultPageSize = 10;
//# sourceMappingURL=extension_options.js.map