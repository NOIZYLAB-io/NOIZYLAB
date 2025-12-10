# 🎯 Complete Guide: Creating Your Preferred Cursor Startup Template

## 📋 Overview

This guide shows you how to create a reusable startup template in Cursor that includes all your preferred configurations, tools, and integrations from your `it_genius` workspace.

## 🚀 Quick Start

### Option 1: Automated Template Creation (Easiest)

```bash
# Run the template creation script
./CREATE_CURSOR_TEMPLATE.sh my-preferred-template

# This creates a template at ~/.cursor-templates/my-preferred-template/
```

Then create new projects from your template:

```bash
~/.cursor-templates/my-preferred-template/scripts/create-from-template.sh \
  ~/.cursor-templates/my-preferred-template \
  /path/to/new-project \
  "MyNewProject"
```

### Option 2: Manual Setup

See the detailed steps below.

## 📁 Understanding Cursor Templates

### What Cursor Loads Automatically

Cursor automatically loads and applies:

1. **`.cursor/rules/*.json`** - Rules and configurations
2. **`.vscode/settings.json`** - Workspace settings (Cursor compatible)
3. **`.cursor/settings.json`** - Cursor-specific settings
4. **Snippets** - Code snippets for faster development

### Your Current Template Includes

- ✅ **AutoKeep Review Engine** - Auto-commit and review system
- ✅ **START_HERE.py** - Main launcher with all integrations
- ✅ **MASTER_LAUNCHER.py** - Master launcher
- ✅ **Cursor Rules** - AutoKeep configuration
- ✅ **Package.json** - NPM scripts
- ✅ **All your preferred tools**

## 🛠️ Step-by-Step: Creating Your Template

### Step 1: Create Template Structure

```bash
# Create template directory
mkdir -p ~/.cursor-templates/my-preferred-template
cd ~/.cursor-templates/my-preferred-template

# Create directory structure
mkdir -p .cursor/rules .vscode/snippets templates scripts
```

### Step 2: Copy Your Configuration Files

From your `it_genius` folder:

```bash
# Copy Cursor rules
cp -r /path/to/it_genius/.cursor/rules/* ~/.cursor-templates/my-preferred-template/.cursor/rules/

# Copy AutoKeep scripts
cp /path/to/it_genius/autokeep-*.js ~/.cursor-templates/my-preferred-template/
cp /path/to/it_genius/package.json ~/.cursor-templates/my-preferred-template/

# Copy launchers as templates
cp /path/to/it_genius/START_HERE.py ~/.cursor-templates/my-preferred-template/templates/START_HERE.py.template
cp /path/to/it_genius/MASTER_LAUNCHER.py ~/.cursor-templates/my-preferred-template/templates/MASTER_LAUNCHER.py.template
```

### Step 3: Create Template Metadata

Create `~/.cursor-templates/my-preferred-template/template.json`:

```json
{
  "name": "My Preferred NOIZYLAB Template",
  "description": "Complete startup template with AutoKeep and all tools",
  "version": "1.0.0",
  "files": [
    ".cursor/rules/autokeep.json",
    ".cursor/rules/project.json",
    "autokeep-commit.js",
    "autokeep-review.js",
    "package.json"
  ],
  "variables": {
    "PROJECT_NAME": "MyProject",
    "AUTHOR": "Your Name"
  }
}
```

### Step 4: Create Project Generation Script

Create `~/.cursor-templates/my-preferred-template/scripts/create-project.sh`:

```bash
#!/bin/bash
# Create new project from template

TEMPLATE_DIR="$HOME/.cursor-templates/my-preferred-template"
PROJECT_DIR="$1"
PROJECT_NAME="${2:-$(basename "$PROJECT_DIR")}"

# Copy template files
cp -r "$TEMPLATE_DIR"/* "$PROJECT_DIR"/
cp -r "$TEMPLATE_DIR"/.cursor "$PROJECT_DIR"/

# Process templates (replace variables)
find "$PROJECT_DIR" -name "*.template" | while read file; do
    dest="${file%.template}"
    sed -e "s/\${PROJECT_NAME}/$PROJECT_NAME/g" "$file" > "$dest"
    rm "$file"
done

# Make scripts executable
chmod +x "$PROJECT_DIR"/autokeep-*.js

# Initialize git
cd "$PROJECT_DIR"
git init

echo "✅ Project created: $PROJECT_NAME"
```

Make it executable:

```bash
chmod +x ~/.cursor-templates/my-preferred-template/scripts/create-project.sh
```

## 🎨 Cursor Rules Configuration

### Current Rules in Your Template

1. **`.cursor/rules/autokeep.json`** - AutoKeep Review Engine
2. **`.cursor/rules/project.json`** - Project-specific rules

### Adding New Rules

Create new JSON files in `.cursor/rules/`:

**Example: `.cursor/rules/coding-standards.json`**

```json
{
  "name": "Coding Standards",
  "description": "Enforce coding standards",
  "rules": {
    "python": {
      "maxLineLength": 120,
      "useTypeHints": true
    },
    "javascript": {
      "useStrict": true,
      "preferConst": true
    }
  }
}
```

## 📝 Creating Custom Snippets

Create snippets in `.vscode/snippets/`:

**Example: `.vscode/snippets/python.json`**

```json
{
  "Python Class": {
    "prefix": "pclass",
    "body": [
      "class ${1:ClassName}:",
      "    \"\"\"${2:Description}\"\"\"",
      "    ",
      "    def __init__(self):",
      "        ${3:pass}"
    ],
    "description": "Python class template"
  }
}
```

## 🚀 Using Your Template

### Method 1: Using the Script

```bash
# Create new project
~/.cursor-templates/my-preferred-template/scripts/create-project.sh \
  /path/to/new-project "MyProject"
```

### Method 2: Manual Copy

```bash
# Copy template
cp -r ~/.cursor-templates/my-preferred-template/* /path/to/new-project/
cp -r ~/.cursor-templates/my-preferred-template/.cursor /path/to/new-project/

# Customize
cd /path/to/new-project
# Edit files as needed
```

### Method 3: Use Cursor's Workspace Template

1. Open Cursor
2. File → New Window
3. File → Open Folder
4. Select your template directory
5. Save as Workspace (`.code-workspace` file)

## ✨ Template Features Checklist

Your template should include:

- [x] AutoKeep Review Engine configuration
- [x] Cursor rules (`.cursor/rules/`)
- [x] AutoKeep scripts (autokeep-*.js)
- [x] Package.json with scripts
- [x] START_HERE.py launcher
- [x] README.md template
- [x] Git initialization
- [x] Project creation script

## 🔧 Customization After Creation

After creating a project from your template:

1. **Update project name** in all files
2. **Initialize git**: `git init`
3. **Install dependencies**: `npm install`
4. **Configure git remote**: `git remote add origin <url>`
5. **Customize for project**: Edit files as needed

## 📚 Additional Resources

- **Cursor Rules Documentation**: `.cursor/rules/` files are automatically loaded
- **AutoKeep Setup**: See `AUTOKEEP_SETUP.md`
- **Template Location**: `~/.cursor-templates/my-preferred-template/`

## 🎉 Benefits

1. **Consistency** - Same setup for all projects
2. **Speed** - Instant project setup
3. **Best Practices** - All your preferred tools included
4. **Automation** - AutoKeep and other automations ready
5. **Documentation** - README and guides included

---

**Your template is ready to use!** 🚀

Run `./CREATE_CURSOR_TEMPLATE.sh` to create your template automatically.

