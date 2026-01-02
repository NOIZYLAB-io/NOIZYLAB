#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cha_cha_bubba_contract.py
--------------------------------
Cha-Cha ⇄ Bubba contract + router
Purpose:
  - Provide the canonical configuration & behavior description that Bubba
    needs to know about Cha-Cha (how to receive commands, how to reply,
    health checking, logging, priorities, retries, addressing other brains).
  - Provide a runnable router that sends commands to worker scripts (subprocess)
    and enforces the contract (timeouts, retries, structured logs).
  - Create a saved JSON contract and a human-readable README in the workspace.

Notes:
  - This script does NOT attempt always-on voice capture; it is the *programmatic*
    contract and router layer between Cha-Cha (frontend) and Bubba/SuperBrain/NoizyBrain.
  - Workers are expected to be local scripts (Python, shell, etc.) found in the WORKSPACE.
"""

from __future__ import annotations
import json
import subprocess
import shutil
import difflib
import sys
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

# ---------------------------
# Workspace paths & helpers
# ---------------------------
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
WORKSPACE.mkdir(parents=True, exist_ok=True)
CONTRACT_FILE = WORKSPACE / "cha_cha_bubba_contract.json"
README_FILE = WORKSPACE / "cha_cha_bubba_README.txt"
LOG_DIR = WORKSPACE / "Saved_Notes"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def now_ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_log(name: str, text: str) -> Path:
    p = LOG_DIR / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    p.write_text(text, encoding="utf-8")
    return p

# ---------------------------
# Contract data structure
# ---------------------------
DEFAULT_CONTRACT = {
    "meta": {
        "created": now_ts(),
        "author": "Cha-Cha (proxy for Rob)",
        "version": "1.0",
        "description": "Contract describing how Cha-Cha routes commands to Bubba and other brains."
    },
    # Workers we know about. Each entry defines how to call the worker and what it supports.
    "workers": {
        "bubba": {
            "type": "script",
            "path": str(WORKSPACE / "bubba_hand_of_god_big_house.py"),
            "cli_prefix": "",           # e.g. if script expects specific subcommand form
            "supported_commands": [
                "audit workspace", "diagnostics", "parallels status",
                "launch parallels", "cleanup desktop", "cleanup big house",
                "project cleanup", "prep appstore"
            ],
            "default_timeout_s": 120,
            "priority": 10
        },
        "super_brain": {
            "type": "script",
            "path": str(WORKSPACE / "super_brain.py"),
            "cli_prefix": "",
            "supported_commands": [
                "draft pitch", "create presentation", "one-liner", "write copy"
            ],
            "default_timeout_s": 30,
            "priority": 5
        },
        "noizy_brain": {
            "type": "script",
            "path": str(WORKSPACE / "noizy_brain.py"),
            "cli_prefix": "",
            "supported_commands": [
                "generate loop", "render track", "music api", "audio convert"
            ],
            "default_timeout_s": 90,
            "priority": 6
        },
        "bucket_switcher": {
            "type": "script",
            "path": str(WORKSPACE / "bucket_switcher.py"),
            "cli_prefix": "",
            "supported_commands": [
                "route", "dispatch"
            ],
            "default_timeout_s": 60,
            "priority": 8
        }
    },
    # routing rules: text match → worker. fuzzy matching is allowed.
    "routing_rules": [
        {"match": ["audit workspace", "audit"], "worker": "bubba"},
        {"match": ["diagnostics", "diagnose"], "worker": "bubba"},
        {"match": ["parallels", "launch parallels", "parallels status"], "worker": "bubba"},
        {"match": ["cleanup desktop", "cleanup big house", "project cleanup"], "worker": "bubba"},
        {"match": ["draft pitch", "one-liner", "presentation"], "worker": "super_brain"},
        {"match": ["generate loop", "render track", "music"], "worker": "noizy_brain"},
        {"match": ["route", "dispatch"], "worker": "bucket_switcher"}
    ],
    # how Cha-Cha expects replies back (standardized wrapper)
    "reply_format": {
        "status": ["ok", "error", "busy", "not_found"],
        "fields": ["worker", "command", "timestamp", "stdout", "stderr", "exit_code"]
    },
    # execution policy
    "policy": {
        "retries": 1,
        "retry_delay_s": 1.5,
        "fuzzy_cutoff": 0.55,
        "log_all_invocations": True
    }
}

# ---------------------------
# Contract management
# ---------------------------
def write_contract(contract: dict = DEFAULT_CONTRACT) -> Path:
    contract["meta"]["modified"] = now_ts()
    CONTRACT_FILE.write_text(json.dumps(contract, indent=2), encoding="utf-8")
    README_FILE.write_text(generate_readme(contract), encoding="utf-8")
    return CONTRACT_FILE

def load_contract() -> dict:
    if not CONTRACT_FILE.exists():
        return DEFAULT_CONTRACT.copy()
    return json.loads(CONTRACT_FILE.read_text(encoding="utf-8"))

def generate_readme(contract: dict) -> str:
    w = contract["workers"]
    lines = [
        "Cha-Cha ⇄ Bubba Contract README",
        "------------------------------",
        f"Generated: {now_ts()}",
        "",
        "Overview:",
        "  This file describes how Cha-Cha will address Bubba and other brains.",
        "",
        "Workers configured:"
    ]
    for k, v in w.items():
        lines.append(f"  - {k}: path={v.get('path')} priority={v.get('priority')} timeout={v.get('default_timeout_s')}s")
        lines.append(f"      supports: {', '.join(v.get('supported_commands', []))}")
    lines += [
        "",
        "Routing rules: (fuzzy matching allowed)",
    ]
    for r in contract["routing_rules"]:
        lines.append(f"  - {r['match']} → {r['worker']}")
    lines += [
        "",
        "Reply format:",
        f"  status ∈ {contract['reply_format']['status']}",
        f"  fields = {contract['reply_format']['fields']}",
        "",
        "Execution policy:",
        f"  retries={contract['policy']['retries']}, retry_delay_s={contract['policy']['retry_delay_s']}, fuzzy_cutoff={contract['policy']['fuzzy_cutoff']}",
        "",
        "How to use the router:",
        "  - Use run_command(text) to dispatch a text command. Router will fuzzy-match rules and call the appropriate worker.",
        "  - Worker scripts are invoked via subprocess and expected to accept a simple CLI argument (text payload).",
        "",
        "Logging:",
        f"  All invocations are logged into {LOG_DIR}",
        "",
        "If you need to add a worker: edit the contract JSON or call write_contract() to overwrite.",
    ]
    return "\n".join(lines)

# ---------------------------
# Router & execution
# ---------------------------
class ChaChaRouter:
    def __init__(self, contract: Optional[dict] = None):
        self.contract = contract or load_contract()
        self.workers = self.contract["workers"]
        self.rules = self.contract["routing_rules"]
        self.policy = self.contract["policy"]

    def fuzzy_match_rule(self, text: str) -> Optional[str]:
        """
        Attempt to match incoming command text to a worker via rules.
        returns worker name or None.
        """
        text_l = text.lower()
        candidates = []
        for rule in self.rules:
            for pattern in rule["match"]:
                # exact containment first
                if pattern in text_l:
                    return rule["worker"]
                # store fuzzy candidates
                candidates.append((pattern, rule["worker"]))
        # fallback fuzzy matching across patterns
        patterns = [p for p, _ in candidates]
        if not patterns:
            return None
        best = difflib.get_close_matches(text_l, patterns, n=1, cutoff=self.policy.get("fuzzy_cutoff", 0.55))
        if best:
            # find worker
            for p, w in candidates:
                if p == best[0]:
                    return w
        return None

    def _call_worker_script(self, worker_name: str, payload: str, timeout_s: Optional[int] = None) -> dict:
        """
        Call a worker script, capture stdout/stderr, and return a standardized reply dict.
        Worker scripts are expected to exist at configured path.
        """
        worker = self.workers.get(worker_name)
        if not worker:
            return self._reply("not_found", worker_name, payload, stdout="", stderr=f"Worker {worker_name} not configured", exit_code=-1)

        path = Path(worker["path"])
        if not path.exists():
            return self._reply("not_found", worker_name, payload, stdout="", stderr=f"Script {path} missing", exit_code=-2)

        cmd = []
        # if worker defines an interpreter or prefix, respect it. Default: python3 script payload
        if path.suffix == ".py":
            cmd = ["python3", str(path), payload]
        else:
            # attempt direct invocation
            cmd = [str(path), payload]

        t = timeout_s or worker.get("default_timeout_s", 60)
        attempt = 0
        last_err = None
        while attempt <= self.policy.get("retries", 1):
            attempt += 1
            try:
                proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=t)
                stdout = proc.stdout.strip()
                stderr = proc.stderr.strip()
                exit_code = proc.returncode
                status = "ok" if exit_code == 0 else "error"
                reply = self._reply(status, worker_name, payload, stdout=stdout, stderr=stderr, exit_code=exit_code)
                if self.policy.get("log_all_invocations", True):
                    save_log("invocation", json.dumps(reply, indent=2))
                return reply
            except subprocess.TimeoutExpired as e:
                last_err = str(e)
                time.sleep(self.policy.get("retry_delay_s", 1.5))
        # exhausted retries
        return self._reply("busy", worker_name, payload, stdout="", stderr=f"Timeout after retries: {last_err}", exit_code=-3)

    def _reply(self, status: str, worker: str, command: str, stdout: str = "", stderr: str = "", exit_code: int = 0) -> dict:
        return {
            "status": status,
            "worker": worker,
            "command": command,
            "timestamp": now_ts(),
            "stdout": stdout,
            "stderr": stderr,
            "exit_code": exit_code
        }

    def run_command(self, text: str) -> dict:
        """
        Top-level routing:
         1. Find worker via rules (fuzzy)
         2. If none found, try fallback to bucket_switcher if present.
         3. Call worker and return standardized reply.
        """
        text = text.strip()
        if not text:
            return self._reply("error", "router", text, stderr="Empty command", exit_code=-1)

        # allow chained commands separated by 'and', 'then', commas
        parts = []
        tmp = text.replace(" then ", " and ")
        for chunk in tmp.split(" and "):
            for p in chunk.split(","):
                s = p.strip()
                if s:
                    parts.append(s)

        overall_results = {"parts": []}
        for p in parts:
            worker = self.fuzzy_match_rule(p)
            if not worker:
                # fallback to bucket_switcher if available
                if "bucket_switcher" in self.workers:
                    worker = "bucket_switcher"
                else:
                    overall_results["parts"].append(self._reply("not_found", "router", p, stderr="No routing rule or bucket_switcher", exit_code=-4))
                    continue
            result = self._call_worker_script(worker, p)
            overall_results["parts"].append(result)

            # quick health ping after each part (lightweight)
            health = self.quick_health_summary()
            overall_results.setdefault("health", []).append(health)
        overall_results["timestamp"] = now_ts()
        if self.policy.get("log_all_invocations", True):
            save_log("router_call", json.dumps(overall_results, indent=2))
        return overall_results

    def quick_health_summary(self) -> Dict[str, Any]:
        # lightweight checks: disk free %, parallels running?
        try:
            df = shutil.disk_usage("/")
            free_gb = round(df.free / (1024**3), 1)
        except Exception:
            free_gb = None
        parallels_running = bool(shutil.which("prlctl")) and bool(subprocess.run(["pgrep", "-fl", "Parallels"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.strip())
        return {"free_gb": free_gb, "parallels_running": bool(parallels_running), "ts": now_ts()}

# ---------------------------
# Utility CLI
# ---------------------------
def cli_dump_contract():
    contract = load_contract()
    print(json.dumps(contract, indent=2))
    return contract

def cli_send_command(cmd: str):
    router = ChaChaRouter()
    result = router.run_command(cmd)
    # print a readable summary
    print("=== Cha-Cha Router Result ===")
    print(json.dumps(result, indent=2))
    return result

def cli_write_default_contract():
    p = write_contract(DEFAULT_CONTRACT)
    print(f"Wrote contract to: {p}")
    print(f"README written to: {README_FILE}")
    return p

# ---------------------------
# When run as a script
# ---------------------------
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Cha-Cha ⇄ Bubba contract & router helper")
    ap.add_argument("--init", action="store_true", help="Write default contract + README to workspace")
    ap.add_argument("--dump", action="store_true", help="Print contract JSON")
    ap.add_argument("--send", type=str, help="Send a one-shot command string to the router (quotes)")
    ap.add_argument("--worker-test", nargs=2, metavar=("WORKER","PAYLOAD"), help="Call worker directly for test")
    args = ap.parse_args()

    if args.init:
        cli_write_default_contract()
        sys.exit(0)
    if args.dump:
        cli_dump_contract()
        sys.exit(0)
    if args.worker_test:
        worker, payload = args.worker_test
        c = load_contract()
        router = ChaChaRouter(c)
        if worker not in c["workers"]:
            print(f"Unknown worker: {worker}")
            sys.exit(2)
        print(json.dumps(router._call_worker_script(worker, payload), indent=2))
        sys.exit(0)
    if args.send:
        cli_send_command(args.send)
        sys.exit(0)

    # interactive help summary
    print("Cha-Cha ⇄ Bubba Contract Tool")
    print("Examples:")
    print("  Initialize default contract + README:")
    print(f"    {sys.argv[0]} --init")
    print("  Dump contract JSON:")
    print(f"    {sys.argv[0]} --dump")
    print('  Send command to router:')
    print(f"    {sys.argv[0]} --send \"cleanup desktop and launch parallels\"")
    print("  Test worker directly:")
    print(f"    {sys.argv[0]} --worker-test bubba \"audit workspace\"")
    print("")
