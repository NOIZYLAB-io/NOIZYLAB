"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ts_mockito_1 = require("ts-mockito");
const askAnything_1 = require("../../commands/askAnything");
suite('Ask anything command - test suite', () => {
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
    test('when the user enters a question, the API is called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your question', 'What is polymorphism?', 'Invalid question')).thenReturn(Promise.resolve('some question'));
        await (0, askAnything_1.askAnythingCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).once();
    });
    test('when the user does not enter a question, the API is not called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your question', 'What is polymorphism?', 'Invalid question')).thenReturn(Promise.resolve(undefined));
        await (0, askAnything_1.askAnythingCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).never();
    });
    test('when the API returns a response, it is written to the console', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your question', 'What is polymorphism?', 'Invalid question')).thenReturn(Promise.resolve('some question'));
        (0, ts_mockito_1.when)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).thenReturn(Promise.resolve('some response'));
        await (0, askAnything_1.askAnythingCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedEditor.writeToConsole('some response')).once();
    });
});
//# sourceMappingURL=askAnything.test.js.map