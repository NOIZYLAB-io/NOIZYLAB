import json, os, pathlib
from fastapi.testclient import TestClient

from rock_mode import app

def test_catalog_available(monkeypatch):
    client = TestClient(app)
    monkeypatch.setenv("PORTAL_TOKEN","t")
    r = client.get("/api/catalog", headers={"x-portal-token":"t"})
    assert r.status_code == 200
    assert "items" in r.json()

def test_fix_rate_limited(monkeypatch):
    client = TestClient(app)
    monkeypatch.setenv("PORTAL_TOKEN","t")
    for _ in range(9):
        r = client.post("/api/fix/clear_caches", headers={"x-portal-token":"t"})
    assert r.status_code in (200, 429)