#!/usr/bin/env python3
"""
Arms the mercenary escalation path (Claude) when anomalies arise.
"""
import argparse
import subprocess


def arm():
    print("🛡️ SENTRY: Mercenary escalation armed (stub).")
    # Placeholder: wire anomaly detection to call Claude via claude_bridge payload.


def main():
    parser = argparse.ArgumentParser(description="Sentry escalation trigger")
    parser.add_argument("--arm-mercenary", action="store_true", help="Arm the mercenary trigger")
    args = parser.parse_args()
    if args.arm_mercenary:
        arm()
    else:
        print("No action specified; use --arm-mercenary to arm.")


if __name__ == "__main__":
    main()
