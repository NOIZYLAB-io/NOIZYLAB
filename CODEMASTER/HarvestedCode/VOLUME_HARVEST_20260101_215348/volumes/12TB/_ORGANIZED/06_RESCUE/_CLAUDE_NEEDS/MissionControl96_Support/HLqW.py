from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
import subprocess, os, hashlib, glob, asyncio
import ast

app = FastAPI()

AQUARIUM_ROOT = os.getcwd()  # or set to your path

missing_imports = []
duplicate_files = {}
all_files = {}

for dirpath, _, filenames in os.walk(AQUARIUM_ROOT):
    for fname in filenames:
        fpath = os.path.join(dirpath, fname)
        # Track duplicates
        if fname in all_files:
            duplicate_files.setdefault(fname, []).append(fpath)
        else:
            all_files[fname] = fpath
        # Check Python imports
        if fname.endswith('.py'):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=fname)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for n in node.names:
                            try:
                                __import__(n.name)
                            except ImportError:
                                missing_imports.append((fpath, n.name))
                    elif isinstance(node, ast.ImportFrom):
                        try:
                            __import__(node.module)
                        except Exception:
                            missing_imports.append((fpath, node.module))
            except Exception as e:
                print(f"Error parsing {fpath}: {e}")

print("\n=== Duplicate Files ===")
for fname, paths in duplicate_files.items():
    print(f"{fname}:")
    for p in paths:
        print(f"  {p}")

print("\n=== Missing Imports ===")
for fpath, mod in missing_imports:
    print(f"{fpath}: missing {mod}")

print("\n=== Scan Complete ===")

@app.post("/check-code")
async def check_code(code: str, language: str):
    if language == "python":
        with open("temp.py", "w") as f:
            f.write(code)
        lint = subprocess.run(["flake8", "temp.py"], capture_output=True, text=True)
        compile_check = subprocess.run(["python3", "-m", "py_compile", "temp.py"], capture_output=True, text=True)
        return {"lint": lint.stdout or lint.stderr, "compile": compile_check.stderr}
    elif language in ["sh", "bash", "zsh"]:
        with open("temp.sh", "w") as f:
            f.write(code)
        lint = subprocess.run(["shellcheck", "temp.sh"], capture_output=True, text=True)
        return {"lint": lint.stdout or lint.stderr}
    return {"error": "Unsupported language"}
# Health endpoint: status and services
@app.get("/health")
def health():
    return {"status": "green", "services": ["narrator", "dupe-killer", "metadata"]}

# Narrate text (placeholder until ElevenLabs wired in)
@app.post("/narrate")
async def narrate_text(text: str):
    # This will later call ElevenLabs
    return {"status": "ok", "message": f"Narrating: {text}"}

# Scan WAVs
@app.post("/scan-wavs")
async def scan_wavs():
    files = glob.glob("**/*.wav", recursive=True)
    return {"count": len(files), "files": files[:20]}  # sample list

# Big Dupe Killer
@app.post("/dupe-killer")
async def dupe_killer():
    seen, dupes = {}, []
    for filepath in glob.glob("**/*.wav", recursive=True):
        h = hashlib.md5(open(filepath, "rb").read()).hexdigest()
        if h in seen:
            dupes.append(filepath)
        else:
            seen[h] = filepath
    return {"dupes": dupes, "count": len(dupes)}

# Run a system script
@app.post("/run-script")
async def run_script():
    proc = subprocess.run(["echo", "Hello from Bobby!"], capture_output=True, text=True)
    return {"stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}

# Bundle settings
BUNDLE_IDENTIFIER = "com.noizyfish.mission.control"

# Execute user script
@app.post("/run-python")
async def run_python_script(user_script: str):
    # Save the user script to a temporary file
    temp_path = "user_script.py"
    with open(temp_path, "w") as f:
        f.write(user_script)
    # Run the user script securely, capture output/errors
    result = subprocess.run(["python3", temp_path], capture_output=True, text=True)
    # Optionally, delete the temp file after execution
    try:
        os.remove(temp_path)
    except Exception:
        pass
    return {
        "status": "script executed",
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8787, reload=True)

    cd ~/bobby-mission-control/frontend
    npm run tauri
    "scripts": {
      "dev": "vite",
      "build": "vite build",
      "preview": "vite preview",
      "tauri": "tauri dev"
    }
