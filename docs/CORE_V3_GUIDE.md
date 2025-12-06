# 💎 NoizyLab CORE v3.0 - Ultimate Intelligence Aggregator

## 🚀 What's New

NoizyLab CORE v3.0 introduces three powerful modules:

### 1. 📤 Smart Composer
- **Manual Mode** - Write emails from scratch
- **AI Auto-Draft** - Generate emails from keywords
- **Tone Selection** - Professional, Casual, or Urgent
- **Smart Expansion** - Context-aware email generation

### 2. 📥 Inbox Scanner
- **Gmail Integration** - Read recent emails
- **Inbox Intelligence** - View sender, subject, snippets
- **Real-time Scanning** - Live inbox updates

### 3. 💾 Data Vault
- **CSV Database** - Structured email logging
- **Complete History** - All sent emails tracked
- **Status Tracking** - SENT/FAILED status
- **Searchable Logs** - Easy to analyze

---

## 📋 Modules

### Module 1: Smart Composer
**Purpose**: Send emails with AI assistance

**Features**:
- Select sender identity
- Choose recipient
- Manual or AI-assisted drafting
- Keyword expansion
- Tone selection
- Preview before sending
- Automatic logging to Data Vault

**AI Composer Modes**:
- **Professional** - Formal business tone
- **Casual** - Friendly, relaxed tone
- **Urgent** - Time-sensitive communication

### Module 2: Inbox Scanner
**Purpose**: Read and analyze incoming emails

**Features**:
- Gmail API integration
- Recent email listing
- Sender information
- Subject lines
- Email snippets
- Inbox scanning with progress

**Setup Required**:
1. Get Gmail credentials from Google Cloud Console
2. Save as `config/gmail_credentials.json`
3. First run will authenticate via browser

### Module 3: Data Vault
**Purpose**: Track and analyze sent emails

**Features**:
- CSV database (`email_database.csv`)
- Timestamp tracking
- Identity logging
- Recipient tracking
- Subject logging
- Status tracking (SENT/FAILED)
- Last 20 entries display

---

## 🎯 Usage

### Launch
```bash
nz
```

### Main Menu
1. **📤 Smart Composer** - Send emails
2. **📥 Inbox Scanner** - Read emails
3. **💾 Data Vault** - View history
4. **👤 Identity Config** - Manage identities
5. **🛑 Shutdown** - Exit

### Smart Composer Flow
1. Select sender identity
2. Enter recipient email
3. Choose mode (Manual or AI)
4. If AI: Enter keywords and tone
5. Review draft
6. Send or cancel

### AI Composer Examples

**Keywords**: "meeting, tuesday, starbucks"
**Tone**: Professional
**Result**: Professional meeting request

**Keywords**: "invoice, payment, due"
**Tone**: Urgent
**Result**: Urgent payment reminder

**Keywords**: "follow-up, project, status"
**Tone**: Casual
**Result**: Casual follow-up message

---

## 📊 Data Vault Structure

CSV File: `email_database.csv`

Columns:
- **Timestamp** - When email was sent
- **Identity** - Sender identity used
- **Recipient** - Email recipient
- **Subject** - Email subject
- **Status** - SENT or FAILED

---

## 🔧 Configuration

### Email Identities
Edit `config/email_config.json`:
```json
{
  "identities": {
    "work": {
      "name": "Your Name",
      "email": "work@example.com",
      "signature": "\n\n--\nYour Name"
    }
  }
}
```

### Gmail API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download credentials as JSON
6. Save as `config/gmail_credentials.json`

---

## 🎨 UI Features

- **Rich Terminal UI** - Beautiful color-coded interface
- **Progress Indicators** - Visual feedback during operations
- **Status Panels** - System status at a glance
- **Formatted Tables** - Clean data display
- **Interactive Prompts** - Easy navigation

---

## 📈 Statistics Dashboard

The dashboard shows:
- **Total Sent** - Number of emails sent
- **Last Activity** - Timestamp of last email

---

## 🔐 Security

- Email credentials stored in config files
- Gmail tokens stored securely
- CSV database for audit trail
- No sensitive data in logs

---

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install rich pandas google-api-python-client
   ```

2. **Configure Identities**
   - Edit `config/email_config.json`
   - Or use Configuration Wizard

3. **Launch**
   ```bash
   nz
   ```

4. **Send Your First Email**
   - Select option 1 (Smart Composer)
   - Follow the prompts
   - Email is logged to Data Vault

---

## 💡 Tips

- **AI Composer** works best with specific keywords
- **Data Vault** can be opened in Excel/Google Sheets
- **Inbox Scanner** requires Gmail API setup
- Use **Professional** tone for business emails
- Use **Casual** tone for friendly communication
- Use **Urgent** tone for time-sensitive matters

---

## 🎉 Features Summary

✅ **Smart Composer** - AI-assisted email drafting
✅ **Inbox Scanner** - Gmail integration
✅ **Data Vault** - CSV database logging
✅ **Rich UI** - Beautiful terminal interface
✅ **Statistics** - System status tracking
✅ **Multiple Identities** - Send from different addresses
✅ **Status Tracking** - SENT/FAILED logging

---

**NoizyLab CORE v3.0 - Ultimate Intelligence Aggregator** 💎

