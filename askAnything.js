"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.askAnythingCommand = void 0;
const askAnythingCommand = async (editor, openAiApi) => {
    const prompt = await editor.getUserInput('Enter your question', 'What is polymorphism?', 'Invalid question');
    if (prompt !== undefined) {
        const response = await openAiApi.makeRequestWithLoadingIndicator(prompt, editor);
        if (response !== undefined) {
            editor.writeToConsole(response);
        }
    }
    else {
        void editor.showErrorMessage('No prompt entered');
    }
};
exports.askAnythingCommand = askAnythingCommand;
//# sourceMappingURL=askAnything.js.map