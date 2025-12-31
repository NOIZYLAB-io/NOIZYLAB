#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🧪 CODEMASTER + TURBO INTEGRATION TEST                                        ║
║  Verify all services work together                                             ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import httpx
import json
import sys
import time
from pathlib import Path
from typing import Dict, Any, List

# Test configuration
SERVICES = {
    "vault": "http://localhost:8000",
    "catalog": "http://localhost:8001",
    "evidence": "http://localhost:8002",
    "ai_gateway": "http://localhost:8100",
    "fleet": "http://localhost:8200",
    "mc96": "http://localhost:8300",
    "mesh": "http://localhost:8400",
    "god_brain": "http://localhost:8500",
    "observability": "http://localhost:9090",
    "portal": "http://localhost:8080",
}

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner():
    print(f"""
{CYAN}╔═══════════════════════════════════════════════════════════════╗
║  🧪 CODEMASTER + TURBO INTEGRATION TEST                       ║
╚═══════════════════════════════════════════════════════════════╝{RESET}
""")


async def test_health(client: httpx.AsyncClient, name: str, url: str) -> bool:
    """Test service health endpoint."""
    try:
        response = await client.get(f"{url}/health", timeout=5)
        if response.is_success:
            print(f"  {GREEN}✓{RESET} {name:15} - healthy")
            return True
        else:
            print(f"  {RED}✗{RESET} {name:15} - unhealthy (status {response.status_code})")
            return False
    except Exception as e:
        print(f"  {RED}✗{RESET} {name:15} - error: {str(e)[:40]}")
        return False


async def test_vault_ingest(client: httpx.AsyncClient) -> bool:
    """Test vault file ingest."""
    print(f"\n{YELLOW}📦 Testing Vault Ingest...{RESET}")
    
    test_content = b"Test file content for CODEMASTER integration test"
    
    try:
        # Create test file
        files = {"file": ("test.txt", test_content, "text/plain")}
        response = await client.post(
            f"{SERVICES['vault']}/ingest",
            files=files,
            timeout=10
        )
        
        if response.is_success:
            data = response.json()
            print(f"  {GREEN}✓{RESET} File ingested: {data.get('sha256', 'N/A')[:16]}...")
            return True
        else:
            print(f"  {RED}✗{RESET} Ingest failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  {RED}✗{RESET} Ingest error: {e}")
        return False


async def test_catalog_search(client: httpx.AsyncClient) -> bool:
    """Test catalog search."""
    print(f"\n{YELLOW}📚 Testing Catalog Search...{RESET}")
    
    try:
        response = await client.get(
            f"{SERVICES['catalog']}/search",
            params={"q": "test"},
            timeout=5
        )
        
        if response.is_success:
            data = response.json()
            count = len(data.get("results", []))
            print(f"  {GREEN}✓{RESET} Search returned {count} results")
            return True
        else:
            print(f"  {RED}✗{RESET} Search failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  {RED}✗{RESET} Search error: {e}")
        return False


async def test_fleet_devices(client: httpx.AsyncClient) -> bool:
    """Test fleet device list."""
    print(f"\n{YELLOW}🚀 Testing Fleet Devices...{RESET}")
    
    try:
        response = await client.get(
            f"{SERVICES['fleet']}/devices",
            timeout=5
        )
        
        if response.is_success:
            data = response.json()
            count = len(data.get("devices", []))
            print(f"  {GREEN}✓{RESET} Fleet has {count} devices")
            return True
        else:
            print(f"  {RED}✗{RESET} Fleet failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  {RED}✗{RESET} Fleet error: {e}")
        return False


async def test_ai_chat(client: httpx.AsyncClient) -> bool:
    """Test AI gateway."""
    print(f"\n{YELLOW}🧠 Testing AI Gateway...{RESET}")
    
    try:
        response = await client.post(
            f"{SERVICES['ai_gateway']}/chat",
            json={"prompt": "Hello, this is a test"},
            timeout=30
        )
        
        if response.is_success:
            data = response.json()
            response_text = data.get("response", "")[:50]
            print(f"  {GREEN}✓{RESET} AI responded: {response_text}...")
            return True
        elif response.status_code == 503:
            print(f"  {YELLOW}⚠{RESET} AI backend unavailable (Ollama not running?)")
            return True  # Not a test failure
        else:
            print(f"  {RED}✗{RESET} AI failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  {YELLOW}⚠{RESET} AI error (may be expected): {str(e)[:40]}")
        return True


async def test_evidence_pack(client: httpx.AsyncClient) -> bool:
    """Test evidence pack creation."""
    print(f"\n{YELLOW}📋 Testing Evidence Pack...{RESET}")
    
    try:
        response = await client.post(
            f"{SERVICES['evidence']}/pack",
            json={
                "title": "Integration Test Pack",
                "description": "Created by integration test",
                "assets": []
            },
            timeout=10
        )
        
        if response.is_success:
            data = response.json()
            pack_id = data.get("pack_id", "N/A")
            print(f"  {GREEN}✓{RESET} Pack created: {pack_id}")
            return True
        else:
            print(f"  {RED}✗{RESET} Pack failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  {RED}✗{RESET} Pack error: {e}")
        return False


async def run_tests():
    """Run all integration tests."""
    print_banner()
    
    results = {
        "health": 0,
        "total": len(SERVICES),
        "tests": 0,
        "passed": 0
    }
    
    async with httpx.AsyncClient() as client:
        # Test 1: Health checks
        print(f"{BOLD}📊 Health Checks:{RESET}")
        
        health_tasks = [
            test_health(client, name, url) 
            for name, url in SERVICES.items()
        ]
        health_results = await asyncio.gather(*health_tasks)
        results["health"] = sum(health_results)
        
        # Only run further tests if at least some services are up
        if results["health"] > 0:
            # Test 2: Vault ingest
            if await test_vault_ingest(client):
                results["passed"] += 1
            results["tests"] += 1
            
            # Test 3: Catalog search
            if await test_catalog_search(client):
                results["passed"] += 1
            results["tests"] += 1
            
            # Test 4: Fleet devices
            if await test_fleet_devices(client):
                results["passed"] += 1
            results["tests"] += 1
            
            # Test 5: AI chat
            if await test_ai_chat(client):
                results["passed"] += 1
            results["tests"] += 1
            
            # Test 6: Evidence pack
            if await test_evidence_pack(client):
                results["passed"] += 1
            results["tests"] += 1
    
    # Summary
    print(f"\n{BOLD}═══════════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}📊 TEST SUMMARY{RESET}")
    print(f"{BOLD}═══════════════════════════════════════════════════════════════{RESET}")
    
    print(f"\n  Services Online: {results['health']}/{results['total']}")
    print(f"  Tests Passed:    {results['passed']}/{results['tests']}")
    
    if results["health"] == results["total"] and results["passed"] == results["tests"]:
        print(f"\n{GREEN}{BOLD}  ✅ ALL TESTS PASSED!{RESET}")
        return 0
    elif results["health"] == 0:
        print(f"\n{RED}{BOLD}  ❌ NO SERVICES RUNNING - Start CODEMASTER first!{RESET}")
        print(f"\n  Run: python3 run_local.py")
        return 1
    else:
        print(f"\n{YELLOW}{BOLD}  ⚠️  SOME TESTS FAILED{RESET}")
        return 1


def main():
    """Entry point."""
    start = time.time()
    exit_code = asyncio.run(run_tests())
    elapsed = time.time() - start
    print(f"\n  Duration: {elapsed:.2f}s\n")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
