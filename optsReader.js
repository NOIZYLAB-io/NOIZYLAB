"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MochaOptsReader = void 0;
const tslib_1 = require("tslib");
const fs = tslib_1.__importStar(require("fs"));
const util = tslib_1.__importStar(require("util"));
const child_process_1 = require("child_process");
class MochaOptsReader {
    constructor(log) {
        this.log = log;
    }
    readMochaOptsFile(file) {
        if (this.log.enabled)
            this.log.debug(`Looking for mocha options in ${file}`);
        return new Promise(resolve => {
            fs.readFile(file, 'utf8', (err, data) => {
                if (err) {
                    if (this.log.enabled) {
                        if (err.code === 'ENOENT') {
                            this.log.debug('Couldn\'t find mocha.opts file');
                        }
                        else {
                            this.log.debug(`Couldn't read mocha.opts file: ${util.inspect(err)}`);
                        }
                    }
                    resolve({ mochaOpts: {}, globs: [], ignores: [], files: [] });
                    return;
                }
                try {
                    const opts = data
                        .replace(/^#.*$/gm, '')
                        .replace(/\\\s/g, '%20')
                        .split(/\s/)
                        .filter(Boolean)
                        .map(value => value.replace(/%20/g, ' '));
                    const globs = this.findPositionalArgs(opts);
                    const files = this.findOptValues(['--file'], opts);
                    const ignores = this.findOptValues(['--ignore', '--exclude'], opts);
                    const ui = this.findOptValue(['-u', '--ui'], opts);
                    const timeoutString = this.findOptValue(['-t', '--timeout'], opts);
                    const timeout = timeoutString ? Number.parseInt(timeoutString) : undefined;
                    const retriesString = this.findOptValue(['--retries'], opts);
                    const retries = retriesString ? Number.parseInt(retriesString) : undefined;
                    const requires = this.findOptValues(['-r', '--require'], opts);
                    const delay = (opts.indexOf('--delay') >= 0) ? true : undefined;
                    const fullTrace = (opts.indexOf('--full-trace') >= 0) ? true : undefined;
                    const exit = (opts.indexOf('--exit') >= 0) ? true : undefined;
                    const asyncOnly = (opts.indexOf('-A') >= 0) || (opts.indexOf('--async-only') >= 0);
                    const mochaOpts = { ui, timeout, retries, requires, delay, fullTrace, exit, asyncOnly };
                    if (this.log.enabled) {
                        this.log.debug(`Options from mocha.opts file: ${JSON.stringify(mochaOpts)}`);
                        this.log.debug(`Globs from mocha.opts file: ${JSON.stringify(globs)}`);
                        this.log.debug(`Files from mocha.opts file: ${JSON.stringify(files)}`);
                    }
                    resolve({ mochaOpts, globs, ignores, files });
                }
                catch (err) {
                    if (this.log.enabled)
                        this.log.debug(`Couldn't parse mocha.opts file: ${util.inspect(err)}`);
                    resolve({ mochaOpts: {}, globs: [], ignores: [], files: [] });
                }
            });
        });
    }
    readOptsUsingMocha(cwd_1, nodePath_1) {
        return tslib_1.__awaiter(this, arguments, void 0, function* (cwd, nodePath, nodeArgv = [], argv = []) {
            const options = yield new Promise((resolve, reject) => {
                const childProcScript = require.resolve('../out/worker/loadConfig.js');
                const stdio = ['pipe', 'pipe', 'pipe', 'ipc'];
                let childProc;
                if (nodePath) {
                    childProc = (0, child_process_1.spawn)(nodePath, [...nodeArgv, childProcScript, ...argv], { cwd, stdio });
                }
                else {
                    childProc = (0, child_process_1.fork)(childProcScript, argv, { cwd, execArgv: nodeArgv, stdio });
                }
                let finished = false;
                childProc.once('message', (options) => {
                    if (!finished) {
                        finished = true;
                        resolve(options);
                    }
                });
                childProc.once('close', (code, signal) => {
                    if (!finished) {
                        const msg = `Couldn't load options using mocha: child process exited with code ${code} and signal ${signal}`;
                        this.log.error(msg);
                        finished = true;
                        reject(new Error(msg));
                    }
                });
                childProc.once('error', (err) => {
                    if (!finished) {
                        const msg = `Couldn't load options using mocha: error from child process ${util.inspect(err)}`;
                        this.log.error(msg);
                        finished = true;
                        reject(new Error(msg));
                    }
                });
                if (this.log.enabled) {
                    childProc.stdout.on('data', data => this.log.info(`Worker (stdout): ${data.toString()}`));
                    childProc.stderr.on('data', data => this.log.error(`Worker (stderr): ${data.toString()}`));
                }
            });
            return {
                files: options.file || [],
                ignores: options.ignore || [],
                globs: options._ || [],
                mochaOpts: {
                    ui: options.ui,
                    requires: options.require,
                    timeout: +options.timeout,
                    retries: (options.retries !== undefined) ? +options.retries : undefined,
                    delay: options.delay,
                    fullTrace: options['full-trace'],
                    exit: options.exit,
                    asyncOnly: options.asyncOnly
                }
            };
        });
    }
    findOptValue(needles, haystack) {
        let index;
        for (const needle of needles) {
            const needleIndex = haystack.lastIndexOf(needle);
            if ((needleIndex >= 0) && ((index === undefined) || (needleIndex > index))) {
                index = needleIndex;
            }
        }
        if ((index !== undefined) && (haystack.length > index + 1)) {
            return haystack[index + 1];
        }
        else {
            return undefined;
        }
    }
    findOptValues(needles, haystack) {
        const values = [];
        for (let i = 0; i < haystack.length; i++) {
            if (needles.indexOf(haystack[i]) >= 0) {
                i++;
                if (i < haystack.length) {
                    values.push(haystack[i]);
                }
            }
        }
        return values;
    }
    findPositionalArgs(haystack) {
        const args = [];
        for (let i = 0; i < haystack.length; i++) {
            if (haystack[i].startsWith('-')) {
                if (MochaOptsReader.booleanOpts.indexOf(haystack[i]) < 0) {
                    i++;
                }
            }
            else {
                args.push(haystack[i]);
            }
        }
        return args;
    }
}
exports.MochaOptsReader = MochaOptsReader;
MochaOptsReader.booleanOpts = [
    '--allow-uncaught',
    '--async-only', '-A',
    '--bail', '-b',
    '--check-leaks',
    '--color', '--colors', '-c',
    '--debug', '-d',
    '--debug-brk',
    '--delay',
    '--diff',
    '--es_staging',
    '--exit',
    '--expose-gc', '-gc',
    '--forbid-only',
    '--forbid-pending',
    '--full-trace',
    '--growl', '-G',
    '--icu-data-dir',
    '--inline-diffs',
    '--inspect',
    '--inspect-brk',
    '--invert', '-i',
    '--log-timer-events',
    '--napi-modules',
    '--no-colors', '-C',
    '--no-deprecation',
    '--no-timeouts',
    '--no-warnings',
    '--perf-basic-prof',
    '--preserve-symlinks',
    '--prof',
    '--recursive',
    '--sort', '-S',
    '--throw-deprecation',
    '--trace',
    '--trace-deprecation',
    '--trace-warnings',
    '--use_strict',
    '--watch', '-w'
];
//# sourceMappingURL=optsReader.js.map