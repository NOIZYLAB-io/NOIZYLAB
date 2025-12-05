#!/usr/bin/env node

const crypto = require('crypto');

// Same key components and salt as in both files
const KEY_PARTS = [
    Buffer.from([0x4B, 0x65, 0x79, 0x50, 0x61, 0x72, 0x74, 0x31]), // KeyPart1
    Buffer.from([0x53, 0x65, 0x63, 0x75, 0x72, 0x65, 0x32, 0x33]), // Secure23
    Buffer.from([0x46, 0x61, 0x73, 0x74, 0x58, 0x4F, 0x52, 0x21])  // FastXOR!
];

const SALT = Buffer.from([
    0x53, 0x61, 0x6C, 0x74, 0x65, 0x64, 0x58, 0x4F,
    0x52, 0x45, 0x6E, 0x63, 0x72, 0x79, 0x70, 0x74
]);

function encrypt(apiKey) {
    // Generate a random nonce (8 bytes)
    const nonce = crypto.randomBytes(8);
    
    // Derive key with nonce
    const masterKey = Buffer.concat(KEY_PARTS);
    const baseKey = crypto.pbkdf2Sync(masterKey, SALT, 1000, 64, 'sha256');
    const keyWithNonce = crypto.createHash('sha256')
        .update(baseKey)
        .update(nonce)
        .digest();
    
    // Fast XOR encryption with position scrambling
    const dataBuffer = Buffer.from(apiKey, 'utf8');
    const encrypted = Buffer.alloc(dataBuffer.length);
    const keyLen = keyWithNonce.length;
    
    for (let i = 0; i < dataBuffer.length; i++) {
        const keyByte = keyWithNonce[i % keyLen];
        const posScramble = ((i * 7) ^ (i >> 3)) & 0xFF;
        encrypted[i] = dataBuffer[i] ^ keyByte ^ posScramble;
    }
    
    // Combine nonce + encrypted data
    const combined = Buffer.concat([nonce, encrypted]);
    
    return combined.toString('base64');
}

function decrypt(encryptedData) {
    const combined = Buffer.from(encryptedData, 'base64');
    
    // Extract nonce (first 8 bytes)
    const nonce = combined.slice(0, 8);
    const encrypted = combined.slice(8);
    
    // Derive key (fast PBKDF2 with 1000 iterations)
    const masterKey = Buffer.concat(KEY_PARTS);
    const baseKey = crypto.pbkdf2Sync(masterKey, SALT, 1000, 64, 'sha256');
    
    // Mix nonce into key
    const keyWithNonce = crypto.createHash('sha256')
        .update(baseKey)
        .update(nonce)
        .digest();
    
    // Fast XOR decryption with position scrambling
    const decrypted = Buffer.alloc(encrypted.length);
    const keyLen = keyWithNonce.length;
    
    for (let i = 0; i < encrypted.length; i++) {
        const keyByte = keyWithNonce[i % keyLen];
        const posScramble = ((i * 7) ^ (i >> 3)) & 0xFF;
        decrypted[i] = encrypted[i] ^ keyByte ^ posScramble;
    }
    
    return decrypted.toString('utf8');
}

// Test with the current encrypted data
const ENCRYPTED_PATTERN_DATA = "klweQxIhL36ksRGxbsJqygYgcziZF2E/Qtg2UFqugsD2k0UJ3krzEXdS2nzv7DU=";

console.log("Testing XOR Encryption/Decryption");
console.log("==================================\n");

// Test 1: Decrypt the existing encrypted data
console.log("Test 1: Decrypting existing encrypted data");
console.log("Encrypted: " + ENCRYPTED_PATTERN_DATA);
try {
    const decrypted = decrypt(ENCRYPTED_PATTERN_DATA);
    console.log("Decrypted: " + decrypted);
    console.log("Starts with 'AIza': " + decrypted.startsWith('AIza'));
    console.log("Length: " + decrypted.length);
} catch (error) {
    console.log("Decryption failed: " + error.message);
}

console.log("\n" + "=".repeat(50) + "\n");

// Test 2: Full cycle test with a sample API key
const testKey = "AIzaSyTest123456789ABCDEFGHIJKLMNOP";
console.log("Test 2: Full encryption/decryption cycle");
console.log("Original:  " + testKey);

const encrypted = encrypt(testKey);
console.log("Encrypted: " + encrypted);

const decrypted2 = decrypt(encrypted);
console.log("Decrypted: " + decrypted2);
console.log("Match:     " + (testKey === decrypted2 ? "✅ SUCCESS" : "❌ FAILED"));

console.log("\n" + "=".repeat(50) + "\n");

// Test 3: Multiple cycles to ensure consistency
console.log("Test 3: Multiple encryption/decryption cycles");
let allPassed = true;
for (let i = 0; i < 5; i++) {
    const enc = encrypt(testKey);
    const dec = decrypt(enc);
    const passed = (dec === testKey);
    console.log(`Cycle ${i + 1}: ${passed ? "✅" : "❌"} (Encrypted: ${enc.substring(0, 20)}...)`);
    allPassed = allPassed && passed;
}
console.log("All cycles passed: " + (allPassed ? "✅ SUCCESS" : "❌ FAILED"));