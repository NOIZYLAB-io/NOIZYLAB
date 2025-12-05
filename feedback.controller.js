"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FeedbackController = void 0;
const vscode_1 = require("vscode");
const configs_1 = require("../configs");
/**
 * FeedbackController manages user feedback actions (About Us, Report Issues, Rate Us, Support Us).
 * All public methods are documented with JSDoc for clarity and maintainability.
 *
 * @class FeedbackController
 * @module controllers/feedback.controller
 */
class FeedbackController {
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructor for the FeedbackController class.
     *
     * @constructor
     * @public
     * @memberof FeedbackController
     */
    constructor() { }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * Opens the extension's marketplace page in the browser.
     */
    aboutUs() {
        vscode_1.env.openExternal(vscode_1.Uri.parse(configs_1.EXTENSION_MARKETPLACE_URL));
    }
    /**
     * Opens the extension's repository issues page in the browser.
     */
    reportIssues() {
        vscode_1.env.openExternal(vscode_1.Uri.parse(`${configs_1.EXTENSION_REPOSITORY_URL}/issues`));
    }
    /**
     * Opens the review page for the extension in the marketplace.
     */
    rateUs() {
        vscode_1.env.openExternal(vscode_1.Uri.parse(`${configs_1.EXTENSION_MARKETPLACE_URL}&ssr=false#review-details`));
    }
    /**
     * Shows support options (Sponsor, Buy Me a Coffee) and opens the selected link.
     * @returns Promise resolved when the user selects an option or cancels.
     */
    async supportUs() {
        // Create the actions
        const actions = [
            { title: vscode_1.l10n.t('Become a Sponsor') },
            { title: vscode_1.l10n.t('Buy Me a Coffee') },
        ];
        // Show the message
        const message = vscode_1.l10n.t('Although {0} is offered at no cost, your support is deeply appreciated if you find it beneficial. Thank you for considering!', configs_1.EXTENSION_DISPLAY_NAME);
        const option = await vscode_1.window.showInformationMessage(message, ...actions);
        // Handle the actions
        switch (option?.title) {
            case actions[0].title:
                vscode_1.env.openExternal(vscode_1.Uri.parse(configs_1.EXTENSION_SPONSOR_URL));
                break;
            case actions[1].title:
                vscode_1.env.openExternal(vscode_1.Uri.parse(configs_1.EXTENSION_BUY_ME_A_COFFEE_URL));
                break;
        }
    }
}
exports.FeedbackController = FeedbackController;
//# sourceMappingURL=feedback.controller.js.map