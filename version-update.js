const fs = require('fs');
const path = require('path');

// Paths to the files
const packageJsonPath = path.join(__dirname, '../../package.json');
const keployVersionPath = path.join(__dirname, '../../keploy-version.json');

// Get the tag name from environment variables
const tagName = process.env.TAG_NAME;
if (!tagName) {
    console.error('Error: TAG_NAME environment variable is not set.');
    process.exit(1);
}

try {
    // Update package.json
    const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));
    if (packageJson.version !== tagName) {
        console.log(`Updating package.json version from ${packageJson.version} to ${tagName}`);
        packageJson.version = tagName;
        fs.writeFileSync(packageJsonPath, JSON.stringify(packageJson, null, 4));
    } else {
        console.log(`package.json version is already ${tagName}`);
    }

    // Update keploy-version.json
    const keployVersion = JSON.parse(fs.readFileSync(keployVersionPath, 'utf8'));
    if (!keployVersion[tagName]) {
        const lastVersion = Object.keys(keployVersion).pop();
        const lastMapping = keployVersion[lastVersion];
        console.log(`Adding ${tagName} to keploy-version.json with mapping ${lastMapping}`);
        keployVersion[tagName] = lastMapping;
        fs.writeFileSync(keployVersionPath, JSON.stringify(keployVersion, null, 4));
    } else {
        console.log(`${tagName} already exists in keploy-version.json`);
    }
} catch (error) {
    console.error('Error updating files:', error);
    process.exit(1);
}