# Noizy.AI Code Service (FastAPI)
# Provides linting, formatting, and AI code suggestions/fixes

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import tempfile
import os

app = FastAPI(title="Noizy.AI Code Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/lint")
async def lint_code(request: Request):
    data = await request.json()
    code = data.get("code", "")
    if not code:
        return JSONResponse({"error": "No code provided"}, status_code=400)
    # Use black for Python formatting
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py', mode='w+') as tmp:
        tmp.write(code)
        tmp.flush()
        try:
            result = subprocess.run(["black", tmp.name, "--fast", "--diff"], capture_output=True, text=True)
            with open(tmp.name, 'r') as f:
                formatted = f.read()
            return {"formatted": formatted, "diff": result.stdout}
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)
        finally:
            os.unlink(tmp.name)

@app.post("/suggest")
async def ai_suggest(request: Request):
    data = await request.json()
    code = data.get("code", "")
    prompt = data.get("prompt", "Improve this code.")
    # Placeholder: Integrate with OpenAI, Noizy.AI, or other LLM here
    # For now, just echo the code
    return {"suggestion": f"[Noizy.AI] {prompt}\n{code}"}

@app.get("/health")
def health():
    return {"status": "ok", "service": "Noizy.AI Code Service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8899)
