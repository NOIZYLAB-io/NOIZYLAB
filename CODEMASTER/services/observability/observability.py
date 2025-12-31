#!/usr/bin/env python3
"""
📊 CODEMASTER OBSERVABILITY 📊
==============================
Centralized metrics, logging, and health monitoring.

Features:
- Prometheus metrics endpoint
- Structured JSON logging
- Health aggregation
- Alerting rules
- Dashboard integration

Every service exports metrics!
"""

import os
import time
import json
import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Response
from pydantic import BaseModel

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

SERVICES = {
    "vault":    os.environ.get("VAULT_URL", "http://localhost:8000"),
    "catalog":  os.environ.get("CATALOG_URL", "http://localhost:8001"),
    "evidence": os.environ.get("EVIDENCE_URL", "http://localhost:8002"),
    "ai":       os.environ.get("AI_GATEWAY_URL", "http://localhost:8100"),
    "fleet":    os.environ.get("FLEET_URL", "http://localhost:8200"),
    "mc96":     os.environ.get("MC96_URL", "http://localhost:8300"),
    "mesh":     os.environ.get("MESH_URL", "http://localhost:8400"),
    "portal":   os.environ.get("PORTAL_URL", "http://localhost:8080"),
}

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

# ═══════════════════════════════════════════════════════════════
# 📝 STRUCTURED LOGGING
# ═══════════════════════════════════════════════════════════════

class JSONFormatter(logging.Formatter):
    """JSON log formatter"""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "service": "observability",
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, 'extra'):
            log_data.update(record.extra)
        
        return json.dumps(log_data)


def setup_logging():
    """Setup structured logging"""
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    
    root = logging.getLogger()
    root.handlers = [handler]
    root.setLevel(getattr(logging, LOG_LEVEL))
    
    return logging.getLogger("observability")

logger = setup_logging()


# ═══════════════════════════════════════════════════════════════
# 📊 METRICS COLLECTOR
# ═══════════════════════════════════════════════════════════════

class MetricsCollector:
    """Collects and exposes Prometheus metrics"""
    
    def __init__(self):
        self.metrics: Dict[str, Any] = {}
        self.last_collection = 0
        self.collection_interval = 15  # seconds
    
    def gauge(self, name: str, value: float, labels: Dict[str, str] = None):
        """Set a gauge metric"""
        key = self._metric_key(name, labels)
        self.metrics[key] = {
            "type": "gauge",
            "name": name,
            "value": value,
            "labels": labels or {},
            "timestamp": time.time(),
        }
    
    def counter(self, name: str, value: float, labels: Dict[str, str] = None):
        """Set/increment a counter metric"""
        key = self._metric_key(name, labels)
        if key in self.metrics:
            self.metrics[key]["value"] += value
        else:
            self.metrics[key] = {
                "type": "counter",
                "name": name,
                "value": value,
                "labels": labels or {},
                "timestamp": time.time(),
            }
    
    def histogram(self, name: str, value: float, labels: Dict[str, str] = None):
        """Record a histogram observation"""
        key = self._metric_key(name, labels)
        if key not in self.metrics:
            self.metrics[key] = {
                "type": "histogram",
                "name": name,
                "values": [],
                "labels": labels or {},
            }
        self.metrics[key]["values"].append(value)
        self.metrics[key]["timestamp"] = time.time()
    
    def _metric_key(self, name: str, labels: Dict[str, str] = None) -> str:
        """Generate unique key for metric"""
        if labels:
            label_str = ",".join(f'{k}="{v}"' for k, v in sorted(labels.items()))
            return f"{name}{{{label_str}}}"
        return name
    
    def export_prometheus(self) -> str:
        """Export metrics in Prometheus format"""
        lines = []
        
        for key, metric in self.metrics.items():
            name = metric["name"]
            labels = metric.get("labels", {})
            
            if labels:
                label_str = ",".join(f'{k}="{v}"' for k, v in labels.items())
                metric_name = f"{name}{{{label_str}}}"
            else:
                metric_name = name
            
            if metric["type"] == "histogram":
                # Export histogram buckets
                values = metric.get("values", [])
                if values:
                    lines.append(f"# TYPE {name} histogram")
                    buckets = [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
                    for bucket in buckets:
                        count = sum(1 for v in values if v <= bucket)
                        lines.append(f'{name}_bucket{{le="{bucket}"}} {count}')
                    lines.append(f'{name}_bucket{{le="+Inf"}} {len(values)}')
                    lines.append(f"{name}_sum {sum(values)}")
                    lines.append(f"{name}_count {len(values)}")
            else:
                lines.append(f"# TYPE {name} {metric['type']}")
                lines.append(f"{metric_name} {metric['value']}")
        
        return "\n".join(lines)


collector = MetricsCollector()


# ═══════════════════════════════════════════════════════════════
# 🏥 HEALTH AGGREGATOR
# ═══════════════════════════════════════════════════════════════

class HealthAggregator:
    """Aggregates health from all services"""
    
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=5.0)
        self.last_check: Dict[str, Dict] = {}
    
    async def close(self):
        await self.client.aclose()
    
    async def check_service(self, name: str, url: str) -> Dict:
        """Check health of a single service"""
        start = time.time()
        
        try:
            response = await self.client.get(f"{url}/health")
            latency = time.time() - start
            
            status = "healthy" if response.status_code == 200 else "degraded"
            data = response.json() if response.status_code == 200 else {}
            
            result = {
                "name": name,
                "url": url,
                "status": status,
                "latency_ms": round(latency * 1000, 2),
                "http_status": response.status_code,
                "details": data,
                "checked_at": datetime.utcnow().isoformat() + "Z",
            }
            
            # Update metrics
            collector.gauge("service_up", 1 if status == "healthy" else 0, {"service": name})
            collector.gauge("service_latency_ms", latency * 1000, {"service": name})
            
        except Exception as e:
            latency = time.time() - start
            result = {
                "name": name,
                "url": url,
                "status": "unhealthy",
                "latency_ms": round(latency * 1000, 2),
                "error": str(e),
                "checked_at": datetime.utcnow().isoformat() + "Z",
            }
            
            collector.gauge("service_up", 0, {"service": name})
        
        self.last_check[name] = result
        return result
    
    async def check_all(self) -> Dict:
        """Check health of all services"""
        tasks = [
            self.check_service(name, url)
            for name, url in SERVICES.items()
        ]
        
        results = await asyncio.gather(*tasks)
        
        # Aggregate status
        healthy = sum(1 for r in results if r["status"] == "healthy")
        total = len(results)
        
        overall = "healthy" if healthy == total else "degraded" if healthy > 0 else "unhealthy"
        
        collector.gauge("services_healthy_total", healthy)
        collector.gauge("services_total", total)
        
        return {
            "status": overall,
            "healthy": healthy,
            "total": total,
            "services": {r["name"]: r for r in results},
            "checked_at": datetime.utcnow().isoformat() + "Z",
        }


