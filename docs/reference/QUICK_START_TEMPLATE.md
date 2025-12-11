# ⚡ Quick Start: Create Your Cursor Template

## 🚀 One Command to Create Your Template

```bash
# From your it_genius directory
./CREATE_CURSOR_TEMPLATE.sh my-preferred-template
```

This creates a complete template at: `~/.cursor-templates/my-preferred-template/`

## 📋 What's Included

Your template includes:
- ✅ AutoKeep Review Engine (`.cursor/rules/autokeep.json`)
- ✅ Project rules (`.cursor/rules/project.json`)
- ✅ AutoKeep scripts (autokeep-*.js)
- ✅ Package.json with scripts
- ✅ Template files (START_HERE.py, README.md)
- ✅ Project creation script

## 🎯 Create New Project from Template

```bash
# Method 1: Use the script (Recommended)
~/.cursor-templates/my-preferred-template/scripts/create-from-template.sh \
  ~/.cursor-templates/my-preferred-template \
  /path/to/new-project \
  "MyProjectName"

# Method 2: Copy manually
cp -r ~/.cursor-templates/my-preferred-template/* /path/to/new-project/
cp -r ~/.cursor-templates/my-preferred-template/.cursor /path/to/new-project/
cd /path/to/new-project
```

## 📚 Full Documentation

- **Complete Guide**: See `CURSOR_TEMPLATE_GUIDE.md`
- **Setup Details**: See `.cursor/CURSOR_TEMPLATE_SETUP.md`

## ✨ That's It!

Your template is ready to use for all new Cursor projects!

---

**Run the script now:**
```bash
./CREATE_CURSOR_TEMPLATE.sh my-preferred-template
```

