"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const options_1 = require("mocha/lib/cli/options");
const yargs = tslib_1.__importStar(require("yargs"));
let args = (0, options_1.loadOptions)(process.argv.slice(2));
(() => tslib_1.__awaiter(void 0, void 0, void 0, function* () {
    var _a;
    process.send(yargs.parserConfiguration((_a = require("mocha/lib/cli/options").YARGS_PARSER_CONFIG) !== null && _a !== void 0 ? _a : {}).config(args).parse(args._));
}))();
//# sourceMappingURL=loadConfig.js.map