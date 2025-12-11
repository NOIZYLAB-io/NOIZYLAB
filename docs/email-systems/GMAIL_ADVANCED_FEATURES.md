# 🚀 Gmail Advanced Features & Power User Guide

## 🎯 Ultimate Gmail Configuration for rsplowman@gmail.com

---

## 🔥 ADVANCED SEARCH OPERATORS

### Master Gmail Search

**Basic Operators:**
- `from:email@domain.com` - Emails from specific sender
- `to:email@domain.com` - Emails to specific address
- `subject:keyword` - Search in subject line
- `has:attachment` - Emails with attachments
- `filename:document.pdf` - Search by attachment name
- `larger:10M` - Emails larger than 10MB
- `smaller:1M` - Emails smaller than 1MB

**Status Operators:**
- `is:unread` - Unread emails
- `is:read` - Read emails
- `is:starred` - Starred emails
- `is:important` - Important emails
- `is:sent` - Sent emails
- `is:draft` - Draft emails
- `is:archived` - Archived emails

**Date Operators:**
- `after:2025/1/1` - After date
- `before:2025/12/31` - Before date
- `newer_than:7d` - Newer than 7 days
- `older_than:30d` - Older than 30 days

**Label Operators:**
- `label:fishmusicinc.com` - Emails with label
- `label:Priority` - Priority label
- `-label:Notifications` - Exclude label

**Combined Searches:**
```
from:rp@fishmusicinc.com is:unread has:attachment
label:Priority newer_than:3d
to:info@fishmusicinc.com larger:5M
```

---

## 🎨 CUSTOM INBOX VIEWS

### Multiple Inboxes Setup

1. **Go to:** https://mail.google.com/mail/u/0/#settings/inbox
2. **Enable:** Multiple Inboxes
3. **Create Sections:**

**Section 1: Priority**
- Search: `is:important is:unread`
- Panel title: "Priority"

**Section 2: Today**
- Search: `newer_than:1d is:unread`
- Panel title: "Today"

**Section 3: Attachments**
- Search: `has:attachment is:unread`
- Panel title: "With Files"

**Section 4: Waiting For**
- Search: `label:Waiting-For is:unread`
- Panel title: "Action Required"

---

## 🏷️  ADVANCED LABEL SYSTEM

### Label Hierarchy

Create nested labels for better organization:

**Primary Labels:**
- 📧 fishmusicinc.com
  - rp@fishmusicinc.com
  - info@fishmusicinc.com
- 📧 noizylab.ca
  - rsp@noizylab.ca
  - help@noizylab.ca
  - hello@noizylab.ca
- 📧 iCloud
  - rsplowman@icloud.com

**Status Labels:**
- ⚡ Priority
- 📋 To Do
- ⏳ Waiting For
- ✅ Done
- 📎 Attachments
- 🔔 Notifications

**Project Labels:**
- Project-Name
- Client-Name
- Category

---

## 🔍 ADVANCED FILTERS

### Power Filter Examples

#### Filter 1: Auto-Archive Newsletters
```
From: contains "noreply" OR "newsletter" OR "unsubscribe"
Actions:
- Skip Inbox (Archive it)
- Apply label: "Newsletters"
- Never mark as spam
```

#### Filter 2: Priority Senders
```
From: rp@fishmusicinc.com OR rsp@noizylab.ca
Actions:
- Always mark as important
- Star it
- Apply label: "Priority"
- Never mark as spam
```

#### Filter 3: Large Attachments
```
Has attachment: yes
Larger than: 5M
Actions:
- Apply label: "Large Attachments"
- Star it
- Forward to: rsplowman@gmail.com
```

#### Filter 4: Calendar Invites
```
Subject: contains "invitation" OR "calendar"
Has attachment: yes
Actions:
- Apply label: "Calendar"
- Never mark as spam
```

#### Filter 5: Social Media Notifications
```
From: contains "facebook" OR "twitter" OR "linkedin" OR "instagram"
Actions:
- Skip Inbox (Archive it)
- Apply label: "Social"
- Never mark as spam
```

---

## ⚡ KEYBOARD SHORTCUTS MASTER LIST

### Navigation
- `j` / `k` - Next / Previous email
- `o` / `Enter` - Open email
- `u` - Return to inbox
- `g` then `i` - Go to inbox
- `g` then `s` - Go to starred
- `g` then `t` - Go to sent
- `g` then `d` - Go to drafts
- `g` then `a` - Go to all mail

