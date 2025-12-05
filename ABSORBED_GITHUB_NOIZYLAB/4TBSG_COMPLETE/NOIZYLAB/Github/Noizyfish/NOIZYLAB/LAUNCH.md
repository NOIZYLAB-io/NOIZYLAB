# 🚀 Launch Guide - AI Engine Aggregator

## Quick Launch (Recommended)

Simply run:
```bash
cd /Users/m2ultra/ai-aggregator
./start.sh
```

The script will:
1. Activate the virtual environment
2. Create config.json if needed
3. Start the Flask server
4. Open in your browser at `http://localhost:5000`

---

## Manual Launch

### Step 1: Activate Virtual Environment
```bash
cd /Users/m2ultra/ai-aggregator
source venv/bin/activate
```

### Step 2: Start the Server
```bash
python app.py
```

### Step 3: Open Browser
Navigate to: `http://localhost:5000`

---

## First Time Setup

If this is your first time running:

1. **Run Setup Script:**
   ```bash
   ./setup.sh
   ```

2. **Configure API Keys:**
   - Option A: Use the Settings UI (Recommended)
     - Click "⚙️ Settings" after starting the app
     - Enter your API keys for each engine
     - Enable the engines you want to use
   
   - Option B: Edit config.json directly
     ```bash
     nano config.json  # or use your preferred editor
     ```

3. **Start the Application:**
   ```bash
   ./start.sh
   ```

---

## Adding API Keys

### Where to Get API Keys

#### ChatGPT (OpenAI)
1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

#### Claude (Anthropic)
1. Go to https://console.anthropic.com/
2. Sign in or create account
3. Navigate to API Keys
4. Create a new key
5. Copy the key (starts with `sk-ant-`)

#### Gemini (Google)
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (starts with `AIza`)

#### GitHub Copilot
1. Go to https://github.com/settings/copilot
2. Ensure you have a Copilot subscription
3. API key is available in GitHub settings

#### Other Engines
- **Mistral AI**: https://console.mistral.ai/
- **Perplexity**: https://www.perplexity.ai/settings/api
- **Cohere**: https://dashboard.cohere.ai/
- **Grok (xAI)**: https://x.ai/api
- **OpenRouter**: https://openrouter.ai/keys

---

## Configuration Example

Edit `config.json`:
```json
{
  "openai": {
    "api_key": "sk-your-key-here",
    "enabled": true,
    "display_name": "ChatGPT (GPT-4)"
  },
  "anthropic": {
    "api_key": "sk-ant-your-key-here",
    "enabled": true,
    "display_name": "Claude (Anthropic)"
  },
  "google": {
    "api_key": "AIza-your-key-here",
    "enabled": true,
    "display_name": "Gemini (Google)"
  }
}
```

---

## Troubleshooting

### Port Already in Use

Change the port:
```bash
python app.py --port 5001
```
Or edit `app.py` and change the port in the last line.

### Module Not Found Error

Install dependencies:
```bash
pip install -r requirements.txt
```

### Virtual Environment Not Activating

Create it first:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Engine Not Responding

1. Check API key is correct
2. Verify engine is enabled in config
3. Check your internet connection
4. Review error message in response card
5. Verify you have credits/quota remaining

---

## Using the Application

### Basic Workflow

1. **Select Engines**
   - Click engines to toggle selection
   - Or drag engines to the selected area
   - Engines are organized by category

2. **Enter Prompt**
   - Type your question in the prompt box
   - Be specific and clear for best results

3. **Query**
   - Click "🚀 Query All Selected Engines"
   - Watch responses come in real-time

4. **Review & Blend**
   - Compare responses side-by-side
   - Copy individual responses
   - Click "🔀 Blend Responses" to combine insights
   - Export in your preferred format

### Subscription Monitoring

1. Click "📊 Subscriptions" in header
2. Configure subscription details for each engine:
   - Plan name
   - Tier level
   - Monthly limits (requests, tokens, budget)
3. Monitor usage in real-time
4. View dashboard summary

---

## Advanced Usage

### Creating Specialist Agents

See [`SPECIALIST_AGENT_BUILDER.md`](SPECIALIST_AGENT_BUILDER.md) for detailed guide.

### Custom Configuration

All configuration files are in JSON format:
- `config.json` - API keys and engine settings
- `subscriptions.json` - Subscription information
- `usage.json` - Usage statistics
- `history.json` - Query history

---

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

---

## Next Steps

- ✅ Set up your API keys
- ✅ Configure subscription monitoring
- ✅ Create your first multi-engine query
- ✅ Explore specialist agent builder
- ✅ Monitor your usage and costs

---

**Ready to launch! 🚀**

For more information, see:
- [README.md](README.md) - Full documentation
- [QUICK_START.md](QUICK_START.md) - Quick start guide
- [SPECIALIST_AGENT_BUILDER.md](SPECIALIST_AGENT_BUILDER.md) - Specialist guide
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Project overview

