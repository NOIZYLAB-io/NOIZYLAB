"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FileController = void 0;
const vscode_1 = require("vscode");
const helpers_1 = require("../helpers");
/**
 * FileController handles file generation and management for Angular elements.
 * All public methods are documented with JSDoc for clarity and maintainability.
 *
 * @class FileController
 * @module controllers/file.controller
 */
class FileController {
    config;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructor for the FileController class.
     *
     * @constructor
     * @param {Config} config - The configuration
     * @public
     * @memberof FileController
     */
    constructor(config) {
        this.config = config;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * Generates a new class file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateClass(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        // Get the type
        let type = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the type name'), vscode_1.l10n.t('E.g. class, dto, entity, model...'), helpers_1.validateEntityName);
        if (!type) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `export class ${className}${(0, helpers_1.titleize)(type)} {}
`;
        type = type.length !== 0 ? `.${type}` : '';
        const filename = `${(0, helpers_1.dasherize)(className)}${type}.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular component file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateComponent(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the component class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const omitSuffix = this.config.omitSuffix;
        let content;
        if (this.config.standalone) {
            content = `import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-${(0, helpers_1.dasherize)(className)}',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.component'}.html',
  styleUrls: ['./${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.component'}.${this.config.style}'],
})
export class ${className}${omitSuffix ? '' : 'Component'} {}
`;
        }
        else {
            content = `import { Component } from '@angular/core';

@Component({
  selector: 'app-${(0, helpers_1.dasherize)(className)}',
  templateUrl: './${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.component'}.html',
  styleUrls: ['./${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.component'}.${this.config.style}'],
})
export class ${className}${omitSuffix ? '' : 'Component'} {}
`;
        }
        const filename = `${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.component'}.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular directive file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateDirective(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the directive class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const omitSuffix = this.config.omitSuffix;
        const content = `import { Directive } from '@angular/core';

@Directive({
  selector: '[app${className}]',
})
export class ${className}${omitSuffix ? '' : 'Directive'} {}
`;
        const filename = `${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.directive'}.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new TypeScript enum file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateEnum(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the enum class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `export enum ${className} {}
`;
        const omitSuffix = this.config.omitSuffix;
        const filename = `${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.enum'}.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular guard file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateGuard(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const entityName = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the guard name'), vscode_1.l10n.t('E.g. user, role, auth...'), (name) => {
            if (!/^[a-z][\w-]+$/.test(name)) {
                return vscode_1.l10n.t('Invalid format! Entity names MUST be declared in camelCase and have at least 1 character (e.g. user, authService)');
            }
            return;
        });
        if (!entityName) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const guardType = await (0, helpers_1.pickItem)(['CanActivate', 'CanActivateChild', 'CanDeactivate', 'CanMatch'], vscode_1.l10n.t('Which type of guard would you like to create?'));
        let params = '';
        switch (guardType) {
            case 'CanActivate':
                params = vscode_1.l10n.t('route, state');
                break;
            case 'CanActivateChild':
                params = vscode_1.l10n.t('childRoute, state');
                break;
            case 'CanDeactivate':
                params = vscode_1.l10n.t('component, currentRoute, currentState, nextState');
                break;
            case 'CanMatch':
                params = vscode_1.l10n.t('route, segments');
                break;
        }
        const content = `import { ${guardType}Fn } from '@angular/router';

export const ${entityName}Guard: ${guardType}Fn = (${params}) => {
  return true;
};
`;
        const filename = `${(0, helpers_1.dasherize)(entityName)}${this.config.typeSeparator}guard.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular interceptor file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateInterceptor(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the interceptor class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class ${className}Interceptor implements HttpInterceptor {
  intercept(
    request: HttpRequest<unknown>,
    next: HttpHandler
  ): Observable<HttpEvent<unknown>> {
    return next.handle(request);
  }
}
`;
        const filename = `${(0, helpers_1.dasherize)(className)}${this.config.typeSeparator}interceptor.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new interface file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateInterface(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the interface class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        // Get the type
        let type = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the interface type name'), vscode_1.l10n.t('E.g. interface, dto, entity, model...'), helpers_1.validateEntityName);
        if (!type) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `export interface ${className}${(0, helpers_1.titleize)(type)} {}
