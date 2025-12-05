"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Prerequisites = void 0;
const Constants_1 = require("./Constants");
const Logger_1 = require("./Logger");
const ShellCommand_1 = require("./ShellCommand");
class Prerequisites {
    static async checkDocker() {
        try {
            //Check by running docker info which will return a version if docker is installed and running.
            const result = await ShellCommand_1.ShellCommand.runexec("docker", ["info"]);
            if (result.toLowerCase().indexOf("version:") > -1) {
                return true;
            }
            else {
                return false;
            }
        }
        catch (error) {
            Logger_1.Logger.instance().log(Constants_1.LogType.error, error.stdout);
            return false;
        }
    }
    static async checkDockerCompose() {
        //Simply checking if docker-compose is installed
        const result = await ShellCommand_1.ShellCommand.runexec("docker-compose", ["-v"]);
        if (result.toLowerCase().indexOf("version ") > -1) {
            return true;
        }
        else {
            return false;
        }
    }
}
exports.Prerequisites = Prerequisites;
//# sourceMappingURL=Prerequisites.js.map