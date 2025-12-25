# NOIZYLAB Performance Improvements

> Last Updated: 2025-12-25  
> Status: Analysis Complete - Recommendations Provided

This document identifies slow or inefficient code patterns found in the NOIZYLAB repository and provides concrete suggestions for improvement.

---

## Table of Contents

1. [Critical Performance Issues](#critical-performance-issues)
2. [JavaScript Frontend Optimizations](#javascript-frontend-optimizations)
3. [Python Backend Optimizations](#python-backend-optimizations)
4. [Shell Script Optimizations](#shell-script-optimizations)
5. [Summary of Recommendations](#summary-of-recommendations)

---

## Critical Performance Issues

### 1. O(n²) Particle Connection Algorithm

**File:** `gabriel/mission_control_portal/app.js`  
**Lines:** 100-113  
**Severity:** High (CPU-intensive on every animation frame)

#### Current Code:
```javascript
// Draw connections between nearby particles
ctx.strokeStyle = 'rgba(0, 255, 65, 0.1)';
ctx.lineWidth = 1;
for (let i = 0; i < this.particles.length; i++) {
    for (let j = i + 1; j < this.particles.length; j++) {
        const dx = this.particles[j].x - this.particles[i].x;
        const dy = this.particles[j].y - this.particles[i].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 100) {
            ctx.beginPath();
            ctx.moveTo(this.particles[i].x, this.particles[i].y);
            ctx.lineTo(this.particles[j].x, this.particles[j].y);
            ctx.stroke();
        }
    }
}
```

#### Problem:
- With 100 particles, this results in **4,950 distance calculations per frame** (100 × 99 / 2)
- At 60 FPS, this equals **~297,000 calculations per second**
- `Math.sqrt()` is called for every pair, even when unnecessary

#### Recommended Fix:
```javascript
// OPTIMIZATION 1: Use squared distance to avoid sqrt
const DISTANCE_THRESHOLD_SQUARED = 100 * 100; // 10000

// OPTIMIZATION 2: Batch path operations
ctx.strokeStyle = 'rgba(0, 255, 65, 0.1)';
ctx.lineWidth = 1;
ctx.beginPath(); // Single beginPath for all lines

for (let i = 0; i < this.particles.length; i++) {
    const p1 = this.particles[i];
    for (let j = i + 1; j < this.particles.length; j++) {
        const p2 = this.particles[j];
        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;
        const distSquared = dx * dx + dy * dy;

        if (distSquared < DISTANCE_THRESHOLD_SQUARED) {
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
        }
    }
}

ctx.stroke(); // Single stroke call for all lines
```

**Expected Improvement:** 30-50% reduction in animation frame time

---

### 2. Repeated Linear Search in Edge Rendering

**File:** `gabriel/mission_control_portal/neural_engine.js`  
**Lines:** 167-184 and 210-213  
**Severity:** High (O(n) lookups on every frame)

#### Current Code:
```javascript
// Edge attraction (updatePhysics)
for (const edge of this.edges) {
    const from = this.nodes.find(n => n.id === edge.from);
    const to = this.nodes.find(n => n.id === edge.to);
    if (!from || !to) continue;
    // ...
}

// Render edges
for (const edge of this.edges) {
    const from = this.nodes.find(n => n.id === edge.from);
    const to = this.nodes.find(n => n.id === edge.to);
    // ...
}
```

#### Problem:
- `Array.find()` is called twice per edge in `updatePhysics()` + twice per edge in `render()`
- For E edges and N nodes, this is O(E × N) per frame
- With 13 edges and 11 nodes, that's 572 iterations per frame at 60 FPS = 34,320/sec

#### Recommended Fix:
```javascript
// Add a node lookup map (call once when data changes)
setData(nodes, edges) {
    this.nodes = nodes.map((n, i) => ({
        ...n,
        x: this.centerX + (Math.random() - 0.5) * 200,
        y: this.centerY + (Math.random() - 0.5) * 200,
        vx: 0,
        vy: 0,
        radius: n.type === 'core' ? 35 : 25
    }));

    // Create lookup map for O(1) access
    this.nodeMap = new Map(this.nodes.map(n => [n.id, n]));

    this.edges = edges.map(e => ({
        ...e,
        pulse: Math.random() * Math.PI * 2
    }));
}

// Use in updatePhysics and render
for (const edge of this.edges) {
    const from = this.nodeMap.get(edge.from);
    const to = this.nodeMap.get(edge.to);
    if (!from || !to) continue;
    // ...
}
```

**Expected Improvement:** O(1) lookups instead of O(n), 80%+ reduction in lookup time

---

### 3. Repeated DOM Queries in Status Updates

**File:** `gabriel/mission_control_portal/app.js`  
**Lines:** 221-239  
**Severity:** Medium (called every 5 seconds, but still wasteful)

#### Current Code:
```javascript
updateMetrics(status) {
    const latencyEl = document.getElementById('latency-value');
    const agentsEl = document.getElementById('agents-value');
    const memcellEl = document.getElementById('memcell-value');
    const uptimeEl = document.getElementById('uptime-value');
    // ...
}
```

#### Problem:
- DOM queries are performed every time `updateMetrics()` is called
- Although not critical at 5-second intervals, it's a wasteful pattern

#### Recommended Fix:
```javascript
constructor() {
    // ... existing code ...
    
    // Cache DOM elements on initialization
    this.elements = {
        latency: null,
        agents: null,
        memcell: null,
        uptime: null,
        statusBadge: null
    };
}

async init() {
    // ... existing code ...
    
    // Cache elements after DOM is ready
    this.elements.latency = document.getElementById('latency-value');
    this.elements.agents = document.getElementById('agents-value');
    this.elements.memcell = document.getElementById('memcell-value');
    this.elements.uptime = document.getElementById('uptime-value');
    this.elements.statusBadge = document.getElementById('system-status');
}

updateMetrics(status) {
    if (this.elements.latency) this.elements.latency.textContent = status.latency || '<7ms';
    if (this.elements.agents) this.elements.agents.textContent = status.agents_active || '3';
    // ... etc
}
```

**Expected Improvement:** Eliminates 4+ DOM queries per update cycle

---

## JavaScript Frontend Optimizations

### 4. Canvas Context State Changes

**File:** `gabriel/mission_control_portal/neural_engine.js`  
**Lines:** 205-284  
**Severity:** Medium

#### Current Code:
The `render()` method changes canvas context state (strokeStyle, fillStyle, lineWidth, font) multiple times per frame.

#### Recommended Fix:
- Group similar drawing operations together
- Use `ctx.save()` and `ctx.restore()` strategically
- Batch similar stroke/fill operations

```javascript
render() {
    const ctx = this.ctx;
    ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw ALL edges first with same style
    ctx.strokeStyle = this.colors.edge;
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (const edge of this.edges) {
        const from = this.nodeMap.get(edge.from);
        const to = this.nodeMap.get(edge.to);
        if (!from || !to) continue;
        ctx.moveTo(from.x, from.y);
        ctx.lineTo(to.x, to.y);
    }
    ctx.stroke();

    // Draw all pulses with same style
    ctx.fillStyle = this.colors.core;
    ctx.beginPath();
    for (const edge of this.edges) {
        // ... pulse drawing
    }
    ctx.fill();

    // ... group other operations similarly
}
```

---

### 5. Unnecessary Object Spread in setData

**File:** `gabriel/mission_control_portal/neural_engine.js`  
**Lines:** 106-121

#### Current Code:
```javascript
this.nodes = nodes.map((n, i) => ({
    ...n,
    x: this.centerX + (Math.random() - 0.5) * 200,
    // ...
}));
```

#### Problem:
Object spread creates new objects but shallow-copies properties that may not be needed.

#### Recommendation:
This is acceptable for small datasets, but for larger graphs, consider:
```javascript
this.nodes = nodes.map(n => {
    n.x = this.centerX + (Math.random() - 0.5) * 200;
    n.y = this.centerY + (Math.random() - 0.5) * 200;
    n.vx = 0;
    n.vy = 0;
    n.radius = n.type === 'core' ? 35 : 25;
    return n;
});
```

---

## Python Backend Optimizations

### 6. File I/O Without Caching

**File:** `gabriel/mc96_server.py`  
**Lines:** 86-95  
**Severity:** Low (only affects `/api/memcell/graph` endpoint)

#### Current Code:
```python
@app.route('/api/memcell/graph')
def get_memcell_graph():
    data_path = os.path.join(os.path.dirname(__file__), 'memcell_data', 'brain.json')
    
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            return jsonify(json.load(f))
```

#### Problem:
- File is read from disk on every request
- For static or rarely-changing data, this is wasteful

#### Recommended Fix:
```python
import functools
from datetime import datetime, timedelta

# Cache with time-based expiration
_graph_cache = {'data': None, 'loaded_at': None, 'ttl': timedelta(minutes=5)}

def get_cached_graph():
    now = datetime.now()
    if (_graph_cache['data'] is None or 
        _graph_cache['loaded_at'] is None or 
        now - _graph_cache['loaded_at'] > _graph_cache['ttl']):
        
        data_path = os.path.join(os.path.dirname(__file__), 'memcell_data', 'brain.json')
        if os.path.exists(data_path):
            with open(data_path, 'r') as f:
                _graph_cache['data'] = json.load(f)
                _graph_cache['loaded_at'] = now
    
    return _graph_cache['data']

@app.route('/api/memcell/graph')
def get_memcell_graph():
    cached = get_cached_graph()
    if cached:
        return jsonify(cached)
    # Return default...
```

---

### 7. Canvas Redraw on Every Frame (Tkinter)

**File:** `gabriel/tools/gabriel_control.py`  
**Lines:** 149-179  
**Severity:** Medium (affects desktop GUI performance)

#### Current Code:
```python
def animate_loop(self):
    # ...
    self.canvas.delete("all")  # Clears entire canvas
    # ... redraws everything
```

#### Problem:
- `canvas.delete("all")` and full redraw is expensive
- For static elements that don't change, this is wasteful

#### Recommended Fix:
Use canvas item tags and only update what changes:

```python
def setup_ui(self):
    # ... existing code ...
    
    # Pre-create canvas items with tags
    self.bar_items = []
    self.line_item = None

def animate_loop(self):
    # Instead of delete("all"), update existing items
    w = self.canvas.winfo_width()
    h = self.canvas.winfo_height()
    
    # Update frequency bars (create once, move after)
    bar_w = 15
    bar_count = w // (bar_w + 2)
    
    # Ensure we have enough bar items
    while len(self.bar_items) < bar_count:
        item = self.canvas.create_rectangle(0, 0, 0, 0, fill=Gabriel_Theme["dim"], outline="")
        self.bar_items.append(item)
    
    # Update positions
    for i, item in enumerate(self.bar_items[:bar_count]):
        x = i * (bar_w + 2)
        val = (math.sin(x * 0.05 + self.anim_frame * 0.15) + 1) * 0.5
        bar_h = val * (h * 0.4)
        color = Gabriel_Theme["fg"] if bar_h > h * 0.3 else Gabriel_Theme["dim"]
        
        self.canvas.coords(item, x, h, x + bar_w, h - bar_h)
        self.canvas.itemconfig(item, fill=color)
```

---

### 8. Subprocess Blocking on Voice Commands

**File:** `gabriel/tools/gabriel_control.py`  
**Line:** 58  
**Severity:** Low (already using threading, but worth noting)

#### Current Code:
```python
subprocess.run(["say", "-v", "Alex", "-r", "180", text])
```

#### Observation:
The code already handles this with a queue-based worker thread, which is good practice. No changes needed.

---

## Shell Script Optimizations

### 9. Multiple rsync Calls in Media Sync

**File:** `AGENTS/sync-media.sh`  
**Lines:** 17-24

#### Current Code:
```bash
rsync -avh --progress --include='*.wav' --include='*.mp3' ...
rsync -avh --progress --include='*.mov' --include='*.mp4' ...
```

#### Problem:
Two separate rsync invocations scan the entire source directory twice.

#### Recommended Fix:
Use a single rsync with combined filters:

```bash
push)
    echo "📤 Pushing media to Google Drive..."
    rsync -avh --progress \
        --include='*.wav' --include='*.mp3' --include='*.flac' \
        --include='*.aif' --include='*.aiff' --include='*.m4a' --include='*.ogg' \
        --include='*.mov' --include='*.mp4' --include='*.avi' \
        --include='*.mkv' --include='*.webm' \
        --include='*/' --exclude='*' \
        "$NOIZYLAB/" "$GDRIVE/"
    echo "✅ Media pushed to Google Drive"
    ;;
```

Or use `--files-from` with a manifest for even better control.

---

## Summary of Recommendations

| Priority | File | Issue | Est. Impact |
|----------|------|-------|-------------|
| **HIGH** | app.js | O(n²) particle connections | 30-50% frame time |
| **HIGH** | neural_engine.js | Linear search for nodes | 80%+ lookup time |
| **MEDIUM** | app.js | DOM query caching | Minor per-cycle |
| **MEDIUM** | neural_engine.js | Canvas state batching | 15-25% render time |
| **MEDIUM** | gabriel_control.py | Canvas item reuse | 20-40% redraw time |
| **LOW** | mc96_server.py | File I/O caching | Minimal |
| **LOW** | sync-media.sh | Single rsync pass | ~2x scan time |

---

## Implementation Priority

1. **Immediate (High Impact, Low Effort):**
   - Add node lookup Map in neural_engine.js
   - Use squared distance comparison in app.js

2. **Short-term (Medium Impact, Medium Effort):**
   - Batch canvas operations in neural_engine.js
   - Cache DOM elements in app.js

3. **When Time Permits (Low Impact):**
   - Add file caching to mc96_server.py
   - Optimize rsync in sync-media.sh
   - Refactor Tkinter canvas for item reuse

---

*Generated by performance analysis tool - NOIZYLAB 2025*
