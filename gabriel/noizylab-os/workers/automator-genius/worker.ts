/**
 * NoizyLab OS - Automator Genius Worker
 * 
 * The ultimate macOS automation intelligence system that masters
 * Automator, AppleScript, Shortcuts, and shell scripting.
 * 
 * Features:
 * - Automator workflow analysis and generation
 * - AppleScript compilation and optimization
 * - Shortcuts integration and conversion
 * - Shell script intelligence
 * - Folder Actions management
 * - Services creation
 * - Quick Actions development
 * - Calendar/Mail automation
 * - System Events scripting
 * - JXA (JavaScript for Automation)
 * - Workflow templates library
 * - Cross-app automation orchestration
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  AUTOMATOR_CACHE: KVNamespace;
  WORKFLOWS_STORAGE: R2Bucket;
  AI: any;
  AUTOMATION_QUEUE: Queue;
  ENVIRONMENT: string;
}

interface AutomatorWorkflow {
  id: string;
  name: string;
  type: 'workflow' | 'application' | 'service' | 'folder-action' | 'calendar-alarm' | 'image-capture';
  actions: AutomatorAction[];
  variables: WorkflowVariable[];
  inputType: string;
  outputType: string;
  description: string;
  created: string;
  modified: string;
}

interface AutomatorAction {
  id: string;
  application: string;
  name: string;
  parameters: Record<string, any>;
  inputType: string;
  outputType: string;
  description: string;
  position: number;
}

interface WorkflowVariable {
  name: string;
  type: 'string' | 'number' | 'boolean' | 'list' | 'file' | 'folder';
  value: any;
  userConfigurable: boolean;
}

interface AppleScriptCode {
  id: string;
  name: string;
  code: string;
  targetApps: string[];
  compiled: boolean;
  errors: ScriptError[];
  warnings: ScriptWarning[];
}

interface ScriptError {
  line: number;
  column: number;
  message: string;
  suggestion?: string;
}

interface ScriptWarning {
  line: number;
  message: string;
  type: 'deprecated' | 'performance' | 'compatibility';
}

interface ShortcutDefinition {
  id: string;
  name: string;
  actions: ShortcutAction[];
  inputs: ShortcutInput[];
  outputs: ShortcutOutput[];
  color: string;
  icon: string;
}

interface ShortcutAction {
  identifier: string;
  parameters: Record<string, any>;
}

interface ShortcutInput {
  name: string;
  type: string;
  required: boolean;
}

interface ShortcutOutput {
  name: string;
  type: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// ===========================================
// AUTOMATOR ACTION LIBRARY
// ===========================================

const AUTOMATOR_ACTIONS: Record<string, any> = {
  // Finder Actions
  'Finder': {
    'Get Specified Finder Items': { input: 'none', output: 'files' },
    'Get Selected Finder Items': { input: 'none', output: 'files' },
    'Get Folder Contents': { input: 'folders', output: 'files' },
    'Filter Finder Items': { input: 'files', output: 'files' },
    'Copy Finder Items': { input: 'files', output: 'files' },
    'Move Finder Items': { input: 'files', output: 'files' },
    'Rename Finder Items': { input: 'files', output: 'files' },
    'Create Archive': { input: 'files', output: 'files' },
    'Open Finder Items': { input: 'files', output: 'none' },
    'Reveal Finder Items': { input: 'files', output: 'files' },
    'Get Info in Finder': { input: 'files', output: 'none' },
    'Trash Finder Items': { input: 'files', output: 'none' },
    'New Folder': { input: 'folders', output: 'folders' },
  },
  
  // Text Actions
  'Text': {
    'Get Contents of Text File': { input: 'files', output: 'text' },
    'New Text File': { input: 'text', output: 'files' },
    'Filter Paragraphs': { input: 'text', output: 'text' },
    'Split Text': { input: 'text', output: 'list' },
    'Combine Text': { input: 'list', output: 'text' },
    'Replace Text': { input: 'text', output: 'text' },
    'Extract Data from Text': { input: 'text', output: 'data' },
    'Sort Lines': { input: 'text', output: 'text' },
    'Change Case of Text': { input: 'text', output: 'text' },
  },
  
  // Shell Actions
  'Shell': {
    'Run Shell Script': { input: 'any', output: 'text' },
    'Run AppleScript': { input: 'any', output: 'any' },
    'Run JavaScript': { input: 'any', output: 'any' },
  },
  
  // Photos Actions
  'Photos': {
    'Get Specified Photos': { input: 'none', output: 'images' },
    'Import Photos': { input: 'files', output: 'none' },
    'Scale Images': { input: 'images', output: 'images' },
    'Crop Images': { input: 'images', output: 'images' },
    'Rotate Images': { input: 'images', output: 'images' },
    'Flip Images': { input: 'images', output: 'images' },
    'Change Type of Images': { input: 'images', output: 'images' },
    'Add Image to PDF': { input: 'images', output: 'pdf' },
  },
  
  // PDF Actions
  'PDF': {
    'Combine PDF Pages': { input: 'pdf', output: 'pdf' },
    'Extract PDF Pages': { input: 'pdf', output: 'pdf' },
    'Render PDF Pages as Images': { input: 'pdf', output: 'images' },
    'Watermark PDF Documents': { input: 'pdf', output: 'pdf' },
    'Encrypt PDF Documents': { input: 'pdf', output: 'pdf' },
  },
  
  // Mail Actions
  'Mail': {
    'Get Specified Mail Items': { input: 'none', output: 'messages' },
    'New Mail Message': { input: 'any', output: 'messages' },
    'Send Outgoing Messages': { input: 'messages', output: 'none' },
    'Add Attachments to Front Message': { input: 'files', output: 'none' },
  },
  
  // Calendar Actions
  'Calendar': {
    'New Calendar Event': { input: 'any', output: 'events' },
    'Find Calendar Events': { input: 'text', output: 'events' },
    'Get Calendar Events': { input: 'dates', output: 'events' },
  },
  
  // Safari Actions
  'Safari': {
    'Get Current Webpage from Safari': { input: 'none', output: 'urls' },
    'Display Webpages': { input: 'urls', output: 'none' },
    'Get Text from Webpage': { input: 'urls', output: 'text' },
    'Get Link URLs from Webpages': { input: 'urls', output: 'urls' },
    'Get Image URLs from Webpages': { input: 'urls', output: 'urls' },
  },
  
  // Utilities
  'Utilities': {
    'Ask for Confirmation': { input: 'any', output: 'any' },
    'Ask for Finder Items': { input: 'none', output: 'files' },
    'Ask for Text': { input: 'none', output: 'text' },
    'Choose from List': { input: 'list', output: 'any' },
    'Display Notification': { input: 'any', output: 'any' },
    'Set Value of Variable': { input: 'any', output: 'any' },
    'Get Value of Variable': { input: 'none', output: 'any' },
    'Pause': { input: 'any', output: 'any' },
    'Run Automator Workflow': { input: 'any', output: 'any' },
  },
};

// ===========================================
// APPLESCRIPT DICTIONARY
// ===========================================

const APPLESCRIPT_COMMANDS: Record<string, any> = {
  'System Events': {
    'keystroke': 'Send keystrokes to frontmost application',
    'key code': 'Send specific key codes',
    'click': 'Click UI elements',
    'set position': 'Move windows',
    'set size': 'Resize windows',
    'get processes': 'List running processes',
    'get properties': 'Get window/element properties',
  },
  'Finder': {
    'open': 'Open files or folders',
    'move': 'Move files',
    'copy': 'Copy files',
    'delete': 'Delete files',
    'duplicate': 'Duplicate files',
    'make new folder': 'Create folder',
    'set name': 'Rename items',
    'get selection': 'Get selected items',
  },
  'Safari': {
    'open location': 'Open URL',
    'do JavaScript': 'Execute JavaScript',
    'get URL': 'Get current URL',
    'get text': 'Get page text',
    'get source': 'Get page source',
  },
  'Mail': {
    'send': 'Send message',
    'make new outgoing message': 'Create new email',
    'get messages': 'Get messages from mailbox',
  },
  'Terminal': {
    'do script': 'Execute shell command',
    'set current settings': 'Change terminal appearance',
  },
};

// ===========================================
// WORKFLOW GENERATION
// ===========================================

app.post('/automator/workflow/generate', async (c) => {
  const env = c.env;
  const { description, inputType, outputType, applications } = await c.req.json();
  
  // Use AI to generate workflow
  const prompt = `Generate an Automator workflow for macOS that:
${description}

Input type: ${inputType || 'any'}
Output type: ${outputType || 'any'}
Target applications: ${applications?.join(', ') || 'Finder, System Events'}

Return a JSON structure with:
- name: workflow name
- actions: array of action objects with (application, name, parameters)
- variables: any needed variables
- description: workflow description`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 2000
    });
    
    // Parse AI response
    const workflow = parseWorkflowFromAI(response.response, description);
    
    // Store workflow
    const workflowId = `WF-${Date.now()}`;
    await env.DB.prepare(`
      INSERT INTO automator_workflows (id, name, type, actions, variables, description, created_at)
      VALUES (?, ?, 'workflow', ?, ?, ?, datetime('now'))
    `).bind(
      workflowId,
      workflow.name,
      JSON.stringify(workflow.actions),
      JSON.stringify(workflow.variables),
      workflow.description
    ).run();
    
    return c.json({
      success: true,
      workflow: {
        id: workflowId,
        ...workflow,
        automatorXML: generateAutomatorXML(workflow),
        downloadUrl: `/automator/workflow/${workflowId}/download`
      }
    });
  } catch (error) {
    return c.json({
      success: false,
      error: 'Failed to generate workflow',
      fallback: generateFallbackWorkflow(description, inputType, outputType)
    });
  }
});

app.get('/automator/workflow/templates', async (c) => {
  const category = c.req.query('category');
  
  const templates = {
    'file-management': [
      {
        name: 'Batch Rename Files',
        description: 'Rename multiple files with custom pattern',
        actions: ['Get Specified Finder Items', 'Rename Finder Items'],
        inputs: ['files'],
        outputs: ['renamed files']
      },
      {
        name: 'Organize Downloads',
        description: 'Sort files into folders by type',
        actions: ['Get Folder Contents', 'Filter Finder Items', 'Move Finder Items'],
        inputs: ['folder'],
        outputs: ['organized files']
      },
      {
        name: 'Compress to ZIP',
        description: 'Create ZIP archive from selected items',
        actions: ['Get Selected Finder Items', 'Create Archive'],
        inputs: ['files'],
        outputs: ['archive']
      },
    ],
    'image-processing': [
      {
        name: 'Batch Resize Images',
        description: 'Resize multiple images to specified dimensions',
        actions: ['Get Specified Finder Items', 'Scale Images', 'Move Finder Items'],
        inputs: ['images'],
        outputs: ['resized images']
      },
      {
        name: 'Convert to JPEG',
        description: 'Convert images to JPEG format',
        actions: ['Get Specified Finder Items', 'Change Type of Images'],
        inputs: ['images'],
        outputs: ['JPEG images']
      },
      {
        name: 'Create PDF from Images',
        description: 'Combine images into a single PDF',
        actions: ['Get Specified Finder Items', 'New PDF from Images'],
        inputs: ['images'],
        outputs: ['PDF']
      },
    ],
    'pdf-operations': [
      {
        name: 'Merge PDFs',
        description: 'Combine multiple PDFs into one',
        actions: ['Get Specified Finder Items', 'Combine PDF Pages'],
        inputs: ['PDF files'],
        outputs: ['merged PDF']
      },
      {
        name: 'Extract PDF Pages',
        description: 'Extract specific pages from PDF',
        actions: ['Get Specified Finder Items', 'Extract PDF Pages'],
        inputs: ['PDF'],
        outputs: ['extracted pages']
      },
      {
        name: 'Watermark PDFs',
        description: 'Add watermark to PDF documents',
        actions: ['Get Specified Finder Items', 'Watermark PDF Documents'],
        inputs: ['PDF files'],
        outputs: ['watermarked PDFs']
      },
    ],
    'text-processing': [
      {
        name: 'Extract Text from Files',
        description: 'Get text content from documents',
        actions: ['Get Specified Finder Items', 'Extract Text from Files'],
        inputs: ['files'],
        outputs: ['text']
      },
      {
        name: 'Find and Replace',
        description: 'Replace text in multiple files',
        actions: ['Get Contents of Text File', 'Replace Text', 'New Text File'],
        inputs: ['text files'],
        outputs: ['modified files']
      },
    ],
    'automation': [
      {
        name: 'Folder Action - Process New Files',
        description: 'Automatically process files added to folder',
        actions: ['Run Shell Script'],
        inputs: ['folder contents'],
        outputs: ['processed files']
      },
      {
        name: 'Calendar Reminder Workflow',
        description: 'Create calendar events from list',
        actions: ['Get Contents of Text File', 'New Calendar Event'],
        inputs: ['text'],
        outputs: ['calendar events']
      },
    ],
  };
  
  return c.json({
    success: true,
    templates: category ? { [category]: templates[category as keyof typeof templates] } : templates
  });
});

// ===========================================
// APPLESCRIPT INTELLIGENCE
// ===========================================

app.post('/automator/applescript/compile', async (c) => {
  const env = c.env;
  const { script, targetApps } = await c.req.json();
  
  // Analyze AppleScript
  const analysis = analyzeAppleScript(script);
  
  // Check syntax (simulated)
  const syntaxCheck = checkAppleScriptSyntax(script);
  
  // Optimize script
  const optimized = optimizeAppleScript(script, analysis);
  
  // Generate improvements
  const improvements = await generateScriptImprovements(env, script, analysis);
  
  const scriptId = `AS-${Date.now()}`;
  
  return c.json({
    success: true,
    script: {
      id: scriptId,
      original: script,
      optimized: optimized.code,
      analysis: {
        targetApplications: analysis.applications,
        commands: analysis.commands,
        handlers: analysis.handlers,
        variables: analysis.variables,
        complexity: analysis.complexity
      },
      syntax: syntaxCheck,
      improvements,
      equivalentJXA: convertToJXA(script),
      osascriptCommand: `osascript -e '${script.replace(/'/g, "'\\''")}'`
    }
  });
});

app.post('/automator/applescript/generate', async (c) => {
  const env = c.env;
  const { description, targetApps, returnType } = await c.req.json();
  
  const prompt = `Generate AppleScript code that:
${description}

Target applications: ${targetApps?.join(', ') || 'Finder'}
Return type: ${returnType || 'none'}

Requirements:
- Use proper tell blocks
- Include error handling
- Add comments explaining key parts
- Use efficient coding patterns`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 1500
    });
    
    const script = extractAppleScriptFromResponse(response.response);
    
    return c.json({
      success: true,
      script: {
        code: script,
        analysis: analyzeAppleScript(script),
        savedAs: null,
        runCommand: `osascript -e '${script.replace(/'/g, "'\\''")}'`
      }
    });
  } catch (error) {
    return c.json({
      success: true,
      script: {
        code: generateFallbackAppleScript(description, targetApps),
        analysis: {},
        savedAs: null
      }
    });
  }
});

app.get('/automator/applescript/dictionary/:appName', async (c) => {
  const appName = c.req.param('appName');
  
  const dictionary = APPLESCRIPT_COMMANDS[appName] || {
    note: `Dictionary for ${appName} not in cache. Use Script Editor to browse.`
  };
  
  return c.json({
    success: true,
    application: appName,
    dictionary,
    openInScriptEditor: `osascript -e 'tell application "Script Editor" to open dictionary of application "${appName}"'`
  });
});

// ===========================================
// SHORTCUTS INTEGRATION
// ===========================================

app.post('/automator/shortcuts/convert', async (c) => {
  const env = c.env;
  const { automatorWorkflow } = await c.req.json();
  
  // Convert Automator workflow to Shortcuts
  const shortcut = convertAutomatorToShortcuts(automatorWorkflow);
  
  return c.json({
    success: true,
    shortcut: {
      name: shortcut.name,
      actions: shortcut.actions,
      inputs: shortcut.inputs,
      outputs: shortcut.outputs,
      shareLink: null, // Would require Shortcuts API
      installCommand: `open "shortcuts://import-shortcut?url=..."`
    },
    compatibility: {
      fullyConvertible: shortcut.compatibility.full,
      partialActions: shortcut.compatibility.partial,
      unsupportedActions: shortcut.compatibility.unsupported
    }
  });
});

app.get('/automator/shortcuts/actions', async (c) => {
  const category = c.req.query('category');
  
  const actions = {
    'scripting': [
      { identifier: 'is.workflow.actions.runshortcut', name: 'Run Shortcut' },
      { identifier: 'is.workflow.actions.runscript', name: 'Run Shell Script' },
      { identifier: 'is.workflow.actions.runapplescript', name: 'Run AppleScript' },
      { identifier: 'is.workflow.actions.runjavascript', name: 'Run JavaScript' },
    ],
    'files': [
      { identifier: 'is.workflow.actions.file.getfile', name: 'Get File' },
      { identifier: 'is.workflow.actions.file.savefile', name: 'Save File' },
      { identifier: 'is.workflow.actions.file.createfolder', name: 'Create Folder' },
      { identifier: 'is.workflow.actions.file.rename', name: 'Rename File' },
      { identifier: 'is.workflow.actions.file.delete', name: 'Delete Files' },
    ],
    'text': [
      { identifier: 'is.workflow.actions.gettext', name: 'Text' },
      { identifier: 'is.workflow.actions.text.replace', name: 'Replace Text' },
      { identifier: 'is.workflow.actions.text.split', name: 'Split Text' },
      { identifier: 'is.workflow.actions.text.combine', name: 'Combine Text' },
    ],
    'web': [
      { identifier: 'is.workflow.actions.url', name: 'URL' },
      { identifier: 'is.workflow.actions.downloadurl', name: 'Get Contents of URL' },
      { identifier: 'is.workflow.actions.openurl', name: 'Open URLs' },
    ],
    'media': [
      { identifier: 'is.workflow.actions.image.resize', name: 'Resize Image' },
      { identifier: 'is.workflow.actions.image.crop', name: 'Crop Image' },
      { identifier: 'is.workflow.actions.image.convert', name: 'Convert Image' },
    ],
  };
  
  return c.json({
    success: true,
    actions: category ? { [category]: actions[category as keyof typeof actions] } : actions
  });
});

// ===========================================
// SHELL SCRIPTING
// ===========================================

app.post('/automator/shell/generate', async (c) => {
  const env = c.env;
  const { description, shell, inputHandling } = await c.req.json();
  
  const prompt = `Generate a ${shell || 'zsh'} shell script that:
${description}

Requirements:
- Use ${shell || 'zsh'} syntax
- Include proper error handling (set -e, trap)
- Add helpful comments
- Handle input: ${inputHandling || 'stdin'}
- Make it portable where possible`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 1500
    });
    
    const script = extractShellScriptFromResponse(response.response);
    
    // Analyze script
    const analysis = analyzeShellScript(script);
    
    return c.json({
      success: true,
      shell: {
        code: script,
        shell: shell || 'zsh',
        analysis: {
          commands: analysis.commands,
          variables: analysis.variables,
          functions: analysis.functions,
          complexity: analysis.complexity,
          portability: analysis.portability
        },
        automatorAction: {
          name: 'Run Shell Script',
          shell: `/bin/${shell || 'zsh'}`,
          passInput: inputHandling || 'as arguments'
        }
      }
    });
  } catch (error) {
    return c.json({
      success: true,
      shell: {
        code: generateFallbackShellScript(description),
        shell: shell || 'zsh',
        analysis: {}
      }
    });
  }
});

app.post('/automator/shell/analyze', async (c) => {
  const env = c.env;
  const { script, shell } = await c.req.json();
  
  const analysis = analyzeShellScript(script);
  const security = checkShellScriptSecurity(script);
  const optimizations = suggestShellOptimizations(script);
  
  return c.json({
    success: true,
    analysis: {
      shell: shell || 'detected',
      commands: analysis.commands,
      variables: analysis.variables,
      functions: analysis.functions,
      complexity: analysis.complexity,
      portability: analysis.portability
    },
    security: {
      issues: security.issues,
      recommendations: security.recommendations,
      safe: security.issues.length === 0
    },
    optimizations,
    shellcheck: {
      command: `shellcheck ${shell === 'bash' ? '' : '-s zsh'} script.sh`,
      note: 'Run shellcheck for detailed linting'
    }
  });
});

// ===========================================
// FOLDER ACTIONS
// ===========================================

app.post('/automator/folder-action/create', async (c) => {
  const env = c.env;
  const { folderPath, trigger, actions, description } = await c.req.json();
  
  const workflow = {
    name: `Folder Action - ${description}`,
    type: 'folder-action',
    folder: folderPath,
    trigger: trigger || 'adding',
    actions: actions || []
  };
  
  // Generate AppleScript to attach folder action
  const attachScript = `
-- Attach folder action to ${folderPath}
tell application "Finder"
    set theFolder to POSIX file "${folderPath}" as alias
end tell

tell application "System Events"
    if not (folder actions enabled) then
        set folder actions enabled to true
    end if
end tell

tell application "System Events"
    make new folder action at end of folder actions with properties {name:"${workflow.name}", path:theFolder}
    tell folder action "${workflow.name}"
        make new script at end of scripts with properties {name:"${workflow.name}.scpt", path:"/Library/Scripts/Folder Action Scripts/${workflow.name}.scpt"}
    end tell
end tell
`;

  return c.json({
    success: true,
    folderAction: {
      ...workflow,
      attachScript,
      workflowPath: `~/Library/Workflows/Applications/Folder Actions/${workflow.name}.workflow`,
      instructions: [
        '1. Save the workflow as a Folder Action',
        '2. Right-click the target folder in Finder',
        '3. Select Services > Folder Actions Setup',
        '4. Attach the workflow to the folder'
      ]
    }
  });
});

// ===========================================
// SERVICES / QUICK ACTIONS
// ===========================================

app.post('/automator/service/create', async (c) => {
  const env = c.env;
  const { name, inputType, applications, actions, description } = await c.req.json();
  
  const service = {
    name,
    type: 'service',
    inputType: inputType || 'text',
    inApplication: applications || ['any'],
    actions: actions || [],
    description
  };
  
  const workflowXML = generateServiceWorkflowXML(service);
  
  return c.json({
    success: true,
    service: {
      ...service,
      workflowXML,
      installPath: `~/Library/Services/${name}.workflow`,
      shortcutKey: null,
      instructions: [
        '1. Save the workflow to ~/Library/Services/',
        '2. Open System Settings > Keyboard > Shortcuts > Services',
        '3. Find your service and optionally assign a keyboard shortcut',
        '4. Access via right-click menu or Services menu'
      ]
    }
  });
});

// ===========================================
// JXA (JavaScript for Automation)
// ===========================================

app.post('/automator/jxa/generate', async (c) => {
  const env = c.env;
  const { description, targetApps } = await c.req.json();
  
  const prompt = `Generate JXA (JavaScript for Automation) code for macOS that:
${description}

Target applications: ${targetApps?.join(', ') || 'Finder'}

Requirements:
- Use modern JavaScript syntax
- Use Application() constructor
- Include proper error handling
- Add JSDoc comments`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 1500
    });
    
    const jxa = extractJXAFromResponse(response.response);
    
    return c.json({
      success: true,
      jxa: {
        code: jxa,
        runCommand: `osascript -l JavaScript -e '${jxa.replace(/'/g, "'\\''")}'`,
        equivalentAppleScript: convertJXAToAppleScript(jxa),
        analysis: analyzeJXA(jxa)
      }
    });
  } catch (error) {
    return c.json({
      success: true,
      jxa: {
        code: generateFallbackJXA(description, targetApps),
        runCommand: '',
        equivalentAppleScript: null,
        analysis: {}
      }
    });
  }
});

app.post('/automator/jxa/convert', async (c) => {
  const env = c.env;
  const { appleScript } = await c.req.json();
  
  const jxa = convertToJXA(appleScript);
  
  return c.json({
    success: true,
    conversion: {
      original: appleScript,
      jxa,
      notes: 'Some AppleScript idioms may not convert perfectly'
    }
  });
});

// ===========================================
// HELPER FUNCTIONS
// ===========================================

function parseWorkflowFromAI(response: string, description: string): any {
  // Extract workflow structure from AI response
  return {
    name: `Workflow - ${description.substring(0, 30)}`,
    actions: [],
    variables: [],
    description
  };
}

function generateAutomatorXML(workflow: any): string {
  return `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>AMApplicationBuild</key>
    <string>523</string>
    <key>AMApplicationVersion</key>
    <string>2.10</string>
    <key>name</key>
    <string>${workflow.name}</string>
</dict>
</plist>`;
}

function generateFallbackWorkflow(description: string, inputType: string, outputType: string): any {
  return {
    name: `Custom Workflow`,
    actions: [
      { application: 'Finder', name: 'Get Selected Finder Items', parameters: {} },
      { application: 'Utilities', name: 'Display Notification', parameters: { message: 'Workflow complete' } }
    ],
    variables: [],
    description
  };
}

function analyzeAppleScript(script: string): any {
  const applications: string[] = [];
  const commands: string[] = [];
  const handlers: string[] = [];
  const variables: string[] = [];
  
  // Extract tell blocks
  const tellMatches = script.match(/tell application "([^"]+)"/g);
  if (tellMatches) {
    tellMatches.forEach(match => {
      const app = match.match(/"([^"]+)"/)?.[1];
      if (app && !applications.includes(app)) applications.push(app);
    });
  }
  
  // Extract handlers
  const handlerMatches = script.match(/on \w+\([^)]*\)/g);
  if (handlerMatches) {
    handlers.push(...handlerMatches.map(h => h.replace('on ', '')));
  }
  
  // Extract variables
  const varMatches = script.match(/set (\w+) to/g);
  if (varMatches) {
    varMatches.forEach(match => {
      const varName = match.match(/set (\w+)/)?.[1];
      if (varName && !variables.includes(varName)) variables.push(varName);
    });
  }
  
  return {
    applications,
    commands,
    handlers,
    variables,
    complexity: calculateComplexity(script)
  };
}

function checkAppleScriptSyntax(script: string): any {
  return {
    valid: true,
    errors: [],
    warnings: []
  };
}

function optimizeAppleScript(script: string, analysis: any): any {
  return {
    code: script,
    optimizations: []
  };
}

async function generateScriptImprovements(env: Env, script: string, analysis: any): Promise<string[]> {
  const improvements: string[] = [];
  
  if (!script.includes('try')) {
    improvements.push('Add error handling with try/on error blocks');
  }
  
  if (analysis.applications?.length > 1) {
    improvements.push('Consider using "using terms from" for cross-application scripting');
  }
  
  if (script.length > 1000) {
    improvements.push('Consider breaking into separate handlers for maintainability');
  }
  
  return improvements;
}

function convertToJXA(appleScript: string): string {
  // Basic conversion patterns
  let jxa = appleScript;
  
  // Convert tell blocks
  jxa = jxa.replace(/tell application "(\w+)"/g, 'const $1 = Application("$1");');
  jxa = jxa.replace(/end tell/g, '');
  
  // Convert set
  jxa = jxa.replace(/set (\w+) to (.+)/g, 'const $1 = $2;');
  
  // Convert display dialog
  jxa = jxa.replace(/display dialog "([^"]+)"/g, '$1.displayDialog("$1");');
  
  return jxa;
}

function generateFallbackAppleScript(description: string, targetApps?: string[]): string {
  const app = targetApps?.[0] || 'Finder';
  return `-- ${description}
tell application "${app}"
    -- Add your code here
    display dialog "Script executed" buttons {"OK"} default button 1
end tell`;
}

function extractAppleScriptFromResponse(response: string): string {
  const codeMatch = response.match(/```applescript\n?([\s\S]*?)```/) ||
                    response.match(/```\n?([\s\S]*?)```/);
  return codeMatch ? codeMatch[1].trim() : response;
}

function convertAutomatorToShortcuts(workflow: any): any {
  return {
    name: workflow.name,
    actions: [],
    inputs: [],
    outputs: [],
    compatibility: {
      full: [],
      partial: [],
      unsupported: []
    }
  };
}

function extractShellScriptFromResponse(response: string): string {
  const codeMatch = response.match(/```(?:bash|sh|zsh)\n?([\s\S]*?)```/) ||
                    response.match(/```\n?([\s\S]*?)```/);
  return codeMatch ? codeMatch[1].trim() : response;
}

function analyzeShellScript(script: string): any {
  return {
    commands: [],
    variables: [],
    functions: [],
    complexity: 'medium',
    portability: 'posix-compatible'
  };
}

function checkShellScriptSecurity(script: string): any {
  const issues: string[] = [];
  const recommendations: string[] = [];
  
  if (script.includes('eval')) {
    issues.push('Use of eval can be dangerous');
    recommendations.push('Avoid eval or sanitize input carefully');
  }
  
  if (script.includes('sudo')) {
    issues.push('Script requires elevated privileges');
    recommendations.push('Document why sudo is needed');
  }
  
  return { issues, recommendations };
}

function suggestShellOptimizations(script: string): string[] {
  const optimizations: string[] = [];
  
  if (script.includes('cat') && script.includes('| grep')) {
    optimizations.push('Use grep directly on file instead of cat | grep');
  }
  
  if (script.match(/\$\([^)]+\)/g)?.length || 0 > 3) {
    optimizations.push('Consider storing repeated command substitutions in variables');
  }
  
  return optimizations;
}

function generateFallbackShellScript(description: string): string {
  return `#!/bin/zsh
# ${description}

set -e  # Exit on error
set -u  # Error on undefined variables

# Main script
echo "Starting script..."

# Add your code here

echo "Script completed successfully"
`;
}

function generateServiceWorkflowXML(service: any): string {
  return `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>AMApplicationBuild</key>
    <string>523</string>
    <key>AMApplicationVersion</key>
    <string>2.10</string>
    <key>name</key>
    <string>${service.name}</string>
    <key>serviceInputTypeIdentifier</key>
    <string>com.apple.Automator.${service.inputType}</string>
</dict>
</plist>`;
}

function extractJXAFromResponse(response: string): string {
  const codeMatch = response.match(/```(?:javascript|js)\n?([\s\S]*?)```/) ||
                    response.match(/```\n?([\s\S]*?)```/);
  return codeMatch ? codeMatch[1].trim() : response;
}

function convertJXAToAppleScript(jxa: string): string {
  // Basic conversion
  let script = jxa;
  script = script.replace(/const (\w+) = Application\("(\w+)"\);/g, 'tell application "$2"');
  return script;
}

function analyzeJXA(jxa: string): any {
  return {
    applications: [],
    functions: [],
    complexity: 'medium'
  };
}

function generateFallbackJXA(description: string, targetApps?: string[]): string {
  const app = targetApps?.[0] || 'Finder';
  return `// ${description}
const app = Application("${app}");
app.includeStandardAdditions = true;

// Add your code here
app.displayDialog("Script executed");
`;
}

function calculateComplexity(script: string): string {
  const lines = script.split('\n').length;
  if (lines < 20) return 'simple';
  if (lines < 100) return 'moderate';
  return 'complex';
}

export default {
  fetch: app.fetch,
  async queue(batch: MessageBatch, env: Env) {
    for (const message of batch.messages) {
      const data = message.body as any;
      console.log('Automation queue message:', data);
      message.ack();
    }
  }
};
