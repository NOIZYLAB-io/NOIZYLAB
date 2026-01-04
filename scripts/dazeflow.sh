#!/bin/bash
# ==============================================================================
# DAZEFLOW - 1 Day = 1 Chat = 1 Truth
# Daily Flow Tracker for NOIZYLAB
# ==============================================================================

DAZEFLOW_DIR="$HOME/NOIZYLAB/logs/dazeflow"
TODAY=$(date '+%Y-%m-%d')
DAZEFLOW_FILE="$DAZEFLOW_DIR/$TODAY.md"

mkdir -p "$DAZEFLOW_DIR"

# If no args, show today's flow
if [ $# -eq 0 ]; then
    if [ -f "$DAZEFLOW_FILE" ]; then
        cat "$DAZEFLOW_FILE"
    else
        echo "No DAZEFLOW for $TODAY yet."
        echo "Usage: dazeflow [command]"
        echo ""
        echo "Commands:"
        echo "  init         - Start today's flow"
        echo "  focus [text] - Set today's ONE THING"
        echo "  win [text]   - Log a win"
        echo "  block [text] - Log a blocker"
        echo "  note [text]  - Add a note"
        echo "  close        - Close out the day"
        echo "  show         - Show today's flow"
        echo "  week         - Show this week's flows"
    fi
    exit 0
fi

case "$1" in
    init)
        if [ -f "$DAZEFLOW_FILE" ]; then
            echo "DAZEFLOW for $TODAY already exists."
            exit 1
        fi
        cat > "$DAZEFLOW_FILE" << EOF
# DAZEFLOW: $TODAY

## 🎯 ONE THING
[Not set yet]

## ✅ WINS
- 

## 🚧 BLOCKERS
- 

## 📝 NOTES
- Started: $(date '+%H:%M')

## 🔥 STATUS
ACTIVE

---
*GORUNFREE*
EOF
        echo "✅ DAZEFLOW initialized for $TODAY"
        ;;
    
    focus)
        shift
        FOCUS_TEXT="$*"
        if [ -z "$FOCUS_TEXT" ]; then
            echo "Usage: dazeflow focus [your one thing]"
            exit 1
        fi
        sed -i '' "s/\[Not set yet\]/$FOCUS_TEXT/" "$DAZEFLOW_FILE"
        echo "🎯 Focus set: $FOCUS_TEXT"
        ;;
    
    win)
        shift
        WIN_TEXT="$*"
        if [ -z "$WIN_TEXT" ]; then
            echo "Usage: dazeflow win [what you accomplished]"
            exit 1
        fi
        sed -i '' "/## ✅ WINS/a\\
- $(date '+%H:%M') $WIN_TEXT" "$DAZEFLOW_FILE"
        echo "✅ Win logged: $WIN_TEXT"
        ;;
    
    block)
        shift
        BLOCK_TEXT="$*"
        if [ -z "$BLOCK_TEXT" ]; then
            echo "Usage: dazeflow block [what's blocking you]"
            exit 1
        fi
        sed -i '' "/## 🚧 BLOCKERS/a\\
- $(date '+%H:%M') $BLOCK_TEXT" "$DAZEFLOW_FILE"
        echo "🚧 Blocker logged: $BLOCK_TEXT"
        ;;
    
    note)
        shift
        NOTE_TEXT="$*"
        if [ -z "$NOTE_TEXT" ]; then
            echo "Usage: dazeflow note [your note]"
            exit 1
        fi
        sed -i '' "/## 📝 NOTES/a\\
- $(date '+%H:%M') $NOTE_TEXT" "$DAZEFLOW_FILE"
        echo "📝 Note added: $NOTE_TEXT"
        ;;
    
    close)
        sed -i '' "s/ACTIVE/COMPLETE - $(date '+%H:%M')/" "$DAZEFLOW_FILE"
        echo "🏁 DAZEFLOW closed for $TODAY"
        ;;
    
    show)
        if [ -f "$DAZEFLOW_FILE" ]; then
            cat "$DAZEFLOW_FILE"
        else
            echo "No DAZEFLOW for $TODAY"
        fi
        ;;
    
    week)
        echo "📅 This Week's DAZEFLOWS:"
        echo ""
        for i in {0..6}; do
            DATE=$(date -v-${i}d '+%Y-%m-%d')
            FILE="$DAZEFLOW_DIR/$DATE.md"
            if [ -f "$FILE" ]; then
                FOCUS=$(grep -A1 "## 🎯 ONE THING" "$FILE" | tail -1)
                STATUS=$(grep "## 🔥 STATUS" "$FILE" -A1 | tail -1)
                echo "  $DATE: $FOCUS [$STATUS]"
            fi
        done
        ;;
    
    *)
        echo "Unknown command: $1"
        echo "Run 'dazeflow' with no args for help."
        exit 1
        ;;
esac
