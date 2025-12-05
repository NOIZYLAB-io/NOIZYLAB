"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.OpenAIWrapper = void 0;
const openai_1 = require("openai");
const vscode = require("vscode");
class OpenAIWrapper {
    async makeRequestWithLoadingIndicator(text, editor) {
        let response;
        await vscode.window.withProgress({
            location: vscode.ProgressLocation.Window,
            cancellable: false,
            title: 'Loading response...'
        }, async (progress) => {
            progress.report({ increment: 0 });
            response = await this.makeRequest(text, editor);
            progress.report({ increment: 100 });
        });
        return response;
    }
    async makeRequest(text, editor) {
        const config = new openai_1.Configuration({
            apiKey: await editor.getSecret('openai-api-key'),
            organization: editor.getConfigValue('organization')
        });
        const openai = new openai_1.OpenAIApi(config);
        const response = await openai.createCompletion({
            prompt: text,
            max_tokens: editor.getConfigValue('maxTokens'),
            temperature: editor.getConfigValue('temperature'),
            model: editor.getConfigValue('model'),
            n: 1,
            stream: false
        });
        return response.data.choices[0].text;
    }
}
exports.OpenAIWrapper = OpenAIWrapper;
//# sourceMappingURL=OpenAIWrapper.js.map