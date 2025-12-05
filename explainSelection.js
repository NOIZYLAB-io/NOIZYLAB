"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.explainSelectionCommand = void 0;
const explainSelectionCommand = async (editor, openAiApi) => {
    const highlighted = editor.getHighlightedText();
    if (highlighted.length > 0) {
        const prompt = `Explain the following ${editor.getCurrentFileExtension()} code: ${highlighted}`;
        const response = await openAiApi.makeRequestWithLoadingIndicator(prompt, editor);
        if (response !== undefined) {
            editor.writeToConsole(response);
        }
    }
    else {
        void editor.showErrorMessage('No text highlighted');
    }
};
exports.explainSelectionCommand = explainSelectionCommand;
//# sourceMappingURL=explainSelection.js.map