# CLAUDE-CURSOR INTEGRATION VIA KEYBOARD MAESTRO
# Install: https://www.keyboardmaestro.com

## MACRO 1: Send Code from Cursor to Claude
# Hotkey: ⌘⌥C (Command-Option-C)

1. Copy selection (⌘C in Cursor)
2. Activate Safari/Chrome (Claude.ai tab)
3. Click in message box
4. Type: "Review this code: "
5. Paste (⌘V)
6. Press Enter
7. Return to Cursor

## MACRO 2: Get Claude Response Back to Cursor
# Hotkey: ⌘⌥V (Command-Option-V)

1. In Claude.ai, select last response
2. Copy (⌘C)
3. Activate Cursor
4. Paste (⌘V)

## MACRO 3: Unified Ask-Claude
# Hotkey: ⌘⌥A (Command-Option-A)

1. Copy selection from Cursor
2. Activate Claude.ai
3. Paste into message
4. Add prefix: "Improve this: "
5. Submit
6. Wait 3 seconds
7. Copy response
8. Return to Cursor
9. Create new file with response

## MACRO 4: Voice-Triggered Claude Review
# Trigger: Say "Claude review"

1. Copy from Cursor
2. Send to Claude.ai
3. Speak response back via TTS
4. Return to Cursor

## SETUP INSTRUCTIONS:

1. Download Keyboard Maestro: https://www.keyboardmaestro.com ($36 one-time)
2. Create new Macro Group: "Claude-Cursor"
3. Add macros above
4. Assign hotkeys
5. Test

## ADVANCED: AUTO-PASTE RESPONSES

Macro watches clipboard:
- If clipboard contains code + "Claude says:"
- Auto-paste to Cursor at cursor position
- Show notification
