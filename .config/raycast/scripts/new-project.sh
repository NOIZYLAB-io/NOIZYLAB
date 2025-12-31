#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title New Project
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🚀
# @raycast.argument1 { "type": "text", "placeholder": "Project name" }
# @raycast.argument2 { "type": "dropdown", "placeholder": "Type", "data": [{"title": "Next.js", "value": "next"}, {"title": "Python", "value": "python"}, {"title": "Node.js", "value": "node"}, {"title": "Empty", "value": "empty"}] }
# @raycast.packageName Developer

# Documentation:
# @raycast.description Create a new project with hot-rod settings
# @raycast.author NOIZYLAB

name="$1"
type="$2"
base_dir="$HOME/NOIZYLAB"

mkdir -p "$base_dir"
cd "$base_dir"

case "$type" in
    next)
        echo "Creating Next.js project: $name"
        pnpm create next-app "$name" --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
        cd "$name"
        ;;
    python)
        echo "Creating Python project: $name"
        mkdir -p "$name" && cd "$name"
        uv init
        uv add fastapi uvicorn
        ;;
    node)
        echo "Creating Node.js project: $name"
        mkdir -p "$name" && cd "$name"
        pnpm init
        ;;
    empty)
        echo "Creating empty project: $name"
        mkdir -p "$name" && cd "$name"
        git init
        ;;
esac

# Hot-rod the project
~/.local/bin/vsc-hotrod .

# Open in VS Code
code-insiders .

echo "✅ Project created at $base_dir/$name"
