"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ts_mockito_1 = require("ts-mockito");
const askAboutSelection_1 = require("../../commands/askAboutSelection");
suite('Ask about selection command - test suite', () => {
    let editor;
    let mockedEditor;
    let openAiApi;
    let mockedOpenAiApi;
    setup(() => {
        mockedEditor = (0, ts_mockito_1.mock)();
        editor = (0, ts_mockito_1.instance)(mockedEditor);
        mockedOpenAiApi = (0, ts_mockito_1.mock)();
        openAiApi = (0, ts_mockito_1.instance)(mockedOpenAiApi);
    });
    test('when the selection is empty, an error is shown', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getHighlightedText()).thenReturn('');
        await (0, askAboutSelection_1.askAboutSelectionCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedEditor.showErrorMessage('No text highlighted')).once();
    });
    test('when the selection is not empty, the user is prompted for a question', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getHighlightedText()).thenReturn('some code');
        await (0, askAboutSelection_1.askAboutSelectionCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedEditor.getUserInput('Enter your question', 'What does this code do?', 'Invalid question')).once();
    });
    test('when the user enters a question, the API is called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getHighlightedText()).thenReturn('some code');
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your question', 'What does this code do?', 'Invalid question')).thenReturn(Promise.resolve('some question'));
        await (0, askAboutSelection_1.askAboutSelectionCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).once();
    });
    test('when the user does not enter a question, the API is not called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getHighlightedText()).thenReturn('some code');
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your question', 'What does this code do?', 'Invalid question')).thenReturn(Promise.resolve(undefined));
        await (0, askAboutSelection_1.askAboutSelectionCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).never();
    });
    test('when the API returns a response, it is written to the console', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getHighlightedText()).thenReturn('some code');
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your question', 'What does this code do?', 'Invalid question')).thenReturn(Promise.resolve('some question'));
        (0, ts_mockito_1.when)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).thenReturn(Promise.resolve('some response'));
        await (0, askAboutSelection_1.askAboutSelectionCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedEditor.writeToConsole('some response')).once();
    });
});
//# sourceMappingURL=askAboutSelection.test.js.map