"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.DeployOptionsModel = void 0;
const vscode = require("vscode");
const constants = require("../../common/constants");
const uiConstants_1 = require("../../common/uiConstants");
class DeployOptionsModel {
    deploymentOptions;
    // key is the option display name and values are checkboxValue and optionName
    optionsValueNameLookup = {};
    excludeObjectTypesLookup = {};
    constructor(deploymentOptions) {
        this.deploymentOptions = deploymentOptions;
        this.setOptionsToValueNameLookup();
        this.setExcludeObjectTypesLookup();
    }
    /*
     * Sets deployment option's checkbox values and property name to the optionsValueNameLookup map
     */
    setOptionsToValueNameLookup() {
        Object.entries(this.deploymentOptions.booleanOptionsDictionary).forEach(option => {
            const optionValue = {
                optionName: option[0],
                checked: option[1].value
            };
            this.optionsValueNameLookup[option[1].displayName] = optionValue;
        });
    }
    /*
     * Initialize options data from deployment options for table component
     * Returns data as [booleanValue, optionName]
     */
    getOptionsData() {
        let data = [];
        Object.entries(this.deploymentOptions.booleanOptionsDictionary).forEach(option => {
            // option[1] holds checkedbox value and displayName
            data.push([
                {
                    value: option[1].value,
                    style: uiConstants_1.cssStyles.optionsTableRowCheckbox,
                    ariaLabel: option[1].displayName
                },
                {
                    value: option[1].displayName,
                    style: uiConstants_1.cssStyles.optionsTableRowLabel,
                }
            ]);
        });
        return data.sort((a, b) => a[1].value.localeCompare(b[1].value));
    }
    /*
    * Sets the selected option checkbox value to the deployment options
    */
    setDeploymentOptions() {
        Object.entries(this.optionsValueNameLookup).forEach(option => {
            // option[1] holds checkedbox value and optionName
            this.deploymentOptions.booleanOptionsDictionary[option[1].optionName].value = option[1].checked;
        });
    }
    /*
    * Sets the checkbox value to the optionsValueNameLookup map
    */
    setOptionValue(displayName, checked) {
        this.optionsValueNameLookup[displayName].checked = checked;
    }
    /*
    * Gets the description of the selected option by getting the option name from the optionsValueNameLookup
    */
    getOptionDescription(displayName) {
        const optionName = this.optionsValueNameLookup[displayName];
        if (optionName === undefined) {
            void vscode.window.showWarningMessage(constants.OptionNotFoundWarningMessage(displayName));
        }
        return optionName !== undefined ? this.deploymentOptions.booleanOptionsDictionary[optionName.optionName].description : '';
    }
    /*
     * Sets exclude object types option's checkbox values and property name to the excludeObjectTypesLookup map
     */
    setExcludeObjectTypesLookup() {
        Object.entries(this.deploymentOptions.objectTypesDictionary).forEach(option => {
            const optionValue = {
                optionName: option[0],
                checked: this.getExcludeObjectTypeOptionCheckStatus(option[0])
            };
            this.excludeObjectTypesLookup[option[1]] = optionValue;
        });
    }
    /*
     * Initialize options data from objectTypesDictionary for table component
     * Returns data as [booleanValue, optionName]
     */
    getExcludeObjectTypesOptionsData() {
        let data = [];
        Object.entries(this.deploymentOptions.objectTypesDictionary).forEach(option => {
            // option[1] is the display name and option[0] is the optionName
            data.push([
                {
                    value: this.getExcludeObjectTypeOptionCheckStatus(option[0]),
                    style: uiConstants_1.cssStyles.optionsTableRowCheckbox,
                    ariaLabel: option[1]
                },
                {
                    value: option[1],
                    style: uiConstants_1.cssStyles.optionsTableRowLabel
                }
            ]);
        });
        return data.sort((a, b) => a[1].value.localeCompare(b[1].value));
    }
    /*
    * Gets the selected/default value of the object type option
    * return true for the deploymentOptions.excludeObjectTypes option, if it is in ObjectTypesDictionary
    */
    getExcludeObjectTypeOptionCheckStatus(optionName) {
        return (this.deploymentOptions.excludeObjectTypes.value?.find(x => x.toLowerCase() === optionName.toLowerCase())) !== undefined ? true : false;
    }
    /*
    * Sets the checkbox value to the excludeObjectTypesLookup map
    */
    setExcludeObjectTypesOptionValue(displayName, checked) {
        this.excludeObjectTypesLookup[displayName].checked = checked;
    }
    /*
    * Sets the selected option checkbox value to the deployment options
    */
    setExcludeObjectTypesToDeploymentOptions() {
        let finalExcludedObjectTypes = [];
        Object.entries(this.excludeObjectTypesLookup).forEach(option => {
            // option[1] holds checkedbox value and optionName
            if (option[1].checked) {
                finalExcludedObjectTypes.push(option[1].optionName);
            }
        });
        this.deploymentOptions.excludeObjectTypes.value = finalExcludedObjectTypes;
    }
}
exports.DeployOptionsModel = DeployOptionsModel;
//# sourceMappingURL=deployOptionsModel.js.map