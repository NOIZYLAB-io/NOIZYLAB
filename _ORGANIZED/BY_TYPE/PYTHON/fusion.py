def fuse_diagnostics(results: dict):
    warnings = [k for k, v in results.items() if v.get("status") == "warning"]

    return {
        "overall": "warning" if warnings else "healthy",
        "warnings": warnings,
        "modules": results
    }
