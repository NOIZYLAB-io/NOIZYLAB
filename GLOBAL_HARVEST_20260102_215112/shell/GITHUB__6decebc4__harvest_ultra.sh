#!/usr/bin/env bash
set -euo pipefail

LIST_FILE="${1:-repos.txt}"
[[ -f "$LIST_FILE" ]] || { echo "Usage: ./harvest_ultra.sh repos.txt"; exit 1; }

# ====== KNOBS ======
PARALLEL="${PARALLEL:-6}"
FULL_HISTORY="${FULL_HISTORY:-1}"         # 1 full, 0 shallow
SHALLOW_DEPTH="${SHALLOW_DEPTH:-100}"
ALL_BRANCHES="${ALL_BRANCHES:-1}"
WITH_SUBMODULES="${WITH_SUBMODULES:-1}"
WITH_LFS="${WITH_LFS:-1}"
WITH_CTAGS="${WITH_CTAGS:-1}"
WITH_GITLEAKS="${WITH_GITLEAKS:-0}"       # 1 if you have gitleaks installed
RETRIES="${RETRIES:-2}"
MAX_FILE_MB="${MAX_FILE_MB:-2}"
CHUNK_MB="${CHUNK_MB:-25}"
# ===================

has(){ command -v "$1" >/dev/null 2>&1; }

DEFAULT_ROOT="/Volumes/GABRIEL"
OUT_ROOT="$DEFAULT_ROOT/HarvestedCode"
[[ -d "$DEFAULT_ROOT" ]] || OUT_ROOT="$(pwd)/HarvestedCode"

TS="$(date +%Y%m%d_%H%M%S)"
RUN_DIR="$OUT_ROOT/RUN_ULTRA_${TS}"
CACHE_DIR="$OUT_ROOT/_cache_mirrors"
LOG_DIR="$RUN_DIR/_logs"
mkdir -p "$RUN_DIR" "$CACHE_DIR" "$LOG_DIR"

EXCLUDES_REGEX='(^|/)(\.git|node_modules|dist|build|\.next|\.cache|coverage|venv|\.venv|__pycache__|\.idea|\.vscode|target|.terraform)(/|$)'

echo "Run: $RUN_DIR"
echo "Cache: $CACHE_DIR"
echo "Parallel=$PARALLEL FullHistory=$FULL_HISTORY Submodules=$WITH_SUBMODULES LFS=$WITH_LFS CTAGS=$WITH_CTAGS"

clone_with_cache() {
  local url="$1" dest="$2" name="$3"
  local mirror="$CACHE_DIR/${name}.git"

  if [[ -d "$mirror" ]]; then
    (cd "$mirror" && git remote set-url origin "$url" && git fetch --all --tags --prune >/dev/null 2>&1) || true
  else
    git clone --mirror "$url" "$mirror" >/dev/null 2>&1 || return 1
  fi

  # clone from mirror (fast)
  if [[ "$FULL_HISTORY" == "1" ]]; then
    git clone "$mirror" "$dest" >/dev/null
  else
    git clone --depth "$SHALLOW_DEPTH" "$mirror" "$dest" >/dev/null
  fi
}

