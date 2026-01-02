from __future__ import annotations
import os, asyncio, json, tempfile, subprocess, shlex, textwrap
from pathlib import Path
from typing import Literal
from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="Bobby Gatehouse")
FEED: asyncio.Queue[str] = asyncio.Queue()

async def emit(level: str, msg: str):
    await FEED.put(json.dumps({"level": level, "msg": msg}))

@app.get("/events")
async def events():
    async def gen():
        while True:
            yield f"data: {await FEED.get()}\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")

class CheckReq(BaseModel):
    language: Literal["python","bash","sh","zsh"]
    code: str
    autofix: bool = True
    strict_security: bool = True

def run(cmd: str, cwd: Path|None=None, timeout=25) -> tuple[int,str,str]:
    p = subprocess.run(shlex.split(cmd), cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr

def clean_env() -> dict:
    # Minimal environment for sandboxed commands
    return {"PATH": os.getenv("PATH","/usr/bin:/bin:/usr/local/bin")}

@app.post("/check-code")
async def check_code(req: CheckReq):
    lang = req.language
    code = req.code
    await emit("info", f"Gatehouse: checking ({lang})")

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        if lang == "python":
            src = td/"snippet.py"; src.write_text(code, encoding="utf-8")
            # 1) syntax
            rc, so, se = run(f"python3 -m py_compile {src}", timeout=20)
            syntax_ok = (rc == 0)
            # 2) lint (ruff)
            rc_r, so_r, se_r = run(f"ruff check {src}", timeout=20)
            # 3) format (black) — dry-run unless autofix
            fmt_cmd = f"black {'--quiet ' if req.autofix else '--check '} {src}"
            rc_b, so_b, se_b = run(fmt_cmd, timeout=25)
            # 4) security quick scan (semgrep) – lightweight ruleset
            policy = "p/ci" if req.strict_security else "auto"
            rc_s, so_s, se_s = run(f"semgrep --quiet --config {policy} {src.parent}", timeout=30)
            fixed_code = src.read_text(encoding="utf-8")
            safe = syntax_ok and rc_s == 0
            report = {
                "syntax_ok": syntax_ok,
                "ruff": (so_r+se_r).strip(),
                "black": (so_b+se_b).strip(),
                "semgrep": (so_s+se_s).strip(),
                "safeToRun": safe,
                "autofixed": req.autofix,
                "fixedCode": fixed_code if req.autofix else code,
            }
            await emit("ok" if safe else "error", f"Python check: {'OK' if safe else 'issues found'}")
            return report

        if lang in ("bash","sh","zsh"):
            src = td/"snippet.sh"; src.write_text(code, encoding="utf-8")
            # shellcheck
            shc = subprocess.run(["shellcheck", str(src)], capture_output=True, text=True, env=clean_env())
            # shfmt (auto-fix if allowed)
            if req.autofix:
                subprocess.run(["shfmt","-w",str(src)], capture_output=True, text=True, env=clean_env())
            else:
                subprocess.run(["shfmt","-d",str(src)], capture_output=True, text=True, env=clean_env())
            fixed_code = src.read_text(encoding="utf-8")
            # quick unsafe heuristics
            dangerous = any(t in fixed_code for t in ["rm -rf /","mkfs",":(){ :|:& };:"])
            safe = (shc.returncode == 0) and not dangerous
            report = {
                "shellcheck": (shc.stdout+shc.stderr).strip(),
                "dangerHeuristics": "BLOCK" if dangerous else "OK",
                "safeToRun": safe,
                "autofixed": req.autofix,
                "fixedCode": fixed_code if req.autofix else code,
            }
            await emit("ok" if safe else "error", f"Shell check: {'OK' if safe else 'issues found'}")
            return report

    return JSONResponse({"status":"error","message":"Unsupported language"}, status_code=400)

class RunReq(BaseModel):
    language: Literal["python","bash","sh","zsh"]
    code: str
    assume_safe: bool = False
    timeout_sec: int = 10

@app.post("/run-code")
async def run_code(req: RunReq):
    # Enforce “check first” unless assume_safe explicitly set
    if not req.assume_safe:
        chk = await check_code(CheckReq(language=req.language, code=req.code, autofix=True))
        if isinstance(chk, JSONResponse):  # error path
            return chk
        if not chk.get("safeToRun", False):
            await emit("error","Execution blocked by Gatehouse")
            return JSONResponse({"status":"blocked","reason":"unsafe"}, status_code=403)
        src_code = chk.get("fixedCode", req.code)
    else:
        src_code = req.code

    await emit("info","Runner: executing")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        if req.language == "python":
            src = td/"run.py"; src.write_text(src_code, encoding="utf-8")
            rc, so, se = run(f"python3 -I {src}", timeout=req.timeout_sec)  # -I: isolated mode
        else:
            src = td/"run.sh"; src.write_text(src_code, encoding="utf-8")
            rc, so, se = run(f"/bin/bash {src}", timeout=req.timeout_sec)
    await emit("ok" if rc==0 else "error", f"Runner exit {rc}")
    return {"exitCode": rc, "stdout": so, "stderr": se}
