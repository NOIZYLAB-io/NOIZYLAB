# Auto-Accept Extension - Activation Instructions

## ✅ Extension Location
The extension is located at: `~/.cursor/extensions/auto-accept-current-mission.ts`

## 🔄 How to Activate

### Option 1: Reload Cursor Window (Recommended)
1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type: `Developer: Reload Window`
3. Press Enter
4. The extension will be active automatically

### Option 2: Restart Cursor
1. Completely quit Cursor
2. Reopen Cursor
3. The extension will load automatically

## ✅ Verification

The extension will automatically:
- ✅ Auto-accept all review/confirm prompts
- ✅ Auto-accept "apply changes" prompts
- ✅ Auto-accept "proceed" prompts
- ✅ Auto-accept "are you sure" prompts

## 🔧 How It Works

The extension uses a regex pattern to detect review/confirmation prompts:
- `review`
- `confirm`
- `approve`
- `apply changes`
- `proceed`
- `continue`
- `are you sure`
- `accept`

When any of these phrases appear in a prompt, it automatically responds with "yes".

## ⚠️ Safety Features

- **Mission-scoped**: Only active during the current mission/session
- **Auto-disables**: Automatically turns off when mission ends
- **Session override**: Also disables if the session ends unexpectedly

## 🎯 Benefits

- **No interruptions**: Continue working without stopping for approvals
- **Faster workflow**: Changes apply immediately
- **Mission-focused**: Only works during active missions

---

**Note**: If the extension doesn't work after reloading, try restarting Cursor completely.

