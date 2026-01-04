# VS Code Glob Patterns Reference

**Date**: January 4, 2026  
**Source**: VS Code Documentation  
**Use Case**: File searching, exclusions, and pattern matching in NOIZYLAB workspace

---

## 🎯 What Are Glob Patterns?

Glob patterns are wildcard expressions used to match files and folders. VS Code uses them in:

- **Search** (finding files across workspace)
- **File Explorer** (hiding/showing files)
- **Settings** (`files.exclude`, `search.exclude`)
- **Language associations** (file type detection)

---

## 📋 Glob Pattern Syntax

### Basic Wildcards

| Pattern | Matches                                      | Example                                             |
| ------- | -------------------------------------------- | --------------------------------------------------- |
| `*`     | Zero or more characters in a path segment    | `*.js` matches all JavaScript files                 |
| `?`     | Exactly one character                        | `file?.txt` matches `file1.txt`, `fileA.txt`        |
| `**`    | Any number of path segments (including none) | `**/*.py` matches all Python files in any subfolder |

### Path Separators

| Pattern | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| `/`     | Separates path segments (use even on Windows!)                                |
| `\`     | ⚠️ **DO NOT USE** - Use `/` instead, but patterns will match both `/` and `\` |

### Character Ranges

| Pattern  | Matches                     | Example                                                       |
| -------- | --------------------------- | ------------------------------------------------------------- |
| `[0-9]`  | Any digit                   | `log[0-9].txt` matches `log0.txt`, `log1.txt`, ... `log9.txt` |
| `[a-z]`  | Any lowercase letter        | `file[a-z].md` matches `filea.md`, `fileb.md`, etc.           |
| `[!0-9]` | Any character EXCEPT digits | `file[!0-9].txt` matches `filea.txt` but not `file1.txt`      |

### Grouping

| Pattern     | Description                          | Example                                                |
| ----------- | ------------------------------------ | ------------------------------------------------------ |
| `{...,...}` | Group multiple conditions (OR logic) | `{**/*.html,**/*.txt}` matches all HTML and text files |

### Special Characters

| Pattern    | How to Match Literally                                                    |
| ---------- | ------------------------------------------------------------------------- |
| `[` or `]` | Place inside brackets: `[[]` or `[]]`                                     |
| Example    | `src/routes/post/[[]id[]]/**.js` matches files in `src/routes/post/[id]/` |

---

## 🔍 Common Use Cases for NOIZYLAB

### 1. **Find All Audio Files**

```
**/*.{mp3,wav,aiff,flac}
```

Matches all audio files in any subfolder.

### 2. **Exclude Archives from Search**

```
**/*.{zip,tar,gz,dmg}
```

Add to `search.exclude` to skip compressed files.

### 3. **Find All Python Scripts**

```
**/*.py
```

Matches all `.py` files across entire workspace.

### 4. **Find Files in Specific Folder**

```
gabriel/_ORGANIZED/**/*.sh
```

Matches all shell scripts in `gabriel/_ORGANIZED/` and subfolders.

### 5. **Match Numbered Backups**

```
backup[0-9].txt
backup[0-9][0-9].txt
```

Matches `backup1.txt`, `backup12.txt`, etc.

### 6. **Exclude Node Modules and Build Folders**

```
{**/node_modules/**,**/build/**,**/dist/**}
```

Skips common development folders.

### 7. **Find All Markdown Documentation**

```
**/*.md
!**/node_modules/**/*.md
```

Finds all `.md` files but excludes those in `node_modules`.

---

## ⚠️ Important Differences: Search View vs Settings

### In Settings (`files.exclude`, `search.exclude`):

```json
{
  "files.exclude": {
    "**/node_modules": true,
    "**/.git": true,
    "**/example": true // Must use ** prefix!
  }
}
```

**Must explicitly use `**/` to match in subfolders.\*\*

### In Search View:

```
example  // Automatically treated as **/example
```

**The `**/` prefix is assumed automatically.\*\*

---

## 🚀 NOIZYLAB-Specific Patterns

### Find All Empty Folders (for cleanup scripts)

Use with `find` command in terminal:

```bash
find . -type d -empty -print
```

### Find All Audio/Video Files

```
**/*.{mp3,wav,aiff,flac,m4a,mp4,mov,avi}
```

### Find All Download Archives

```
**/downloads/**/*.{zip,tar,gz,dmg}
```

### Find All NOIZYLAB Archives

```
**/NOIZYLAB_ARCHIVE*/**
```

### Exclude System Files from Search

```json
{
  "search.exclude": {
    "**/.DS_Store": true,
    "**/._*": true,
    "**/.Spotlight-V100": true,
    "**/.fseventsd": true
  }
}
```

### Find All Scripts

```
**/*.{sh,py,js,ts}
```

### Find All Configuration Files

```
**/*.{json,yaml,yml,toml,ini,conf}
```

---

## 🔧 Advanced Patterns

### Match Files with Dates in Name

```
**/*202[0-9]-[0-1][0-9]-[0-3][0-9]*
```

Matches files with dates like `2020-01-01`, `2025-12-31`.

### Match Backup Files with Numbers

```
**/*_backup[0-9]*.{txt,md,json}
```

Matches `file_backup1.txt`, `config_backup2.json`.

### Exclude All Hidden Files (dot files)

```
**/.*
```

Matches `.gitignore`, `.DS_Store`, etc.

### Find Large Media Files (by extension)

```
**/*.{dmg,iso,pkg,zip,tar,gz}
```

---

## 💡 Pro Tips

### 1. **Test Patterns in Search First**

Before adding to settings, test in Search view (Cmd+Shift+F) to verify.

### 2. **Use Exclusions to Speed Up Search**

Add heavy folders to `search.exclude`:

```json
{
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.dmg": true,
    "**/*.zip": true
  }
}
```

### 3. **Combine Patterns for Complex Searches**

```
{**/*.py,**/*.js,**/*.sh}
```

Finds all Python, JavaScript, and shell scripts.

### 4. **Use Negation to Refine Results**

```
**/*.js
!**/node_modules/**
!**/vendor/**
```

Finds all JS files except those in `node_modules` or `vendor`.

### 5. **Remember: `/` Works on All Platforms**

Even on Windows, always use `/` for path separators.

---

## 🎯 NOIZYLAB Cleanup Script Integration

When building cleanup scripts, use glob patterns to:

### Find Empty Folders

```bash
# Terminal command
find /Volumes/12TB -type d -empty -print
```

### Find Duplicate Archives

```bash
# Search for NOIZYLAB_ARCHIVE folders
fd -t d "NOIZYLAB_ARCHIVE" /Volumes/12TB
```

### Find Large Files

```bash
# Files over 1GB
find /Volumes/12TB -type f -size +1G
```

### Find Old Backups

```bash
# Files ending with .bak or .old
fd -e bak -e old /Volumes/12TB
```

---

## 📚 Quick Reference Card

```
WILDCARDS:
  *       = match any characters in segment
  ?       = match one character
  **      = match any number of segments

SEPARATORS:
  /       = path separator (always use this!)

RANGES:
  [0-9]   = match digits
  [a-z]   = match lowercase letters
  [!0-9]  = match anything except digits

GROUPING:
  {A,B}   = match A or B

ESCAPING:
  [[]     = literal [
  []]     = literal ]
```

---

## 🔗 Integration with NOIZYLAB Scripts

### In `HUNT_EMPTY_FOLDERS.sh`

Use VS Code search to find empty folders first:

```
Search: **/*
Files to Include: (leave empty)
Files to Exclude: (add heavy folders)
```

### In `HUNT_ARCHIVES.sh`

Search pattern:

```
**/NOIZYLAB_ARCHIVE*
```

### In `ULTRA_AGGRESSIVE.sh`

Exclude patterns for safety:

```
{**/Logic/**,**/LUNA/**,**/AUDIO_MASTER/**}
```

---

## ✨ The Phineas Potts Standard

Glob patterns help achieve **MAGICAL** file management:

- ⚡ Find files **instantly** (no manual searching)
- 🎯 Precise targeting (no false positives)
- 🛡️ Safe exclusions (protect critical data)
- 🚀 Fast cleanup (skip irrelevant files)

**Use glob patterns to make file operations PERFECT.**

---

## 📖 Official Documentation

VS Code Glob Patterns: https://code.visualstudio.com/docs/editor/codebasics#_glob-patterns  
Last Updated: December 10, 2025

---

**Remember**: Glob patterns are tools for **PRECISION** and **SPEED** - essential for the Phineas Potts Standard! 🚗✨
