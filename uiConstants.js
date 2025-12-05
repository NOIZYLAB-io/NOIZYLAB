"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.cssStyles = void 0;
// CSS Styles
var cssStyles;
(function (cssStyles) {
    cssStyles.text = { 'user-select': 'text', 'cursor': 'text' };
    cssStyles.tableHeader = { ...cssStyles.text, 'text-align': 'left', 'border': 'none', 'font-size': '12px', 'font-weight': 'normal', 'color': '#666666' };
    cssStyles.tableRow = { ...cssStyles.text, 'border-top': 'solid 1px #ccc', 'border-bottom': 'solid 1px #ccc', 'border-left': 'none', 'border-right': 'none', 'font-size': '12px' };
    cssStyles.fontWeightBold = { 'font-weight': 'bold' };
    cssStyles.titleFontSize = 13;
    cssStyles.optionsTableHeader = { 'display': 'none', 'border': 'none !important' };
    cssStyles.optionsTableRowLabel = { ...cssStyles.text, 'border-left': 'none', 'border-right': 'none', 'border-top': 'none', 'border-bottom': 'none' };
    cssStyles.optionsTableRowCheckbox = { 'border-left': 'none', 'border-right': 'none', 'border-top': 'none', 'border-bottom': 'none' };
    cssStyles.publishDialogLabelWidth = '205px';
    cssStyles.publishDialogTextboxWidth = '190px';
    cssStyles.publishDialogDropdownWidth = '192px';
    cssStyles.PublishingOptionsButtonWidth = '100px';
    cssStyles.addDatabaseReferenceDialogLabelWidth = '215px';
    cssStyles.addDatabaseReferenceInputboxWidth = '220px';
    cssStyles.createProjectFromDatabaseLabelWidth = '110px';
    cssStyles.createProjectFromDatabaseTextboxWidth = '300px';
    cssStyles.updateProjectFromDatabaseLabelWidth = '110px';
    cssStyles.updateProjectFromDatabaseTextboxWidth = '300px';
    // font-styles
    let fontStyle;
    (function (fontStyle) {
        fontStyle.normal = 'normal';
        fontStyle.italics = 'italic';
    })(fontStyle = cssStyles.fontStyle || (cssStyles.fontStyle = {}));
})(cssStyles || (exports.cssStyles = cssStyles = {}));
//# sourceMappingURL=uiConstants.js.map