process_repo() {
  local url="$1"
  [[ -z "${url// }" ]] && return 0
  [[ "$url" =~ ^# ]] && return 0

  local name base repo_dir out_dir log_file done_flag
  name="$(basename -s .git "$url")"
  base="$RUN_DIR/$name"
  repo_dir="$base/repo"
  out_dir="$base/out"
  log_file="$LOG_DIR/${name}.log"
  done_flag="$out_dir/.DONE"

  mkdir -p "$out_dir"

  if [[ -f "$done_flag" ]]; then
    echo "==> [$name] skip (done)"
    return 0
  fi

  {
    echo "==> [$name] start"
    rm -rf "$repo_dir" || true

    local attempt=0
    until (( attempt > RETRIES )); do
      if clone_with_cache "$url" "$repo_dir" "$name"; then
        break
      fi
      attempt=$((attempt+1))
      echo "retry $attempt/$RETRIES"
      sleep 1
    done

    cd "$repo_dir"

    [[ "$ALL_BRANCHES" == "1" ]] && (git fetch --all --tags --prune >/dev/null 2>&1 || true)

    [[ "$WITH_SUBMODULES" == "1" ]] && (git submodule update --init --recursive >/dev/null 2>&1 || true)

    if [[ "$WITH_LFS" == "1" ]] && git lfs version >/dev/null 2>&1; then
      git lfs pull >/dev/null 2>&1 || true
    fi

    {
      echo "repo_url=$url"
      echo "default_branch=$(git symbolic-ref --quiet --short HEAD 2>/dev/null || echo unknown)"
      echo "head_commit=$(git rev-parse HEAD 2>/dev/null || echo unknown)"
      echo "head_date=$(git show -s --format=%ci HEAD 2>/dev/null || echo unknown)"
    } > "$out_dir/meta.txt"

    git log --oneline -n 5000 > "$out_dir/git_log_oneline.txt" 2>/dev/null || true
    git shortlog -sn > "$out_dir/git_shortlog.txt" 2>/dev/null || true

    # CTAGS symbols (jump-to-definition across the repo)
    if [[ "$WITH_CTAGS" == "1" ]] && has ctags; then
      ctags -R --languages=+JavaScript,TypeScript,Python,Go,Rust,C,C++,C#,Java \
        --exclude=.git --exclude=node_modules --exclude=dist --exclude=build \
        -f "$out_dir/tags" . >/dev/null 2>&1 || true
    fi

    # Optional secrets scan
    if [[ "$WITH_GITLEAKS" == "1" ]] && has gitleaks; then
      gitleaks detect --source . --no-git --redact --report-format json \
        --report-path "$out_dir/gitleaks.json" >/dev/null 2>&1 || true
    fi

    # Tree
    find . -type d -print | grep -Ev "$EXCLUDES_REGEX" > "$out_dir/tree.txt"

    # Inventory + duplicates + chunked all_code + per-repo FTS
    python3 - <<'PY' "$repo_dir" "$out_dir" "$EXCLUDES_REGEX" "$MAX_FILE_MB" "$CHUNK_MB"
import os, sys, csv, re, hashlib, json, sqlite3
root, out_dir = sys.argv[1], sys.argv[2]
ex_re = re.compile(sys.argv[3])
max_file_bytes = int(float(sys.argv[4]) * 1024 * 1024)
chunk_target = int(float(sys.argv[5]) * 1024 * 1024)

skip_ext = {
  ".png",".jpg",".jpeg",".gif",".webp",".ico",".pdf",".zip",".7z",".dmg",".exe",".dll",".so",".dylib",
  ".mp3",".wav",".aiff",".mp4",".mov",".m4v",".ttf",".otf",".woff",".woff2",".psd",".ai",".sketch"
}

def sha256(path: str) -> str:
  h=hashlib.sha256()
  with open(path,"rb") as f:
    for chunk in iter(lambda: f.read(1024*1024), b""):
      h.update(chunk)
  return h.hexdigest()

def is_texty(path: str) -> bool:
  ext=os.path.splitext(path)[1].lower()
  if ext in skip_ext: return False
  try:
    with open(path,"rb") as f:
      b=f.read(4096)
    return b.find(b"\x00")==-1
  except: return False

rows=[]
hash_map={}
ext_counts={}
text_files=[]

for dirpath, dirnames, filenames in os.walk(root):
  rel_dir=os.path.relpath(dirpath, root)
  if rel_dir=="." : rel_dir=""
  if ex_re.search(rel_dir):
    dirnames[:] = []
    continue
  dirnames[:] = [d for d in dirnames if not ex_re.search(os.path.join(rel_dir,d))]
  for fn in filenames:
    p=os.path.join(dirpath, fn)
    rel=os.path.relpath(p, root)
    if ex_re.search(rel): continue
    try: sz=os.path.getsize(p)
    except: continue
    ext=os.path.splitext(fn)[1].lower()
    ext_counts[ext]=ext_counts.get(ext,0)+1
    h=""
    try:
      if sz <= 50*1024*1024:
        h=sha256(p)
        hash_map.setdefault(h,[]).append(rel)
    except: pass
    rows.append((rel,sz,ext,h))
    if sz<=max_file_bytes and is_texty(p):
      text_files.append((rel,sz,ext))

rows.sort(key=lambda x:x[0])

# inventory
with open(os.path.join(out_dir,"inventory.csv"),"w",newline="",encoding="utf-8") as f:
  w=csv.writer(f); w.writerow(["path","bytes","ext","sha256"]); w.writerows(rows)

# duplicates
dupes=[(h,paths) for h,paths in hash_map.items() if h and len(paths)>1]
dupes.sort(key=lambda x:(-len(x[1]),x[0]))
with open(os.path.join(out_dir,"duplicates.csv"),"w",newline="",encoding="utf-8") as f:
  w=csv.writer(f); w.writerow(["sha256","count","paths"])
  for h,paths in dupes:
    w.writerow([h,len(paths)," | ".join(sorted(paths))])

# chunked all_code
chunks_dir=os.path.join(out_dir,"all_code_chunks")
os.makedirs(chunks_dir, exist_ok=True)
chunk_i=1; chunk_bytes=0
out_path=os.path.join(chunks_dir, f"all_code_{chunk_i:03d}.txt")
out=open(out_path,"w",encoding="utf-8",errors="replace")

def rotate():
  global chunk_i, chunk_bytes, out, out_path
  out.close()
  chunk_i += 1
  chunk_bytes = 0
  out_path=os.path.join(chunks_dir, f"all_code_{chunk_i:03d}.txt")
  out=open(out_path,"w",encoding="utf-8",errors="replace")

for rel,sz,ext in sorted(text_files, key=lambda x:x[0]):
  p=os.path.join(root, rel)
  if chunk_bytes + sz > chunk_target and chunk_bytes>0:
    rotate()
  out.write(f"\n\n===== FILE: {rel} ({sz} bytes) =====\n")
  try:
    with open(p,"r",encoding="utf-8",errors="replace") as f:
      s=f.read()
    out.write(s)
    chunk_bytes += len(s.encode("utf-8", errors="ignore"))
  except: pass
out.close()

# SQLite FTS (deep search)
fts_db=os.path.join(out_dir,"search_fts.sqlite")
con=sqlite3.connect(fts_db); cur=con.cursor()
cur.execute("PRAGMA journal_mode=WAL;")
cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS files USING fts5(path, content);")
cur.execute("DELETE FROM files;")
for rel,sz,ext in sorted(text_files, key=lambda x:x[0]):
  p=os.path.join(root, rel)
  try:
    with open(p,"r",encoding="utf-8",errors="replace") as f:
      content=f.read()
    cur.execute("INSERT INTO files(path, content) VALUES (?,?);",(rel,content))
  except: continue
con.commit(); con.close()

stats={
  "files_total": len(rows),
  "text_files_indexed": len(text_files),
  "duplicates_groups": len(dupes),
  "chunks": chunk_i,
  "max_concat_file_bytes": max_file_bytes,
  "chunk_target_bytes": chunk_target,
  "ext_counts": dict(sorted(ext_counts.items(), key=lambda kv:(-kv[1],kv[0]))),
}
with open(os.path.join(out_dir,"stats.json"),"w",encoding="utf-8") as f:
  json.dump(stats,f,indent=2)
PY

    (cd "$base" && zip -qr "${name}.zip" . >/dev/null) || true
    touch "$done_flag"
    echo "==> [$name] done"
  } >"$log_file" 2>&1
}

export -f process_repo clone_with_cache has
export RUN_DIR CACHE_DIR LOG_DIR FULL_HISTORY SHALLOW_DEPTH ALL_BRANCHES WITH_SUBMODULES WITH_LFS WITH_CTAGS WITH_GITLEAKS RETRIES MAX_FILE_MB CHUNK_MB EXCLUDES_REGEX

mapfile -t REPOS < <(grep -Ev '^\s*$|^\s*#' "$LIST_FILE" | sed 's/\r$//')

pids=()
for url in "${REPOS[@]}"; do
  process_repo "$url" &
  pids+=("$!")
  while (( ${#pids[@]} >= PARALLEL )); do
    wait -n
    alive=()
    for pid in "${pids[@]}"; do kill -0 "$pid" 2>/dev/null && alive+=("$pid"); done
    pids=("${alive[@]}")
  done
done
wait

python3 - <<'PY' "$RUN_DIR"
import os, json, sys
run_dir=sys.argv[1]
index=[]
for repo in sorted(os.listdir(run_dir)):
  p=os.path.join(run_dir,repo,"out","stats.json")
  m=os.path.join(run_dir,repo,"out","meta.txt")
  if os.path.isfile(p):
    s=json.load(open(p,"r",encoding="utf-8"))
    meta={}
    if os.path.isfile(m):
      for line in open(m,"r",encoding="utf-8"):
        if "=" in line:
          k,v=line.strip().split("=",1); meta[k]=v
    index.append({"repo":repo, **meta, **s})
json.dump(index, open(os.path.join(run_dir,"MASTER_INDEX.json"),"w",encoding="utf-8"), indent=2)
PY

(cd "$RUN_DIR" && zip -qr "RUN_ULTRA_MASTER.zip" . >/dev/null)
echo "Done: $RUN_DIR"
