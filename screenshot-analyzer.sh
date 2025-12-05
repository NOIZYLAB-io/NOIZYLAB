#!/bin/bash
# SCREENSHOT ANALYZER
# Capture screenshot and analyze with AI vision
# PHASE 2 - Advanced Features

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}📸 Screenshot Analyzer${NC}"
echo ""

# Detect platform
PLATFORM=$(uname -s)

# Temporary file for screenshot
SCREENSHOT="/tmp/ai-screenshot-$(date +%s).png"

# Take screenshot based on platform
case "$PLATFORM" in
    Darwin)
        echo -e "${BLUE}📷 Select area to capture (press Space for full screen)${NC}"
        screencapture -i "$SCREENSHOT" 2>/dev/null
        
        if [ ! -f "$SCREENSHOT" ]; then
            echo -e "${YELLOW}⚠️  Screenshot cancelled${NC}"
            exit 0
        fi
        ;;
    
    Linux)
        if command -v gnome-screenshot &> /dev/null; then
            echo -e "${BLUE}📷 Capturing screenshot...${NC}"
            gnome-screenshot -a -f "$SCREENSHOT"
        elif command -v scrot &> /dev/null; then
            echo -e "${BLUE}📷 Select area to capture...${NC}"
            scrot -s "$SCREENSHOT"
        else
            echo -e "${YELLOW}⚠️  No screenshot tool found${NC}"
            echo "Install: sudo apt install gnome-screenshot"
            exit 1
        fi
        ;;
    
    *)
        echo -e "${YELLOW}⚠️  Platform not supported: $PLATFORM${NC}"
        exit 1
        ;;
esac

echo -e "${GREEN}✓ Screenshot captured${NC}"
echo ""

# Convert to base64
echo -e "${BLUE}🔄 Processing image...${NC}"
IMAGE_BASE64=$(base64 < "$SCREENSHOT")

# Analysis options
echo -e "${CYAN}What would you like to know about this image?${NC}"
echo ""
echo "1. Describe what's in the image"
echo "2. Extract text (OCR)"
echo "3. Identify UI elements"
echo "4. Explain code/diagram"
echo "5. Custom question"
echo ""
read -p "Choose (1-5): " CHOICE

case "$CHOICE" in
    1) PROMPT="Describe everything you see in this image in detail." ;;
    2) PROMPT="Extract all text from this image. Present it in a readable format." ;;
    3) PROMPT="Identify all UI elements, buttons, and interface components in this image. Describe their layout." ;;
    4) PROMPT="Explain the code, diagram, or technical content shown in this image." ;;
    5) 
        echo ""
        read -p "Your question: " CUSTOM_PROMPT
        PROMPT="$CUSTOM_PROMPT"
        ;;
    *)
        PROMPT="Describe what you see in this image."
        ;;
esac

echo ""
echo -e "${BLUE}🤖 Analyzing with Claude Vision...${NC}"
echo ""

# Call Claude API with vision
RESPONSE=$(curl -s https://api.anthropic.com/v1/messages \
    -H "x-api-key: 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" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d "{
        \"model\": \"claude-sonnet-4-20250514\",
        \"max_tokens\": 2000,
        \"messages\": [{
            \"role\": \"user\",
            \"content\": [
                {
                    \"type\": \"image\",
                    \"source\": {
                        \"type\": \"base64\",
                        \"media_type\": \"image/png\",
                        \"data\": \"$IMAGE_BASE64\"
                    }
                },
                {
                    \"type\": \"text\",
                    \"text\": \"$PROMPT\"
                }
            ]
        }]
    }")

# Extract response text
ANALYSIS=$(echo "$RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data['content'][0]['text'])" 2>/dev/null)

if [ -z "$ANALYSIS" ]; then
    echo -e "${YELLOW}⚠️  Analysis failed${NC}"
    echo "Response: $RESPONSE"
else
    echo -e "${GREEN}✓ Analysis complete${NC}"
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo "$ANALYSIS"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    # Copy to clipboard
    if command -v pbcopy &> /dev/null; then
        echo "$ANALYSIS" | pbcopy
        echo -e "${GREEN}✓ Copied to clipboard${NC}"
    elif command -v xclip &> /dev/null; then
        echo "$ANALYSIS" | xclip -selection clipboard
        echo -e "${GREEN}✓ Copied to clipboard${NC}"
    fi
    
    # Save analysis
    ANALYSIS_FILE="/tmp/ai-analysis-$(date +%s).txt"
    echo "$ANALYSIS" > "$ANALYSIS_FILE"
    echo -e "${BLUE}💾 Saved to: $ANALYSIS_FILE${NC}"
fi

# Keep or delete screenshot
echo ""
read -p "Keep screenshot? (y/n): " KEEP

if [ "$KEEP" = "y" ] || [ "$KEEP" = "Y" ]; then
    SAVED_SCREENSHOT="$HOME/Desktop/ai-screenshot-$(date +%Y%m%d-%H%M%S).png"
    mv "$SCREENSHOT" "$SAVED_SCREENSHOT"
    echo -e "${GREEN}✓ Screenshot saved: $SAVED_SCREENSHOT${NC}"
else
    rm "$SCREENSHOT"
    echo -e "${BLUE}Screenshot deleted${NC}"
fi

echo ""
echo -e "${CYAN}🎯 Done!${NC}"
