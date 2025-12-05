"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.setupCommand = void 0;
const validateInput = (value) => {
    if (value === undefined) {
        return false;
    }
    if (value.length === 0) {
        return false;
    }
    return true;
};
const setupCommand = async (editor) => {
    await editor.getUserInput('Enter your OpenAI API Key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Invalid API Key', true).then((key) => {
        if (validateInput(key) && key !== undefined) {
            editor.setSecret('openai-api-key', key);
        }
    });
};
exports.setupCommand = setupCommand;
//# sourceMappingURL=setup.js.map