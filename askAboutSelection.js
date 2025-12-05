"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.askAboutSelectionCommand = void 0;
const askAboutSelectionCommand = async (editor, openAiApi) => {
    const highlighted = editor.getHighlightedText();
    const userQuestion = await editor.getUserInput('Enter your question', 'What does this code do?', 'Invalid question');
    if (highlighted.length > 0 && userQuestion !== undefined) {
        const prompt = `${userQuestion}: ${highlighted}`;
        const response = await openAiApi.makeRequestWithLoadingIndicator(prompt, editor);
        if (response !== undefined) {
            editor.writeToConsole(response);
        }
    }
    else {
        void editor.showErrorMessage('No text highlighted');
    }
};
exports.askAboutSelectionCommand = askAboutSelectionCommand;
//# sourceMappingURL=askAboutSelection.js.map