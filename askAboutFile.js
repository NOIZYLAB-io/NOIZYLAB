"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.askAboutFileCommand = void 0;
const askAboutFileCommand = async (editor, openAiApi) => {
    const fileContents = editor.getCurrentFileContents();
    const userQuestion = await editor.getUserInput('Enter your question', 'What does this code do?', 'Invalid question');
    if (fileContents.length > 0 && userQuestion !== undefined) {
        const prompt = `${userQuestion}: ${fileContents}`;
        const response = await openAiApi.makeRequestWithLoadingIndicator(prompt, editor);
        if (response !== undefined) {
            editor.writeToConsole(response);
        }
    }
    else {
        editor.showErrorMessage('File is empty');
    }
};
exports.askAboutFileCommand = askAboutFileCommand;
//# sourceMappingURL=askAboutFile.js.map