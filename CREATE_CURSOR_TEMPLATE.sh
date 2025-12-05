#!/bin/bash
# 🚀 Create Cursor Startup Template from Current Setup
# This script creates a reusable template from your current it_genius configuration

set -e

TEMPLATE_NAME="${1:-my-preferred-cursor-template}"
TEMPLATE_DIR="$HOME/.cursor-templates/$TEMPLATE_NAME"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🎯 Creating Cursor Startup Template: $TEMPLATE_NAME"
echo "📍 Template location: $TEMPLATE_DIR"
echo ""

# Create template directory structure
mkdir -p "$TEMPLATE_DIR"/{.cursor/rules,.vscode/snippets,templates,scripts}

echo "📁 Creating directory structure..."

# Copy Cursor rules
if [ -d "$CURRENT_DIR/.cursor/rules" ]; then
    echo "  ✅ Copying Cursor rules..."
    cp -r "$CURRENT_DIR/.cursor/rules"/* "$TEMPLATE_DIR/.cursor/rules/" 2>/dev/null || true
fi

# Copy AutoKeep files
echo "  ✅ Copying AutoKeep files..."
cp "$CURRENT_DIR/autokeep-commit.js" "$TEMPLATE_DIR/" 2>/dev/null || echo "    ⚠️  autokeep-commit.js not found"
cp "$CURRENT_DIR/autokeep-review.js" "$TEMPLATE_DIR/" 2>/dev/null || echo "    ⚠️  autokeep-review.js not found"

# Copy package.json
if [ -f "$CURRENT_DIR/package.json" ]; then
    echo "  ✅ Copying package.json..."
    cp "$CURRENT_DIR/package.json" "$TEMPLATE_DIR/"
fi

# Create template versions of key files
echo "  ✅ Creating template files..."

# START_HERE.py template (with placeholders)
if [ -f "$CURRENT_DIR/START_HERE.py" ]; then
    sed 's/it_genius/${PROJECT_NAME}/g' "$CURRENT_DIR/START_HERE.py" > "$TEMPLATE_DIR/templates/START_HERE.py.template"
fi

# README template
cat > "$TEMPLATE_DIR/templates/README.md.template" << 'EOF'
# ${PROJECT_NAME}

## 🚀 Quick Start

\`\`\`bash
python3 START_HERE.py
\`\`\`

## 🤖 AutoKeep

AutoKeep is configured to automatically commit and review changes.

- Auto-commit on save
- AI-powered commit messages
- Auto-generated reviews

## 📁 Project Structure

\`\`\`
${PROJECT_NAME}/
├── .cursor/
│   └── rules/
│       └── autokeep.json
├── autokeep-commit.js
├── autokeep-review.js
├── package.json
└── START_HERE.py
\`\`\`

## 🔧 Setup

1. Install dependencies: \`npm install\`
2. Initialize git: \`git init\`
3. Start developing!

---

Created from NOIZYLAB preferred template
EOF

# Create template metadata
cat > "$TEMPLATE_DIR/template.json" << EOF
{
  "name": "$TEMPLATE_NAME",
  "description": "Preferred Cursor startup template with AutoKeep and all tools",
  "version": "1.0.0",
  "author": "$USER",
  "created": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "files": [
    ".cursor/rules/autokeep.json",
    "autokeep-commit.js",
    "autokeep-review.js",
    "package.json",
    "templates/START_HERE.py.template",
    "templates/README.md.template"
  ],
  "variables": {
    "PROJECT_NAME": "MyProject",
    "AUTHOR": "$USER"
  },
  "scripts": {
    "setup": "chmod +x autokeep-*.js && npm install",
    "test": "node autokeep-commit.js --dry-run"
  }
}
EOF

# Create project creation script
cat > "$TEMPLATE_DIR/scripts/create-from-template.sh" << 'EOF'
#!/bin/bash
# Create new project from template

TEMPLATE_DIR="$1"
PROJECT_DIR="$2"
PROJECT_NAME="${3:-$(basename "$PROJECT_DIR")}"

if [ -z "$TEMPLATE_DIR" ] || [ -z "$PROJECT_DIR" ]; then
    echo "Usage: $0 <template-dir> <project-dir> [project-name]"
    exit 1
fi

echo "🚀 Creating project: $PROJECT_NAME"
echo "📍 Location: $PROJECT_DIR"
echo ""

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Copy template files
echo "📁 Copying template files..."
cp -r "$TEMPLATE_DIR"/* . 2>/dev/null || true
cp -r "$TEMPLATE_DIR"/.cursor . 2>/dev/null || true

# Process templates with variables
echo "🔧 Processing templates..."
find templates -type f -name "*.template" 2>/dev/null | while read -r file; do
    dest="${file%.template}"
    dest="${dest#templates/}"
    mkdir -p "$(dirname "$dest")"
    sed -e "s/\${PROJECT_NAME}/$PROJECT_NAME/g" \
        -e "s/\${AUTHOR}/$USER/g" \
        "$file" > "$dest"
    echo "  ✅ Created: $dest"
done

# Remove template directory
rm -rf templates

# Make scripts executable
chmod +x autokeep-*.js 2>/dev/null || true
chmod +x scripts/*.sh 2>/dev/null || true

# Initialize git if not already
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    echo ".cursor-templates/" >> .gitignore 2>/dev/null || true
fi

echo ""
echo "✅ Project created successfully!"
echo ""
echo "📋 Next steps:"
echo "  1. cd $PROJECT_DIR"
echo "  2. npm install"
echo "  3. python3 START_HERE.py"
echo ""
EOF

chmod +x "$TEMPLATE_DIR/scripts/create-from-template.sh"

# Create usage guide
cat > "$TEMPLATE_DIR/README.md" << EOF
# $TEMPLATE_NAME

## 🎯 Cursor Startup Template

This is your preferred Cursor startup template with all your favorite tools and configurations.

## ✨ Features

- ✅ AutoKeep Review Engine
- ✅ START_HERE.py launcher
- ✅ Package.json with scripts
- ✅ Cursor rules configuration
- ✅ All preferred tools integrated

## 🚀 Using This Template

### Create New Project

\`\`\`bash
$TEMPLATE_DIR/scripts/create-from-template.sh "$TEMPLATE_DIR" /path/to/new-project "ProjectName"
\`\`\`

### Or Copy Manually

\`\`\`bash
cp -r "$TEMPLATE_DIR"/* /path/to/new-project/
cp -r "$TEMPLATE_DIR"/.cursor /path/to/new-project/
cd /path/to/new-project
# Customize as needed
\`\`\`

## 📁 Template Contents

- \`.cursor/rules/\` - Cursor configuration rules
- \`autokeep-commit.js\` - AutoKeep commit script
- \`autokeep-review.js\` - AutoKeep review script
- \`package.json\` - NPM scripts
- \`templates/\` - Template files for new projects

## 🔧 Customization

Edit files in this template directory to customize for future projects.

---

**Template Location:** \`$TEMPLATE_DIR\`

Created: $(date)
EOF

echo ""
echo "✅ Template created successfully!"
echo ""
echo "📋 Template location: $TEMPLATE_DIR"
echo ""
echo "🚀 To create a new project from this template:"
echo "   $TEMPLATE_DIR/scripts/create-from-template.sh \"$TEMPLATE_DIR\" /path/to/new-project \"ProjectName\""
echo ""
echo "📚 See $TEMPLATE_DIR/README.md for more information"
echo ""