`;
        type = type.length !== 0 ? `.${type}` : '';
        const filename = `${(0, helpers_1.dasherize)(className)}${type}.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular module file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateModule(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the module class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

@NgModule({
  declarations: [],
  imports: [CommonModule],
})
export class ${className}Module {}
`;
        const filename = `${(0, helpers_1.dasherize)(className)}${this.config.typeSeparator}module.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular pipe file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generatePipe(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the pipe class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: '${(0, helpers_1.dasherize)(className)}',
})
export class ${className}Pipe implements PipeTransform {
  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }
}
`;
        const filename = `${(0, helpers_1.dasherize)(className)}${this.config.typeSeparator}pipe.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular resolver file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateResolver(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the resolver class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `import { Injectable } from '@angular/core';
import {
  Router,
  Resolve,
  RouterStateSnapshot,
  ActivatedRouteSnapshot,
} from '@angular/router';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ${className}Resolver implements Resolve<boolean> {
  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> {
    return of(true);
  }
}
`;
        const filename = `${(0, helpers_1.dasherize)(className)}${this.config.typeSeparator}resolver.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular service file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateService(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the service class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const omitSuffix = this.config.omitSuffix;
        const content = `import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ${className}${omitSuffix ? '' : 'Service'} {}
`;
        const filename = `${(0, helpers_1.dasherize)(className)}${omitSuffix ? '' : '.service'}.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new Angular test (spec) file based on user input.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateTest(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        const skipFolderConfirmation = this.config.skipFolderConfirmation;
        let folder;
        if (!folderPath || !skipFolderConfirmation) {
            // Get the path to the folder
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showError)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        // Get the class name
        const className = await (0, helpers_1.getName)(vscode_1.l10n.t('Enter the test class name'), vscode_1.l10n.t('E.g. User, Role, Auth...'), helpers_1.validateClassName);
        if (!className) {
            return;
        }
        // Get the type using enhanced selector with icons
        const typeOptions = [
            {
                label: 'Class',
                value: 'class',
                icon: '$(symbol-class)',
                description: 'Simple class for domain objects',
            },
            {
                label: 'Interface',
                value: 'interface',
                icon: '$(symbol-interface)',
                description: 'Define object shapes and contracts',
            },
            {
                label: 'DTO',
                value: 'dto',
                icon: '$(symbol-structure)',
                description: 'Data Transfer Objects',
            },
            {
                label: 'Model',
                value: 'model',
                icon: '$(database)',
                description: 'Data models for business logic',
            },
            {
                label: 'Entity',
                value: 'entity',
                icon: '$(references)',
                description: 'Database entities',
            },
            {
                label: 'Enum',
                value: 'enum',
                icon: '$(symbol-enum)',
                description: 'Type-safe enumeration',
            },
        ];
        let type = await (0, helpers_1.pickItemWithIcons)(typeOptions, vscode_1.l10n.t('Select the test type'));
        if (!type) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const content = `import { TestBed } from '@angular/core/testing';

import { ${className}${(0, helpers_1.titleize)(type)} } from './${(0, helpers_1.dasherize)(className)}${this.config.typeSeparator}${type}';

describe('${className}${(0, helpers_1.titleize)(type)}', () => {
  let ${type}: ${className}${(0, helpers_1.titleize)(type)};

  beforeEach(() => {
    TestBed.configureTestingModule({});
    ${type} = TestBed.inject(${className}${(0, helpers_1.titleize)(type)});
  });

  it('should be created', () => {
    expect(${type}).toBeTruthy();
  });
});
`;
        const filename = `${(0, helpers_1.dasherize)(className)}.spec.ts`;
        (0, helpers_1.saveFile)(folder, filename, content);
    }
    /**
     * Generates a new custom element file based on user input and selected template.
     * @param path Optional Uri for the target folder. If a file is provided, its parent folder is used.
     * @returns Promise resolved when the file is created or operation is cancelled.
     */
    async generateCustomElement(path) {
        // Get the relative path
        const folderPath = (0, helpers_1.relativePath)(path, this.config.useRootWorkspace);
        let folder;
        if (!folderPath || !this.config.skipFolderConfirmation) {
            folder = await (0, helpers_1.getPath)(vscode_1.l10n.t('Enter the folder name'), vscode_1.l10n.t('Folder name. E.g. src, app...'), folderPath, helpers_1.validateFolderName);
            if (!folder) {
                const message = vscode_1.l10n.t('Operation cancelled by user');
                (0, helpers_1.showMessage)(message);
                return;
            }
        }
        else {
            folder = folderPath;
        }
        if (this.config.templates.length === 0) {
            const message = vscode_1.l10n.t('The custom components list is empty. Please add custom components to the configuration');
            (0, helpers_1.showError)(message);
            return;
        }
        const items = this.config.templates.map((item) => ({
            label: item.name,
            description: item.description,
            detail: item.type,
            template: item.template,
        }));
        const option = await vscode_1.window.showQuickPick(items, {
            placeHolder: vscode_1.l10n.t('Select the template for the custom element generation'),
        });
        if (!option) {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        const template = this.config.templates.find((item) => item.name === option.label);
        let content = Object(template).template.join('\n');
        // Resolve placeholders in template content
        try {
            content = await (0, helpers_1.resolvePlaceholders)(content, this.config.style);
        }
        catch {
            const message = vscode_1.l10n.t('Operation cancelled by user');
            (0, helpers_1.showMessage)(message);
            return;
        }
        // Generate filename
        const ext = Object(template).type ? `.${Object(template).type}` : '';
        // Extraer el nombre de la clase de forma segura
        const classNameMatch = content.match(/class\s+(\w+)/);
        if (!classNameMatch) {
            const message = vscode_1.l10n.t('Could not extract class name from template');
            (0, helpers_1.showError)(message);
            return;
        }
        const filename = `${(0, helpers_1.dasherize)(classNameMatch[1])}${ext}.ts`;
        // Save file
        (0, helpers_1.saveFile)(folder, filename, content);
    }
}
exports.FileController = FileController;
//# sourceMappingURL=file.controller.js.map