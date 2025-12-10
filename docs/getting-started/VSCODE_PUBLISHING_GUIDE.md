# 📦 VS Code Marketplace Publishing Guide

Complete step-by-step guide to publish your SSH & WSL extension to the Visual Studio Code Marketplace.

## 🚀 **Quick Publish**

```bash
cd vscode
npm run build
```

This will create a `.vsix` file ready for upload to the VS Code Marketplace.

## 📋 **Step-by-Step Publishing Process**

### **Step 1: Prepare Your Extension**

1. **Navigate to VS Code directory**
   ```bash
   cd vscode
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Build the extension**
   ```bash
   npm run build
   ```

This creates a `.vsix` file (e.g., `ssh-wsl-remote-development-0.0.1.vsix`)

### **Step 2: Create VS Code Marketplace Account**

1. **Visit the Publisher Portal**
   - Go to: https://marketplace.visualstudio.com/manage
   - Sign in with your Microsoft account

2. **Create a Publisher**
   - Click "Create publisher"
   - **Publisher ID**: `sak1620` (or your preferred ID)
   - **Display Name**: Your name or organization
   - **Description**: Brief description of your extensions
   - **Website**: Your website or GitHub profile

### **Step 3: Upload Your Extension**

#### **Option A: Web Upload (Recommended for first-time)**

1. **Go to Publisher Portal**
   - Visit: https://marketplace.visualstudio.com/manage/publishers/sak1620

2. **Upload Extension**
   - Click "New extension" → "Visual Studio Code"
   - Upload your `.vsix` file
   - The marketplace will automatically extract metadata

3. **Review Information**
   - **Name**: SSH & WSL Remote Development
   - **Categories**: Other, Extension Packs
   - **Tags**: ssh, wsl, remote, linux, server, development
   - **Description**: Automatically filled from package.json
   - **Repository**: https://github.com/sak1620/kiro-ssh-wsl-extension

4. **Submit for Review**
   - Click "Upload"
   - Wait for automated validation (usually instant)
   - Extension goes live immediately if validation passes

#### **Option B: Command Line Publishing**

1. **Install vsce globally**
   ```bash
   npm install -g vsce
   ```

2. **Create Personal Access Token**
   - Go to: https://dev.azure.com/[your-org]/_usersSettings/tokens
   - Create token with "Marketplace (manage)" scope
   - Copy the token

3. **Login to vsce**
   ```bash
   vsce login sak1620
   # Enter your Personal Access Token when prompted
   ```

4. **Publish directly**
   ```bash
   vsce publish
   ```

### **Step 4: Verify Publication**

1. **Check Marketplace**
   - Visit: https://marketplace.visualstudio.com/items?itemName=sak1620.ssh-wsl-remote-development
   - Verify all information is correct

2. **Test Installation**
   ```bash
   code --install-extension sak1620.ssh-wsl-remote-development
   ```

## 🎯 **Marketplace Optimization**

### **Extension Manifest (package.json)**

Key fields for marketplace visibility:

```json
{
  "displayName": "SSH & WSL Remote Development",
  "description": "Complete SSH and WSL integration for VS Code - Connect to remote servers and WSL distributions seamlessly",
  "categories": ["Other", "Extension Packs"],
  "keywords": ["ssh", "wsl", "remote", "linux", "server", "development", "terminal", "sftp", "deployment"],
  "icon": "assets/icon.png",
  "repository": {
    "type": "git",
    "url": "https://github.com/sak1620/kiro-ssh-wsl-extension"
  }
}
```

### **README.md Optimization**

Your README.md is automatically used as the marketplace description. Ensure it includes:

- ✅ Clear feature list with emojis
- ✅ Installation instructions
- ✅ Usage examples with screenshots
- ✅ Configuration options
- ✅ Troubleshooting section
- ✅ Links to documentation and support

### **Screenshots and Media**

Add screenshots to showcase your extension:

1. **Create screenshots** showing:
   - Connection interface
   - File browser
   - Command execution
   - Settings panel

2. **Add to package.json**:
   ```json
   "galleryBanner": {
     "color": "#1e1e1e",
     "theme": "dark"
   }
   ```

## 🔄 **Update Process**

### **For Future Updates**

1. **Update version** in `package.json`:
   ```json
   "version": "0.0.2"
   ```

2. **Build and publish**:
   ```bash
   npm run build
   vsce publish
   ```

3. **Or upload manually** to the marketplace portal

### **Version Management**

- **Patch** (0.0.1 → 0.0.2): Bug fixes
- **Minor** (0.0.1 → 0.1.0): New features
- **Major** (0.0.1 → 1.0.0): Breaking changes

## 📊 **Success Metrics**

Track these metrics after publication:

- **Installs**: Number of extension installations
- **Ratings**: User ratings and reviews
- **Downloads**: Download statistics
- **Active Users**: Daily/monthly active users

## 🆘 **Troubleshooting**

### **Common Issues**

1. **Validation Errors**
   - Check package.json format
   - Ensure all required fields are present
   - Verify icon file exists

2. **Publishing Fails**
   - Check Personal Access Token permissions
   - Verify publisher ID is correct
   - Ensure you're logged in: `vsce login`

3. **Extension Not Appearing**
   - Wait 5-10 minutes for indexing
   - Check if extension was rejected (email notification)
   - Verify publisher and extension names

### **Getting Help**

- **VS Code Extension API**: https://code.visualstudio.com/api
- **Publishing Documentation**: https://code.visualstudio.com/api/working-with-extensions/publishing-extension
- **vsce CLI Help**: `vsce --help`

## 🎉 **Post-Publication**

### **Promote Your Extension**

1. **Social Media**
   - Tweet about your extension
   - Post on LinkedIn
   - Share in developer communities

2. **Documentation**
   - Create GitHub Pages site
   - Write blog posts
   - Record demo videos

3. **Community Engagement**
   - Respond to user issues
   - Collect feedback
   - Plan future features

### **Maintenance**

1. **Monitor Issues**: Check GitHub issues regularly
2. **Update Dependencies**: Keep packages up to date
3. **Add Features**: Based on user feedback
4. **Fix Bugs**: Respond quickly to bug reports

---

## 🚀 **Ready to Publish?**

Your VS Code extension is ready for the marketplace! Run:

```bash
cd vscode
npm run build
```

Then upload the generated `.vsix` file to https://marketplace.visualstudio.com/manage

**Good luck with your VS Code extension! 🎉**