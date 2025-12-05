"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = createPrompt;
function createPrompt(question, settings, selection) {
    console.log("createPrompt called with:", { question, settings, selection }); // Debug log
    let prompt = selection
        ? `${question}\n${settings.selectedInsideCodeblock ? "```\n" : ""}${selection}\n${settings.selectedInsideCodeblock ? "```\n" : ""}`
        : question;
    if (settings.model !== "ChatGPT") {
        prompt = `Role: DevPal, a helpful coding expert who is never verbose and always truthful, you assist USER. Use markdown, always wrap code in codeblocks. Follow formats strictly, responses short, simplified. DO NOT ANSWER anything apart from the Code related query in any language.
    \n\nUSER: ${prompt}\n\DevPal: `;
    }
    else {
        prompt = `Role: DevPal, a helpful coding expert who is never verbose and always truthful, you assist USER. Use markdown, always wrap code in codeblocks. Follow formats strictly, responses short, simplified.DO NOT ANSWER anything apart from the Code related query in any language.
    \n\nUSER: ${prompt}\n\DevPal: `;
    }
    return prompt;
}
//# sourceMappingURL=prompt.js.map