# ═══════════════════════════════════════════════════════════════
# 📈 STATS COLLECTOR
# ═══════════════════════════════════════════════════════════════

async def collect_service_stats(health: HealthAggregator) -> Dict:
    """Collect detailed stats from services"""
    stats = {}
    
    for name, url in SERVICES.items():
        try:
            response = await health.client.get(f"{url}/stats", timeout=5.0)
            if response.status_code == 200:
                stats[name] = response.json()
                
                # Export key metrics
                for key, value in stats[name].items():
                    if isinstance(value, (int, float)):
                        collector.gauge(f"{name}_{key}", value, {"service": name})
        except:
            stats[name] = {"error": "unavailable"}
    
    return stats


# ═══════════════════════════════════════════════════════════════
# 🚀 FASTAPI APP
# ═══════════════════════════════════════════════════════════════

health_agg: Optional[HealthAggregator] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage health aggregator lifecycle"""
    global health_agg
    health_agg = HealthAggregator()
    
    # Start background health checks
    asyncio.create_task(background_health_check())
    
    yield
    await health_agg.close()


async def background_health_check():
    """Periodic health checks"""
    while True:
        try:
            await health_agg.check_all()
            logger.info("Health check completed", extra={
                "healthy": collector.metrics.get("services_healthy_total", {}).get("value", 0)
            })
        except Exception as e:
            logger.error(f"Health check failed: {e}")
        
        await asyncio.sleep(30)


app = FastAPI(
    title="📊 CODEMASTER Observability",
    version="0.1.0",
    lifespan=lifespan,
)


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES
# ═══════════════════════════════════════════════════════════════

@app.get("/health")
async def health():
    """Observability service health"""
    return {"status": "ok", "service": "observability"}


@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(
        content=collector.export_prometheus(),
        media_type="text/plain"
    )


@app.get("/health/all")
async def health_all():
    """Aggregated health of all services"""
    return await health_agg.check_all()


@app.get("/health/{service}")
async def health_service(service: str):
    """Health of specific service"""
    if service not in SERVICES:
        return {"error": f"Unknown service: {service}"}
    return await health_agg.check_service(service, SERVICES[service])


@app.get("/stats")
async def stats():
    """Aggregated stats from all services"""
    return await collect_service_stats(health_agg)


@app.get("/status")
async def status():
    """Full system status"""
    health = await health_agg.check_all()
    stats = await collect_service_stats(health_agg)
    
    return {
        "health": health,
        "stats": stats,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


# ═══════════════════════════════════════════════════════════════
# 🎯 MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    import uvicorn
    import argparse
    
    parser = argparse.ArgumentParser(description='📊 CODEMASTER Observability')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=9090)
    parser.add_argument('--reload', action='store_true')
    
    args = parser.parse_args()
    
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  📊 CODEMASTER OBSERVABILITY                                  ║
║                                                               ║
║  Port: {args.port:<51} ║
║                                                               ║
║  Endpoints:                                                   ║
║    /metrics     - Prometheus metrics                          ║
║    /health/all  - Aggregated health                           ║
║    /stats       - Service statistics                          ║
║    /status      - Full system status                          ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "observability:app" if args.reload else app,
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