### Actions
- `c` - Compose
- `r` - Reply
- `a` - Reply all
- `f` - Forward
- `e` - Archive
- `#` - Delete
- `x` - Select email
- `*` - Star
- `+` - Mark important
- `-` - Mark unimportant

### Search
- `/` - Search
- `Esc` - Clear search

### Composing
- `Tab` then `Enter` - Send
- `Ctrl+Enter` - Send (Windows)
- `Cmd+Enter` - Send (Mac)

---

## 🤖 GMAIL LABS (Experimental Features)

### Enable Labs

1. Go to: https://mail.google.com/mail/u/0/#settings/labs
2. Enable these recommended labs:

**Canned Responses**
- Save email templates
- Quick access to common replies

**Undo Send**
- Already in main settings, but labs version has more options

**Google Calendar Gadget**
- View calendar in Gmail sidebar

**Preview Pane**
- Split view for reading emails

**Right-side Chat**
- Move chat to right side

**Unread Message Icon**
- Badge with unread count

**Custom Keyboard Shortcuts**
- Create your own shortcuts

---

## 📧 SEND & ARCHIVE

### Enable Send & Archive

1. Go to: https://mail.google.com/mail/u/0/#settings/general
2. Enable "Send & Archive"
3. Button appears when replying

**Benefits:**
- Automatically archive after sending
- Keeps inbox clean
- Faster email processing

---

## 🎯 SMART FEATURES

### Smart Compose
- AI-powered email writing
- Suggests completions as you type
- Learn your writing style

### Smart Reply
- Quick reply suggestions
- Based on email content
- One-click responses

### Nudges
- Reminds you to follow up
- Highlights important emails
- Suggests replies

---

## 📱 MOBILE POWER FEATURES

### Gmail Mobile App

**Swipe Actions:**
- Swipe right = Archive
- Swipe left = Delete
- Long swipe = More options

**Quick Actions:**
- Long press email = Quick menu
- Swipe down = Refresh
- Pull to refresh

**Notifications:**
- Enable for important emails only
- Customize notification sounds
- Smart notifications

---

## 🔒 SECURITY ADVANCED

### 2-Step Verification
- Required for security
- App-specific passwords
- Backup codes

### Account Activity
- Monitor sign-ins
- Review devices
- Check recent activity

### Less Secure Apps
- Disable for security
- Use app-specific passwords instead

---

## 📊 PRODUCTIVITY METRICS

### Track Your Email Habits

**Gmail Insights:**
- Time spent in email
- Response times
- Email volume

**Third-Party Tools:**
- Boomerang (scheduling, follow-ups)
- Mixmax (email tracking)
- Mailtrack (read receipts)

---

## 🎨 CUSTOMIZATION

### Themes
- Custom backgrounds
- Dark mode
- High contrast

### Density
- Comfortable (default)
- Cozy (more emails visible)
- Compact (maximum density)

### Inbox Type
- Default
- Important first
- Unread first
- Starred first
- Priority Inbox

---

## 🔗 QUICK LINKS REFERENCE

- **All Settings:** https://mail.google.com/mail/u/0/#settings/all
- **Accounts:** https://mail.google.com/mail/u/0/#settings/accounts
- **Labels:** https://mail.google.com/mail/u/0/#settings/labels
- **Filters:** https://mail.google.com/mail/u/0/#settings/filters
- **General:** https://mail.google.com/mail/u/0/#settings/general
- **Inbox:** https://mail.google.com/mail/u/0/#settings/inbox
- **Labs:** https://mail.google.com/mail/u/0/#settings/labs
- **Themes:** https://mail.google.com/mail/u/0/#settings/themes
- **Security:** https://myaccount.google.com/security

---

## 🚀 PRO TIPS

1. **Use Multiple Inboxes** for different views
2. **Create Label Shortcuts** for quick access
3. **Use Filters** to auto-organize
4. **Master Keyboard Shortcuts** for speed
5. **Enable Smart Features** for efficiency
6. **Use Search Operators** for finding emails
7. **Archive, Don't Delete** (unless necessary)
8. **Use Stars** for priority marking
9. **Set Up Send & Archive** for clean inbox
10. **Regular Security Audits** for safety

---

**Your Gmail:** rsplowman@gmail.com  
**Status:** Maximum Power Configuration! 🚀

