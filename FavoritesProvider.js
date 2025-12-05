"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Resource = exports.FavoritesProvider = void 0;
const vscode = require("vscode");
const fs = require("fs");
const path = require("path");
const os = require("os");
const util_1 = require("../helper/util");
const configMgr_1 = require("../helper/configMgr");
const enum_1 = require("../enum");
class FavoritesProvider {
    constructor() {
        this._onDidChangeTreeData = new vscode.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
    }
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    getTreeItem(element) {
        return element;
    }
    getChildren(element) {
        return this.getSortedFavoriteResources().then((resources) => {
            if (!resources || !resources.length) {
                return [];
            }
            const currentGroup = configMgr_1.default.get('currentGroup') || enum_1.DEFAULT_GROUP;
            if (!element) {
                return Promise.all(resources.map((r) => this.getResourceStat(r)))
                    .then((data) => {
                    return data.filter((i) => i.stat !== enum_1.FileStat.NEITHER);
                })
                    .then((data) => {
                    return data.filter((i) => i.group === currentGroup);
                })
                    .then((data) => this.data2Resource(data, 'resource'));
            }
            return this.getChildrenResources({ filePath: element.value, group: currentGroup });
        });
    }
    getChildrenResources(item) {
        const sort = vscode.workspace.getConfiguration('favorites').get('sortOrder');
        if (item.filePath.match(/^[A-Za-z][A-Za-z0-9+-.]*:\/\//)) {
            // filePath is a uri string
            const uri = vscode.Uri.parse(item.filePath);
            return vscode.workspace.fs
                .readDirectory(uri)
                .then((entries) => this.sortResources(entries.map((e) => ({ filePath: vscode.Uri.joinPath(uri, e[0]).toString(), group: '' })), sort === 'MANUAL' ? 'ASC' : sort))
                .then((items) => this.data2Resource(items, 'resourceChild'));
        }
        // Not a uri string
        return new Promise((resolve, reject) => {
            fs.readdir((0, util_1.pathResolve)(item.filePath), (err, files) => {
                if (err) {
                    return resolve([]);
                }
                this.sortResources(files.map((f) => ({ filePath: path.join(item.filePath, f), group: '' })), sort === 'MANUAL' ? 'ASC' : sort)
                    .then((data) => this.data2Resource(data, 'resourceChild'))
                    .then(resolve);
            });
        });
    }
    getSortedFavoriteResources() {
        const resources = (0, util_1.getCurrentResources)();
        const sort = vscode.workspace.getConfiguration('favorites').get('sortOrder');
        if (sort === 'MANUAL') {
            return Promise.resolve(resources);
        }
        return this.sortResources(resources.map((item) => item), sort).then((res) => res.map((r) => ({ filePath: r.filePath, group: r.group })));
    }
    sortResources(resources, sort) {
        return Promise.all(resources.map((r) => this.getResourceStat(r))).then((resourceStats) => {
            const isAsc = sort === 'ASC';
            resourceStats.sort(function (a, b) {
                const aName = path.basename(a.filePath);
                const bName = path.basename(b.filePath);
                const aStat = a.stat;
                const bStat = b.stat;
                if (aStat === enum_1.FileStat.DIRECTORY && bStat === enum_1.FileStat.FILE) {
                    return -1;
                }
                if (aStat === enum_1.FileStat.FILE && bStat === enum_1.FileStat.DIRECTORY) {
                    return 1;
                }
                if (aName < bName) {
                    return isAsc ? -1 : 1;
                }
                return aName === bName ? 0 : isAsc ? 1 : -1;
            });
            return resourceStats;
        });
    }
    getResourceStat(item) {
        return new Promise((resolve) => {
            if (item.filePath.match(/^[A-Za-z][A-Za-z0-9+-.]*:\/\//)) {
                // filePath is a uri string
                const uri = vscode.Uri.parse(item.filePath);
                resolve(vscode.workspace.fs.stat(uri).then((fileStat) => {
                    if (fileStat.type === vscode.FileType.File) {
                        return {
                            filePath: item.filePath,
                            stat: enum_1.FileStat.FILE,
                            uri,
                            group: item.group,
                        };
                    }
                    if (fileStat.type === vscode.FileType.Directory) {
                        return {
                            filePath: item.filePath,
                            stat: enum_1.FileStat.DIRECTORY,
                            uri,
                            group: item.group,
                        };
                    }
                    return {
                        filePath: item.filePath,
                        stat: enum_1.FileStat.NEITHER,
                        uri,
                        group: item.group,
                    };
                }));
            }
            else {
                // filePath is a file path
                fs.stat((0, util_1.pathResolve)(item.filePath), (err, stat) => {
                    if (err) {
                        return resolve({
                            filePath: item.filePath,
                            stat: enum_1.FileStat.NEITHER,
                            group: item.group,
                        });
                    }
                    if (stat.isDirectory()) {
                        return resolve({
                            filePath: item.filePath,
                            stat: enum_1.FileStat.DIRECTORY,
                            group: item.group,
                        });
                    }
                    if (stat.isFile()) {
                        return resolve({
                            filePath: item.filePath,
                            stat: enum_1.FileStat.FILE,
                            group: item.group,
                        });
                    }
                    return resolve({
                        filePath: item.filePath,
                        stat: enum_1.FileStat.NEITHER,
                        group: item.group,
                    });
                });
            }
        });
    }
    data2Resource(data, contextValue) {
        const enablePreview = vscode.workspace.getConfiguration('workbench.editor').get('enablePreview');
        // contextValue set on Resource gets a 'uri.' prefix if the favorite is specified as a uri,
        //   and a '.dir' suffix if it represents a directory rather than a file.
        // The when-clauses on our contributions to the 'view/item/context' menu use these modifiers
        //   to be smarter about which commands to offer.
        return data.map((i) => {
            if (!i.uri) {
                let uri = vscode.Uri.parse(`file://${(0, util_1.pathResolve)(i.filePath)}`);
                if (os.platform().startsWith('win')) {
                    uri = vscode.Uri.parse(`file:///${(0, util_1.pathResolve)(i.filePath)}`.replace(/\\/g, '/'));
                }
                if (i.stat === enum_1.FileStat.DIRECTORY) {
                    return new Resource(path.basename(i.filePath), vscode.TreeItemCollapsibleState.Collapsed, i.filePath, contextValue + '.dir', undefined, uri);
                }
                return new Resource(path.basename(i.filePath), vscode.TreeItemCollapsibleState.None, i.filePath, contextValue, {
                    command: 'favorites.open',
                    title: '',
                    arguments: [uri],
                }, uri);
            }
            else {
                if (i.stat === enum_1.FileStat.DIRECTORY) {
                    return new Resource(path.basename(i.filePath), vscode.TreeItemCollapsibleState.Collapsed, i.filePath, 'uri.' + contextValue + '.dir', undefined, i.uri);
                }
                return new Resource(path.basename(i.filePath), vscode.TreeItemCollapsibleState.None, i.filePath, 'uri.' + contextValue, {
                    command: 'favorites.open',
                    title: '',
                    arguments: [i.uri],
                }, i.uri);
            }
        });
    }
}
exports.FavoritesProvider = FavoritesProvider;
class Resource extends vscode.TreeItem {
    constructor(label, collapsibleState, value, contextValue, command, uri) {
        super(label, collapsibleState);
        this.label = label;
        this.collapsibleState = collapsibleState;
        this.value = value;
        this.contextValue = contextValue;
        this.command = command;
        this.uri = uri;
        this.resourceUri = uri ? uri : vscode.Uri.file(value);
        this.tooltip = value;
    }
}
exports.Resource = Resource;

//# sourceMappingURL=FavoritesProvider.js.map
