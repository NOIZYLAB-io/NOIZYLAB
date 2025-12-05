"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ShellCommand = void 0;
const ChildProcess = require("child_process");
const Logger_1 = require("./Logger");
const constants = require("./Constants");
const path = require("path");
class ShellCommand {
    static async run(cmd, pwd, args, printLogs = true) {
        const logger = Logger_1.Logger.instance();
        const regEx = new RegExp(this.pattern, 'g');
        const options = {
            cwd: pwd,
            env: process.env
        };
        //Give execute permissions to the script folder.
        if (!this.isExecPermissionSet && process.platform !== "win32") {
            ChildProcess.execSync(`chmod u+x \`ls ${path.join(constants.Settings.dockerDir, '..', '..', 'scripts')}/*.sh\``);
            this.isExecPermissionSet = true;
        }
        //Submit the actual command.
        const childProcess = ChildProcess.spawn(cmd, args, options);
        let ouput = "";
        childProcess.stdout.on("data", data => {
            let messages = data.toString().replace(regEx, "").split("\n");
            messages.forEach((message) => {
                if (message) {
                    if (printLogs) {
                        logger.log(constants.LogType.info, message);
                    }
                    ouput = `${ouput}${message}\n`;
                }
            });
        });
        childProcess.stderr.on("data", data => {
            let messages = data.toString().replace(regEx, "").split("\n");
            messages.forEach((message) => {
                if (message) {
                    if (printLogs
                        && message.toLowerCase().indexOf("found orphan containers") === -1 /*suppress orphan container messages as we are using two docker-compose files*/) {
                        logger.log(constants.LogType.info, message);
                    }
                    ouput = `${ouput}${message}\n`;
                }
            });
        });
        return new Promise((resolve, reject) => {
            childProcess.on('error', (error) => {
                logger.log(constants.LogType.error, error.message);
                ouput = `${ouput}${error.message}\n`;
                return reject(ouput);
            });
            childProcess.on('close', (code) => {
                if (code) {
                    //Check if the command exited because Docker was not running.
                    if (ouput.toLowerCase().indexOf("docker daemon is not running") > -1) {
                        return reject(ouput);
                    }
                    else {
                        return resolve(ouput);
                    }
                }
                else {
                    return resolve(ouput);
                }
            });
        });
    }
    static async runexec(cmd, args) {
        cmd = `${cmd} ${args.join(" ")}`;
        return ChildProcess.execSync(cmd).toString();
    }
    static async runDockerCompose(composeFileName, args, printLogs = true) {
        const cmd = "docker-compose";
        let dockerArgs = ["-p", constants.Settings.singleOrgProj, "-f", composeFileName];
        return this.run(cmd, constants.Settings.dockerDir, [...dockerArgs, ...args], printLogs);
    }
    static async execDockerComposeSh(composeFileName, container, cmd, args = [], printLogs = true) {
        let dockerArgs = ["exec", "-T", container, "sh", "-c", `${cmd} ${args.join(" ")}`];
        return this.runDockerCompose(composeFileName, dockerArgs, printLogs);
    }
    static async execDockerComposeBash(composeFileName, container, cmd, args = [], printLogs = true) {
        let dockerArgs = ["exec", "-T", container, "/bin/bash", "-c", `${cmd} ${args.join(" ")}`];
        return this.runDockerCompose(composeFileName, dockerArgs, printLogs);
    }
}
exports.ShellCommand = ShellCommand;
ShellCommand.pattern = [
    '[\\u001B\\u009B][[\\]()#;?]*(?:(?:(?:(?:;[-a-zA-Z\\d\\/#&.:=?%@~_]+)*|[a-zA-Z\\d]+(?:;[-a-zA-Z\\d\\/#&.:=?%@~_]*)*)?\\u0007)',
    '(?:(?:\\d{1,4}(?:;\\d{0,4})*)?[\\dA-PR-TZcf-nq-uy=><~]))'
].join('|');
ShellCommand.isExecPermissionSet = false;
//# sourceMappingURL=ShellCommand.js.map