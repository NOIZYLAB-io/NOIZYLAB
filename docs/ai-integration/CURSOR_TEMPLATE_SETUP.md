# 🎯 Cursor Local Startup Template Setup

## Quick Guide to Create Your Preferred Template

### Method 1: Use the Automated Script (Recommended)

```bash
# Run the template creation script
./CREATE_CURSOR_TEMPLATE.sh
```

### Method 2: Manual Setup

#### 1. Create Template Directory

```bash
mkdir -p ~/.cursor-templates/my-preferred-template
cd ~/.cursor-templates/my-preferred-template
```

#### 2. Copy Your Current Setup

```bash
# From your it_genius folder
cp -r .cursor ~/.cursor-templates/my-preferred-template/
cp autokeep-commit.js ~/.cursor-templates/my-preferred-template/
cp autokeep-review.js ~/.cursor-templates/my-preferred-template/
cp package.json ~/.cursor-templates/my-preferred-template/
cp START_HERE.py ~/.cursor-templates/my-preferred-template/START_HERE.py.template
```

#### 3. Create Template Metadata

Create `~/.cursor-templates/my-preferred-template/template.json`:

```json
{
  "name": "My Preferred NOIZYLAB Template",
  "description": "Complete startup template with AutoKeep, launchers, and all tools",
  "version": "1.0.0",
  "author": "Your Name",
  "files": [
    ".cursor/rules/autokeep.json",
    "autokeep-commit.js",
    "autokeep-review.js",
    "package.json",
    "START_HERE.py"
  ],
  "variables": {
    "PROJECT_NAME": "MyProject",
    "AUTHOR": "Your Name"
  }
}
```

#### 4. Create New Project from Template

```bash
# Use the template script
~/.cursor-templates/create-from-template.sh my-preferred-template /path/to/new-project
```

## 🎨 Cursor Rules Configuration

Cursor automatically loads configuration from `.cursor/rules/*.json` files.

### Current Rules in Your Template:

1. **autokeep.json** - AutoKeep Review Engine configuration
2. **project.json** (optional) - Project-specific rules

## 📝 Adding Custom Rules

Create new `.json` files in `.cursor/rules/`:

```json
{
  "name": "My Custom Rule",
  "description": "Description of what this rule does",
  "triggers": {
    "onFileSave": {
      "run": ["custom-script"]
    }
  },
  "settings": {
    "enabled": true
  }
}
```

## 🚀 Using Your Template

### Option 1: Copy Manually

```bash
cp -r ~/.cursor-templates/my-preferred-template/* /path/to/new-project/
cd /path/to/new-project
# Customize as needed
```

### Option 2: Use the Script

```bash
./CREATE_FROM_TEMPLATE.sh ~/.cursor-templates/my-preferred-template /path/to/new-project
```

## ✨ Template Features

Your template includes:

- ✅ AutoKeep Review Engine (auto-commit on save)
- ✅ START_HERE.py launcher
- ✅ Package.json with scripts
- ✅ Cursor rules configuration
- ✅ All your preferred tools and integrations

## 🔧 Customization

After creating a project from your template:

1. Update project name in files
2. Configure git repository
3. Install dependencies: `npm install`
4. Initialize git: `git init`
5. Customize for your specific project needs

---

**Your template is ready to use!** 🎉

