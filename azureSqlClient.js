"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.AzureSqlClient = void 0;
const utils = require("../../common/utils");
/**
 * Client module to call Azure APIs for getting or creating resources
 */
class AzureSqlClient {
    _azureAccountServiceFactory;
    _azureResourceServiceFactory;
    constructor(_azureAccountServiceFactory = utils.defaultAzureAccountServiceFactory, _azureResourceServiceFactory = utils.defaultAzureResourceServiceFactory) {
        this._azureAccountServiceFactory = _azureAccountServiceFactory;
        this._azureResourceServiceFactory = _azureResourceServiceFactory;
    }
    /**
     * Returns existing Azure accounts
     */
    async getAccounts() {
        const azureAccountService = await this._azureAccountServiceFactory();
        return await azureAccountService.getAccounts();
    }
    /**
     * Prompt user to login to Azure and returns the account
     * @returns Azure account that user logged in to
     */
    async getAccount() {
        const azureAccountService = await this._azureAccountServiceFactory();
        return await azureAccountService.addAccount();
    }
    /**
     * Returns Azure locations for given subscription
     */
    async getLocations(session) {
        const azureResourceService = await this._azureResourceServiceFactory();
        return await azureResourceService.getLocations(session);
    }
    /**
     * Returns Azure sessions with subscription, tenant and token for given account
     */
    async getSessions(account) {
        const azureAccountService = await this._azureAccountServiceFactory();
        return await azureAccountService.getAccountSessions(account);
    }
    /**
     * Creates a new Azure SQL server for given subscription, resource group and location
     */
    async createOrUpdateServer(session, resourceGroupName, serverName, parameters) {
        const azureResourceService = await this._azureResourceServiceFactory();
        return await azureResourceService.createOrUpdateServer(session, resourceGroupName, serverName, parameters);
    }
    /**
     * Returns Azure resource groups for given subscription
     */
    async getResourceGroups(session) {
        const azureResourceService = await this._azureResourceServiceFactory();
        return await azureResourceService.getResourceGroups(session);
    }
}
exports.AzureSqlClient = AzureSqlClient;
//# sourceMappingURL=azureSqlClient.js.map