"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ResourcesTreeProvider = void 0;
const path = require("path");
const vscode = require("vscode");
const Constants_1 = require("../utilities/Constants");
const ResourceItem_1 = require("../views/trees/ResourceItem");
class ResourcesTreeProvider {
    getTreeItem(element) {
        return element.getTreeItem();
    }
    async getChildren(element) {
        const tree = [];
        if (!element) {
            tree.push(new ResourceItem_1.ResourceItem("Documentation", "Extension Documentation", new vscode.ThemeIcon("book"), Constants_1.Links.documentation));
            tree.push(new ResourceItem_1.ResourceItem("Contribute", "Contribute to this Extension", new vscode.ThemeIcon("git-pull-request"), Constants_1.Links.contribute));
            tree.push(new ResourceItem_1.ResourceItem("Report an Issue", "Report issues or make feature requests", new vscode.ThemeIcon("bug"), Constants_1.Links.reportIssue));
            tree.push(new ResourceItem_1.ResourceItem("Review", "Share your love for this extension", new vscode.ThemeIcon("comment-discussion"), Constants_1.Links.review));
            tree.push(new ResourceItem_1.ResourceItem("Contact Spydra", "Learn more about how our services can support your business", path.join(__filename, '..', '..', '..', 'media', 'spydra-blue.png'), Constants_1.Links.contactUs));
        }
        return Promise.resolve(tree);
    }
}
exports.ResourcesTreeProvider = ResourcesTreeProvider;
//# sourceMappingURL=ResourcesTreeProvider.js.map