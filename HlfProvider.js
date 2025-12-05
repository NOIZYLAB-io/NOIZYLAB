"use strict";
var _a;
Object.defineProperty(exports, "__esModule", { value: true });
exports.HlfProvider = void 0;
const vscode = require("vscode");
const ShellCommand_1 = require("../utilities/ShellCommand");
const Constants_1 = require("../utilities/Constants");
const Logger_1 = require("../utilities/Logger");
const promises_1 = require("timers/promises");
const Prerequisites_1 = require("../utilities/Prerequisites");
const TelemetryLogger_1 = require("../utilities/TelemetryLogger");
const fs = require("fs");
const path = require("path");
const fabric_network_1 = require("fabric-network");
class HlfProvider {
    static async createNetwork() {
        const logger = Logger_1.Logger.instance();
        try {
            if (!(await Prerequisites_1.Prerequisites.checkDocker())) {
                logger.showMessage(Constants_1.LogType.error, "Prerequisite- Docker is not installed or running. Please install and start Docker and try again");
                return false;
            }
            if (!(await Prerequisites_1.Prerequisites.checkDockerCompose())) {
                logger.showMessage(Constants_1.LogType.error, "Prerequisite- Docker-compose is not installed. Please install latest version of Docker-compose and try again");
                return false;
            }
            var startTime = process.hrtime();
            const telemetryLogger = TelemetryLogger_1.TelemetryLogger.instance();
            await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: "Starting local Fabric network",
                cancellable: true
            }, async (progress) => {
                //Create the network by invoking Docker compose
                //It is Ok to invoke Docker compose on a running network also
                //Create the CA node first
                await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localCa, ["up", "--detach"]);
                progress.report({ increment: 10 });
                //Wait for some time for the CA node to be fully functional
                await (0, promises_1.setTimeout)(1000);
                //Create the required certificates
                await ShellCommand_1.ShellCommand.execDockerComposeSh(Constants_1.DockerComposeFiles.localCa, Constants_1.Settings.singleOrgSettings.caDomain, "/etc/hyperledger/fabric/scripts/registerEnrollOneOrg.sh");
                progress.report({ increment: 20 });
                //Create the rest of the nodes
                await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localNetwork, ["up", "--detach"]);
                logger.log(Constants_1.LogType.info, "Created local Fabric network");
                progress.report({ increment: 70, message: "Creating channel" });
                //Wait for some time for the nodes to be fully functional
                await (0, promises_1.setTimeout)(1000);
                //Create the default channel
                await ShellCommand_1.ShellCommand.execDockerComposeBash(Constants_1.DockerComposeFiles.localNetwork, "debug-cli", "/etc/hyperledger/fabric/scripts/createChannelInternal.sh");
                progress.report({ increment: 85, message: "Deploying chaincode" });
                if (Constants_1.Settings.isCaas) {
                    //Install chaincode on peers
                    await this.installCaasChaincode();
                }
                else {
                    Constants_1.Settings.defaultChaincodePackageId = `${Constants_1.Settings.defaultChaincodeId}:${Constants_1.Settings.defaultChaincodeVersion}`;
                }
                //Approve and Commit chaincode on the channel
                let chaincodeArgs = [Constants_1.Settings.defaultChaincodeId, Constants_1.Settings.defaultChaincodeVersion, Constants_1.Settings.defaultChaincodePackageId];
                await ShellCommand_1.ShellCommand.execDockerComposeBash(Constants_1.DockerComposeFiles.localNetwork, "debug-cli", "/etc/hyperledger/fabric/scripts/deployChaincodeInternal.sh", chaincodeArgs);
                progress.report({ increment: 100 });
                HlfProvider.islocalNetworkStarted = true;
                vscode.commands.executeCommand('hlf.identity.refresh');
                vscode.commands.executeCommand('hlf.localnetwork.refresh');
                logger.showMessage(Constants_1.LogType.info, "Local Fabric Network started");
            });
            const elapsedTime = telemetryLogger.parseHrtimeToMs(process.hrtime(startTime));
            telemetryLogger.sendTelemetryEvent('CreateNetwork', null, { 'createNetworkDuration': elapsedTime });
            return true;
        }
        catch (error) {
            Logger_1.Logger.instance().showMessageOnly(Constants_1.LogType.error, `Failed to start local Fabric Network. ${error}`);
            return false;
        }
    }
    static setChaincodeName(name) {
        if (name) {
            Constants_1.Settings.defaultChaincodeId = name.replace(/\W+/g, "-").replace(/^-+/, "").replace(/-+$/, "");
        }
        else if (vscode.workspace.name) {
            //Chaincode name is the current workspace name. Replace all non-alphanumeric characters with "-".
            Constants_1.Settings.defaultChaincodeId = vscode.workspace.name.replace(/\W+/g, "-").replace(/^-+/, "").replace(/-+$/, "");
            if (Constants_1.Settings.isCaas) {
                Constants_1.Settings.defaultChaincodeId = `${Constants_1.Settings.defaultChaincodeId}-caas`;
            }
        }
        Constants_1.Settings.debugEnv.CORE_CHAINCODE_ID_NAME = `${Constants_1.Settings.defaultChaincodeId}:${Constants_1.Settings.defaultChaincodeVersion}`;
    }
    static async stopNetwork() {
        //Stop existing debug session
        vscode.debug.stopDebugging(vscode.debug.activeDebugSession);
        var startTime = process.hrtime();
        const telemetryLogger = TelemetryLogger_1.TelemetryLogger.instance();
        await vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "Stopping local Fabric network",
            cancellable: true
        }, async (progress) => {
            try {
                progress.report({ increment: 20 });
                //Stop the CA node
                await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localCa, ["stop"]);
                progress.report({ increment: 40 });
                //Stop the rest of the nodes
                await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localNetwork, ["stop"]);
                progress.report({ increment: 100 });
            }
            catch (error) {
                if (error.indexOf('ENOENT') > -1) {
                    Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `Prerequisite- Docker is not installed. Please install latest version of Docker and Docker-compose and try again`);
                }
                else {
                    Logger_1.Logger.instance().showMessageOnly(Constants_1.LogType.error, "Failed to stop local Fabric Network");
                }
            }
            HlfProvider.islocalNetworkStarted = false;
            vscode.commands.executeCommand('hlf.identity.refresh');
            vscode.commands.executeCommand('hlf.localnetwork.refresh');
            Logger_1.Logger.instance().showMessage(Constants_1.LogType.info, "Local Fabric Network stopped");
        });
        const elapsedTime = telemetryLogger.parseHrtimeToMs(process.hrtime(startTime));
        telemetryLogger.sendTelemetryEvent('StopNetwork', null, { 'stopNetworkDuration': elapsedTime });
    }
    static async restartNetwork() {
        await this.stopNetwork();
        await this.createNetwork();
    }
    static async removeNetwork() {
        //Stop existing debug session
        vscode.debug.stopDebugging(vscode.debug.activeDebugSession);
        var startTime = process.hrtime();
        const telemetryLogger = TelemetryLogger_1.TelemetryLogger.instance();
        await vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "Removing local Fabric network",
            cancellable: true
        }, async (progress) => {
            try {
                //Cleanup the files related to the local network
                await ShellCommand_1.ShellCommand.execDockerComposeBash(Constants_1.DockerComposeFiles.localNetwork, "debug-cli", "/etc/hyperledger/fabric/scripts/cleanupFiles.sh");
                progress.report({ increment: 20 });
                //Remove all the nodes except CA
                await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localNetwork, ["down", "-v"]);
                progress.report({ increment: 80 });
                //Remove the CA node
                await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localCa, ["down", "-v"]);
                progress.report({ increment: 100 });
            }
            catch (error) {
                if (error.indexOf('ENOENT') > -1) {
                    Logger_1.Logger.instance().showMessage(Constants_1.LogType.error, `Prerequisite- Docker is not installed. Please install latest version of Docker and Docker-compose and try again`);
                }
                else {
                    Logger_1.Logger.instance().showMessageOnly(Constants_1.LogType.error, "Failed to remove local Fabric Network");
                }
            }
            HlfProvider.islocalNetworkStarted = false;
            vscode.commands.executeCommand('hlf.identity.refresh');
            vscode.commands.executeCommand('hlf.localnetwork.refresh');
            Logger_1.Logger.instance().showMessage(Constants_1.LogType.info, "Local Fabric Network removed");
        });
        const elapsedTime = telemetryLogger.parseHrtimeToMs(process.hrtime(startTime));
        telemetryLogger.sendTelemetryEvent('RemoveNetwork', null, { 'removeNetworkDuration': elapsedTime });
    }
    static async installCaasChaincode() {
        let chaincodeArgs = [Constants_1.Settings.defaultChaincodeId];
        //Package the chaincode first
        Constants_1.Settings.defaultChaincodePackageId = (await ShellCommand_1.ShellCommand.execDockerComposeBash(Constants_1.DockerComposeFiles.localNetwork, "debug-cli", "/etc/hyperledger/fabric/scripts/packageCaasChaincode.sh", chaincodeArgs)).replace("\n", "");
        Constants_1.Settings.debugCaasEnv.CHAINCODE_ID = Constants_1.Settings.defaultChaincodePackageId;
        //Install the chaincode on the peers
        await ShellCommand_1.ShellCommand.execDockerComposeBash(Constants_1.DockerComposeFiles.localNetwork, "debug-cli", "/etc/hyperledger/fabric/scripts/installCaasChaincode.sh", chaincodeArgs);
    }
    static async shouldRestart(debugConfiguration) {
        let shouldRestart = false;
        //If external chaincode setting has changed, we should restart
        if (Constants_1.Settings.isCaas !== debugConfiguration.isCaas) {
            shouldRestart = true;
        }
        //if chaincode name has changed, we should restart
        if (debugConfiguration.chaincodeName && Constants_1.Settings.defaultChaincodeId !== debugConfiguration.chaincodeName) {
            shouldRestart = true;
        }
        //Check if all the docker containers are running. If not, we should try to restart
        const result = await ShellCommand_1.ShellCommand.runDockerCompose(Constants_1.DockerComposeFiles.localNetwork, ["ls", "--filter", `name=${Constants_1.Settings.singleOrgProj}`], false);
        if (result.toLowerCase().indexOf("running(5)") === -1) {
            shouldRestart = true;
        }
        return shouldRestart;
    }
    static async startChaincodeListener() {
        const logger = Logger_1.Logger.instance();
        try {
            let contract;
            if (!HlfProvider.contracts.has(Constants_1.Settings.defaultChaincodeId)) {
                //Create wallet from the admin user's certificate and key
                const mspPath = path.join(Constants_1.Settings.dockerDir, '..', '..', 'local', 'organizations', 'peerOrganizations', Constants_1.Settings.singleOrgSettings.domain, 'users', Constants_1.Settings.singleOrgSettings.adminUser, 'msp');
                const certPath = path.join(mspPath, 'signcerts', 'cert.pem');
                const keyPath = path.join(mspPath, 'keystore');
                let privatekey = '';
                const files = fs.readdirSync(keyPath);
                files.forEach(function (file) {
                    privatekey = fs.readFileSync(path.join(keyPath, file), 'utf8');
                });
                const certificate = fs.readFileSync(certPath, 'utf8');
                if (!certificate || !privatekey) {
                    logger.log(Constants_1.LogType.warning, "Certificate or private key not found for admin user. Skipping Event listener setup. Events won't be streamed to the output.");
                    return;
                }
                const x509Identity = {
                    credentials: {
                        certificate: certificate,
                        privateKey: privatekey,
                    },
                    mspId: Constants_1.Settings.singleOrgSettings.msp,
                    type: 'X.509',
                };
                const wallet = await fabric_network_1.Wallets.newInMemoryWallet();
                await wallet.put(Constants_1.Settings.singleOrgSettings.adminUser, x509Identity);
                const ccpPath = path.join(Constants_1.Settings.dockerDir, '..', '..', 'sampleconfig', 'ccp', Constants_1.Settings.singleOrgSettings.ccpFileName);
                const fileExists = fs.existsSync(ccpPath);
                if (!fileExists) {
                    logger.log(Constants_1.LogType.warning, "CCP profile not found. Skipping Event listener setup. Events won't be streamed to the output.");
                    return;
                }
                const contents = fs.readFileSync(ccpPath, 'utf8');
                const ccp = JSON.parse(contents);
                const gateway = new fabric_network_1.Gateway();
                await gateway.connect(ccp, {
                    wallet,
                    identity: Constants_1.Settings.singleOrgSettings.adminUser,
                    discovery: { enabled: false, asLocalhost: true } // using asLocalhost as this gateway is using a fabric network deployed locally
                });
                const network = await gateway.getNetwork(Constants_1.Settings.defaultChannel);
                contract = network.getContract(Constants_1.Settings.defaultChaincodeId);
                HlfProvider.contracts.set(Constants_1.Settings.defaultChaincodeId, contract);
            }
            else {
                contract = HlfProvider.contracts.get(Constants_1.Settings.defaultChaincodeId);
            }
            //Cleanup any existing listener
            contract.removeContractListener(HlfProvider.listener);
            //Add a new event listener
            const checkpointer = await fabric_network_1.DefaultCheckpointers.file(path.join(Constants_1.Settings.dockerDir, '..', '..', 'local', 'checkpointer'));
            await contract.addContractListener(HlfProvider.listener, { checkpointer: checkpointer });
        }
        catch (error) {
            logger.log(Constants_1.LogType.warning, `Skipping Event listener setup. Events won't be streamed to the output. ${error}`);
        }
    }
    static async openCouchDb() {
        vscode.window.showInformationMessage("Credentials for login to CouchDB.\nUsername: admin\nPassword: adminpw", { modal: true, detail: `Navigate to the database 'default_${Constants_1.Settings.defaultChaincodeId}' to view the documents.` })
            .then(() => {
            vscode.commands.executeCommand('vscode.open', vscode.Uri.parse(Constants_1.Settings.singleOrgSettings.couchDbUrl));
        });
    }
}
exports.HlfProvider = HlfProvider;
_a = HlfProvider;
HlfProvider.islocalNetworkStarted = false;
HlfProvider.contracts = new Map();
HlfProvider.listener = async (event) => {
    const transaction = event.getTransactionEvent();
    Logger_1.Logger.instance().log(Constants_1.LogType.info, `Chaincode Event: Name: ${event.eventName}, Block No: ${transaction.getBlockEvent().blockNumber}, Transaction Id: ${transaction.transactionId}, Payload: ${event.payload.toString()}`);
};
//# sourceMappingURL=HlfProvider.js.map