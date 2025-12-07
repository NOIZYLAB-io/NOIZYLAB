def analyze_network(net: dict) -> dict:
    """
    Evaluates core network stability metrics.
    """

    if not net:
        return {"status": "no_data", "issue": "Network metrics missing."}

    latency = net.get("latency_ms", 0)
    jitter = net.get("jitter_ms", 0)
    loss = net.get("packet_loss_pct", 0)

    issues = []

    if latency >= 150:
        issues.append(f"High latency: {latency}ms")

    if jitter >= 30:
        issues.append(f"High jitter: {jitter}ms")

    if loss > 1:
        issues.append(f"Packet loss: {loss}%")

    if issues:
        return {
            "status": "warning",
            "issues": issues,
            "recommended_action": "Check router, cables, interference, or ISP."
        }

    return {"status": "healthy", "info": "Network stable"}
